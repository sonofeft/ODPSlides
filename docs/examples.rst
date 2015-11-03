
.. examples


Examples
========

Slan, by A.E. vanVogt
---------------------

As a kid, Slan is one of the first scifi novels I read. 
This is a simple slide presentation about that book.

The code below initializes the ``Presentation`` object with a background color
and footer text.

The three charts are added by the commands P.add_title_chart, P.add_titled_outline_chart
and P.add_titled_image.

Note the lines in the ``add_titled_image`` command with the parameters ``pcent_stretch_center``
and ``pcent_stretch_content``.

``pcent_stretch_center`` causes the title, date, footer and page number to move toward the edges of
the chart from 0% to 100% as far as they can go. This can open up the center of the chart for the 
next command (``pcent_stretch_content``) to make central content larger.

``pcent_stretch_content`` causes the central content of a chart to get larger.
The central content will expand from 0% to 100% of the available space.

The final command, P.save, will save the presentation to file and, if the ``launch`` flag
is set, will launch whichever application is linked to ``odp`` files on your system.
(PowerPoint, LibreOffice or OpenOffice)

.. code:: python

    from odpslides.presentation import Presentation

    P = Presentation(background_color='darkseagreen', footer="slan example")

    P.add_title_chart( title='Slan, from 1946', subtitle='A. E. van Vogt')

    P.add_titled_outline_chart( title='Slans Are Evolved Humans', outline="""
    The Slan are named after Samuel Lann
        The creator of Slans
    There are two kinds of Slans
        With tendrils
            can read minds of ordinary humans
            can communicate telepathically with other Slans
        Without tendrils
            super intelligent
            no telepathy
            can hide thoughts from other Slan""")

    P.add_titled_image( title='Ninth Big Printing', image_file='slan.png',
                        pcent_stretch_center=80, pcent_stretch_content=80)

    P.save( filename='slan.odp', launch=1 )


:download:`download slan.odp <./_static/slan.odp>`

:download:`download slan.py <./_static/slan.py>`




.. raw:: html

    <table border="1">
    <tr><th>PowerPoint Output</th></tr>
    
    <tr>
        <td> 
            <a  href="./_static/slan_in_PowerPoint.png">
            <img src="./_static/slan_in_PowerPoint.png" width="60%">
            </a>
        </td>
    </tr>
    
    <tr><th>OpenOffice Output</th></tr>
    <tr>
        <td> 
            <a  href="./_static/slan_in_OpenOffice.png">
            <img src="./_static/slan_in_OpenOffice.png" width="60%">
            </a>
        </td>
    </tr>
    
    </table>


`Click images to see full size`

John Varley
-----------

John Varley is an author I discovered in college with the three books shown here.

This example demonstrates a gradient background color as well as the fact that the 
``P.add_titled_image`` command can take from 1 to 4 image names (image_file, image_2_file,
image_3_file, image_4_file).

I'm showing a gradient style here of "linear", however, other styles like "radial",
"axial", "ellipsoid", "rectangle" and "square" are, **in theory** available.
(You may need to experiment to get the look you want.)


.. code:: python

    from odpslides.presentation import Presentation

    P = Presentation(grad_start_color='ff9999', grad_end_color="#ffffff", 
                     grad_angle_deg=45, grad_draw_style='linear',
                     footer='Gaea Trilogy', show_date=True)

    P.add_title_chart( title='Titan, Wizard, Demon', subtitle='John Varley')


    P.add_titled_image( title='Locus, Nebula, Hugo', image_file='Titan.jpg',
                        image_2_file='Wizard.jpg', image_3_file='Demon.jpg',
                        pcent_stretch_center=80, pcent_stretch_content=80)

    P.save( filename='varley.odp', launch=1 )


:download:`download varley.odp <./_static/varley.odp>`

:download:`download varley.py <./_static/varley.py>`




.. raw:: html

    <table border="1">
    <tr><th>PowerPoint Output</th></tr>
    
    <tr>
        <td> 
            <a  href="./_static/varley_in_PowerPoint.png">
            <img src="./_static/varley_in_PowerPoint.png" width="60%">
            </a>
        </td>
    </tr>
    
    <tr><th>LibreOfficeOffice Output</th></tr>
    <tr>
        <td> 
            <a  href="./_static/varley_in_LibreOffice.png">
            <img src="./_static/varley_in_LibreOffice.png" width="60%">
            </a>
        </td>
    </tr>
    
    </table>


`Click images to see full size`

Isaac Asimov
------------

You can't read scifi and not read Asimov. "I Robot" might be his most famous novel, but he has
many related works. 

This presentation highlights the "Foundation Series" originally a trilogy, it was exapanded on in 
later years.

The background of this presentation uses a bitmap image. The various font colors are
specified using the short color names "dm" (dark magenta) and "i" (indigo)

Note the center slide, ``P.add_titled_text_and_image``.  It uses the alternate method of entering
outline text, a list of strings.  Each member of the list is a line of outline text.
The indentation can be marked with tab characters "\t", or four spaces per indent.


.. code:: python

    from odpslides.presentation import Presentation

    P = Presentation(background_image='robot_bg_light.png',
                     title_font_color='dm', subtitle_font_color='dm',
                     footer='Foundation Trilogy', show_date=True,
                     date_font_color='i',
                     footer_font_color='i', 
                     page_number_font_color="i")

    P.add_title_chart( title='The Foundation Series', subtitle='Isaac Asimov')

    P.add_titled_text_and_image( text_location='top',
                                 title='"Best All-Time Series" in 1966', title_font_color='',  
                                 outline=["Psychohistory","    Hari Seldon's Invention",
                                 "R. Daneel Olivaw","    Humanity's Protector"], text_font_color='dm', 
                                 image_file='Foundation_Series.jpg', keep_aspect_ratio=True, 
                                 pcent_stretch_center=50, pcent_stretch_content=100)

    P.add_titled_image( title='Two Prequels, Two Sequels, Many Reprints',
                        image_file='Foudation_Series_v3.jpg',
                        image_2_file='foundation_x7.png',
                        image_3_file='Foudation_Series_v2.jpg', 
                        image_4_file='r_daneel_olivaw.jpg',
                        pcent_stretch_center=80, pcent_stretch_content=80)
                        
    P.save( filename='asimov.odp', launch=1 )


:download:`download asimov.odp <./_static/asimov.odp>`

:download:`download asimov.py <./_static/asimov.py>`


.. raw:: html

    <table border="1">
    <tr><th>PowerPoint Output</th></tr>
    
    <tr>
        <td> 
            <a  href="./_static/foundation_in_PPT.png">
            <img src="./_static/foundation_in_PPT.png" width="60%">
            </a>
        </td>
    </tr>
    </table>


`Click images to see full size`
