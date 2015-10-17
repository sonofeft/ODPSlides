# Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
"""
Utility(ies) to compare elements
"""
from odpslides.find_obj import find_elem_w_attrib, elem_set, NS_attrib, NS

def get_elem_diffs(presObj, elem1, elem2, ignore_attrL=None ):
    """
    Return list of differences (excluding children)
    """
    returnL = []
    
    if ignore_attrL is None:
        ignore_attrL = []
    
    for i,v in enumerate( ignore_attrL ):
        ignore_attrL[i] = NS(v, presObj.content_xml_obj.rev_nsOD)
    
    if elem1.tag != elem2.tag:
        returnL.append( ['tag', elem1.tag, elem2.tag] )
    
    if elem1.text != elem2.text:
        returnL.append( ['text', elem1.text, elem2.text] )
    
    if elem1.tail != elem2.tail:
        returnL.append( ['tail', elem1.tail, elem2.tail] )
        
    for attribute, val1 in elem1.items():
        val2 = elem2.get( attribute, None )
        if (val2 != val1) and (attribute not in ignore_attrL):
            short_name = presObj.content_xml_obj.qnameOD[ attribute ]
            returnL.append( [short_name, val1, val2] )
        
    for attribute, val2 in elem2.items():
        val1 = elem1.get( attribute, None )
        if val1 is None:
            short_name = presObj.content_xml_obj.qnameOD[ attribute ]
            returnL.append( [short_name, val1, val2] )
            
    if len(elem1.getchildren()) != len(elem2.getchildren()):
        returnL.append( ['#children', len(elem1.getchildren()), len(elem2.getchildren())] )
    else:
        ichild = 0
        for child1, child2 in zip(elem1.getchildren(), elem2.getchildren()):
            childL = get_elem_diffs(presObj, child1, child2, ignore_attrL=ignore_attrL )
            if childL:
                childL.insert(0, 'ch#%i'%ichild)
                returnL.append( childL )
            ichild += 1
    
    return returnL
    
    
