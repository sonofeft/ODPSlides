# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function


r"""
Creates OpenDocument Presentations for Microsoft PowerPoint, LibreOffice and OpenOffice

<Paragraph description see docstrings at http://www.python.org/dev/peps/pep-0257/>
ODPSlides will create odp files readable by Microsoft Excel, LibreOffice or OpenOffice.

The format is a very narrow subset of full presentation support::
    #. Slides are one of the following
        - A slide with text
        - A slide with a central image and text box
        - A slide with drawing objects

There is no attempt to supply a full API interface.



ODPSlides
Copyright (C) 2015  Charlie Taylor

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

-----------------------

"""
import os
import sys
import zipfile
import time
from copy import deepcopy
import datetime

from odpslides.template_xml_file import TemplateXML_File
from odpslides.find_obj import find_elem_w_attrib, NS_attrib, NS

from odpslides.master_styles import init_master_styles, get_next_a_style
from odpslides.content import add_title_chart, add_title_text_chart

here = os.path.abspath(os.path.dirname(__file__))

# for multi-file projects see LICENSE file for authorship info
# for single file projects, insert following information
__author__ = 'Charlie Taylor'
__copyright__ = 'Copyright (c) 2015 Charlie Taylor'
__license__ = 'GPL-3'
exec( open(os.path.join( here,'_version.py' )).read() )  # creates local __version__ variable
__email__ = "cet@appliedpython.com"
__status__ = "3 - Alpha" # "3 - Alpha", "4 - Beta", "5 - Production/Stable"

#
# import statements here. (built-in first, then 3rd party, then yours)
#
# Code goes below.
# Adjust docstrings to suite your taste/requirements.
#

def load_template_xml_from_odp(ods_fname, fname, subdir='' ):

    full_ods_path = os.path.join( here, 'templates', ods_fname )

    if subdir:
        inner_fname = subdir + '/' + fname
    else:
        inner_fname =  fname

    odsfile = zipfile.ZipFile( full_ods_path )
    src = odsfile.read( inner_fname ).decode('utf-8')
        

    return TemplateXML_File( src )


def zipfile_insert( zipfileobj, filename, data):
    """Create a file named filename, in the zip archive.
       "data" is the UTF-8 string that is placed into filename.

       (Not called by User)
    """

    # zip seems to struggle with non-ascii characters
    #data = data.encode('utf-8')

    now = time.localtime(time.time())[:6]
    info = zipfile.ZipInfo(filename)
    info.date_time = now
    info.compress_type = zipfile.ZIP_DEFLATED
    zipfileobj.writestr(info, data)

def clear_children( parent ):
    parent.clear_children()

class BadNewStyleError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)

