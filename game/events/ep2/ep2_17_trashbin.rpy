label ep2_17_trashbin:
    $ Hide('give_item_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    if time.time_now in ('evening', 'night'):
        $ locations['City_Park'].image_buttons.pop('trashbin', 0)
        show GG GiveGun
        show GG GiveGun:
            xalign .5
            ypos 1085
            zoom 1.0-0.035
        with Dissolve(.5)
        $ renpy.pause(999)
        '[gg]' "Жил молодым, и умер молодым."
        $ remove_from_inventory('Резиновые перчатки')
        $ descript = _('Вернуться домой.')
        $ Event('ep2_18_end', 'Corridor')
        show screen give_item_screen(i_path+'/items/gun.png', _('Сильверболлер'), [_('Говорят, это оружие'), _('пользуется спросом у наёмных убийц.')])
        with Dissolve(.5)
        $ renpy.pause(999999)
        hide screen give_item_screen
        $ add_to_inventory(name = 'Сильверболлер')
    elif True:
        '[gg]' "Не сейчас, меня могут заметить."
        '[gg]' "Нужно придти вечером."
    jump main_interface_label


label ep2_17_trashbin_stump:
    $ Hide('give_item_screen')()
    $ Hide('main_interface')()
    '[gg]' "Я не полезу туда без перчаток."
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
