# Support Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function

import sys, os
from collections import OrderedDict

if sys.version_info < (3,):
    import odpslides.ElementTree_27OD as ET
else:
    import odpslides.ElementTree_34OD as ET
from odpslides.find_obj import find_elem_w_attrib, NS_attrib, NS

from namespace import XMLNS_STR, force_to_short, force_to_tag
from namespace import python_param_from_tag, python_def_from_tag

func_quick_lookupD = {} # index=display name, value=function name
layout_name_lookupD = {} # index=display-name "Title Only", value=layout name "Master1-PPL6"
display_name_lookupD = {} # index=layout name "Master1-PPL6", display-name "Title Only"

def make_function_from_root( root, suffix='' ):
    """build python source to make the Elements from scratch"""
    
    suffix = suffix.replace(',','_')
    if suffix in func_quick_lookupD:
        n = 2
        while '%s_%i'%(suffix, n) in func_quick_lookupD:
            n += 1
        suffix = '%s_%i'%(suffix, n)
    
    func_name = python_def_from_tag(root.tag)
    if suffix:
        func_name = func_name + '_%s'%python_def_from_tag(suffix)
        
    # Used after code is generated
    func_quick_lookupD[suffix] = func_name    
    dname = root.get( force_to_tag('style:display-name'), '' )
    lname = root.get( force_to_tag('style:name'), '' )
    if dname and lname:
        layout_name_lookupD[dname] = lname
        display_name_lookupD[lname] = dname
    
    keyL = sorted( root.keys() )
    
    sL = ['def %s():'%(func_name, )]
    sL.append( '    ' )
    doc_str = 'Build Element %s'%force_to_short(root.tag)
    if suffix:
        doc_str = doc_str + ' for %s'%suffix
    sL.append( '''    """%s """'''%doc_str )
    sL.append( '    ' )
    
    sL.append( '    elem = ET.Element( "%s" )'%root.tag )
    for key in keyL:
        sL.append( '    elem.set("%s", "%s")'%(key, root.get(key) ) )
    if root.text:
        sL.append('    elem.text = "%s"'%root.text)
    sL.append( '    ' )
    
    for child in root.getchildren():
        sL.append('    child = ET.Element( "%s" )'%child.tag)
        for ckey in sorted( child.keys() ):
            sL.append( '    child.set("%s", "%s")'%(ckey, child.get(ckey) ) )
        if child.text:
            sL.append('    child.text = "%s"'%child.text)
        sL.append( '    elem.append( child )' )
        sL.append( '    ' )
    
    
    sL.append( '    ' )
    sL.append( '    return elem\n\n' )
    
    return '\n'.join(sL)

if __name__ == "__main__":

    from odpslides.odp_file import ODPFile
    
    here = os.path.abspath(os.path.dirname(__file__))
    
    for suffix in ['image', 'grad', 'plain']:
    #for suffix in ['plain']:
        func_quick_lookupD.clear() # need to empty dict
        layout_name_lookupD.clear()
        display_name_lookupD.clear()
    
        fname = r'D:\py_proj_2015\ODPSlides\odpslides\templates\ppt_all_layouts_%s.odp'%suffix
        odp = ODPFile( fname )
        
        py_file = os.path.join(here, suffix, 'page_layouts.py')
        print('Opening:',py_file)
        fOut = open( py_file, 'w' )
        
        fOut.write( '''
# Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
        
"""Code Generated to build style:presentation-page-layout objects for odp files"""

import sys, os
from collections import OrderedDict

if sys.version_info < (3,):
    import odpslides.ElementTree_27OD as ET
else:
    import odpslides.ElementTree_34OD as ET
                
''' )
        fOut.write('\n\n# Use func_quick_lookupD for access to function calls')
        fOut.write( '\n\nfunc_quick_lookupD = {} # index=display name, value=function name\n' )
        
        fOut.write( 'layout_name_lookupD = {}\n' )
        fOut.write( 'display_name_lookupD = {}\n' )
        fOut.write('\n\n')
        
        # do style:presentation-page-layout
        page_layoutL = odp.office_styles_elem.findall( force_to_tag('style:presentation-page-layout') )
        for layout in page_layoutL:
            fOut.write( make_function_from_root( layout, 
                    suffix=layout.get( force_to_tag('style:display-name') ) ) )
        
        # do style:default-style
        page_layoutL = odp.office_styles_elem.findall( force_to_tag('style:default-style') )
        for layout in page_layoutL:
            fOut.write( make_function_from_root( layout, 
                    suffix=layout.get( force_to_tag('style:family') ) ) )

        
        # do draw:gradient
        page_styleL = odp.office_styles_elem.findall( force_to_tag('draw:gradient') )
        for style in page_styleL:
            fOut.write( make_function_from_root( style, suffix='' ) )
            break # only do one
        
        # do draw:fill-image
        page_styleL = odp.office_styles_elem.findall( force_to_tag('draw:fill-image') )
        for style in page_styleL:
            fOut.write( make_function_from_root( style, suffix='' ) )
            break # only do one


        fOut.write('\n\n# Set values in func_quick_lookupD\n')
        keyL = sorted( func_quick_lookupD.keys() )
        for key in keyL:
            fOut.write( 'func_quick_lookupD["%s"] = %s\n'%(key, func_quick_lookupD[key]) )

        fOut.write('\n\n')


        fOut.write('\n\n# Set values in layout_name_lookupD\n')
        keyL = sorted( layout_name_lookupD.keys() )
        for key in keyL:
            fOut.write( 'layout_name_lookupD["%s"] = "%s"\n'%(key, layout_name_lookupD[key]) )

        fOut.write('\n\n')

        fOut.write('\n\n# Set values in display_name_lookupD\n')
        keyL = sorted( display_name_lookupD.keys() )
        for key in keyL:
            fOut.write( 'display_name_lookupD["%s"] = "%s"\n'%(key, display_name_lookupD[key]) )

        fOut.write('\n\n')


        fOut.write('''
if __name__ == "__main__":
    print( func_quick_lookupD["Title Only"]() )
''')
        
