image gg_gipno_jerk:
    'characters/GG/emo/Dick 1.png' with Dissolve(.2)
    .5
    'characters/GG/emo/Dick 2.png' with Dissolve(.2)

    .5
    'characters/GG/emo/Dick 1.png' with Dissolve(.2)
    .5
    'characters/GG/emo/Dick 2.png' with Dissolve(.2)

    .5
    'characters/GG/emo/Dick 1.png' with Dissolve(.2)
    .5
    'characters/GG/emo/Dick 2.png' with Dissolve(.2)

    1
    repeat
label milf_magic_label:
    call show_bg_image_label from _call_show_bg_image_label_85
    call show_additional_images_label from _call_show_additional_images_label_71
    with Dissolve(.5)
    show GG Clock
    show GG Clock:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    if time.time_now == 'evening':
        show Milf Night_Normal
        show Milf Night_Normal:
            xalign .85
            ypos 1085
            zoom 1.0-0.035
    elif True:

        show Milf Normal
        show Milf Normal:
            xalign .85
            ypos 1085
            zoom 1.0-0.035


    with Dissolve(.5)

    '[gg]' "Подруга, я хочу тебе кое-что показать."
    'Марина' "Откуда у тебя эти часы?"
    '[gg]' "Присмотрись внимательней. Они тебе знакомы?"
    'Марина' "Не вижу ничего необычного…"
    '[gg]' "Обрати внимание на их размеренное покачивание…"
    'Марина' "Да… Размеренное… "
    if time.time_now == 'evening':
        show Milf Night_Gipno
    elif True:
        show Milf Gipno
    '[gg]' "Ты полностью под моим контролем…"
    show shadow_full
    with my_dissolve
    'Марина' "{i}Ха, кажется [gg] надеется меня загипнотизировать.{/i}"
    'Марина' "{i}Как это наивно с его стороны, учитывая, что он и сам не особо верит в эту чепуху.{/i}"
    'Марина' "{i}Но, видимо, ему хочется ощутить себя в роли властителя...{/i}"
    'Марина' "{i}Что ж, почему бы и нет. Я с радостью подыграю ему.{/i}"
    hide shadow_full
    with my_dissolve

    'Марина' "Да, я полностью под твоим контролем…"
label milf_magic_label_menu:
    show GG Normal
    show GG Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    if time.time_now == 'evening':
        show Milf Night_Normal
        show Milf Night_Normal:
            xalign .85
            ypos 1085
            zoom 1.0-0.035
    elif True:

        show Milf Normal
        show Milf Normal:
            xalign .85
            ypos 1085
            zoom 1.0-0.035


    with Dissolve(.5)
    menu:
        "1. «Ты хочешь показать мне свою грудь.»" if True:
            jump milf_magic_label_boobs
        "2. «Ты хочешь показать мне свою киску.»" if True:
            jump milf_magic_label_pussy
        "3. Прекратить магию." if True:
            $ add_to_gallery(-1)
            jump main_interface_label

label milf_magic_label_boobs:
    'Марина' "Я хочу показать тебе свою грудь…"
    if time.time_now == 'evening':
        show Milf Night_Titis
    elif True:
        show Milf Titis
    with Dissolve(.5)
    'Марина' "Вот, гляди… "
    '[gg]' "О да, твои сиськи просто супер."
    'Марина' "…."


    jump milf_magic_label_jerk_menu
label milf_magic_label_jerk_menu:
    menu:
        "Подрочить." if True:
            $ pass
        "Другие приказы." if True:
            jump milf_magic_label_menu

label milf_magic_label_boobs_jerk:
    hide GG
    show gg_gipno_jerk
    show gg_gipno_jerk:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    '[gg]' "Обожаю смотреть на твою сексуальную беспомощность. "
    '[gg]' "Твой безразличный взгляд словно говорит мне: «Мне плевать. Трахни меня куда хочешь!»"
    '[gg]' "Я сделаю это, обязательно."
    '[gg]' "Как только придёт время."
    menu:
        "Продолжать смотреть." if True:
            jump milf_magic_label_boobs_jerk
        "Кончить." if True:
            $ pass

    hide gg_gipno_jerk
    show GG Dick_3
    show GG Dick_3:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    show expression 'characters/GG/Sperm/Sperm 1.png'
    show expression 'characters/GG/Sperm/Sperm 1.png':
        ypos 1080
        xpos 1100
    with Dissolve(.1)
    $ renpy.pause(.1, hard = True)
    hide expression 'characters/GG/Sperm/Sperm 1.png'
    show expression 'characters/GG/Sperm/Sperm 2.png'
    show expression 'characters/GG/Sperm/Sperm 2.png':
        ypos 1080
        xpos 1100
    with Dissolve(.1)
    $ renpy.pause(.1, hard = True)
    hide expression 'characters/GG/Sperm/Sperm 2.png'
    show expression 'characters/GG/Sperm/Sperm 3.png'
    show expression 'characters/GG/Sperm/Sperm 3.png':
        ypos 1080
        xpos 1100
    with Dissolve(.1)
    $ renpy.pause(.1, hard = True)
    hide expression 'characters/GG/Sperm/Sperm 3.png'
    show expression 'characters/GG/Sperm/Sperm 4.png'
    show expression 'characters/GG/Sperm/Sperm 4.png':
        ypos 1080
        xpos 1100
    with Dissolve(.1)
    $ renpy.pause(.1, hard = True)
    hide expression 'characters/GG/Sperm/Sperm 4.png'
    show expression 'characters/GG/Sperm/Sperm 5.png'
    show expression 'characters/GG/Sperm/Sperm 5.png':
        ypos 1080
        xpos 1100
    with Dissolve(.1)
    $ renpy.pause(.1, hard = True)

    '[gg]' "Вот так!"
    '[gg]' "Просто великолепно. "

    hide expression 'characters/GG/Sperm/Sperm 5.png'
    hide GG Dick_3
    jump milf_magic_label_menu

label milf_magic_label_pussy:

    'Марина' "Я хочу показать тебе свою киску…"
    if time.time_now == 'evening':
        show Milf Night_Pussy
    elif True:
        show Milf Pussy

    with Dissolve(.5)
    'Марина' "Вот, гляди… "
    '[gg]' "Великолепно! "
    'Марина' "…."
    jump milf_magic_label_jerk_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
