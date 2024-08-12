label sister_at_restroom:
    menu:
        "Наблюдать":
            $ pass
        "Назад":
            jump main_interface_label
    menu:
        "Уровень 1":
            $ pass
        "Уровень 2" if hasattr(store, 'tyan_falos_text'):
            #pass
            jump christie_at_bath_lvl_2
        "Уровень 3" if hasattr(store, 'tyan_falos_text'):
            #pass
            jump christie_at_bath_lvl_3


        "!Уровень 2" if not hasattr(store, 'tyan_falos_text'):
            pass
            
        "!Уровень 3" if not hasattr(store, 'tyan_falos_text'):
            pass
            
        "Назад":
            jump sister_at_restroom

    show expression 'cg/milf_and_sister_activities/sister_restroom_full.png'
    with Dissolve(.5)
    $ renpy.pause(99999)
    if preferences.language in (None, 'eng', 'rus'):
        "[gg]" "Вау. Она выглядит такой беззаботной... и желанной."
    jump main_interface_label

label talk_with_sister_before:
    $ _every_day_events = getattr(store, 'christie_every_day_events', [])
    $ location_now_tmp = copy.deepcopy(location_now)
    $ location_now     = 'Christie'
    $ check_ev         = get_all_events_from_location(ignore=_every_day_events)
    $ check_ev_buttons = get_check_ev_buttons(check_ev)
    $ location_now     = copy.deepcopy(location_now_tmp)
    $ _len_check_ev = len(check_ev)
    return

