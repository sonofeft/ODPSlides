# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
"""
Build the content.xml elements.
Fill the Presentation objects lists: new_styleL and new_draw_pageL
"""
from collections import OrderedDict
from odpslides.find_obj import find_elem_w_attrib, elem_set, NS_attrib, NS
from odpslides.pres_class_obj import get_pres_class_obj
from odpslides.copy_master_elem import new_draw_page

def add_title_chart( presObj, title='My Title', subtitle='My Subtitle' ):
    """
    Get some reference style:style and draw:page elements from ref template.
    Add them as attributes to presObj.
    
    Assume that get_master_styles has been called from presentation.py
    
    :param presObj: a Presentation object from presentation.py
    :type  presObj: Presentation
    :return: None
    :rtype: None
    """
    master_name = "Master1-Layout1-title-Title-Slide"
    print('Adding %s'%master_name)
    
    master_elem = presObj.master_page_elem_from_nameD[ master_name ] # from ref styles.xml (master-page Element)
    draw_page_elem = presObj.draw_page_elem_from_nameD[ master_name ] # from ref content.xml
    layout_name = presObj.matching_layout_nameD[ master_name ]
    layout_elem = presObj.page_layout_elem_from_nameD[ layout_name ]
    
    tree_styles = presObj.styles_xml_obj
    placeholder_elemL = layout_elem.findall( NS('presentation:placeholder', tree_styles.rev_nsOD)  )
    master_elem_draw_frameL = master_elem.findall( NS('draw:frame', tree_styles.rev_nsOD) )
    
    # Build new draw:page
    draw_page = new_draw_page(presObj, master_elem)
    
    for i,placeholder_elem in enumerate(placeholder_elemL):
        master_elem_draw_frame = master_elem_draw_frameL[i]
        print( placeholder_elem.tag,  master_elem_draw_frame.tag)
        
        draw_frame = get_pres_class_obj(presObj, placeholder_elem, master_elem_draw_frame)
        
        if draw_frame is not None:
            draw_page.append( draw_frame )
        
    
    presObj.slideL.append( draw_page )
    
    for elem in draw_page.iter():
        if elem.tag == '{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page':
            print('WARN', elem)
            
        for atr,val in elem.items():
            if atr == '{urn:oasis:names:tc:opendocument:xmlns:style:1.0}master-page':
                print('WARN', atr,val)
        
    