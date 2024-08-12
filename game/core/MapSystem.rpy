
image city_icon_igor = Transform(i_path+'/city_interface/city_icon_igor.png', zoom = .8)

image city_icon_gg   = Transform(i_path+'/city_interface/city_icon_gg.png', zoom = .8)

image city_icon_christie = Transform(i_path+'/city_interface/city_icon_christie.png', zoom = .8)

image city_icon_jay_bob = Transform(i_path+'/city_interface/city_icon_jay_bob.png', zoom = .8)

image city_icon_milf = Transform(i_path+'/city_interface/city_icon_milf.png', zoom = .8)

image city_icon_misha = Transform(i_path+'/city_interface/city_icon_misha.png', zoom = .8)


image city_icon_officer = Transform(i_path+'/city_interface/city_icon_officer.png', zoom = .8)


image city_icon_jokers normal = Transform(i_path+'/city_interface/city_icon_jokers_normal.png', zoom = .8)


image city_icon_jokers scared = Transform(i_path+'/city_interface/city_icon_jokers_scared.png', zoom = .8)



init python:
    def go_to_city():
        global city_click
        city_click = False
        play_map_music()
        JumpToLocation(location = 'City_Home')

    def city_walk_def():
        global location_now_i, time_now_i, location_now, city_new_location, locations, city_old_location
        
        if location_now in locations:
            

            location_now_i = locations[location_now].bg
        else:
            location_now_i = location_now
            
        time_now_i = time.time_now
        
        renpy.hide_screen('main_city_screen')

        JumpToLocation(location = city_new_location, need_time_forward = time.time_now != 'night' and location_now != city_new_location)


    def play_map_music():
        global gigiena
        
        gigiena = max(0,   gigiena-1)
        
        if time.time_now =='night':
            if not renpy.music.get_playing() or 'map' not in renpy.music.get_playing():
                renpy.music.stop(fadeout=1.5) 
                renpy.music.play('audio/map_n.mp3', fadein = 1.5)
        else:
            if not renpy.music.get_playing() or 'city' not in renpy.music.get_playing():
                renpy.music.stop(fadeout=1.5) 
                renpy.music.play('audio/city_d.mp3', fadein = 1.5)



    def play_city_music():
        if not renpy.music.get_playing() or 'city' not in renpy.music.get_playing():
            renpy.music.stop(fadeout=1.5) 
            renpy.music.play('audio/city_d.mp3', fadein = 1.5)

    city_old_location = 'City_Home'

    city_new_location = 'City_Home'

screen fake_city_screen(mpn=True):
    imagebutton:
        idle '#0000'
        hover '#0000'
        action NullAction()
    zorder 900
    if mpn:
        add 'images/interface/city_interface/city_bg_'+time.time_now+'.png'
    add 'gradient_up'
    button:
        add time.time_now+'_button'
        xalign .5
        action NullAction()

    
    add 'pause_icon' xalign .5





    add 'interface/Panel_Money.png' xalign 1.0
    text '$' + str(money) xalign .9 color '#000' ypos 40
    add 'interface/Panel_Day.png' xpos 587 ypos 30
    add 'interface/Panel_Day.png' xpos 1020 ypos 30 xzoom -1
    viewport:
        xmaximum 310
        ymaximum 90
        add '#0000'

        $ times = time.tdtd.title()
        text _(str(times)) color '#000' xalign .5 yalign .5 size 25
        xpos 587 ypos 30
    viewport:
        xmaximum 310
        ymaximum 90
        add '#0000'
        $ times = rus_time[time.time_now].title()
        text _(str(times)) xalign .5 yalign .5 color '#000' size 25
        xpos 1020 ypos 30


transform _transform_map_cloud_alpha(alpha_start=0.3, alpha_finish = 1.0, duration = .5, pause_start = 0.0):
    alpha alpha_start
    pause pause_start
    easein duration alpha alpha_finish


transform map_bg_transform():
    alpha .0
    easein .5 alpha 1.0

