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

from odpslides.template_xml_file import TemplateXML_File
from odpslides.find_obj import find_elem_w_attrib, NS_attrib, NS

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


class Presentation(object):
    """
    Creates OpenDocument Presentations for Microsoft PowerPoint, LibreOffice and OpenOffice.
    Output is a *.odp file.
    """

    def __init__(self, title='My Title', author='My Name', dated=None,
        template_name="plain"):
        """
        Inits Presentation with filename and blank content.
        
        :keyword str title: Main title on presentation title page (default=='My Title')
        :type  title: str or unicode
        :keyword str author: Name of Author, put on main title page (default=='My Name')
        :type  author: str or unicode
        :keyword None dated: Date put on main title page (if blank then today) (default==None)
        :type  dated: str, unicode or None

        :keyword str template_name: Name of presentation template 
            (can be "plain", "blue", "gray")  (default=="plain")
        
        :return: None
        :rtype: None
        
        """
        
        self.filename = None
        self.template_name = template_name
        self.template_fname = 'ppt_%s.odp'%template_name.lower()
        self.slideL = [] # list of slide pages content
        

        self.content_xml_obj = load_template_xml_from_odp( self.template_fname, 'content.xml' )
        self.meta_xml_obj = load_template_xml_from_odp( self.template_fname, 'meta.xml' )
        self.settings_xml_obj = load_template_xml_from_odp( self.template_fname, 'settings.xml' )
        
        
        self.mimetype_str = 'application/vnd.oasis.opendocument.presentation'
        self.styles_xml_obj = load_template_xml_from_odp( self.template_fname, 'styles.xml' )
        
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



if __name__ == '__main__':
    C = Presentation(title='My Title', author='My Name', dated=None,
        template_name="gray")
        
    C.save( filename='my_ppt', launch=False)
