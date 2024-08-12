label final_act_17:    #Final_Act_14
   # $ events.pop('final_act_17', 0)
    
    call prison_talk_with_girl_officer_start from _call_prison_talk_with_girl_officer_start_2
    "Офицерша" "В чём твой секрет?"
    
    "[gg]" "Что ты имеешь в виду?"
    show GirlOfficer Normal
    "Офицерша" "Это женщина, что посещает тебя. Она так самоотверженно любит тебя."
    show GG Prison_Surprise
    with my_vpunch
    "[gg]" "Ты наблюдала за нами?"
    show GirlOfficer Normal
    "Офицерша" "Извини, было трудно сдержаться. "
    show GirlOfficer Normal
    "Офицерша" "Вы такие страстные любовники."
    show GG Prison_Embarrassment
    with my_dissolve
    "[gg]" "С…спасибо."
    
    "[gg]" "Ради Маришки я готов на всё. "
    
    "[gg]" "Мне нет смысла жизнь, если её или Кристи нет рядом."
    show GirlOfficer Normal
    "Офицерша" "Кристи?.."
    show GirlOfficer Normal
    "Офицерша" "У тебя сразу две любимые женщины?"
    
    "[gg]" "Да, но вряд ли ты поймёшь…"
    #show GirlOfficer Normal
    with my_vpunch
    "Офицерша" "Эй, я не какая-то зануда."
    #show GirlOfficer Normal
    "Офицерша" "И всё прекрасно понимаю."
    #show GirlOfficer Normal
    "Офицерша" "Просто меня удивляет, что даже здесь, в таком мрачном месте, где вся система настроена против человека, вы умудряетесь отдаться в руки страсти. "
    show GG Prison_Embarrassment
    with my_dissolve
    "[gg]" "Не знаю что и сказать… Нам сложно друг без друга."
    show GG Prison_WTF
    with my_dissolve
    "[gg]" "Да и к тому же, Маришки и Кристи – это смысл моей жизни. Мотивация сражаться."
    show GG Prison_Chagrin
    with my_dissolve
    
    "[gg]" "В противном случае я бы давно сдался…"
    
    "[gg]" "И принял бы участь такой, какая она есть."
    #show GirlOfficer Normal
    "Офицерша" "Признаюсь, мне очень завидно."
    #show GirlOfficer Normal
    "Офицерша" "Я бы тоже хотела иметь такую любовь."
    show GG Prison_Smile
    with my_dissolve
    
    "[gg]" "Никогда не поздно её найти."
    #show GirlOfficer Normal
    "Офицерша" "Возможно…"
    #//+ 50 ВЫНОСЛИВОСТИ
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_21
    $ renpy.pause(.3, hard = True)
    $ locations['Prison'].image_buttons_times['afternoon'].update(
        {'milf':Jump('final_act_19')}
        )
    
    
    $ Hide('info_panel')()
    $ final_act_sitost = min(final_act_sitost+50, 100)
    $ Show('info_panel', ttext = "+50", iimage = "info_panel_prison_sitost")()

    

    call final_act_blind_transition_to_black_label from _call_final_act_blind_transition_to_black_label_11
        
    $ time.time_now = 'morning'


    jump main_interface_label

