
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
