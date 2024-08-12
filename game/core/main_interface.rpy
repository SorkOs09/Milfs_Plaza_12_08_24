init -5000 python:

    eng_tdtd = {
     'Понедельник' : 'Monday',
     'Вторник' : 'Tuesday',
     'Среда' : 'Wednesday',
     'Четверг' : 'Thursday',
     'Пятница' : 'Friday',
     'Суббота' : 'Saturday',
     'Воскресенье' : 'Sunday'

    }

    rus_time = {
    'morning'   : 'Утро',
    'afternoon' : 'День',
    'evening'   : 'Вечер',
    'night'     : 'Ночь',

    }
    def pop_up_new_event(text = ""): 
        show_text_animation(text)

    def show_descript_screen():
        global old_descript, descript
        
        Show('descript_screen')()

    def get_imagebuttons_from_location(location_name):
        global list_files, locations, time


        rtrn_list = []
        

        if location_name not in locations:
            return rtrn_list
        
        _location = locations[location_name]


        for i in list(_location.image_buttons):
            _img = 'images/locations/imagebuttons/' + location_name + '/' + i + '.png'
            if _img in list_files or _img[7:] in list_files:
                rtrn_list.append(i)

        if time.time_now not in _location.image_buttons_times:
            return rtrn_list

        for i in list(_location.image_buttons_times[time.time_now]):
            
            _img = 'images/locations/imagebuttons/' + location_name + '/' + i + '.png'
            if _img in list_files or _img[7:] in list_files:
                rtrn_list.append(i)


        return rtrn_list

    def stnd_music_play():
        if getattr(store, 'location_now', 0) != 'Prison':
            if time.time_now == 'night':
                if not renpy.music.get_playing() or '/night.mp3' not in renpy.music.get_playing():
                    renpy.music.stop(fadeout=1.5) 
                    renpy.music.play('audio/night.mp3', fadein = 1.5)
            
            elif time.time_now == 'morning':
                if not renpy.music.get_playing() or '/morning.mp3' not in renpy.music.get_playing():
                    renpy.music.stop(fadeout=1.5) 
                    renpy.music.play('audio/morning.mp3', fadein = 1.5)
            
            
            else:
                if not renpy.music.get_playing() or '/day.mp3' not in renpy.music.get_playing():
                    renpy.music.stop(fadeout=1.5) 
                    renpy.music.play('audio/day.mp3', fadein = 1.5)
        else:
            if not renpy.music.get_playing() or '/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3' not in renpy.music.get_playing():
                renpy.music.stop(fadeout=1.5) 
                renpy.music.play("audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3", fadein = 1.5)

                
    def get_comic_array(comic_string = '', i_p = False):
        rtrn_array = []
        v          = ''
        
        tmp_comic_string = copy.deepcopy(comic_string.split(' '))
        last_i     = ''
        last_v     = ''
        s_n        = 0
        for i in comic_string.split(' '):
            
            v     += ' ' + i
            
            
            if len(v) + len(i) + 1 > 35:
                s  = []
                
                if i_p:
                    v = '{i}' + v + '{/i}'
                s.append(v)
                
                tmp_comic_string.remove(i)
                
                rtrn_array.append(s)
                
                v  = ''
                s_n   += 1
        if len(v):
            
            s  = []
            if i_p:
                v = '{i}' + v + '{/i}'
            s.append(v)
            rtrn_array.append(s)
        
        return rtrn_array


screen rtrn_screen(img='cg/christie_root/activate_psi.png', hvr=None, show_icons_interface = True, with_transform = False, with_hovered = False):
    if hvr is None:
        default hover_image = im.MatrixColor(img, im.matrix.brightness(.3))
    else:
        default hover_image = hvr

    imagebutton:
        idle img
        if with_hovered:
            hovered Return()
        hover hover_image
        focus_mask True

        action Return()
    if show_icons_interface:
        use icons_interface(with_transform=with_transform)


screen comic_frame(txt=_('!'), xp=0, yp=0, xz=1, end_img='interface/comic_frame_end_1.png', i_p=False, yz = True, xlgn = 1.0, xlgn_text = 1.0):
    default lang_check = preferences.language in ('kor', 'jap', 'chinese_simpl', 'chinese_trad')
    vbox:
        xpos xp ypos yp yalign 1.0
        $ lv = get_comic_array(__(txt), i_p)
        viewport:
            xmaximum 650
            image '#0000'
            if yz:

                ymaximum 15
                add 'interface/comic_frame_start.png': 
                    xzoom xz xalign xlgn
                    

            else:
                ymaximum 40
                add end_img xzoom xz yzoom -1 xalign xlgn
        for i in lv:
            viewport:
                xmaximum 650
                image '#0000'
                if len(lv)==1:
                    ymaximum 42
                else:
                    ymaximum 32
                add 'interface/comic_frame.png' xzoom xz xalign xlgn
                viewport:
                    add '#0000'
                    if len(lv)==1:
                        ymaximum 42
                    else:
                        ymaximum 32
                    if xz == 1:
                        xmaximum 640
                        xpos 10
                    else:

                        xmaximum 600


                    text i:
                        if lang_check:
                            size 18

                        else:

                            size 28
                        yalign .5
                        if xz != 1:
                            xalign xlgn_text
        viewport:
            xmaximum 650
            add '#fff0'

            if yz:
                if 'comic_frame_end_' in end_img:
                    ymaximum 40
                    add end_img xzoom xz ypos -7 xalign xlgn

                else:

                    ymaximum 60
                    add end_img xzoom xz ypos -7 xalign xlgn
            else:
                ymaximum 20
                add 'interface/comic_frame_start.png' xzoom xz yzoom -1 ypos -40 xalign xlgn
                


    key "dismiss" action Return()

    if renpy.get_screen("skip_indicator"):
        timer .1 action Return()

    imagebutton:
        idle '#0000'
        hover '#0000'
        action Return()
