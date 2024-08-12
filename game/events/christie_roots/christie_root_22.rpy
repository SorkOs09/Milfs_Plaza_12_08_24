label christie_root_22:











    $ events.pop('christie_root_22', 0)

    call show_all_images_label from _call_show_all_images_label

    with my_dissolve











    "Какие-то звуки" "О даааааа!!..."
    "Какие-то звуки" "Уффффф-уфффф!!!...."
    "Какие-то звуки" "Ахххх Ахххххх…. Няяяяя!!"
    "Какие-то звуки" "О-о-о-о-о-о…!!!"

    show GG Surprise
    show GG Surprise at go_from_right(xxzoom = -1)


    "[gg]" "Снова эти стоны, а единственное, что я могу сделать, это кусать себе локти от бессилия. "

    "[gg]" "Надо взломать эту чёртову дверь, и только один человек знает, как это сделать."
    show GG Think: 
        xalign .85
    with my_vpunch
    "[gg]" "Игорь!"
    $ block_time_forward = False

    if 'christie_root_22' in allowed_events:
        $ allowed_events.remove("christie_root_22")


    $ Event('christie_root_23_block', 'Sister_Room', time = 'night')

    $ Event('christie_root_23', 'Igor', button_name = _('Замок на двери'))

    $ descript_Christie = _("Сначала поговорить с Игорем, а после отправиться в библиотеку и продолжить написание реферата по теме «Обществознание».")
    
    if getattr(store, 'block_igor_position', False):

        $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")

    jump main_interface_label

label christie_root_23_block:

    $ Event('christie_root_23_block', 'Sister_Room', time = 'night')
    show christie_root_18_gg_listening:
        xalign .5
    with my_dissolve
    "[gg]" "Надо взломать эту чёртову дверь, и только один человек знает, как это сделать."
    "[gg]" "Игорь!"
    $ location_now = 'Corridor'
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
