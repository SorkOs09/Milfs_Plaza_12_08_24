
transform final_act_7_action_arrow_transform(
             pos_finish=(0, 0), 
             dur = .1, 
             rot = 0.0,
             alpha_finish = 1.0,
             ):
    
    rotate rot 
    parallel:
        easein_cubic dur pos pos_finish 
    parallel:
        easein_cubic dur*.5 alpha alpha_finish
label final_act_7_debug:
    $ locations['Prison'].image_buttons_times['afternoon'].update(
                {'milf':Jump('final_act_7')}
                )

    $locations['Prison'].image_buttons_times['morning'].update(
                {'officer': Jump('final_act_13_officer_repeat')}
                )

                

        #time.time_forward(jump_to_main_interface = False)
    $ descript = _("Я на грани срыва…")
    
      

    $ time.time_now = 'afternoon'

    scene black
    show image Text("DEBUG: переход к final_act_7"):
        align(.5, .5)
    with my_dissolve 
    call wait_click_label from _call_wait_click_label_31 
label final_act_7:    #Final_Act_6 
    # if store.test_debug_mod:
    #     scene black
    #     with my_dissolve
    #     menu:
    #         "DEBUG: Этот ивент уже был в предыдущих сборках и возможно вы его уже проверяли.\nПропустить ивент?"

    #         "  Да  ":
    #             jump final_act_7_end
    #         "  Нет  ":
    #             pass
    call prison_talk_with_milf_start from _call_prison_talk_with_milf_start

    #"Description" "Я на грани срыва…"


    #//Milf_Turma

    #//Нужно нажать на спрайт Милфы, чтобы активировать диалог

    #//Если игрок пропустит время – ничего страшного. 
    #Этот спрайт для активации должен будет появляться Утром и Днём 
    #до тех пор, пока игрок не активирует его.

    #//Возможно, ты спросишь «А нахуя?» Не проще ли заблокировать? 
    #Нет, не проще, так как если мы постоянно будем блочить управление, 
    #интерактив совсем исчезнет и игра скатится в сраную линейную новеллу. 
    #Мы имитируем маленькую, мнимую, но всё же свободу действий.





    #//Kamera_Scene

    ##show Milf City
    #"Марина" ""
    #show GG Prison_Normal
    "[gg]" "Извини…"
    show Milf Street_Silence
    with my_dissolve
    #show Milf City
    "Марина" "Тебе не за что извиняться, дорогой!"
    #show Milf City

    show Milf Street_Sad
    with my_dissolve
    "Марина" "Это я во всём виновата!"
    #show Milf City
    "Марина" "Мне не стоило тебя пускать…"
    show GG Prison_Please
    "[gg]" "Прекрати. Ты прекрасно знаешь, что ВСЁ ЭТО – последствия моего образа жизни."
    #show GG Prison_Normal
    show GG Prison_WTF
    "[gg]" "Я сам себе враг, Маришка. "
    #show GG Prison_Normal
    show GG:
        xzoom 1.0
        easein 5.0 xalign 1.5
    show shadow_full
    show shadow_full:
        alpha 0.0
        easein 10.0 alpha 1.0
    "[gg]" "Лучше оставь меня…."
    #show Milf City
    show Milf Street_Angry
    with my_vpunch
    "Марина" "Хватит самобичевания! Я тебя не брошу. Мы обязательно придумаем, как тебя вызволить отсюда. "
    #show Milf City
    with my_vpunch
    "Марина" "Ну же. Ты мужчина! Держи себя в руках. Николас просто хочет испугать тебя. "
    #show GG Prison_Normal
    show GG Prison_Please:
        xzoom -1.0
        easein 3.5 xalign .86
    show shadow_full:
        easein .5 alpha 0.0
    
    "[gg]" "Ты думаешь, это проделки брата?"
    #show Milf City
    show GG Prison_Chagrin
    with my_dissolve
    "Марина" "Уверена."
    #show Milf City
    hide shadow_full
    show GG Prison_Please:
        xzoom -1.0
        xalign .86
    with my_dissolve
    "Марина" "У него полно связей в полиции."
    #show Milf City
    with my_vpunch
    "Марина" "Чтобы там тебе не вменяли, дело шито белыми нитками! Я знаю, что ты невиновен."
    #show GG Prison_Normal
    show GG Prison_WTF
    with my_dissolve
    "[gg]" "В этот раз я бессилен. "
    #show GG Prison_Normal
    show GG Prison_Chagrin
    with my_dissolve
    "[gg]" "Офицер сказал, что у него есть свидетель, который убедил прокурора в моей вине."
    #show Milf City
    show Milf Street_Sad
    with my_dissolve
    "Марина" "Это ещё ничего не значит, милый."
    #show Milf City
    "Марина" "Тебя не смогут посадить, если нет фактических доказательств. "
    #show GG Prison_Normal
    show GG Prison_Please
    with my_dissolve
    "[gg]" "Ты уверена?"
    #show Milf City
    show Milf Street_Angry
    with my_vpunch
    "Марина" "Абсолютно!"
    #show Milf City
    "Марина" "Им понадобится время, чтобы собрать улики, а мы сделаем всё возможное, чтобы найти хорошего адвоката."
    #show GG Prison_Normal
    show GG Prison_Please
    with my_dissolve
    "[gg]" "Спасибо, Маришка. Спасибо за всё, что ты делаешь для меня."
    #show Milf City
    "Марина" "Не отчаивайся, [gg]. Я с тобой."
    #show GG Prison_Normal
    show GG Prison_Chagrin
    with my_dissolve
    "[gg]" "Я люблю тебя."
    #show Milf City
    show Milf Street_Chagrin
    with my_dissolve
    "Марина" "И да, я тоже тебя люблю."
    #//Officer_Normal выезжает слева
    show final_act_prison_large_bg morning:
        easein_cubic 1.0 xalign .28
    show GG Prison_Please:
        easein_cubic 1.0 xalign .93
    
    show Officer Normal
    show Officer Normal at go_from_left(xxalign=-.12,)# ttimer=1.7)
    show Milf
    show Milf:
        easein_cubic 1.0 xalign .27

    "Офицер" "Свидание окончено. Я попрошу вас следовать за мной, к выходу."
    #show Milf City
    show Milf:
        xzoom 1.0 xalign .27
    with my_dissolve
    "Марина" "Да, разумеется."
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_2 
    
    $ renpy.pause(.5, hard = True)
    #//Конец сцены
    show Officer:
        xzoom -1
        easein 1.75 xalign -.65
    show Milf:
        easein 1.75 xalign -.65
    $ renpy.pause(2.0, hard = True)
    #with my_dissolve
    #//Kamera_Evening

    #//GG_Kamera_1
    #$ locations['Prison'].image_buttons_times['afternoon'].pop('milf', 0)

label final_act_7_end:
    $ debug_next('final_act_8_debug',)
    
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
    
    call final_act_blind_transition_to_black_label from _call_final_act_blind_transition_to_black_label_1


    
    jump main_interface_label #final_act_8



