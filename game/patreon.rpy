image activate_quest_info_0 = Text(__('Это функция принудительного запуска сцены по текущему квесту.'), color = '#ae845e', font = 'fonts/FUTURA-N.ttf', size = 31)
image activate_quest_info_1 = Text(__('Использовать только в {b}крайних{/b} случаях, например, когда задание не проходимо из-за бага.'), color = '#ae845e', font = 'fonts/FUTURA-N.ttf', size = 31)
image activate_quest_info_2 = Text("")





init -500 python:
    
    unlock_milf_costume = True
    
    for i in images_exts_list:

        build.classify('game/images/characters/Milf/EMO/**.'+i,  'images')
        build.classify('game/images/characters/Milf/atlas/**.'+i,  'images')
    
        for j in ('bdsm', 'cow', 'gantz', 'Blin','n_body','Night_Pose_1','Night_Pose_2','Night_Pose_3'):
            build.classify('game/images/characters/Milf/1POSES/' + j + "." + i, "images")
    

    patreon_descript_ypos = 50



    def unlock_gallery():
        mp.gallery_save = copy.deepcopy(mp.gallery)
        mp.save()
        

        for i in store.gallery_images_list:
            add_to_gallery(i)

    def gallery_return():
        if mp.gallery_save != None:
            mp.gallery = copy.deepcopy(mp.gallery_save)
            
        mp.gallery_save = None
        mp.save()

    def test_check_evnt_label(event_label, labels_list):
        if not event_label:
            return False
        for i in labels_list:
            if i.lower() in event_label.lower():
                return True
        return False
    def test_get_events_list(for_who='Milf', main = False):
        global events, milf_costume
        need_return = []
        try:
            for i in events:
                evnt = events[i]
                if 'night_girl' in evnt.label.lower():
                    continue
                
                
                if for_who == 'Milf':
                    if test_check_evnt_label(evnt.label,
                        ('milf_root_', 'ep1_', 'ep2_', 'ep3_', 'ep4_', 'ep45_', 'ep5_')):
                        
                        milf_costume = 'n_body'
                        need_return.append(i)
                elif for_who == 'Christie':
                    if main:
                        if 'christie_root_' in evnt.label:
                            need_return.append(i)
                    
                    else:
                        if 'tyan_falos_' in evnt.label:
                            need_return.append(i)
                    
                elif for_who == 'Misha':
                    if 'misha_root_' in evnt.label:  
                        
                        need_return.append(i)
                
                elif for_who == 'Cat':
                    if 'cat_root_' in evnt.label: 
                        need_return.append(i)
        
        
        except:
            pass
        return need_return


    def test_event_check_jump(_list):
        if len(_list) == 1:

            test_event_jump(_list[0])
        else:
            Show('descript_screen_activate_quest', events_list_to_show = _list)()




    def test_event_jump(event_name):
        
        global time, location_now, event
        if event_name not in events: 
            return
        event = events[event_name]
        if event.time and len(event.time):
            if type(event.time) == str: 
                time.time_now = copy.deepcopy(event.time)
            else:
                time.time_now = copy.deepcopy(event.time[0])
        if event.day_start:
            if time.day_now < event.day_start:
                time.day_now = copy.deepcopy(event.day_start)
        Hide('icons_interface')()
        Hide('descript_screen')()
        
        Hide('descript_screen_3')()
        Hide('descript_screen_2')()
        Hide('descript_screen_activate_quest')()
        if event.location:
            lower_location = event.location.lower()
            if  'hall' in lower_location:
                location_now = 'Hall'
            elif 'kitchen' in lower_location:
                location_now = 'Kitchen'
            elif 'corridor' in lower_location:
                location_now = 'Corridor'
            elif 'gg_room' in  lower_location:
                location_now = "GG_Room"
            else:
                
                location_now = copy.deepcopy(event.location)
            
            
            
            
            
            
            
            if 'christie' in lower_location:
                location_now = 'Hall'
                Jump('talk_with_sister_label')()
                return
            
            elif 'milf' in lower_location:
                location_now = 'Hall'
                Jump('talk_with_milf_label')()
                return
            
            elif 'jaybob' in lower_location:
                location_now = "City_Shop"
                Jump('talk_with_jay_bob_label_with_images')()
                return
            elif 'cat' in lower_location:
                location_now = "GG_Room"
                Jump('talk_with_kat_label')()
                return
            
            elif 'igor' in lower_location:
                location_now = 'City_Park'
                Jump('talk_with_igor_label_with_images')()
                return
            elif 'store_misha' in lower_location or 'after_storein' in lower_location:
                location_now = 'StoreIn'
                Jump('talk_with_igor_label_with_images')()
                return
            
            elif 'bibliogirl' in lower_location:
                
                JumpToLocation('City_Library')
                return
        
        
        Jump(event.label)()
        
        pass


