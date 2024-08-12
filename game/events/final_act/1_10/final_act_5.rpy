label final_act_5_block:
    
    show GG Invis
    show GG Invis:
        xalign .95
    "[gg]" "Нет, сейчас слишком опасно двигать конструкцию. "
    return
label final_act_5_block_power:
    "[gg]" "Уффф…."
    "[gg]" "Аргххх..!!!"
    "[gg]" "Нет, не получается."
    "[gg]" "Я всё ещё слишком слаб."

    return
label final_act_5_lvl_up:
    "[gg]" "Воооооо!"
    "[gg]" "Нормально пошло!"
    show final_act_gg_push_toilet 1
    with my_dissolve
    "[gg]" "У меня начинает получаться!"
    "[gg]" "Ещё несколько подходов, и я унитаз сдвинется в сторону. "
    "[gg]" "Но для этого мне надо подкачаться ещё сильнее!"
    return

label final_act_5_lvl_1:
    show final_act_gg_push_toilet anim_1
    with my_dissolve
    call final_act_5_lvl_up from _call_final_act_5_lvl_up
    $ descript = _("Мне удалось немного расшатать болты унитаза, но этого недостаточно. Теперь мне надо подкачаться ЕЩЁ СИЛЬНЕЕ!")
    $ final_act_toilet_lvl = 1
    $ time.time_forward(jump_to_main_interface = False)
    return


label final_act_5_lvl_2:
    show final_act_gg_push_toilet anim_2
    with my_dissolve
    call final_act_5_lvl_up from _call_final_act_5_lvl_up_1
    $ descript = _('Я практически расшатал болты унитаза. Остался последний рывок. Надо подкачаться. Сильнее. Намного сильнее. Чтоб аж вены на лбу выскочили.')
    $ final_act_toilet_lvl = 2
    $ time.time_forward(jump_to_main_interface = False)
    return

label final_act_5_lvl_3:
    show final_act_gg_push_toilet anim_3
    with my_dissolve
    $ final_act_toilet_lvl = 3
    call final_act_20 from _call_final_act_20
    return
label final_act_5:    
    $ i = locations['Prison'].image_buttons_times[time.time_now]
    if time.time_now != 'night' or 'james' in i or 'food' in i:
        call final_act_5_block from _call_final_act_5_block
    call show_bg_image_label from _call_show_bg_image_label_79
    show GG Invis
    show GG Invis:
        xalign .6
    show final_act_gg_push_toilet 1
    with my_dissolve
    call wait_click_label from _call_wait_click_label_15
    
    if final_act_toilet_lvl == 0:
        if final_act_power < 30:
            call final_act_5_block_power from _call_final_act_5_block_power
        else:
            call final_act_5_lvl_1 from _call_final_act_5_lvl_1

    elif final_act_toilet_lvl == 1:
        if final_act_power < 70:
            call final_act_5_block_power from _call_final_act_5_block_power_1
        else:
            call final_act_5_lvl_2 from _call_final_act_5_lvl_2
    elif final_act_toilet_lvl == 2:
        if final_act_power < 100:
            call final_act_5_block_power from _call_final_act_5_block_power_2
        else:
            call final_act_5_lvl_3 from _call_final_act_5_lvl_3


        #_("Я практически расшатал болты унитаза. Остался последний рывок. Надо подкачаться. Сильнее. Намного сильнее. Чтоб аж вены на лбу выскочили. ")

    jump main_interface_label



    # #"//При Попытке Активировать Унитаз Ночью, Когда Сил – 
    # #Недостаточно, Будет Появляться Сцена" ""
    # #//GG_vs_Tualet_1

    # "[gg]" "Уффф…."
    # "[gg]" "Аргххх..!!!"
    # "[gg]" "Нет, не получается."
    # "[gg]" "Я всё ещё слишком слаб."

    # #"////При Попытке Активировать Унитаз Ночью, 
    # #Когда Сил Хватает, Будет Появляется  Сцена" ""
    # #//GG_vs_Tualet_2

    # "[gg]" "Воооооо!"
    # "[gg]" "Нормально пошло!"
    # "[gg]" "У меня начинает получаться!"
    # "[gg]" "Ещё несколько подходов, и я унитаз сдвинется в сторону. "
    # "[gg]" "Но для этого мне надо подкачаться ещё сильнее!"


    # #Ну, собственно… всё, ёпта!


    # #Наша задача – убрать унитаз, найти там флешку. 
    # #Это активирует последний квест в тюрьме, который позволит нам из неё выйти. 

    # #///

    # #//Но, чтобы немного поднапрчь игрока, мы сделаем пару 
    # #незначительно эро-сцен, которые потребуют ВЫНОСЛИВОСТИ, 
    # #тем самым затянем игровое время.


    # # 



