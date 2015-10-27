# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function

import os
import sys

from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag
from odpslides.color_utils import getValidHexStr
from odpslides.template_xml_file import TemplateXML_File

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
        self.background_image = self.presObj.background_image
        self.internal_background_image = self.presObj.internal_background_image
        
        # Start out as "plain", can be changed later
        self.page_type = 'plain' # "plain", "grad", "image"
        self.disp_name = disp_name  # "Title Slide"
        
        print('in class Page: inpD=%s'%inpD)
        
        self.lay_name = plain.page_layouts.layout_name_lookupD[ self.disp_name ] # like: "Master1-PPL1"
        
        # master_name like: Master1-Layout1-title-Title-Slide
        self.master_name = plain.content_body_presentation.master_page_name_lookupD[ self.lay_name ]
        
        self.draw_page = plain.content_body_presentation.func_quick_lookupD[ self.lay_name ]() # Element object
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
        
        if self.background_image:
            self.set_background_image( self.background_image )

    def normalize_content_styles(self):
        
        self.draw_page_style_name = ''
        
        for elem in self.draw_page.iter():
            for aname, aval in elem.items():
                if aname.endswith( '}style-name' ):
                    a_new = self.presObj.get_next_a_style()
                    
                    elem.set( force_to_tag(aname), a_new )
                    style_elem = plain.content_auto_styles.content_style_name_lookupD[ aval ]()
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
            
    def set_to_gradient(self, grad_start_color="#99ff99", grad_end_color="#ffffff", grad_angle=0, grad_draw_style='linear' ):
        # Get current style element
        style_elem = self.presObj.new_content_styleD[ self.draw_page_style_name ]
        i_style_elem = self.presObj.new_content_styleL.index( style_elem )
        
        draw_grad_style_name = self.presObj.get_next_a_style()
        
        new_style_elem = TemplateXML_File( GRAD_ELEM_STR%(XMLNS_STR, self.draw_page_style_name, draw_grad_style_name  ) )
        
        new_draw_grad_elem = TemplateXML_File( DRAW_GRAD_STR%(XMLNS_STR, draw_grad_style_name, grad_draw_style,
                            grad_start_color, grad_end_color) )
                            
        self.presObj.new_content_styleD[ self.draw_page_style_name ] = new_style_elem.root
        self.presObj.new_content_styleL[ i_style_elem ] = new_style_elem.root
        
        self.presObj.new_styles_office_stylesL.append( new_draw_grad_elem.root )

            
    def set_background_image(self, background_image='' ):
        # Get current style element
        
        if not background_image:
            return
        
        self.background_image = background_image
        self.internal_background_image = self.presObj.get_next_image_name(background_image)
        
        style_elem = self.presObj.new_content_styleD[ self.draw_page_style_name ]
        i_style_elem = self.presObj.new_content_styleL.index( style_elem )
        
        draw_img_style_name = self.presObj.get_next_a_style()
                
        new_style_elem = TemplateXML_File( IMG_ELEM_STR%(XMLNS_STR, self.draw_page_style_name, draw_img_style_name )  )
        
        new_draw_img_elem = TemplateXML_File( DRAW_IMG_STR%(XMLNS_STR, draw_img_style_name, self.internal_background_image ) )
                            
        self.presObj.new_content_styleD[ self.draw_page_style_name ] = new_style_elem.root
        self.presObj.new_content_styleL[ i_style_elem ] = new_style_elem.root
        
        self.presObj.new_styles_office_stylesL.append( new_draw_img_elem.root )

IMG_ELEM_STR = """<style:style %s style:family="drawing-page" style:name="%s">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="%s" style:repeat="stretch" 
presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" 
presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" 
presentation:display-page-number="false" presentation:display-date-time="false"/>
</style:style>"""

DRAW_IMG_STR = """<draw:fill-image %s draw:name="%s" xlink:href="media/%s" 
xlink:show="embed" xlink:actuate="onLoad"/>"""

GRAD_ELEM_STR = """<style:style %s style:family="drawing-page" style:name="%s">
<style:drawing-page-properties draw:fill="gradient" draw:fill-gradient-name="%s" presentation:visibility="visible" 
draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" 
presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" 
presentation:display-date-time="false"/>
</style:style>"""

DRAW_GRAD_STR = """<draw:gradient %s draw:name="%s" draw:style="%s" draw:angle="0" draw:start-color="%s" 
draw:end-color="%s" draw:start-intensity="100%%" draw:end-intensity="100%%"/>"""
