
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


# Use master_page_name_lookupD for access to master page names
# index=layout name (e.g. "Master1-PPL24"), value=master name (e.g. "Master1-Layout24-tbl-Title-and-Table")

master_page_name_lookupD = {}

# Use layout_page_name_lookupD for access layout page names
# index=layout name (e.g. "Master1-Layout24-tbl-Title-and-Table"), value=master name (e.g. "Master1-PPL24")

layout_page_name_lookupD = {}

def draw_8_page_Master1_PPL1():
    
    """Build Element draw:page for Master1-PPL1 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-256")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout1-title-Title-Slide")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide1")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1141")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id146")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1145")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.60764in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "8.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.75in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "2.32986in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1144")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1142")
    child_4.text = "ppLayoutTitle"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1143")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id147")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Subtitle 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "subtitle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1152")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.91667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "7in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "1.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.25in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1147")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1146")
    child_4.text = "Text(2)"
    child_3.append( child_4 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1151")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1151")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1150")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1148")
    child_8.text = "For ppLayoutTitle"
    child_7.append( child_8 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1149")
    child_7.append( child_8 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL12():
    
    """Build Element draw:page for Master1-PPL12 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-257")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout12-tx-Title-and-Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide2")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1154")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL12")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id148")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1158")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1157")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1155")
    child_4.text = "ppLayoutText"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1156")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id149")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1166")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1161")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1160")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1159")
    child_6.text = "Text(2)"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1165")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1165")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1164")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1162")
    child_8.text = "For ppLayoutText"
    child_7.append( child_8 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1163")
    child_7.append( child_8 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL13():
    
    """Build Element draw:page for Master1-PPL13 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-258")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout13-twoColTx-Title-and-2-Column-Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide3")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1168")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL13")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id150")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1172")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1171")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1169")
    child_4.text = "ppLayoutTwoColumnText"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1170")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id151")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1180")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1175")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1174")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1173")
    child_6.text = "Text(2)"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1179")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1179")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1178")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1176")
    child_8.text = "For ppLayoutTwoColumnText"
    child_7.append( child_8 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1177")
    child_7.append( child_8 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id152")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1188")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1183")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1182")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1181")
    child_6.text = "Text(3)"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1187")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1187")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1186")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1184")
    child_8.text = "For ppLayoutTwoColumnText"
    child_7.append( child_8 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1185")
    child_7.append( child_8 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL2():
    
    """Build Element draw:page for Master1-PPL2 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-259")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout2-obj-Title-and-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide4")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1190")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL2")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id153")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1194")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1193")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1191")
    child_4.text = "ppLayoutObject"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1192")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id154")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1195")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "3.125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "2.91667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "2.66233in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image1.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL14():
    
    """Build Element draw:page for Master1-PPL14 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-260")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout14-txOverObj-Title-and-Text-over-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide5")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1197")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL14")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id155")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1201")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1200")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1198")
    child_4.text = "ppLayoutTextOverObject"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1199")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id156")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1209")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1204")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1203")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1202")
    child_6.text = "Text(2)"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1208")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1208")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1207")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1205")
    child_8.text = "For ppLayoutTextOverObject"
    child_7.append( child_8 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1206")
    child_7.append( child_8 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id157")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1210")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.18981in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.40509in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image2.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL15():
    
    """Build Element draw:page for Master1-PPL15 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-261")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout15-txAndObj-Title,-Text,-and-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide6")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1212")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL15")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id158")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1216")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1215")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1213")
    child_4.text = "ppLayoutTextAndObject"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1214")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id159")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1224")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1219")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1218")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1217")
    child_6.text = "Text(2)"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1223")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1223")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1222")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1220")
    child_8.text = "For ppLayoutTextAndObject"
    child_7.append( child_8 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1221")
    child_7.append( child_8 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id160")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1225")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "3.125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.20833in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "2.66233in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image3.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL4():
    
    """Build Element draw:page for Master1-PPL4 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-262")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout4-twoObj-Two-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide7")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1227")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL4")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id161")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1231")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1230")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1228")
    child_4.text = "ppLayoutTwoObjects"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1229")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id162")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1232")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "3.125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.625in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "2.66233in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image4.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id163")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1233")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "3.125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.20833in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "2.66233in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image5.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL16():
    
    """Build Element draw:page for Master1-PPL16 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-263")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout16-objAndTx-Title,-Content-and-Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide8")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1235")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL16")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id164")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1239")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1238")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1236")
    child_4.text = "ppLayoutObjectAndText"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1237")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id165")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1240")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "3.125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.625in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "2.66233in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image6.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id166")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1248")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1243")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1242")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1241")
    child_6.text = "Text(3)"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1247")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1247")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1246")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1244")
    child_8.text = "For ppLayoutObjectAndText"
    child_7.append( child_8 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1245")
    child_7.append( child_8 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL17():
    
    """Build Element draw:page for Master1-PPL17 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-264")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout17-txAndTwoObj-Title,-Text,-and-2-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide9")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1250")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL17")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id167")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1254")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1253")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1251")
    child_4.text = "ppLayoutTextAndTwoObjects"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1252")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id168")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1262")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1257")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1256")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1255")
    child_6.text = "Text(2)"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1261")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1261")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1260")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1258")
    child_8.text = "For ppLayoutTextAndTwoObjects"
    child_7.append( child_8 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1259")
    child_7.append( child_8 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id169")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1263")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.1875in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.69792in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image7.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id170")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1264")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.18981in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.69676in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image8.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL18():
    
    """Build Element draw:page for Master1-PPL18 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-265")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout18-objAndTwoObj-Title,-Content,-and-2-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide10")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1266")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL18")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id171")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1270")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1269")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1267")
    child_4.text = "ppLayoutObjectAndTwoObjects"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1268")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id172")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1271")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "3.125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.625in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "2.66233in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image9.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id173")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1272")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.1875in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.69792in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image10.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id174")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 7")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1273")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.18981in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.69676in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image11.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL19():
    
    """Build Element draw:page for Master1-PPL19 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-266")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout19-objOverTx-Title-and-Content-over-Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide11")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1275")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL19")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id175")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1279")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1278")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1276")
    child_4.text = "ppLayoutObjectOverText"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1277")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id176")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1280")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.1875in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.40625in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image12.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id177")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1288")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1283")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1282")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1281")
    child_6.text = "Text(3)"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1287")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1287")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1286")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1284")
    child_8.text = "For ppLayoutObjectOverText"
    child_7.append( child_8 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1285")
    child_7.append( child_8 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL20():
    
    """Build Element draw:page for Master1-PPL20 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-267")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout20-fourObj-Title-and-4-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide12")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1290")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL20")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id178")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1294")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1293")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1291")
    child_4.text = "ppLayoutFourObjects"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1292")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id179")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1295")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.1875in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "1.11458in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image13.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id180")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 7")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1296")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.1875in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.69792in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image14.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id181")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 8")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1297")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.18981in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "1.11343in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image15.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id182")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 9")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1298")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.18981in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.69676in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image16.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL21():
    
    """Build Element draw:page for Master1-PPL21 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-268")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout21-twoObjAndObj-Title,-2-Content-and-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide13")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1300")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL21")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id183")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1304")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1303")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1301")
    child_4.text = "ppLayoutTwoObjectsAndObject"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1302")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id184")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1305")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.1875in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "1.11458in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image17.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id185")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1306")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.18981in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "1.11343in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image18.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id186")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 7")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1307")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "3.125in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.20833in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "2.66233in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image19.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL22():
    
    """Build Element draw:page for Master1-PPL22 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-269")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout22-twoObjAndTx-Title,-2-Content-and-Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide14")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1309")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL22")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id187")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1313")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1312")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1310")
    child_4.text = "ppLayoutTwoObjectsAndText"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1311")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id188")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1314")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.1875in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "1.11458in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image20.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id189")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1315")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.18981in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "1.11343in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image21.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id190")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1323")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1318")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1317")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1316")
    child_6.text = "Text(4)"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1322")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1322")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1321")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1319")
    child_8.text = "For ppLayoutTwoObjectsAndText"
    child_7.append( child_8 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1320")
    child_7.append( child_8 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL23():
    
    """Build Element draw:page for Master1-PPL23 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-270")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout23-twoObjOverTx-Title-and-2-Content-over-Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide15")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1325")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL23")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id191")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1329")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1328")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1326")
    child_4.text = "ppLayoutTwoObjectsOverText"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1327")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id192")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1330")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.1875in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "1.11458in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image22.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id193")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "graphic")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1331")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-height", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}rel-width", "scale")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.1875in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.69792in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}image" )
    child_2.set("{http://www.w3.org/1999/xlink}actuate", "onLoad")
    child_2.set("{http://www.w3.org/1999/xlink}href", "media/image23.png")
    child_2.set("{http://www.w3.org/1999/xlink}show", "embed")
    child_2.set("{http://www.w3.org/1999/xlink}type", "simple")
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id194")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1339")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1334")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1333")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1332")
    child_6.text = "Text(4)"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1338")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1338")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1337")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1335")
    child_8.text = "For ppLayoutTwoObjectsOverText"
    child_7.append( child_8 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1336")
    child_7.append( child_8 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def draw_8_page_Master1_PPL24():
    
    """Build Element draw:page for Master1-PPL24 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "Slide-271")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}master-page-name", "Master1-Layout24-tbl-Title-and-Table")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide16")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1341")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}presentation-page-layout-name", "Master1-PPL24")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id195")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1345")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "1.25in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "0.30035in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1344")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1342")
    child_4.text = "ppLayoutTable"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1343")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id196")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Table Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "table")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "true")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1346")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def presentation_8_settings_presentation_8_settings():
    
    """Build Element presentation:settings for presentation:settings """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}settings" )
    
    
    return elem



