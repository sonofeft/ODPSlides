# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function

import time
import sys
from copy import deepcopy

from odpslides.color_utils import getValidHexStr

class StylesXML(object):
    """
    StylesXML wraps the styles.xml internal file of the reference odp file
    """
    
    def __init__(self, presObj, odp_ref):
        """
        presObj is the Presentation object
        
        odp_ref is the odp file opened by the Presentation object
        """
        
        self.presObj = presObj
        self.odp_ref = odp_ref
        self.make_clean_copy()
        
        
    def make_clean_copy(self):
        # Make a copy of the original styles.xml Elements
        self.styles_tmplt = deepcopy( self.odp_ref.styles_xml_obj )
        
        
    def set_background(self):
        
        if self.presObj.page_type == 'solidbg':
            hex_col_str = getValidHexStr(  self.presObj.background_color , "#ffffff") # default to white
            self.styles_tmplt.set_all_attr_of_tag( 'style:drawing-page-properties', 'draw:fill-color', hex_col_str)
        
        