transform _transform_map_cloud_pos_repeat(

    xpos_start = 0.0, ypos_start = -2160.0, 

    xpos_finish = -3840.0, ypos_finish = 0.0,
    
    duration = 180.0,

    ):
    _transform_map_cloud_pos(xpos_start, ypos_start, xpos_finish, ypos_finish, duration)
    repeat

transform _transform_map_cloud_pos(
    xpos_start = 0.0, ypos_start = -2160.0, 

    xpos_finish = -3840.0, ypos_finish = 0,
    
    duration = 180.0,

    ):
                                

    xpos xpos_start ypos ypos_start
    easein_cubic duration xpos xpos_finish ypos ypos_finish
    #repeat



init python:
    def easeInOutCubic_2(t):
                #return -(math.cos(math.pi * t) - 1.0) / 2.0
        if t > .1:
            return t+.25

        t = t*10.0
        
        #t += .2

        #r = 1.0 - math.pow(1 - t, 5.0)
        if t < 0.5:
            r = 4.0 * t * t * t 

        else:
            r = 1.0 - math.pow(-2.0 * t + 2.0, 3) / 2.0

        return r*.35#/4.0

    def easeInOutCubic(t):
        #return -(math.cos(math.pi * t) - 1.0) / 2.0
            
        if t < 0.5:
            r = 4.0 * t * t * t 

        else:
            r = 1.0 - math.pow(-2.0 * t + 2.0, 3) / 2.0

        return r

transform _transform_map_cloud_pos_speed_up(
    sp_up_xpos_start, sp_up_ypos_start,

    sp_up_xpos_finish, sp_up_ypos_finish,
     
    sp_up_duration = 1.0, duration = 180.0,

    all_duration = 180.0

    ):
    
    
    xpos sp_up_xpos_start ypos sp_up_ypos_start
    
    warp easeInOutCubic sp_up_duration xpos sp_up_xpos_finish ypos sp_up_ypos_finish

    #_transform_map_cloud_pos(sp_up_xpos_start, sp_up_ypos_start, sp_up_xpos_finish, sp_up_ypos_finish, sp_up_duration)
    #block:

    _transform_map_cloud_pos(sp_up_xpos_finish, sp_up_ypos_finish, xpos_finish = -3840.0, ypos_finish = 0.0, duration = duration)
    _transform_map_cloud_pos_repeat(
        xpos_start = 0.0, ypos_start = -2160.0, 
        xpos_finish = -3840.0, ypos_finish = 0.0, duration = all_duration)

