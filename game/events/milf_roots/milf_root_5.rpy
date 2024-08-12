
label milf_root_5:
    $ events.pop('milf_root_5', 0)
    $ time.time_now = 'night'
    call show_bg_image_label from _call_show_bg_image_label_113
    call show_additional_images_label from _call_show_additional_images_label_93
    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_left
    $ renpy.pause(.5, hard = True)
    show GG Think
    "[gg]" "Странно, сегодня меня никто не встречает. "
    show GG Think:
        xalign .15
    with my_dissolve
    "[gg]" "Кажется я перегнул палку."

    show GG Think
    "[gg]" "Зайду к Марине в спальню и проверю её."

    $ milf_root_1_text = _('Зайти к Марине в спальню.')
    $ new_events = True

    $ Event('milf_root_6', 'Milf_Room')
    $ block_exit_home    = True
    $ block_time_forward = True
    $ block_milf_home    = True
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