screen descript_screen_activate_quest(events_list_to_show=[]):
    zorder 890
    imagebutton:
        idle '#000a'
        hover '#000a'
        action Hide('descript_screen_activate_quest')
    add 'interface/Quest_Text.png' xalign .5 yalign .5
    vbox:
        xalign .5
        yalign .5
        spacing 5

        if not len(events_list_to_show):
            add Text(__('Извините, но данная функция не доступна для этого квеста.'), color = '#ae845e', font = 'fonts/FUTURA-N.ttf', bold = True, size = 40)

        else:
            for i in events_list_to_show:
                viewport:
                    xmaximum 750
                    ymaximum 50
                    add '#0000'
                    imagebutton:
                        xalign .5
                        yalign .5
                        idle Text(__('Перейти к ') + str(i), color = '#ae845e', font = 'fonts/FUTURA-N.ttf', size = 45, alpha = .55)

                        hover Text(__('Перейти к ') + str(i), color = '#ae845e', font = 'fonts/FUTURA-N.ttf', size = 50)

                        action Function(test_event_jump, i)







###############################
#phone



init python:
    def plus_nastroi(plus):
        global nastroi
        if plus > 0:
            show_text_animation('+'+str(plus) + ' nastroi')
            nastroi  = min(100, nastroi+plus)
        else:
            show_text_animation('-'+str(plus) + ' nastroi')
            nastroi  = max(100, nastroi+plus)

    def plus_gigiena(plus):
        global gigiena
        if plus > 0:
            show_text_animation('+'+str(plus) + ' gigiena')
            gigiena  = min(100, gigiena+plus)
        else:
            show_text_animation('-'+str(plus) + ' gigiena')
            gigiena  = max(0, gigiena+plus)

    def plus_sitost(plus):
        global sitost
        if plus > 0:
            show_text_animation('+'+str(plus) + ' sitost')
            sitost  = min(100, sitost+plus)
        else:
            show_text_animation('-'+str(plus) + ' sitost')
            sitost  = max(0, sitost+plus)

    def plus_money(plus):
        global money
        if plus > 0:
            show_text_animation('+'+str(plus) + ' money')
            money += plus
        else:
            show_text_animation('-'+str(plus) + ' money')
            money  = max(0, money+plus)