screen main_interface_hotspot_buttons_default:
    default loc = locations[location_now]

    for hov in xrange(len(loc.buttons)):
        $ btns = loc.buttons[hov]
        imagemap:

            ground '#0000'





            hover 'locations/buttons/'+str(loc.bg)+'_hover_'+str(hov)+'.png'

            for btn in btns:
                hotspot (
                    btns[btn][0][0], 
                    btns[btn][0][1], 
                    btns[btn][0][2], 
                    btns[btn][0][3], 
                ):
                    if not (getattr(store, 'block_exit_home', False) and ('City' in btn)):
                        if 'City' in btn:
                            clicked  [Function(_map_sky.setup), Hide('icons_interface', transition = Dissolve(.2)), btns[btn][1]] at ButtonEffect01 focus_mask None
                        else:
                            clicked  [Hide('icons_interface', transition = Dissolve(.2)), btns[btn][1]] at ButtonEffect01 focus_mask None
                    else:
                        clicked [Hide('icons_interface', transition = Dissolve(.2)), Jump('block_exit_home_label')] at ButtonEffect01 focus_mask None


screen main_interface:
    zorder 10



    if location_now in locations:
        if location_now == "Prison":
            use main_interface_hotspot_buttons_final_act 
        else:
            use main_interface_hotspot_buttons_default

        if not renpy.get_screen('choose_quest_screen'):
            if not getattr(store, 'block_milf_home', False):
                if milf_position[time.time_now][0] == location_now and not (sister_position[time.time_now][0] == 'Kitchen' and milf_position[time.time_now][0] == 'Kitchen'):
                    if milf_costume != 'n_body':
                        imagebutton:
                            idle 'images/cg/milf_and_sister_activities/' + milf_position[time.time_now][1] + "_" + milf_costume + '.png'

                            hover im.MatrixColor( 'images/cg/milf_and_sister_activities/' + milf_position[time.time_now][1] + "_" + milf_costume + '.png', im.matrix.brightness(.3))
                            at ButtonEffect01
                            focus_mask True
                            action [Hide('icons_interface', transition = Dissolve(.2)), Function(renpy.jump, 'talk_with_milf_label')]

                    else:
                        imagebutton:
                            idle 'images/cg/milf_and_sister_activities/' + milf_position[time.time_now][1] + '.png'

                            hover im.MatrixColor( 'images/cg/milf_and_sister_activities/' + milf_position[time.time_now][1] + '.png', im.matrix.brightness(.3))
                            at ButtonEffect01
                            focus_mask True
                            action [Hide('icons_interface', transition = Dissolve(.2)), Function(renpy.jump, 'talk_with_milf_label')]



            if not getattr(store, 'block_sister_home', False):
                if sister_position[time.time_now][0] == location_now:
                    if christie_costume != 'n_body':
                        imagebutton:
                            idle 'images/cg/milf_and_sister_activities/' + sister_position[time.time_now][1] +"_"+christie_costume + '.png'

                            hover im.MatrixColor( 'images/cg/milf_and_sister_activities/' + sister_position[time.time_now][1] +"_"+christie_costume + '.png', im.matrix.brightness(.3))
                            at ButtonEffect01
                            focus_mask True
                            action [Hide('icons_interface', transition = Dissolve(.2)), Function(renpy.jump, 'talk_with_sister_label')]

                    else:
                        imagebutton:
                            idle 'images/cg/milf_and_sister_activities/' + sister_position[time.time_now][1] + '.png'

                            hover im.MatrixColor( 'images/cg/milf_and_sister_activities/' + sister_position[time.time_now][1] + '.png', im.matrix.brightness(.3))
                            at ButtonEffect01
                            focus_mask True
                            action [Hide('icons_interface', transition = Dissolve(.2)), Function(renpy.jump, 'talk_with_sister_label')]


            if not getattr(store, 'block_igor_position', False):
                if igor_position[time.time_now][0] == location_now:

                    imagebutton:
                        idle 'images/cg/igor_activities/' + igor_position[time.time_now][1] + '.png'

                        hover im.MatrixColor('images/cg/igor_activities/' + igor_position[time.time_now][1] + '.png', im.matrix.brightness(.3))
                        at ButtonEffect01
                        focus_mask True
                        action [Hide('icons_interface', transition = Dissolve(.2)), Function(renpy.jump, 'talk_with_igor_label')]




            for i in locations[location_now].image_buttons:
                $ _img = 'images/locations/imagebuttons/' + location_now + '/' + i + '.png'
                if _img in list_files or _img[7:] in list_files:
                    imagebutton:
                        idle _img
                        hover im.MatrixColor(_img, im.matrix.brightness(.3))
                        at ButtonEffect01
                        focus_mask True
                        action [Hide('icons_interface', transition = Dissolve(.2)), locations[location_now].image_buttons[i]]


            for i in locations[location_now].image_buttons_times[time.time_now]:
                if locations[location_now].image_buttons_times[time.time_now][i] is not None:
                    $ _img = 'images/locations/imagebuttons/' + location_now + '/' + i + '.png'
                    if _img in list_files or _img[7:] in list_files:

                        imagebutton:
                            idle _img

                            hover im.MatrixColor(_img, im.matrix.brightness(.3))
                            at ButtonEffect01
                            focus_mask True

                            action [Hide('icons_interface', transition = Dissolve(.2)), locations[location_now].image_buttons_times[time.time_now][i]]




            if (location_now == 'Restroom' and 'Corridor' in locations[location_now].buttons[0]
                ) or(
                location_now == 'Milf_Room' and 'Hall' in locations[location_now].buttons[0]) or(
                location_now == 'Sister_Room' and len(locations[location_now].buttons) and 'Corridor' in locations[location_now].buttons[0]):
                add 'back_button':
                       
                    ypos 35
                imagebutton:
                    
                    ypos 35
                    idle 'back_button_hover'
                    hover 'back_button_hover'
                    focus_mask True
                    at ButtonEffect01
                    if location_now in ['Restroom', 'Sister_Room']:

                        action locations[location_now].buttons[0]['Corridor'][1]

                    else:

                        action locations[location_now].buttons[0]['Hall'][1]






