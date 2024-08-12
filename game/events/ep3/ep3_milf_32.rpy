label bed_night_milf_34:
    $ location_now = 'GG_Room'
    hide screen main_interface
    '[gg]' "Сейчас некогда отдыхать!"

    $ events.pop('bed_night_milf_34', 0)

    $ events.pop('bed_night_milf_35', 0)
    jump main_interface_label

label bed_night_milf_35:
    $ location_now = 'GG_Room'
    hide screen main_interface
    '[gg]' "Сейчас некогда отдыхать!"

    $ events.pop('bed_night_milf_34', 0)

    $ events.pop('bed_night_milf_35', 0)

    jump main_interface_label
label ep3_milf_32:
    $ events.pop('ep3_milf_32', 0)
    $ location_now = 'Corridor'

    hide screen main_interface

    call show_all_images_label from _call_show_all_images_label_88



    show Milf Invis
    show Milf Invis:
        xalign .85

    show GG Nude_OMG
    show GG Nude_OMG:
        xalign .15
        ypos 1085


    with Dissolve(.5)















    "Марина" "Да?"
    "[gg]" "Можно войти? Я принёс вещи. "
    "Марина" "Ага. "
    scene expression '#000' with Dissolve(.5)
    scene expression 'images/cg/ep3/Milf_Fap_Water/bg.png'
    show expression 'images/cg/ep3/Milf_Fap_Water/milf_1.png'

    show Milf Invis
    show Milf Invis:
        xalign .85
    with Dissolve(.5)
    "Марина" "Пожалуйста, забирай свои штаны и оставь вещи на стиральной машине. "
    "[gg]" "Хорошо."












    scene expression '#000' with Dissolve(.5)



    "[gg]" "Нужно поторопить Игоря. "

    $ add_to_gallery(9)
    if not from_gallery_check():
        $ block_time_forward = True
        $ events.pop('ep3_milf_28', 0)
        $ Event('ep3_milf_33',     'Milf_Room')

        $ descript = _("Поторопить Игоря.")
        $ Event('ep3_milf_30_stump',     'Restroom')

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
