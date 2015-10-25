
# Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
        
"""Code Generated to build style:presentation-page-layout objects for odp files"""

import sys, os
from collections import OrderedDict

if sys.version_info < (3,):
    import odpslides.ElementTree_27OD as ET
else:
    import odpslides.ElementTree_34OD as ET
                


# Use func_quick_lookupD for access to function calls

func_quick_lookupD = {} # index=display name, value=function name
layout_name_lookupD = {}
display_name_lookupD = {}


def style_8_presentation_page_layout_Title_Slide():
    
    """Build Element style:presentation-page-layout for Title Slide """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title Slide")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.60764in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "8.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.75in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "2.32986in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "subtitle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.91667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "7in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "1.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.25in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title_and_Content():
    
    """Build Element style:presentation-page-layout for Title and Content """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title and Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL2")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Section_Header():
    
    """Build Element style:presentation-page-layout for Section Header """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Section Header")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL3")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.48958in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "8.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.78993in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.81944in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.64062in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "8.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.78993in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "3.17882in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Two_Content():
    
    """Build Element style:presentation-page-layout for Two Content """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Two Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL4")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Comparison():
    
    """Build Element style:presentation-page-layout for Comparison """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Comparison")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL5")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.69965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.4184in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.67882in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.32118in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.4184in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "2.37847in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.69965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.42014in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.07986in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.67882in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.32118in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.42014in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.07986in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "2.37847in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title_Only():
    
    """Build Element style:presentation-page-layout for Title Only """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title Only")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL6")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Blank():
    
    """Build Element style:presentation-page-layout for Blank """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Blank")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL7")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Content_with_Caption():
    
    """Build Element style:presentation-page-layout for Content with Caption """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Content with Caption")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL8")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.27083in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.28993in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.29861in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "6.40104in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "5.59028in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.90972in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.29861in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "5.13021in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.28993in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.56944in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Picture_with_Caption():
    
    """Build Element style:presentation-page-layout for Picture with Caption """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Picture with Caption")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL9")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.61979in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "6in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "1.96007in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "5.25in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "6in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "1.96007in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.67014in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.88021in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "6in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "1.96007in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "5.86979in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title_and_Vertical_Text():
    
    """Build Element style:presentation-page-layout for Title and Vertical Text """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title and Vertical Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL10")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Vertical_Title_and_Text():
    
    """Build Element style:presentation-page-layout for Vertical Title and Text """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Vertical Title and Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL11")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "6.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "6.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "6.58333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title_and_Text():
    
    """Build Element style:presentation-page-layout for Title and Text """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title and Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL12")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title_and_2_Column_Text():
    
    """Build Element style:presentation-page-layout for Title and 2-Column Text """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title and 2-Column Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL13")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title_and_Text_over_Content():
    
    """Build Element style:presentation-page-layout for Title and Text over Content """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title and Text over Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL14")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title__Text__and_Content():
    
    """Build Element style:presentation-page-layout for Title_ Text_ and Content """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title, Text, and Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL15")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title__Content_and_Text():
    
    """Build Element style:presentation-page-layout for Title_ Content and Text """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title, Content and Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL16")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title__Text__and_2_Content():
    
    """Build Element style:presentation-page-layout for Title_ Text_ and 2 Content """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title, Text, and 2 Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL17")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title__Content__and_2_Content():
    
    """Build Element style:presentation-page-layout for Title_ Content_ and 2 Content """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title, Content, and 2 Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL18")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title_and_Content_over_Text():
    
    """Build Element style:presentation-page-layout for Title and Content over Text """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title and Content over Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL19")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title_and_4_Content():
    
    """Build Element style:presentation-page-layout for Title and 4 Content """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title and 4 Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL20")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title__2_Content_and_Content():
    
    """Build Element style:presentation-page-layout for Title_ 2 Content and Content """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title, 2 Content and Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL21")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title__2_Content_and_Text():
    
    """Build Element style:presentation-page-layout for Title_ 2 Content and Text """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title, 2 Content and Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL22")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title_and_2_Content_over_Text():
    
    """Build Element style:presentation-page-layout for Title and 2 Content over Text """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title and 2 Content over Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL23")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_presentation_page_layout_Title_and_Table():
    
    """Build Element style:presentation-page-layout for Title and Table """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}presentation-page-layout" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}display-name", "Title and Table")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-PPL24")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "table")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}object", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    
    return elem