# Set values in func_quick_lookupD
func_quick_lookupD["Master1-PPL1"] = draw_8_page_Master1_PPL1
func_quick_lookupD["Master1-PPL12"] = draw_8_page_Master1_PPL12
func_quick_lookupD["Master1-PPL13"] = draw_8_page_Master1_PPL13
func_quick_lookupD["Master1-PPL14"] = draw_8_page_Master1_PPL14
func_quick_lookupD["Master1-PPL15"] = draw_8_page_Master1_PPL15
func_quick_lookupD["Master1-PPL16"] = draw_8_page_Master1_PPL16
func_quick_lookupD["Master1-PPL17"] = draw_8_page_Master1_PPL17
func_quick_lookupD["Master1-PPL18"] = draw_8_page_Master1_PPL18
func_quick_lookupD["Master1-PPL19"] = draw_8_page_Master1_PPL19
func_quick_lookupD["Master1-PPL2"] = draw_8_page_Master1_PPL2
func_quick_lookupD["Master1-PPL20"] = draw_8_page_Master1_PPL20
func_quick_lookupD["Master1-PPL21"] = draw_8_page_Master1_PPL21
func_quick_lookupD["Master1-PPL22"] = draw_8_page_Master1_PPL22
func_quick_lookupD["Master1-PPL23"] = draw_8_page_Master1_PPL23
func_quick_lookupD["Master1-PPL24"] = draw_8_page_Master1_PPL24
func_quick_lookupD["Master1-PPL4"] = draw_8_page_Master1_PPL4
func_quick_lookupD["presentation:settings"] = presentation_8_settings_presentation_8_settings




