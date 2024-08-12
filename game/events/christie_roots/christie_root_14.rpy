label christie_root_14:
    $ events.pop('christie_root_14', 0)






    python:
        remove_from_inventory(name = 'Кофе «Релакс»')
        for i in ('afternoon', 'evening', 'night'):
            locations['Kitchen'].image_buttons_times[i].pop("coffe_50_percent", 0)
            locations['Kitchen'].image_buttons_times[i].update({"coffe_100_percent": Jump('christie_root_14_0')})




    $ location_now = "Kitchen"
    call show_all_images_label from _call_show_all_images_label_99
    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_right(xxzoom = -1)
    $ renpy.pause(.5)
    "[gg]" "Вот и всё."
    show GG Think:
        xalign .85
        xzoom -1.0
    with my_dissolve
    "[gg]" "Теперь надо дождаться, пока Кристи взбодрится любимым кофе и вновь побеседовать с ней."





    $ Event('christie_root_15', 'Christie', time = ['morning'], button_name = _("Кофе «Релакс»"))
    $ sister_position['morning'] = ['Kitchen', 'sister_kitchen_1']
    $ block_milf_home_8546412 = copy.deepcopy(block_milf_home)
    $ block_milf_home = True

    $ descript_Christie= _("Поговорить с Кристи Утром на Кухне.")

    jump main_interface_label


label christie_root_14_0:
    "[gg]" "Теперь надо дождаться, пока Кристи взбодрится любимым кофе и вновь побеседовать с ней."

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
