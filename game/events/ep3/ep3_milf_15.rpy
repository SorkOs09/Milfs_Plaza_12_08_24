













label ep3_milf_15:

    $ events.pop('ep3_milf_15', 0)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/thinking-music-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    $ Hide('main_interface', transition = Dissolve(.5))()
    call show_all_images_label from _call_show_all_images_label_46
    show GG Normal
    show GG Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    show Milf Street_Normal
    show Milf Street_Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035

    with Dissolve(.5)





    "[gg]" "Ты уходишь? "
    "Марина" "[gg], рад, что ты уже проснулся. Еда в холодильнике, ключ на петельке в шкафу, и не забудь почистить зубы. "
    "[gg]" "Эээээ…"

    "Марина" "Офицер полиции, который привёл тебя в тот вечер, пригласил меня на ужин."
    show GG Skepticism
    "[gg]" "Чего?!!"


    show Milf Street_Chagrin
    "Марина" "Не смотри на меня так. Он приличный человек и так же, как и я, хочет ускорить твоё искупление перед законом."

    show Milf Street_Normal
    "Марина" "Я расскажу ему о твоих позитивных изменениях, а он обещал внести эту информацию в твоё дело."

    show Milf Street_Passion
    "Марина" "Поведаю офицеру, каким ты стал… заботливым."
    show GG Angry
    "[gg]" "Мне это не нравится."

    show Milf Street_Angry
    "Марина" "А мне не нравится, что я вынуждена общаться с полицейским о твоих проблемах с законом."

    show GG Chagrin
    "[gg]" "Ладно-ладно. Ты права."

    show Milf Street_Normal
    "Марина" "Я скоро вернусь."











    hide Milf
    with Dissolve(.5)
    show GG Think
    with Dissolve(.5)

    "[gg]" "Отлично. Мой план всё ближе к реализации. Осталось только узнать, дома ли Кристи и дело в шляпе."
    $ ep3_milf_16 = True
    $ block_time_forward = True
    $ descript    = _('Проверить все комнаты, убедившись, что дома никого нет.')

    $ block_milf_home   = True
    $ block_sister_home = True
    $ block_exit_home   = True

    $ milf_15_audio     = True

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/sneaky-adventure-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    $ Event('ep3_milf_16_1', 'Sister_Room', 'ep3_milf_16_1')
    $ Event('ep3_milf_16_2', 'Restroom', 'ep3_milf_16_2')
    $ Event('ep3_milf_16_3', 'Kitchen', 'ep3_milf_16_3')
    $ Event('ep3_milf_16_4', 'Hall', 'ep3_milf_16_4')
    $ Event('ep3_milf_16_5', 'Milf_Room', 'ep3_milf_16_5')
    $ events.pop('ep2_14_milf_restroom', 0)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