class Presentation(object):
    """
    Creates OpenDocument Presentations for Microsoft PowerPoint, LibreOffice and OpenOffice.
    Output is a *.odp file.
    """

    def __init__(self, title='My Title', author='My Name', 
        template_name="plain", 
        show_date=False, date_font_color='gray',
        footer="",
        show_page_number=False):
            
        """
        Inits Presentation with filename and blank content.
        
        :keyword str title: Main title on presentation title page (default=='My Title')
        :type  title: str or unicode
        :keyword str author: Name of Author, put on main title page (default=='My Name')
        :type  author: str or unicode

        :keyword str template_name: Name of presentation template 
            (can be "plain", "grad", "gray")  (default=="plain")
            
        :keyword bool show_date: Flag to show current date or date_text string (default==False)
        :type  show_date: bool
        :keyword None date_font_color:  (default=="gray")
        :type  date_font_color: str or unicode
        
        :keyword str footer: Text put at bottom of every page (default=="")
        :type  footer: str or unicode
                
        :keyword bool show_page_number: Flag to show page numbers or not (default==False)
        :type  show_page_number: bool
        
        :return: None
        :rtype: None
        
        """
        
        self.filename = None
        self.template_name = template_name
        self.template_fname = 'ppt_all_layouts_%s.odp'%template_name.lower()
                
        self.show_date = show_date
        self.date_font_color = date_font_color
        
        self.footer = footer
        self.show_page_number = show_page_number
        
        self.slideL = [] # list of slide pages content
        
        # ................. Need to do some prep work with content_xml_obj ...............
        # Get ref auto_styles and presentation sections for document
        self.content_xml_obj = load_template_xml_from_odp( self.template_fname, 'content.xml' )
        
        # Need styles info as part of prep work
        self.styles_xml_obj = load_template_xml_from_odp( self.template_fname, 'styles.xml' )
        
        init_master_styles( self )
        
        # Get ref auto_styles sections for document
        self.auto_styles = self.content_xml_obj.find('office:automatic-styles')
        print('auto_styles =', self.auto_styles)
        self.body_presentation = self.content_xml_obj.find('office:body/office:presentation')
        print('presentation =', self.body_presentation)
        
        
        #self.ref_auto_styles = deepcopy( self.auto_styles )
        self.new_styleL = [] # style:style elements to be added to auto_styles
        clear_children( self.auto_styles ) # <== add new_styleL when saveing
        
        # Get ref presentation sections for document
        #self.ref_presentation = deepcopy( self.body_presentation )
        self.new_draw_pageL = [] # draw:page elements to be added to presentation
        clear_children( self.body_presentation ) # <== add new_draw_pageL when saving
        # ............... end of content_xml_obj prep work .......................
        
        self.meta_xml_obj = load_template_xml_from_odp( self.template_fname, 'meta.xml' )
        self.settings_xml_obj = load_template_xml_from_odp( self.template_fname, 'settings.xml' )
        
        
        self.mimetype_str = 'application/vnd.oasis.opendocument.presentation'
        
        # Need to fix attribute xmlns:number in all the date-style entries... An error in ElementTree
        #dateStyleL = find_elem_w_attrib('office:automatic-styles/number:date-style', self.styles_xml_obj, self.styles_xml_obj.rev_nsOD, return_list=True)
        #print('dateStyleL =',dateStyleL )
        #for elem, ielem in dateStyleL:
        #    #elem.set(NS('xmlns:number', self.styles_xml_obj.rev_nsOD), "urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0")
        #    print( elem.tag)

        self.metainf_manifest_xml_obj = load_template_xml_from_odp(self.template_fname, 'manifest.xml', subdir='META-INF')

        self.meta_creation_date_obj = self.meta_xml_obj.find('office:meta/meta:creation-date')
        self.meta_dc_date_obj = self.meta_xml_obj.find('office:meta/dc:date')

        self.meta_init_creator_obj = self.meta_xml_obj.find('office:meta/meta:initial-creator')
        self.meta_dc_creator_obj = self.meta_xml_obj.find('office:meta/dc:creator')
        

    def meta_time(self):
        "Return time string in meta data format"
        t = time.localtime()
        stamp = "%04d-%02d-%02dT%02d:%02d:%02d" % (t[0], t[1], t[2], t[3], t[4], t[5])
        return stamp

    def add_new_a_style(self, style_elem):
        """
        get new style:name for style_elem and add it to self.new_styleL as well
        as self.style_name_elem_from_nameD
        """
        
        new_a_val = get_next_a_style()
        style_elem.set( '{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name', new_a_val )
        self.new_styleL.append( style_elem )
        self.style_name_elem_from_nameD[new_a_val] = style_elem
        
        if style_elem is None:
            raise BadNewStyleError('None for new style')
            
        return new_a_val
        

    # make sure any added Element objects are in nsOD, rev_nsOD and qnameOD of parent_obj
    def add_tag(self, tag, parent_obj ):
        sL = tag.split('}')
        uri = sL[0][1:]
        name = sL[1]

        parent_obj.qnameOD[tag] = parent_obj.nsOD[uri] + ':' + name


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

        self.meta_creation_date_obj.text = self.meta_time()
        self.meta_dc_date_obj.text = self.meta_time()
        self.meta_init_creator_obj.text = 'ODPSlides'
        self.meta_dc_creator_obj.text = 'ODPSlides'


        zipfile_insert( zipfileobj, 'meta.xml', self.meta_xml_obj.tostring())

        zipfile_insert( zipfileobj, 'mimetype', self.mimetype_str.encode('UTF-8'))

        zipfile_insert( zipfileobj, 'META-INF/manifest.xml', self.metainf_manifest_xml_obj.tostring())
        
        # put ODPSlides thumbnail into archive
        full_png_path = os.path.join( here, 'templates', 'thumbnail.png' )
        zipfileobj.write( full_png_path, 'Thumbnails/thumbnail.png')

        if self.template_name == 'gray':
            full_png_path = os.path.join( here, 'templates', 'image1.png' )
            zipfileobj.write( full_png_path, 'media/image1.png')

        #  ========== content.xml ===================
        # Rebuild content_xml_obj for each save
        clear_children( self.auto_styles ) # <== add new_styleL when saveing
        clear_children( self.body_presentation ) # <== add new_draw_pageL when saving
        
        for new_page in self.slideL:
            self.body_presentation.append( new_page )

        for new_style in self.new_styleL:# style:style elements to be added to auto_styles
            self.auto_styles.append( new_style )
            
        for new_draw_page in self.new_draw_pageL:# draw:page elements to be added to presentation
            self.body_presentation.append( new_draw_page )

        zipfile_insert( zipfileobj, 'content.xml', self.content_xml_obj.tostring())
        
        zipfile_insert( zipfileobj, 'settings.xml', self.settings_xml_obj.tostring())

        #zipfile_insert( zipfileobj, 'styles.xml', self.styles_xml_obj.tostring())
        style_xml_src = self.styles_xml_obj.tostring().decode('utf-8')
        #style_xml_src = style_xml_src.replace(' xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0"','', 1)
        style_xml_src = style_xml_src.replace('<number:date-style ','<number:date-style xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" ')
        zipfile_insert( zipfileobj, 'styles.xml', style_xml_src.encode('utf-8'))
        

        zipfileobj.close()

        if launch:
            self.launch_application()

    def add_title_chart( self, title='My Title', subtitle='My Subtitle', title_font_color=None,
                            subtitle_font_color=None):
        add_title_chart( self, title=title, subtitle=subtitle, title_font_color=title_font_color,
                         subtitle_font_color=subtitle_font_color)
        
    def add_title_text_chart( self, title='My Title', title_font_color=None,
                             outline='A long drawn-out piece of text\rWith multiple lines.',
                             outline_font_color=None):
        add_title_text_chart(self, title=title, outline=outline, title_font_color=title_font_color,
                             outline_font_color=outline_font_color)

if __name__ == '__main__':
    C = Presentation(title='My Title', author='My Name',
        template_name="plain", 
        show_date=True, date_font_color='coral',
        footer="",
        show_page_number=False)
        
    C.add_title_chart( title='My Title', subtitle='My Subtitle', title_font_color="darkmagenta",
                        subtitle_font_color="darkcyan")
    
    sL = ['1st','\t2nd','\t\t3rd','            4th','Normal < 1st but > 9','    Indent 2nd']
    C.add_title_text_chart( title='My Outline Title', outline=sL, title_font_color="darkgreen",
                            outline_font_color="darkblue")
    
    C.save( filename='my_ppt', launch=1)
    
