
.. examples


Examples
========

Slan, by A.E. vanVogt
---------------------

As a kid, Slan is one of the first scifi novels I read. 
This is a simple slide presentation about that book.

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

:download:`download slan.ods <./_static/slan.odp>`

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