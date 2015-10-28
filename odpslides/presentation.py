# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function

import os
import subprocess
import sys
import zipfile
import time
import datetime

from odpslides.zip_file import zipfile_insert
import odpslides.init_internal_odp_files as init_internal_odp_files
from odpslides.page import Page
from odpslides.color_utils import getValidHexStr

import plain.page_layouts


here = os.path.abspath(os.path.dirname(__file__))


class Presentation(object):
    """
    Creates OpenDocument Presentations for Microsoft PowerPoint, LibreOffice and OpenOffice.
    Output is a *.odp file.
    """

    def __init__(self, title='My Title', author='My Name', 
        background_image="", background_color="white",
        grad_start_color="", grad_end_color="", grad_angle=0, grad_draw_style='linear',
        show_date=False, date_font_color='gray',
        footer="", footer_font_color='gray',
        show_page_number=False, page_number_font_color="gray", include_styles_xml=False, for_excel=True):
            
        """
        :keyword bool include_styles_xml: If True, include style info in styles.xml (Required by Excel, not by OO)
        """        


        self.filename = None
        self.include_styles_xml = include_styles_xml # Excel needs styles.xml style:master-page elements
        self.for_excel = for_excel
        
        # keep a list of images for inclusion in ODP file
        self.image_nameD = {}     # index=file system name,    value=internal image name
        self.sys_image_nameD = {} # index=internal image name, value=file system name
        self.image_nameL = [] # ordered list of internal image names 
        self.max_image_int = 0
        
        self.background_image = background_image
        if self.background_image:
            self.internal_background_image = self.get_next_image_name( background_image )
        else:
            self.internal_background_image = ''
        
        self.background_color = getValidHexStr( background_color, "#ffffff" ) # default to white
        
        
        self.grad_start_color = grad_start_color
        self.grad_end_color = grad_end_color
        self.grad_angle = grad_angle
        self.grad_draw_style = grad_draw_style
                
        self.show_date = show_date
        self.date_font_color = date_font_color
        
        self.footer = footer
        self.footer_font_color = footer_font_color
        
        self.show_page_number = show_page_number
        self.page_number_font_color = page_number_font_color
        
        # style names will be in order, "a0", "a1", "a2", ...
        self.new_content_styleL = [] # style:style elements to be added to auto_styles
        self.new_content_pageL = [] # draw:page elements to be added to presentation
        self.new_master_styleL = [] # For each new_content_pageL item, there are many master-page style elements
        self.new_master_page_styleL = [] # For each new_content_pageL item, there is a style:master-page item
        
        self.new_styles_office_stylesL = [] # usually draw:gradient or draw:fill-image statements

        self.new_content_styleD = {} # index="a123", value=style elem
        self.new_master_styleD = {} # index="a123", value=style elem

        # style names and id values start at 0 (i.e. "a0", "a1", ... and "id0", "id1", ...)
        self.max_style_name_int = -1 # used for nameing styles (ex. draw:style-name="a123")
        self.max_draw_id_int = -1 # some internal use ???
        


    def get_next_a_style(self):
        """Returns a string like "a123"  """
        self.max_style_name_int += 1
        return 'a%i'%self.max_style_name_int
        
    def get_next_draw_id(self):
        """Returns a string like "id123"  """
        self.max_draw_id_int += 1
        return 'id%i'%self.max_draw_id_int
        
    def get_next_image_name(self, file_sys_name):
        """Returns a string like "image1", "image2", ...  """
        
        if file_sys_name in self.image_nameD:
            return self.image_nameD[ file_sys_name ]
        
        head, tail = os.path.splitext( file_sys_name ) # tail is usually ".png"
        
        self.max_image_int += 1
        int_name = 'image%i%s'%(self.max_image_int, tail)
        
        self.image_nameD[ file_sys_name ] = int_name
        self.sys_image_nameD[ int_name ] = file_sys_name
        self.image_nameL.append( int_name )
        
        return int_name
            

    def launch_application(self):
        """
        Will launch PowerPoint, LibreOffice or Openoffice using "os.startfile" or "open" or
        "xdg-open" depending on the platform.

        ONLY WORKS IF file has been saved.
        """

        if self.filename is None:
            print( '='*75 )
            print( '='*5, 'MUST SAVE FILE before launch_application will work.' , '='*5)
            print( '='*75 )
            return

        #os.startfile( self.filename )
        if sys.platform == "win32":
            os.startfile(self.filename)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, self.filename])

    def add_office_styles(self, style_elem):
        """
        Put draw:gradient and draw:image-fill into styles.xml 
        """
        
        office_styles = style_elem.find( 'office:styles' )
        for elem in self.new_styles_office_stylesL:
            style_elem.acclimate_new_elem( elem )
            office_styles.append( elem )

    def add_page_layouts(self, style_elem):
        """
        Put used layouts into styles.xml 
        """
        office_styles = style_elem.find( 'office:styles' )
        #print('office_styles =',office_styles)
        
        layout_set = set() # Only put one copy of layout into styles.xml
        for page in self.new_content_pageL:
            layout_set.add( page.disp_name )
            
        for disp_name in layout_set:
            lay_elem = plain.page_layouts.func_quick_lookupD[ disp_name ]()
            style_elem.acclimate_new_elem( lay_elem )
            office_styles.append( lay_elem )

    def add_style_master_page(self, style_elem ):
        office_auto_styles = style_elem.find( 'office:master-styles' )
        #print('office_auto_styles =',office_auto_styles)
        
        # For each new_content_pageL item, there are many master-page style elements
        for master_elem in self.new_master_styleL:
            office_auto_styles.append( master_elem )
            style_elem.acclimate_new_elem( master_elem )
        
        # For each new_content_pageL item, there is a style:master-page item
        for master_page_elem in self.new_master_page_styleL:
            office_auto_styles.append( master_page_elem )
            style_elem.acclimate_new_elem( master_page_elem )
    

    def save(self, filename='my_presentation.odp', launch=False):
        """
        Saves Presentation to an odp file readable by Microsoft PowerPoint, LibreOffice or OpenOffice.

        If the launch flag is set, will launch PowerPoint, LibreOffice or Openoffice using "os.startfile"
        or "open" or "xdg-open" depending on the platform.

        :keyword filename: Name of ods file to save (default=='my_presentation.odp')
        :type  filename: str or unicode
        :keyword bool launch: If True, will launch PowerPoint, LibreOffice or OpenOffice (default==False)
        :keyword bool include_styles_xml: If True, include style info in styles.xml (Required by Excel, not by OO)
        
        :return: None
        :rtype: None
        """        
       
        if not filename.lower().endswith('.odp'):
            filename = filename + '.odp'

        print('Saving odp file: %s'%filename)
        self.filename = filename

        zipfileobj = zipfile.ZipFile(filename, "w")

        zipfile_insert( zipfileobj, 'meta.xml', init_internal_odp_files.get_meta_xml_str() )

        zipfile_insert( zipfileobj, 'mimetype', init_internal_odp_files.get_mimetype_str())

        manifest_elem = init_internal_odp_files.get_manifest_elem()
        zipfile_insert( zipfileobj, 'META-INF/manifest.xml', manifest_elem)
        
        # put ODPSlides thumbnail into archive
        full_png_path = os.path.join( here, 'templates', 'thumbnail.png' )
        zipfileobj.write( full_png_path, 'Thumbnails/thumbnail.png')

        if self.image_nameL:
            for img_name in self.image_nameL:
                zipfileobj.write( self.sys_image_nameD[ img_name ], 'media/%s'%img_name)

        # Gets new empty content with each save
        content_elem = init_internal_odp_files.get_empty_content_elem()
        auto_style_elem = content_elem.find('office:automatic-styles')
        body_pres_elem = content_elem.find('office:body/office:presentation')
        
        for style_elem in self.new_content_styleL:
            content_elem.acclimate_new_elem( style_elem )
            auto_style_elem.append( style_elem )
        for page in self.new_content_pageL:
            content_elem.acclimate_new_elem( page.draw_page )
            body_pres_elem.append( page.draw_page )
            
        last_body_elem = init_internal_odp_files.get_final_presentation_elem()
        content_elem.acclimate_new_elem( last_body_elem )
        body_pres_elem.append( last_body_elem )
        
        # <<<<<<<<<<<<<<<< Add new content objects here ===================
        zipfile_insert( zipfileobj, 'content.xml', content_elem)
        
        zipfile_insert( zipfileobj, 'settings.xml', init_internal_odp_files.get_settings_xml_str() )

        style_elem = init_internal_odp_files.get_empty_styles_elem()
        if self.include_styles_xml:
            self.add_page_layouts( style_elem )
            self.add_style_master_page( style_elem )
            
        self.add_office_styles( style_elem )
        
        # <<<<<<<<<<<<<<<< Add new content objects here ===================
        # Need to fix local namespace in subelement
        style_xml_src = style_elem.tostring().decode('utf-8')
        style_xml_src = style_xml_src.replace('<number:date-style ','<number:date-style xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" ')
        zipfile_insert( zipfileobj, 'styles.xml', style_xml_src.encode('utf-8'))
        
        zipfileobj.close()

        if launch:
            self.launch_application()
 

    def add_title_chart( self, title='My Title', subtitle='My Subtitle', title_font_color='',
                            subtitle_font_color='',background_color=""):
        
        if background_color:
            background_color = getValidHexStr( background_color, "#ffffff" ) # default to white
        else:
            background_color = self.background_color
        
        inpD = {'title':'My Title', 'subtitle':'My Subtitle', 'background_color':background_color,
                'title_font_color':title_font_color, 'subtitle_font_color':subtitle_font_color}
                    
        new_page = Page( self, disp_name="Title Slide", **inpD)
        
        self.new_content_pageL.append( new_page )
 
if __name__ == '__main__':
    
    C = Presentation(title='My Title', author='My Name',
        #background_image=r'D:\py_proj_2015\ODPSlides\odpslides\templates\image1.png',
        background_color='#CCCCFF',
        #grad_start_color="#99ff99", grad_end_color="#ffffff", grad_angle=0, grad_draw_style='linear',
        show_date=True, date_font_color='coral',
        footer="testing 123", footer_font_color='lime',
        show_page_number=True, page_number_font_color='dm', include_styles_xml=True, for_excel=True)
    
    C.add_title_chart( title='My Title', subtitle='My Subtitle', title_font_color='red',
                        subtitle_font_color='red')
    
    #C.new_content_pageL[-1].set_to_gradient(grad_start_color="#99ff99", grad_end_color="#ffffff", 
    #                                         grad_angle=0, grad_draw_style='linear' )
    
    C.save( filename='my_ppt.odp', launch=1 )
    
 
 