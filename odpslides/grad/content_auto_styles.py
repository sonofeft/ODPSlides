
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

func_quick_lookupD = {} # index=suffix name, value=function name


# Use content_style_name_lookupD for access to function calls

content_style_name_lookupD = {} # index=style name (e.g. "a123"), value=function name


def style_8_style_presentation_a1239():
    
    """Build Element style:style for presentation_a1239 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1239")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1288():
    
    """Build Element style:style for presentation_a1288 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1288")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "top")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1300():
    
    """Build Element style:style for drawing-page_a1300 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1300")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1299")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1301():
    
    """Build Element style:style for text_a1301 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1301")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1302():
    
    """Build Element style:style for text_a1302 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1302")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1303():
    
    """Build Element style:style for paragraph_a1303 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1303")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1304():
    
    """Build Element style:style for presentation_a1304 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1304")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1305():
    
    """Build Element style:style for presentation_a1305 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1305")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1306():
    
    """Build Element style:style for presentation_a1306 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1306")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1307():
    
    """Build Element style:style for presentation_a1307 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1307")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1170():
    
    """Build Element style:style for text_a1170 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1170")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1309():
    
    """Build Element style:style for drawing-page_a1309 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1309")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1308")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1171():
    
    """Build Element style:style for paragraph_a1171 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1171")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1172():
    
    """Build Element style:style for presentation_a1172 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1172")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1173():
    
    """Build Element style:style for text_a1173 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1173")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1174():
    
    """Build Element style:style for paragraph_a1174 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1174")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.375in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.09722in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.375in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1176():
    
    """Build Element style:style for text_a1176 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1176")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1177():
    
    """Build Element style:style for text_a1177 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1177")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1178():
    
    """Build Element style:style for paragraph_a1178 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1178")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.8125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.3125in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1240():
    
    """Build Element style:style for presentation_a1240 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1240")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1241():
    
    """Build Element style:style for text_a1241 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1241")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1290():
    
    """Build Element style:style for drawing-page_a1290 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1290")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1289")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1242():
    
    """Build Element style:style for paragraph_a1242 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1242")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.375in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.11111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.375in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1291():
    
    """Build Element style:style for text_a1291 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1291")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1292():
    
    """Build Element style:style for text_a1292 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1292")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1244():
    
    """Build Element style:style for text_a1244 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1244")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1293():
    
    """Build Element style:style for paragraph_a1293 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1293")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1245():
    
    """Build Element style:style for text_a1245 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1245")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1294():
    
    """Build Element style:style for presentation_a1294 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1294")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1246():
    
    """Build Element style:style for paragraph_a1246 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1246")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.8125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.09722in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.3125in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1295():
    
    """Build Element style:style for presentation_a1295 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1295")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1296():
    
    """Build Element style:style for presentation_a1296 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1296")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1248():
    
    """Build Element style:style for presentation_a1248 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1248")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "top")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1297():
    
    """Build Element style:style for presentation_a1297 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1297")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1298():
    
    """Build Element style:style for presentation_a1298 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1298")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1310():
    
    """Build Element style:style for text_a1310 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1310")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1311():
    
    """Build Element style:style for text_a1311 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1311")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1312():
    
    """Build Element style:style for paragraph_a1312 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1312")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1313():
    
    """Build Element style:style for presentation_a1313 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1313")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1314():
    
    """Build Element style:style for presentation_a1314 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1314")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1315():
    
    """Build Element style:style for presentation_a1315 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1315")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1316():
    
    """Build Element style:style for text_a1316 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1316")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1317():
    
    """Build Element style:style for paragraph_a1317 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1317")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.375in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.11111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.375in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1180():
    
    """Build Element style:style for presentation_a1180 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1180")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "top")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1319():
    
    """Build Element style:style for text_a1319 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1319")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1181():
    
    """Build Element style:style for text_a1181 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1181")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1182():
    
    """Build Element style:style for paragraph_a1182 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1182")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.375in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.09722in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.375in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1184():
    
    """Build Element style:style for text_a1184 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1184")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1185():
    
    """Build Element style:style for text_a1185 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1185")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1186():
    
    """Build Element style:style for paragraph_a1186 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1186")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.8125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.3125in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1188():
    
    """Build Element style:style for presentation_a1188 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1188")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "top")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1200():
    
    """Build Element style:style for paragraph_a1200 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1200")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1201():
    
    """Build Element style:style for presentation_a1201 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1201")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1250():
    
    """Build Element style:style for drawing-page_a1250 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1250")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1249")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1202():
    
    """Build Element style:style for text_a1202 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1202")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1251():
    
    """Build Element style:style for text_a1251 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1251")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1203():
    
    """Build Element style:style for paragraph_a1203 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1203")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.375in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.11111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.375in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1252():
    
    """Build Element style:style for text_a1252 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1252")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1253():
    
    """Build Element style:style for paragraph_a1253 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1253")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1205():
    
    """Build Element style:style for text_a1205 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1205")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1254():
    
    """Build Element style:style for presentation_a1254 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1254")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1206():
    
    """Build Element style:style for text_a1206 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1206")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1255():
    
    """Build Element style:style for text_a1255 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1255")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1207():
    
    """Build Element style:style for paragraph_a1207 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1207")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.8125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.09722in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.3125in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1256():
    
    """Build Element style:style for paragraph_a1256 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1256")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.375in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.11111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.375in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1209():
    
    """Build Element style:style for presentation_a1209 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1209")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "top")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1258():
    
    """Build Element style:style for text_a1258 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1258")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1259():
    
    """Build Element style:style for text_a1259 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1259")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1320():
    
    """Build Element style:style for text_a1320 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1320")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1321():
    
    """Build Element style:style for paragraph_a1321 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1321")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.8125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.09722in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.3125in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1323():
    
    """Build Element style:style for presentation_a1323 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1323")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "top")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1325():
    
    """Build Element style:style for drawing-page_a1325 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1325")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1324")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1326():
    
    """Build Element style:style for text_a1326 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1326")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1327():
    
    """Build Element style:style for text_a1327 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1327")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1141():
    
    """Build Element style:style for drawing-page_a1141 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1141")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1140")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1328():
    
    """Build Element style:style for paragraph_a1328 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1328")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1142():
    
    """Build Element style:style for text_a1142 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1142")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1329():
    
    """Build Element style:style for presentation_a1329 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1329")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1190():
    
    """Build Element style:style for drawing-page_a1190 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1190")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1189")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1143():
    
    """Build Element style:style for text_a1143 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1143")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1191():
    
    """Build Element style:style for text_a1191 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1191")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1144():
    
    """Build Element style:style for paragraph_a1144 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1144")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1192():
    
    """Build Element style:style for text_a1192 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1192")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1145():
    
    """Build Element style:style for presentation_a1145 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1145")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1193():
    
    """Build Element style:style for paragraph_a1193 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1193")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1146():
    
    """Build Element style:style for text_a1146 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1146")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#898989")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1194():
    
    """Build Element style:style for presentation_a1194 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1194")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1147():
    
    """Build Element style:style for paragraph_a1147 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1147")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.11111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1195():
    
    """Build Element style:style for presentation_a1195 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1195")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1148():
    
    """Build Element style:style for text_a1148 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1148")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#898989")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1149():
    
    """Build Element style:style for text_a1149 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1149")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#898989")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1197():
    
    """Build Element style:style for drawing-page_a1197 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1197")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1196")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1198():
    
    """Build Element style:style for text_a1198 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1198")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1199():
    
    """Build Element style:style for text_a1199 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1199")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1210():
    
    """Build Element style:style for presentation_a1210 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1210")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1260():
    
    """Build Element style:style for paragraph_a1260 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1260")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.8125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.09722in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.3125in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1212():
    
    """Build Element style:style for drawing-page_a1212 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1212")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1211")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1213():
    
    """Build Element style:style for text_a1213 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1213")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1262():
    
    """Build Element style:style for presentation_a1262 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1262")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "top")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1214():
    
    """Build Element style:style for text_a1214 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1214")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1263():
    
    """Build Element style:style for presentation_a1263 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1263")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1215():
    
    """Build Element style:style for paragraph_a1215 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1215")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1264():
    
    """Build Element style:style for presentation_a1264 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1264")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1216():
    
    """Build Element style:style for presentation_a1216 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1216")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1217():
    
    """Build Element style:style for text_a1217 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1217")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1266():
    
    """Build Element style:style for drawing-page_a1266 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1266")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1265")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1218():
    
    """Build Element style:style for paragraph_a1218 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1218")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.375in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.11111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.375in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1267():
    
    """Build Element style:style for text_a1267 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1267")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1268():
    
    """Build Element style:style for text_a1268 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1268")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1269():
    
    """Build Element style:style for paragraph_a1269 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1269")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1330():
    
    """Build Element style:style for presentation_a1330 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1330")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1331():
    
    """Build Element style:style for presentation_a1331 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1331")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1332():
    
    """Build Element style:style for text_a1332 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1332")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1333():
    
    """Build Element style:style for paragraph_a1333 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1333")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.375in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.11111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.375in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1335():
    
    """Build Element style:style for text_a1335 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1335")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1336():
    
    """Build Element style:style for text_a1336 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1336")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1150():
    
    """Build Element style:style for paragraph_a1150 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1150")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.09722in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1337():
    
    """Build Element style:style for paragraph_a1337 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1337")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.8125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.09722in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.3125in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1152():
    
    """Build Element style:style for presentation_a1152 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1152")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "top")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1339():
    
    """Build Element style:style for presentation_a1339 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1339")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "top")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1154():
    
    """Build Element style:style for drawing-page_a1154 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1154")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1153")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1155():
    
    """Build Element style:style for text_a1155 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1155")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1156():
    
    """Build Element style:style for text_a1156 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1156")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1157():
    
    """Build Element style:style for paragraph_a1157 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1157")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1158():
    
    """Build Element style:style for presentation_a1158 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1158")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1159():
    
    """Build Element style:style for text_a1159 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1159")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1220():
    
    """Build Element style:style for text_a1220 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1220")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1221():
    
    """Build Element style:style for text_a1221 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1221")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1222():
    
    """Build Element style:style for paragraph_a1222 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1222")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.8125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.09722in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.3125in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1270():
    
    """Build Element style:style for presentation_a1270 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1270")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1271():
    
    """Build Element style:style for presentation_a1271 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1271")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1224():
    
    """Build Element style:style for presentation_a1224 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1224")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "top")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1272():
    
    """Build Element style:style for presentation_a1272 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1272")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1225():
    
    """Build Element style:style for presentation_a1225 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1225")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1273():
    
    """Build Element style:style for presentation_a1273 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1273")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1227():
    
    """Build Element style:style for drawing-page_a1227 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1227")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1226")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1275():
    
    """Build Element style:style for drawing-page_a1275 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1275")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1274")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1228():
    
    """Build Element style:style for text_a1228 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1228")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1276():
    
    """Build Element style:style for text_a1276 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1276")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1229():
    
    """Build Element style:style for text_a1229 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1229")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1277():
    
    """Build Element style:style for text_a1277 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1277")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1278():
    
    """Build Element style:style for paragraph_a1278 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1278")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1279():
    
    """Build Element style:style for presentation_a1279 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1279")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1341():
    
    """Build Element style:style for drawing-page_a1341 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1341")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1340")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1342():
    
    """Build Element style:style for text_a1342 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1342")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1343():
    
    """Build Element style:style for text_a1343 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1343")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1344():
    
    """Build Element style:style for paragraph_a1344 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1344")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1345():
    
    """Build Element style:style for presentation_a1345 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1345")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1346():
    
    """Build Element style:style for presentation_a1346 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1346")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1160():
    
    """Build Element style:style for paragraph_a1160 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1160")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.375in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.11111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.375in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1162():
    
    """Build Element style:style for text_a1162 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1162")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1163():
    
    """Build Element style:style for text_a1163 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1163")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1164():
    
    """Build Element style:style for paragraph_a1164 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1164")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.8125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.09722in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.3125in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1166():
    
    """Build Element style:style for presentation_a1166 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1166")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "top")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1168():
    
    """Build Element style:style for drawing-page_a1168 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1168")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1167")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1169():
    
    """Build Element style:style for text_a1169 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1169")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1230():
    
    """Build Element style:style for paragraph_a1230 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1230")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1231():
    
    """Build Element style:style for presentation_a1231 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1231")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-height", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}auto-grow-width", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-horizontal-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}textarea-vertical-align", "middle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-bottom", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-left", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-right", "0.1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}padding-top", "0.05in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}wrap-option", "wrap")
    elem.append( child )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-independent-line-spacing", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1232():
    
    """Build Element style:style for presentation_a1232 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1232")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1280():
    
    """Build Element style:style for presentation_a1280 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1280")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_presentation_a1233():
    
    """Build Element style:style for presentation_a1233 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "presentation")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1233")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}graphic-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}stroke", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1281():
    
    """Build Element style:style for text_a1281 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1281")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.44444in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1282():
    
    """Build Element style:style for paragraph_a1282 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1282")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.375in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.11111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.375in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_drawing_page_a1235():
    
    """Build Element style:style for drawing-page_a1235 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "drawing-page")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1235")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}drawing-page-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}background-size", "border")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill", "gradient")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}fill-gradient-name", "a1234")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-objects-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}background-visible", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-date-time", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-footer", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-header", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}display-page-number", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}visibility", "visible")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1236():
    
    """Build Element style:style for text_a1236 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1236")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1284():
    
    """Build Element style:style for text_a1284 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1284")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1237():
    
    """Build Element style:style for text_a1237 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1237")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.61111in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_text_a1285():
    
    """Build Element style:style for text_a1285 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1285")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}country", "US")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Calibri")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.38889in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}language", "en")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1238():
    
    """Build Element style:style for paragraph_a1238 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1238")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "center")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "0in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def style_8_style_paragraph_a1286():
    
    """Build Element style:style for paragraph_a1286 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}family", "paragraph")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1286")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}paragraph-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}punctuation-wrap", "hanging")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stop-distance", "1in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}vertical-align", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}writing-mode", "lr-tb")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}line-height", "100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-bottom", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-left", "0.8125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-right", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}margin-top", "0.09722in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-align", "left")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-indent", "-0.3125in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}tab-stops" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-asian", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-size-complex", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-style-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-asian", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-weight-complex", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}letter-kerning", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-line-through-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-position", "0% 100%")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-color", "font-color")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-mode", "continuous")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-style", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-type", "none")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-underline-width", "auto")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color", "#000000")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "0.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-style", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-variant", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-weight", "normal")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}letter-spacing", "0in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}text-transform", "none")
    elem.append( child )
    
    
    return elem