# Set values in master_page_name_lookupD
master_page_name_lookupD["Master1-PPL1"] = "Master1-Layout1-title-Title-Slide"
master_page_name_lookupD["Master1-PPL12"] = "Master1-Layout12-tx-Title-and-Text"
master_page_name_lookupD["Master1-PPL13"] = "Master1-Layout13-twoColTx-Title-and-2-Column-Text"
master_page_name_lookupD["Master1-PPL14"] = "Master1-Layout14-txOverObj-Title-and-Text-over-Content"
master_page_name_lookupD["Master1-PPL15"] = "Master1-Layout15-txAndObj-Title,-Text,-and-Content"
master_page_name_lookupD["Master1-PPL16"] = "Master1-Layout16-objAndTx-Title,-Content-and-Text"
master_page_name_lookupD["Master1-PPL17"] = "Master1-Layout17-txAndTwoObj-Title,-Text,-and-2-Content"
master_page_name_lookupD["Master1-PPL18"] = "Master1-Layout18-objAndTwoObj-Title,-Content,-and-2-Content"
master_page_name_lookupD["Master1-PPL19"] = "Master1-Layout19-objOverTx-Title-and-Content-over-Text"
master_page_name_lookupD["Master1-PPL2"] = "Master1-Layout2-obj-Title-and-Content"
master_page_name_lookupD["Master1-PPL20"] = "Master1-Layout20-fourObj-Title-and-4-Content"
master_page_name_lookupD["Master1-PPL21"] = "Master1-Layout21-twoObjAndObj-Title,-2-Content-and-Content"
master_page_name_lookupD["Master1-PPL22"] = "Master1-Layout22-twoObjAndTx-Title,-2-Content-and-Text"
master_page_name_lookupD["Master1-PPL23"] = "Master1-Layout23-twoObjOverTx-Title-and-2-Content-over-Text"
master_page_name_lookupD["Master1-PPL24"] = "Master1-Layout24-tbl-Title-and-Table"
master_page_name_lookupD["Master1-PPL4"] = "Master1-Layout4-twoObj-Two-Content"


