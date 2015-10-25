
# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function

from namespace import XMLNS_STR, force_to_short, force_to_tag
from color_set import set_drawframe_font_color

import plain.content_auto_styles
import plain.content_body_presentation
import plain.page_layouts

def normalize_content_styles(presObj, draw_page):
    
    for elem in draw_page.iter():
        for aname, aval in elem.items():
            if aname.endswith( '}style-name' ):
                a_new = presObj.get_next_a_style()
                
                elem.set( force_to_tag(aname), a_new )
                style_elem = plain.content_auto_styles.content_style_name_lookupD[ aval ]()
                style_elem.set( force_to_tag('style:name'), a_new )
                presObj.new_content_styleL.append( style_elem )
    

def add_title_chart( presObj, title='My Title', subtitle='My Subtitle', title_font_color='',
                        subtitle_font_color=''):
    """
    Get some reference style:style and draw:page elements from ref template.
    Add them as attributes to presObj.
    
    Assume that get_master_styles has been called from presentation.py
    (i.e. some look-up dictionaries are required)
    
    :param presObj: a Presentation object from presentation.py
    :type  presObj: Presentation
    :return: None
    :rtype: None
    """
    disp_name = "Title Slide"
    lay_name = plain.page_layouts.layout_name_lookupD[ disp_name ] # like: "Master1-PPL1"
    
    # master_name like: Master1-Layout1-title-Title-Slide
    master_name = plain.content_body_presentation.master_page_name_lookupD[ lay_name ]
    
    draw_page = plain.content_body_presentation.func_quick_lookupD[ lay_name ]()
    normalize_content_styles(presObj, draw_page)
    
    if title_font_color:
        set_drawframe_font_color(presObj, draw_page, frame_class='title', font_color=title_font_color )
    
    if subtitle_font_color:
        set_drawframe_font_color(presObj, draw_page, frame_class='subtitle', font_color=subtitle_font_color )
    
    presObj.new_content_pageL.append( draw_page )
