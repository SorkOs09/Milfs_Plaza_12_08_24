
label milf_root_3:
    $ events.pop('milf_root_3', 0)

    $ Event('milf_root_3_2', 'Corridor')
    jump main_interface_label
label milf_root_3_2:
    $ events.pop('milf_root_3_2', 0)
    $ time.time_now = 'night'
    call show_bg_image_label from _call_show_bg_image_label_115
    call show_additional_images_label from _call_show_additional_images_label_95
    with Dissolve(.5)
    show GG Embarrassment
    show GG Embarrassment at go_from_left
    $ renpy.pause(.5, hard = True)
    show Milf Night_Extaz
    show Milf Night_Extaz:

        xalign 1.5 ypos 1200

    $ renpy.pause(.7, hard = True)
    show Milf Night_Extaz:

        linear .5 xalign 1.2 ypos 1085



    $ renpy.pause(.7, hard = True)
    show Milf Night_Extaz:

        linear .5 xalign .99 ypos 1200

    $ renpy.pause(.7, hard = True)
    show Milf Night_Extaz:

        linear .5 ypos 1085 xalign .85


    $ renpy.pause(.7, hard = True)


    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    show Milf:
        ypos 1085 xalign .85
    show GG:
        xalign .15
    with my_dissolve
    "Марина" "Это невыносимо, [gg]!"
    show Milf Night_Extaz
    "Марина" "Моя дырочка, в которую я вставила анальную пробку, готова на любые истязания, только бы вынуть её и почувствовать ласки твоего члена."
    show GG Passion
    "[gg]" "Чёрт, ты выглядишь как умалишённая."
    show Milf Night_Extaz
    "Марина" "Твоя анальная пробка вышибает мне остаток мозга, [gg]. "
    show Milf Night_Extaz
    "Марина" "Я не могу ни о чём думать, кроме как сексе с тобой."
    show Milf Night_Extaz
    "Марина" "О грязном, животном сексе в мою разгоревшуюся от нетерпения задницу. "
    show GG Passion
    "[gg]" "Потерпи ещё немножечко."
    show Milf Night_Extaz
    "Марина" "Нет, нет, нет!"
    show Milf Night_Extaz
    "Марина" "Пожалуйста, не оставляй меня в таком виде."
    show Milf Night_Extaz
    "Марина" "Я не выдержу!"
    show GG Passion
    "[gg]" "Тебе незачем терпеть, ты всегда можешь прекратить свои мучения и игре конец."
    show Milf Night_Extaz
    "Марина" "Но ведь тогда ты не захочешь меня ласкать."
    show GG Passion
    "[gg]" "Тогда сделай правильный выбор."
    show Milf Night_Extaz
    "Марина" "Ну лааааааааааадно."

    show Milf Night_Extaz:
        xzoom -1
    with Dissolve(.5)
    show Milf Night_Extaz:
        xzoom -1

        linear .5 xalign .99 ypos 1200
    $ renpy.pause(.7, hard = True)

    show Milf Night_Extaz:

        linear .5 xalign 1.2 ypos 1085
    $ renpy.pause(.7, hard = True)
    show Milf Night_Extaz:

        linear .5 xalign 1.5 ypos 1200
    $ renpy.pause(.7, hard = True)
    $ stnd_music_play()
    hide Milf
    show GG Think
    with my_dissolve
    "[gg]" "Марина уже на грани, ещё чуточку, и можно брать её горяченькой. "

    $ milf_root_1_text = _("Марина уже на грани. Пожалуй, мне стоит ещё раз прогуляться и вернуться домой поздно ночью, прежде чем я позволю ей вынуть анальную пробку. ")

    $ new_events = True


    $ Event('milf_root_4', 'City_Home', day_start = time.day_now + 1)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
