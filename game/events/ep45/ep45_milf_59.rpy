label ep45_milf_59:
    $ location_now = 'City_Shop'
    call show_all_images_label from _call_show_all_images_label_7

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
    show GG Angry
    "[gg]" "Нашли мне горшок?"
    show Jay Normal
    show GG:
        xalign .1
    with my_dissolve
    "Бубнило" "А ты принёс нам трусики?"
    show GG Normal
    "[gg]" "Ага."
    show Jay Normal
    "Бубнило" "Забирай горшок."
    show GG Angry
    "[gg]" "Ловите трусы."
    show Jay Normal
    "Бубнило" "Оххх!!!.."
    show Jay Normal
    "Бубнило" "Чуешь как пахнет, Бубнило?"
    show Jay Normal
    "Бубнило" "Первый сорт! Сладкий пирожочек!"


    "Бубнило" "…."



    $ add_to_inventory(name = 'Растение в горшке')
    $ remove_from_inventory('Растение')
    $ remove_from_inventory('Трусики Кристи')





    $ descript = _("Установить горшок с растением в коридоре. Сделать это следует или Утром, или Днём.")

    $ events.pop('ep45_milf_59', 0)


    #$ locations['Corridor'].buttons[0].update({'ep5_milf_60': ((1350, 250, 100, 145), [Jump('ep5_milf_60')])})

    $ Event('ep5_milf_60', 'Corridor', time = ['morning', 'afternoon'])

    $ block_change_milf_position = True

    $ milf_position['morning']     = ['Kitchen', 'milf_kitchen']

    $ milf_position['afternoon']   = ['Kitchen', 'milf_kitchen']

    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(1)
    $ location_now = 'City_Shop'
    $ time.time_now = 'evening'

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
