
from odpslides.presentation import Presentation

P = Presentation(grad_start_color='ff9999', grad_end_color="#ffffff", 
                 grad_angle_deg=45, grad_draw_style='linear',
                 footer='Gaea Trilogy', show_date=True)

P.add_title_chart( title='Titan, Wizard, Demon', subtitle='John Varley')


P.add_titled_image( title='Locus, Nebula, Hugo', image_file='Titan.jpg',
                    image_2_file='Wizard.jpg', image_3_file='Demon.jpg',
                    pcent_stretch_center=80, pcent_stretch_content=80)

P.save( filename='varley.odp', launch=1 )
