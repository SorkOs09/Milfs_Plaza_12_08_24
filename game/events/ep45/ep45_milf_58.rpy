label ep45_milf_58:
    $ events.pop('ep45_milf_58', 0)
    $ locations['Restroom'].buttons[0].update({'washer': ((0, 650, 453, 429), [Jump('ep45_milf_58_2')])})
    $ location_now = 'Restroom'
    $ locations['Restroom'].buttons[0].update({'Corridor': ((683, 995, 535, 80),  [Jump('ep45_milf_58_corridor')])})

    jump main_interface_label

label ep45_milf_58_corridor:
    "[gg]" "Сначала нужно найти трусики Кристи."
    $ location_now = 'Restroom'
    jump main_interface_label

label ep45_milf_58_2:

    $ locations['Restroom'].buttons[0].update({'washer':   ((0, 650, 453, 429),   [Jump('restroom_washer_label')])})
    $ locations['Restroom'].buttons[0].update({'Corridor': ((683, 995, 535, 80),  [Function(JumpToLocation, 'Corridor')])})


    play sound 'audio/get_item.ogg'
    call show_all_images_label from _call_show_all_images_label_33
    $ add_to_inventory('Трусики Кристи')

    show screen give_item_screen(i_path+'/items/kristy_pants.png', _('Трусики Кристи'), _('Женское нижнее бельё.'))
    with Dissolve(.5)
    "[gg]" "До чего я докатился? Уже ворую женское нижнее бельё…"

    hide screen give_item_screen
    $ block_change_milf_position = False
    with Dissolve(.5)

    $ descript = _("Обменять трусики Кристи на горшок у Зудилы и Бубнилы.")

    $ Event('ep45_milf_59',     'JayBob')

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