screen icons_interface(click=True, with_transform = False):
    zorder 15
    viewport:
        xmaximum 1920
        ymaximum 1080
        if with_transform:
            at transform:
                on show:
                    alpha 0.0
                    easein 1.0 alpha 1.0
        if mp.interface_scale_number != 1.0:



            viewport:
                image '#fff0'
                

                if mp.interface_scale_number > 1.5:
                    at transform:
                        yalign .5
                        zoom mp.interface_scale_number
                    xmaximum 150
                    ymaximum 550
                            
                elif mp.interface_scale_number > 1.0:
                    at transform:
                        yalign .0
                        zoom mp.interface_scale_number
                    xmaximum 300
                    ymaximum 300

                else:
                    at transform:
                        yalign .0
                        xalign .0 
                        zoom mp.interface_scale_number
                    
                    xmaximum 600
                    ymaximum 170
                button:
                    if mp.interface_scale_number > 1.0:
                        if mp.interface_scale_number > 1.5:
                            ypos 295 xpos 0
                        else:
                            ypos 165 xpos 0
                    else:
                        ypos 20 xpos 260
                    add 'quest_button'
                    if click:
                        action Function(show_descript_screen)
                    else:
                        action NullAction()
                if (old_descript != descript and descript not in ("!", "") ) or (
                    getattr(store, 'old_descript_Christie', '!') != getattr(store, 'descript_Christie', '!')) or (
                    getattr(store, 'old_descript_Cat', '!') != getattr(store, 'descript_Cat', '!')) or getattr(store, 'new_events', False) or (
                    getattr(store, 'old_descript_Misha', '!') != getattr(store, 'descript_Misha', '!')) or (
                    hasattr(store, 'new_events_christie') and new_events_christie):
                
                    add 'warning_icon': 
                        if mp.interface_scale_number > 1.0:
                            if mp.interface_scale_number > 1.5:
                                xpos 82 ypos 375
                            else:
                                xpos 80 ypos 245
                        else:
                            xpos 340 ypos 100
                    

                button: 
                    if mp.interface_scale_number > 1.5:
                        ypos 165 xpos 0
                    else:
                        ypos 20 xpos 130
                    add 'bag_button'
                    if click:
                        action Show('bag_interface')
                    else:
                        action NullAction()


                button:
                    add 'mobile_button'
                    if click:
                        action [Function(renpy.play, 'audio/mobile.ogg'), Show('phone_interface')]
                    else:
                        action NullAction()
                if get_sms_check():
                    add 'warning_icon' xpos 60 ypos 115

                if 'City' in location_now and not getattr(store, 'block_map', False):
            
                    button:
                        if mp.interface_scale_number > 1.0:
                            if mp.interface_scale_number > 1.5:
                                ypos 425 xpos 0
                            else:
                                ypos 165 xpos 130
                        else:
                            ypos 20 xpos 400
                        add 'map_button'
                        if click:
                            
                            action [Show('main_city_screen', hides = [Hide('main_city_screen')]), Function(play_map_music)]
                        
                        else:
                            action NullAction()

       
            viewport:
                xmaximum 340
                ymaximum 135
                
                if mp.interface_scale_number == 2.0:
                    at transform:
                        xalign 1.0
                        yalign .4
                        zoom mp.interface_scale_number
                    
                elif mp.interface_scale_number > 1.3:
                    at transform:
                        xalign 1.0
                        yalign .3
                        zoom mp.interface_scale_number
                    
                else:
                    at transform:
                        xalign 1.0
                        yalign .0
                        zoom mp.interface_scale_number
               
                image '#fff0'
                image 'interface/Panel_Money.png'
                
                text '$' + str(money) xalign .35 color '#000' ypos 40
       
        
            viewport:
                xmaximum 740
                ymaximum 220
                image '#fff0'
                #text str(mp.interface_scale_number)    
                if mp.interface_scale_number == 2.0:
                    at transform:
                        xalign .8
                        yalign .0
                        zoom mp.interface_scale_number
               
                    
                else:
                    at transform:
                        xalign .5
                        yalign .0
                        zoom mp.interface_scale_number
                        
                

                if not getattr(store, 'not_survival', False):

                    add 'survival_icons' xalign .5 ypos 100
                    
                    viewport:
                        xmaximum 50
                        ymaximum 30
                        xpos 250
                        ypos 132
                        add 'alpha_solid'
                        text str(nastroi) xalign .5 yalign .5 size 20 color '#000'


                    viewport:
                        xmaximum 50
                        ymaximum 30
                        xpos 360
                        ypos 165
                        add 'alpha_solid'
                        text str(sitost) xalign .5 yalign .5 size 20 color '#000'



                    viewport:
                        xmaximum 50
                        ymaximum 30
                        xpos 460
                        ypos 132
                        add 'alpha_solid'
                        text str(gigiena) xalign .5 yalign .5 size 20 color '#000'
                

                    # viewport:
                    #     xmaximum 50
                    #     ymaximum 30
                    #     xpos 250
                    #     ypos 132
                    #     add 'alpha_solid'
                    #     text str(nastroi) xalign .5 yalign .5 size 20 color '#000'


                    # viewport:
                    #     xmaximum 50
                    #     ymaximum 30
                    #     xpos 360
                    #     ypos 165
                    #     add 'alpha_solid'
                    #     text str(sitost) xalign .5 yalign .5 size 20 color '#000'



                    # viewport:
                    #     xmaximum 50
                    #     ymaximum 30
                    #     xpos 460
                    #     ypos 132
                    #     add 'alpha_solid'
                    #     text str(gigiena) xalign .5 yalign .5 size 20 color '#000'


                button:
                    add time.time_now+'_button'
                    xalign .5
                    if not getattr(store,  'block_time_forward', False) and click:
                        action [Function(renpy.play, 'audio/time_forward.ogg'), Function(time.time_forward)]
                    else:
                        action NullAction()

                if location_now in ('Hall', 'GG_Room', 'Prison') and time.time_now != 'night' and not getattr(store,  'block_time_forward', False):

                    add 'play_icon' xalign .5

                else:
                    viewport:
                        xmaximum 170
                        ymaximum 195
                        xalign .5
                        imagebutton:
                            idle 'alpha_solid'
                            hover 'alpha_solid'
                            action NullAction()

                    add 'pause_icon' xalign .5
                
                add 'interface/Panel_Day.png' xpos -3 ypos 30
                add 'interface/Panel_Day.png' xpos 430 ypos 30 xzoom -1
                viewport:
                    xmaximum 310
                    ymaximum 90
                    add 'alpha_solid'
                    $ times = time.tdtd.title()
                    text __(str(times)) color '#000' xalign .5 yalign .5 size 25
                    xpos -3 ypos 30
                viewport:
                    xmaximum 310
                    ymaximum 90
                    add 'alpha_solid'

                    $ times = rus_time[time.time_now].title()
                    text __(str(times)) xalign .5 yalign .5 color '#000' size 25
                    xpos 430 ypos 30


        else:

            button ypos 20 xpos 260:
                add 'quest_button'
                if click:
                    action Function(show_descript_screen)
                else:
                    action NullAction()
            if (old_descript != descript and descript not in ("!", "") ) or (
            getattr(store, 'old_descript_Christie', '!') != getattr(store, 'descript_Christie', '!')) or (
            getattr(store, 'old_descript_Cat', '!') != getattr(store, 'descript_Cat', '!')) or getattr(store, 'new_events', False) or (
            getattr(store, 'old_descript_Misha', '!') != getattr(store, 'descript_Misha', '!')) or (
            hasattr(store, 'new_events_christie') and new_events_christie):
            
                add 'warning_icon' xpos 340 ypos 100
           
            button ypos 20 xpos 130:
                add 'bag_button'
                if click:

                    action Show('bag_interface')
                else:
                    action NullAction()

            button:
                add 'mobile_button'
                action [Function(renpy.play, 'audio/mobile.ogg'), Show('phone_interface')]
            if get_sms_check():
                add 'warning_icon' xpos 60 ypos 115
            if 'City' in location_now and not getattr(store, 'block_map', False):
                button ypos 20 xpos 400:

                    add 'map_button'
                    if click:

                        action [Show('main_city_screen', hides = [Hide('main_city_screen')]), Function(play_map_music)]
                        
                    else:
                        action NullAction()






            if not getattr(store, 'not_survival', False):

                add 'survival_icons' xalign .5 ypos 100
                viewport:
                    xmaximum 50
                    ymaximum 30
                    xpos 840
                    ypos 132
                    add 'alpha_solid'
                    text str(nastroi) xalign .5 yalign .5 size 20 color '#000'


                viewport:
                    xmaximum 50
                    ymaximum 30
                    xpos 950
                    ypos 165
                    add 'alpha_solid'
                    text str(sitost) xalign .5 yalign .5 size 20 color '#000'



                viewport:
                    xmaximum 50
                    ymaximum 30
                    xpos 1050
                    ypos 132
                    add 'alpha_solid'
                    text str(gigiena) xalign .5 yalign .5 size 20 color '#000'


                    # viewport:
                    #     xmaximum 50
                    #     ymaximum 30
                    #     xpos 250
                    #     ypos 132
                    #     add 'alpha_solid'
                    #     text str(nastroi) xalign .5 yalign .5 size 20 color '#000'


                    # viewport:
                    #     xmaximum 50
                    #     ymaximum 30
                    #     xpos 360
                    #     ypos 165
                    #     add 'alpha_solid'
                    #     text str(sitost) xalign .5 yalign .5 size 20 color '#000'



                    # viewport:
                    #     xmaximum 50
                    #     ymaximum 30
                    #     xpos 460
                    #     ypos 132
                    #     add 'alpha_solid'
                    #     text str(gigiena) xalign .5 yalign .5 size 20 color '#000'

            button:
                add time.time_now+'_button'
                xalign .5
                if not getattr(store,  'block_time_forward', False) and click:
                    action [Function(renpy.play, 'audio/time_forward.ogg'), Function(time.time_forward)]
                else:
                    action NullAction()

            if location_now in ('Hall', 'GG_Room', 'Prison') and time.time_now != 'night' and not getattr(store,  'block_time_forward', False):

                add 'play_icon' xalign .5

            else:
                viewport:
                    xmaximum 170
                    ymaximum 195
                    xalign .5
                    imagebutton:
                        idle 'alpha_solid'
                        hover 'alpha_solid'
                        action NullAction()

                add 'pause_icon' xalign .5




            add 'interface/Panel_Money.png' xalign 1.0
            text '$' + str(money) xalign .9 color '#000' ypos 40
            add 'interface/Panel_Day.png' xpos 587 ypos 30
            add 'interface/Panel_Day.png' xpos 1020 ypos 30 xzoom -1
            viewport:
                xmaximum 310
                ymaximum 90
                add 'alpha_solid'
                $ times = time.tdtd.title()
                text _(str(times)) color '#000' xalign .5 yalign .5 size 25
                xpos 587 ypos 30
            viewport:
                xmaximum 310
                ymaximum 90
                add 'alpha_solid'

                $ times = rus_time[time.time_now].title()
                text _(str(times)) xalign .5 yalign .5 color '#000' size 25
                xpos 1020 ypos 30




    if hasattr(store, 'final_act_prison_start'):
       use prison_survival_screen


    # viewport:
    #     xmaximum 125
    #     ymaximum 125
    #     ypos 200-50*getattr(store, 'not_survival', False)
    #     xalign .5
    #     image 'alpha_solid'
    #     imagebutton:
    #         xalign .5
    #         yalign .5
    #         idle  'quest_icon_bg'
    #         hover 'quest_icon_bg'
    #         focus_mask None
    #         at transform:
    #             on idle:
    #                 easeout .3 rotate 0
    #             on hover:
    #                 easein .3 rotate 90

    #         action SetField(persistent, 'first_show_choose_quest_screen_up', True), SetField(persistent, 'event_for_preview', -1), Jump('choose_quest_show_label')

    #     image 'quest_icon_mark':
    #         xalign .5 yalign .5
    #         at transform:
    #             zoom 1.0
    #             1
    #             easein .3 zoom .7
    #             easein .3 zoom 1.0
    #             easein .3 zoom .7
    #             easein .3 zoom 1.0
    #             3
    #             repeat