def style_8_default_style_graphic():
    
    """Build Element style:default-style for graphic """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}default-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "graphic")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "solid")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-color", "#4f81bd")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}opacity", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "solid")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}stroke-color", "#385d8a")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}stroke-opacity", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}stroke-width", "0.02778in")
    elem.append( child )
    
    
    return elem

def draw_8_gradient():
    
    """Build Element draw:gradient """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}gradient" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}angle", "0")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}end-color", "#85c2ff")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}end-intensity", "100%")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "a825")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}start-color", "#5e9eff")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}start-intensity", "100%")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style", "linear")
    
    
    return elem



# Set values in func_quick_lookupD
func_quick_lookupD[""] = draw_8_gradient
func_quick_lookupD["Blank"] = style_8_presentation_page_layout_Blank
func_quick_lookupD["Comparison"] = style_8_presentation_page_layout_Comparison
func_quick_lookupD["Content with Caption"] = style_8_presentation_page_layout_Content_with_Caption
func_quick_lookupD["Picture with Caption"] = style_8_presentation_page_layout_Picture_with_Caption
func_quick_lookupD["Section Header"] = style_8_presentation_page_layout_Section_Header
func_quick_lookupD["Title Only"] = style_8_presentation_page_layout_Title_Only
func_quick_lookupD["Title Slide"] = style_8_presentation_page_layout_Title_Slide
func_quick_lookupD["Title and 2 Content over Text"] = style_8_presentation_page_layout_Title_and_2_Content_over_Text
func_quick_lookupD["Title and 2-Column Text"] = style_8_presentation_page_layout_Title_and_2_Column_Text
func_quick_lookupD["Title and 4 Content"] = style_8_presentation_page_layout_Title_and_4_Content
func_quick_lookupD["Title and Content"] = style_8_presentation_page_layout_Title_and_Content
func_quick_lookupD["Title and Content over Text"] = style_8_presentation_page_layout_Title_and_Content_over_Text
func_quick_lookupD["Title and Table"] = style_8_presentation_page_layout_Title_and_Table
func_quick_lookupD["Title and Text"] = style_8_presentation_page_layout_Title_and_Text
func_quick_lookupD["Title and Text over Content"] = style_8_presentation_page_layout_Title_and_Text_over_Content
func_quick_lookupD["Title and Vertical Text"] = style_8_presentation_page_layout_Title_and_Vertical_Text
func_quick_lookupD["Title_ 2 Content and Content"] = style_8_presentation_page_layout_Title__2_Content_and_Content
func_quick_lookupD["Title_ 2 Content and Text"] = style_8_presentation_page_layout_Title__2_Content_and_Text
func_quick_lookupD["Title_ Content and Text"] = style_8_presentation_page_layout_Title__Content_and_Text
func_quick_lookupD["Title_ Content_ and 2 Content"] = style_8_presentation_page_layout_Title__Content__and_2_Content
func_quick_lookupD["Title_ Text_ and 2 Content"] = style_8_presentation_page_layout_Title__Text__and_2_Content
func_quick_lookupD["Title_ Text_ and Content"] = style_8_presentation_page_layout_Title__Text__and_Content
func_quick_lookupD["Two Content"] = style_8_presentation_page_layout_Two_Content
func_quick_lookupD["Vertical Title and Text"] = style_8_presentation_page_layout_Vertical_Title_and_Text
func_quick_lookupD["graphic"] = style_8_default_style_graphic




