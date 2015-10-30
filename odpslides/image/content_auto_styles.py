
# Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
        
"""Code Generated to build style:presentation-page-layout objects for odp files"""

import sys, os
from collections import OrderedDict

from odpslides.template_xml_file import TemplateXML_File
from odpslides.namespace import XMLNS_STR

def build_element( s ):
    """Add namespace to string and use TemplateXML_File to make Element"""
    s = s.replace(' ',' %s '%XMLNS_STR, 1) # First space ONLY
    return TemplateXML_File( s ).root
                


# Use func_quick_lookupD for access to function calls

func_quick_lookupD = {} # index=suffix name, value=function name


# Use content_style_name_lookupD for access to function calls

content_style_name_lookupD = {} # index=style name (e.g. "a123"), value=function name


def style_8_style_paragraph_a1239():
    
    """Build Element style:style for paragraph_a1239 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1239">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1287():
    
    """Build Element style:style for paragraph_a1287 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1287">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.95in" fo:margin-right="0in" fo:text-indent="-0.31in" fo:margin-top="0.08333in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1289():
    
    """Build Element style:style for presentation_a1289 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1289">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1301():
    
    """Build Element style:style for drawing-page_a1301 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1301">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1300" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1302():
    
    """Build Element style:style for text_a1302 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1302">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.51389in" style:font-size-asian="0.51389in" style:font-size-complex="0.51389in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1303():
    
    """Build Element style:style for text_a1303 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1303">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.51389in" style:font-size-asian="0.51389in" style:font-size-complex="0.51389in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1304():
    
    """Build Element style:style for paragraph_a1304 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1304">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1305():
    
    """Build Element style:style for presentation_a1305 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1305">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1306():
    
    """Build Element style:style for presentation_a1306 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1306">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1307():
    
    """Build Element style:style for presentation_a1307 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1307">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1308():
    
    """Build Element style:style for presentation_a1308 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1308">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1170():
    
    """Build Element style:style for text_a1170 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1170">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1171():
    
    """Build Element style:style for text_a1171 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1171">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1172():
    
    """Build Element style:style for paragraph_a1172 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1172">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1173():
    
    """Build Element style:style for presentation_a1173 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1173">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1174():
    
    """Build Element style:style for text_a1174 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1174">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1175():
    
    """Build Element style:style for paragraph_a1175 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1175">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.6in" fo:margin-right="0in" fo:text-indent="-0.45in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1177():
    
    """Build Element style:style for text_a1177 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1177">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1178():
    
    """Build Element style:style for text_a1178 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1178">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1179():
    
    """Build Element style:style for paragraph_a1179 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1179">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.95in" fo:margin-right="0in" fo:text-indent="-0.31in" fo:margin-top="0.08333in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1240():
    
    """Build Element style:style for presentation_a1240 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1240">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1241():
    
    """Build Element style:style for presentation_a1241 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1241">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1242():
    
    """Build Element style:style for text_a1242 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1242">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1291():
    
    """Build Element style:style for drawing-page_a1291 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1291">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1290" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1243():
    
    """Build Element style:style for paragraph_a1243 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1243">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.6in" fo:margin-right="0in" fo:text-indent="-0.45in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1292():
    
    """Build Element style:style for text_a1292 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1292">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1293():
    
    """Build Element style:style for text_a1293 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1293">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1245():
    
    """Build Element style:style for text_a1245 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1245">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1246():
    
    """Build Element style:style for text_a1246 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1246">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1294():
    
    """Build Element style:style for paragraph_a1294 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1294">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1247():
    
    """Build Element style:style for paragraph_a1247 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1247">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.95in" fo:margin-right="0in" fo:text-indent="-0.31in" fo:margin-top="0.08333in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1295():
    
    """Build Element style:style for presentation_a1295 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1295">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1296():
    
    """Build Element style:style for presentation_a1296 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1296">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1249():
    
    """Build Element style:style for presentation_a1249 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1249">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1297():
    
    """Build Element style:style for presentation_a1297 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1297">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1298():
    
    """Build Element style:style for presentation_a1298 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1298">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1299():
    
    """Build Element style:style for presentation_a1299 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1299">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1310():
    
    """Build Element style:style for drawing-page_a1310 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1310">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1309" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1311():
    
    """Build Element style:style for text_a1311 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1311">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1312():
    
    """Build Element style:style for text_a1312 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1312">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1313():
    
    """Build Element style:style for paragraph_a1313 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1313">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1314():
    
    """Build Element style:style for presentation_a1314 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1314">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1315():
    
    """Build Element style:style for presentation_a1315 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1315">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1316():
    
    """Build Element style:style for presentation_a1316 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1316">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1317():
    
    """Build Element style:style for text_a1317 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1317">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1318():
    
    """Build Element style:style for paragraph_a1318 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1318">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.6in" fo:margin-right="0in" fo:text-indent="-0.45in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1181():
    
    """Build Element style:style for presentation_a1181 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1181">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1182():
    
    """Build Element style:style for text_a1182 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1182">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1183():
    
    """Build Element style:style for paragraph_a1183 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1183">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.6in" fo:margin-right="0in" fo:text-indent="-0.45in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1185():
    
    """Build Element style:style for text_a1185 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1185">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1186():
    
    """Build Element style:style for text_a1186 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1186">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1187():
    
    """Build Element style:style for paragraph_a1187 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1187">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.95in" fo:margin-right="0in" fo:text-indent="-0.31in" fo:margin-top="0.08333in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1189():
    
    """Build Element style:style for presentation_a1189 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1189">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1200():
    
    """Build Element style:style for text_a1200 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1200">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1201():
    
    """Build Element style:style for paragraph_a1201 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1201">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1202():
    
    """Build Element style:style for presentation_a1202 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1202">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1251():
    
    """Build Element style:style for drawing-page_a1251 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1251">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1250" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1203():
    
    """Build Element style:style for text_a1203 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1203">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1252():
    
    """Build Element style:style for text_a1252 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1252">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1204():
    
    """Build Element style:style for paragraph_a1204 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1204">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.6in" fo:margin-right="0in" fo:text-indent="-0.45in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1253():
    
    """Build Element style:style for text_a1253 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1253">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1254():
    
    """Build Element style:style for paragraph_a1254 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1254">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1206():
    
    """Build Element style:style for text_a1206 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1206">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1255():
    
    """Build Element style:style for presentation_a1255 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1255">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1207():
    
    """Build Element style:style for text_a1207 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1207">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1256():
    
    """Build Element style:style for text_a1256 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1256">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1208():
    
    """Build Element style:style for paragraph_a1208 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1208">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.95in" fo:margin-right="0in" fo:text-indent="-0.31in" fo:margin-top="0.08333in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1257():
    
    """Build Element style:style for paragraph_a1257 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1257">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.6in" fo:margin-right="0in" fo:text-indent="-0.45in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1259():
    
    """Build Element style:style for text_a1259 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1259">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1320():
    
    """Build Element style:style for text_a1320 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1320">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1321():
    
    """Build Element style:style for text_a1321 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1321">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1322():
    
    """Build Element style:style for paragraph_a1322 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1322">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.95in" fo:margin-right="0in" fo:text-indent="-0.31in" fo:margin-top="0.08333in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1324():
    
    """Build Element style:style for presentation_a1324 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1324">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1326():
    
    """Build Element style:style for drawing-page_a1326 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1326">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1325" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1327():
    
    """Build Element style:style for text_a1327 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1327">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.51389in" style:font-size-asian="0.51389in" style:font-size-complex="0.51389in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1328():
    
    """Build Element style:style for text_a1328 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1328">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.51389in" style:font-size-asian="0.51389in" style:font-size-complex="0.51389in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1142():
    
    """Build Element style:style for drawing-page_a1142 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1142">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1141" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1329():
    
    """Build Element style:style for paragraph_a1329 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1329">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1143():
    
    """Build Element style:style for text_a1143 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1143">
<style:text-properties fo:text-transform="uppercase" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.66667in" style:font-size-asian="0.66667in" style:font-size-complex="0.66667in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.15466in 0.15466in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1191():
    
    """Build Element style:style for drawing-page_a1191 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1191">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1190" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1144():
    
    """Build Element style:style for text_a1144 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1144">
<style:text-properties fo:text-transform="uppercase" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.66667in" style:font-size-asian="0.66667in" style:font-size-complex="0.66667in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.15466in 0.15466in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1192():
    
    """Build Element style:style for text_a1192 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1192">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1145():
    
    """Build Element style:style for paragraph_a1145 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1145">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1193():
    
    """Build Element style:style for text_a1193 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1193">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1146():
    
    """Build Element style:style for presentation_a1146 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1146">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0in" fo:padding-bottom="0in" fo:padding-left="0.05in" fo:padding-right="0.05in" draw:textarea-vertical-align="bottom" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1194():
    
    """Build Element style:style for paragraph_a1194 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1194">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1147():
    
    """Build Element style:style for text_a1147 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1147">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1195():
    
    """Build Element style:style for presentation_a1195 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1195">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1148():
    
    """Build Element style:style for paragraph_a1148 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1148">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1196():
    
    """Build Element style:style for presentation_a1196 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1196">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1149():
    
    """Build Element style:style for text_a1149 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1149">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1198():
    
    """Build Element style:style for drawing-page_a1198 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1198">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1197" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1199():
    
    """Build Element style:style for text_a1199 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1199">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1210():
    
    """Build Element style:style for presentation_a1210 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1210">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1211():
    
    """Build Element style:style for presentation_a1211 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1211">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1260():
    
    """Build Element style:style for text_a1260 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1260">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1261():
    
    """Build Element style:style for paragraph_a1261 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1261">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.95in" fo:margin-right="0in" fo:text-indent="-0.31in" fo:margin-top="0.08333in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1213():
    
    """Build Element style:style for drawing-page_a1213 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1213">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1212" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1214():
    
    """Build Element style:style for text_a1214 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1214">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1263():
    
    """Build Element style:style for presentation_a1263 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1263">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1215():
    
    """Build Element style:style for text_a1215 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1215">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1264():
    
    """Build Element style:style for presentation_a1264 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1264">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1216():
    
    """Build Element style:style for paragraph_a1216 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1216">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1265():
    
    """Build Element style:style for presentation_a1265 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1265">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1217():
    
    """Build Element style:style for presentation_a1217 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1217">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1218():
    
    """Build Element style:style for text_a1218 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1218">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1267():
    
    """Build Element style:style for drawing-page_a1267 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1267">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1266" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1219():
    
    """Build Element style:style for paragraph_a1219 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1219">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.6in" fo:margin-right="0in" fo:text-indent="-0.45in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1268():
    
    """Build Element style:style for text_a1268 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1268">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.51389in" style:font-size-asian="0.51389in" style:font-size-complex="0.51389in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1269():
    
    """Build Element style:style for text_a1269 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1269">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.51389in" style:font-size-asian="0.51389in" style:font-size-complex="0.51389in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1330():
    
    """Build Element style:style for presentation_a1330 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1330">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1331():
    
    """Build Element style:style for presentation_a1331 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1331">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1332():
    
    """Build Element style:style for presentation_a1332 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1332">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1333():
    
    """Build Element style:style for text_a1333 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1333">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1334():
    
    """Build Element style:style for paragraph_a1334 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1334">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.6in" fo:margin-right="0in" fo:text-indent="-0.45in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1336():
    
    """Build Element style:style for text_a1336 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1336">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1150():
    
    """Build Element style:style for text_a1150 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1150">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1337():
    
    """Build Element style:style for text_a1337 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1337">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1151():
    
    """Build Element style:style for paragraph_a1151 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1151">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0.5in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0.08333in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1338():
    
    """Build Element style:style for paragraph_a1338 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1338">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.95in" fo:margin-right="0in" fo:text-indent="-0.31in" fo:margin-top="0.08333in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1153():
    
    """Build Element style:style for presentation_a1153 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1153">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1155():
    
    """Build Element style:style for drawing-page_a1155 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1155">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1154" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1156():
    
    """Build Element style:style for text_a1156 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1156">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1157():
    
    """Build Element style:style for text_a1157 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1157">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1158():
    
    """Build Element style:style for paragraph_a1158 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1158">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1159():
    
    """Build Element style:style for presentation_a1159 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1159">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1221():
    
    """Build Element style:style for text_a1221 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1221">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1222():
    
    """Build Element style:style for text_a1222 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1222">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1270():
    
    """Build Element style:style for paragraph_a1270 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1270">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1223():
    
    """Build Element style:style for paragraph_a1223 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1223">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.95in" fo:margin-right="0in" fo:text-indent="-0.31in" fo:margin-top="0.08333in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1271():
    
    """Build Element style:style for presentation_a1271 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1271">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1272():
    
    """Build Element style:style for presentation_a1272 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1272">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1225():
    
    """Build Element style:style for presentation_a1225 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1225">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1273():
    
    """Build Element style:style for presentation_a1273 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1273">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1226():
    
    """Build Element style:style for presentation_a1226 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1226">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1274():
    
    """Build Element style:style for presentation_a1274 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1274">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1228():
    
    """Build Element style:style for drawing-page_a1228 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1228">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1227" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1276():
    
    """Build Element style:style for drawing-page_a1276 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1276">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1275" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1229():
    
    """Build Element style:style for text_a1229 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1229">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1277():
    
    """Build Element style:style for text_a1277 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1277">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1278():
    
    """Build Element style:style for text_a1278 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1278">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1279():
    
    """Build Element style:style for paragraph_a1279 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1279">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1340():
    
    """Build Element style:style for presentation_a1340 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1340">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1342():
    
    """Build Element style:style for drawing-page_a1342 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1342">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1341" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1343():
    
    """Build Element style:style for text_a1343 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1343">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1344():
    
    """Build Element style:style for text_a1344 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1344">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1345():
    
    """Build Element style:style for paragraph_a1345 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1345">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1346():
    
    """Build Element style:style for presentation_a1346 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1346">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1160():
    
    """Build Element style:style for text_a1160 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1160">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1347():
    
    """Build Element style:style for presentation_a1347 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1347">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1161():
    
    """Build Element style:style for paragraph_a1161 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1161">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.6in" fo:margin-right="0in" fo:text-indent="-0.45in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1163():
    
    """Build Element style:style for text_a1163 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1163">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1164():
    
    """Build Element style:style for text_a1164 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1164">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1165():
    
    """Build Element style:style for paragraph_a1165 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1165">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.95in" fo:margin-right="0in" fo:text-indent="-0.31in" fo:margin-top="0.08333in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1167():
    
    """Build Element style:style for presentation_a1167 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1167">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1169():
    
    """Build Element style:style for drawing-page_a1169 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1169">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1168" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1230():
    
    """Build Element style:style for text_a1230 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1230">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1231():
    
    """Build Element style:style for paragraph_a1231 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1231">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1232():
    
    """Build Element style:style for presentation_a1232 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1232">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1280():
    
    """Build Element style:style for presentation_a1280 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1280">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1233():
    
    """Build Element style:style for presentation_a1233 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1233">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1281():
    
    """Build Element style:style for presentation_a1281 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1281">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1234():
    
    """Build Element style:style for presentation_a1234 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1234">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1282():
    
    """Build Element style:style for text_a1282 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1282">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1283():
    
    """Build Element style:style for paragraph_a1283 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1283">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.6in" fo:margin-right="0in" fo:text-indent="-0.45in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1236():
    
    """Build Element style:style for drawing-page_a1236 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1236">