# Set values in layout_page_name_lookupD
layout_page_name_lookupD["Master1-Layout1-title-Title-Slide"] = "Master1-PPL1"
layout_page_name_lookupD["Master1-Layout12-tx-Title-and-Text"] = "Master1-PPL12"
layout_page_name_lookupD["Master1-Layout13-twoColTx-Title-and-2-Column-Text"] = "Master1-PPL13"
layout_page_name_lookupD["Master1-Layout14-txOverObj-Title-and-Text-over-Content"] = "Master1-PPL14"
layout_page_name_lookupD["Master1-Layout15-txAndObj-Title,-Text,-and-Content"] = "Master1-PPL15"
layout_page_name_lookupD["Master1-Layout16-objAndTx-Title,-Content-and-Text"] = "Master1-PPL16"
layout_page_name_lookupD["Master1-Layout17-txAndTwoObj-Title,-Text,-and-2-Content"] = "Master1-PPL17"
layout_page_name_lookupD["Master1-Layout18-objAndTwoObj-Title,-Content,-and-2-Content"] = "Master1-PPL18"
layout_page_name_lookupD["Master1-Layout19-objOverTx-Title-and-Content-over-Text"] = "Master1-PPL19"
layout_page_name_lookupD["Master1-Layout2-obj-Title-and-Content"] = "Master1-PPL2"
layout_page_name_lookupD["Master1-Layout20-fourObj-Title-and-4-Content"] = "Master1-PPL20"
layout_page_name_lookupD["Master1-Layout21-twoObjAndObj-Title,-2-Content-and-Content"] = "Master1-PPL21"
layout_page_name_lookupD["Master1-Layout22-twoObjAndTx-Title,-2-Content-and-Text"] = "Master1-PPL22"
layout_page_name_lookupD["Master1-Layout23-twoObjOverTx-Title-and-2-Content-over-Text"] = "Master1-PPL23"
layout_page_name_lookupD["Master1-Layout24-tbl-Title-and-Table"] = "Master1-PPL24"
layout_page_name_lookupD["Master1-Layout4-twoObj-Two-Content"] = "Master1-PPL4"

if __name__ == "__main__":
    print( master_page_name_lookupD["Master1-PPL24"] )
