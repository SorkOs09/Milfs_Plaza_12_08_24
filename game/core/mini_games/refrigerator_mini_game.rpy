transform refrigerator_mini_game_transform(zzoom = 1.1):
    on idle:
        easein .25 zoom 1.0
    on hover:
        easeout .25 zoom zzoom
transform refrigerator_mini_game_c_lr_transform(xp = 0, yp = 0):
    alpha 1.0 xpos xp ypos yp
    easein 1.0 alpha 0.0
init python:
    _rvv = None
    class RefrigeratorMiniGameItem(renpy.Displayable):

        def __init__(self, image, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)
            self.image = Transform(image)
            self.last_mouse_pos = (0, 0)
            self.lr_list = []

        def set_clicked(self):
            self.clicked = True
        def render(self, width, height, st, at):
            

            rend = renpy.Render(1, 1)
            mouse_pos = renpy.get_mouse_pos()
            m_x = mouse_pos[0]-60
            m_y = mouse_pos[1]-50
            

            if self.last_mouse_pos != mouse_pos:
                self.last_mouse_pos = mouse_pos
                self.lr_list.append(refrigerator_mini_game_c_lr_transform(child = "mini_games/refrigerator/c_lr.png", xp = m_x, yp = m_y))
            
            for i in self.lr_list:
                if i.alpha > 0.05:

                    rend.blit(renpy.render(i,
                        55, 55, st, at), (i.xpos, i.ypos))



            rend.blit(renpy.render(self.image,
                100, 475, st, at), (m_x, m_y))

            
            # rend.blit(renpy.render(Text(str(len(self.lr_list))),
            #     100, 475, st, at), (100, 100))
            renpy.redraw(self, 0)
            
            return rend

screen refrigerator_mini_game_screen_image:
    image '#000a'
    viewport:
        xpos -250
        xmaximum 1080
        ymaximum 1080
        image '#0000'
        image "mini_games/refrigerator/refrigerator.png" xpos 30 ypos -30

    image "mini_games/refrigerator/c_ir.png":
        yanchor .5 xanchor .5 xpos 1400 ypos 500
        at transform:
            zoom 1.0
            ease .25 zoom .9
            ease .25 zoom 1.0
            ease .25 zoom .9
            ease .25 zoom 1.0
            #ease .25 zoom .9
            #easeout 5.0 zoom 1.0
            pause 1.5
            repeat
    # image "mini_games/refrigerator/l_ir.png":
    #     xpos 500
    #     ypos 50
    #     zoom .7
    if not renpy.get_screen("refrigerator_mini_game_screen"):
        viewport:
            xmaximum 1080
            ymaximum 1080
            image '#fff0'
            image "mini_games/refrigerator/basket.png"  xalign .5 yalign .5

            yanchor .5 xanchor .5 xpos 1400 ypos 500
    
screen refrigerator_mini_game_screen:
    default _item_now = -1
    default _item_now_obj = None

    #text str(len(_refrigerator_items))

    $ j = -1
    vpgrid:
        cols 2
        rows 4
        xspacing 5
        yspacing 40
        xpos 205
        ypos 155
       
        for i in refrigerator_items:
            $ j += 1
            viewport:
                xmaximum 160
                ymaximum 160
                image '#0000'
                    
                if _item_now != j and j not in _refrigerator_items:
                    imagebutton:
                        idle  i
                        hover i
                        action SetScreenVariable("_item_now", j), SetScreenVariable("_item_now_obj", RefrigeratorMiniGameItem(i))
                        at refrigerator_mini_game_transform
                        xalign .5 yalign .5
        
                
    if _item_now_obj:
        imagebutton:
            idle  '#000a'
            hover '#000a'
            action NullAction()
    
    viewport:
        xmaximum 1080
        ymaximum 1080
        image '#fff0'
        imagebutton:
            idle  "mini_games/refrigerator/basket.png" 
            hover "mini_games/refrigerator/basket.png"
            if _item_now_obj:
                if len(_refrigerator_items) +1 == len(refrigerator_items):
                    action Return()
                else:
                    action Function(_refrigerator_items.append, _item_now), SetScreenVariable("_item_now_obj", None), SetScreenVariable("_item_now", -1)
            else:
                action NullAction()
            at refrigerator_mini_game_transform
            xalign .5 yalign .5
    
        yanchor .5 xanchor .5 xpos 1400 ypos 500
    


    if _item_now_obj:
    
        add _item_now_obj

label refrigerator_mini_game_label:
    
    show screen refrigerator_mini_game_screen_image with Dissolve(.3)

    $ renpy.pause(.25, hard = True)
    call screen refrigerator_mini_game_screen

    $ renpy.pause(.1, hard = True)
    hide screen refrigerator_mini_game_screen_image with Dissolve(.3)

    $ renpy.pause(.3, hard = True)
    return