screen Phone_Cheats_Screen:
    zorder 20
    imagebutton:
        idle '#000a'
        hover '#000a'
        action Hide('Phone_Cheats_Screen')
    imagebutton:
        idle 'phone_cheat_screen'
        hover 'phone_cheat_screen'
        action NullAction()
        focus_mask True
    viewport:
        xmaximum 70
        ymaximum 70
        xpos 965
        ypos 938

        imagebutton:
            idle '#0000'
            hover '#fff0'
            action Hide('Phone_Cheats_Screen')
    viewport:
        xmaximum 40
        ymaximum 30
        xpos 895
        ypos 420

        imagebutton:
            idle '#0000'
            hover '#fff0'
            action Function(plus_nastroi, 10)

    viewport:
        xmaximum 40
        ymaximum 30
        xpos 895
        ypos 470

        imagebutton:
            idle '#0000'
            hover '#fff0'
            action Function(plus_sitost, 10)

    viewport:
        xmaximum 40
        ymaximum 30
        xpos 895
        ypos 520

        imagebutton:
            idle '#0000'
            hover '#fff0'
            action Function(plus_gigiena, 10)

    viewport:
        xmaximum 45
        ymaximum 35
        xpos 895
        ypos 590

        imagebutton:
            idle '#0000'
            hover '#fff0'
            action Function(plus_money, 10)



    viewport:
        xmaximum 40
        ymaximum 30
        xpos 895+160
        ypos 420

        imagebutton:
            idle '#0000'
            hover '#fff0'
            action Function(plus_nastroi, -10)

    viewport:
        xmaximum 40
        ymaximum 30
        xpos 895+160
        ypos 470

        imagebutton:
            idle '#0000'
            hover '#fff0'
            action Function(plus_sitost, -10)

    viewport:
        xmaximum 40
        ymaximum 30
        xpos 895+160
        ypos 520

        imagebutton:
            idle '#0000'
            hover '#fff0'
            action Function(plus_gigiena, -10)

    viewport:
        xmaximum 45
        ymaximum 35
        xpos 895+160
        ypos 590

        imagebutton:
            idle '#0000'
            hover '#fff0'
            action Function(plus_money, -10)


image phone_cheats = 'interface/phone_interface/phone_cheats.png'

screen phone_cheats_patreon:
    pass
    imagebutton:
        idle 'phone_cheats'
        hover 'phone_cheats'
        action Function(renpy.play, 'audio/mobile.ogg'), Show('Phone_Cheats_Screen')
        xpos 1100
        ypos 240
        at ButtonEffect07


#phone
###############################





###############################
#costume

init -500 python:
    milf_additional_costumes = ["bdsm", 'cow', 'gantz']

label milf_standart_talk_gantz:
label milf_standart_talk_cow:
label milf_standart_talk_bdsm:

    call show_bg_image_label from _call_show_bg_image_label_172

    call show_additional_images_label from _call_show_additional_images_label_103

    show Milf Normal
    show Milf Normal:
        xalign .75
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    show GG Normal

    show GG Normal at go_from_left
    if location_now == "Corridor":

        show GG Passion
        "[gg]" "Всякий раз, когда я прохожу мимо, мне хочется трахнуть тебя."

        show Milf Smile
        "Марина" "Хи-хи-хи."
        show Milf Passion
        "Марина" "Я готова утолить твою жажду в любое время, милый."
        show GG Passion
        "[gg]" "Да?"
        "[gg]" "Что ж, я подумаю на твоим предложением. "

        "Марина" "Продолжишь издеваться и не успеешь оглянуться, как я сама тебя трахну."
        show GG Embarrassment
        "[gg]" "Это самые приятные угрозы, какие я слышал в своей жизни. "

        "Марина" "Рррррррр."
    elif location_now == "Kitchen":

        show GG Passion
        show Milf Chagrin
        with my_dissolve
        "[gg]" "Что готовишь?"

        show Milf Passion
        "Марина" "Хи-хи-хи. В таком виде я лучше любого блюда."
        "[gg]" "Чёрт…"
        "[gg]" "Теперь я вдвойне проголодался."
        "Марина" "Угощайся, милый. Я вся твоя. "
    elif time.time_now == "evening":

        show GG Smile
        "[gg]" "Скучаешь?"
        show Milf Chagrin
        "Марина" "Всегда."
        show Milf Passion
        "Марина" "Но ты в любой момент можешь развеять мою тоску, просто сняв штаны. "
        show GG Laughs
        "[gg]" "Ха-ха-ха!"
        show Milf Normal
        "Марина" "Я серьёзно."
        show GG Surprise
        "[gg]" "Оу…."
        show Milf Passion
        "Марина" "Надеюсь, ты найдёшь время, чтобы присоединиться ко мне. "

        show GG Smile
        "[gg]" "Я постараюсь, честно."
    elif True:
        show GG Smile
        "[gg]" "У тебя игривое настроение."
        show Milf Passion
        "Марина" "Хочу разделить его с тобой, любименький. "
        show GG Passion
        "[gg]" "А как же Кристи и Кэт?"
        show Milf Passion
        "Марина" "Нет, ты только мой!"
        show GG Embarrassment
        "[gg]" "Вообще-то, я имел в виду их реакцию…"
        show Milf Smile
        "Марина" "Я думаю, они обзавидуются, хи-хи-хи!"

    jump main_interface_label


