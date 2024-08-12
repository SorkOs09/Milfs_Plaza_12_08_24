
label ep5_milf_67:
    $ events.pop('ep5_milf_67', 0)
    $ remove_from_inventory('Слабительное')
    call show_bg_image_label from _call_show_bg_image_label_59
    call show_additional_images_label from _call_show_additional_images_label_53
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

    show GG Normal
    show GG Normal at go_from_left
    $ renpy.pause(.5)

    "Марина" "Да, мой хороший? "
    show GG Normal:
        xalign .15
    with my_dissolve
    "[gg]" "Вот, возьми это. "
    if time.time_now == 'evening':
        show Milf Night_Surprise
    elif True:

        show Milf Surprise
    "Марина" "Слабительное? "

    if time.time_now == 'evening':
        show Milf Night_Angry
    elif True:

        show Milf Angry
    "Марина" "Что за намёки?!"
    show GG Laughs
    "[gg]" "Дурочка, это не тебе, а для офицера полиции."

    if time.time_now == 'evening':
        show Milf Night_Normal
    elif True:

        show Milf Normal

    show GG Smile
    "[gg]" "Подсыпь ему слабительное в чай или вино, пусть отсидится в туалете. "

    "Марина" "Но зачем?"
    show GG Normal
    "[gg]" "Для надёжности, разумеется."
    show GG Normal
    "[gg]" "Во-первых, у него быстро пропадёт всякое желание к тебе приставать."
    show GG Normal
    "[gg]" "А во вторых, если явится брат, полицейский будет находится в относительной безопасности."

    "Марина" "А это не опасно? Я не отравлю его?"
    show GG Skepticism
    "[gg]" "Чёрт возьми, женщина, просто почитай инструкцию. "

    if time.time_now == 'evening':
        show Milf Night_Chagrin
    elif True:
        show Milf Chagrin


    "Марина" "Извини, я сильно волнуюсь. "

    "Марина" "Мало ли что может случится."
    show GG Normal
    "[gg]" "Что-то обязательно случится, в этом и заключается смысл наших слаженных действий, но ты же сама рвалась на помощь, не правда ли?"
    if time.time_now == 'evening':
        show Milf Night_Normal
    elif True:

        show Milf Normal

    "Марина" "Да, ты прав, любимый."

    "Марина" "Я сделаю всё необходимое."

    if time.time_now == 'evening':
        show Milf Night_Smile
    elif True:
        show Milf Smile

    "Марина" "Если скажешь, я ему яд подсыплю!"
    show GG Surprise
    "[gg]" "Эй, спокойно. Мы «Бони и Клайд», а не Майкл Дуглас и Шэрон Стоун из «Основного инстинкта». "

    if time.time_now == 'evening':
        show Milf Night_Passion
    elif True:
        show Milf Passion

    "Марина" "Как знать, хи-хи-хи."
    show GG Smile
    "[gg]" "Роковая женщина."

    "Марина" "Значит тебе повезло."
    show GG Normal
    "[gg]" "Ладно, шутки в сторону."
    show GG Normal
    "[gg]" "Скоро я уточню, когда именно следует пригласить офицера на ужин."
    if time.time_now == 'evening':
        show Milf Night_Normal
    elif True:

        show Milf Normal

    "Марина" "Жду ваших распоряжений, милорд. "

    if time.time_now == 'evening':
        show Milf Night_Smile
    elif True:
        show Milf Smile

    "Марина" "Хи-хи-хи."
    show GG Normal
    "[gg]" "…."
    $ time.time_now = 'evening'

    $ descript = _('Как только я буду готов вызволить Игоря, следует поговорить с Мариной Утром или Днём.')
    $ Event('ep5_milf_68', 'Milf', time = ['morning', 'afternoon'])
    $ block_change_milf_position = True

    $ milf_position = {
        'morning'   : ['Kitchen',  'milf_kitchen'],
        'afternoon' : ['Corridor',  'milf_corridor'],
        'evening'   : ['Hall',      'milf_evening_hall'],
        'night'     : ['Milf_Room', 'milf_room'],
        
        }
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
