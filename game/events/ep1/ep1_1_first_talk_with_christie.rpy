label ep1_1_first_talk_with_christie:

    call show_bg_image_label from _call_show_bg_image_label_67


    show Christie Normal
    show Christie Normal:
        xalign .1
        ypos 1085
        xzoom -1
        zoom 1.0-0.035
    with Dissolve(.3)

    show GG Normal
    show GG Normal at go_from_right(xxzoom = -1)

    '[gg]' "О, Кристи! Привет."
    
    show GG Surprise: 
        xalign .85
    with my_dissolve
    '[gg]' "Ты почему ещё не спишь?"
    #'Кристи' "Я только вернулась. "
    'Кристи' "Слышала, у тебя крупные неприятности."
    show GG Embarrassment
    '[gg]' "Ну…"
    show GG Normal
    'Кристи' "Сочувствую."
    show GG Chagrin
    '[gg]' "Хоть кому-то я не безразличен."
    "Кристи" "Ха!"

    "Кристи" "После того как тебя вышвырнули из колледжа на третьем курсе, я уже ничему не удивлена. "

    show GG Laughs
    "[gg]" "В 18 лет все совершают ошибки."

    "Кристи" "Тебе уже 20, и ты совершил их куда больше, чем многие за 100 лет!"

    show GG WTF
    with my_dissolve
    "Кристи" "Рано или поздно тебя обнаружат в какой-нибудь канаве, это точно…"

    "Кристи" "Я бы не желала тебе такого исхода."

    show GG Chagrin
    with my_dissolve
    "[gg]" "Всего-лишь временные трудности. Не волнуйся за меня."

    show Christie Laughs
    with my_dissolve
    "Кристи" "А я и не волнуюсь, чудак. "

    "Кристи" "Ты главное не забудь адрес исправительного учреждения указать."

    show GG Angry
    with my_dissolve
    "[gg]" "Эй! Я думал ты на моей стороне!"

    show Christie Passion
    with my_dissolve
    "Кристи" "Только если это не грозит мне последствиями, хи-хи-хи!"

    show Christie Normal
    with my_dissolve
    "Кристи" "Марина совсем не в духе. "

    show GG Please
    with my_dissolve
    "[gg]" "Нашла кому рассказывать…"

    show Christie Angry
    with my_dissolve
    "Кристи" "Мне, как ты знаешь, очень повезло, что она приютила меня после гибели моих родителей."

    "[gg]" "Понимаю."

    "Кристи" "Поэтому ты уж постарайся, [gg], чтобы твои проблемы никак не отразились ни на мне, ни на Марине."

    "[gg]" "Попробую…"

    "Кристи" "…"

    "Кристи" "Тебе трудно верить, [gg]. Я бы даже сказала – невозможно. "

    "Кристи" "Но именно поэтому ты и один. "

    "[gg]" "Ты знаешь как поддержать в трудную минуту."

    "Кристи" "Подумай об этом на досуге, [gg], подумай."

    "[gg]" "Спокойной ночи…"

    "Кристи" "Ага. И постарайся не умереть."



    $ events.pop('ep1_1_first_talk_with_christie', 0)
    $ Event('ep1_2_morning',  'GG_Room', time = ['morning'])

    $ block_time_forward = False
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
