screen cards_screen:
    default _item  = get_item('Купон «кекса»', True) 
    if _item:
        default _quant = _item.quant
    else:
        default _quant = 0 

    default _cards = [
    2,
    1,
    1,
    2,
    1,
    2,
    2,
    2,
    2,
    1,
    ]
    
    imagebutton:
        idle  'black'
        hover 'black'
        action NullAction()
    image 'images/cards/bg.png'
    
    text __("Коллекция"):
        size 55 
        bold True 
        color '#ffeade' 
        xalign .5 ypos 125
    
    imagebutton:
        idle Transform('images/cards/back.png', zoom = .98)
        hover  'images/cards/back.png'
        action Hide('cards_screen', transition = Dissolve(.3))

        pos (90, 60)
         
    for ypos, range_0, range_1 in ((231, 0, 5), (520, 5, 10)):
        hbox:
            pos (445, ypos)
            spacing 17
            for i in range(range_0, range_1):

                viewport:
                    maximum (200, 283)
                    if _quant > i:
                        image Frame('cards/'+str(i)+'/0.png')
                        imagebutton:
                            idle  'alpha_solid'
                            hover '#fffa'
                            action Show('cards_screen_image', img = [str(i), _cards[i]])
                    else:
                        image Frame('cards/'+str(i)+'/0_lock.png'):
                            blur 16
                        image '#000a'
                        image 'gallery_block' align (.5, .5)


    viewport:
        maximum (250, 60)
        pos     (860, 873)
        image 'alpha_solid'
        text str(_quant) + "/10" align (.5, .5)

screen cards_screen_image(img=['0', 2]):

    default gallery_page = 0
    default gallery_page_im = 0
    default gallery_screen = 0
    
    default interface_hide = False

    imagebutton:
        idle  'alpha_solid'
        hover 'alpha_solid'
        action Hide('cards_screen_image')
    image '#000a'
    image 'cards/'+img[0]+'/'+str(gallery_page_im)+'.png':
        xalign .5

    if not interface_hide:
        hbox:
            xalign 0.5
            yalign .99

            #spacing 45
            for page in range(1, 
                img[1]+1):
                viewport:
                    xmaximum 100
                    ymaximum 100
                    image '_zero_image_button'
                    textbutton "[page]": 
                        text_outlines [(2, "#000a", 0, 0),] 
                        text_size 80 
                        text_idle_color '#fff5' 
                        text_hover_color '#fff' 
                        text_selected_color '#fff'
                        align (.5, .5)
                        action SetScreenVariable('gallery_page_im', page-1) 

    key "hide_windows" action SetScreenVariable('interface_hide', not interface_hide)