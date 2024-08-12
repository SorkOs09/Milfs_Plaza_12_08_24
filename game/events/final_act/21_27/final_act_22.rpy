label final_act_22:    #Final_Act_22
   # $ events.pop('final_act_22', 0)
   # $ time.time_now = "evening"

   # "Description" "Мне удалось немного расшатать болты унитаза, но этого недостаточно. Теперь мне надо подкачаться ЕЩЁ СИЛЬНЕЕ! "

    call prison_talk_with_girl_officer_start from _call_prison_talk_with_girl_officer_start_3


    #Активировать Покушать



    #Активировать «питаться» ночью //хотя там в любом случае в другое время нельзя



    #show Policegirl Eda
    "Офицерша" "Проголодался, бедняга?"
    #show GG Turma
    show GG Prison_Embarrassment
    with my_dissolve
    "[gg]" "Да... Но больше не могу брать у тебя еду."
    #show Policegirl Eda
    "Офицерша" "Звучит как полный бред."
    #show Policegirl Eda
    "Офицерша" "Но я тебе не официантка. Не хочешь как хочешь. "
    #show GG Turma
    show GG Prison_Please
    with my_dissolve
    "[gg]" "Извини, я вовсе не пытаюсь выделываться. "
    #show GG Turma
    show GG Prison_WTF
    with my_dissolve
    "[gg]" "Просто Марина, моя женщина, очень ревнивая…"
    #show Policegirl Eda
    show GirlOfficer Smile
    with my_vpunch
    "Офицерша" "Она думает, что я таким образом подбиваю к тебе клинья?!"
    #//мысли

    #show GG Turma
    show shadow_full:
        alpha .75
    with my_dissolve
    "[gg]" "{i}И вновь я боюсь говорить правду…{/i}"
    #show GG Turma
    "[gg]" "{i}Может быть, если я промолчу, она сама всё додумает?{/i}"
    #//конец мысли
    hide shadow_full
    show GirlOfficer Normal
    with my_dissolve
    #show Policegirl Eda
    "Офицерша" "Это нелепо, [gg], но кто я такая, чтобы вставать между тобой и твоей женщиной?"
    #show Policegirl Eda
    "Офицерша" "Наверное ей лучше знать, как о тебе позаботиться. "
    #show Policegirl Eda
    show GirlOfficer:
        xzoom 1.0 xalign 0.0
        easein_cubic 4.5 xalign -1.0
    "Офицерша" "Прощай."
    #show GG Turma
    show GG Prison_Please
    with my_dissolve
    "[gg]" "Извини…"
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_37 
    $ renpy.pause(.3, hard = True)
    call final_act_blind_transition_to_black_label from _call_final_act_blind_transition_to_black_label_16

    python:
        try:
            del prison_food_activate
        except:
            pass
        
        
        
        renpy.pause(1.5, hard = True)
        time.time_now = 'morning'
        locations['Prison'].image_buttons_times['afternoon'].update(
        {'milf':Jump('final_act_23')}
        )
        descript = _("Я жутко голоден. Нужно поговорить об этом с Мариной.")

    jump main_interface_label

