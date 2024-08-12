label final_act_24:    #Final_Act_24


    $ events.pop('final_act_24', 0)
    #$ time.time_now = "evening"
    #call prison_talk_with_girl_officer_start
    #"Description" "Судя по царапинам на полу, под унитазом расположен тайник. Неплохо было бы узнать, что там.  Для этого я должен расшатать конструкцию, но мне не хватает сил. Надо подкачаться, как бы смешно это не звучало."
    scene black
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_232
    show GG Prison_WTF
    show GG Prison_WTF: 
        xzoom -1.0
        xalign .92 ypos 1081
    with my_dissolve
    #Активировать «кушать» ночью.
 
   #$ time.time_now = 'night'

    #Активировать «кушать» ночью.



    #show GG Turma
    "[gg]" "Эта девушка сегодня не придёт?.."
    #show GG Turma

    "[gg]" "Или она уже не придёт никогда?"
    #show GG Turma
    show GG Prison_Please
    with my_dissolve
    "[gg]" "Но ведь так умру с голоду!"
    #show GG Turma
    "[gg]" "Нет.. Я так не хочу."
    #show GG Turma
    "[gg]" "Это слишком мучительно. Живот и без того ноет от боли."
    #show GG Turma
    show GG Prison_Angry:
        easein_cubic .5 xalign .65
    "[gg]" "ЭЙ!!!"
    #show GG Turma
    "[gg]" "КТО-НИБУДЬ!!!"
    show GG Prison_Angry:
        easein_cubic .1 xalign .58
        easein_cubic .3 xalign .65
    #show GG Turma
    "[gg]" "Я ХОЧУ КУШАТЬ! КТО-НИБУДЬ! ПРИНЕСИТЕ МНЕ ЕДЫ!"
    #show GG Turma
    show GG Prison_Angry:
        easein_cubic .1 xalign .58
        easein_cubic .3 xalign .65
    "[gg]" "ВЫ НЕ ИМЕЕТЕ ПРАВА МОРИТЬ МЕНЯ ГОЛОДОМ! "
    #show GG Turma
    show GG Prison_Angry:
        easein_cubic .1 xalign .58
        easein_cubic .3 xalign .65
    "[gg]" "ВЫ МЕНЯ СЛЫШИТЕ?!! АЛО!!!"
    show GG Prison_WTF:
        easein_cubic 1.5 xalign .9
    #show GG Turma
    "[gg]" "Блядь…"
    #show GG Turma
    "[gg]" "Никого нет."
    #//функция «кушать» более недоступна

    $ Event(
        'final_act_25',  
        time      = ['night',], 
        )
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_23 
    $ renpy.pause(.3, hard = True)
    call final_act_blind_transition_to_black_label from _call_final_act_blind_transition_to_black_label_14
    $ time.time_now = 'morning'
    jump main_interface_label