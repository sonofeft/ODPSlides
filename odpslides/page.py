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


DRAW_FRAME_TAG = force_to_tag( 'draw:frame' )
TEXT_SPAN_TAG =  force_to_tag( 'text:span' )
TEXT_STYLE_NAME_ATTR = force_to_tag( 'text:style-name' )
DRAW_STYLE_NAME_ATTR = force_to_tag( 'draw:style-name' )
DRAW_FILL_COLOR_ATTR = force_to_tag( 'draw:fill-color' )
FONT_COLOR_ATTR = force_to_tag( 'fo:color' )
PRESENTATION_CLASS_ATTR = force_to_tag( 'presentation:class' )

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
        normalize_content_styles(presObj, self.draw_page)
                        
        self.draw_frameL = self.draw_page.findall( DRAW_FRAME_TAG )
        self.draw_frameD = {} # index=frame_class (e.g. "title"), value = draw:frame element list
        for draw_frame in self.draw_frameL:
            frame_class = draw_frame.get( PRESENTATION_CLASS_ATTR, '' )
            #print('frame_class:', frame_class)
            if frame_class:
                self.draw_frameD[frame_class] = self.draw_frameD.get(frame_class, [])
                self.draw_frameD[frame_class].append( draw_frame )
                
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
        
        if frame_class in self.draw_frameD:
            try:
                draw_frame = self.draw_frameD[frame_class][num_frame]
            except:
                draw_frame = self.draw_frameD[frame_class][-1]
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
        
        if frame_class in self.draw_frameD:
            for draw_frame in self.draw_frameD[frame_class]:
            
                for subelem in draw_frame.iter():
                    if subelem.tag == TEXT_SPAN_TAG:
                        aNNN = subelem.get( TEXT_STYLE_NAME_ATTR, '' )
                        a_int = int( aNNN[1:] )
                        if a_int >= len(self.presObj.new_content_styleL):
                            print( 'Bad style index = %i, when len new_content_styleL = %i'%\
                                  (a_int, len(self.presObj.new_content_styleL)) )
                        else:
                            span_elem = self.presObj.new_content_styleL[ a_int ]
                            for sub_span_elem in span_elem.iter():
                                if sub_span_elem.get(FONT_COLOR_ATTR, ''):
                                    sub_span_elem.set( FONT_COLOR_ATTR, hex_col_str )

    def set_background_color(self, background_color='white' ):
        
        hex_col_str = getValidHexStr( background_color, "#ffffff") # default to white
        print( 'hex_col_str in set_background_color =',hex_col_str )
        
        aNNN = self.draw_page.get( DRAW_STYLE_NAME_ATTR, '' )
        a_int = int( aNNN[1:] )
        if a_int >= len(self.presObj.new_content_styleL):
            print( 'Bad style index = %i, when len new_content_styleL = %i'%\
                  (a_int, len(self.presObj.new_content_styleL)) )
        else:
            style_elem = self.presObj.new_content_styleL[ a_int ]
            style_elem.getchildren()[0].set(DRAW_FILL_COLOR_ATTR  , hex_col_str)
        
        
        