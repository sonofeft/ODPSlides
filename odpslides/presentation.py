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
from odpslides.odp_file import ODPFile, read_source_from_odp
from odpslides.styles_xml import StylesXML
from odpslides.content_xml import ContentXML
from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag
from odpslides.image_size import get_image_size


here = os.path.abspath(os.path.dirname(__file__))

#           right-arr  open-rt-arr  black-circ  bullet    open-circ   diamond  open-dmnd  arrow    open-arr    arr-circ   star
#BULLET_L = [u'\u25B6', u'\u2587',  u'\u25CF',  u'\u2022',u'\u25CE',u'\u25C6',u'\u25C7', u'\u27A1',u'\u27B1',u'\u27B2',u'\u2730']


class Presentation(object):
    """
    Creates OpenDocument Presentations for Microsoft PowerPoint, LibreOffice and OpenOffice.
    Output is a *.odp file.
    """

    def __init__(self, title='My Title', author='My Name', 
        background_image="", background_color="white",
        grad_start_color="", grad_end_color="", grad_angle_deg=0, grad_draw_style='linear',
        show_date=False, date_font_color='gray',
        footer="", footer_font_color='gray',
        show_page_number=False, page_number_font_color="gray"):
            
        """
        Make Presentation object
        """        


        self.filename = None
        
        # keep a list of images for inclusion in ODP file
        self.image_nameD = {}     # index=file system name,    value=internal image name
        self.sys_image_nameD = {} # index=internal image name, value=file system name
        self.image_nameL = [] # ordered list of internal image names 
        self.image_sizeD = {} # index=internal image name, value=tuple of image size (w,h)
        self.max_image_int = 0
        
        self.background_image = background_image
        if self.background_image:
            self.internal_background_image = self.get_next_image_name( background_image )
        else:
            self.internal_background_image = ''
        
        self.background_color = getValidHexStr( background_color, "#ffffff" ) # default to white
        
        
        self.grad_start_color = grad_start_color
        self.grad_end_color = grad_end_color
        self.grad_angle = '%s'%(int(grad_angle_deg)*10, ) # odp understands tenths of deg input
        self.grad_draw_style = grad_draw_style
        
        if self.internal_background_image:
            self.ref_odp_filename = 'ppt_all_layouts_image.odp'
            self.page_type = 'image' # "solidbg", "grad", "image"
        elif self.grad_start_color and self.grad_end_color:
            self.ref_odp_filename = 'ppt_all_layouts_grad.odp'
            self.page_type = 'grad' # "solidbg", "grad", "image"
        else:
            self.ref_odp_filename = 'ppt_all_layouts_solidbg.odp'
            self.page_type = 'solidbg' # "solidbg", "grad", "image"
                
        # open reference odp file
        self.full_odp_ref_path = os.path.join( here, 'templates', self.ref_odp_filename )
        self.odp_ref = ODPFile( self.full_odp_ref_path )
        
        self.styles_xml_obj = StylesXML( self, self.odp_ref )
        self.content_xml_obj = ContentXML(self, self.odp_ref )
        
        
        # figure out max style:name (e.g. "a123")
        self.odp_ref.styles_xml_obj.init_all_annn_style8name()
                
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
        #self.new_master_styleD = {} # index="a123", value=style elem

        # style names and id values start at 0 (i.e. "a0", "a1", ... and "id0", "id1", ...)
        #self.max_style_name_int = -1 # used for nameing styles (ex. draw:style-name="a123")
        #self.max_draw_id_int = -1 # some internal use ???
        self.max_style_name_int = self.odp_ref.styles_xml_obj.max_annn_def + 1000
        self.max_draw_id_int = self.odp_ref.styles_xml_obj.max_idnnn_def + 1000
        


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
            
        if not os.path.isfile( file_sys_name ):
            print('...WARNING... image file: "%s" NOT FOUND'%file_sys_name)
            file_sys_name = os.path.join(here, 'templates', 'no_image_found.png')
        
        head, tail = os.path.splitext( file_sys_name ) # tail is usually ".png"
        
        self.max_image_int += 1
        int_name = 'image%i%s'%(self.max_image_int, tail)
        
        self.image_nameD[ file_sys_name ] = int_name
        self.sys_image_nameD[ int_name ] = file_sys_name
        self.image_nameL.append( int_name )
        
        self.image_sizeD[ int_name ] = get_image_size( file_sys_name )
        
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
    

    def save(self, filename='my_presentation.odp', launch=False):
        """
        Saves Presentation to an odp file readable by Microsoft PowerPoint, LibreOffice or OpenOffice.

        If the launch flag is set, will launch PowerPoint, LibreOffice or Openoffice using "os.startfile"
        or "open" or "xdg-open" depending on the platform.

        :keyword filename: Name of ods file to save (default=='my_presentation.odp')
        :type  filename: str or unicode
        :keyword bool launch: If True, will launch PowerPoint, LibreOffice or OpenOffice (default==False)
        
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
        
        # just duplicate reference file's styles.xml
        self.styles_xml_obj.make_clean_copy()
        self.styles_xml_obj.set_background()

        #self.set_bullets( self.styles_xml_obj.styles_tmplt.root )
        styles_xml_str = self.styles_xml_obj.styles_tmplt.tostring().decode('utf-8')
        styles_xml_str = styles_xml_str.replace(' xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0"','')
        styles_xml_str = styles_xml_str.replace( '<number:date-style ', '<number:date-style xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" ' )
        zipfile_insert( zipfileobj, 'styles.xml',  styles_xml_str.encode('utf-8'))

        # Gets new empty content with each save
        content_tmplt = self.content_xml_obj.content_tmplt # make a shorter var name for content_tmplt
        #content_tmplt = init_internal_odp_files.get_empty_content_elem()
        auto_style_elem = content_tmplt.find('office:automatic-styles')
        body_pres_elem = content_tmplt.find('office:body/office:presentation')
        
        for style_elem in self.new_content_styleL:
            content_tmplt.acclimate_new_elem( style_elem )
            auto_style_elem.append( style_elem )
        for page in self.new_content_pageL:
            content_tmplt.acclimate_new_elem( page.draw_page )
            body_pres_elem.append( page.draw_page )
            
        last_body_elem = init_internal_odp_files.get_final_presentation_elem()
        content_tmplt.acclimate_new_elem( last_body_elem )
        body_pres_elem.append( last_body_elem )
        
        self.content_xml_obj.set_background()
        self.set_bullets( content_tmplt.root )
        content_xml_str = content_tmplt.tostring().decode('utf-8')
        
        # <<<<<<<<<<<<<<<< Add new content objects here ===================
        zipfile_insert( zipfileobj, 'content.xml', content_xml_str.encode('utf-8'))
        
        zipfile_insert( zipfileobj, 'settings.xml', init_internal_odp_files.get_settings_xml_str() )

        
        zipfileobj.close()

        if launch:
            self.launch_application()
 
    def set_bullets(self, top_elem ):
        """
        I can't seem to find where my unicode bullet chars are getting messed up.
        For now, set all bullets to the bullet character.
        """
        
        bull_tag = force_to_tag( 'text:list-level-style-bullet' )
        for elem in top_elem.iter():
            if elem.tag == bull_tag:
                level = elem.get(force_to_tag('text:level'),'')
                if level:
                    i = int( level )
                    bchar = u'\u2022' # BULLET_L[ i-1 ]  # u'\u25CF'
                    elem.set(force_to_tag('text:bullet-char'), bchar)
                    #print(bchar, end='')
        
        

    def add_a_new_page(self, new_page ):
        
        self.new_content_pageL.append( new_page )
        new_page.set_page_number( len(self.new_content_pageL) )
        

    def add_title_chart( self, title='My Title', subtitle='My Subtitle', title_font_color='',
                            subtitle_font_color='',background_color=""):
        
        # <<<<==== Temporarily leave background color... does nothing for now, may delete later
        if background_color:
            background_color = getValidHexStr( background_color, "#ffffff" ) # default to white
        else:
            background_color = self.background_color
        
        inpD = {'title':title, 'subtitle':subtitle, 'background_color':background_color,
                'title_font_color':title_font_color, 'subtitle_font_color':subtitle_font_color}
                    
        new_page = Page( self, disp_name="Title Slide", **inpD)
        self.add_a_new_page( new_page )
        
    def add_titled_outline_chart(self, title='My Title', outline='', title_font_color='',
                                     text_font_color='', 
                                     pcent_stretch_center=0, pcent_stretch_content=0):
                                         
        
        inpD = {'title':title,  'outline':outline,
                'title_font_color':title_font_color, 'text_font_color':text_font_color,
                'pcent_stretch_center':pcent_stretch_center, 
                'pcent_stretch_content':pcent_stretch_content}
                    
        new_page = Page( self, disp_name="Title and Text", **inpD)
        self.add_a_new_page( new_page )
        
    def add_titled_image(self, title='My Picture', image_file='', title_font_color='', 
                            keep_aspect_ratio=True, 
                            pcent_stretch_center=0, pcent_stretch_content=0):
        
        image_name = self.get_next_image_name( image_file )
        inpD = {'title':title,  'image_name':image_name, 'title_font_color':title_font_color,
                'keep_aspect_ratio':keep_aspect_ratio,
                'pcent_stretch_center':pcent_stretch_center, 
                    'pcent_stretch_content':pcent_stretch_content}
                        
        new_page = Page( self, disp_name="Title and Content", **inpD)
        self.add_a_new_page( new_page )
 
if __name__ == '__main__':
    
    C = Presentation(title='My Title', author='My Name',
        #background_image=r'D:\py_proj_2015\ODPSlides\odpslides\templates\image1.png',
        background_color='#ccffcc',
        #grad_start_color='ff0000', grad_end_color="#ffffff", grad_angle_deg=45, grad_draw_style='linear',
        show_date=True, date_font_color='lime',
        footer="testing 123", footer_font_color='lime',
        show_page_number=True, page_number_font_color='dm')
    
    C.add_title_chart( title='My Title', subtitle='My Subtitle', title_font_color='red',
                        subtitle_font_color='red')
    
    sL = ['1st','\t2nd','\t\t3rd','            4th','Normal < 1st but > 9','    Indent 2nd']
    C.add_titled_outline_chart( title='My Second Title', outline=sL, 
                                title_font_color='blue', text_font_color='green',
                                pcent_stretch_center=80, pcent_stretch_content=80)
    
    C.add_titled_image( title='Tall Aspect Ratio', image_file='./templates/planets.jpg', 
                        title_font_color='dr', keep_aspect_ratio=True,
                        pcent_stretch_center=80, pcent_stretch_content=80)
    C.add_titled_image( title='My 2nd Picture', image_file='./templates/sysMass_vs_vol_Ptank.png', 
                        title_font_color='g')
    C.add_titled_image( title='My Third Picture', image_file='./templates/Pressure_1T_Spin.gif')
    
    C.save( filename='my_ppt.odp', launch=1 )
    
 
 