# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
"""
Build each of the presentation:class objects.
(i.e. object, subtitle, outline, footer, title, page-number, table, date-time)
"""
from copy import deepcopy

from color_utils import getValidHexStr
from odpslides.find_obj import find_elem_w_attrib, elem_set, NS_attrib, NS
import odpslides.copy_master_elem as copy_master_elem

COLOR_TAG = '{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}color'
TEXT_STYLE_NAME_ATTR_TAG = '{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name'
TEXT_SPAN_TAG = '{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span'

def set_all_font_colors(presObj, draw_frame, hex_col_str ):
    print('_'*55)
    print('Setting all text:style-name to color=',hex_col_str)
    for elem in draw_frame.iter():
        if elem.tag == TEXT_SPAN_TAG:
            
            # find text:style-name 
            style_name = elem.get( TEXT_STYLE_NAME_ATTR_TAG, None )
            if style_name is not None:
                print('    found text:style-name element')
                
                style_elem = presObj.style_name_elem_from_nameD[ style_name ]
                for selem in style_elem.iter():
                    scolor = selem.get(COLOR_TAG, None)
                    if scolor is not None:
                        print('        found fo:color element')
                        selem.set( COLOR_TAG, hex_col_str )


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
    
    if pres_object_name == 'date-time' and presObj.show_date:
        draw_frame = copy_master_elem.copy(presObj, master_elem_draw_frame )
        
        if presObj.date_font_color:
            hex_col_str = getValidHexStr( presObj.date_font_color, "#000000") # default to black
            set_all_font_colors(presObj, draw_frame, hex_col_str )
        
        return draw_frame
    
    
    if pres_object_name == 'title':
        draw_frame = copy_master_elem.copy(presObj, master_elem_draw_frame )
        if 'title' in inpD:
            #print('Found title in inpD with value =',inpD['title'])
            text_span = draw_frame.find( 'draw:text-box/text:p/text:span', tree_content.rev_nsOD )
            
            if text_span is not None:
                text_span.text = inpD['title']
                
            if 'title_font_color' in inpD:
                hex_col_str = getValidHexStr( inpD['title_font_color'], "#000000") # default to black
                set_all_font_colors(presObj, draw_frame, hex_col_str )
        
        return draw_frame
    
    elif pres_object_name == 'subtitle':
        draw_frame = copy_master_elem.copy(presObj, master_elem_draw_frame )
        if 'subtitle' in inpD:
            #print('Found title in inpD with value =',inpD['title'])
            text_span = draw_frame.find( 'draw:text-box/text:p/text:span', tree_content.rev_nsOD )
            
            if text_span is not None:
                text_span.text = inpD['subtitle']
                
            if 'subtitle_font_color' in inpD:
                hex_col_str = getValidHexStr( inpD['subtitle_font_color'], "#999999") # default to gray
                set_all_font_colors(presObj, draw_frame, hex_col_str )
        
        return draw_frame

    
    elif pres_object_name == 'outline':
        draw_frame = copy_master_elem.copy(presObj, master_elem_draw_frame )
        if 'outlineL' in inpD:
            #print('Found title in inpD with value =',inpD['title'])
            text_box = draw_frame.find( 'draw:text-box', tree_content.rev_nsOD )
            text_listL = draw_frame.findall( 'draw:text-box/text:list', tree_content.rev_nsOD )
            max_indent = len( text_listL )-1
            
            if (text_box is not None) and text_listL:
                print('max_indent = %i'%max_indent)
                text_box.clear_children()
                
                for n, sInp in inpD['outlineL']:
                    n = min(n, max_indent)
                    text_list = deepcopy( text_listL[n] )
                    
                    text_span = None
                    target_tag = NS('text:span', tree_content.rev_nsOD)
                    for elem in text_list.iter():
                        if elem.tag == target_tag:
                            text_span = elem
                            break
                    
                    if text_span is not None:
                        text_span.text = sInp
                        text_box.append( text_list )
                
            if 'outline_font_color' in inpD:
                hex_col_str = getValidHexStr( inpD['outline_font_color'], "#000000") # default to black
                set_all_font_colors(presObj, draw_frame, hex_col_str )
        
        return draw_frame

    # If nothing specific is done, return None
    return None
    
    