label milf_root_11:





    call show_bg_image_label from _call_show_bg_image_label_155
    with my_dissolve
    show GG Normal
    show GG Normal at go_from_left
    if time.time_now == 'evening':
        show Milf Night_Normal
    elif True:
        show Milf Normal
    show Milf at go_from_right
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Всё, Маришка, можешь не полноваться, я купил тебе газовый балончик. "
    show GG:
        xalign .15
    show Milf:
        xalign .85
    with my_dissolve
    "Марина" "Спасибо, милый."

    "Марина" "Но ты уверен, что он защитит меня от вооружённого полицейского?"
    show GG Smile
    "[gg]" "По крайней мере, он придаст тебе некоторой уверенности. "
    if time.time_now == 'evening':
        show Milf Night_Embarrassment
    else:
        show Milf Embarrassment
    with my_dissolve
    "Марина" "Хм… И правда. Ещё раз спасибо"
    show GG Normal
    "[gg]" "Сидеть сложа руки мы тоже не можем. Я предлагаю действовать. "
    if time.time_now == 'evening':
        show Milf Night_Normal
    else:
        show Milf Normal
    with my_dissolve
    "Марина" "Я вся во внимании. "
    show GG Skepticism
    "[gg]" "Он довольно высокомерный и напористый. Упивается властью. Мы можем воспользоваться его наглостью и запечатлеть момент, как он шантажирует или угрожает мне. "
    if time.time_now != 'evening':
        show Milf Laughs
    "Марина" "Гениально! Давай!"
    show GG GivePhone
    "[gg]" "Когда он придёт снова, я включу запись звука, а ты, когда он захочет поговорить со мной тэт-а-тэт, попробуй снять нас на камеру из-за угла, хорошо?"
    if time.time_now == 'evening':
        show Milf Night_Smile
    else:
        show Milf Smile

    with my_dissolve
    "Марина" "Конечно-конечно! Ты просто супер, [gg]! "
    show GG Passion
    "[gg]" "Рано радоваться, но попробовать можно. "
    if time.time_now == 'evening':
        show Milf Night_Normal
    elif True:
        show Milf Normal

    "Марина" "Ага."
    $ Event('milf_root_12', location = "Corridor", day_start = time.day_now+2, time = ['evening'])
    $ milf_root_9_text= _("Прождать 2-3 дня, прежде чем полицейский снова явится в гости. Приходит он в основном вечером.")
    $ new_events = True
    $ events.pop('milf_root_11', 0)
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