label milf_costume_0:

    call show_bg_image_label from _call_show_bg_image_label_166

    call show_additional_images_label from _call_show_additional_images_label_102

    with Dissolve(.5)
    show GG Smile



    show GG Smile:
        xalign .1
        ypos 1085
        zoom 1.0-0.035
    show Milf Normal
    if time.time_now == 'evening':
        show Milf Night_Normal:
            xalign .75
            ypos 1085
            zoom 1.0-0.035
    elif location_now == 'Hall':
        show Milf Losi_Embarrassment:
            xalign .75
            ypos 1085
            zoom 1.0-0.035
    elif True:

        show Milf Normal:
            xalign .75
            ypos 1085
            zoom 1.0-0.035

    with Dissolve(.5)
    if preferences.language in (None, 'rus'):
        "[gg]" "Могу я попросить тебя примерить это?"
        if time.time_now == 'evening':
            show Milf Night_Passion
        elif location_now == 'Hall':
            pass
        elif True:
            show Milf Passion
        "Марина" "Ты тот, кто может просить меня о чём угодно."

        if time.time_now == 'evening':
            show Milf Night_Smile
        elif location_now == 'Hall':
            pass
        elif True:
            show Milf Smile
        "Марина" "Показывай мне свой наряд, милый."

    menu:
        "Gantz" if getattr(store, 'milf_costume', 'n_body') != 'gantz':
            $ renpy.music.stop(fadeout=.5)
            $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


            show Milf:
                xzoom -1
                easein 1.5 xalign 2.0
            $ renpy.pause(1.2, hard = True)
            $ milf_costume = 'gantz'
            $ milf_night_costume_1 = "gantz"
            $ milf_night_costume_2 = "gantz"
            $ milf_night_costume_3 = "gantz"
            show Milf Embarrassment:
                xzoom 1
                easein 1 xalign .75
            $ renpy.pause(1.5, hard = True)
        "Коровка" if getattr(store, 'milf_costume', 'n_body') != 'cow':
            $ renpy.music.stop(fadeout=.5)
            $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


            show Milf:
                xzoom -1
                easein 1.5 xalign 2.0
            $ renpy.pause(1.2, hard = True)
            $ milf_costume = 'cow'
            $ milf_night_costume_1 = "cow"
            $ milf_night_costume_2 = "cow"
            $ milf_night_costume_3 = "cow"
            show Milf Embarrassment:
                xzoom 1
                easein 1 xalign .75
            $ renpy.pause(1.5, hard = True)
            # "Марина" "Кажется… я выгляжу слишком вызывающе. "
            # show GG Passion:
            # show Milf Embarrassment:
            #     xzoom 1
            #     xalign .75
            # "[gg]" "Но тебе ведь нравится?"

            # "Марина" "Да. Но что скажет Кристи или эта… как её там, Кэт?"

            # "[gg]" "Тебя не должно волновать их мнение."

            # "[gg]" "Это твой дом, и ты здесь хозяйка."

            # "Марина" "Хм… Наверное, ты прав."
            # show Milf Passion
            # "Марина" "В этом наряде я такая развратная, правда?"

            # "Марина" "Это то, чего я и добивался. "

            # "Марина" "Хи-хи-хи."
            # "" "{i}ВЫ НЕ СМОЖЕТЕ ВЫПОЛНЯТЬ СТАНДАРТНЫЕ КВЕСТЫ ПОКА ИСПОЛЬЗУЕТСЯ ЭТОТ КОСТЮМ!{/i}"
        "DLC 1" if getattr(store, 'jun_2024_dlc', False) and getattr(store, 'milf_costume', 'n_body') != 'med':
            $ milf_costume = 'med'
            $ milf_night_costume_1 = "med"
            $ milf_night_costume_2 = "med"
            $ milf_night_costume_3 = "med"

        "DLC 2" if getattr(store, 'jun_2024_dlc', False) and getattr(store, 'milf_costume', 'n_body') != 'tayt':
            $ milf_costume = 'tayt'
            $ milf_night_costume_1 = "tayt"
            $ milf_night_costume_2 = "tayt"
            $ milf_night_costume_3 = "tayt"

        "Бондаж" if getattr(store, 'milf_costume', 'n_body') != 'bdsm':
            $ renpy.music.stop(fadeout=.5)
            $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


            show Milf:
                xzoom -1
                easein 1.5 xalign 2.0
            $ renpy.pause(1.2, hard = True)
            $ milf_costume = 'bdsm'
            $ milf_night_costume_1 = "bdsm"
            $ milf_night_costume_2 = "bdsm"
            $ milf_night_costume_3 = "bdsm"
            show Milf Embarrassment:
                xzoom 1
                easein 1 xalign .75
            if preferences.language in (None, 'rus'):
                "Марина" "Кажется… я выгляжу слишком вызывающе. "
                show GG Passion:
                show Milf Embarrassment:
                    xzoom 1
                    xalign .75
                "[gg]" "Но тебе ведь нравится?"

                "Марина" "Да. Но что скажет Кристи или эта… как её там, Кэт?"

                "[gg]" "Тебя не должно волновать их мнение."

                "[gg]" "Это твой дом, и ты здесь хозяйка."

                "Марина" "Хм… Наверное, ты прав."
                show Milf Passion
                "Марина" "В этом наряде я такая развратная, правда?"

                "Марина" "Это то, чего я и добивался. "

                "Марина" "Хи-хи-хи."
                "" "{i}ВЫ НЕ СМОЖЕТЕ ВЫПОЛНЯТЬ СТАНДАРТНЫЕ КВЕСТЫ ПОКА ИСПОЛЬЗУЕТСЯ ЭТОТ КОСТЮМ!{/i}"

        "Оригинальный наряд" if getattr(store, 'milf_costume', 'n_body') != 'n_body':
            if preferences.language in ('rus', None):
                "[gg]" "Я хочу, чтобы ты снова носила старую одежду."
                "Марина" "Хорошо."
            $ milf_costume = 'n_body'
            $ milf_night_costume_1 = "Night_Pose_1"
            $ milf_night_costume_2 = "Night_Pose_2"
            $ milf_night_costume_3 = "Night_Pose_3"
        "Назад" if True:
            jump main_interface_label

    return





