# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function

import os
import sys

from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag
from odpslides.color_utils import getValidHexStr
from odpslides.template_xml_file import TemplateXML_File

import solidbg.content_auto_styles
import solidbg.content_body_presentation
import solidbg.page_layouts
import solidbg.styles_auto_styles
import solidbg.styles_master_pages

import image.content_auto_styles
import image.content_body_presentation
import image.page_layouts
import image.styles_auto_styles
import image.styles_master_pages

import grad.content_auto_styles
import grad.content_body_presentation
import grad.page_layouts
import grad.styles_auto_styles
import grad.styles_master_pages

DRAW_FRAME_TAG = force_to_tag( 'draw:frame' )
TEXT_SPAN_TAG =  force_to_tag( 'text:span' )
TEXT_STYLE_NAME_ATTR = force_to_tag( 'text:style-name' )
DRAW_STYLE_NAME_ATTR = force_to_tag( 'draw:style-name' )
DRAW_FILL_COLOR_ATTR = force_to_tag( 'draw:fill-color' )
DRAW_ID_ATTR = force_to_tag( 'draw:id' )
DRAW_PAGE_TAG = force_to_tag( 'draw:page' )
FONT_COLOR_ATTR = force_to_tag( 'fo:color' )
PRESENTATION_CLASS_ATTR = force_to_tag( 'presentation:class' )
PRESENTATION_TRANSITION_TYPE_ATTR = force_to_tag( 'presentation:transition-type' )
PRESENTATION_TRANSITION_SPEED_ATTR = force_to_tag( 'presentation:transition-speed' )
STYLE_STYLE_TAG = force_to_tag( 'style:style' )
PRESENTATION_BG_VISIBLE_ATTR = force_to_tag( 'presentation:background-visible' )
PRESENTATION_BG_OBJ_VISIBLE_ATTR = force_to_tag('presentation:background-objects-visible' )

STYLE_DRAWING_PAGE_PROPS_TAG = force_to_tag( 'style:drawing-page-properties' )

