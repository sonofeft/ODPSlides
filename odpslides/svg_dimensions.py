# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function

import os
import sys

from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag

# Assume that all reference slides conform to "pageLayout3" (10in x 7.5in)
PAGE_WIDTH = 10.0 # inches
PAGE_HEIGHT = 7.5 # inches

def force_svg_dim_to_float( s ):
    """Usually gets a value like:"1.23456in" (i.e. inches) """
    try:
        val = float( s[:-2] )
    except:
        val = 0.0
        print('...ERROR... in force_svg_dim_to_float. Inches value = "%s"'%s)
    return val


def adjust_draw_page_internal_dims( pageObj, pcent_stretch_center=100, pcent_stretch_content=100  ):
    """
    Change the page layout. Typically to maximize the size of the content.
    """
    
    pcent_stretch_center =  max(0, min(100, pcent_stretch_center)) # assure range of 0 to 100
    pcent_stretch_content = max(0, min(100, pcent_stretch_content)) # assure range of 0 to 100
    
    if (pcent_stretch_center == 0) and (pcent_stretch_content == 0):
        return
    
    # At this point we know there will be changes
    for draw_frame in pageObj.draw_frameL:
        draw_frame.set( force_to_tag('presentation:user-transformed'),"true" )
    
    ymin = 0.0
    ymax = PAGE_HEIGHT
    xmin = 0.0
    xmax = PAGE_WIDTH
    N_content = 0 # count number of content objects
    content_dimL = [] # hold (x,y,w,h) of content
    content_frameL = [] # hold draw_frame of content
    
    if pcent_stretch_center:
        # If we are stretching the center, do it first before stretching the content
        for draw_frame in pageObj.draw_frameL:
            
            frame_class = draw_frame.get( force_to_tag('presentation:class'), '')
            
            if frame_class == 'title':
                svg_y = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:y'), '' ) )
                svg_h = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:height'), '' ) )
                svg_y *= (100.0 - float(pcent_stretch_center)) / 100.0
                draw_frame.set( force_to_tag('svg:y'), '%sin'%svg_y )
                ymin = max(ymin, svg_y + svg_h)
                print('svg_y = %s, where min=0.0'%(svg_y, ))
                
            elif frame_class in ['date-time', 'footer', 'page-number']:
                svg_y = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:y'), '' ) )
                svg_h = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:height'), '' ) )
                
                y_limit = PAGE_HEIGHT - svg_h
                delta_max = y_limit - svg_y
                svg_y = y_limit - delta_max * (100.0 - float(pcent_stretch_center)) / 100.0
                draw_frame.set( force_to_tag('svg:y'), '%sin'%svg_y )
                ymax = min(ymax, svg_y)
                print('svg_y = %s, where y_limit=%s'%(svg_y, y_limit))
            else:
                N_content += 1
                
                svg_x = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:x'), '' ) )
                svg_y = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:y'), '' ) )
                svg_w = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:width'), '' ) )
                svg_h = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:height'), '' ) )
                content_dimL.append( (svg_x, svg_y, svg_w, svg_h) )
                content_frameL.append( draw_frame )
                
            
    if pcent_stretch_content:
        # it's easy if there's only one content object 
        
        if N_content == 1:
            draw_frame = content_frameL[0]
            
            svg_x, svg_y, svg_w, svg_h = content_dimL[0]
            
            svg_x *= (100.0 - float(pcent_stretch_content)) / 100.0
            svg_w = (xmax - xmin) - 2.0*svg_x
            
            ybottom_old = svg_y + svg_h
            ybottom_new = ybottom_old + (ymax - ybottom_old) * float(pcent_stretch_content) / 100.0
            svg_y = svg_y - (svg_y - ymin) * float(pcent_stretch_content) / 100.0
            svg_h = ybottom_new - svg_y
            
            draw_frame.set( force_to_tag('svg:x'), '%sin'%svg_x )
            draw_frame.set( force_to_tag('svg:y'), '%sin'%svg_y )
            draw_frame.set( force_to_tag('svg:width'), '%sin'%svg_w )
            draw_frame.set( force_to_tag('svg:height'), '%sin'%svg_h )
            
    
    
    