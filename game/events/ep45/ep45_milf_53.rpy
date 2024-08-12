label ep45_milf_53:
    $ Hide('main_interface')()
    call show_bg_image_label from _call_show_bg_image_label_9
    call show_additional_images_label from _call_show_additional_images_label_6
    show GG Normal
    show GG Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035

    show Milf Normal
    show Milf Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)





















    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    show Milf Normal
    "Марина" "В последнее время ты такой занятой."
    show Milf Normal
    "Марина" "Может, останешься сегодня дома?"
    show GG Passion
    "[gg]" "Заманчивое предложение."
    show Milf Passion
    "Марина" "Мы сделаем этот день незабываемым. "


    show Milf Passion
    "Марина" "Обещаю."
    show GG Laughs
    "[gg]" "Ты ставишь меня в затруднительное положение."
    show GG Normal
    "[gg]" "Если можно, я подумаю."
    show Milf Passion
    "Марина" "Каждая секунда на счету, малыш. "
    show GG Embarrassment
    "[gg]" "Интриганка…"
    hide Milf with Dissolve(.5)

    show GG Think



    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)




    "[gg]" "Марина предложила мне прогулять уборку и провести это время с ней."
    "[gg]" "Если я соглашусь, последствия могут быть самыми плачевными."
    "[gg]" "Офицер полиции ищет любую причину, чтобы придраться ко мне."
    "[gg]" "Лучше не рисковать..."

    $ block_change_milf_position = True
    $ milf_position['evening']   = ['Hall', 'milf_evening_hall']
    $ milf_position['morning']   = ['Kitchen',   'milf_kitchen']
    $ milf_position['afternoon'] = ['Kitchen',   'milf_kitchen']

    $ events.pop('ep45_milf_park', 0)

    $ Event('ep45_milf_52_skip', None, 'ep45_milf_52_skip', time = ['evening', 'night'])

    $ Event('ep45_milf_54_city_home', 'City_Home', 'ep45_milf_54_city_home', time = ['morning', 'afternoon'])

    $ Event('ep45_milf_54_hall', 'Milf', 'ep45_milf_54_hall', time = ['morning', 'afternoon'])
    $ descript = _("Марина предложила мне прогулять уборку и провести это время с ней.")

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
