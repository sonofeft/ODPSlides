
.. colors

Colors in ODPSlides
===================

There are a number of places in ODPSlides where colors are assigned
(Fonts, background color and gradient definitions).

These inputs accept any number of valid color formats.

    * Common Names ('green', 'coral', 'fuchsia')
    * Short Names  ('r', 'g', 'db')
    * Standard Hex String ('#336699', '#0000FF', '#000000')
    * Short Hex String ('#369', '#00F', '#000')

A variety of entry formats is shown below.

.. code:: python

    page_number_font_color='black'
    text_font_color='CYan'        # note mixed case is OK
    title_font_color='#69a'
    subtitle_font_color='006400'  # note missing "#" is OK
    
    background_color='#ccffcc'
    grad_start_color='r'
    grad_end_color="#FFFFFF"

Any color not recognized by name should be input in "#AACCFF" format.

Some common colors such as red, green or blue can be specified in shorthand as r, g or b. 
(see Short Name Color Table below)


.. raw:: html
   :file: ./_static/odpslides_colors.html

