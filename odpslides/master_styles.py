# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
"""
Get placeholder elements from styles.xml
These will act as templates for adding charts.
"""

from odpslides.find_obj import find_elem_w_attrib, elem_set, NS_attrib, NS

_max_style_name_int = 0 # used for nameing styles (ex. draw:style-name="a123")
_max_draw_id_int = 0 # some internal use ???


def get_next_a_style():
    """Returns a string like "a123"  """
    global _max_style_name_int
    _max_style_name_int += 1
    return 'a%i'%_max_style_name_int
    
def get_next_draw_id():
    """Returns a string like "id123"  """
    global _max_draw_id_int
    _max_draw_id_int += 1
    return 'id%i'%_max_draw_id_int
    

def init_master_styles( presObj ):
    """
    Use presObj.styles_xml_obj and presObj.content_xml_obj to organize page 
    layouts and master-page styles.
    
    Note:  presentation:object values == presentation:class values
    (i.e. object, subtitle, outline, footer, title, page-number, table, date-time)
    """
    global _max_style_name_int, _max_draw_id_int
    
    # Make some shorter names
    tree_styles = presObj.styles_xml_obj
    tree_content = presObj.content_xml_obj
    #print(NS('draw:id', tree_styles.rev_nsOD))
    
    STYLE_NAME_ATTRIB_NAME = NS('style:name', tree_styles.rev_nsOD)
    DRAW_ID_ATTRIB_NAME = NS('draw:id', tree_styles.rev_nsOD)
    DRAW_GRADIENT_TAG = NS('draw:gradient', tree_styles.rev_nsOD)
    DRAW_START_COLOR_ATTR = NS('draw:start-color', tree_styles.rev_nsOD)
    DRAW_END_COLOR_ATTR = NS('draw:end-color', tree_styles.rev_nsOD)
    DRAW_ANGLE_ATTR = NS('draw:angle', tree_styles.rev_nsOD)
    DRAW_STYLE_ATTR = NS('draw:style', tree_styles.rev_nsOD)
    
    # Find the highest value of _max_style_name_int
    presObj.style_name_elem_from_nameD = {} # index=style-name (ex. "a123"), value=elem
    for elem in tree_styles.root.iter():
        #aval1 = elem.get( NS('draw:style-name', tree_styles.rev_nsOD) )
        #aval2 = elem.get( NS('text:style-name', tree_styles.rev_nsOD) )
        #aval3 = elem.get( NS('presentation:style-name', tree_styles.rev_nsOD) )
        #for aval in [aval1, aval2, aval3]:
        aval = elem.get(STYLE_NAME_ATTRIB_NAME, None)
        #for aname,aval in elem.items():
        if aval is not None:
            #if aname.endswith('}style-name') and aval.startswith('a'):
            if aval.startswith('a'):
                try:
                    aint = int( aval[1:] )
                    if aint > _max_style_name_int:
                        _max_style_name_int = aint
                    presObj.style_name_elem_from_nameD[aval] = elem
                except:
                    print('FAILED to get integer of style: "%s"'%aval)
                    
        id_val = elem.get(DRAW_ID_ATTRIB_NAME, None)
        if id_val is not None:
            if id_val.startswith('id'):
                try:
                    idint = int( aval[2:] )
                    if idint > _max_draw_id_int:
                        _max_draw_id_int = idint
                except:
                    pass

        if elem.tag == DRAW_GRADIENT_TAG:
            elem.set(DRAW_ANGLE_ATTR, '%s'%presObj.grad_angle)
            elem.set(DRAW_STYLE_ATTR, '%s'%presObj.grad_style)
            
            if presObj.grad_start_color:
                elem.set(DRAW_START_COLOR_ATTR, presObj.grad_start_color)
            
            if presObj.grad_end_color:
                elem.set(DRAW_END_COLOR_ATTR,  presObj.grad_end_color)


    print('Highest value of style   from styles.xml is "a%i"'%_max_style_name_int)
    print('Highest value of draw id from styles.xml is "id%i"'%_max_draw_id_int)
    print()
    
    # Build a lookup to select proper style:presentation-page-layout when 
    # the name of the master-page is given.
    # (ex. master="Master1-Layout1-title-Title-Slide",  layout="Master1-PPL1")

    # ==================== content info =======================
    page_contentL = tree_content.findall('office:body/office:presentation/draw:page') # Element objects
    print('Number of page_contentL = %i'%len(page_contentL))


    # =================== styles info =========================
    print('='*77)

    # index=style:name of presentation-page-layout,  value=elem
    pres_page_layout_styleL = tree_styles.findall('office:styles/style:presentation-page-layout') # Element objects
    print('Number of presentation-page-layout styles = %i'%len(pres_page_layout_styleL))
    presObj.page_layout_elem_from_nameD = {} # index=layout name,  value=elem
    for pres_page_layout in pres_page_layout_styleL:
        presObj.page_layout_elem_from_nameD[ pres_page_layout.get( NS('style:name', tree_styles.rev_nsOD) ) ] = pres_page_layout

    #land_port_styleL =  tree_styles.findall('office:automatic-styles/style:page-layout') # Element objects
    #print('Number of land_port_styleL = %i'%len(land_port_styleL))

    #component_styleL =  tree_styles.findall('office:automatic-styles/style:style') # Element objects
    #print('Number of component_styleL = %i'%len(component_styleL))

    #text_list_styleL =  tree_styles.findall('office:automatic-styles/text:list-style') # Element objects
    #print('Number of text_list_styleL = %i'%len(text_list_styleL))

    #numb_date_styleL =  tree_styles.findall('office:automatic-styles/number:date-style') # Element objects
    #print('Number of numb_date_styleL = %i'%len(numb_date_styleL))

    master_page_styleL =  tree_styles.findall('office:master-styles/style:master-page') # Element objects
    print('Number of master-page styles = %i'%len(master_page_styleL))

    # Will need master page Element objects when generating new pages
    presObj.master_page_elem_from_nameD = {} # index=master name, value=elem (master-page Element)
    for master_page in master_page_styleL:
        name = master_page.get('{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name')
        #print( 'Master Page Name = %s'%name )
        presObj.master_page_elem_from_nameD[ master_page.get( NS('style:name', tree_styles.rev_nsOD) ) ] = master_page


    # ============= check layout infor vs master info =======================
    #  from content, there are matching master and layout choices.
    #  Make sure that the number and type of child elements match
    #  Master elements have draw:frame elements with presentation:class attributes
    #  Layout elements have presentation:placeholder with presentation:object attributes
    print('='*77)

    presObj.matching_layout_nameD = {} # index=draw:master-page-name, value=presentation:presentation-page-layout-name
    presObj.draw_page_elem_from_nameD = {} # index=draw:master-page-name, value=Element obj for draw:page
    for page in page_contentL:
        master_name = page.get( NS('draw:master-page-name', tree_content.rev_nsOD) )
        layout_name = page.get( NS('presentation:presentation-page-layout-name', tree_content.rev_nsOD) )
        print('used master="%60s",  layout="%s"'%(master_name, layout_name)  )
        presObj.matching_layout_nameD[master_name] = layout_name
        presObj.draw_page_elem_from_nameD[master_name] = page