init python:
    _city_bg_mask = renpy.display.im.Image('interface/city_interface/city_bg_mask.png').load(unscaled=True)
    def _hide_map():
        global store
        if store.locations.get(store.location_now):
            store.location_now_i = store.locations[store.location_now].bg
        store.time_now_i     = time.time_now
    class MapSkyDisplayable(renpy.Displayable):

        def setup(self):
            #if not mp.clouds_anim:
            #    return
            self.map_bg = Image('interface/city_interface/city_bg_'+time.time_now+'.png')

           # self.image  = _transform_map_cloud_pos_repeat(child = self.fn, duration = self.duration)

        def __init__(self, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)
            self.map_bg_old = Image('interface/city_interface/city_bg_morning.png')
            self.map_bg = map_bg_transform(child = 'interface/city_interface/city_bg_morning.png')
            self.time   = 0

            self.last_dur = 0.0
            
            self.sp_up_duration = 1.0
            
            self.duration = 420.0

            #self.alpha_st = 0
            
            self.fn = Composite(
        (5760, 3240),
        

        (0, 0), "tests/clouds_1.png",

        (1920, 0), "tests/clouds_1.png",
        
        (3840, 0), "tests/clouds_1.png",


        (0, 1080), "tests/clouds_2.png",

        (1920, 1080), "tests/clouds_2.png",
        
        (3840, 1080), "tests/clouds_2.png",

        (0, 2160), "tests/clouds_1.png",

        (1920, 2160), "tests/clouds_1.png",
        
        (3840, 2160), "tests/clouds_1.png",

        )
            self.image  = _transform_map_cloud_pos_repeat(child = self.fn, duration = self.duration)

        def speed_up(self):
            self.map_bg_old = 'interface/city_interface/city_bg_'+time.time_now+'.png'
            
            if mp.clouds_anim:
                
                sp_up_xpos_start = float(self.image.xpos)
                
                sp_up_ypos_start = float(self.image.ypos)

                
                sp_up_duration = self.sp_up_duration



                mn = .1

                #self.alpha_st = self.image.st

                sp_up_xpos_finish = sp_up_xpos_start - 3840.0*mn


                sp_up_ypos_finish = sp_up_ypos_start + 2160.0*mn



                if sp_up_ypos_finish > 0:
                    sp_up_xpos_finish = -3839.0
                    sp_up_ypos_finish = -1.0

                    duration  = .01

                    #sp_up_duration = float(sp_up_ypos_finish)/2160.0 
                
                else:


                    duration  = self.duration
                    
                    duration -= self.duration*(math.fabs(sp_up_xpos_finish)/3840.0)
                    




                self.image  = _transform_map_cloud_pos_speed_up(

                child = self.fn,

                sp_up_xpos_start = sp_up_xpos_start, sp_up_ypos_start = sp_up_ypos_start,

                sp_up_xpos_finish = sp_up_xpos_finish, sp_up_ypos_finish = sp_up_ypos_finish,
                 
                sp_up_duration = sp_up_duration, duration = duration, all_duration = self.duration)
                
                #self.image  = _transform_map_cloud_pos_speed_up(child = self.fn, xpos_start = _x, ypos_start= _y, duration = _duration)

            time.time_forward(False, need_check_ev = False) 

            #self.image.st = 0.1
            store._city_bg_need_update = True
            store._hide_map()
            renpy.restart_interaction()

        def render(self, width, height, st, at):
            

            rend = renpy.Render(1920, 1080)

            rend.blit(renpy.render(self.image, 

            1920, 1080, st, at), (self.image.xpos, self.image.ypos))

            
            # rend.blit(renpy.render(Text(str(self.image.ypos), color = "#FFF", size = 60, outlines = [(1, '#000a', 0, 0)]), 

            # 300, 100, st, at), (100, 100))
            



            # rend.blit(renpy.render(Text(str(self.last_dur), color = "#FFF", size = 60, outlines = [(1, '#000a', 0, 0)]), 

            # 300, 100, st, at), (100, 200))
            

            renpy.redraw(self, 0)
            
            return rend

    def my_warper(t, x = 1.0):
        return t*x



    #_map_sky = MapSkyDisplayable()
    _map_sky = MapSkyDisplayable()
    _map_sky_mask = AlphaMask(_map_sky, 'interface/city_interface/city_bg_mask.png')
    _map_sky_mask_no_anim = AlphaMask("tests/clouds_1.png", 'interface/city_interface/city_bg_mask.png')
    _city_bg_need_update = False
# image _city_var = 'interface/city_interface/city_bg_[time.time_now].png'
# image _city_morning  = 'interface/city_interface/city_bg_morning.png'
# image _city_afternoon  = 'interface/city_interface/city_bg_afternoon.png'
# image _city_evening  = 'interface/city_interface/city_bg_evening.png'
# image _city_night  = 'interface/city_interface/city_bg_night.png'


image _bg_frame_2_mini_main = 'interface/comic_v2/bg_frame_2_mini.png'
image _bg_frame_2_mini_main_frame = Frame('_bg_frame_2_mini_main', Borders(64, 64, 64, 64))


image _map_city_bg_morning = 'interface/city_interface/city_bg_morning.png'
image _map_city_bg_afternoon = 'interface/city_interface/city_bg_afternoon.png'
image _map_city_bg_evening = 'interface/city_interface/city_bg_evening.png'
image _map_city_bg_night = 'interface/city_interface/city_bg_night.png'

init python:
    def _switch_clouds_anim():

        mp.clouds_anim = not mp.clouds_anim
        mp.save()
        
    if mp.clouds_anim is True:
        mp.clouds_anim = False
        mp.save()
