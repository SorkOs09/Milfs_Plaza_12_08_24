

label ep4_milf_44:
    $ events.pop('ep4_milf_44', 0)

    call show_bg_image_label from _call_show_bg_image_label_121
    call show_additional_images_label from _call_show_additional_images_label_100


    show Milf Normal
    show Milf Night_Normal:
        xalign .85
        ypos 1085





    with Dissolve(.5)

    show GG Smile
    show GG Smile at go_from_left

    $ renpy.pause(1, hard = True)
    "[gg]" "Я тут в поисках самой роскошной женщины для похода в ресторан…"

    show Milf Night_Smile
    "Марина" "И как ваши успехи, сэр?"
    show GG Smile:
        xalign .15
    with my_dissolve
    "[gg]" "Грандиозные. Я обнаружил вас!"
    show Milf Night_Smile
    "Марина" "Чудненько. Только дай минутку, я переоденусь. "

    show Milf Night_Smile:
        xzoom -1
        linear .75 xalign 1.5
        ypos 1085


    $ renpy.pause(.75, hard = True)
    hide Milf
    show GG Think
    with my_dissolve
    "[gg]" "Я достаточно ждал… Пора действовать."




    $ descript = _("Заглянуть в комнату Марины.")
    $ block_time_forward = True
    $ block_exit_home    = True
    $ milf_position['evening'] = ['None', 'milf_evening_hall']




    $ Event('ep4_milf_45', 'Milf_Room', time = ['morning', 'afternoon','evening'],)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
