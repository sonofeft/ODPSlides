# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
from copy import deepcopy

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
        
        #print('in class Page: inpD=%s'%inpD)
        
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
        
        if 'outline' in inpD:
            self.set_textspan_text( frame_class='outline', text=inpD['outline'], num_frame=0, clear_all=True )
            if 'text_font_color' in inpD:
                self.set_drawframe_font_color( frame_class='outline', font_color=inpD['text_font_color'] )
            
        if 'image_name' in inpD:
            keep_aspect_ratio = inpD.get('keep_aspect_ratio', True)
            
            self.set_image_href( frame_class='graphic', image_name=inpD['image_name'], 
                                 num_image=0, keep_aspect_ratio=keep_aspect_ratio)
        
    
    
    
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
            
    
    def build_outline_list(self, outline):
        """
        Start building outlineL, i.e a list of tuples with indent level and string.
        ( e.g. [(1,'Top'),(2,'Indent')] )
        """
        
        if type(outline) == type('text'): # a single string with \r and \t
            s = outline.replace('\n','\r')
            tempL = s.split( '\r' )
        elif type(outline) == type(['s','t']): # a list of strings
            tempL = []
            for s in outline:
                s2 = s.replace('\n','\r')
                sL = s2.split('\r')
                tempL.extend( sL )
        else:
            tempL = ['No Outline Text']
        
        for i,s in enumerate( tempL ):
            tempL[i] = s.replace('\t','    ') # replace tabs with 4 spaces
        # change the list of strings into tuples of indent level and string, e.g. [(1,'Top'),(2,'Indent')]
        outlineL = []
        for s in tempL:
            s2 = s.lstrip()
            n = int( (len(s)-len(s2)) / 4 )
            outlineL.append( (n, s2.strip()) ) # <======== outlineL sent to make outline chart
            
        return outlineL
        
    
    def set_textspan_text(self, frame_class='title', text='My Text', num_frame=0, 
                             num_textspan=0, clear_all=True ):
        
        
        if frame_class in self.draw_frameD:
            try:
                draw_frame = self.draw_frameD[frame_class][num_frame]
            except:
                draw_frame = self.draw_frameD[frame_class][-1]
                print('...ERROR... in Page.set_textspan_text, num_frame>len(frameL)')
            
            # ============================================ outline =========================================
            if frame_class == 'outline':
                text_box = draw_frame.find( force_to_tag('draw:text-box') )
                text_listL = draw_frame.findall( force_to_tag('draw:text-box/text:list') )
                max_indent = len( text_listL )-1
                
                if (text_box is not None) and text_listL:
                    #print('max_indent of outline = %i'%max_indent)
                    text_box.clear_children()
                    
                    # text comes in w/o formatting for outline.
                    outlineL = self.build_outline_list( text )
                    for n, sInp in outlineL:
                        n = min(n, max_indent)
                        text_list = deepcopy( text_listL[n] )
                        
                        #annn_new = self.presObj.get_next_a_style()
                        #text_list.set( force_to_tag('style:name'), annn_new )
                        
                        text_span = None
                        target_tag = force_to_tag('text:span')
                        for elem in text_list.iter():
                            if elem.tag == target_tag:
                                text_span = elem
                                break
                        
                        if text_span is not None:
                            text_span.text = sInp
                            text_box.append( text_list )
                
                
            # ============================================ title/subtitle ====================================
            else: # NOT an outline
                count_textspan = 0 # Use in case num_textspan is set
                for subelem in draw_frame.iter():
                    if subelem.tag == TEXT_SPAN_TAG:
                        if count_textspan == num_textspan:
                            subelem.text = text
                        elif clear_all:
                            subelem.text = ''
                        count_textspan += 1
    
    def set_image_href(self, frame_class='graphic', image_name='', num_image=0, keep_aspect_ratio=True):
        """
        Set the image xlink:href property in the draw:image element
        
        May need to adjust sizing:
        <draw:frame draw:name="Content Placeholder 3" draw:style-name="gr2" draw:text-style-name="P8" 
        draw:layer="layout" svg:width="7.884cm" svg:height="9.815cm" svg:x="8.758cm" svg:y="4.618cm" 
        presentation:class="graphic" 
        presentation:user-transformed="true">  <============== NOTE: <<<<<<<<<<
        
        <draw:image xlink:href="media/image2.jpg" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad">
        
        """
        DRAW_IMAGE_TAG = force_to_tag('draw:image')
        
        def force_to_float( s ):
            """Usually gets a value like:"1.23456in" (i.e. inches) """
            try:
                val = float( s[:-2] )
            except:
                val = 0.0
                print('...ERROR... in set_image_href. Inches value = "%s"'%s)
            return val
        
        if image_name and (frame_class in self.draw_frameD):
        
            # make sure index does not overrun
            if num_image >= len(self.draw_frameD[frame_class]):
                print('...ERROR... image index too bit in set_image_href')
                return
            
            draw_frame = self.draw_frameD[frame_class][num_image]
                    
            elem = draw_frame.find( DRAW_IMAGE_TAG )
            if elem is not None:
                elem.set( force_to_tag('xlink:href'), 'media/%s'%image_name )
                
                if keep_aspect_ratio:
                    svg_x = force_to_float( draw_frame.get( force_to_tag('svg:x'), '' ) )
                    svg_y = force_to_float( draw_frame.get( force_to_tag('svg:y'), '' ) )
                    svg_w = force_to_float( draw_frame.get( force_to_tag('svg:width'), '' ) )
                    svg_h = force_to_float( draw_frame.get( force_to_tag('svg:height'), '' ) )
                    #print('%s: x=%s, y=%s, w=%s, h=%s'%(image_name, svg_x, svg_y, svg_w, svg_h))
                    w_img,h_img = self.presObj.image_sizeD[ image_name ]
                    
                    # only continue if dimenstions are available
                    if w_img and h_img:
                        w = float(w_img)
                        h = float(h_img)
                        
                        if h/w > svg_h/svg_w:
                            # Leave svg_h and svg_y alone, change svg_w and svg_x
                            svg_w_old = svg_w
                            svg_w = svg_h * w/h
                            svg_x = svg_x + (svg_w_old - svg_w) / 2.0
                            draw_frame.set( force_to_tag('svg:width'), '%sin'%svg_w )
                            draw_frame.set( force_to_tag('svg:x'), '%sin'%svg_x )
                        else:
                            # Leave svg_w and svg_x alone, change svg_h and svg_y
                            svg_h_old = svg_h
                            svg_h = svg_w * h/w
                            svg_y = svg_y + (svg_h_old - svg_h) / 2.0
                            draw_frame.set( force_to_tag('svg:height'), '%sin'%svg_h )
                            draw_frame.set( force_to_tag('svg:y'), '%sin'%svg_y )
                        
                        # Need to tell app that things have changed from master
                        draw_frame.set( force_to_tag('presentation:user-transformed'),"true" )
    
    def set_drawframe_font_color( self, frame_class='title', font_color='black' ):
        """
        Set the fo:color in all the style elements of the frame
        
        """

        hex_col_str = getValidHexStr( font_color, "#000000") # default to black
        
        if frame_class in self.draw_frameD:
            for draw_frame in self.draw_frameD[frame_class]:
            
                for subelem in draw_frame.iter():
                    if subelem.tag == TEXT_SPAN_TAG:
                        aNNN = subelem.get( TEXT_STYLE_NAME_ATTR, '' )
                        if aNNN not in self.presObj.new_content_styleD:
                            print( 'Bad style index = %s, in set_drawframe_font_color'%aNNN )
                        else:
                            span_elem = self.presObj.new_content_styleD[ aNNN ]
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
