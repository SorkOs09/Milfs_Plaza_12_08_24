image circle_mini_game_red   = 'mini_games/circle_mini_game_red.png'
image circle_mini_game_black = 'mini_games/circle_mini_game.png'
image phone_frame_bg_2       = 'interface/phone_interface/phone_frame_bg_2.png'


init python:


    class QteMiniGamePhoto(renpy.Displayable):

        def __init__(self, time = 10, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)
            self.image = 'circle_mini_game_red'

            self.alpha = .5 
            self.xpos  = 400 
            self.ypos  = 500 
            self.zoom  = 2
            
            self.max_time = float(time)

            self.do_zoom = False

            self.time_start = datetime.datetime.today()

        
        def get_progress(self):
            t = (datetime.datetime.today() - self.time_start).total_seconds()/self.max_time
            
            return (1.0 - math.pow(1.0 - t, 3.0))


        def render(self, width, height, st, at):
            

            rend = renpy.Render(1, 1)
            mouse_pos = renpy.get_mouse_pos()
            
            progress = self.get_progress()

            if progress >= 1:
                self.time_start = datetime.datetime.today()
                self.do_zoom = not self.do_zoom

            if self.do_zoom:
                self.zoom = 2.0*progress
            else:
                self.zoom = 2.0 - (2.0*progress)

            rend.blit(renpy.render(Transform(self.image, zoom = self.zoom, alpha = self.alpha), 
                100, 475, st, at), (self.xpos, self.ypos))

            
            renpy.redraw(self, 0)
            
            return rend


screen qte_mini_game_photo(bg = 'location_now_image', x_pos = 790, y_pos = 200, x_align = .525, y_align = .62):
    default crop_bg = Crop((x_pos,y_pos,415,740), bg)

    on "show" action Show('circle_mini_game_red_screen', x_align = x_align, y_align = y_align)

    on "hide" action Hide('circle_mini_game_red_screen')

    

    default timer_now = 0

    # default x_align_2 = x_align + .025
    
    # default y_align_2 = y_align + .05
        
    image bg

    image '#0007'
    
    imagebutton:
        xpos x_pos ypos y_pos
        if timer_now == 2:
            idle  crop_bg

            hover crop_bg
            action Return()
        else:
            idle  crop_bg

            hover crop_bg
            at transform:
                blur 16
            action NullAction()
        

    image 'phone_frame_bg_2' xalign x_align yalign y_align zoom .94
    #add game

    if timer_now == 2:
        timer 1 repeat True action SetScreenVariable('timer_now', 0)
    else:
        timer 1 repeat True action SetScreenVariable('timer_now', timer_now+1)
    


    text str(timer_now)

    
screen circle_mini_game_red_screen(x_align = .5, y_align = .5):
    zorder 100
    image 'circle_mini_game_black': 
        at transform:
            alpha .5 xalign x_align yalign y_align zoom 1
            easein_cubic .5 zoom 3
            .5
            linear 1 zoom 1
            1
            
            
            repeat

screen qte_mini_game(ttimer = 10, qte_line = 'lrududlrlrud', shake = False, invis = False, time_line_yalign = .1, key_images_line_yalign = .6, key_buttons_line_yalign = .95):
    default xmaximum_timer = int(ttimer*100)
    default timer_align = 0

    default ttrtimer_now   = 0
    default qte_line_now = 0
    
    $ timer_align = 1.0 - float(ttrtimer_now)/xmaximum_timer
    

    if timer_align > .5:
        timer 1 repeat True action SetScreenVariable('ttrtimer_now', ttrtimer_now+150)

    elif timer_align > .3:
        timer 1 repeat True action SetScreenVariable('ttrtimer_now', ttrtimer_now+75)
    
    elif timer_align > .15:
        timer 1 repeat True action SetScreenVariable('ttrtimer_now', ttrtimer_now+50)

    elif timer_align > .0:
        timer 1 repeat True action SetScreenVariable('ttrtimer_now', ttrtimer_now+30)





    else:
        timer 1 repeat True action Return(0)


    # text str(timer_align) xalign .5

    # text str(ttrtimer_now) xalign .5 ypos 75
    # text str(20+1000*(timer_align)) xalign .5 ypos 200
    viewport:
        xalign .5 yalign time_line_yalign
        xmaximum 1000
        ymaximum 100
        image 'time_line_bg'
        viewport:
            xmaximum int(20+1000*(timer_align))# - (1000*( math.sqrt(1.0 - math.pow((ttrtimer_now/xmaximum_timer) - 1.0, 2)) )))
            ymaximum 100
            image 'time_line_fg'
    if qte_line_now +1 <= len(qte_line):

        if qte_line[qte_line_now] == 'u':
            key "K_UP" action SetScreenVariable('qte_line_now', qte_line_now+1)
            
        elif qte_line[qte_line_now] == 'd':
            key "K_DOWN" action SetScreenVariable('qte_line_now', qte_line_now+1)
        elif qte_line[qte_line_now] == 'l':
            key "K_LEFT" action SetScreenVariable('qte_line_now', qte_line_now+1)
        elif qte_line[qte_line_now] == 'r':
            key "K_RIGHT" action SetScreenVariable('qte_line_now', qte_line_now+1)
    else:
        timer .5 repeat True action Return(1)
    hbox:
        xalign .5 yalign key_images_line_yalign
        #spacing 10

        for i in qte_line[:qte_line_now]:
            
            image "key_" + i
        
        $ j = 0
        for i in qte_line[qte_line_now:]:
            image "key_" + i:   
                if j and invis:
                    alpha 0.0
                else:
                    alpha .5

                if shake:
                    if not j:
                        at transform:
                            easein_cubic .1 xpos 5
                            easein_cubic .1 xpos -5
                            repeat
            $ j += 1
    if qte_line_now +1 <= len(qte_line):
            
        hbox:
            xalign .5 yalign key_buttons_line_yalign
            vbox:
                viewport:
                    xmaximum 95
                    ymaximum 108
                    image '#0000'
                

                imagebutton:
                    idle Transform('key_l', zoom = .8)
                    hover Transform('key_l', zoom = .8)
                    if qte_line[qte_line_now] == 'l':
                        action SetScreenVariable('qte_line_now', qte_line_now+1)
                    else:
                        action NullAction()
            vbox:
                imagebutton:
                    idle Transform('key_u', zoom = .8)
                    hover Transform('key_u', zoom = .8)
                    action NullAction()
                    if qte_line[qte_line_now] == 'u':
                        action SetScreenVariable('qte_line_now', qte_line_now+1)
                    else:
                        action NullAction()
                imagebutton:
                    idle Transform('key_d', zoom = .8)
                    hover Transform('key_d', zoom = .8)
                    if qte_line[qte_line_now] == 'd':
                        action SetScreenVariable('qte_line_now', qte_line_now+1)
                    else:
                        action NullAction()
            vbox:
                viewport:
                    xmaximum 95
                    ymaximum 108
                    image '#0000'
                

                imagebutton:
                    idle Transform('key_r', zoom = .8)
                    hover Transform('key_r', zoom = .8)
                    if qte_line[qte_line_now] == 'r':
                        action SetScreenVariable('qte_line_now', qte_line_now+1)
                    else:
                        action NullAction()