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
from odpslides.pres_class_obj import get_presentation_class_obj
from odpslides.copy_master_elem import new_draw_page

def add_title_chart( presObj, title='My Title', subtitle='My Subtitle' ):
    """
    Get some reference style:style and draw:page elements from ref template.
    Add them as attributes to presObj.
    
    Assume that get_master_styles has been called from presentation.py
    (i.e. some look-up dictionaries are required)
    
    :param presObj: a Presentation object from presentation.py
    :type  presObj: Presentation
    :return: None
    :rtype: None
    """
    master_name = "Master1-Layout1-title-Title-Slide"
    print('Adding %s'%master_name)
    
    master_elem = presObj.master_page_elem_from_nameD[ master_name ] # from ref styles.xml (master-page Element)
    draw_page_elem = presObj.draw_page_elem_from_nameD[ master_name ] # from ref content.xml
    layout_name = presObj.matching_layout_nameD[ master_name ]
    layout_elem = presObj.page_layout_elem_from_nameD[ layout_name ]
    
    tree_styles = presObj.styles_xml_obj
    placeholder_elemL = layout_elem.findall( NS('presentation:placeholder', tree_styles.rev_nsOD)  )
    master_elem_draw_frameL = master_elem.findall( NS('draw:frame', tree_styles.rev_nsOD) )
    
    # Build new draw:page
    draw_page = new_draw_page(presObj, master_elem)
    
    for i,placeholder_elem in enumerate(placeholder_elemL):
        master_elem_draw_frame = master_elem_draw_frameL[i]
        print( placeholder_elem.tag,  master_elem_draw_frame.tag)
        
        draw_frame = get_presentation_class_obj(presObj, placeholder_elem, master_elem_draw_frame,
            **{'title':title, 'subtitle':subtitle})
        
        if draw_frame is not None:
            draw_page.append( draw_frame )
        
    
    presObj.slideL.append( draw_page )
    

def add_title_text_chart( presObj, title='My Title', 
                             outline='A piece of text\r\tWith multiple lines.' ):
    """
    Make a new page with a title and outline text below it.
    
    Assume that get_master_styles has been called from presentation.py
    (i.e. some look-up dictionaries are required)
    
    outline can be a list of strings, each placed on its own line.
    If outline is a single string, it is split into a list by \r and/or \n

    :param presObj: a Presentation object from presentation.py
    :type  presObj: Presentation
    
    :keyword str title: Text to be placed in title field (default=='My Title')
    :type  title: str or unicode
    :keyword str outline: text placed in outline (default=='A piece of text\r\tWith multiple lines.')
    :type  outline: str or unicode or list
    
    :return: None
    :rtype: None
    """
    master_name = "Master1-Layout12-tx-Title-and-Text"
    print('Adding %s'%master_name)
    
    # Start building outlineL, i.e a list of tuples with indent level and string.
    #  ( e.g. [(1,'Top'),(2,'Indent')] )
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
    
    
    master_elem = presObj.master_page_elem_from_nameD[ master_name ] # from ref styles.xml (master-page Element)
    draw_page_elem = presObj.draw_page_elem_from_nameD[ master_name ] # from ref content.xml
    layout_name = presObj.matching_layout_nameD[ master_name ]
    layout_elem = presObj.page_layout_elem_from_nameD[ layout_name ]
    
    tree_styles = presObj.styles_xml_obj
    placeholder_elemL = layout_elem.findall( NS('presentation:placeholder', tree_styles.rev_nsOD)  )
    master_elem_draw_frameL = master_elem.findall( NS('draw:frame', tree_styles.rev_nsOD) )
    
    # Build new draw:page
    draw_page = new_draw_page(presObj, master_elem)
    
    for i,placeholder_elem in enumerate(placeholder_elemL):
        master_elem_draw_frame = master_elem_draw_frameL[i]
        print( placeholder_elem.tag,  master_elem_draw_frame.tag)
        
        draw_frame = get_presentation_class_obj(presObj, placeholder_elem, master_elem_draw_frame,
            **{'title':title, 'outlineL':outlineL})
        
        if draw_frame is not None:
            draw_page.append( draw_frame )
        
    
    presObj.slideL.append( draw_page )
    
        