def text_8_list_style_a1179():
    
    """Build Element text:list-style for a1179 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1179")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.0625in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.5in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1187():
    
    """Build Element text:list-style for a1187 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1187")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.0625in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.5in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1247():
    
    """Build Element text:list-style for a1247 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1247")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.0625in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.5in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1261():
    
    """Build Element text:list-style for a1261 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1261")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.0625in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.5in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1322():
    
    """Build Element text:list-style for a1322 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1322")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.0625in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.5in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1257():
    
    """Build Element text:list-style for a1257 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1257")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1318():
    
    """Build Element text:list-style for a1318 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1318")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1334():
    
    """Build Element text:list-style for a1334 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1334")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1204():
    
    """Build Element text:list-style for a1204 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1204")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1151():
    
    """Build Element text:list-style for a1151 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1151")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-number" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0in")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-number" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.5in")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-number" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1in")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-number" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.5in")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-number" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2in")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-number" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.5in")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-number" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3in")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-number" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.5in")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-number" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "4in")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1283():
    
    """Build Element text:list-style for a1283 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1283")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1338():
    
    """Build Element text:list-style for a1338 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1338")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.0625in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.5in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1208():
    
    """Build Element text:list-style for a1208 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1208")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.0625in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.5in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1161():
    
    """Build Element text:list-style for a1161 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1161")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1287():
    
    """Build Element text:list-style for a1287 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1287")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.0625in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.5in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1223():
    
    """Build Element text:list-style for a1223 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1223")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.0625in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.5in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1219():
    
    """Build Element text:list-style for a1219 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1219")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1165():
    
    """Build Element text:list-style for a1165 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1165")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.0625in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.5in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\x93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.3125in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.9375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1175():
    
    """Build Element text:list-style for a1175 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1175")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1183():
    
    """Build Element text:list-style for a1183 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1183")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem

def text_8_list_style_a1243():
    
    """Build Element text:list-style for a1243 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-style" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "a1243")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "1")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "2")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.4375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "3")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "0.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "4")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "5")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "1.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "6")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "7")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "2.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "8")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.375in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-level-style-bullet" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}bullet-char", "\xE2\x80\xA2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}level", "9")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}list-level-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}min-label-width", "0.375in")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}space-before", "3.875in")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}text-properties" )
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-family-generic", "swiss")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}font-pitch", "variable")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-family", "Arial")
    child_2.set("{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}font-size", "100%")
    child.append( child_2 )
    
    
    return elem



# Set values in func_quick_lookupD
func_quick_lookupD["a1151"] = text_8_list_style_a1151
func_quick_lookupD["a1161"] = text_8_list_style_a1161
func_quick_lookupD["a1165"] = text_8_list_style_a1165
func_quick_lookupD["a1175"] = text_8_list_style_a1175
func_quick_lookupD["a1179"] = text_8_list_style_a1179
func_quick_lookupD["a1183"] = text_8_list_style_a1183
func_quick_lookupD["a1187"] = text_8_list_style_a1187
func_quick_lookupD["a1204"] = text_8_list_style_a1204
func_quick_lookupD["a1208"] = text_8_list_style_a1208
func_quick_lookupD["a1219"] = text_8_list_style_a1219
func_quick_lookupD["a1223"] = text_8_list_style_a1223
func_quick_lookupD["a1243"] = text_8_list_style_a1243
func_quick_lookupD["a1247"] = text_8_list_style_a1247
func_quick_lookupD["a1257"] = text_8_list_style_a1257
func_quick_lookupD["a1261"] = text_8_list_style_a1261
func_quick_lookupD["a1283"] = text_8_list_style_a1283
func_quick_lookupD["a1287"] = text_8_list_style_a1287
func_quick_lookupD["a1318"] = text_8_list_style_a1318
func_quick_lookupD["a1322"] = text_8_list_style_a1322
func_quick_lookupD["a1334"] = text_8_list_style_a1334
func_quick_lookupD["a1338"] = text_8_list_style_a1338
func_quick_lookupD["drawing-page_a1141"] = style_8_style_drawing_page_a1141
func_quick_lookupD["drawing-page_a1154"] = style_8_style_drawing_page_a1154
func_quick_lookupD["drawing-page_a1168"] = style_8_style_drawing_page_a1168
func_quick_lookupD["drawing-page_a1190"] = style_8_style_drawing_page_a1190
func_quick_lookupD["drawing-page_a1197"] = style_8_style_drawing_page_a1197
func_quick_lookupD["drawing-page_a1212"] = style_8_style_drawing_page_a1212
func_quick_lookupD["drawing-page_a1227"] = style_8_style_drawing_page_a1227
func_quick_lookupD["drawing-page_a1235"] = style_8_style_drawing_page_a1235
func_quick_lookupD["drawing-page_a1250"] = style_8_style_drawing_page_a1250
func_quick_lookupD["drawing-page_a1266"] = style_8_style_drawing_page_a1266
func_quick_lookupD["drawing-page_a1275"] = style_8_style_drawing_page_a1275
func_quick_lookupD["drawing-page_a1290"] = style_8_style_drawing_page_a1290
func_quick_lookupD["drawing-page_a1300"] = style_8_style_drawing_page_a1300
func_quick_lookupD["drawing-page_a1309"] = style_8_style_drawing_page_a1309
func_quick_lookupD["drawing-page_a1325"] = style_8_style_drawing_page_a1325
func_quick_lookupD["drawing-page_a1341"] = style_8_style_drawing_page_a1341
func_quick_lookupD["paragraph_a1144"] = style_8_style_paragraph_a1144
func_quick_lookupD["paragraph_a1147"] = style_8_style_paragraph_a1147
func_quick_lookupD["paragraph_a1150"] = style_8_style_paragraph_a1150
func_quick_lookupD["paragraph_a1157"] = style_8_style_paragraph_a1157
func_quick_lookupD["paragraph_a1160"] = style_8_style_paragraph_a1160
func_quick_lookupD["paragraph_a1164"] = style_8_style_paragraph_a1164
func_quick_lookupD["paragraph_a1171"] = style_8_style_paragraph_a1171
func_quick_lookupD["paragraph_a1174"] = style_8_style_paragraph_a1174
func_quick_lookupD["paragraph_a1178"] = style_8_style_paragraph_a1178
func_quick_lookupD["paragraph_a1182"] = style_8_style_paragraph_a1182
func_quick_lookupD["paragraph_a1186"] = style_8_style_paragraph_a1186
func_quick_lookupD["paragraph_a1193"] = style_8_style_paragraph_a1193
func_quick_lookupD["paragraph_a1200"] = style_8_style_paragraph_a1200
func_quick_lookupD["paragraph_a1203"] = style_8_style_paragraph_a1203
func_quick_lookupD["paragraph_a1207"] = style_8_style_paragraph_a1207
func_quick_lookupD["paragraph_a1215"] = style_8_style_paragraph_a1215
func_quick_lookupD["paragraph_a1218"] = style_8_style_paragraph_a1218
func_quick_lookupD["paragraph_a1222"] = style_8_style_paragraph_a1222
func_quick_lookupD["paragraph_a1230"] = style_8_style_paragraph_a1230
func_quick_lookupD["paragraph_a1238"] = style_8_style_paragraph_a1238
func_quick_lookupD["paragraph_a1242"] = style_8_style_paragraph_a1242
func_quick_lookupD["paragraph_a1246"] = style_8_style_paragraph_a1246
func_quick_lookupD["paragraph_a1253"] = style_8_style_paragraph_a1253
func_quick_lookupD["paragraph_a1256"] = style_8_style_paragraph_a1256
func_quick_lookupD["paragraph_a1260"] = style_8_style_paragraph_a1260
func_quick_lookupD["paragraph_a1269"] = style_8_style_paragraph_a1269
func_quick_lookupD["paragraph_a1278"] = style_8_style_paragraph_a1278
func_quick_lookupD["paragraph_a1282"] = style_8_style_paragraph_a1282
func_quick_lookupD["paragraph_a1286"] = style_8_style_paragraph_a1286
func_quick_lookupD["paragraph_a1293"] = style_8_style_paragraph_a1293
func_quick_lookupD["paragraph_a1303"] = style_8_style_paragraph_a1303
func_quick_lookupD["paragraph_a1312"] = style_8_style_paragraph_a1312
func_quick_lookupD["paragraph_a1317"] = style_8_style_paragraph_a1317
func_quick_lookupD["paragraph_a1321"] = style_8_style_paragraph_a1321
func_quick_lookupD["paragraph_a1328"] = style_8_style_paragraph_a1328
func_quick_lookupD["paragraph_a1333"] = style_8_style_paragraph_a1333
func_quick_lookupD["paragraph_a1337"] = style_8_style_paragraph_a1337
func_quick_lookupD["paragraph_a1344"] = style_8_style_paragraph_a1344
func_quick_lookupD["presentation_a1145"] = style_8_style_presentation_a1145
func_quick_lookupD["presentation_a1152"] = style_8_style_presentation_a1152
func_quick_lookupD["presentation_a1158"] = style_8_style_presentation_a1158
func_quick_lookupD["presentation_a1166"] = style_8_style_presentation_a1166
func_quick_lookupD["presentation_a1172"] = style_8_style_presentation_a1172
func_quick_lookupD["presentation_a1180"] = style_8_style_presentation_a1180
func_quick_lookupD["presentation_a1188"] = style_8_style_presentation_a1188
func_quick_lookupD["presentation_a1194"] = style_8_style_presentation_a1194
func_quick_lookupD["presentation_a1195"] = style_8_style_presentation_a1195
func_quick_lookupD["presentation_a1201"] = style_8_style_presentation_a1201
func_quick_lookupD["presentation_a1209"] = style_8_style_presentation_a1209
func_quick_lookupD["presentation_a1210"] = style_8_style_presentation_a1210
func_quick_lookupD["presentation_a1216"] = style_8_style_presentation_a1216
func_quick_lookupD["presentation_a1224"] = style_8_style_presentation_a1224
func_quick_lookupD["presentation_a1225"] = style_8_style_presentation_a1225
func_quick_lookupD["presentation_a1231"] = style_8_style_presentation_a1231
func_quick_lookupD["presentation_a1232"] = style_8_style_presentation_a1232
func_quick_lookupD["presentation_a1233"] = style_8_style_presentation_a1233
func_quick_lookupD["presentation_a1239"] = style_8_style_presentation_a1239
func_quick_lookupD["presentation_a1240"] = style_8_style_presentation_a1240
func_quick_lookupD["presentation_a1248"] = style_8_style_presentation_a1248
func_quick_lookupD["presentation_a1254"] = style_8_style_presentation_a1254
func_quick_lookupD["presentation_a1262"] = style_8_style_presentation_a1262
func_quick_lookupD["presentation_a1263"] = style_8_style_presentation_a1263
func_quick_lookupD["presentation_a1264"] = style_8_style_presentation_a1264
func_quick_lookupD["presentation_a1270"] = style_8_style_presentation_a1270
func_quick_lookupD["presentation_a1271"] = style_8_style_presentation_a1271
func_quick_lookupD["presentation_a1272"] = style_8_style_presentation_a1272
func_quick_lookupD["presentation_a1273"] = style_8_style_presentation_a1273
func_quick_lookupD["presentation_a1279"] = style_8_style_presentation_a1279
func_quick_lookupD["presentation_a1280"] = style_8_style_presentation_a1280
func_quick_lookupD["presentation_a1288"] = style_8_style_presentation_a1288
func_quick_lookupD["presentation_a1294"] = style_8_style_presentation_a1294
func_quick_lookupD["presentation_a1295"] = style_8_style_presentation_a1295
func_quick_lookupD["presentation_a1296"] = style_8_style_presentation_a1296
func_quick_lookupD["presentation_a1297"] = style_8_style_presentation_a1297
func_quick_lookupD["presentation_a1298"] = style_8_style_presentation_a1298
func_quick_lookupD["presentation_a1304"] = style_8_style_presentation_a1304
func_quick_lookupD["presentation_a1305"] = style_8_style_presentation_a1305
func_quick_lookupD["presentation_a1306"] = style_8_style_presentation_a1306
func_quick_lookupD["presentation_a1307"] = style_8_style_presentation_a1307
func_quick_lookupD["presentation_a1313"] = style_8_style_presentation_a1313
func_quick_lookupD["presentation_a1314"] = style_8_style_presentation_a1314
func_quick_lookupD["presentation_a1315"] = style_8_style_presentation_a1315
func_quick_lookupD["presentation_a1323"] = style_8_style_presentation_a1323
func_quick_lookupD["presentation_a1329"] = style_8_style_presentation_a1329
func_quick_lookupD["presentation_a1330"] = style_8_style_presentation_a1330
func_quick_lookupD["presentation_a1331"] = style_8_style_presentation_a1331
func_quick_lookupD["presentation_a1339"] = style_8_style_presentation_a1339
func_quick_lookupD["presentation_a1345"] = style_8_style_presentation_a1345
func_quick_lookupD["presentation_a1346"] = style_8_style_presentation_a1346
func_quick_lookupD["text_a1142"] = style_8_style_text_a1142
func_quick_lookupD["text_a1143"] = style_8_style_text_a1143
func_quick_lookupD["text_a1146"] = style_8_style_text_a1146
func_quick_lookupD["text_a1148"] = style_8_style_text_a1148
func_quick_lookupD["text_a1149"] = style_8_style_text_a1149
func_quick_lookupD["text_a1155"] = style_8_style_text_a1155
func_quick_lookupD["text_a1156"] = style_8_style_text_a1156
func_quick_lookupD["text_a1159"] = style_8_style_text_a1159
func_quick_lookupD["text_a1162"] = style_8_style_text_a1162
func_quick_lookupD["text_a1163"] = style_8_style_text_a1163
func_quick_lookupD["text_a1169"] = style_8_style_text_a1169
func_quick_lookupD["text_a1170"] = style_8_style_text_a1170
func_quick_lookupD["text_a1173"] = style_8_style_text_a1173
func_quick_lookupD["text_a1176"] = style_8_style_text_a1176
func_quick_lookupD["text_a1177"] = style_8_style_text_a1177
func_quick_lookupD["text_a1181"] = style_8_style_text_a1181
func_quick_lookupD["text_a1184"] = style_8_style_text_a1184
func_quick_lookupD["text_a1185"] = style_8_style_text_a1185
func_quick_lookupD["text_a1191"] = style_8_style_text_a1191
func_quick_lookupD["text_a1192"] = style_8_style_text_a1192
func_quick_lookupD["text_a1198"] = style_8_style_text_a1198
func_quick_lookupD["text_a1199"] = style_8_style_text_a1199
func_quick_lookupD["text_a1202"] = style_8_style_text_a1202
func_quick_lookupD["text_a1205"] = style_8_style_text_a1205
func_quick_lookupD["text_a1206"] = style_8_style_text_a1206
func_quick_lookupD["text_a1213"] = style_8_style_text_a1213
func_quick_lookupD["text_a1214"] = style_8_style_text_a1214
func_quick_lookupD["text_a1217"] = style_8_style_text_a1217
func_quick_lookupD["text_a1220"] = style_8_style_text_a1220
func_quick_lookupD["text_a1221"] = style_8_style_text_a1221
func_quick_lookupD["text_a1228"] = style_8_style_text_a1228
func_quick_lookupD["text_a1229"] = style_8_style_text_a1229
func_quick_lookupD["text_a1236"] = style_8_style_text_a1236
func_quick_lookupD["text_a1237"] = style_8_style_text_a1237
func_quick_lookupD["text_a1241"] = style_8_style_text_a1241
func_quick_lookupD["text_a1244"] = style_8_style_text_a1244
func_quick_lookupD["text_a1245"] = style_8_style_text_a1245
func_quick_lookupD["text_a1251"] = style_8_style_text_a1251
func_quick_lookupD["text_a1252"] = style_8_style_text_a1252
func_quick_lookupD["text_a1255"] = style_8_style_text_a1255
func_quick_lookupD["text_a1258"] = style_8_style_text_a1258
func_quick_lookupD["text_a1259"] = style_8_style_text_a1259
func_quick_lookupD["text_a1267"] = style_8_style_text_a1267
func_quick_lookupD["text_a1268"] = style_8_style_text_a1268
func_quick_lookupD["text_a1276"] = style_8_style_text_a1276
func_quick_lookupD["text_a1277"] = style_8_style_text_a1277
func_quick_lookupD["text_a1281"] = style_8_style_text_a1281
func_quick_lookupD["text_a1284"] = style_8_style_text_a1284
func_quick_lookupD["text_a1285"] = style_8_style_text_a1285
func_quick_lookupD["text_a1291"] = style_8_style_text_a1291
func_quick_lookupD["text_a1292"] = style_8_style_text_a1292
func_quick_lookupD["text_a1301"] = style_8_style_text_a1301
func_quick_lookupD["text_a1302"] = style_8_style_text_a1302
func_quick_lookupD["text_a1310"] = style_8_style_text_a1310
func_quick_lookupD["text_a1311"] = style_8_style_text_a1311
func_quick_lookupD["text_a1316"] = style_8_style_text_a1316
func_quick_lookupD["text_a1319"] = style_8_style_text_a1319
func_quick_lookupD["text_a1320"] = style_8_style_text_a1320
func_quick_lookupD["text_a1326"] = style_8_style_text_a1326
func_quick_lookupD["text_a1327"] = style_8_style_text_a1327
func_quick_lookupD["text_a1332"] = style_8_style_text_a1332
func_quick_lookupD["text_a1335"] = style_8_style_text_a1335
func_quick_lookupD["text_a1336"] = style_8_style_text_a1336
func_quick_lookupD["text_a1342"] = style_8_style_text_a1342
func_quick_lookupD["text_a1343"] = style_8_style_text_a1343




# Set values in content_style_name_lookupD
content_style_name_lookupD["a1141"] = style_8_style_drawing_page_a1141
content_style_name_lookupD["a1142"] = style_8_style_text_a1142
content_style_name_lookupD["a1143"] = style_8_style_text_a1143
content_style_name_lookupD["a1144"] = style_8_style_paragraph_a1144
content_style_name_lookupD["a1145"] = style_8_style_presentation_a1145
content_style_name_lookupD["a1146"] = style_8_style_text_a1146
content_style_name_lookupD["a1147"] = style_8_style_paragraph_a1147
content_style_name_lookupD["a1148"] = style_8_style_text_a1148
content_style_name_lookupD["a1149"] = style_8_style_text_a1149
content_style_name_lookupD["a1150"] = style_8_style_paragraph_a1150
content_style_name_lookupD["a1151"] = text_8_list_style_a1151
content_style_name_lookupD["a1152"] = style_8_style_presentation_a1152
content_style_name_lookupD["a1154"] = style_8_style_drawing_page_a1154
content_style_name_lookupD["a1155"] = style_8_style_text_a1155
content_style_name_lookupD["a1156"] = style_8_style_text_a1156
content_style_name_lookupD["a1157"] = style_8_style_paragraph_a1157
content_style_name_lookupD["a1158"] = style_8_style_presentation_a1158
content_style_name_lookupD["a1159"] = style_8_style_text_a1159
content_style_name_lookupD["a1160"] = style_8_style_paragraph_a1160
content_style_name_lookupD["a1161"] = text_8_list_style_a1161
content_style_name_lookupD["a1162"] = style_8_style_text_a1162
content_style_name_lookupD["a1163"] = style_8_style_text_a1163
content_style_name_lookupD["a1164"] = style_8_style_paragraph_a1164
content_style_name_lookupD["a1165"] = text_8_list_style_a1165
content_style_name_lookupD["a1166"] = style_8_style_presentation_a1166
content_style_name_lookupD["a1168"] = style_8_style_drawing_page_a1168
content_style_name_lookupD["a1169"] = style_8_style_text_a1169
content_style_name_lookupD["a1170"] = style_8_style_text_a1170
content_style_name_lookupD["a1171"] = style_8_style_paragraph_a1171
content_style_name_lookupD["a1172"] = style_8_style_presentation_a1172
content_style_name_lookupD["a1173"] = style_8_style_text_a1173
content_style_name_lookupD["a1174"] = style_8_style_paragraph_a1174
content_style_name_lookupD["a1175"] = text_8_list_style_a1175
content_style_name_lookupD["a1176"] = style_8_style_text_a1176
content_style_name_lookupD["a1177"] = style_8_style_text_a1177
content_style_name_lookupD["a1178"] = style_8_style_paragraph_a1178
content_style_name_lookupD["a1179"] = text_8_list_style_a1179
content_style_name_lookupD["a1180"] = style_8_style_presentation_a1180
content_style_name_lookupD["a1181"] = style_8_style_text_a1181
content_style_name_lookupD["a1182"] = style_8_style_paragraph_a1182
content_style_name_lookupD["a1183"] = text_8_list_style_a1183
content_style_name_lookupD["a1184"] = style_8_style_text_a1184
content_style_name_lookupD["a1185"] = style_8_style_text_a1185
content_style_name_lookupD["a1186"] = style_8_style_paragraph_a1186
content_style_name_lookupD["a1187"] = text_8_list_style_a1187
content_style_name_lookupD["a1188"] = style_8_style_presentation_a1188
content_style_name_lookupD["a1190"] = style_8_style_drawing_page_a1190
content_style_name_lookupD["a1191"] = style_8_style_text_a1191
content_style_name_lookupD["a1192"] = style_8_style_text_a1192
content_style_name_lookupD["a1193"] = style_8_style_paragraph_a1193
content_style_name_lookupD["a1194"] = style_8_style_presentation_a1194
content_style_name_lookupD["a1195"] = style_8_style_presentation_a1195
content_style_name_lookupD["a1197"] = style_8_style_drawing_page_a1197
content_style_name_lookupD["a1198"] = style_8_style_text_a1198
content_style_name_lookupD["a1199"] = style_8_style_text_a1199
content_style_name_lookupD["a1200"] = style_8_style_paragraph_a1200
content_style_name_lookupD["a1201"] = style_8_style_presentation_a1201
content_style_name_lookupD["a1202"] = style_8_style_text_a1202
content_style_name_lookupD["a1203"] = style_8_style_paragraph_a1203
content_style_name_lookupD["a1204"] = text_8_list_style_a1204
content_style_name_lookupD["a1205"] = style_8_style_text_a1205
content_style_name_lookupD["a1206"] = style_8_style_text_a1206
content_style_name_lookupD["a1207"] = style_8_style_paragraph_a1207
content_style_name_lookupD["a1208"] = text_8_list_style_a1208
content_style_name_lookupD["a1209"] = style_8_style_presentation_a1209
content_style_name_lookupD["a1210"] = style_8_style_presentation_a1210
content_style_name_lookupD["a1212"] = style_8_style_drawing_page_a1212
content_style_name_lookupD["a1213"] = style_8_style_text_a1213
content_style_name_lookupD["a1214"] = style_8_style_text_a1214
content_style_name_lookupD["a1215"] = style_8_style_paragraph_a1215
content_style_name_lookupD["a1216"] = style_8_style_presentation_a1216
content_style_name_lookupD["a1217"] = style_8_style_text_a1217
content_style_name_lookupD["a1218"] = style_8_style_paragraph_a1218
content_style_name_lookupD["a1219"] = text_8_list_style_a1219
content_style_name_lookupD["a1220"] = style_8_style_text_a1220
content_style_name_lookupD["a1221"] = style_8_style_text_a1221
content_style_name_lookupD["a1222"] = style_8_style_paragraph_a1222
content_style_name_lookupD["a1223"] = text_8_list_style_a1223
content_style_name_lookupD["a1224"] = style_8_style_presentation_a1224
content_style_name_lookupD["a1225"] = style_8_style_presentation_a1225
content_style_name_lookupD["a1227"] = style_8_style_drawing_page_a1227
content_style_name_lookupD["a1228"] = style_8_style_text_a1228
content_style_name_lookupD["a1229"] = style_8_style_text_a1229
content_style_name_lookupD["a1230"] = style_8_style_paragraph_a1230
content_style_name_lookupD["a1231"] = style_8_style_presentation_a1231
content_style_name_lookupD["a1232"] = style_8_style_presentation_a1232
content_style_name_lookupD["a1233"] = style_8_style_presentation_a1233
content_style_name_lookupD["a1235"] = style_8_style_drawing_page_a1235
content_style_name_lookupD["a1236"] = style_8_style_text_a1236
content_style_name_lookupD["a1237"] = style_8_style_text_a1237
content_style_name_lookupD["a1238"] = style_8_style_paragraph_a1238
content_style_name_lookupD["a1239"] = style_8_style_presentation_a1239
content_style_name_lookupD["a1240"] = style_8_style_presentation_a1240
content_style_name_lookupD["a1241"] = style_8_style_text_a1241
content_style_name_lookupD["a1242"] = style_8_style_paragraph_a1242
content_style_name_lookupD["a1243"] = text_8_list_style_a1243
content_style_name_lookupD["a1244"] = style_8_style_text_a1244
content_style_name_lookupD["a1245"] = style_8_style_text_a1245
content_style_name_lookupD["a1246"] = style_8_style_paragraph_a1246
content_style_name_lookupD["a1247"] = text_8_list_style_a1247
content_style_name_lookupD["a1248"] = style_8_style_presentation_a1248
content_style_name_lookupD["a1250"] = style_8_style_drawing_page_a1250
content_style_name_lookupD["a1251"] = style_8_style_text_a1251
content_style_name_lookupD["a1252"] = style_8_style_text_a1252
content_style_name_lookupD["a1253"] = style_8_style_paragraph_a1253
content_style_name_lookupD["a1254"] = style_8_style_presentation_a1254
content_style_name_lookupD["a1255"] = style_8_style_text_a1255
content_style_name_lookupD["a1256"] = style_8_style_paragraph_a1256
content_style_name_lookupD["a1257"] = text_8_list_style_a1257
content_style_name_lookupD["a1258"] = style_8_style_text_a1258
content_style_name_lookupD["a1259"] = style_8_style_text_a1259
content_style_name_lookupD["a1260"] = style_8_style_paragraph_a1260
content_style_name_lookupD["a1261"] = text_8_list_style_a1261
content_style_name_lookupD["a1262"] = style_8_style_presentation_a1262
content_style_name_lookupD["a1263"] = style_8_style_presentation_a1263
content_style_name_lookupD["a1264"] = style_8_style_presentation_a1264
content_style_name_lookupD["a1266"] = style_8_style_drawing_page_a1266
content_style_name_lookupD["a1267"] = style_8_style_text_a1267
content_style_name_lookupD["a1268"] = style_8_style_text_a1268
content_style_name_lookupD["a1269"] = style_8_style_paragraph_a1269
content_style_name_lookupD["a1270"] = style_8_style_presentation_a1270
content_style_name_lookupD["a1271"] = style_8_style_presentation_a1271
content_style_name_lookupD["a1272"] = style_8_style_presentation_a1272
content_style_name_lookupD["a1273"] = style_8_style_presentation_a1273
content_style_name_lookupD["a1275"] = style_8_style_drawing_page_a1275
content_style_name_lookupD["a1276"] = style_8_style_text_a1276
content_style_name_lookupD["a1277"] = style_8_style_text_a1277
content_style_name_lookupD["a1278"] = style_8_style_paragraph_a1278
content_style_name_lookupD["a1279"] = style_8_style_presentation_a1279
content_style_name_lookupD["a1280"] = style_8_style_presentation_a1280
content_style_name_lookupD["a1281"] = style_8_style_text_a1281
content_style_name_lookupD["a1282"] = style_8_style_paragraph_a1282
content_style_name_lookupD["a1283"] = text_8_list_style_a1283
content_style_name_lookupD["a1284"] = style_8_style_text_a1284
content_style_name_lookupD["a1285"] = style_8_style_text_a1285
content_style_name_lookupD["a1286"] = style_8_style_paragraph_a1286
content_style_name_lookupD["a1287"] = text_8_list_style_a1287
content_style_name_lookupD["a1288"] = style_8_style_presentation_a1288
content_style_name_lookupD["a1290"] = style_8_style_drawing_page_a1290
content_style_name_lookupD["a1291"] = style_8_style_text_a1291
content_style_name_lookupD["a1292"] = style_8_style_text_a1292
content_style_name_lookupD["a1293"] = style_8_style_paragraph_a1293
content_style_name_lookupD["a1294"] = style_8_style_presentation_a1294
content_style_name_lookupD["a1295"] = style_8_style_presentation_a1295
content_style_name_lookupD["a1296"] = style_8_style_presentation_a1296
content_style_name_lookupD["a1297"] = style_8_style_presentation_a1297
content_style_name_lookupD["a1298"] = style_8_style_presentation_a1298
content_style_name_lookupD["a1300"] = style_8_style_drawing_page_a1300
content_style_name_lookupD["a1301"] = style_8_style_text_a1301
content_style_name_lookupD["a1302"] = style_8_style_text_a1302
content_style_name_lookupD["a1303"] = style_8_style_paragraph_a1303
content_style_name_lookupD["a1304"] = style_8_style_presentation_a1304
content_style_name_lookupD["a1305"] = style_8_style_presentation_a1305
content_style_name_lookupD["a1306"] = style_8_style_presentation_a1306
content_style_name_lookupD["a1307"] = style_8_style_presentation_a1307
content_style_name_lookupD["a1309"] = style_8_style_drawing_page_a1309
content_style_name_lookupD["a1310"] = style_8_style_text_a1310
content_style_name_lookupD["a1311"] = style_8_style_text_a1311
content_style_name_lookupD["a1312"] = style_8_style_paragraph_a1312
content_style_name_lookupD["a1313"] = style_8_style_presentation_a1313
content_style_name_lookupD["a1314"] = style_8_style_presentation_a1314
content_style_name_lookupD["a1315"] = style_8_style_presentation_a1315
content_style_name_lookupD["a1316"] = style_8_style_text_a1316
content_style_name_lookupD["a1317"] = style_8_style_paragraph_a1317
content_style_name_lookupD["a1318"] = text_8_list_style_a1318
content_style_name_lookupD["a1319"] = style_8_style_text_a1319
content_style_name_lookupD["a1320"] = style_8_style_text_a1320
content_style_name_lookupD["a1321"] = style_8_style_paragraph_a1321
content_style_name_lookupD["a1322"] = text_8_list_style_a1322
content_style_name_lookupD["a1323"] = style_8_style_presentation_a1323
content_style_name_lookupD["a1325"] = style_8_style_drawing_page_a1325
content_style_name_lookupD["a1326"] = style_8_style_text_a1326
content_style_name_lookupD["a1327"] = style_8_style_text_a1327
content_style_name_lookupD["a1328"] = style_8_style_paragraph_a1328
content_style_name_lookupD["a1329"] = style_8_style_presentation_a1329
content_style_name_lookupD["a1330"] = style_8_style_presentation_a1330
content_style_name_lookupD["a1331"] = style_8_style_presentation_a1331
content_style_name_lookupD["a1332"] = style_8_style_text_a1332
content_style_name_lookupD["a1333"] = style_8_style_paragraph_a1333
content_style_name_lookupD["a1334"] = text_8_list_style_a1334
content_style_name_lookupD["a1335"] = style_8_style_text_a1335
content_style_name_lookupD["a1336"] = style_8_style_text_a1336
content_style_name_lookupD["a1337"] = style_8_style_paragraph_a1337
content_style_name_lookupD["a1338"] = text_8_list_style_a1338
content_style_name_lookupD["a1339"] = style_8_style_presentation_a1339
content_style_name_lookupD["a1341"] = style_8_style_drawing_page_a1341
content_style_name_lookupD["a1342"] = style_8_style_text_a1342
content_style_name_lookupD["a1343"] = style_8_style_text_a1343
content_style_name_lookupD["a1344"] = style_8_style_paragraph_a1344
content_style_name_lookupD["a1345"] = style_8_style_presentation_a1345
content_style_name_lookupD["a1346"] = style_8_style_presentation_a1346

if __name__ == "__main__":
    print( content_style_name_lookupD["a1160"]() )