screen tutorial_screen:
    
    imagebutton: 
        idle  '#000c'
        hover '#000c'
        action Function(set_mp_tutorial, True), Return()
    image 'interface/tutorial.png'
    use icons_interface(click=False)
    #image Text(_('Отправить баг репорт'), font = 'fonts/mini_game.ttf', outlines = [(3, '#F00c', 0, 0)]) xpos 1500 ypos 845
    vbox:
        xpos 430 ypos 740
        image Text(_('Изменить скейл интерфейса, для устройств'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)]) xalign .5
        image Text(_('с маленьким экраном (например андроид)'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)]) xalign .5
        
    image Text(_('Инвентарь'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)]) xpos 110 ypos 390
    image Text(_('Квесты'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)]) xpos 543 ypos 314








define tmp_image_buttons_1_v = '1'
define tmp_image_buttons_2_v = '2'
define tmp_image_buttons_3_v = '3'
define tmp_image_buttons_4_v = '4'
define tmp_image_buttons_5_v = '5'
define tmp_image_buttons_6_v = '6'
define tmp_image_buttons_7_v = '7'
define tmp_image_buttons_8_v = '8'
define tmp_image_buttons_9_v = '9'
define tmp_image_buttons_10_v = '10'

image tmp_image_buttons_1 = 'locations/imagebuttons/[location_now_i]/[tmp_image_buttons_1_v].png'
image tmp_image_buttons_2 = 'locations/imagebuttons/[location_now_i]/[tmp_image_buttons_2_v].png'
image tmp_image_buttons_3 = 'locations/imagebuttons/[location_now_i]/[tmp_image_buttons_3_v].png'
image tmp_image_buttons_4 = 'locations/imagebuttons/[location_now_i]/[tmp_image_buttons_4_v].png'
image tmp_image_buttons_5 = 'locations/imagebuttons/[location_now_i]/[tmp_image_buttons_5_v].png'
image tmp_image_buttons_6 = 'locations/imagebuttons/[location_now_i]/[tmp_image_buttons_6_v].png'
image tmp_image_buttons_7 = 'locations/imagebuttons/[location_now_i]/[tmp_image_buttons_7_v].png'
image tmp_image_buttons_8 = 'locations/imagebuttons/[location_now_i]/[tmp_image_buttons_8_v].png'
image tmp_image_buttons_9 = 'locations/imagebuttons/[location_now_i]/[tmp_image_buttons_9_v].png'
image tmp_image_buttons_10 = 'locations/imagebuttons/[location_now_i]/[tmp_image_buttons_10_v].png'