class Page(object):
    """
    A Page object manages the underlying draw:page object that will build the XML source
    inside the content.xml file (under the office:presentation element)
    """
    
    def __init__(self, presObj, disp_name="Title Slide", **inpD):
        """
        presObj is the Presentation object
        The master_name is something like: "Master1-Layout1-title-Title-Slide"  
        """
        self.presObj = presObj
        self.background_image = self.presObj.background_image
        self.internal_background_image = self.presObj.internal_background_image
        
        # Start out as "solidbg", can be changed later
        self.disp_name = disp_name  # "Title Slide"
        
        print('in class Page: inpD=%s'%inpD)
        
        if presObj.page_type == 'grad':
            self.page_layouts = grad.page_layouts
            self.content_body_presentation = grad.content_body_presentation
            self.content_body_presentation = grad.content_body_presentation
            self.content_auto_styles = grad.content_auto_styles
        elif presObj.page_type == 'image':
            self.page_layouts = image.page_layouts
            self.content_body_presentation = image.content_body_presentation
            self.content_body_presentation = image.content_body_presentation
            self.content_auto_styles = image.content_auto_styles
        else:
            self.page_layouts = solidbg.page_layouts
            self.content_body_presentation = solidbg.content_body_presentation
            self.content_body_presentation = solidbg.content_body_presentation
            self.content_auto_styles = solidbg.content_auto_styles
        
        self.lay_name = self.page_layouts.layout_name_lookupD[ self.disp_name ] # like: "Master1-PPL1"
        
        # master_name like: Master1-Layout1-title-Title-Slide
        self.master_name = self.content_body_presentation.master_page_name_lookupD[ self.lay_name ]
        
        self.draw_page = self.content_body_presentation.func_quick_lookupD[ self.lay_name ]() # Element object
        self.normalize_content_styles()
                        
        self.draw_frameL = self.draw_page.findall( DRAW_FRAME_TAG )
        self.draw_frameD = {} # index=frame_class (e.g. "title"), value = draw:frame element list
        for draw_frame in self.draw_frameL:
            frame_class = draw_frame.get( PRESENTATION_CLASS_ATTR, '' )
            #print('frame_class:', frame_class)
            if frame_class:
                self.draw_frameD[frame_class] = self.draw_frameD.get(frame_class, [])
                self.draw_frameD[frame_class].append( draw_frame )

        # Do similar logic for master-page if it is needed
        self.master_frameD = {} # index=frame_class (e.g. "title"), value = draw:frame element list
        
        # CHECK THESE FOR USE ????????????????????????????
        self.master_frameL = [] # ???????????????????????
        self.master_page_elem = None # ??????????????????


        #print( self.draw_frameD )
    
        if 'title' in inpD:
            self.set_textspan_text( frame_class='title', text=inpD['title'], num_frame=0, clear_all=True )
        
        if 'subtitle' in inpD:
            self.set_textspan_text( frame_class='subtitle', text=inpD['subtitle'], num_frame=0, clear_all=True )
    
        if 'title_font_color' in inpD:
            self.set_drawframe_font_color( frame_class='title', font_color=inpD['title_font_color'] )
        
        if 'subtitle_font_color' in inpD:
            self.set_drawframe_font_color( frame_class='subtitle', font_color=inpD['subtitle_font_color'] )
        
        
    def set_page_number(self, ipage):
        
        self.draw_page.set( force_to_tag('draw:name'), 'Slide%i'%ipage )
        
        self.draw_page.set( force_to_tag( 'draw:id' ), 'Slide-%i'%ipage )

    def normalize_content_styles(self):
        
        self.draw_page_style_name = ''
        
        for elem in self.draw_page.iter():
            for aname, aval in elem.items():
                if aname.endswith( '}style-name' ):
                    a_new = self.presObj.get_next_a_style()
                    
                    elem.set( force_to_tag(aname), a_new )
                    style_elem = self.content_auto_styles.content_style_name_lookupD[ aval ]()
                    style_elem.set( force_to_tag('style:name'), a_new )
                    self.presObj.new_content_styleL.append( style_elem )
                    self.presObj.new_content_styleD[ a_new ] = style_elem
                    
                    if self.draw_page_style_name == '':
                        self.draw_page_style_name = a_new # first style-name is draw:page style:style
                    
                    if style_elem.tag == STYLE_STYLE_TAG:
                        sub_style_childL = style_elem.getchildren()
                        if sub_style_childL:
                            for sub_style_elem in sub_style_childL:
                                if sub_style_elem.tag == STYLE_DRAWING_PAGE_PROPS_TAG:
                                        sub_style_elem.set( PRESENTATION_BG_VISIBLE_ATTR, 'true' )
                    
                    
            if elem.get(DRAW_ID_ATTR, ''):
                if elem.tag != DRAW_PAGE_TAG:
                    id_new = self.presObj.get_next_draw_id()
                    elem.set(DRAW_ID_ATTR, id_new)
            
    
    def set_textspan_text(self, frame_class='title', text='My Text', num_frame=0, 
                             num_textspan=0, clear_all=True ):
        
        # Change both content page and styles.xml master-page (if used)
        for frameD in [self.draw_frameD, self.master_frameD]:
        
            if frame_class in frameD:
                try:
                    draw_frame = frameD[frame_class][num_frame]
                except:
                    draw_frame = frameD[frame_class][-1]
                    print('...ERROR... in Page.set_textspan_text, num_frame>len(frameL)')
                
                count_textspan = 0 # Use in case num_textspan is set
                for subelem in draw_frame.iter():
                    if subelem.tag == TEXT_SPAN_TAG:
                        if count_textspan == num_textspan:
                            subelem.text = text
                        elif clear_all:
                            subelem.text = ''
                        count_textspan += 1
            
            
    
    def set_drawframe_font_color( self, frame_class='title', font_color='black' ):
        """
        Set the fo:color in all the style elements of the frame
        
        """

        hex_col_str = getValidHexStr( font_color, "#000000") # default to black
        # Change both content page and styles.xml master-page (if used)
        for frameD,styleD in [(self.draw_frameD, self.presObj.new_content_styleD), 
                               (self.master_frameD, self.presObj.new_master_styleD)]:
        
            if frame_class in frameD:
                for draw_frame in frameD[frame_class]:
                
                    for subelem in draw_frame.iter():
                        if subelem.tag == TEXT_SPAN_TAG:
                            aNNN = subelem.get( TEXT_STYLE_NAME_ATTR, '' )
                            if aNNN not in styleD:
                                print( 'Bad style index = %s, in set_drawframe_font_color'%aNNN )
                            else:
                                span_elem = styleD[ aNNN ]
                                for sub_span_elem in span_elem.iter():
                                    if sub_span_elem.get(FONT_COLOR_ATTR, ''):
                                        sub_span_elem.set( FONT_COLOR_ATTR, hex_col_str )

#  style element to replace solidbg/original style element (in content.xml)
IMG_ELEM_STR = """<style:style %s style:family="drawing-page" style:name="%s">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="%s" style:repeat="stretch" 
presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" 
presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" 
presentation:display-page-number="false" presentation:display-date-time="false"/>
</style:style>"""

#  draw:fill-image element to put into office:styles of styles.xml
DRAW_IMG_STR = """<draw:fill-image %s draw:name="%s" xlink:href="media/%s" 
xlink:show="embed" xlink:actuate="onLoad"/>"""

#  style element to replace solidbg/original style element (in content.xml)
GRAD_ELEM_STR = """<style:style %s style:family="drawing-page" style:name="%s">
<style:drawing-page-properties draw:fill="gradient" draw:fill-gradient-name="%s" presentation:visibility="visible" 
draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" 
presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" 
presentation:display-date-time="false"/>
</style:style>"""

#  draw:gradient element to put into office:styles of styles.xml
DRAW_GRAD_STR = """<draw:gradient %s draw:name="%s" draw:style="%s" draw:angle="0" draw:start-color="%s" 
draw:end-color="%s" draw:start-intensity="100%%" draw:end-intensity="100%%"/>"""
