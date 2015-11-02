
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
