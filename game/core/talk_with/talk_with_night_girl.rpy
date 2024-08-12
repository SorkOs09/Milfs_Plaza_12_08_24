label night_girl:
label talk_with_night_girl:
    if preferences.language not in (None, 'eng', 'rus', 'turk'):
        #$ add_to_gallery(-5)
        $ Event('night_girl',     'GG_Room',     'night_girl', day_start = time.day_now + 7, time = ['morning'])
        #scene black with my_dissolve
        #$ renpy.pause(.5, hard = True)

        jump main_interface_label
    if from_gallery_check():
        $ money = 500
    stop music fadeout 1.5
    play music 'audio/n_girl.mp3' fadein 1.5
    scene expression 'images/cg/ep1/night_collector/Night_collector_1.png'
    show GG Invis
    show GG Invis:
        xalign .75
    with vpunch


    '[gg]' "Какого хера?!"
    scene expression 'images/cg/ep1/night_collector/Night_collector_5.png'
    show GG Invis
    show GG Invis:
        xalign .75
    with my_dissolve
    'Ночная гостья' "Соскучился?"
    '[gg]' "Опять ты! Так и до сердечного приступа недалеко!"
    scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
    show GG Invis
    show GG Invis:
        xalign .75
    with my_dissolve
    'Ночная гостья' "Ого, серьёзно?"
    '[gg]' "Ну а ты как думаешь?"
    scene expression 'images/cg/ep1/night_collector/Night_collector_5.png'
    show GG Invis
    show GG Invis:
        xalign .75
    with my_dissolve
    'Ночная гостья' "Оу, мне так неловко…"
    '[gg]' "Хорошо, что ты понимаешь это."
    scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
    show GG Invis
    show GG Invis:
        xalign .75
    with my_dissolve
    'Ночная гостья' "Да я шучу, придурок. Мне на тебя насрать."
    '[gg]' "Это жестоко…"
    'Ночная гостья' "Жестоко будет, когда ты не заплатишь. Где мои деньги?"


    menu:
        "Вот, возьми (отдать {i}{b}20{/b}{/i} баксов)." if money >= 20:
            $ money -= 20
            $ show_text_animation('-20 money')
            scene expression 'images/cg/ep1/night_collector/Night_collector_8.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Люблю, когда всё по-моему. "
            '[gg]' " Надеюсь, ты удовлетворена и мы больше не увидимся."
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with vpunch
            'Ночная гостья' "Ещё чего. Я буду навещать тебя каждую неделю, пока ты, наконец, не выплатишь долг. "
            '[gg]' " …"
            scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Оривидэрчи, придурок. "
        "!Вот, возьми (отдать {i}{b}20{/b}{/i} баксов)." if money <  20:
            $ pass
        "Это всё, что я могу дать (отдать {i}{b}[money]{/b}{/i} баксов)." if money > 0 and money < 20:
            $ add_ach('ACH_13')
            $ show_text_animation('-'+str(money)+' money')
            $ money = 0
            scene expression 'images/cg/ep1/night_collector/Night_collector_8.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Не густо, конечно, но это лучше, чем совсем ничего. "
            '[gg]' " Надеюсь, ты удовлетворена и мы больше не увидимся."
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with vpunch
            'Ночная гостья' "Ещё чего. Я буду навещать тебя каждую неделю, пока ты, наконец, не выплатишь долг. "
            '[gg]' " …"
            scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Оривидэрчи, придурок. "
        "Извини, но у меня вообще ничего нет…" if True:
            scene expression 'images/cg/ep1/night_collector/Night_collector_3.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Мать твою, ты что, хочешь, чтобы я выпотрошила тебя? "
            '[gg]' " Клянусь собственными яйцами, у меня нет ни копейки."
            'Ночная гостья' "Хочется в это верить, иначе в следующий раз, ты обязательно останешься без них."
            '[gg]' " В следующий раз?!"
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "А ты что думал? Я буду навещать тебя каждую неделю, пока ты, наконец, не выплатишь долг. "
            '[gg]' " …"
            scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Оривидэрчи, придурок. "
        "Я дам тебе вдвое больше, если ты покажешь мне сиськи (отдать {i}{b}40{/b}{/i} баксов)." if money >= 40:
            $ money -= 40
            scene expression 'images/cg/ep1/night_collector/Night_collector_11.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with my_dissolve
            'Ночная гостья' "Чёртов извращенец."
            '[gg]' "Каков уж есть."
            'Ночная гостья' "Ладно-ладно. Тебе нравятся мои сиськи, мне – твои деньги."
            'Ночная гостья' "Но на большее не рассчитывай, сопляк."
            '[gg]' "Показывай уже!"
            scene expression 'images/cg/ep1/night_collector/Night_collector_12.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with my_dissolve
            'Ночная гостья' "Смотри и запоминай. Ты видишь их в первый и последний раз в жизни."
            '[gg]' "Чёрт, а ты горячая."
            'Ночная гостья' "…"
            '[gg]' "А можно потрогать?"
            'Ночная гостья' "Нет."
            '[gg]' "И за большую сумму?"
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with my_dissolve
            'Ночная гостья' "Всё, заткнись. Представление окончено. Давай бабки."
            $ show_text_animation('-40 money')
            scene expression 'images/cg/ep1/night_collector/Night_collector_8.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with my_dissolve
            '[gg]' "Вот."
            'Ночная гостья' "Оривидэрчи, придурок. Увидимся на следующей неделе."
            '[gg]' "Чего?!"
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with my_dissolve
            'Ночная гостья' "А ты что думал? Я буду навещать тебя каждую неделю, пока ты, наконец, не выплатишь долг."
            '[gg]' "…"
        "!Я дам тебе вдвое больше, если ты покажешь мне сиськи (отдать {i}{b}40{/b}{/i} баксов)." if money <  40:
            $ pass
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_32
    $ add_to_gallery(-5)
    $ Event('night_girl',     'GG_Room',     'night_girl', day_start = time.day_now + 7, time = ['morning'])
    scene black with my_dissolve
    $ renpy.pause(.5, hard = True)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
