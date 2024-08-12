label ep45_milf_57:

    $ events.pop('ep45_milf_57', 0)
    $ location_now = 'City_Shop'
    call show_bg_image_label from _call_show_bg_image_label_35




    show Jay Normal
    show Jay Normal:
        xalign .35
        ypos 1085
        zoom 1.0-0.035
        xalign .65
    show Bob Normal
    show Bob Normal:
        xalign .65
        ypos 1085
        zoom 1.0-0.035
        xalign .95

    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left(xxalign = .1)

    $ renpy.pause(.5, hard = True)
    "Бубнило" "Ёу, чувак, рады тебя снова видеть! "
    show Jay Normal
    show GG:
        xalign .1
    with my_dissolve
    "Бубнило" "Хочешь поучаствовать в нашем новом пранке?"
    show GG Angry
    "[gg]" "Не сегодня."
    show GG Normal
    "[gg]" "Мне нужно купить горшок."
    show Jay Normal
    "Бубнило" "…."
    show Jay Normal
    "Бубнило" "Горшок?"
    show GG Laughs
    "[gg]" "Горшок."
    show Jay Normal
    "Бубнило" "Бубнило, ты это слышал? Поверить не могу! "
    show Jay Normal
    "Бубнило" "Наш малыш уже подрос и может самостоятельно справлять нужду на горшке. "



    "Бубнило" "Нужно помочь, а то глядишь, обосрётся прям здесь!"

    show GG Angry
    "Бубнило" "Гы-гы-гы!!"
    "[gg]" "Идиоты. "
    show GG Normal
    "[gg]" "Мне нужен горшок для домашнего растения. "
    show GG Normal
    "[gg]" "В магазине его нет, а я понятия не имею, где его можно купить."
    show Jay Normal
    "Бубнило" "О, ну так ты по адресу."
    show Jay Normal
    "Бубнило" "Бубнило и я самые охуеные гончары в этом городе. "
    show Jay Normal
    "Бубнило" "Вазы, горшки, столовая посуда, всё, бля, только для тебя, малыш! "
    show GG Normal
    "[gg]" "А если серьёзно?"
    show Jay Normal
    "Бубнило" "А если серьёзно, то ты самые чокнутый чувак, которого мне приходилось знать."
    show Jay Normal
    "Бубнило" "Ты натуральный извращуга. "
    show Jay Normal
    "Бубнило" "Спектр твоих интересов поражает моё скромное воображение"
    show Jay Normal
    "Бубнило" "Что дальше? Синхрофразатрон? "
    show Jay Normal
    "Бубнило" "Мы обычные барыги, если ты не заметил."
    show GG Think
    "[gg]" "Но билеты-то вы достали. "
    show Jay Normal
    "Бубнило" "Чёрт, это верно."
    show Jay Normal
    "Бубнило" "…."
    show Jay Normal
    "Бубнило" "А знаешь, ты прав."
    show Jay Normal
    "Бубнило" "Мы можем достать любую херню, главное бабки на базу. "
    show GG Normal
    "[gg]" "Цена вопроса? "
    show Jay Normal
    "Бубнило" "Трусики твоей соседки. "
    show GG Chagrin
    "[gg]" "Кристи?"
    show Jay Normal
    "Бубнило" "Ага. Она клёвая."
    show Jay Normal
    "Бубнило" "Только трусики, как ты понимаешь, должны быть использованными. "
    show GG Skepticism
    "[gg]" "И ты ещё называешь меня извращенцем?!"
    show Jay Normal
    "Бубнило" "Мы эстеты, чувак. "
    show Jay Normal
    "Бубнило" "К тому же, сейчас на женские использованные трусики большой спрос. "
    show Jay Normal
    "Бубнило" "И если тебя, как я понял, заводят горшки, то других наших клиентов интересует куда более приземлённые вещи. К примеру: нижнее бельё."
    show GG Angry
    "[gg]" "Мне горшок для растения нужен, а не чтобы свой член туда пихать."

    "Бубнило" "Да нам плевать, чувак."

    "Бубнило" "Мы люди прогрессивные и никого не осуждаем."

    "Бубнило" "Так что, принесёшь? А мы пока поищем тебе твой сосуд для растения. "
    show GG Normal
    "[gg]" "По рукам."

    $ descript =  _("Украсть у Кристи трусики, пока она принимает ванну и обменять их на горшок у Зудилы и Бубнилы.")
    $ events.pop('ep45_milf_57', 0)

    $ Event('ep45_milf_58', 'Restroom', time = ['afternoon'])

    $ block_change_milf_position = True

    $ milf_position['afternoon']   = ['Kitchen', 'milf_kitchen']
    $ sister_position['afternoon'] = ['Restroom', 'sister_restroom']

    scene black with Dissolve(.5)
    $ renpy.pause(1)
    $ time.time_now = 'evening'
    $ events.pop('ep45_milf_52_skip', 0)

    $ location_now  = 'City_Shop'
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
