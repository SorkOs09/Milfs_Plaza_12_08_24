label ep2_18_end:
    call show_bg_image_label from _call_show_bg_image_label_54
    call show_additional_images_label from _call_show_additional_images_label_48

    with Dissolve(.5)
    show Milf Night_Angry
    show Milf Night_Angry:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    show GG Surprise
    show GG Surprise at go_from_left
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    $ from_say_screen = False
    $ renpy.pause(1)

    'Марина' "Ну и где ты шлялся?"
    show GG Embarrassment:
        xalign .15
    '[gg]' "Эй-эй, не дави на меня так. "
    '[gg]' "Просто гулял."
    show Milf Night_Angry
    'Марина' "Ты понимаешь, что если ты опять куда-то вляпаешься, то мы уже ничего не сможем сделать. Тебя посадят!"
    show GG Angry
    '[gg]' "Послушай, Марина, если ты хочешь, чтобы я говорил тебе правду, ты должна научиться доверять мне!"
    show Milf Night_Chagrin
    'Марина' "Это сложно делать, когда твой друг постоянно замешан в мутных историях."
    show GG Normal
    '[gg]' "Я просто гулял. Верь мне. "
    show Milf Night_Normal
    'Марина' "И ты ни в чём больше не замешан? "
    show GG Normal
    '[gg]' "Нет. "
    show Milf Night_Normal
    'Марина' " …."
    show Milf Night_Chagrin
    'Марина' "Хорошо, я поверю тебе."
    show Milf Night_Normal
    'Марина' "Но в последний раз."
    show GG Embarrassment
    '[gg]' "Спасибо."
    show Milf Night_Normal
    'Марина' "Спокойной ночи."


    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/night.mp3', fadein = 1.5)


    hide Milf
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show GG Embarrassment:
        linear 1 xalign .5
    $ renpy.pause(1, hard = True)
    '[gg]' "Да, я снова наврал ей. Но разве у меня был выбор?"
    show GG WTF
    '[gg]' "Мне что, следовало ей рассказать, что я задолжал кучу денег бандитам? Что в любой день меня могут прирезать за неуплаченный процент? Или что я ходил за пистолетом для самозащиты? "
    '[gg]' "…"
    show GG Chagrin:
        xalign .5
    '[gg]' "Каждый мой день может стать последним."
    '[gg]' "И если мне суждено погибнуть в перестрелке, то остаток своей жизни я хочу с человеком, которого люблю больше всего на свете…"
    '[gg]' "Мариной."
    '[gg]' "Надо будет купить её любимое красное вино и подобрать подходящий фильм для просмотра в романтической обсстановке.\nДиск с подходящим фильмом можно найти в зале."


    if love_milf >= 3:

        $ descript = _("Лучшее, что я сейчас могу сделать, это провести свой последний вечер с единственным человеком, которому я неравнодушен: следует купить красное вино и подобрать подходящий фильм.\nДиск с подходящим фильмом можно найти в зале.")
        $ locations['Hall'].buttons[0]['tumba_under_tv'] = ((1470, 725, 135, 180),   Jump('hall_tumba_under_tv_lolita_label_ep3_1'))


        $ Event('ep3_1_start', 'Hall_Milf', time = ['evening'])

    elif True:

        $ descript = _('Требование: Привязанность Марины (3)')

        $ milf_love_quests = 3

    $ events.pop('ep2_18_end', 0)


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
