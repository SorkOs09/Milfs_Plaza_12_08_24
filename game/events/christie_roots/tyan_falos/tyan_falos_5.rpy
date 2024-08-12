label tyan_falos_5_debug:
    $ location_now = 'Hall'
    scene black
    show image Text('DEBUG: Переход к ивенту tyan_falos_5'):
        align (.5, .5)
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call wait_click_label from _call_wait_click_label_43

label tyan_falos_5:
    $ events.pop('tyan_falos_5', 0)
#A task: 
    call show_bg_image_label from _call_show_bg_image_label_168
#1. Активировать Кристи Утром или Днём.
    show Christie Normal
    show Christie Normal:
        xalign .85
        ypos 1085
    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left

    "[gg]" "Ну как, у тебя получилось забрать свою линейку?"
    "Кристи" "Ага. Вот она, моя рулеточка. "

    "Кристи" "На, держи. Пользуйся, сколько пожелаешь. "
    show GG:
        xalign .15
    with my_dissolve

    "[gg]" "Благодарю. "
    show GG Smile
    "[gg]" "Ты не пожалеешь, хе-хе-хе."
    "Кристи" "У тебя странная интонация смеха. "
    "Кристи" "Для чего тебе на самом деле понадобилась моя линейка?"
    show GG Smile
    "[gg]" "Для кое-каких мужских дел."
    "Кристи" "Мужских?"
    show GG Smile
    "[gg]" "Да. Строительно-мебельного характера."
    "Кристи" "Ну ладно. Удачи в реализации."
    show GG Smile
    "[gg]" "Хе-хе-хе. Спасибо."
    #//мысль
    show Christie Angry
    with my_dissolve
    "Кристи" "{i}Снова этот дурацкий, ехидный смех.{/i}"

    "Кристи" "{i}Он явно что-то замышляет.{/i}"
     

    $ debug_next('tyan_falos_6_debug')

    $ tyan_falos_text = _("Нужно зайти к Кристи в комнату, когда её там нет, и измерить место на стене, куда она крепит свой фалос.")

    $ Event('tyan_falos_6', 'Sister_Room', button_name = _("Линейка"))
    $ new_events_christie = True
    jump main_interface_label