translate eng milf_costume_0_b39aa018:

    # "[gg]" "Могу я попросить тебя примерить это?"
    "[gg]" "Can I ask you to try this on?"


translate eng milf_costume_0_186f9ce2:

    # "Mary" "Ты тот, кто может просить меня о чём угодно."
    "Mary" "You can ask anything you want."


translate eng milf_costume_0_d8ed7cbb:

    # "Mary" "Показывай мне свой наряд, милый."
    "Mary" "Show me your outfit, honey."


translate eng milf_costume_0_a491cf73:

    # "Mary" "Кажется… я выгляжу слишком вызывающе. "
    "Mary" " I think... I look too…revealing."


translate eng milf_costume_0_a12d8f07:

    # "[gg]" "Но тебе ведь нравится?"
    "[gg]" "But you like it, don't you?"


translate eng milf_costume_0_a66cb28b:

    # "Mary" "Да. Но что скажет Кристи или эта… как её там, Кэт?"
    "Mary" "Yes. But what will Christy say, or the other one... I think her name was Kat."


translate eng milf_costume_0_07143ff0:

    # "[gg]" "Тебя не должно волновать их мнение."
    "[gg]" "You shouldn't care what they say."


translate eng milf_costume_0_e1c11dae:

    # "[gg]" "Это твой дом, и ты здесь хозяйка."
    "[gg]" "This is your home and you are the mistress here."


