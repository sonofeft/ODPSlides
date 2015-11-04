# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
from copy import deepcopy

from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag
from odpslides.segments import segment_intersect, Point, BBox
from odpslides.blockade import Blockade

# Assume that all reference slides conform to "pageLayout3" (10in x 7.5in)
PAGE_WIDTH = 10.0 # inches
PAGE_HEIGHT = 7.5 # inches
FOOTER_HEIGHT = 6.95139 # inches

PRESENTATION_CLASS_ATTR = force_to_tag( 'presentation:class' )

def force_svg_dim_to_float( s ):
    """Usually gets a value like:"1.23456in" (i.e. inches) """
    try:
        val = float( s[:-2] )
    except:
        val = 0.0
        print('...ERROR... in force_svg_dim_to_float. Inches value = "%s"'%s)
    return val

class FrameDim(object):
    """
    The dimensions of a draw:frame object.
    Has four Blockade objects to limit translation and a bounding box to define location.
    """
    
    def __init__(self, my_page, my_draw_frame):
        """
        Build blockades and bbox
        """
        self.my_page = my_page
        self.my_draw_frame = my_draw_frame
        
        self.my_frame_class = my_draw_frame.get( PRESENTATION_CLASS_ATTR, '' )
        
        # Start out with blockades the same as full page
        self.left_blockade   = deepcopy( my_page.left_blockade )
        self.right_blockade  = deepcopy( my_page.right_blockade )
        self.top_blockade    = deepcopy( my_page.top_blockade )
        self.bottom_blockade = deepcopy( my_page.bottom_blockade )

        svg_x = force_svg_dim_to_float( my_draw_frame.get( force_to_tag('svg:x'), '' ) )
        svg_y = force_svg_dim_to_float( my_draw_frame.get( force_to_tag('svg:y'), '' ) )
        svg_w = force_svg_dim_to_float( my_draw_frame.get( force_to_tag('svg:width'), '' ) )
        svg_h = force_svg_dim_to_float( my_draw_frame.get( force_to_tag('svg:height'), '' ) )
        
        self.bbox = BBox( svg_x, svg_x + svg_w, svg_y, svg_y + svg_h )
        
        self.make_side_segments() # for current state of BBox
        
    def make_side_segments(self):
        """
        Use current state of bbox to make side segments
        """
        b = self.bbox
        self.left_seg  = ( Point(b.left_x, b.top_y), Point(b.left_x, b.bottom_y) )
        self.right_seg = ( Point(b.right_x,b.top_y), Point(b.right_x,b.bottom_y) )

        self.top_seg    = ( Point(b.left_x, b.top_y),    Point(b.right_x, b.top_y) )
        self.bottom_seg = ( Point(b.left_x, b.bottom_y), Point(b.right_x, b.bottom_y) )

        

    def calc_local_blockades(self):
        
        right_distL = [] # holds a tuples of (distance, draw_frame)
        left_distL  = []
        top_distL   = []
        bottom_distL= []
        
        for frame_dim in self.my_page.frame_dimL:
            if frame_dim != self:
                
                is_good, dist = right_distance( self.right_seg, frame_dim.left_seg )
                if is_good:
                    right_distL.append( (dist, frame_dim) )
                
                is_good, dist = left_distance( self.left_seg, frame_dim.right_seg )
                if is_good:
                    left_distL.append( (dist, frame_dim) )
                
                is_good, dist = top_distance( self.top_seg, frame_dim.bottom_seg )
                if is_good:
                    top_distL.append( (dist, frame_dim) )
                                
                is_good, dist = bottom_distance( self.bottom_seg, frame_dim.top_seg )
                if is_good:
                    bottom_distL.append( (dist, frame_dim) )
                    
        right_distL.sort() # sort the tuples of (distance, frame_dim) so shortest is first
        left_distL.sort()
        top_distL.sort()
        bottom_distL.sort()
        
        if right_distL:
            dist, frame_dim = right_distL[0]
            a0, a1 = self.right_seg
            b0, b1 = frame_dim.left_seg
            x = a0.x + dist/2.0
            self.right_blockade.set_new_x_value( x )
            frame_dim.left_blockade.set_new_x_value( x )
        else:
            self.right_blockade = deepcopy( self.my_page.right_blockade )
        
        if left_distL:
            dist, frame_dim = left_distL[0]
            a0, a1 = self.left_seg
            b0, b1 = frame_dim.right_seg
            x = b0.x + dist/2.0
            self.left_blockade.set_new_x_value( x )
            frame_dim.right_blockade.set_new_x_value( x )
        else:
            self.left_blockade = deepcopy( self.my_page.left_blockade )
        
        if top_distL:
            dist, frame_dim = top_distL[0]
            a0, a1 = self.top_seg
            b0, b1 = frame_dim.bottom_seg
            y = b0.y + dist/2.0
            self.top_blockade.set_new_y_value( y )
            frame_dim.bottom_blockade.set_new_y_value( y )
        else:
            self.top_blockade = deepcopy( self.my_page.top_blockade )

        
        if bottom_distL:
            dist, frame_dim = bottom_distL[0]
            a0, a1 = self.bottom_seg
            b0, b1 = frame_dim.top_seg
            y = a0.y + dist/2.0
            self.bottom_blockade.set_new_y_value( y )
            frame_dim.top_blockade.set_new_y_value( y )
        else:
            self.bottom_blockade = deepcopy( self.my_page.bottom_blockade )


