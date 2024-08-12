label final_act_9:    #Final_Act_8

        
    # "Description" "Судя по царапинам на полу, под унитазом расположен тайник. Неплохо было бы узнать, что там. "



    #Активировать туалет НОЧЬЮ (КОГДА НИКОГО НЕТ – ЭТО ВАЖНО!)

    #"//При Любой Попытке Активировать Туалет Днём Или Когда 
    #В Сцене Присутствуют Посторонние Спрайты Ночью, 
    #Игрок Должен Комментировать Так" ""
    $ i = locations['Prison'].image_buttons_times[time.time_now]
    if time.time_now != 'night' or 'james' in i or 'food' in i:
        call final_act_5_block from _call_final_act_5_block_1
        jump main_interface_label
    if hasattr(store, 'final_act_toilet_lvl'):
        jump final_act_5
    call show_bg_image_label from _call_show_bg_image_label_234
    show GG Invis
    show GG Invis:
        xalign .6
    show final_act_gg_push_toilet 1
    with my_dissolve

    #//GG_vs_Tualet_1

    "[gg]" "Уффф…."
    "[gg]" "Аргххх..!!!"
    "[gg]" "Нет, не получается."
    "[gg]" "Болты, что его удерживают, слишком хорошо закреплены."
    "[gg]" "Возможно, если я попробую расшатать, у меня всё получится. "
    #//GG_vs_Tualet_1anim
    show final_act_gg_push_toilet anim_1
    with my_dissolve
    "[gg]" "Уууууууффффф!!!"
    "[gg]" "Давай…"
    "[gg]" "Ну же!!..."
    #//GG_vs_Tualet_1
    show final_act_gg_push_toilet 1
    with my_dissolve
    "[gg]" "Нет, не выходит."
    "[gg]" "Не хватает сил. "
    "[gg]" "Я слишком слаб, и я жутко голоден…"
    "[gg]" "В другой раз."

    #for i in ('morning', 'afternoon'):

    $ i = Function(renpy.show, 'final_act_prison_action_arrow_gym', what = 'final_act_prison_action_arrow', 
                at_list=[
                final_act_7_action_arrow_transform(
                     pos_finish=(1150, 820),
                     dur = .15, 
                     rot = 0.0,
                     alpha_finish = 1.0,
                     )
                ])
    
    $ j = Function(renpy.show, 'final_act_prison_action_arrow_gym', what = 'final_act_prison_action_arrow', 
                at_list=[
                final_act_7_action_arrow_transform(
                     pos_finish=(1200, 900),
                     dur = .15, 
                     rot = 0.0,
                     alpha_finish = 0.0,
                     )
                ])

    $ locations['Prison'].buttons[0].update({
        'gym':{
            'cords'  : (1150, 810, 285, 230), 
            'hovered': i,
            'unhovered': j,
            'action' : [j, Jump('prison_gym_label')],
            }
            }
            )

    python:
        final_act_power      = 0
        final_act_toilet_lvl = 0

    
        locations['Prison'].image_buttons_times['night'].update(
        {'james':Jump('final_act_9_james')}
        )


        
        for i in range(1, 20):
            n = (i-1)*100
            j = Crop((0, 0, 120, 1080), 'black')
            renpy.show('black_'+str(i), what = j, 
                at_list=[
                final_act_4_blinds_transform(
                    xp  = n,
                    dur = i*.075,
                    xp_fin = n,
                    )
                ])
        
        renpy.pause(1.6, hard = True)
        
        descript = _('Судя по царапинам на полу, под унитазом расположен тайник. Неплохо было бы узнать, что там.  Для этого я должен расшатать конструкцию, но мне не хватает сил. Надо подкачаться, как бы смешно это не звучало.')
    
        time.time_now = 'morning'
        time.day_now += 1
    #//На следующий день появится кнопка «Отжиматься». 

    jump main_interface_label




    #Пропустить 1 день.

    #Активировать спрайт Джеймса, который появляется только ночью



label final_act_9_james:
    #//Kamera_Scene
    
    scene final_act_prison_large_bg night:
        xalign 1.0
    #show final_act_prison_milf_at_large_bg:
    #    xalign 1.0
    #show final_act_prison_officer_at_large_bg:
    #    xalign 1.0
    show GG Prison_WTF
    show GG Prison_WTF: 
        xzoom -1.0
        xalign .86 ypos 1081

    with my_dissolve
    $ renpy.pause(.35, hard = True)
    show final_act_prison_large_bg night:
        easein .75 xalign .47
   #show final_act_prison_milf_at_large_bg:
   #     easein .75 xalign .47
   # show final_act_prison_officer_at_large_bg:
   #     easein .75 xalign .47
    
    $ renpy.pause(.8, hard = True)
    scene final_act_prison_large_bg night:
        xalign .47
    show Nikolaya Normal
    show Nikolaya Normal:
        xzoom -1.0
        xalign .1 ypos 1081
    show GG Prison_WTF
    show GG Prison_WTF: 
        xzoom -1.0
        xalign .86 ypos 1081
    with my_dissolve


    #show GG Turma
    "[gg]" "Джеймс?.."
    #show GG Turma
    "[gg]" "Это ты?"
    ##show Brat Normal
    "Джеймс" "Я."
    #show GG Turma
    "[gg]" "….."
    #show GG Turma
    "[gg]" "Я знаю, мне никогда не оправдаться перед тобой."
    #show GG Turma
    "[gg]" "Моё предательство очевидно, а моя вина требует наказания."
    #show GG Turma
    "[gg]" "И ты вправе поступать со мной так, как считаешь нужным. "
    #show GG Turma
    "[gg]" "Но я не могу не сказать…"
    #show Brat Normal
    "Джеймс" "…?"
    #show GG Turma
    "[gg]" "Прости меня, брат."
    #show GG Turma
    "[gg]" "Прости…"
    #show Brat Normal
    "Джеймс" "У меня нет брата."
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_10

    show Nikolaya:
        xzoom 1.0 xalign .07
        easein 1.75 xalign -.8

    $ from_say_screen = False
    $ renpy.pause(2.0, hard = True)
    #// Brat_Normal исчезает влево

    #show GG Turma
    "[gg]" "Чёрт…"
    #show GG Turma
    "[gg]" "Вот и поговорили."
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_11
    $ renpy.pause(.5, hard = True)

    $ locations['Prison'].image_buttons_times['morning'].update(
            {'officer': Jump('final_act_10')}
            )


        

    
    $ locations['Prison'].image_buttons_times['night'].pop('james', 0)
    

    call final_act_blind_transition_to_black_label from _call_final_act_blind_transition_to_black_label_7

    python:
        for i in range(1, 20):
            n = (19-i)*102
            j = Crop((n, 0, 102, 1080), 'locations/bg/Prison/afternoon.png')
            

            dur = .2+i*.1,
            renpy.show('final_act_4_prison_morning_'+str(i), what = j, 
                at_list=[
                final_act_4_blinds_transform(
                    xp  = n+102,
                    dur = .25+i*.08,
                    xp_fin = n,
                    )
                ])

        renpy.pause(2.5, hard = True)

        time.time_now = 'morning'
        
    jump main_interface_label

    #//Kamera_Night

    #//GG_Kamera_1


