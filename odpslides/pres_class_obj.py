# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
"""
Build each of the presentation:class objects.
(i.e. object, subtitle, outline, footer, title, page-number, table, date-time)
"""
from odpslides.find_obj import find_elem_w_attrib, elem_set, NS_attrib, NS
import odpslides.copy_master_elem as copy_master_elem


def get_presentation_class_obj(presObj, placeholder_elem, master_elem_draw_frame,
                                   **inpD):
    """
    Depending on presentation:object value of placeholder_elem, get one of:
    object, subtitle, outline, footer, title, page-number, table, date-time
    
    :param presObj: Presentation object
    :type  presObj: object
    :param placeholder_elem: xml Element with placeholder information
    :type  placeholder_elem: object
    :param master_elem_draw_frame: xml Element of draw:frame from style:master-page in styles.xml
    :type  master_elem_draw_frame: object
    :param **inpD: any input information for class object
    :type  **inpD: dict
    :return: None
    :rtype: None
    
    """
    tree_styles = presObj.styles_xml_obj
    tree_content = presObj.content_xml_obj
    
    pres_object_name = placeholder_elem.get( NS('presentation:object', tree_styles.rev_nsOD) )
    
    if pres_object_name == 'title':
        draw_frame = copy_master_elem.copy(presObj, master_elem_draw_frame )
        if 'title' in inpD:
            #print('Found title in inpD with value =',inpD['title'])
            text_span = draw_frame.find( 'draw:text-box/text:p/text:span', tree_content.rev_nsOD )
            
            if text_span is not None:
                text_span.text = inpD['title']
        
        return draw_frame
    
    elif pres_object_name == 'subtitle':
        draw_frame = copy_master_elem.copy(presObj, master_elem_draw_frame )
        if 'subtitle' in inpD:
            #print('Found title in inpD with value =',inpD['title'])
            text_span = draw_frame.find( 'draw:text-box/text:p/text:span', tree_content.rev_nsOD )
            
            if text_span is not None:
                text_span.text = inpD['subtitle']
        
        return draw_frame

    return None
    
    