translate eng milf_costume_0_2b34b544:

    # "Mary" "Хм… Наверное, ты прав."
    "Mary" "Hmm... you're probably right."


translate eng milf_costume_0_2bd0cff2:

    # "Mary" "В этом наряде я такая развратная, правда?"
    "Mary" "I'm so slutty in this bondage costume, don’t you think?"


translate eng milf_costume_0_e9708081:

    # "Mary" "Это то, чего я и добивался. "
    "Mary" "This is just what I wanted."


translate eng milf_costume_0_079aaa6a:

    # "Mary" "Хи-хи-хи."
    "Mary" "He-he-he"


translate eng milf_costume_0_6f7374db:

    # "" "{i}ВЫ НЕ СМОЖЕТЕ ВЫПОЛНЯТЬ СТАНДАРТНЫЕ КВЕСТЫ ПОКА ИСПОЛЬЗУЕТСЯ ЭТОТ КОСТЮМ!{/i}"
    "" "YOU WILL NOT BE ABLE TO PERFORM STANDARD QUESTS WHILE THIS COSTUME IS IN USE!"


translate eng milf_costume_0_4ba8d2e7:

    # "[gg]" "Я хочу, чтобы ты снова носила старую одежду."
    "[gg]" "I want you to wear your old clothes again."


translate eng milf_costume_0_c0f59bf4:

    # "Mary" "Хорошо."
    "Mary" "Okay"





















# game/core/talk_with/talk_with_milf.rpy:119
translate eng milf_standart_talk_bdsm_8db4a7bb:

    # "[gg]" "Всякий раз, когда я прохожу мимо, мне хочется трахнуть тебя."
    "[gg]" "Every time I pass by, I want to fuck you."

# game/core/talk_with/talk_with_milf.rpy:124
translate eng milf_standart_talk_bdsm_29305588:

    # "Марина" "Я готова утолить твою жажду в любое время, милый."
    "Mary" "I'm ready to quench your thirst at any time, honey"

# game/core/talk_with/talk_with_milf.rpy:126
translate eng milf_standart_talk_bdsm_0db72315:

    # "[gg]" "Да?"
    "[gg]" "Yes?"

# game/core/talk_with/talk_with_milf.rpy:127
translate eng milf_standart_talk_bdsm_e47b6a5d:

    # "[gg]" "Что ж, я подумаю на твоим предложением. "
    "[gg]" "Well, I'll consider your offer."

# game/core/talk_with/talk_with_milf.rpy:129
translate eng milf_standart_talk_bdsm_0ad2dc38:

    # "Марина" "Продолжишь издеваться и не успеешь оглянуться, как я сама тебя трахну."
    "Mary" "You keep bullying and before you know it, I'll fuck you myself."

# game/core/talk_with/talk_with_milf.rpy:131
translate eng milf_standart_talk_bdsm_8d438d3a:

    # "[gg]" "Это самые приятные угрозы, какие я слышал в своей жизни. "
    "[gg]" "These are the nicest threats I've ever heard in my life."

# game/core/talk_with/talk_with_milf.rpy:133
translate eng milf_standart_talk_bdsm_e4cae6a3:

    # "Марина" "Рррррррр."
    "Mary" "Rrrrrrr."

# game/core/talk_with/talk_with_milf.rpy:137
translate eng milf_standart_talk_bdsm_ec9a34ce:

    # "[gg]" "Что готовишь?"
    "[gg]" "What are you cooking?"

# game/core/talk_with/talk_with_milf.rpy:140
translate eng milf_standart_talk_bdsm_2b230ca5:

    # "Марина" "Хи-хи-хи. В таком виде я лучше любого блюда."
    "Mary" "Hee hee hee. In this form, I am better than any dish."