image location_now_image = 'locations/bg/[location_now_i]/[time_now_i].png'
image error_background = 'interface/error_background.png'
define location_now_i = '1'
define time_now_i = '1'

init python:
    
    scene_lists = renpy.display.core.scene_lists
    def show(name, at_list=[ ], layer=None, what=None, zorder=None, tag=None, behind=[ ], atl=None, transient=False, munge_name=True):
        print("!"+str(name))
        """
        :doc: se_images
        :args: (name, at_list=[], layer='master', what=None, zorder=0, tag=None, behind=[])

        Shows an image on a layer. This is the programmatic equivalent of the show
        statement.

        `name`
            The name of the image to show, a string.

        `at_list`
            A list of transforms that are applied to the image.
            The equivalent of the ``at`` property.

        `layer`
            A string, giving the name of the layer on which the image will be shown.
            The equivalent of the ``onlayer`` property. If None, uses the default
            layer associated with the tag.

        `what`
            If not None, this is a displayable that will be shown in lieu of
            looking on the image. (This is the equivalent of the show expression
            statement.) When a `what` parameter is given, `name` can be used to
            associate a tag with the image.

        `zorder`
            An integer, the equivalent of the ``zorder`` property. If None, the
            zorder is preserved if it exists, and is otherwise set to 0.

        `tag`
            A string, used to specify the image tag of the shown image. The
            equivalent of the ``as`` property.

        `behind`
            A list of strings, giving image tags that this image is shown behind.
            The equivalent of the ``behind`` property.
        """

        default_transform = renpy.config.default_transform

        if renpy.game.context().init_phase:
            raise Exception("Show may not run while in init phase.")

        if not isinstance(name, tuple):
            name = tuple(name.split())

        if zorder is None and not renpy.config.preserve_zorder:
            zorder = 0

        sls = scene_lists()
        key = tag or name[0]

        layer = renpy.exports.default_layer(layer, key)

        if renpy.config.sticky_positions:
            if not at_list and key in sls.at_list[layer]:
                at_list = sls.at_list[layer][key]

        if not at_list:
            tt = renpy.config.tag_transform.get(key, None)
            if tt is not None:
                if not isinstance(tt, list):
                    at_list = [ tt ]
                else:
                    at_list = list(tt)

        if what is None:
            what = name
        elif isinstance(what, basestring):
            what = tuple(what.split())

        if isinstance(what, renpy.display.core.Displayable):

            if renpy.config.wrap_shown_transforms and isinstance(what, renpy.display.motion.Transform):
                base = img = renpy.display.image.ImageReference(what, style='image_placement')

                # Semi-principled, but mimics pre-6.99.6 behavior - if `what` is
                # already a transform, do not apply the default transform to it.
                default_transform = None

            else:
                base = img = what

        else:
            name, what = _find_image(layer, key, name, what)
            base = img = renpy.display.image.ImageReference(what, style='image_placement')

            if not base.find_target() and renpy.config.missing_show:
                result = renpy.config.missing_show(name, what, layer)

                if isinstance(result, renpy.display.core.Displayable):
                    base = img = result
                elif result:
                    return

        for i in at_list:
            if isinstance(i, renpy.display.motion.Transform):
                img = i(child=img)
            else:
                img = i(img)

            # Mark the newly created images unique.
            img._unique()

        # Update the list of images we have ever seen.
        renpy.game.persistent._seen_images[tuple(str(i) for i in name)] = True

        if tag and munge_name:
            name = (tag,) + name[1:]

        if renpy.config.missing_hide:
            renpy.config.missing_hide(name, layer)

        sls.add(layer, img, key, zorder, behind, at_list=at_list, name=name, atl=atl, default_transform=default_transform, transient=transient)


    def show_bg_image_def():
        global locations,  location_now, location_now_i
        global time_now_i, from_say_screen
        
        if locations.get(location_now):
            location_now_i = locations[location_now].bg
        time_now_i     = time.time_now
        
        Hide("icons_interface")()

        
        from_say_screen = False
        try:
            renpy.scene()
            renpy.show('location_now_image')

        except:
            renpy.scene()
            renpy.show('error_background')
        renpy.pause(.5, hard = True)
        Rollback()()
        

