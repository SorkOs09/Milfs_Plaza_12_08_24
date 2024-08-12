label final_act_8_debug:


    
    $ descript = _("Одиночество становится невыносимым. Стоило бы походить, да осмотреть своё временное жилище, пока я совсем не поехал крышей от гнетущих мыслей.")
    

    $ j = Function(renpy.show, 'final_act_prison_action_arrow_toilet', what = 'final_act_prison_action_arrow', 
                at_list=[
                final_act_7_action_arrow_transform(
                     pos_finish=(970, 540),
                     dur = .15, 
                     rot = 0.0,
                     alpha_finish = 0.0,
                     )
                ])
    $ i = Function(renpy.show, 'final_act_prison_action_arrow_toilet', what = 'final_act_prison_action_arrow', 
                at_list=[
                final_act_7_action_arrow_transform(
                     pos_finish=(980, 575),
                     dur = .15, 
                     rot = 0.0,
                     alpha_finish = 1.0,
                     )
                ])
    
    $ locations['Prison'].buttons[0].update({
        'toilet':{
            'cords'  : (930, 400, 280, 415), 
            'hovered': i,
            'unhovered': j,
            'action' : [j, Jump('final_act_8')],
            }
            }
            )
    $ time.time_now = 'evening'
    scene black
    show image Text("DEBUG: переход к final_act_8"):
        align(.5, .5)
    with my_dissolve 
    call wait_click_label from _call_wait_click_label_33 
label final_act_8:    #Final_Act_7 
    # if store.test_debug_mod:
    #     scene black
    #     with my_dissolve
    #     menu:
    #         "DEBUG: Этот ивент уже был в предыдущих сборках и возможно вы его уже проверяли.\nПропустить ивент?"

    #         "  Да  ":
    #             jump final_act_8_end
    #         "  Нет  ":
    #             pass

    #"Description" "Одиночество становится невыносимым. Стоило бы походить, да осмотреть своё временное жилище, пока я совсем не поехал крышей от гнетущих мыслей."

    

    call show_bg_image_label from _call_show_bg_image_label_231
    
    show GG Prison_WTF
    show GG Prison_WTF:
        xzoom -1.0
        xalign .95

    with my_dissolve

    #Активировать туалет.




    #//Tualet_art

    "[gg]" "Хм… "
    "[gg]" "И зачем мне пялиться на унитаз?"
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_3

    $ from_say_screen = False
    $ i = renpy.call_screen('circle_attention_screen', xp = 1100, yp = 750, zm = .5)
    show GG Prison_WTF:
        xzoom -1.0
        easein .75 xalign .36
        xzoom 1.0
    "[gg]" "Ну хорошо. Вот. Я смотрю на него. Ничего примечательного. "

    show shadow_full:
        alpha .75
    with my_dissolve
    "[gg]" "А хотя постойте-ка…"
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_4

    $ from_say_screen = False
    $ renpy.call_screen('circle_attention_screen', xp = 1150, yp = 750, zm = .5)
    show GG Prison_WTF:
        xalign .36
        xzoom 1.0
    with my_dissolve
    "[gg]" "Рядом с унитазом видны малозаметные царапины на полу."
    show GG Prison_WTF:
        easein .85 xalign .75
        
    "[gg]" "И о чём это тебе говорит, Мисс Марпл?"
    show GG Prison_Speak:
        xalign .85
        xzoom -1.0
    hide shadow_full
    with my_dissolve
    
    "[gg]" "Очевидно, его отодвигали. "
    show GG Prison_WTF
    "[gg]" "Но зачем? "
    
    "[gg]" "Кто знает, может снизу вырыт тоннель, ведущий на другой конец города, а лучше – в другой штат!"
    
    "[gg]" "Допустим. Но это последнее, что я стал бы делать при текущих обстоятельствах."
    show GG Prison_Speak
    "[gg]" "А что, если там тайник с посланием от предыдущего сидельца? "
    show GG Prison_Surprise
    "[gg]" "Например, сто миллионов долларов, которые я смогу использоваться для расплаты!"
    show GG Prison_Smile
    
    "[gg]" "Отстрою себе роскошное шато на берегу Порт-Марли, а дворецкий по имени Альфрэд поможет мне шить костюм летучей мыши…"
    show GG Prison_Angry:
        xzoom 1.0
    show shadow_full:
        alpha .4
    with my_vpunch
    "[gg]" "Держи себя в руках, [gg], это не замок Иф, а я не Монте-Кристо. "
    "[gg]" "….."
    show GG Prison_Speak:
        xzoom -1.0
    hide shadow_full
    with my_vpunch
    "[gg]" "Ну что-то же под унитазом наверняка есть! "
    show GG Prison_WTF
    "[gg]" "Не стали бы его просто так отодвигать и задвигать обратно."
    show GG Prison_Please
    "[gg]" "Ну и чего я пялюсь?"
    show GG Prison_WTF
    "[gg]" "Надо бы пододвинуть самому и узнать."
    "[gg]" "….."
    show GG Prison_Please
    "[gg]" "Сейчас? "
label final_act_8_end:
    
    $ descript = _("Судя по царапинам на полу, под унитазом расположен тайник. Неплохо было бы узнать, что там. ")
    
    $ i = locations['Prison'].buttons[0]['toilet']
    $ i['action'][1] = Jump('final_act_9')

    if time.time_now != 'night':
        show GG Prison_WTF
        "[gg]" "Нет, сейчас я этого делать не стану. Полицейский может явится в любой момент. Лучше попробую ночью, посетителей не придвидится…"
        call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_5

        $ renpy.pause(.5, hard = True)
    else:
        jump final_act_9
    

    call final_act_blind_transition_to_black_label from _call_final_act_blind_transition_to_black_label_2
        #time.time_now = 'morning'
        #time.day_now += 1
    $ time.time_forward(jump_to_main_interface = False)
        
    jump main_interface_label #final_act_10
