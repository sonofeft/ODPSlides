# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function

import os
import sys

from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag
from odpslides.color_utils import getValidHexStr

import plain.content_auto_styles
import plain.content_body_presentation
import plain.page_layouts
import plain.styles_auto_styles
import plain.styles_master_pages

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
STYLE_STYLE_TAG = force_to_tag( 'style:style' )
PRESENTATION_BG_VISIBLE_ATTR = force_to_tag( 'presentation:background-visible' )

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
        
        # Start out as "plain", can be changed later
        self.page_type = 'plain' # "plain", "grad", "image"
        self.disp_name = disp_name  # "Title Slide"
        
        print('in class Page: inpD=%s'%inpD)
        
        self.lay_name = plain.page_layouts.layout_name_lookupD[ self.disp_name ] # like: "Master1-PPL1"
        
        # master_name like: Master1-Layout1-title-Title-Slide
        self.master_name = plain.content_body_presentation.master_page_name_lookupD[ self.lay_name ]
        
        self.draw_page = plain.content_body_presentation.func_quick_lookupD[ self.lay_name ]()
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
        if self.presObj.include_styles_xml:
            self.build_master_page_and_styles()
            self.master_frameL = self.presObj.new_master_page_styleL[-1].findall( DRAW_FRAME_TAG )
            for master_frame in self.master_frameL:
                frame_class = master_frame.get( PRESENTATION_CLASS_ATTR, '' )
                #print('frame_class:', frame_class)
                if frame_class:
                    self.master_frameD[frame_class] = self.master_frameD.get(frame_class, [])
                    self.master_frameD[frame_class].append( master_frame )
        else:
            self.master_frameL = []
            self.master_page_elem = None


        #print( self.draw_frameD )
    
        if 'title' in inpD:
            self.set_textspan_text( frame_class='title', text=inpD['title'], num_frame=0, clear_all=True )
        
        if 'subtitle' in inpD:
            self.set_textspan_text( frame_class='subtitle', text=inpD['subtitle'], num_frame=0, clear_all=True )
    
        if 'title_font_color' in inpD:
            self.set_drawframe_font_color( frame_class='title', font_color=inpD['title_font_color'] )
        
        if 'subtitle_font_color' in inpD:
            self.set_drawframe_font_color( frame_class='subtitle', font_color=inpD['subtitle_font_color'] )
        
        if 'background_color' in inpD:
            self.set_background_color( background_color=inpD['background_color'] )

    def normalize_content_styles(self):
        
        for elem in self.draw_page.iter():
            for aname, aval in elem.items():
                if aname.endswith( '}style-name' ):
                    a_new = self.presObj.get_next_a_style()
                    
                    elem.set( force_to_tag(aname), a_new )
                    style_elem = plain.content_auto_styles.content_style_name_lookupD[ aval ]()
                    style_elem.set( force_to_tag('style:name'), a_new )
                    self.presObj.new_content_styleL.append( style_elem )
                    self.presObj.new_content_styleD[ a_new ] = style_elem
                    
                    if style_elem.tag == STYLE_STYLE_TAG:
                        sub_style_childL = style_elem.getchildren()
                        if sub_style_childL:
                            for sub_style_elem in sub_style_childL:
                                if sub_style_elem.tag == STYLE_DRAWING_PAGE_PROPS_TAG:
                                    if self.presObj.for_excel:
                                        sub_style_elem.set( PRESENTATION_TRANSITION_TYPE_ATTR , "manual")
                                        sub_style_elem.set( PRESENTATION_BG_VISIBLE_ATTR, 'false' )
                                    else:
                                        sub_style_elem.set( PRESENTATION_BG_VISIBLE_ATTR, 'true' )
                    
                    
            if elem.get(DRAW_ID_ATTR, ''):
                if elem.tag == DRAW_PAGE_TAG:
                    #del elem.attrib[DRAW_ID_ATTR]
                    elem.set(DRAW_ID_ATTR, 'Slide-256')
                else:
                    id_new = self.presObj.get_next_draw_id()
                    elem.set(DRAW_ID_ATTR, id_new)
    
    def build_master_page_and_styles(self):
        # presObj.new_master_styleL, For each new_content_pageL item, there are many master-page style elements
        # presObj.new_master_page_styleL, For each new_content_pageL item, there is a style:master-page item
        self.master_page_elem = plain.styles_master_pages.func_quick_lookupD[self.lay_name]()
        self.presObj.new_master_page_styleL.append( self.master_page_elem )
        
        for elem in self.master_page_elem.iter():
            for aname, aval in elem.items():
                if aname.endswith( '}style-name' ):
                    a_new = self.presObj.get_next_a_style()
                    
                    elem.set( force_to_tag(aname), a_new )
                    style_elem = plain.styles_auto_styles.styles_style_name_lookupD[ aval ]()
                    
                    style_elem.set( force_to_tag('style:name'), a_new )
                    self.presObj.new_master_styleL.append( style_elem )
                    self.presObj.new_master_styleD[a_new] = style_elem


    def get_drawframe_list_from_drawpage(self, frame_class='title'):
        """Look for all draw:frame elements of presentation:class == frame_class"""
        draw_frameL = []
        for elem in self.draw_page.iter():
            if elem.tag == DRAW_FRAME_TAG:
                if elem.get( PRESENTATION_CLASS_ATTR, '' ) == frame_class:
                    draw_frameL.append( elem  ) # return elem as a draw_frame
        return draw_frameL
        
    
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

    def set_background_color(self, background_color='white' ):
        
        hex_col_str = getValidHexStr( background_color, "#ffffff") # default to white
        print( 'hex_col_str in set_background_color =',hex_col_str )

        for page_elem,styleD in [(self.draw_page, self.presObj.new_content_styleD), 
                               (self.master_page_elem, self.presObj.new_master_styleD)]:
            if page_elem is not None:
                aNNN = page_elem.get( DRAW_STYLE_NAME_ATTR, '' )
                if aNNN not in styleD:
                    print( 'Bad style index = %s, in set_background_color'%aNNN)
                else:
                    style_elem = styleD[aNNN]
                    style_elem.getchildren()[0].set(DRAW_FILL_COLOR_ATTR  , hex_col_str)
            
        
        