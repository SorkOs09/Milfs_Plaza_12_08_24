label ep1_7_phone:

    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()


    call show_bg_image_label from _call_show_bg_image_label_2
    show GG Think
    show GG Think:
        ypos 1085
        zoom 1.0-0.035
        xalign .5

    with Dissolve(.5)


    '[gg]' "{i}Мне срочно нужны деньги. И много!{/i}"
    '[gg]' "{i}Но если Марина узнает о моей проблеме, то навсегда разочаруется во мне. А значит, я не могу обратиться к ней за помощью.{/i}"
    '[gg]' "{i}Надо свалить из города. Хотя бы на время. Меня поищут и успокоятся.{/i}"
    '[gg]' "{i}Я понимаю, что обещал брату присматривать за Мариной, но со мной ей будет грозит опасность.{/i}"
    '[gg]' "{i}К тому же, я не собираюсь исчезнуть навсегда. {/i}"
    '[gg]' "{i}Недельку или две перекантуюсь у приятеля в соседнем городе… {/i}"
    '[gg]' "{i}Надо бы сходить в магазин, купить большой новый рюкзак и кое-какие продукты для поездки.{/i}"

    $ descript = _("Надо бы сходить в магазин, купить большой новый рюкзак и кое-какие продукты для поездки.")


    $ block_exit_home  = False


    $ milf_position['morning']   = ('Kitchen', 'milf_kitchen')
    $ milf_position['afternoon'] = ('Kitchen', 'milf_kitchen')
    $ milf_position['evening']   = ('None', 'None')

    $ block_change_milf_position = True

    $ show_text_animation(_('Дверь в квартиру теперь доступна!'))

    $ locations['Corridor'].buttons[0].update({'Exit To City Home'  : ((906, 381, 162, 353,), [Function(renpy.play, 'audio/door.mp3'), Jump('ep2_1_door')]),})


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