<style:drawing-page-properties draw:fill="bitmap" draw:fill-image-name="a1235" style:repeat="stretch" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1237():
    
    """Build Element style:style for text_a1237 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1237">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1285():
    
    """Build Element style:style for text_a1285 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1285">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1238():
    
    """Build Element style:style for text_a1238 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1238">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Lucida Sans" fo:font-size="0.56944in" style:font-size-asian="0.56944in" style:font-size-complex="0.56944in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" fo:text-shadow="0.07857in 0.07857in 1pc #000000" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1286():
    
    """Build Element style:style for text_a1286 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1286">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#ffffff" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Book Antiqua" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def text_8_list_style_a1188():
    
    """Build Element text:list-style for a1188 """
    
    elem = build_element( """<text:list-style style:name="a1188">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.29in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.64in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.93in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.17in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.38in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.62in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.84in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.06in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.28in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1248():
    
    """Build Element text:list-style for a1248 """
    
    elem = build_element( """<text:list-style style:name="a1248">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.29in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.64in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.93in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.17in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.38in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.62in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.84in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.06in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.28in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1262():
    
    """Build Element text:list-style for a1262 """
    
    elem = build_element( """<text:list-style style:name="a1262">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.29in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.64in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.93in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.17in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.38in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.62in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.84in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.06in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.28in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1323():
    
    """Build Element text:list-style for a1323 """
    
    elem = build_element( """<text:list-style style:name="a1323">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.29in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.64in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.93in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.17in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.38in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.62in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.84in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.06in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.28in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1258():
    
    """Build Element text:list-style for a1258 """
    
    elem = build_element( """<text:list-style style:name="a1258">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.15in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.79in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.03in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.24in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.48in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.7in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.92in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="2.14in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1319():
    
    """Build Element text:list-style for a1319 """
    
    elem = build_element( """<text:list-style style:name="a1319">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.15in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.79in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.03in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.24in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.48in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.7in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.92in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="2.14in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1335():
    
    """Build Element text:list-style for a1335 """
    
    elem = build_element( """<text:list-style style:name="a1335">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.15in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.79in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.03in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.24in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.48in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.7in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.92in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="2.14in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1205():
    
    """Build Element text:list-style for a1205 """
    
    elem = build_element( """<text:list-style style:name="a1205">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.15in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.79in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.03in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.24in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.48in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.7in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.92in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="2.14in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1152():
    
    """Build Element text:list-style for a1152 """
    
    elem = build_element( """<text:list-style style:name="a1152">
<text:list-level-style-number text:level="1" style:num-format="">
<style:list-level-properties text:space-before="0in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="2" style:num-format="">
<style:list-level-properties text:space-before="0.5in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="3" style:num-format="">
<style:list-level-properties text:space-before="1in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="4" style:num-format="">
<style:list-level-properties text:space-before="1.5in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="5" style:num-format="">
<style:list-level-properties text:space-before="2in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="6" style:num-format="">
<style:list-level-properties text:space-before="2.5in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="7" style:num-format="">
<style:list-level-properties text:space-before="3in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="8" style:num-format="">
<style:list-level-properties text:space-before="3.5in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="9" style:num-format="">
<style:list-level-properties text:space-before="4in" />
</text:list-level-style-number>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1284():
    
    """Build Element text:list-style for a1284 """
    
    elem = build_element( """<text:list-style style:name="a1284">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.15in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.79in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.03in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.24in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.48in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.7in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.92in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="2.14in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1220():
    
    """Build Element text:list-style for a1220 """
    
    elem = build_element( """<text:list-style style:name="a1220">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.15in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.79in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.03in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.24in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.48in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.7in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.92in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="2.14in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1339():
    
    """Build Element text:list-style for a1339 """
    
    elem = build_element( """<text:list-style style:name="a1339">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.29in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.64in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.93in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.17in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.38in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.62in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.84in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.06in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.28in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1209():
    
    """Build Element text:list-style for a1209 """
    
    elem = build_element( """<text:list-style style:name="a1209">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.29in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.64in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.93in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.17in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.38in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.62in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.84in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.06in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.28in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1162():
    
    """Build Element text:list-style for a1162 """
    
    elem = build_element( """<text:list-style style:name="a1162">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.15in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.79in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.03in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.24in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.48in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.7in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.92in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="2.14in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1288():
    
    """Build Element text:list-style for a1288 """
    
    elem = build_element( """<text:list-style style:name="a1288">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.29in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.64in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.93in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.17in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.38in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.62in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.84in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.06in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.28in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1224():
    
    """Build Element text:list-style for a1224 """
    
    elem = build_element( """<text:list-style style:name="a1224">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.29in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.64in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.93in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.17in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.38in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.62in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.84in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.06in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.28in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1166():
    
    """Build Element text:list-style for a1166 """
    
    elem = build_element( """<text:list-style style:name="a1166">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.29in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.64in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.93in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.17in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.38in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.62in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.84in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.06in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.28in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1180():
    
    """Build Element text:list-style for a1180 """
    
    elem = build_element( """<text:list-style style:name="a1180">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.29in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.64in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="0.93in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.17in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.38in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.62in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="1.84in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.06in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA1">
<style:list-level-properties text:space-before="2.28in" text:min-label-width="0.31in" />
<style:text-properties fo:color="#ffffff" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="80%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1176():
    
    """Build Element text:list-style for a1176 """
    
    elem = build_element( """<text:list-style style:name="a1176">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.15in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.79in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.03in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.24in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.48in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.7in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.92in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="2.14in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1184():
    
    """Build Element text:list-style for a1184 """
    
    elem = build_element( """<text:list-style style:name="a1184">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.15in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.79in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.03in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.24in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.48in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.7in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.92in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="2.14in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1244():
    
    """Build Element text:list-style for a1244 """
    
    elem = build_element( """<text:list-style style:name="a1244">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.15in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="0.79in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.03in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.24in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.48in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.7in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="1.92in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xEF\x82\xA8">
<style:list-level-properties text:space-before="2.14in" text:min-label-width="0.45in" />
<style:text-properties fo:color="#f9f9f9" fo:font-family="Wingdings 2" style:font-charset="x-symbol" fo:font-size="65%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem



# Set values in func_quick_lookupD
func_quick_lookupD["a1152"] = text_8_list_style_a1152
func_quick_lookupD["a1162"] = text_8_list_style_a1162
func_quick_lookupD["a1166"] = text_8_list_style_a1166
func_quick_lookupD["a1176"] = text_8_list_style_a1176
func_quick_lookupD["a1180"] = text_8_list_style_a1180
func_quick_lookupD["a1184"] = text_8_list_style_a1184
func_quick_lookupD["a1188"] = text_8_list_style_a1188
func_quick_lookupD["a1205"] = text_8_list_style_a1205
func_quick_lookupD["a1209"] = text_8_list_style_a1209
func_quick_lookupD["a1220"] = text_8_list_style_a1220
func_quick_lookupD["a1224"] = text_8_list_style_a1224
func_quick_lookupD["a1244"] = text_8_list_style_a1244
func_quick_lookupD["a1248"] = text_8_list_style_a1248
func_quick_lookupD["a1258"] = text_8_list_style_a1258
func_quick_lookupD["a1262"] = text_8_list_style_a1262
func_quick_lookupD["a1284"] = text_8_list_style_a1284
func_quick_lookupD["a1288"] = text_8_list_style_a1288
func_quick_lookupD["a1319"] = text_8_list_style_a1319
func_quick_lookupD["a1323"] = text_8_list_style_a1323
func_quick_lookupD["a1335"] = text_8_list_style_a1335
func_quick_lookupD["a1339"] = text_8_list_style_a1339
func_quick_lookupD["drawing-page_a1142"] = style_8_style_drawing_page_a1142
func_quick_lookupD["drawing-page_a1155"] = style_8_style_drawing_page_a1155
func_quick_lookupD["drawing-page_a1169"] = style_8_style_drawing_page_a1169
func_quick_lookupD["drawing-page_a1191"] = style_8_style_drawing_page_a1191
func_quick_lookupD["drawing-page_a1198"] = style_8_style_drawing_page_a1198
func_quick_lookupD["drawing-page_a1213"] = style_8_style_drawing_page_a1213
func_quick_lookupD["drawing-page_a1228"] = style_8_style_drawing_page_a1228
func_quick_lookupD["drawing-page_a1236"] = style_8_style_drawing_page_a1236
func_quick_lookupD["drawing-page_a1251"] = style_8_style_drawing_page_a1251
func_quick_lookupD["drawing-page_a1267"] = style_8_style_drawing_page_a1267
func_quick_lookupD["drawing-page_a1276"] = style_8_style_drawing_page_a1276
func_quick_lookupD["drawing-page_a1291"] = style_8_style_drawing_page_a1291
func_quick_lookupD["drawing-page_a1301"] = style_8_style_drawing_page_a1301
func_quick_lookupD["drawing-page_a1310"] = style_8_style_drawing_page_a1310
func_quick_lookupD["drawing-page_a1326"] = style_8_style_drawing_page_a1326
func_quick_lookupD["drawing-page_a1342"] = style_8_style_drawing_page_a1342
func_quick_lookupD["paragraph_a1145"] = style_8_style_paragraph_a1145
func_quick_lookupD["paragraph_a1148"] = style_8_style_paragraph_a1148
func_quick_lookupD["paragraph_a1151"] = style_8_style_paragraph_a1151
func_quick_lookupD["paragraph_a1158"] = style_8_style_paragraph_a1158
func_quick_lookupD["paragraph_a1161"] = style_8_style_paragraph_a1161
func_quick_lookupD["paragraph_a1165"] = style_8_style_paragraph_a1165
func_quick_lookupD["paragraph_a1172"] = style_8_style_paragraph_a1172
func_quick_lookupD["paragraph_a1175"] = style_8_style_paragraph_a1175
func_quick_lookupD["paragraph_a1179"] = style_8_style_paragraph_a1179
func_quick_lookupD["paragraph_a1183"] = style_8_style_paragraph_a1183
func_quick_lookupD["paragraph_a1187"] = style_8_style_paragraph_a1187
func_quick_lookupD["paragraph_a1194"] = style_8_style_paragraph_a1194
func_quick_lookupD["paragraph_a1201"] = style_8_style_paragraph_a1201
func_quick_lookupD["paragraph_a1204"] = style_8_style_paragraph_a1204
func_quick_lookupD["paragraph_a1208"] = style_8_style_paragraph_a1208
func_quick_lookupD["paragraph_a1216"] = style_8_style_paragraph_a1216
func_quick_lookupD["paragraph_a1219"] = style_8_style_paragraph_a1219
func_quick_lookupD["paragraph_a1223"] = style_8_style_paragraph_a1223
func_quick_lookupD["paragraph_a1231"] = style_8_style_paragraph_a1231
func_quick_lookupD["paragraph_a1239"] = style_8_style_paragraph_a1239
func_quick_lookupD["paragraph_a1243"] = style_8_style_paragraph_a1243
func_quick_lookupD["paragraph_a1247"] = style_8_style_paragraph_a1247
func_quick_lookupD["paragraph_a1254"] = style_8_style_paragraph_a1254
func_quick_lookupD["paragraph_a1257"] = style_8_style_paragraph_a1257
func_quick_lookupD["paragraph_a1261"] = style_8_style_paragraph_a1261
func_quick_lookupD["paragraph_a1270"] = style_8_style_paragraph_a1270
func_quick_lookupD["paragraph_a1279"] = style_8_style_paragraph_a1279
func_quick_lookupD["paragraph_a1283"] = style_8_style_paragraph_a1283
func_quick_lookupD["paragraph_a1287"] = style_8_style_paragraph_a1287
func_quick_lookupD["paragraph_a1294"] = style_8_style_paragraph_a1294
func_quick_lookupD["paragraph_a1304"] = style_8_style_paragraph_a1304
func_quick_lookupD["paragraph_a1313"] = style_8_style_paragraph_a1313
func_quick_lookupD["paragraph_a1318"] = style_8_style_paragraph_a1318
func_quick_lookupD["paragraph_a1322"] = style_8_style_paragraph_a1322
func_quick_lookupD["paragraph_a1329"] = style_8_style_paragraph_a1329
func_quick_lookupD["paragraph_a1334"] = style_8_style_paragraph_a1334
func_quick_lookupD["paragraph_a1338"] = style_8_style_paragraph_a1338
func_quick_lookupD["paragraph_a1345"] = style_8_style_paragraph_a1345
func_quick_lookupD["presentation_a1146"] = style_8_style_presentation_a1146
func_quick_lookupD["presentation_a1153"] = style_8_style_presentation_a1153
func_quick_lookupD["presentation_a1159"] = style_8_style_presentation_a1159
func_quick_lookupD["presentation_a1167"] = style_8_style_presentation_a1167
func_quick_lookupD["presentation_a1173"] = style_8_style_presentation_a1173
func_quick_lookupD["presentation_a1181"] = style_8_style_presentation_a1181
func_quick_lookupD["presentation_a1189"] = style_8_style_presentation_a1189
func_quick_lookupD["presentation_a1195"] = style_8_style_presentation_a1195
func_quick_lookupD["presentation_a1196"] = style_8_style_presentation_a1196
func_quick_lookupD["presentation_a1202"] = style_8_style_presentation_a1202
func_quick_lookupD["presentation_a1210"] = style_8_style_presentation_a1210
func_quick_lookupD["presentation_a1211"] = style_8_style_presentation_a1211
func_quick_lookupD["presentation_a1217"] = style_8_style_presentation_a1217
func_quick_lookupD["presentation_a1225"] = style_8_style_presentation_a1225
func_quick_lookupD["presentation_a1226"] = style_8_style_presentation_a1226
func_quick_lookupD["presentation_a1232"] = style_8_style_presentation_a1232
func_quick_lookupD["presentation_a1233"] = style_8_style_presentation_a1233
func_quick_lookupD["presentation_a1234"] = style_8_style_presentation_a1234
func_quick_lookupD["presentation_a1240"] = style_8_style_presentation_a1240
func_quick_lookupD["presentation_a1241"] = style_8_style_presentation_a1241
func_quick_lookupD["presentation_a1249"] = style_8_style_presentation_a1249
func_quick_lookupD["presentation_a1255"] = style_8_style_presentation_a1255
func_quick_lookupD["presentation_a1263"] = style_8_style_presentation_a1263
func_quick_lookupD["presentation_a1264"] = style_8_style_presentation_a1264
func_quick_lookupD["presentation_a1265"] = style_8_style_presentation_a1265
func_quick_lookupD["presentation_a1271"] = style_8_style_presentation_a1271
func_quick_lookupD["presentation_a1272"] = style_8_style_presentation_a1272
func_quick_lookupD["presentation_a1273"] = style_8_style_presentation_a1273
func_quick_lookupD["presentation_a1274"] = style_8_style_presentation_a1274
func_quick_lookupD["presentation_a1280"] = style_8_style_presentation_a1280
func_quick_lookupD["presentation_a1281"] = style_8_style_presentation_a1281
func_quick_lookupD["presentation_a1289"] = style_8_style_presentation_a1289
func_quick_lookupD["presentation_a1295"] = style_8_style_presentation_a1295
func_quick_lookupD["presentation_a1296"] = style_8_style_presentation_a1296
func_quick_lookupD["presentation_a1297"] = style_8_style_presentation_a1297
func_quick_lookupD["presentation_a1298"] = style_8_style_presentation_a1298
func_quick_lookupD["presentation_a1299"] = style_8_style_presentation_a1299
func_quick_lookupD["presentation_a1305"] = style_8_style_presentation_a1305
func_quick_lookupD["presentation_a1306"] = style_8_style_presentation_a1306
func_quick_lookupD["presentation_a1307"] = style_8_style_presentation_a1307
func_quick_lookupD["presentation_a1308"] = style_8_style_presentation_a1308
func_quick_lookupD["presentation_a1314"] = style_8_style_presentation_a1314
func_quick_lookupD["presentation_a1315"] = style_8_style_presentation_a1315
func_quick_lookupD["presentation_a1316"] = style_8_style_presentation_a1316
func_quick_lookupD["presentation_a1324"] = style_8_style_presentation_a1324
func_quick_lookupD["presentation_a1330"] = style_8_style_presentation_a1330
func_quick_lookupD["presentation_a1331"] = style_8_style_presentation_a1331
func_quick_lookupD["presentation_a1332"] = style_8_style_presentation_a1332
func_quick_lookupD["presentation_a1340"] = style_8_style_presentation_a1340
func_quick_lookupD["presentation_a1346"] = style_8_style_presentation_a1346
func_quick_lookupD["presentation_a1347"] = style_8_style_presentation_a1347
func_quick_lookupD["text_a1143"] = style_8_style_text_a1143
func_quick_lookupD["text_a1144"] = style_8_style_text_a1144
func_quick_lookupD["text_a1147"] = style_8_style_text_a1147
func_quick_lookupD["text_a1149"] = style_8_style_text_a1149
func_quick_lookupD["text_a1150"] = style_8_style_text_a1150
func_quick_lookupD["text_a1156"] = style_8_style_text_a1156
func_quick_lookupD["text_a1157"] = style_8_style_text_a1157
func_quick_lookupD["text_a1160"] = style_8_style_text_a1160
func_quick_lookupD["text_a1163"] = style_8_style_text_a1163
func_quick_lookupD["text_a1164"] = style_8_style_text_a1164
func_quick_lookupD["text_a1170"] = style_8_style_text_a1170
func_quick_lookupD["text_a1171"] = style_8_style_text_a1171
func_quick_lookupD["text_a1174"] = style_8_style_text_a1174
func_quick_lookupD["text_a1177"] = style_8_style_text_a1177
func_quick_lookupD["text_a1178"] = style_8_style_text_a1178
func_quick_lookupD["text_a1182"] = style_8_style_text_a1182
func_quick_lookupD["text_a1185"] = style_8_style_text_a1185
func_quick_lookupD["text_a1186"] = style_8_style_text_a1186
func_quick_lookupD["text_a1192"] = style_8_style_text_a1192
func_quick_lookupD["text_a1193"] = style_8_style_text_a1193
func_quick_lookupD["text_a1199"] = style_8_style_text_a1199
func_quick_lookupD["text_a1200"] = style_8_style_text_a1200
func_quick_lookupD["text_a1203"] = style_8_style_text_a1203
func_quick_lookupD["text_a1206"] = style_8_style_text_a1206
func_quick_lookupD["text_a1207"] = style_8_style_text_a1207
func_quick_lookupD["text_a1214"] = style_8_style_text_a1214
func_quick_lookupD["text_a1215"] = style_8_style_text_a1215
func_quick_lookupD["text_a1218"] = style_8_style_text_a1218
func_quick_lookupD["text_a1221"] = style_8_style_text_a1221
func_quick_lookupD["text_a1222"] = style_8_style_text_a1222
func_quick_lookupD["text_a1229"] = style_8_style_text_a1229
func_quick_lookupD["text_a1230"] = style_8_style_text_a1230
func_quick_lookupD["text_a1237"] = style_8_style_text_a1237
func_quick_lookupD["text_a1238"] = style_8_style_text_a1238
func_quick_lookupD["text_a1242"] = style_8_style_text_a1242
func_quick_lookupD["text_a1245"] = style_8_style_text_a1245
func_quick_lookupD["text_a1246"] = style_8_style_text_a1246
func_quick_lookupD["text_a1252"] = style_8_style_text_a1252
func_quick_lookupD["text_a1253"] = style_8_style_text_a1253
func_quick_lookupD["text_a1256"] = style_8_style_text_a1256
func_quick_lookupD["text_a1259"] = style_8_style_text_a1259
func_quick_lookupD["text_a1260"] = style_8_style_text_a1260
func_quick_lookupD["text_a1268"] = style_8_style_text_a1268
func_quick_lookupD["text_a1269"] = style_8_style_text_a1269
func_quick_lookupD["text_a1277"] = style_8_style_text_a1277
func_quick_lookupD["text_a1278"] = style_8_style_text_a1278
func_quick_lookupD["text_a1282"] = style_8_style_text_a1282
func_quick_lookupD["text_a1285"] = style_8_style_text_a1285
func_quick_lookupD["text_a1286"] = style_8_style_text_a1286
func_quick_lookupD["text_a1292"] = style_8_style_text_a1292
func_quick_lookupD["text_a1293"] = style_8_style_text_a1293
func_quick_lookupD["text_a1302"] = style_8_style_text_a1302
func_quick_lookupD["text_a1303"] = style_8_style_text_a1303
func_quick_lookupD["text_a1311"] = style_8_style_text_a1311
func_quick_lookupD["text_a1312"] = style_8_style_text_a1312
func_quick_lookupD["text_a1317"] = style_8_style_text_a1317
func_quick_lookupD["text_a1320"] = style_8_style_text_a1320
func_quick_lookupD["text_a1321"] = style_8_style_text_a1321
func_quick_lookupD["text_a1327"] = style_8_style_text_a1327
func_quick_lookupD["text_a1328"] = style_8_style_text_a1328
func_quick_lookupD["text_a1333"] = style_8_style_text_a1333
func_quick_lookupD["text_a1336"] = style_8_style_text_a1336
func_quick_lookupD["text_a1337"] = style_8_style_text_a1337
func_quick_lookupD["text_a1343"] = style_8_style_text_a1343
func_quick_lookupD["text_a1344"] = style_8_style_text_a1344




# Set values in content_style_name_lookupD
content_style_name_lookupD["a1142"] = style_8_style_drawing_page_a1142
content_style_name_lookupD["a1143"] = style_8_style_text_a1143
content_style_name_lookupD["a1144"] = style_8_style_text_a1144
content_style_name_lookupD["a1145"] = style_8_style_paragraph_a1145
content_style_name_lookupD["a1146"] = style_8_style_presentation_a1146
content_style_name_lookupD["a1147"] = style_8_style_text_a1147
content_style_name_lookupD["a1148"] = style_8_style_paragraph_a1148
content_style_name_lookupD["a1149"] = style_8_style_text_a1149
content_style_name_lookupD["a1150"] = style_8_style_text_a1150
content_style_name_lookupD["a1151"] = style_8_style_paragraph_a1151
content_style_name_lookupD["a1152"] = text_8_list_style_a1152
content_style_name_lookupD["a1153"] = style_8_style_presentation_a1153
content_style_name_lookupD["a1155"] = style_8_style_drawing_page_a1155
content_style_name_lookupD["a1156"] = style_8_style_text_a1156
content_style_name_lookupD["a1157"] = style_8_style_text_a1157
content_style_name_lookupD["a1158"] = style_8_style_paragraph_a1158
content_style_name_lookupD["a1159"] = style_8_style_presentation_a1159
content_style_name_lookupD["a1160"] = style_8_style_text_a1160
content_style_name_lookupD["a1161"] = style_8_style_paragraph_a1161
content_style_name_lookupD["a1162"] = text_8_list_style_a1162
content_style_name_lookupD["a1163"] = style_8_style_text_a1163
content_style_name_lookupD["a1164"] = style_8_style_text_a1164
content_style_name_lookupD["a1165"] = style_8_style_paragraph_a1165
content_style_name_lookupD["a1166"] = text_8_list_style_a1166
content_style_name_lookupD["a1167"] = style_8_style_presentation_a1167
content_style_name_lookupD["a1169"] = style_8_style_drawing_page_a1169
content_style_name_lookupD["a1170"] = style_8_style_text_a1170
content_style_name_lookupD["a1171"] = style_8_style_text_a1171
content_style_name_lookupD["a1172"] = style_8_style_paragraph_a1172
content_style_name_lookupD["a1173"] = style_8_style_presentation_a1173
content_style_name_lookupD["a1174"] = style_8_style_text_a1174
content_style_name_lookupD["a1175"] = style_8_style_paragraph_a1175
content_style_name_lookupD["a1176"] = text_8_list_style_a1176
content_style_name_lookupD["a1177"] = style_8_style_text_a1177
content_style_name_lookupD["a1178"] = style_8_style_text_a1178
content_style_name_lookupD["a1179"] = style_8_style_paragraph_a1179
content_style_name_lookupD["a1180"] = text_8_list_style_a1180
content_style_name_lookupD["a1181"] = style_8_style_presentation_a1181
content_style_name_lookupD["a1182"] = style_8_style_text_a1182
content_style_name_lookupD["a1183"] = style_8_style_paragraph_a1183
content_style_name_lookupD["a1184"] = text_8_list_style_a1184
content_style_name_lookupD["a1185"] = style_8_style_text_a1185
content_style_name_lookupD["a1186"] = style_8_style_text_a1186
content_style_name_lookupD["a1187"] = style_8_style_paragraph_a1187
content_style_name_lookupD["a1188"] = text_8_list_style_a1188
content_style_name_lookupD["a1189"] = style_8_style_presentation_a1189
content_style_name_lookupD["a1191"] = style_8_style_drawing_page_a1191
content_style_name_lookupD["a1192"] = style_8_style_text_a1192
content_style_name_lookupD["a1193"] = style_8_style_text_a1193
content_style_name_lookupD["a1194"] = style_8_style_paragraph_a1194
content_style_name_lookupD["a1195"] = style_8_style_presentation_a1195
content_style_name_lookupD["a1196"] = style_8_style_presentation_a1196
content_style_name_lookupD["a1198"] = style_8_style_drawing_page_a1198
content_style_name_lookupD["a1199"] = style_8_style_text_a1199
content_style_name_lookupD["a1200"] = style_8_style_text_a1200
content_style_name_lookupD["a1201"] = style_8_style_paragraph_a1201
content_style_name_lookupD["a1202"] = style_8_style_presentation_a1202
content_style_name_lookupD["a1203"] = style_8_style_text_a1203
content_style_name_lookupD["a1204"] = style_8_style_paragraph_a1204
content_style_name_lookupD["a1205"] = text_8_list_style_a1205
content_style_name_lookupD["a1206"] = style_8_style_text_a1206
content_style_name_lookupD["a1207"] = style_8_style_text_a1207
content_style_name_lookupD["a1208"] = style_8_style_paragraph_a1208
content_style_name_lookupD["a1209"] = text_8_list_style_a1209
content_style_name_lookupD["a1210"] = style_8_style_presentation_a1210
content_style_name_lookupD["a1211"] = style_8_style_presentation_a1211
content_style_name_lookupD["a1213"] = style_8_style_drawing_page_a1213
content_style_name_lookupD["a1214"] = style_8_style_text_a1214
content_style_name_lookupD["a1215"] = style_8_style_text_a1215
content_style_name_lookupD["a1216"] = style_8_style_paragraph_a1216
content_style_name_lookupD["a1217"] = style_8_style_presentation_a1217
content_style_name_lookupD["a1218"] = style_8_style_text_a1218
content_style_name_lookupD["a1219"] = style_8_style_paragraph_a1219
content_style_name_lookupD["a1220"] = text_8_list_style_a1220
content_style_name_lookupD["a1221"] = style_8_style_text_a1221
content_style_name_lookupD["a1222"] = style_8_style_text_a1222
content_style_name_lookupD["a1223"] = style_8_style_paragraph_a1223
content_style_name_lookupD["a1224"] = text_8_list_style_a1224
content_style_name_lookupD["a1225"] = style_8_style_presentation_a1225
content_style_name_lookupD["a1226"] = style_8_style_presentation_a1226
content_style_name_lookupD["a1228"] = style_8_style_drawing_page_a1228
content_style_name_lookupD["a1229"] = style_8_style_text_a1229
content_style_name_lookupD["a1230"] = style_8_style_text_a1230
content_style_name_lookupD["a1231"] = style_8_style_paragraph_a1231
content_style_name_lookupD["a1232"] = style_8_style_presentation_a1232
content_style_name_lookupD["a1233"] = style_8_style_presentation_a1233
content_style_name_lookupD["a1234"] = style_8_style_presentation_a1234
content_style_name_lookupD["a1236"] = style_8_style_drawing_page_a1236
content_style_name_lookupD["a1237"] = style_8_style_text_a1237
content_style_name_lookupD["a1238"] = style_8_style_text_a1238
content_style_name_lookupD["a1239"] = style_8_style_paragraph_a1239
content_style_name_lookupD["a1240"] = style_8_style_presentation_a1240
content_style_name_lookupD["a1241"] = style_8_style_presentation_a1241
content_style_name_lookupD["a1242"] = style_8_style_text_a1242
content_style_name_lookupD["a1243"] = style_8_style_paragraph_a1243
content_style_name_lookupD["a1244"] = text_8_list_style_a1244
content_style_name_lookupD["a1245"] = style_8_style_text_a1245
content_style_name_lookupD["a1246"] = style_8_style_text_a1246
content_style_name_lookupD["a1247"] = style_8_style_paragraph_a1247
content_style_name_lookupD["a1248"] = text_8_list_style_a1248
content_style_name_lookupD["a1249"] = style_8_style_presentation_a1249
content_style_name_lookupD["a1251"] = style_8_style_drawing_page_a1251
content_style_name_lookupD["a1252"] = style_8_style_text_a1252
content_style_name_lookupD["a1253"] = style_8_style_text_a1253
content_style_name_lookupD["a1254"] = style_8_style_paragraph_a1254
content_style_name_lookupD["a1255"] = style_8_style_presentation_a1255
content_style_name_lookupD["a1256"] = style_8_style_text_a1256
content_style_name_lookupD["a1257"] = style_8_style_paragraph_a1257
content_style_name_lookupD["a1258"] = text_8_list_style_a1258
content_style_name_lookupD["a1259"] = style_8_style_text_a1259
content_style_name_lookupD["a1260"] = style_8_style_text_a1260
content_style_name_lookupD["a1261"] = style_8_style_paragraph_a1261
content_style_name_lookupD["a1262"] = text_8_list_style_a1262
content_style_name_lookupD["a1263"] = style_8_style_presentation_a1263
content_style_name_lookupD["a1264"] = style_8_style_presentation_a1264
content_style_name_lookupD["a1265"] = style_8_style_presentation_a1265
content_style_name_lookupD["a1267"] = style_8_style_drawing_page_a1267
content_style_name_lookupD["a1268"] = style_8_style_text_a1268
content_style_name_lookupD["a1269"] = style_8_style_text_a1269
content_style_name_lookupD["a1270"] = style_8_style_paragraph_a1270
content_style_name_lookupD["a1271"] = style_8_style_presentation_a1271
content_style_name_lookupD["a1272"] = style_8_style_presentation_a1272
content_style_name_lookupD["a1273"] = style_8_style_presentation_a1273
content_style_name_lookupD["a1274"] = style_8_style_presentation_a1274
content_style_name_lookupD["a1276"] = style_8_style_drawing_page_a1276
content_style_name_lookupD["a1277"] = style_8_style_text_a1277
content_style_name_lookupD["a1278"] = style_8_style_text_a1278
content_style_name_lookupD["a1279"] = style_8_style_paragraph_a1279
content_style_name_lookupD["a1280"] = style_8_style_presentation_a1280
content_style_name_lookupD["a1281"] = style_8_style_presentation_a1281
content_style_name_lookupD["a1282"] = style_8_style_text_a1282
content_style_name_lookupD["a1283"] = style_8_style_paragraph_a1283
content_style_name_lookupD["a1284"] = text_8_list_style_a1284
content_style_name_lookupD["a1285"] = style_8_style_text_a1285
content_style_name_lookupD["a1286"] = style_8_style_text_a1286
content_style_name_lookupD["a1287"] = style_8_style_paragraph_a1287
content_style_name_lookupD["a1288"] = text_8_list_style_a1288
content_style_name_lookupD["a1289"] = style_8_style_presentation_a1289
content_style_name_lookupD["a1291"] = style_8_style_drawing_page_a1291
content_style_name_lookupD["a1292"] = style_8_style_text_a1292
content_style_name_lookupD["a1293"] = style_8_style_text_a1293
content_style_name_lookupD["a1294"] = style_8_style_paragraph_a1294
content_style_name_lookupD["a1295"] = style_8_style_presentation_a1295
content_style_name_lookupD["a1296"] = style_8_style_presentation_a1296
content_style_name_lookupD["a1297"] = style_8_style_presentation_a1297
content_style_name_lookupD["a1298"] = style_8_style_presentation_a1298
content_style_name_lookupD["a1299"] = style_8_style_presentation_a1299
content_style_name_lookupD["a1301"] = style_8_style_drawing_page_a1301
content_style_name_lookupD["a1302"] = style_8_style_text_a1302
content_style_name_lookupD["a1303"] = style_8_style_text_a1303
content_style_name_lookupD["a1304"] = style_8_style_paragraph_a1304
content_style_name_lookupD["a1305"] = style_8_style_presentation_a1305
content_style_name_lookupD["a1306"] = style_8_style_presentation_a1306
content_style_name_lookupD["a1307"] = style_8_style_presentation_a1307
content_style_name_lookupD["a1308"] = style_8_style_presentation_a1308
content_style_name_lookupD["a1310"] = style_8_style_drawing_page_a1310
content_style_name_lookupD["a1311"] = style_8_style_text_a1311
content_style_name_lookupD["a1312"] = style_8_style_text_a1312
content_style_name_lookupD["a1313"] = style_8_style_paragraph_a1313
content_style_name_lookupD["a1314"] = style_8_style_presentation_a1314
content_style_name_lookupD["a1315"] = style_8_style_presentation_a1315
content_style_name_lookupD["a1316"] = style_8_style_presentation_a1316
content_style_name_lookupD["a1317"] = style_8_style_text_a1317
content_style_name_lookupD["a1318"] = style_8_style_paragraph_a1318
content_style_name_lookupD["a1319"] = text_8_list_style_a1319
content_style_name_lookupD["a1320"] = style_8_style_text_a1320
content_style_name_lookupD["a1321"] = style_8_style_text_a1321
content_style_name_lookupD["a1322"] = style_8_style_paragraph_a1322
content_style_name_lookupD["a1323"] = text_8_list_style_a1323
content_style_name_lookupD["a1324"] = style_8_style_presentation_a1324
content_style_name_lookupD["a1326"] = style_8_style_drawing_page_a1326
content_style_name_lookupD["a1327"] = style_8_style_text_a1327
content_style_name_lookupD["a1328"] = style_8_style_text_a1328
content_style_name_lookupD["a1329"] = style_8_style_paragraph_a1329
content_style_name_lookupD["a1330"] = style_8_style_presentation_a1330
content_style_name_lookupD["a1331"] = style_8_style_presentation_a1331
content_style_name_lookupD["a1332"] = style_8_style_presentation_a1332
content_style_name_lookupD["a1333"] = style_8_style_text_a1333
content_style_name_lookupD["a1334"] = style_8_style_paragraph_a1334
content_style_name_lookupD["a1335"] = text_8_list_style_a1335
content_style_name_lookupD["a1336"] = style_8_style_text_a1336
content_style_name_lookupD["a1337"] = style_8_style_text_a1337
content_style_name_lookupD["a1338"] = style_8_style_paragraph_a1338
content_style_name_lookupD["a1339"] = text_8_list_style_a1339
content_style_name_lookupD["a1340"] = style_8_style_presentation_a1340
content_style_name_lookupD["a1342"] = style_8_style_drawing_page_a1342
content_style_name_lookupD["a1343"] = style_8_style_text_a1343
content_style_name_lookupD["a1344"] = style_8_style_text_a1344
content_style_name_lookupD["a1345"] = style_8_style_paragraph_a1345
content_style_name_lookupD["a1346"] = style_8_style_presentation_a1346
content_style_name_lookupD["a1347"] = style_8_style_presentation_a1347

if __name__ == "__main__":
    print( content_style_name_lookupD["a1160"]() )
