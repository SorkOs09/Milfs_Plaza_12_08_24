label ep5_milf_73_stump:
    $ location_now = 'Corridor'
    call show_all_images_label from _call_show_all_images_label_44
    "[gg]" "Прежде я должен переодеться. "

    $ Event('ep5_milf_73_stump_1', 'Hall', 'ep5_milf_73_stump')
    $ Event('ep5_milf_73_stump_2', 'Restroom', 'ep5_milf_73_stump')
    $ Event('ep5_milf_73_stump_3', 'Kitchen', 'ep5_milf_73_stump')
    $ Event('ep5_milf_73_stump_4', 'Sister_Room', 'ep5_milf_73_stump')
    jump main_interface_label

label ep5_milf_73:
























    $ locations['GG_Room'].image_buttons.pop('pants_ep5_milf_72', 0)
    $ events.pop('ep5_milf_73_stump_1', 0)
    $ events.pop('ep5_milf_73_stump_2', 0)
    $ events.pop('ep5_milf_73_stump_3', 0)
    $ events.pop('ep5_milf_73_stump_4', 0)
    $ events.pop('ep5_milf_73_stump_5', 0)
    $ Event('ep5_milf_74', 'Hall')
    menu:
        "Переодеться." if True:

            $ pass
    scene black
    $ remove_from_inventory('Костюм 1')
    $ remove_from_inventory('Костюм 2')

    with Dissolve(.5)
    call show_all_images_label from _call_show_all_images_label_45
    show GG Think
    with my_dissolve
    "[gg]" "Готово."
    show GG Think
    "[gg]" "Так я чувствую себя намного лучше."

    $ descript = _('Проверить Марину у себя в спальне.')

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