# game/core/talk_with/talk_with_milf.rpy:141
translate eng milf_standart_talk_bdsm_9cb23ca5:

    # "[gg]" "Чёрт…"
    "[gg]" "Damn..."

# game/core/talk_with/talk_with_milf.rpy:142
translate eng milf_standart_talk_bdsm_53a59617:

    # "[gg]" "Теперь я вдвойне проголодался."
    "[gg]" "Now I'm doubly hungry."

# game/core/talk_with/talk_with_milf.rpy:143
translate eng milf_standart_talk_bdsm_f55f14b8:

    # "Марина" "Угощайся, милый. Я вся твоя. "
    "Mary" "Help yourself, honey. I'm all yours."

# game/core/talk_with/talk_with_milf.rpy:147
translate eng milf_standart_talk_bdsm_722aebd9:

    # "[gg]" "Скучаешь?"
    "[gg]" "Are you bored?"

# game/core/talk_with/talk_with_milf.rpy:149
translate eng milf_standart_talk_bdsm_64abbb5c:

    # "Марина" "Всегда."
    "Mary" "Always."

# game/core/talk_with/talk_with_milf.rpy:151
translate eng milf_standart_talk_bdsm_fc96a6f3:

    # "Марина" "Но ты в любой момент можешь развеять мою тоску, просто сняв штаны. "
    "Mary" "But at any moment you can dispel my longing just by taking off your pants."

# game/core/talk_with/talk_with_milf.rpy:153
translate eng milf_standart_talk_bdsm_ddce27c0:

    # "[gg]" "Ха-ха-ха!"
    "[gg]" "Ha ha ha!"

# game/core/talk_with/talk_with_milf.rpy:155
translate eng milf_standart_talk_bdsm_89f1329f:

    # "Марина" "Я серьёзно."
    "Mary" "I'm serious."

# game/core/talk_with/talk_with_milf.rpy:157
translate eng milf_standart_talk_bdsm_287f44fc:

    # "[gg]" "Оу…."
    "[gg]" "Oh...."

# game/core/talk_with/talk_with_milf.rpy:159
translate eng milf_standart_talk_bdsm_c0e58df9:

    # "Марина" "Надеюсь, ты найдёшь время, чтобы присоединиться ко мне. "
    "Mary" "I hope you find time to join me."

# game/core/talk_with/talk_with_milf.rpy:162
translate eng milf_standart_talk_bdsm_42b5b05c:

    # "[gg]" "Я постараюсь, честно."
    "[gg]" " I'll try, honestly."

# game/core/talk_with/talk_with_milf.rpy:165
translate eng milf_standart_talk_bdsm_9239fd04:

    # "[gg]" "У тебя игривое настроение."
    "[gg]" " You're in a playful mood."

# game/core/talk_with/talk_with_milf.rpy:167
translate eng milf_standart_talk_bdsm_61cb8c54:

    # "Марина" "Хочу разделить его с тобой, любименький. "
    "Mary" "I want to share it with you, my love."

# game/core/talk_with/talk_with_milf.rpy:169
translate eng milf_standart_talk_bdsm_a694d657:

    # "[gg]" "А как же Кристи и Кэт?"
    "[gg]" "What about Christy and Kat?"

# game/core/talk_with/talk_with_milf.rpy:171
translate eng milf_standart_talk_bdsm_c33a37ae:

    # "Марина" "Нет, ты только мой!"
    "Mary" "No, you're only mine!"

# game/core/talk_with/talk_with_milf.rpy:173
translate eng milf_standart_talk_bdsm_0a8a7e93:

    # "[gg]" "Вообще-то, я имел в виду их реакцию…"
    "[gg]" "Actually, I meant their reaction..."

# game/core/talk_with/talk_with_milf.rpy:175
translate eng milf_standart_talk_bdsm_864eb0f3:

    # "Марина" "Я думаю, они обзавидуются, хи-хи-хи!"
    "Mary" "I think they will be jealous, hee hee hee!"






#costume
###############################

