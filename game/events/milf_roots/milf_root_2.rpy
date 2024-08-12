label milf_root_2_tmp:
    "[gg]" "Я не могу развлекаться с Мариной, пока она носит в себе анальную пробку. "
    jump main_interface_label

label milf_root_2:
    $ events.pop('milf_root_2', 0)

    $ Event('milf_root_2_2', 'Corridor')
    jump main_interface_label
label milf_root_2_2:
    $ events.pop('milf_root_2_2', 0)
    $ time.time_now = 'night'
    call show_bg_image_label from _call_show_bg_image_label_103
    call show_additional_images_label from _call_show_additional_images_label_88

    show Milf Night_Embarrassment
    show Milf Night_Embarrassment at go_from_right
    $ renpy.pause(.5, hard = True)
    show GG Embarrassment
    show GG Embarrassment at go_from_left
    $ renpy.pause(.5, hard = True)


    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "Марина" "Где ты пропадал весь день, [gg]?"
    show Milf:
        xalign .85
    show GG:
        xalign .15
    with my_dissolve
    "Марина" "Я… Вся…"

    "Марина" "Я так волновалась за тебя. "
    show GG Passion
    "[gg]" "Ты уже хочешь, да?"

    "Марина" "А ты?.."

    "Марина" "Я уже могу избавиться от этой штучки?"
    show GG Passion
    "[gg]" "Рано."
    show Milf Night_Chagrin
    "Марина" "Рано? "

    "Марина" "Я с трудом сдерживаюсь, чтобы не сорвать с тебя штаны и не высосать у тебя всю сперму из члена, а ты говоришь рано?"
    show GG Passion
    "[gg]" "Да, ты торопишь события."

    "Марина" "Хорошо…"

    "Марина" "Я постараюсь продержаться хотя бы до завтра."
    show GG Passion
    "[gg]" "Нет. Ты должна терпеть ровно столько, сколько нужно."
    show Milf Night_Embarrassment
    "Марина" "Это жестоко…"
    show GG Passion
    "[gg]" "Ну или вытаскивай анальную пробку, но тогда у нас ничего не будет."
    show Milf Night_Chagrin
    "Марина" "Ну всё, хватит!"
    show Milf Night_Chagrin
    "Марина" "Я тебя поняла и буду стараться. "
    show GG Passion
    "[gg]" "Вот и замечательно."
    show Milf Night_Chagrin:
        xzoom -1
        linear 1 xalign 1.5

    $ renpy.pause(1, hard = True)
    $ new_events = True

    $ milf_root_1_text   = _("ПРОДОЛЖАТЬ ждать какое-то время, доведя Марину до экстаза. Чтобы ускорить стимуляцию, мне стоит избегать Марину, и возвращаться домой поздно ночью. ")

    $ Event('milf_root_3', 'City_Home', day_start = time.day_now + 1, time = ['evening', 'night'])

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
