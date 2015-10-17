# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
"""
Build the content.xml elements.
Fill the Presentation objects lists: new_styleL and new_draw_pageL
"""
from collections import OrderedDict
from odpslides.find_obj import find_elem_w_attrib, elem_set, NS_attrib, NS

import sys
if sys.version_info < (3,):
    import odscharts.ElementTree_27OD as ET
else:
    import odscharts.ElementTree_34OD as ET

def add_title_chart( presObj, title='My Title', subtitle='My Subtitle' ):
    """
    Get some reference style:style and draw:page elements from ref template.
    Add them as attributes to presObj.
    
    Assume that get_master_styles has been called from presentation.py
    
    :param presObj: a Presentation object from presentation.py
    :type  presObj: Presentation
    :return: None
    :rtype: None
    """

    pass
        