label show_bg_image_label:
    if locations.get(location_now):
        $ location_now_i = locations[location_now].bg
    $ time_now_i     = time.time_now
    hide screen icons_interface

    python:
        from_say_screen = False
        try:
            renpy.scene()
            renpy.show('location_now_image')

        except:
            renpy.scene()
            renpy.show('error_background')

    return
label main_interface_label:
    call check_gallery_label from _call_check_gallery_label_2
    hide expression '#000a'
    hide expression 'interface/Inventory.png'
    hide expression 'interface/Grid.png'
    hide screen pc_game_interface
    hide screen online_shop
    hide screen pc_interface
    $ stnd_music_play()
    if hasattr(store, 'name_boxes_displ'):
        $ store.name_boxes_displ.force_update = False
        $ store.name_boxes_displ.block_render = False
    
    $ store._from_talk_with_milf = False
    $ store.sex_name_box = False
    if hasattr(store, 'milf_position'):
        if 'evening' in milf_position:
            if milf_position['evening'] == 'Hall':
                $ milf_position['evening'] = ['Hall', 'milf_evening_hall']
            if milf_position['evening'] == ['Kitchen', 'milf_evening_hall']:
                $ milf_position['evening'] = ['Hall', 'milf_evening_hall']

        if hasattr(store, 'time') and hasattr(time, 'time_now') and time.time_now in milf_position:
            if milf_position[time.time_now][0] == 'Restroom' and milf_position[time.time_now][1] != 'milf_restroom':
                $ milf_position[time.time_now]  = ['Restroom',  'milf_restroom']

    if getattr(store, 'not_survival', False):
        $ gigiena     = 10000
        $ sitost      = 10000
        $ nastroi     = 10000
        if not hasattr(store, 'final_act_prison_start'):
            $ love_milf   = 10000
            $ love_sister = 10000

    # if getattr(get_item('Товар', True), 'quant', 0) and inventory_drugs > 30:
    #     $ inventory_drugs = 30
    #     $ add_ach('ACH_2')

    
    
    if hasattr(store, 'money') and money > 3000:
        $ money = 3000


    if getattr(store, 'money', 0) == 3000:
        $ add_ach('ACH_17')

    call show_all_images_label from _call_show_all_images_label_79
    window hide 

    python:
        relations_milf_tmp = relations_milf/50

        if relations_milf_tmp:
            if love_milf + relations_milf_tmp <= getattr(store, 'milf_love_quests', 0) + 1:
                
                love_milf += int(relations_milf_tmp)
                relations_milf -= int(50*relations_milf_tmp)
            else:
                relations_milf = 45
        if getattr(store, 'milf_love_quests', 0):
            if love_milf >= milf_love_quests:
                relations_milf_tmp = 45
                love_milf = copy.deepcopy(milf_love_quests)
                renpy.jump('milf_love_'+str(milf_love_quests))

        check_evnts = get_all_events_from_location()
        if len(check_evnts):
            if len(check_evnts) == 1: 
                check_ev = check_evnts[0]# check_events()
                Hide('main_interface')()
                renpy.jump(check_ev.label)
            else:
                
                persistent.first_show_choose_quest_screen_up = True
                persistent.event_for_preview = -1
                renpy.jump('choose_quest_show_label')



    if hasattr(store, 'love_milf') and love_milf > 7:
        $ relations_milf = 45
        $ love_milf = 7


    if hasattr(store, 'love_sister') and love_sister > 7:
        $ love_sister = 7

    if location_now == 'Sister_Room' and not getattr(store, 'unlock_sister_room', False):
        $ location_now = 'Corridor'
        call show_all_images_label from _call_show_all_images_label_95
        '[gg]' "Мне ещё рано туда заходить."
        jump main_interface_label

    if location_now == 'Restroom' and (
        (milf_position[time.time_now][0] == location_now and not block_milf_home) or (
        sister_position[time.time_now][0] == location_now and not block_sister_home)

        ):
        if not unlock_restroom:
            $ location_now = 'Corridor'
            call show_all_images_label from _call_show_all_images_label_91
            if not get_item('Отмычка', True):
                "[gg]" "Дверь заперта... Мне нужна отмычка чтобы её взломать."
                jump main_interface_label
            $ Hide('lock_pick_screen', transition = Dissolve(.5))()
            $ renpy.music.stop(fadeout=1.5)

            $ lockergame = LockerGame(lvl = 1, image_now = 'images/mini_games/lock_mini_game/locker.png')
            play music 'audio/mini_game.mp3' fadein 1.5
            call screen LockerGameScreen
            $ unlock_restroom = True

            $ Hide('main_interface')()

            play sound 'audio/lock.ogg'
            '[gg]' "Готово. Я взломал замок."
    if location_now == 'Milf_Room' and time.time_now == 'night':
        $ location_now = 'Hall'
        call show_all_images_label from _call_show_all_images_label_92
        if not getattr(store, 'ep2_milf_room_unlock', False):
            "[gg]" "Мне нечего там делать сейчас."
            jump main_interface_label
        if not unlock_milf_room:
            call show_all_images_label from _call_show_all_images_label_93
            if not get_item('Отмычка', True):
                "[gg]" "Дверь заперта... Мне нужна отмычка чтобы её взломать."
                jump main_interface_label
            $ Hide('lock_pick_screen', transition = Dissolve(.5))()
            $ renpy.music.stop(fadeout=1.5)

            $ lockergame = LockerGame(lvl = 1, image_now = 'images/mini_games/lock_mini_game/locker.png')
            play music 'audio/mini_game.mp3' fadein 1.5
            call screen LockerGameScreen
            $ unlock_milf_room = True

            $ Hide('main_interface')()

            play sound 'audio/lock.ogg'
            '[gg]' "Готово. Я взломал замок."
            $ solar_milf_room = False
        if not getattr(store, 'solar_milf_room', False):



            play sound 'audio/door_squeak.ogg'   
            $ renpy.pause(1, hard = True)
            '!' "Скриииииип!"

            show GG Embarrassment
            show GG Embarrassment:
                xalign .32
                ypos 1085
                zoom 1.0-0.035
            show Milf Night_Surprise
            show Milf Night_Surprise:
                xalign .85
                ypos 1085
                zoom 1.0-0.035
            with Dissolve(.5)

            'Марина' "[gg], что ты здесь делаешь в такой поздний час? "
            '[gg]' "Эм… Мне послышалось, будто ты не спишь. "
            show Milf Night_Angry
            'Марина' "Вообще-то я спала. Пока ты не разбудил меня."
            show GG Laughs
            '[gg]' "Ну, тогда спокойной ночи."

            show Milf Night_Embarrassment
            'Марина' "Спокойной…"



            $ location_now = 'Hall'

            jump main_interface_label
        elif True:
            $ location_now = 'Milf_Room'
            $ remove_from_inventory('Солнечное масло')
            call show_all_images_label from _call_show_all_images_label_94
    $ Hide('phone_contacts_screen_2')()
    if not mp.tutorial:
        call screen tutorial_screen
        
    show screen icons_interface
    with Dissolve(.2)

    call screen main_interface

    jump main_interface_label


