# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
"""
Copy a master element by first making a deepcopy, then replacing/renameing master style-name
values with new values (e.g. change "a123" to "a1000")
"""
import sys
from collections import OrderedDict
from copy import deepcopy

if sys.version_info < (3,):
    import odpslides.ElementTree_27OD as ET
else:
    import odpslides.ElementTree_34OD as ET

from odpslides.find_obj import find_elem_w_attrib, elem_set, NS_attrib, NS
from odpslides.master_styles import  get_next_draw_id


def new_draw_page(presObj, master_elem): # master_elem is master-page Element
    """
    Starts a new slide with a draw:page Element.
    """
    tree_styles = presObj.styles_xml_obj
    tree_content = presObj.content_xml_obj
    
    # Build new style element
    old_aval = master_elem.get( NS('draw:style-name', tree_styles.rev_nsOD) )
    new_style_obj = deepcopy( presObj.style_name_elem_from_nameD[old_aval] )
    print('In new_draw_page, new_style_obj =',new_style_obj)    
    
    new_a_val = presObj.add_new_a_style( new_style_obj )
    
    # turn style:master-page into draw:page 
    #new_style_obj.clear_attrib()
    #new_style_obj.tag = NS('draw:page', tree_content.rev_nsOD)
    new_style_obj.set( NS('style:family', tree_content.rev_nsOD), "drawing-page")
    
    
    # make sure qnameOD is up to date for new_style_obj
    tree_content.acclimate_new_elem( new_style_obj )
    
    # Get master name 
    master_name = master_elem.get( NS('style:name', tree_styles.rev_nsOD) )
    
    # Create attributes for new page 
    attribOD = OrderedDict()
    attribOD[ NS('draw:name',tree_content.rev_nsOD) ] = "Slide%i"%( len(presObj.slideL)+1, )
    attribOD[ NS('draw:style-name',tree_content.rev_nsOD) ] = new_a_val
    attribOD[ NS('draw:master-page-name',tree_content.rev_nsOD) ] = master_name
    attribOD[ NS('presentation:presentation-page-layout-name',tree_content.rev_nsOD) ] = presObj.matching_layout_nameD[master_name]
    attribOD[ NS('draw:id',tree_content.rev_nsOD) ] = get_next_draw_id()
    
    #draw_page = ET.Element( NS('draw:page',tree_content.rev_nsOD), attrib=attribOD )
    draw_page = tree_content.new_elem( 'draw:page', attribOD=attribOD)
    #print( draw_page )
    #print( attribOD )
    #print()
    
    return draw_page
    

def copy(presObj, master_elem_draw_frame):
    """
    Used to make content from draw:frame Elements in Master Page.
    """
    
    new_elem = deepcopy( master_elem_draw_frame )
    tree_styles = presObj.styles_xml_obj
    tree_content = presObj.content_xml_obj
    
    print('IN-COPY', new_elem)
    
    # if master has duplicate style ref, make new refs duplicate also
    duplicateD = {} # index=old "a123", value= new "a123"
    
    for sub_elem in new_elem.iter():
        for aname,aval in sub_elem.items():
            if aname.endswith('}style-name') and aval.startswith('a'):
                if aval in duplicateD:
                    new_a_val = duplicateD[aval]
                else:
                    new_style_obj = deepcopy( presObj.style_name_elem_from_nameD[aval] )
                    new_a_val = presObj.add_new_a_style( new_style_obj )
                    
                    new_style_obj.set( NS('style:name', tree_styles.rev_nsOD), new_a_val )
                    
                    # make sure qnameOD is up to date for new_style_obj
                    tree_content.acclimate_new_elem( new_style_obj )
                    
                sub_elem.set( aname, new_a_val ) # the new style will be a match of master
                
                duplicateD[aval] = new_a_val
        
            if aname == '{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}id' and aval.startswith('id'):
                new_id_val = get_next_draw_id()
                sub_elem.set(aname, new_id_val)        
    
    # make sure that qnameOD is up to date for new_elem
    tree_content.acclimate_new_elem( new_elem )
    
    return new_elem
