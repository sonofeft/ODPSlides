# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function

import os
import sys

from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag
from odpslides.segments import segment_intersect, Point

# Assume that all reference slides conform to "pageLayout3" (10in x 7.5in)
PAGE_WIDTH = 10.0 # inches
PAGE_HEIGHT = 7.5 # inches

X_MID = PAGE_WIDTH / 2.0
Y_MID = PAGE_HEIGHT / 2.0

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
    
    # At this point we know there will be changes <<<<<<<<<< ==================
    for draw_frame in pageObj.draw_frameL:
        draw_frame.set( force_to_tag('presentation:user-transformed'),"true" )
    
    ymin = 0.0
    if pageObj.presObj.show_page_numbers or pageObj.presObj.show_date:
        ymax = 6.95139
    else:
        ymax = PAGE_HEIGHT
    
    xmin = 0.0
    xmax = PAGE_WIDTH
    N_content = 0 # count number of content objects
    content_dimL = [] # hold (x,y,w,h) of content
    content_boxL = [] # holds box of content (x0, y0, x1, y1)
    content_centerlineL = [] # holds xcenter, ycenter
    content_frameL = [] # hold draw_frame of content
    
    # fill out the content lists
    for draw_frame in pageObj.draw_frameL:
        frame_class = draw_frame.get( force_to_tag('presentation:class'), '')
        if frame_class not in ['date-time', 'footer', 'page-number', 'title']:
            N_content += 1
            
            svg_x = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:x'), '' ) )
            svg_y = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:y'), '' ) )
            svg_w = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:width'), '' ) )
            svg_h = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:height'), '' ) )
            content_dimL.append( (svg_x, svg_y, svg_w, svg_h) )
            content_boxL.append( (svg_x, svg_y, svg_x+svg_w, svg_y+svg_h) ) # (x0, y0, x1, y1)
            content_centerlineL.append( (svg_x+svg_w/2.0, svg_y+svg_h/2.0) ) # (xcenter, ycenter)
            content_frameL.append( draw_frame )
    
    
    # If we are stretching the center, do it first before stretching the content
    for draw_frame in pageObj.draw_frameL:
        
        frame_class = draw_frame.get( force_to_tag('presentation:class'), '')
        
        if frame_class == 'title':
            svg_y = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:y'), '' ) )
            svg_h = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:height'), '' ) )
            svg_y *= (100.0 - float(pcent_stretch_center)) / 100.0
            if pcent_stretch_center:
                draw_frame.set( force_to_tag('svg:y'), '%sin'%svg_y )
            ymin = max(ymin, svg_y + svg_h)
            #print('svg_y = %s, where min=0.0'%(svg_y, ))
            
        elif frame_class in ['date-time', 'footer', 'page-number']:
            svg_y = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:y'), '' ) )
            svg_h = force_svg_dim_to_float( draw_frame.get( force_to_tag('svg:height'), '' ) )
            
            y_limit = PAGE_HEIGHT - svg_h
            delta_max = y_limit - svg_y
            svg_y = y_limit - delta_max * (100.0 - float(pcent_stretch_center)) / 100.0
            if pcent_stretch_center:
                draw_frame.set( force_to_tag('svg:y'), '%sin'%svg_y )
            ymax = min(ymax, svg_y)
            #print('svg_y = %s, where y_limit=%s'%(svg_y, y_limit))
                
            
    if pcent_stretch_content:
        
        def set_content_dims( index, xmn, xmx, ymn, ymx ):
            """Use this routine with local xmin, xmax, ymin, ymax to set draw:frame dimensions"""
            draw_frame = content_frameL[index]
            
            svg_x, svg_y, svg_w, svg_h = content_dimL[index]
            
            x_right_old = svg_x + svg_w
            x_right_new = x_right_old + (xmx - x_right_old) * float(pcent_stretch_content) / 100.0
            svg_x = xmn + (svg_x - xmn) * (100.0 - float(pcent_stretch_content)) / 100.0
            svg_w = x_right_new - svg_x
            
            ybottom_old = svg_y + svg_h
            ybottom_new = ybottom_old + (ymx - ybottom_old) * float(pcent_stretch_content) / 100.0
            svg_y = svg_y - (svg_y - ymn) * float(pcent_stretch_content) / 100.0
            svg_h = ybottom_new - svg_y
            #print('   SETTING %s svg_x=%s, svg_y=%s, svg_w=%s, svg_h=%s'%(\
            #      draw_frame.get( force_to_tag('presentation:class'), ''),svg_x, svg_y, svg_w, svg_h))
            
            draw_frame.set( force_to_tag('svg:x'), '%sin'%svg_x )
            draw_frame.set( force_to_tag('svg:y'), '%sin'%svg_y )
            draw_frame.set( force_to_tag('svg:width'), '%sin'%svg_w )
            draw_frame.set( force_to_tag('svg:height'), '%sin'%svg_h )


        def get_content_local_box( index ):
            """
            For the content indicated by index, find the mid-point between it
            and all of the other content
            Use segment intersections of content bounding boxes to determing max
            dimensions of each content item.
            """
            
            xmn = xmin
            xmx = xmax
            ymn = ymin
            ymx = ymax
            if N_content == 1:
                return xmn, xmx, ymn, ymx
            
            x0, y0, x1, y1 = content_boxL[index]
            
            # horizontal and vertical lines that exit out the edges of the page
            horz_lineL = []
            vert_lineL = []
            for frac in [0., .25,  .5, .75,  1.0]:
                yval = y0 + frac*(y1-y0)
                horz_lineL.append( (Point(x0-PAGE_WIDTH, yval), Point(x0+PAGE_WIDTH,yval)) )
                
                xval = x0 + frac*(x1-x0)
                vert_lineL.append( (Point(xval, y0-PAGE_HEIGHT), Point(xval,y0+PAGE_HEIGHT)) )
            
            
            for i in range( len(content_dimL) ):
                if i == index:
                    continue
                
                # create bounding segments for each other content
                x0_i, y0_i, x1_i, y1_i = content_boxL[i]
                h_i_segL = []
                v_i_segL = []
                for frac in [0., .25,  .5, .75,  1.0]:
                    yval = y0_i + frac*(y1_i-y0_i)
                    h_i_segL.append( (Point(x0_i,yval), Point(x1_i,yval)) )
                    
                    xval = x0_i + frac*(x1_i-x0_i)
                    v_i_segL.append( (Point(xval,y0_i), Point(xval,y1_i)) )
                
                # See if index horizontal lines intersect with ith content segments
                for h in horz_lineL:
                    for vi in v_i_segL:
                        if segment_intersect(h, vi):
                            #print('Intersecting y=',h[0].y)
                            #print('        with',vi[0],vi[1])
                            
                            if vi[0].x < x0:
                                xmn = max(xmn, x1_i + (x0 - x1_i)/2.0)
                            elif vi[0].x > x1:
                                xmx = min(xmx, x1 + (x0_i - x1)/2.0)
                
                # See if index vertical lines intersect with ith content segments.
                for v in vert_lineL:
                    for hi in h_i_segL:
                        if segment_intersect(v, hi):
                            
                            if hi[0].y < y0:
                                ymn = max(ymn, y1_i + (y0 - y1_i)/2.0)
                            elif hi[0].y > y1:
                                ymx = min(ymx, y1 + (y0_i - y1)/2.0)
                
                
            #print('for outline %i, xmn=%s, xmx=%s, ymn=%s, ymx=%s'%(index, xmn, xmx, ymn, ymx))
            return xmn, xmx, ymn, ymx
        
        # ================== set content dimensions ======================
        for i in range( len(content_frameL) ):
            xmn, xmx, ymn, ymx = get_content_local_box( i )
            set_content_dims(i, xmn, xmx, ymn, ymx)
            
    
    