# Set values in layout_name_lookupD
layout_name_lookupD["Blank"] = "Master1-PPL7"
layout_name_lookupD["Comparison"] = "Master1-PPL5"
layout_name_lookupD["Content with Caption"] = "Master1-PPL8"
layout_name_lookupD["Picture with Caption"] = "Master1-PPL9"
layout_name_lookupD["Section Header"] = "Master1-PPL3"
layout_name_lookupD["Title Only"] = "Master1-PPL6"
layout_name_lookupD["Title Slide"] = "Master1-PPL1"
layout_name_lookupD["Title and 2 Content over Text"] = "Master1-PPL23"
layout_name_lookupD["Title and 2-Column Text"] = "Master1-PPL13"
layout_name_lookupD["Title and 4 Content"] = "Master1-PPL20"
layout_name_lookupD["Title and Content"] = "Master1-PPL2"
layout_name_lookupD["Title and Content over Text"] = "Master1-PPL19"
layout_name_lookupD["Title and Table"] = "Master1-PPL24"
layout_name_lookupD["Title and Text"] = "Master1-PPL12"
layout_name_lookupD["Title and Text over Content"] = "Master1-PPL14"
layout_name_lookupD["Title and Vertical Text"] = "Master1-PPL10"
layout_name_lookupD["Title, 2 Content and Content"] = "Master1-PPL21"
layout_name_lookupD["Title, 2 Content and Text"] = "Master1-PPL22"
layout_name_lookupD["Title, Content and Text"] = "Master1-PPL16"
layout_name_lookupD["Title, Content, and 2 Content"] = "Master1-PPL18"
layout_name_lookupD["Title, Text, and 2 Content"] = "Master1-PPL17"
layout_name_lookupD["Title, Text, and Content"] = "Master1-PPL15"
layout_name_lookupD["Two Content"] = "Master1-PPL4"
layout_name_lookupD["Vertical Title and Text"] = "Master1-PPL11"




# Set values in display_name_lookupD
display_name_lookupD["Master1-PPL1"] = "Title Slide"
display_name_lookupD["Master1-PPL10"] = "Title and Vertical Text"
display_name_lookupD["Master1-PPL11"] = "Vertical Title and Text"
display_name_lookupD["Master1-PPL12"] = "Title and Text"
display_name_lookupD["Master1-PPL13"] = "Title and 2-Column Text"
display_name_lookupD["Master1-PPL14"] = "Title and Text over Content"
display_name_lookupD["Master1-PPL15"] = "Title, Text, and Content"
display_name_lookupD["Master1-PPL16"] = "Title, Content and Text"
display_name_lookupD["Master1-PPL17"] = "Title, Text, and 2 Content"
display_name_lookupD["Master1-PPL18"] = "Title, Content, and 2 Content"
display_name_lookupD["Master1-PPL19"] = "Title and Content over Text"
display_name_lookupD["Master1-PPL2"] = "Title and Content"
display_name_lookupD["Master1-PPL20"] = "Title and 4 Content"
display_name_lookupD["Master1-PPL21"] = "Title, 2 Content and Content"
display_name_lookupD["Master1-PPL22"] = "Title, 2 Content and Text"
display_name_lookupD["Master1-PPL23"] = "Title and 2 Content over Text"
display_name_lookupD["Master1-PPL24"] = "Title and Table"
display_name_lookupD["Master1-PPL3"] = "Section Header"
display_name_lookupD["Master1-PPL4"] = "Two Content"
display_name_lookupD["Master1-PPL5"] = "Comparison"
display_name_lookupD["Master1-PPL6"] = "Title Only"
display_name_lookupD["Master1-PPL7"] = "Blank"
display_name_lookupD["Master1-PPL8"] = "Content with Caption"
display_name_lookupD["Master1-PPL9"] = "Picture with Caption"



if __name__ == "__main__":
    print( func_quick_lookupD["Title Only"]() )
