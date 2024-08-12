label _prison_gym_del_label:
    python:
        try:
            del _power_img
        except:
            pass
        
        try:
            del _sitost_img
        except:
            pass
    hide screen prison_survival_screen
    with my_dissolve
    return
label prison_gym_label:
    if time.time_now == 'night':
        show GG Invis
        show GG Invis:
            xalign .95
        "[gg]" "Нет, я не могу заниматья спортом ночью. "
        jump main_interface_label
    show screen prison_survival_screen
    with my_dissolve
    $ _power_img  = 'interface/prison_survival_power.png'
    $ _sitost_img = 'interface/prison_survival_sitost.png'
    $ Hide('info_panel')()

    menu:
        "Отжиматься (-20 {image=[_sitost_img]}, +10 {image=[_power_img]})":
            if final_act_sitost < 20:
                show GG Invis
                show GG Invis:
                    xalign .95
                "[gg]" "У меня нет сил на это..."
                call _prison_gym_del_label from _call__prison_gym_del_label
                jump main_interface_label

            #hide final_act_push_up 1
            #$ show_text_animation('+100 sitost')
            
            $ final_act_sitost -= 20
            $ Show('info_panel', ttext = "-20", iimage = "info_panel_prison_sitost")()
        
            #play audio "audio/eat.ogg"
            show final_act_gg_activities push_up_anim_1
            with my_dissolve
            $ renpy.pause(.5, hard = True)
            call wait_click_label from _call_wait_click_label_18
            $ final_act_power   = min(final_act_power+10, 100)
            $ Hide('info_panel')()
            $ Show('info_panel', ttext = "+10", iimage = "info_panel_prison_power")()
           # $ show_text_animation('+10 prison_power')
        

            $ time.time_forward(jump_to_main_interface = False)
            scene black
            with my_dissolve
            $ renpy.pause(.5, hard = True)
        "Назад":
            pass
    call _prison_gym_del_label from _call__prison_gym_del_label_1
    jump main_interface_label