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


def get_pres_class_obj(presObj, placeholder_elem, master_elem_draw_frame):
    """
    Depending on presentation:object value of placeholder_elem, get one of:
    object, subtitle, outline, footer, title, page-number, table, date-time
    """
    tree_styles = presObj.styles_xml_obj
    
    pres_object_name = placeholder_elem.get( NS('presentation:object', tree_styles.rev_nsOD) )
    
    if pres_object_name == 'title':
        
        draw_frame = copy_master_elem.copy(presObj, master_elem_draw_frame )
        
        return draw_frame
