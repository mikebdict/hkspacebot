from wand.drawing import Drawing
from wand.image import Image
from os import makedirs

def img_combiner_f(picture_info_li):
    # A few strings we will need
    savefolder_str = picture_info_li[2].rsplit('/',1)[0]+'/composite/'
    filename_srt=(picture_info_li[2].rsplit('/',1)[1])
    folder_filename_str = (savefolder_str+filename_srt)
    # Create a folder to save to
    makedirs(savefolder_str, exist_ok=True)
    # The text to overaly on the image - A lot of the formating is preserved.
    fspace_txt = (f'''
Instrument name   :   {picture_info_li[0][1]}
Instrument target :   {picture_info_li[0][3]}
Time captured     :   {picture_info_li[0][2][:10]}
                      {picture_info_li[0][2][11:]}''')
    # Some defaults for all the images
    def image_defaults_f():
        img.format = 'jpeg'
        draw(img)
        img.save(filename=folder_filename_str)
# A big loop that determines the right text to overlay on the image based of information
# in OPUS JSON, resizes the images so they are the right aspect ratio for facebook and sets the
# position of the overlaid text based of the resultion of the images.
    with Drawing() as draw:    
        with Image(filename=picture_info_li[2]) as img:
            draw.font = 'Noto-Mono'      
            if picture_info_li[0][1] == 'New Horizons LORRI':
                if img.width <= 800:
                    img.resize(600, 600)
                    print('img.width <= 800')
                    img.frame(matte = 'white', width=2, height=2, inner_bevel=1, outer_bevel=1)
                    draw.fill_color = 'black'
                    draw.fill_opacity = 0.5
                    draw.rectangle(left=8, top=7, width=290, height=75)
                    draw.fill_opacity = 1
                    draw.fill_color = 'white'
                    draw.text(10, 10, fspace_txt)
                    image_defaults_f()
                elif img.width >= 800:
                    img.frame(matte = 'white', width=5, height=5, inner_bevel=2, outer_bevel=2) 
                    draw.fill_color = 'black'
                    draw.fill_opacity = 0.5
                    draw.rectangle(left=11, top=10, width=413, height=90)
                    draw.fill_opacity = 1
                    draw.fill_color = 'white'
                    draw.font_size = 16
                    draw.text(13, 20, fspace_txt)
                    image_defaults_f()

            if picture_info_li[0][1] == 'Hubble WFC3' or picture_info_li[0][1] == 'Hubble ACS':
                if img.width <= 4142:
                    img.transform(resize='x1024')
                    draw.fill_color = 'black'
                draw.fill_opacity = 0.5
                draw.rectangle(left=10, top=15, width=350, height=90)
                draw.fill_opacity = 1
                draw.fill_color = 'white'
                draw.font_size = 16
                draw.text(13, 20, fspace_txt)
                image_defaults_f()

            if picture_info_li[0][1] == 'Cassini ISS':
                img.frame(matte = 'white', width=5, height=5, inner_bevel=2, outer_bevel=2) 
                draw.fill_color = 'black'
                draw.fill_opacity = 0.5
                draw.rectangle(left=10, top=15, width=350, height=90)
                draw.fill_opacity = 1
                draw.fill_color = 'white'
                draw.font_size = 16
                draw.text(13, 20, fspace_txt)
                image_defaults_f()

            if picture_info_li[0][1] == 'Galileo SSI':
                img.frame(matte = 'white', width=5, height=5, inner_bevel=2, outer_bevel=2) 
                draw.fill_color = 'black'
                draw.fill_opacity = 0.5
                draw.rectangle(left=8, top=8, width=380, height=85)
                draw.fill_opacity = 1
                draw.fill_color = 'white'
                draw.font_size = 16
                draw.text(13, 8, fspace_txt)
                image_defaults_f()

            if picture_info_li[0][1] == 'Voyager ISS':
                img.frame(matte = 'white', width=5, height=5, inner_bevel=2, outer_bevel=2) 
                draw.fill_color = 'black'
                draw.fill_opacity = 0.5
                draw.rectangle(left=8, top=10, width=380, height=85)
                draw.fill_opacity = 1
                draw.fill_color = 'white'
                draw.font_size = 16
                draw.text(13, 8, fspace_txt)
                image_defaults_f()
    # We need the folder and image path for the posting program - 
    return folder_filename_str               