label talk_with_sister_label:
    if location_now == 'Restroom':
        jump sister_at_restroom
    $ Hide('main_interface')()
    
    if getattr(store, 'block_sister_events', None):
        $ renpy.jump(block_sister_events)

    $ _back_to = "talk_with_sister_label"
    $ _back_to_tmp = copy.deepcopy(_back_to)
    

    call talk_with_sister_before from _call_talk_with_sister_before

    $ create_talk_with_translates()

    
    menu talk_with_sister_menu:

        "Говорить." if time.time_now != 'night':
            call talk_with_sister_before from _call_talk_with_sister_before_1
            $ _back_to_tmp = "talk_with_sister_menu"
            if not _len_check_ev:
            
                menu talk_with_sister_menu_2:
                    #$ _back_to = copy.deepcopy(_back_to_tmp)

                    "{b}Повторяющиеся квесты{/b}":
                        $ _back_to = "talk_with_sister_menu_2"

                        jump christie_every_day_events_label
                    
                    
                    "Назад":

                        #$ renpy.jump(_back_to)
                        call talk_with_sister_before from _call_talk_with_sister_before_2
                        jump talk_with_sister_menu

            elif _len_check_ev == 1:
                if len(_every_day_events):
                    
                    menu talk_with_sister_menu_3:


                        "{b}Повторяющиеся квесты{/b}":
                            $ _back_to = "talk_with_sister_menu_3"
                            jump christie_every_day_events_label
                        

                        
                        "[tmp_names_tmp_0]" if len(check_ev):
                            $ _back_to = "talk_with_sister_menu_3"

                           
                            $ Jump(check_ev[0].label)()
                        "Назад":
                            #$ renpy.jump(_back_to)
                            call talk_with_sister_before from _call_talk_with_sister_before_3
                            jump talk_with_sister_menu

                else:
                    #"" "!"
                    $ Jump(check_ev[0].label)()

            else:
                
                menu talk_with_sister_menu_4:
                    
                    "{b}Повторяющиеся квесты{/b}" if len(_every_day_events):

                        $ _back_to = "talk_with_sister_menu_4"
                        jump christie_every_day_events_label
                    

                    "[tmp_names_tmp_0]" if len(check_ev_buttons) >= 1:
                        $ renpy.jump(check_ev[0].label)
                    "[tmp_names_tmp_1]" if len(check_ev_buttons) >= 2:
                        $ renpy.jump(check_ev[1].label)
                    "[tmp_names_tmp_2]" if len(check_ev_buttons) >= 3:
                        $ renpy.jump(check_ev[2].label)
                    "[tmp_names_tmp_3]" if len(check_ev_buttons) >= 4:
                        $ renpy.jump(check_ev[3].label)
                    "[tmp_names_tmp_4]" if len(check_ev_buttons) >= 5:
                        $ renpy.jump(check_ev[4].label)
                    "[tmp_names_tmp_5]" if len(check_ev_buttons) >= 6:
                        $ renpy.jump(check_ev[5].label)
                    "[tmp_names_tmp_6]" if len(check_ev_buttons) >= 7:
                        $ renpy.jump(check_ev[6].label)
                    "[tmp_names_tmp_7]" if len(check_ev_buttons) >= 8:
                        $ renpy.jump(check_ev[7].label)
                    "[tmp_names_tmp_8]" if len(check_ev_buttons) >= 9:
                        $ renpy.jump(check_ev[8].label)
                    "[tmp_names_tmp_9]" if len(check_ev_buttons) >= 10:
                        $ renpy.jump(check_ev[9].label)
                    "Назад":
                        #$ renpy.jump(_back_to)
                        call talk_with_sister_before from _call_talk_with_sister_before_4
                        jump talk_with_sister_menu


        "Просто поздороваться." if not (time.time_now == 'night' and location_now == 'Sister_Room') and preferences.language in (None, 'eng', 'rus'):
            $ _back_to_tmp = "talk_with_sister_menu"
            $ _back_to = "talk_with_sister_menu"
            
            pass

        "{alpha=*0.5}Сменить костюм{/alpha} {image=star.png}" if location_now != 'Restroom' and time.time_now != 'night' and (not getattr(store, 'unlock_milf_costumes', False) or not getattr(store, 'jun_2024_dlc', False)):

            call _not_to_fast_label from _call__not_to_fast_label_5 
            jump main_interface_label
        "Сменить костюм {image=star.png}" if location_now != 'Restroom' and time.time_now != 'night' and (getattr(store, 'unlock_milf_costumes', False) and getattr(store, 'jun_2024_dlc', False)):
            call christie_costume_0 from _call_christie_costume_0
            jump main_interface_label

        "Уйти." if True:



            jump main_interface_label


    call show_bg_image_label from _call_show_bg_image_label_1
    call show_additional_images_label from _call_show_additional_images_label_1

    show Christie Normal
    show Christie Normal:
        xalign .85
        ypos 1085
    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left

    '[gg]' "Привет, Кристи."
    show Christie Smile
    'Кристи' "Привет, чудик."
    show GG Passion
    '[gg]' "Не хочешь прогуляться?"
    show Christie Angry

    if location_now == "Hall":
        'Кристи' "Извини, но я читаю."
        show GG Think
        '[gg]' "А когда дочитаешь?"
        show Christie Laughs
        'Кристи' "Когда буквы закончатся. Хи-хи-хи."
    elif True:
        'Кристи' "Извини, но я занята."
    show GG Chagrin
    '[gg]' "Ясно..."
    show Christie Passion
    'Кристи' "Не скучай."
    call show_all_images_label from _call_show_all_images_label_111
    with my_dissolve
    $ renpy.jump(_back_to)
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label christie_every_day_events_label:


    $ location_now_tmp = copy.deepcopy(location_now)
    $ location_now     = 'Christie'

    $ check_ev         = get_all_events_from_location(allowed=_every_day_events)
    $ check_ev_buttons = get_check_ev_buttons(check_ev)
    
    $ location_now     = copy.deepcopy(location_now_tmp)





    python:

        if len(check_ev_buttons) >= 1:
            tmp_names_tmp_0 = check_ev_buttons[0]
            if preferences.language == 'eng':
               if tmp_names_tmp_0 in add_translate:
                   tmp_names_tmp_0 = add_translate[tmp_names_tmp_0]
        if len(check_ev_buttons) >= 2:
            tmp_names_tmp_1 = check_ev_buttons[1]
            if preferences.language == 'eng':
                if tmp_names_tmp_1 in add_translate:
                    tmp_names_tmp_1 = add_translate[tmp_names_tmp_1]
        if len(check_ev_buttons) >= 3:
            tmp_names_tmp_2 = check_ev_buttons[2]
            if preferences.language == 'eng':
                if tmp_names_tmp_2 in add_translate:
                    tmp_names_tmp_2 = add_translate[tmp_names_tmp_2]
        if len(check_ev_buttons) >= 4:
            tmp_names_tmp_3 = check_ev_buttons[3]
            if preferences.language == 'eng':
                if tmp_names_tmp_3 in add_translate:
                    tmp_names_tmp_3 = add_translate[tmp_names_tmp_3]
        if len(check_ev_buttons) >= 5:
            tmp_names_tmp_4 = check_ev_buttons[4]
            if preferences.language == 'eng':
                if tmp_names_tmp_4 in add_translate:
                    tmp_names_tmp_4 = add_translate[tmp_names_tmp_4]
        if len(check_ev_buttons) >= 6:
            tmp_names_tmp_5 = check_ev_buttons[5]
            if preferences.language == 'eng':
                if tmp_names_tmp_5 in add_translate:
                    tmp_names_tmp_5 = add_translate[tmp_names_tmp_5]
        if len(check_ev_buttons) >= 7:
            tmp_names_tmp_6 = check_ev_buttons[6] 
            if preferences.language == 'eng':
                if tmp_names_tmp_6 in add_translate:
                    tmp_names_tmp_6 = add_translate[tmp_names_tmp_6]
        if len(check_ev_buttons) >= 8:
            tmp_names_tmp_7 = check_ev_buttons[7] 
            if preferences.language == 'eng':
                if tmp_names_tmp_7 in add_translate:
                    tmp_names_tmp_7 = add_translate[tmp_names_tmp_7]
        if len(check_ev_buttons) >= 9:
            tmp_names_tmp_8 = check_ev_buttons[8] 
            if preferences.language == 'eng':
                if tmp_names_tmp_8 in add_translate:
                    tmp_names_tmp_8 = add_translate[tmp_names_tmp_8]
        if len(check_ev_buttons) >= 10:
            tmp_names_tmp_9 = check_ev_buttons[9] 
            if preferences.language == 'eng':
                if tmp_names_tmp_9 in add_translate:
                    tmp_names_tmp_9 = add_translate[tmp_names_tmp_9]

        _len_check_ev = len(check_ev)

    menu:
        "[tmp_names_tmp_0]" if len(check_ev_buttons) >= 1:
            if check_ev[0].name in christie_every_day_events_block:
                call already_did_it_today from _call_already_did_it_today_3
                jump christie_every_day_events_label

            $ christie_every_day_events_block.append(check_ev[0].name) 
            $ renpy.jump(check_ev[0].label)
        "[tmp_names_tmp_1]" if len(check_ev_buttons) >= 2:
            if check_ev[1].name in christie_every_day_events_block:
                call already_did_it_today from _call_already_did_it_today_4
                jump christie_every_day_events_label
            $ christie_every_day_events_block.append(check_ev[1].name) 
            $ renpy.jump(check_ev[1].label)
        "[tmp_names_tmp_2]" if len(check_ev_buttons) >= 3:
            if check_ev[2].name in christie_every_day_events_block:
                call already_did_it_today from _call_already_did_it_today_5
                jump christie_every_day_events_label
            $ christie_every_day_events_block.append(check_ev[2].name) 
            $ renpy.jump(check_ev[2].label)
        "[tmp_names_tmp_3]" if len(check_ev_buttons) >= 4:
            if check_ev[3].name in christie_every_day_events_block:
                call already_did_it_today from _call_already_did_it_today_6
                jump christie_every_day_events_label
            $ christie_every_day_events_block.append(check_ev[3].name) 
            $ renpy.jump(check_ev[3].label)
        "[tmp_names_tmp_4]" if len(check_ev_buttons) >= 5:
            if check_ev[4].name in christie_every_day_events_block:
                call already_did_it_today from _call_already_did_it_today_7
                jump christie_every_day_events_label
            $ christie_every_day_events_block.append(check_ev[4].name) 
            $ renpy.jump(check_ev[4].label)
        "[tmp_names_tmp_5]" if len(check_ev_buttons) >= 6:
            if check_ev[5].name in christie_every_day_events_block:
                call already_did_it_today from _call_already_did_it_today_8
                jump christie_every_day_events_label
            $ christie_every_day_events_block.append(check_ev[5].name) 
            $ renpy.jump(check_ev[5].label)
        "[tmp_names_tmp_6]" if len(check_ev_buttons) >= 7:
            if check_ev[6].name in christie_every_day_events_block:
                call already_did_it_today from _call_already_did_it_today_9
                jump christie_every_day_events_label
            $ christie_every_day_events_block.append(check_ev[6].name) 
            $ renpy.jump(check_ev[6].label)
        "[tmp_names_tmp_7]" if len(check_ev_buttons) >= 8:
            if check_ev[7].name in christie_every_day_events_block:
                call already_did_it_today from _call_already_did_it_today_10
                jump christie_every_day_events_label
            $ christie_every_day_events_block.append(check_ev[7].name) 
            $ renpy.jump(check_ev[7].label)
        "[tmp_names_tmp_8]" if len(check_ev_buttons) >= 9:
            if check_ev[8].name in christie_every_day_events_block:
                call already_did_it_today from _call_already_did_it_today_11
                jump christie_every_day_events_label
            $ christie_every_day_events_block.append(check_ev[8].name) 
            $ renpy.jump(check_ev[8].label)
        "[tmp_names_tmp_9]" if len(check_ev_buttons) >= 10:
            if check_ev[9].name in christie_every_day_events_block:
                call already_did_it_today from _call_already_did_it_today_12
                jump christie_every_day_events_label
            $ christie_every_day_events_block.append(check_ev[9].name) 
            $ renpy.jump(check_ev[9].label)
        "Назад":
            #jump talk_with_sister_label
            #$ _back_to = copy.deepcopy(_back_to_tmp)
            $ renpy.jump(_back_to)
            #jump talk_with_sister_menu

    jump main_interface_label


label christie_costume_0:
    menu:
        "DLC" if getattr(store, 'jun_2024_dlc', False) and getattr(store, 'christie_costume', 'n_body') != 'maid':
            $ christie_costume = 'maid'
            
        "Оригинальный наряд" if getattr(store, 'christie_costume', 'n_body') != 'n_body':
            $ christie_costume = 'n_body'
        "Назад":
             jump main_interface_label
            
    return