label tmp_image_buttons_label:
    "" "[i]"
    show expression 'images/locations/imagebuttons/' + location_now + '/' + i + '.png'
    return


label show_characters_images_label:
    if not getattr(store, 'block_milf_home', False):
        if milf_position[time.time_now][0] == location_now and milf_position[time.time_now][0] == location_now and not (sister_position[time.time_now][0] == 'Kitchen' and milf_position[time.time_now][0] == 'Kitchen'):
            if milf_costume != 'n_body':
                show expression 'images/cg/milf_and_sister_activities/' + milf_position[time.time_now][1]  + "_" + milf_costume + '.png'

            else:
                show expression 'images/cg/milf_and_sister_activities/' + milf_position[time.time_now][1] + '.png'

    if not getattr(store, 'block_sister_home', False):
        if sister_position[time.time_now][0] == location_now:
            if christie_costume != 'n_body':
                show expression 'images/cg/milf_and_sister_activities/' + sister_position[time.time_now][1] +"_"+christie_costume + '.png'

            else:
                show expression 'images/cg/milf_and_sister_activities/' + sister_position[time.time_now][1] + '.png'

    if not getattr(store, 'block_igor_position', False):
        if igor_position[time.time_now][0] == location_now:
            show expression 'images/cg/igor_activities/' + igor_position[time.time_now][1] + '.png'

    return