screen main_city_screen(hides=[NullAction()]):
    default old_time = time.time_now
    zorder 900
    add zero_button
   # on "show" action SetField(_map_sky, "map_bg_old", 'interface/city_interface/city_bg_'+time.time_now+'.png')
    #image '_city_var'
    image _map_sky.map_bg_old# '_city_'+time.time_now
    image '_map_city_bg_'+time.time_now: 

        if _city_bg_need_update:
            at transform:
                alpha .0
                easein .5 alpha 1.0
    if mp.clouds_anim:

        add _map_sky_mask
    else:
        add _map_sky_mask_no_anim

    #image 'tests/cloud_1.png'
    # image 'tests/cloud_1.png':
    #     at transform:

    #         #xpos 1200 ypos 500

    #         xpos 900 ypos 800

    #         pause 3.0
    #         easein 3.0 xpos 600 ypos 1100
    # image 'tests/cloud_1.png':
    #     at transform:
    #         xpos 1800 ypos 200
    #         warp my_warper 4.0 3.0 xpos -120 ypos 1280
    add 'gradient_up'
    # hbox:
    #     xalign .01 yalign .99
    #     viewport:
    #         xmaximum 64
    #         ymaximum 64
    #         image '_bg_frame_2_mini_main' #'interface/comic_v2/bg_frame_2_mini.png' # Frame('interface/comic_v2/bg_frame_2_mini.png', Borders(30, 30, 30, 30)) 
    #         image '_bg_frame_2_mini_main'
    #         if mp.clouds_anim:
    #             text "V" size 45 italic True bold True color "#6fc276" xalign .45 yalign .9
    #         else:
    #             text "X" size 45 bold True color "#FF2C2C" xalign .5 yalign .9
    #         imagebutton:
    #             idle  '#0000'
    #             hover '_bg_frame_2_mini_main'
    #             action Function(_switch_clouds_anim)


        #image 'interface/comic_v2/bg_frame_2_mini.png' 
        # viewport:
        #     xmaximum 300
        #     ymaximum 64
        #     xpos 5
        #     image '#0000'
        #     image '_bg_frame_2_mini_main_frame' #Frame('interface/comic_v2/bg_frame_2_mini.png' , Borders(64, 64, 64, 64)) #xzoom 1.0 yzoom .5
        #     image '_bg_frame_2_mini_main_frame'
        #     #text "V" size 45 italic True bold True color "#0F0a" xalign .5 yalign .5
        #     text __("Анимация Облаков") size 30 xalign .5 yalign .5
    imagebutton:
        idle 'city_home_button'
        hover 'city_home_button'
        at ButtonEffect01
        focus_mask True
        action [
            SetVariable('city_old_location', location_now), 
            SetVariable('city_new_location', 'City_Home'), 
            Function(city_walk_def)
            ]
    imagebutton:

        idle 'city_park_button'
        hover 'city_park_button'
        at ButtonEffect01
        focus_mask True
        action [
            SetVariable('city_old_location', location_now), 
            SetVariable('city_new_location', 'City_Park'), 
            Function(city_walk_def)
            ]
    #image 'city_icon_gg' xpos 950 ypos 500









    imagebutton:
        idle 'city_shop_button'
        hover 'city_shop_button'
        at ButtonEffect01
        focus_mask True
        action [
            SetVariable('city_old_location', location_now), 
            SetVariable('city_new_location', 'City_Shop'), 
            Function(city_walk_def)
            ]


    if time.time_now != 'night' and hasattr(store, 'storein_costumes_shop_items'):

        imagebutton:
            idle 'city_clothes_shop_button'
            hover 'city_clothes_shop_button'
            at ButtonEffect01
            focus_mask True

            action [SetVariable('city_old_location', location_now), 
            SetVariable('city_new_location', 'ClothesStore'), 
            Function(city_walk_def)]




    if time.time_now not in ['evening', 'night']:
        if getattr(store, 'unlock_city_getto', False):
            
            imagebutton:

                idle 'city_getto_button'
                hover 'city_getto_button'

                at ButtonEffect01

                focus_mask True

                
                action [SetVariable('city_old_location', location_now), 
                SetVariable('city_new_location', 'City_Getto'), 
                Function(city_walk_def)]
        if getattr(store, 'unlock_city_psi', False):

            #if len(get_all_events_from_location("City_Psi", only_first = True)):

            imagebutton:

                idle 'city_psi_button'
                hover 'city_psi_button'

                at ButtonEffect01

                focus_mask True

                
                action [SetVariable('city_old_location', location_now), 
                SetVariable('city_new_location', 'City_Psi'), 
                Function(city_walk_def)]


        if getattr(store, 'unlock_city_library', False):


            imagebutton:

                idle 'city_library_button'
                hover 'city_library_button'

                at ButtonEffect01

                focus_mask True

                action [SetVariable('city_old_location', location_now), 
                SetVariable('city_new_location', 'City_Library'), 
                Function(city_walk_def)]


    # if time.time_now in ('morning', 'afternoon'):

    #     image 'city_icon_igor' xpos 850 ypos 550
    #     image 'city_icon_jay_bob' xpos 620 ypos 180

    # if time.time_now in ('morning', 'afternoon', 'evening'):

    #     image 'city_icon_misha' xpos 720 ypos 110
    


    # image 'city_icon_christie' xpos 1565 ypos 500
    

    # image 'city_icon_milf' xpos 1690 ypos 555
    

    # image 'city_icon_gg': 
    #     if location_now in ('City_Home', 'Corridor'):
    #         xpos 1580 ypos 650
    #     elif location_now == 'City_Park':
    #         xpos 960 ypos 700

    #     elif location_now in ('City_Shop', 'StoreIn'):
    #         xpos 660 ypos 280







    button:
        add time.time_now+'_button'
        xalign .5
        action [ 

        SetScreenVariable("old_time", time.time_now),
        
        Function(renpy.play, 'audio/time_forward.ogg'), 
        Function(play_map_music),
        Function(_map_sky.speed_up)
        ]
    add 'play_icon' xalign .5
    if time.time_now == 'night':
        viewport:
            xmaximum 170
            ymaximum 195
            xalign .5
            imagebutton:
                idle '#0000'
                hover '#0000'
                action NullAction()

        add 'pause_icon' xalign .5





    add 'interface/Panel_Money.png' xalign 1.0
    text '$' + str(money) xalign .9 color '#000' ypos 40
    add 'interface/Panel_Day.png' xpos 587 ypos 30
    add 'interface/Panel_Day.png' xpos 1020 ypos 30 xzoom -1
    viewport:
        xmaximum 310
        ymaximum 90
        add '#0000'

        $ times = time.tdtd.title()
        text _(str(times)) color '#000' xalign .5 yalign .5 size 25
        xpos 587 ypos 30
    viewport:
        xmaximum 310
        ymaximum 90
        add '#0000'
        $ times = rus_time[time.time_now].title()
        text _(str(times)) xalign .5 yalign .5 color '#000' size 25
        xpos 1020 ypos 30
    imagebutton xpos 35 ypos 25:
        idle 'button_no'
        hover "button_no hover" 



        if type(hides) == list:
            action hides + [SetVariable('_city_bg_need_update', False), Jump('main_interface_label')]
        else:
            action hides, SetVariable('_city_bg_need_update', False), Jump('main_interface_label')


    #add my_get_mouse_pos