def between( val, low, high):
    if val>=low and val<=high:
        return True
    else:
        return False

def vertical_overlap(seg1, seg2):
    """Return true if there is vertical overlap"""
    a0, a1 = seg1
    b0, b1 = seg2
    if between(a0.y, b0.y, b1.y):
        return True

    if between(a1.y, b0.y, b1.y):
        return True

    if between(b0.y, a0.y, a1.y):
        return True

    if between(b1.y, a0.y, a1.y):
        return True
    
    return False

def right_distance( seg1, seg2 ):
    """
    IF seg1 and seg2 overlap, return distance of vertical seg2 from seg 1.
    
    seg parameters are each a tuple of two Point objects
    """
    if vertical_overlap( seg1, seg2):
        a0, a1 = seg1
        b0, b1 = seg2
        if b0.x > a0.x:
            return True, b0.x - a0.x
    
    return False, None
    

def left_distance( seg1, seg2 ):
    """
    IF seg1 and seg2 overlap, return distance of vertical seg2 from seg 1.
    
    seg parameters are each a tuple of two Point objects
    """
    if vertical_overlap( seg1, seg2):
        a0, a1 = seg1
        b0, b1 = seg2
        if a0.x > b0.x:
            return True, a0.x - b0.x
    
    return False, None
    

def horizontal_overlap(seg1, seg2):
    """Return true if there is horizontal overlap"""
    a0, a1 = seg1
    b0, b1 = seg2
    if between(a0.x, b0.x, b1.x):
        return True

    if between(a1.x, b0.x, b1.x):
        return True

    if between(b0.x, a0.x, a1.x):
        return True

    if between(b1.x, a0.x, a1.x):
        return True
    
    return False


def top_distance( seg1, seg2 ):
    """
    IF seg1 and seg2 overlap, return distance of horizontal seg2 from seg 1.
    
    seg parameters are each a tuple of two Point objects
    """
    if horizontal_overlap( seg1, seg2):
        a0, a1 = seg1
        b0, b1 = seg2
        if a0.y > b0.y:
            return True, a0.y - b0.y
    
    return False, None
                    
                

def bottom_distance( seg1, seg2 ):
    """
    IF seg1 and seg2 overlap, return distance of horizontal seg2 from seg 1.
    
    seg parameters are each a tuple of two Point objects
    """
    if horizontal_overlap( seg1, seg2):
        a0, a1 = seg1
        b0, b1 = seg2
        if b0.y > a0.y:
            return True, b0.y - a0.y
    
    return False, None
                    
                                
                
                
                
            