# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function

import os
import sys

from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag
from odpslides.color_set import set_drawframe_font_color

import plain.content_auto_styles
import plain.content_body_presentation
import plain.page_layouts

import grad.content_auto_styles
import grad.content_body_presentation
import grad.page_layouts

import image.content_auto_styles
import image.content_body_presentation
import image.page_layouts

def normalize_content_styles(presObj, draw_page):
    
    for elem in draw_page.iter():
        for aname, aval in elem.items():
            if aname.endswith( '}style-name' ):
                a_new = presObj.get_next_a_style()
                
                elem.set( force_to_tag(aname), a_new )
                style_elem = plain.content_auto_styles.content_style_name_lookupD[ aval ]()
                style_elem.set( force_to_tag('style:name'), a_new )
                presObj.new_content_styleL.append( style_elem )
    

class Page(object):
    """
    A Page object manages the underlying draw:page object that will build the XML source
    inside the content.xml file (under the office:presentation element)
    """
    
    def __init__(self, presObj, page_type="plain", disp_name="Title Slide", **inpD):
        """
        presObj is the Presentation object
        The master_name is something like: "Master1-Layout1-title-Title-Slide"  
        """
        self.presObj = presObj
        self.page_type = page_type # "plain", "grad", "image"
        self.disp_name = disp_name  # "Title Slide"
        
        print('inpD=%s'%inpD)
        
        if page_type == "plain":
            self.lay_name = plain.page_layouts.layout_name_lookupD[ self.disp_name ] # like: "Master1-PPL1"
            
            # master_name like: Master1-Layout1-title-Title-Slide
            self.master_name = plain.content_body_presentation.master_page_name_lookupD[ self.lay_name ]
            
            self.draw_page = plain.content_body_presentation.func_quick_lookupD[ self.lay_name ]()
            normalize_content_styles(presObj, self.draw_page)
            
        elif page_type == "grad":
            pass
        elif page_type == "image":
            pass
        else:
            print( '...ERROR... illegal page_type=%s'%page_type )
            sys.exit()
            
            
    
        if 'title_font_color' in inpD:
            set_drawframe_font_color(presObj, self.draw_page, frame_class='title', 
                                     font_color=inpD['title_font_color'] )
        
        if 'subtitle_font_color' in inpD:
            set_drawframe_font_color(presObj, self.draw_page, frame_class='subtitle', 
                                     font_color=inpD['subtitle_font_color'] )
            
 