label show_special_loc_images_label:
    if location_now in getattr(store, 'special_loc_images_dir', [-1,]):
        $ renpy.call(store.special_loc_images_dir[store.location_now])


label show_additional_images_label:
    if locations.get(location_now):
        $ show_additional_images_tmp = get_imagebuttons_from_location(location_now)

    

    elif True:
        $ show_additional_images_tmp = []
    if len(show_additional_images_tmp) >= 10:
        $ tmp_image_buttons_10_v = show_additional_images_tmp[9]
        $ renpy.show('tmp_image_buttons_10')
    if len(show_additional_images_tmp) >= 9:
        $ tmp_image_buttons_9_v  = show_additional_images_tmp[8]
        $ renpy.show('tmp_image_buttons_9')
    if len(show_additional_images_tmp) >= 8:
        $ tmp_image_buttons_8_v  = show_additional_images_tmp[7]
        $ renpy.show('tmp_image_buttons_8')
    if len(show_additional_images_tmp) >= 7:
        $ tmp_image_buttons_7_v  = show_additional_images_tmp[6]
        $ renpy.show('tmp_image_buttons_7')
    if len(show_additional_images_tmp) >= 6:
        $ tmp_image_buttons_6_v  = show_additional_images_tmp[5]
        $ renpy.show('tmp_image_buttons_6')
    if len(show_additional_images_tmp) >= 5:
        $ tmp_image_buttons_5_v  = show_additional_images_tmp[4]
        $ renpy.show('tmp_image_buttons_5')
    if len(show_additional_images_tmp) >= 4:
        $ tmp_image_buttons_4_v  = show_additional_images_tmp[3]
        $ renpy.show('tmp_image_buttons_4')
    if len(show_additional_images_tmp) >= 3:
        $ tmp_image_buttons_3_v  = show_additional_images_tmp[2]
        $ renpy.show('tmp_image_buttons_3')
    if len(show_additional_images_tmp) >= 2:
        $ tmp_image_buttons_2_v  = show_additional_images_tmp[1]
        $ renpy.show('tmp_image_buttons_2')
    if len(show_additional_images_tmp) >= 1:
        $ tmp_image_buttons_1_v  = show_additional_images_tmp[0]
        $ renpy.show('tmp_image_buttons_1')



    return

label show_all_images_label:
    call show_bg_image_label from _call_show_bg_image_label_57
    call show_additional_images_label from _call_show_additional_images_label_51
    call show_characters_images_label from _call_show_characters_images_label
    call show_special_loc_images_label from _call_show_special_loc_images_label
    return


label block_exit_home_label:
    "[gg]" "Прежде чем куда-то идти, я должен уладить все вопросы дома."

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
