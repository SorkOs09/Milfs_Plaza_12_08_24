label final_act_26_end_func:
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_29
    $ renpy.pause(.4, hard=True)
    scene black with my_dissolve
    $ renpy.pause(.4, hard=True)
    if time.time_now == 'morning':
        $ time.time_now = 'afternoon'
    else:
        $ time.time_now = 'night'
    if location_now == 'Milf_Room':
        $ location_now = 'Hall'
    return
label final_act_26_christie:    #Final_Act_26
    $ events.pop('final_act_26_christie', 0)
    call show_bg_image_label from _call_show_bg_image_label_242 
    call show_additional_images_label from _call_show_additional_images_label_65
    show Christie Normal
    show Christie Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Smile
    show GG Smile at go_from_left



    #Поговорить с Кристи или Мариной утром, днём или вечером.



    #//Если с Кристи

    "[gg]" "Знаешь, Кристи, мне было очень приятно получить от подарок, когда я находился в заключении. "
    show Christie Smile
    "Кристи" "Ты имеешь в виду мои трусики? Хи-хи-хи."
    show GG Passion
    "[gg]" "Ага. "
    show GG Passion
    "[gg]" "Мысли о тебе позволили мне продержаться на пару ночей дольше."
    show Christie Passion
    "Кристи" "Я лишь хотела раззадорить тебя, [gg]."
    show Christie Passion
    "Кристи" "Настоящий подарок ты найдёшь лишь тогда, когда посетишь Марину ночью. "
    show GG Surprise
    "[gg]" "Только Марину?  "
    show Christie Smile
    "Кристи" "Не умничай!"
    #GG_Normal

    show Christie Smile
    "Кристи" "Там тебя ожидает всё то, о чём ты не мог и помыслить. "
    show GG Surprise
    "[gg]" "Добавки просить не придётся, хи-хи-хи!"
    show GG Normal
    "[gg]" "Придётся поверить тебе на слово. "
    $ block_sister_home = True

    call final_act_26_end_func from _call_final_act_26_end_func
    jump main_interface_label
#     #//Если с Милфой
label final_act_26_milf:
    $ events.pop('final_act_26_milf', 0)
    call show_bg_image_label from _call_show_bg_image_label_243 
    call show_additional_images_label from _call_show_additional_images_label_115
    if time.time_now in ('evening', 'night'):
        show Milf Night_Normal
        show Milf Night_Normal:
            xalign .85
            ypos 1085

    else:
        show Milf Normal
        show Milf Normal:
            xalign .85
            ypos 1085

    with Dissolve(.5)

    show GG Smile
    show GG Smile at go_from_left

    "[gg]" "Маришка, любимая, наконец-то мы можем… Ну…."
    show GG  Embarrassment
    "[gg]" "Реализовать всё то, о чём так жалостливо фантазировали во время моего заключения. "
    if time.time_now  in ('evening', 'night'):
        show Milf Night_Smile
    
    else:
        show Milf Laughs
    
    "Марина" "Ха-ха-ха! "
    if time.time_now in ('evening', 'night'):
        show Milf Night_Smile
    else:
        show Milf Smile
    "Марина" "Ты опомнился быстрее, чем я рассчитывала. "
    show GG Skepticism
    "[gg]" "Сомневалась в моих силах? "
    if time.time_now in ('evening', 'night'):
        show Milf Night_Passion
    else:
        show Milf Passion
    "Марина" "Ниcколечко."
    if time.time_now in ('evening', 'night'):
        show Milf Night_Passion
    else:
        show Milf Passion
    "Марина" "Я прямо сейчас готова затрахать тебя до смерти, но не хочу, чтобы дом рухнул под ударами моих ягодиц, хе-хе-хе."
    show GG Skepticism
    "[gg]" "Ну и чего же мы тогда ждём?!"
    show GG Skepticism
    "[gg]" "Я весь сгораю от нетерпения!"
    if time.time_now in ('evening', 'night'):
        show Milf Night_Passion
    else:
        show Milf Passion
    "Марина" "Ночью, дорогой. Приходи ко мне в комнату ночью."
    show GG Surprise
    "[gg]" "А как же Кристи?"
    show GG Normal
    "[gg]" "Она наверняка услышит наши стоны и грохот. "
    if time.time_now in ('evening', 'night'):
        show Milf Night_Passion
    else:
        show Milf Passion
    "Марина" "И?"
    show GG Normal
    "[gg]" "И обидится."
    if time.time_now in ('evening', 'night'):
        show Milf Night_Passion
    else:
        show Milf Passion
    "Марина" "Тогда не забудь уделять время и ей тоже. "
    show GG Normal
    "[gg]" "Она тоже приглашена? "
    if time.time_now in ('evening', 'night'):
        show Milf Night_Embarrassment
    else:
        show Milf Embarrassment
    "Марина" "Я же говорила – мы сдружились. "
    if time.time_now in ('evening', 'night'):
        show Milf Night_Embarrassment
    else:
        show Milf Embarrassment
    "Марина" "Да и ты, как я помню, упоминал о своей любви к нам обеим."
    show GG Smile
    "[gg]" "И это чистая правда!"
    if time.time_now in ('evening', 'night'):
        show Milf Night_Passion
    else:
        show Milf Passion
    "Марина" "Нет. Не надо. Только не словами."
    if time.time_now in ('evening', 'night'):
        show Milf Night_Passion
    else:
        show Milf Passion
    "Марина" "Язык тебе ещё пригодится."
    if time.time_now in ('evening', 'night'):
        show Milf Night_Smile at hehe_transform()
    else:
        show Milf Smile at hehe_transform()
    "Марина" "Хи-хи-хи."
    $ block_milf_home = True
    $ descript = _("Посетить спальню Марины сегодня ночью.")
    $ Event('final_act_27', location = "Milf_Room", time = 'night')
    call final_act_26_end_func from _call_final_act_26_end_func_1
    jump main_interface_label