label main_city_Label_ep2:
    hide screen empty_screen
    $ city_click = False
    show screen main_city_screen(hides = [SetVariable('location_now', 'Corridor'), Hide('main_city_screen', transition = Dissolve(.5)), Jump('main_interface_label')]) with Dissolve(.3)
    call screen empty_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc


screen city_walk_screen:
    zorder 900
    image '#000'
    
    # add 'gradient_up'

    add i_path + '/city_interface/city_bg_'+time.time_now+'.png'
    
    if time.time_now == 'night' or getattr(store, 'block_time_forward', False):
        pass
    else:
        add i_path + '/city_interface/city_bg_'+get_next_time()+'.png':
            at transform:
                alpha .0
                
                linear 1.15 alpha 1.0
        
    use fake_city_screen(mpn=False)

    if get_next_time() == 'afternoon':

        image 'city_icon_igor' xpos 850 ypos 550
        image 'city_icon_jay_bob' xpos 620 ypos 180
    elif get_next_time() == 'evening':
        image 'city_icon_jay_bob': 
            at transform:
                xpos 620 ypos 180 alpha 1.0
                linear .5 alpha .0
        image 'city_icon_igor': 
            at transform:
                xpos 850 ypos 550 alpha 1.0
                linear .5 alpha .0
                

    if get_next_time() == 'night':
        image 'city_icon_misha': 
            at transform:
                xpos 720 ypos 110 alpha 1.0
                linear .5 alpha .0
    elif time.time_now != 'night':

        image 'city_icon_misha' xpos 720 ypos 110
    


    image 'city_icon_christie' xpos 1565 ypos 500
    

    image 'city_icon_milf' xpos 1690 ypos 555
    

    image 'city_icon_gg': 
        if location_now in ('City_Home', 'Corridor'):
            if city_new_location == 'City_Park':
                at transform:
                    xpos 1580 ypos 650
                    easein .55 xpos 1220 ypos 530
                    pause .15
                    
                    easein .5 xpos 960 ypos 700
            elif city_new_location in ('City_Shop', 'StoreIn'):
                at transform:
                    xpos 1580 ypos 650
                    easein_cubic 1.15 xpos 660 ypos 280
            
            else:
                xpos 1580 ypos 650
            

        elif location_now == 'City_Park':
            if city_new_location == 'City_Home':
                at transform:
                    xpos 960 ypos 700
                    linear .5 xpos 1220 ypos 530
                    pause .15
                    linear .5 xpos 1580 ypos 650
            elif city_new_location in ('City_Shop', 'StoreIn'):
                at transform:
                    xpos 960 ypos 700
                    linear .3 xpos 1220 ypos 530
                    pause .15
                    easein_cubic .7 xpos 660 ypos 280
            
            else:
                
                xpos 960 ypos 700

        elif location_now in ('City_Shop', 'StoreIn'):
            if city_new_location == 'City_Home':
                at transform:
                    xpos 660 ypos 280
                    

                    easein_cubic 1.15 xpos 1580 ypos 650

            elif city_new_location == 'City_Park':
                at transform:
                    xpos 660 ypos 280
                    

                    easein .55 xpos 1220 ypos 530
                    pause .15
                    

                    easein .45 xpos 960 ypos 700
            
            else:
                
                
                xpos 660 ypos 280 







    # button:
    #     add time.time_now+'_button'
    #     xalign .5
    #     action NullAction()


    # add 'play_icon' xalign .5
    # if time.time_now == 'night':
        
    #     add 'pause_icon' xalign .5





    # add 'interface/Panel_Money.png' xalign 1.0
    # text '$' + str(money) xalign .9 color '#000' ypos 40
    # add 'interface/Panel_Day.png' xpos 587 ypos 30
    # add 'interface/Panel_Day.png' xpos 1020 ypos 30 xzoom -1
    # viewport:
    #     xmaximum 310
    #     ymaximum 90
    #     add '#0000'

    #     $ times = time.tdtd.title()
    #     text _(str(times)) color '#000' xalign .5 yalign .5 size 25
    #     xpos 587 ypos 30
    # viewport:
    #     xmaximum 310
    #     ymaximum 90
    #     add '#0000'
    #     $ times = rus_time[time.time_now].title()
    #     text _(str(times)) xalign .5 yalign .5 color '#000' size 25
    #     xpos 1020 ypos 30
    


label city_walk_label:
    $ renpy.hide_screen('main_city_screen')
    if location_now != city_new_location:
        $ renpy.show_screen('city_walk_screen')

        $ renpy.pause(1.15, hard = True)
        if time.time_now != 'night':

            $ renpy.play('audio/time_forward.ogg')
            $ time.time_forward(jump_to_main_interface = False), 
        
    $ time_now_i = time.time_now

    scene image 'locations/bg/[city_new_location]/[time_now_i].png'
    hide screen city_walk_screen 
    with Dissolve(.15)
    $ renpy.pause(.15, hard = True)


    $ JumpToLocation(location = city_new_location)
    #else:
    #    $ city_click = True
    #    $ play_map_music()
    #    $ JumpToLocation(location = city_new_location)

    jump main_interface_label