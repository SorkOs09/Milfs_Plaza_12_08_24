label ep4_milf_38:

    $ events.pop('hall_mother_5', 0)

    $ events.pop('ep4_milf_38', 0)

    $ events.pop('ep4_milf_38_2', 0)
    call show_bg_image_label from _call_show_bg_image_label_39
    call show_additional_images_label from _call_show_additional_images_label_33

    $ Hide('main_interface')()

    if time.time_now not in ['night', 'evening']:

        show Milf Normal
        show Milf Normal:
            xalign .85
            ypos 1085

    elif True:

        show Milf Night_Normal
        show Milf Night_Normal:
            xalign .85
            ypos 1085


    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left
    $ renpy.pause(1, hard = True)
    "[gg]" "Марина, у меня для тебя сюрприз. "

    if time.time_now not in ['night', 'evening']:


        show Milf Embarrassment
    elif True:
        show Milf Night_Embarrassment
    show GG:
        xalign .15
    with my_dissolve

    "Марина" "Как мило с твоей стороны. Но я сейчас совсем не в том настроении, чтобы радоваться жизни…"

    "[gg]" "Что-то случилось? "

    "Марина" "К сожалению, случилось."
    "[gg]" "Это касается нас с тобой?"
    "Марина" "Да…"
    "[gg]" "Ну чего же ты тянешь? Говори, как есть."
    show GG Chagrin

    if time.time_now not in ['night', 'evening']:
        show Milf Chagrin
    elif True:
        show Milf Night_Chagrin

    "Марина" "Мы можем обсудить это позже? К примеру, в твоей комнате в первой половине дня."

    "[gg]" "Конечно. Я буду ждать."

    if time.time_now not in ['night', 'evening']:
        show Milf Normal
    elif True:
        show Milf Night_Normal


    "Марина" "Спасибо."















    $ descript = _('Дождаться Марину днём в своей комнате.')

    $ Event('ep4_milf_39', 'GG_Room', time = ['afternoon', 'evening'])
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
