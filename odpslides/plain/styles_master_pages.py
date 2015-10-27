
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


def draw_8_layer_set():
    
    """Build Element draw:layer-set """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}layer-set" )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}layer" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Master1-bg")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}protected", "true")
    elem.append( child )
    
    
    return elem

def style_8_master_page_Master1_PPL1():
    
    """Build Element style:master-page for Master1-PPL1 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a34")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout1-title-Title-Slide")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a38")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a37")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a35")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a36")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Subtitle 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "subtitle")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a42")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a41")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a39")
    child_4.text = "Click to edit Master subtitle style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a40")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id7")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a47")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a46")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a43")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a44")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a45")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id8")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a50")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a49")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a48")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id9")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a54")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a53")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a51")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a52")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL2():
    
    """Build Element style:master-page for Master1-PPL2 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a55")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout2-obj-Title-and-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id10")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a59")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a58")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a56")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a57")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id11")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a76")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a62")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a61")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a60")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a65")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a65")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a64")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a63")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a68")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a68")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a68")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a67")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a66")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a71")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a71")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a71")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a71")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a70")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a69")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a75")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a75")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a75")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a75")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a75")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a74")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a72")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a73")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id12")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a81")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a80")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a77")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a78")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a79")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id13")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a84")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a83")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a82")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id14")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a88")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a87")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a85")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a86")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL4():
    
    """Build Element style:master-page for Master1-PPL4 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a110")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout4-twoObj-Two-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id20")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a114")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a113")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a111")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a112")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id21")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a131")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a117")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a116")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a115")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a120")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a120")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a119")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a118")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a123")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a123")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a123")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a122")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a121")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a126")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a126")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a126")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a126")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a125")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a124")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a130")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a130")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a130")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a130")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a130")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a129")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a127")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a128")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id22")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a148")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a134")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a133")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a132")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a137")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a137")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a136")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a135")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a140")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a140")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a140")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a139")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a138")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a143")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a143")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a143")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a143")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a142")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a141")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a147")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a147")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a147")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a147")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a147")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a146")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a144")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a145")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id23")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a153")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a152")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a149")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a150")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a151")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id24")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a156")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a155")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a154")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id25")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a160")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a159")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a157")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a158")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL12():
    
    """Build Element style:master-page for Master1-PPL12 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a380")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout12-tx-Title-and-Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id63")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a384")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a383")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a381")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a382")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id64")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a401")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a387")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a386")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a385")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a390")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a390")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a389")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a388")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a393")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a393")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a393")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a392")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a391")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a396")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a396")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a396")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a396")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a395")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a394")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a400")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a400")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a400")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a400")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a400")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a399")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a397")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a398")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id65")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a406")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a405")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a402")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a403")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a404")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id66")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a409")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a408")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a407")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id67")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a413")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a412")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a410")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a411")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL13():
    
    """Build Element style:master-page for Master1-PPL13 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a414")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout13-twoColTx-Title-and-2-Column-Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id68")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a418")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a417")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a415")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a416")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id69")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a435")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a421")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a420")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a419")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a424")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a424")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a423")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a422")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a427")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a427")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a427")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a426")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a425")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a430")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a430")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a430")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a430")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a429")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a428")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a434")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a434")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a434")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a434")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a434")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a433")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a431")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a432")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id70")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a452")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a438")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a437")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a436")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a441")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a441")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a440")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a439")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a444")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a444")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a444")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a443")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a442")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a447")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a447")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a447")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a447")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a446")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a445")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a451")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a451")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a451")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a451")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a451")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a450")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a448")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a449")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id71")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a457")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a456")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a453")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a454")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a455")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id72")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a460")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a459")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a458")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id73")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a464")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a463")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a461")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a462")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL14():
    
    """Build Element style:master-page for Master1-PPL14 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a465")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout14-txOverObj-Title-and-Text-over-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id74")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a469")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a468")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a466")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a467")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id75")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a486")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a472")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a471")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a470")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a475")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a475")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a474")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a473")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a478")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a478")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a478")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a477")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a476")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a481")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a481")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a481")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a481")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a480")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a479")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a485")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a485")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a485")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a485")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a485")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a484")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a482")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a483")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id76")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a503")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a489")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a488")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a487")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a492")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a492")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a491")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a490")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a495")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a495")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a495")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a494")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a493")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a498")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a498")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a498")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a498")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a497")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a496")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a502")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a502")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a502")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a502")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a502")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a501")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a499")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a500")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id77")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a508")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a507")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a504")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a505")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a506")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id78")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a511")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a510")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a509")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id79")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a515")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a514")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a512")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a513")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL15():
    
    """Build Element style:master-page for Master1-PPL15 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a516")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout15-txAndObj-Title,-Text,-and-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id80")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a520")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a519")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a517")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a518")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id81")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a537")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a523")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a522")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a521")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a526")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a526")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a525")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a524")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a529")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a529")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a529")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a528")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a527")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a532")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a532")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a532")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a532")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a531")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a530")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a536")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a536")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a536")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a536")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a536")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a535")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a533")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a534")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id82")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a554")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a540")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a539")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a538")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a543")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a543")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a542")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a541")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a546")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a546")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a546")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a545")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a544")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a549")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a549")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a549")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a549")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a548")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a547")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a553")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a553")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a553")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a553")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a553")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a552")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a550")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a551")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id83")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a559")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a558")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a555")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a556")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a557")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id84")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a562")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a561")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a560")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id85")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a566")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a565")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a563")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a564")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL16():
    
    """Build Element style:master-page for Master1-PPL16 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a567")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout16-objAndTx-Title,-Content-and-Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id86")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a571")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a570")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a568")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a569")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id87")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a588")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a574")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a573")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a572")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a577")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a577")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a576")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a575")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a580")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a580")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a580")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a579")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a578")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a583")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a583")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a583")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a583")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a582")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a581")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a587")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a587")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a587")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a587")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a587")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a586")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a584")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a585")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id88")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a605")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a591")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a590")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a589")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a594")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a594")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a593")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a592")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a597")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a597")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a597")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a596")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a595")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a600")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a600")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a600")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a600")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a599")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a598")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a604")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a604")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a604")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a604")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a604")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a603")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a601")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a602")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id89")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a610")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a609")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a606")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a607")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a608")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id90")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a613")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a612")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a611")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id91")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a617")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a616")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a614")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a615")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL17():
    
    """Build Element style:master-page for Master1-PPL17 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a618")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout17-txAndTwoObj-Title,-Text,-and-2-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id92")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a622")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a621")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a619")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a620")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id93")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a639")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a625")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a624")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a623")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a628")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a628")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a627")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a626")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a631")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a631")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a631")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a630")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a629")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a634")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a634")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a634")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a634")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a633")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a632")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a638")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a638")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a638")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a638")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a638")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a637")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a635")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a636")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id94")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a656")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a642")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a641")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a640")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a645")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a645")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a644")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a643")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a648")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a648")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a648")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a647")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a646")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a651")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a651")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a651")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a651")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a650")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a649")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a655")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a655")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a655")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a655")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a655")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a654")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a652")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a653")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id95")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a673")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a659")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a658")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a657")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a662")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a662")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a661")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a660")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a665")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a665")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a665")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a664")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a663")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a668")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a668")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a668")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a668")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a667")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a666")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a672")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a672")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a672")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a672")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a672")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a671")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a669")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a670")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id96")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a678")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a677")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a674")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a675")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a676")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id97")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a681")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a680")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a679")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id98")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 7")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a685")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a684")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a682")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a683")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL18():
    
    """Build Element style:master-page for Master1-PPL18 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a686")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout18-objAndTwoObj-Title,-Content,-and-2-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id99")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a690")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a689")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a687")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a688")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id100")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a707")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a693")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a692")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a691")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a696")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a696")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a695")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a694")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a699")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a699")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a699")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a698")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a697")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a702")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a702")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a702")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a702")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a701")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a700")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a706")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a706")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a706")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a706")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a706")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a705")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a703")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a704")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id101")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a724")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a710")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a709")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a708")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a713")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a713")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a712")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a711")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a716")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a716")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a716")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a715")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a714")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a719")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a719")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a719")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a719")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a718")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a717")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a723")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a723")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a723")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a723")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a723")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a722")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a720")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a721")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id102")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a741")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a727")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a726")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a725")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a730")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a730")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a729")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a728")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a733")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a733")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a733")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a732")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a731")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a736")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a736")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a736")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a736")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a735")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a734")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a740")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a740")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a740")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a740")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a740")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a739")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a737")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a738")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id103")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a746")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a745")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a742")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a743")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a744")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id104")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a749")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a748")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a747")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id105")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 7")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a753")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a752")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a750")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a751")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL19():
    
    """Build Element style:master-page for Master1-PPL19 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a754")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout19-objOverTx-Title-and-Content-over-Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id106")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a758")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a757")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a755")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a756")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id107")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a775")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a761")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a760")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a759")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a764")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a764")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a763")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a762")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a767")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a767")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a767")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a766")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a765")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a770")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a770")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a770")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a770")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a769")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a768")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a774")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a774")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a774")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a774")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a774")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a773")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a771")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a772")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id108")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a792")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a778")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a777")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a776")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a781")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a781")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a780")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a779")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a784")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a784")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a784")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a783")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a782")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a787")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a787")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a787")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a787")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a786")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a785")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a791")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a791")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a791")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a791")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a791")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a790")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a788")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a789")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id109")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a797")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a796")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a793")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a794")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a795")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id110")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a800")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a799")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a798")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id111")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a804")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a803")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a801")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a802")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL20():
    
    """Build Element style:master-page for Master1-PPL20 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a805")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout20-fourObj-Title-and-4-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id112")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a809")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a808")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a806")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a807")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id113")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a826")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a812")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a811")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a810")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a815")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a815")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a814")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a813")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a818")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a818")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a818")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a817")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a816")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a821")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a821")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a821")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a821")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a820")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a819")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a825")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a825")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a825")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a825")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a825")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a824")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a822")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a823")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id114")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a843")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a829")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a828")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a827")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a832")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a832")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a831")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a830")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a835")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a835")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a835")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a834")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a833")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a838")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a838")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a838")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a838")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a837")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a836")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a842")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a842")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a842")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a842")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a842")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a841")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a839")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a840")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id115")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a860")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a846")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a845")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a844")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a849")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a849")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a848")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a847")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a852")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a852")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a852")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a851")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a850")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a855")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a855")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a855")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a855")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a854")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a853")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a859")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a859")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a859")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a859")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a859")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a858")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a856")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a857")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id116")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a877")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a863")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a862")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a861")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a866")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a866")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a865")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a864")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a869")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a869")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a869")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a868")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a867")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a872")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a872")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a872")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a872")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a871")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a870")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a876")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a876")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a876")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a876")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a876")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a875")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a873")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a874")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id117")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a882")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a881")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a878")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a879")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a880")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id118")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 7")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a885")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a884")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a883")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id119")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 8")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a889")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a888")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a886")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a887")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL21():
    
    """Build Element style:master-page for Master1-PPL21 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a890")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout21-twoObjAndObj-Title,-2-Content-and-Content")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id120")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a894")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a893")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a891")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a892")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id121")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a911")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a897")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a896")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a895")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a900")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a900")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a899")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a898")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a903")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a903")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a903")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a902")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a901")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a906")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a906")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a906")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a906")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a905")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a904")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a910")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a910")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a910")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a910")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a910")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a909")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a907")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a908")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id122")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a928")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a914")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a913")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a912")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a917")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a917")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a916")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a915")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a920")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a920")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a920")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a919")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a918")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a923")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a923")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a923")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a923")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a922")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a921")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a927")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a927")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a927")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a927")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a927")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a926")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a924")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a925")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id123")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a945")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a931")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a930")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a929")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a934")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a934")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a933")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a932")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a937")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a937")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a937")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a936")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a935")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a940")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a940")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a940")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a940")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a939")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a938")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a944")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a944")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a944")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a944")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a944")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a943")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a941")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a942")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id124")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a950")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a949")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a946")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a947")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a948")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id125")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a953")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a952")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a951")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id126")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 7")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a957")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a956")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a954")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a955")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL22():
    
    """Build Element style:master-page for Master1-PPL22 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a958")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout22-twoObjAndTx-Title,-2-Content-and-Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id127")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a962")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a961")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a959")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a960")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id128")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a979")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a965")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a964")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a963")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a968")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a968")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a967")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a966")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a971")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a971")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a971")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a970")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a969")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a974")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a974")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a974")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a974")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a973")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a972")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a978")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a978")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a978")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a978")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a978")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a977")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a975")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a976")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id129")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a996")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a982")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a981")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a980")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a985")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a985")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a984")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a983")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a988")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a988")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a988")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a987")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a986")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a991")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a991")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a991")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a991")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a990")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a989")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a995")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a995")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a995")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a995")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a995")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a994")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a992")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a993")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id130")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1013")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a999")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a998")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a997")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1002")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1002")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1001")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1000")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1005")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1005")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1005")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1004")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1003")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1008")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1008")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1008")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1008")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1007")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1006")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1012")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1012")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1012")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1012")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1012")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1011")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1009")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1010")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id131")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1018")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1017")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1014")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a1015")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1016")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id132")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1021")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1020")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1019")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id133")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 7")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1025")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1024")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1022")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1023")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL23():
    
    """Build Element style:master-page for Master1-PPL23 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1026")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout23-twoObjOverTx-Title-and-2-Content-over-Text")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id134")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1030")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1029")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1027")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1028")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id135")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1047")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1033")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1032")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1031")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1036")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1036")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1035")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1034")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1039")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1039")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1039")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1038")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1037")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1042")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1042")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1042")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1042")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1041")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1040")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1046")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1046")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1046")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1046")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1046")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1045")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1043")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1044")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id136")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Content Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "object")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1064")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39063in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "4.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "5.08333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1050")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1049")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1048")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1053")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1053")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1052")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1051")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1056")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1056")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1056")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1055")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1054")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1059")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1059")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1059")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1059")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1058")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1057")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1063")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1063")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1063")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1063")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1063")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1062")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1060")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1061")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id137")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Text Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "outline")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1081")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "2.39236in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "4.30729in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1067")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1066")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1065")
    child_6.text = "Click to edit Master text styles"
    child_5.append( child_6 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1070")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1070")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1069")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_8.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1068")
    child_8.text = "Second level"
    child_7.append( child_8 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1073")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1073")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1073")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1072")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_10.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1071")
    child_10.text = "Third level"
    child_9.append( child_10 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1076")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1076")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1076")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1076")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1075")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_12.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1074")
    child_12.text = "Fourth level"
    child_11.append( child_12 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1080")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1080")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_5.append( child_6 )
    
    child_7 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_7.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1080")
    child_6.append( child_7 )
    
    child_8 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_7.append( child_8 )
    
    child_9 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_9.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1080")
    child_8.append( child_9 )
    
    child_10 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_9.append( child_10 )
    
    child_11 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_11.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1080")
    child_10.append( child_11 )
    
    child_12 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_11.append( child_12 )
    
    child_13 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_13.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1079")
    child_12.append( child_13 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1077")
    child_14.text = "Fifth level"
    child_13.append( child_14 )
    
    child_14 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_14.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1078")
    child_13.append( child_14 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id138")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1086")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1085")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1082")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a1083")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1084")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id139")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 6")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1089")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1088")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1087")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id140")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 7")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1093")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1092")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1090")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1091")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem

def style_8_master_page_Master1_PPL24():
    
    """Build Element style:master-page for Master1-PPL24 """
    
    elem = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page" )
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}style-name", "a1094")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name", "Master1-Layout24-tbl-Title-and-Table")
    elem.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}page-layout-name", "pageLayout1")
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id141")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Title 1")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "title")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1098")
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
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1097")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1095")
    child_4.text = "Click to edit Master title style"
    child_3.append( child_4 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1096")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id142")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Table Placeholder 2")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "table")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1102")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "4.94965in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "9in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "1.75in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1101")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item" )
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1100")
    child_4.append( child_5 )
    
    child_6 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_6.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1099")
    child_5.append( child_6 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id143")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Date Placeholder 3")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "date-time")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1107")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "0.5in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1106")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1103")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}date" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}data-style-name", "a1104")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1105")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id144")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Footer Placeholder 4")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "footer")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1110")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "3.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "3.41667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1109")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1108")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    child = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}frame" )
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id", "id145")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name", "Slide Number Placeholder 5")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}class", "page-number")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}placeholder", "false")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}style-name", "a1114")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height", "0.39931in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width", "2.33333in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x", "7.16667in")
    child.set("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y", "6.95139in")
    elem.append( child )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box" )
    child.append( child_2 )
    
    child_3 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p" )
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}cond-style-name", "")
    child_3.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1113")
    child_2.append( child_3 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1111")
    child_3.append( child_4 )
    
    child_5 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}page-number" )
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:style:1.0}num-format", "1")
    child_5.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}fixed", "false")
    child_4.append( child_5 )
    
    child_4 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span" )
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}class-names", "")
    child_4.set("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name", "a1112")
    child_3.append( child_4 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}title" )
    child.append( child_2 )
    
    child_2 = ET.Element( "{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}desc" )
    child.append( child_2 )
    
    
    return elem



# Set values in func_quick_lookupD
func_quick_lookupD["Master1-PPL1"] = style_8_master_page_Master1_PPL1
func_quick_lookupD["Master1-PPL12"] = style_8_master_page_Master1_PPL12
func_quick_lookupD["Master1-PPL13"] = style_8_master_page_Master1_PPL13
func_quick_lookupD["Master1-PPL14"] = style_8_master_page_Master1_PPL14
func_quick_lookupD["Master1-PPL15"] = style_8_master_page_Master1_PPL15
func_quick_lookupD["Master1-PPL16"] = style_8_master_page_Master1_PPL16
func_quick_lookupD["Master1-PPL17"] = style_8_master_page_Master1_PPL17
func_quick_lookupD["Master1-PPL18"] = style_8_master_page_Master1_PPL18
func_quick_lookupD["Master1-PPL19"] = style_8_master_page_Master1_PPL19
func_quick_lookupD["Master1-PPL2"] = style_8_master_page_Master1_PPL2
func_quick_lookupD["Master1-PPL20"] = style_8_master_page_Master1_PPL20
func_quick_lookupD["Master1-PPL21"] = style_8_master_page_Master1_PPL21
func_quick_lookupD["Master1-PPL22"] = style_8_master_page_Master1_PPL22
func_quick_lookupD["Master1-PPL23"] = style_8_master_page_Master1_PPL23
func_quick_lookupD["Master1-PPL24"] = style_8_master_page_Master1_PPL24
func_quick_lookupD["Master1-PPL4"] = style_8_master_page_Master1_PPL4
func_quick_lookupD["draw_8_layer_set"] = draw_8_layer_set



if __name__ == "__main__":
    print( func_quick_lookupD["Master1-PPL24"]() )