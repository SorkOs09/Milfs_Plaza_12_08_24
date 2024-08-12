label ep3_milf_23:

    $ events.pop('ep3_milf_23', 0)


    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085

    show Jay Normal
    show Jay Normal:
        xalign .35
        ypos 1085

        xalign .65
    show Bob Normal
    show Bob Normal:
        xalign .65
        ypos 1085

        xalign .95

    with Dissolve(.5)
















    "Зудило" "Рады тебя видеть, чувак!"
    show GG Skepticism
    "[gg]" "Да ладно?"
    "Зудило" "Ага, вчерашний пранк собрал хренову тучу просмотров. Мы попали в тренды!"
    show GG Skepticism
    "[gg]" "Безумно за вас рад. Гоните билеты. "
    "Зудило" "Конечно. Вот."






    $ add_to_inventory(name = 'Билеты')

    window hide
    show screen give_item_screen(i_path+'/items/ticket.png', _("Билеты"), [_("Билеты"), _("Театральные билеты на постановку «Кошки».")])



    with Dissolve(.5)

    $ renpy.pause(99999)

    hide screen give_item_screen
    show GG Angry
    with Dissolve(.5)
    "[gg]" "Спасибо говорить не стану."
    "Зудило" "Какой обидчивый."

    if love_milf >= 5:

        $ descript = _("Убедить Марину и Кристи отправиться в театр.")
        $ Event('ep3_milf_24',     'Milf')
        $ Event('ep3_milf_24_2',   'Christie')
    elif True:



        $ descript = _('Требование: 5 Любовь Марины.')

        $ milf_love_quests = 5


    $ block_change_milf_position = True

    $ milf_position = {
        'morning'   : ('Restroom',  'milf_restroom'),
        'afternoon' : ('Kitchen',   'milf_kitchen'),
        'evening'   : ('Hall',      'milf_evening_hall'),
        'night'     : ('Milf_Room', 'milf_room'),
    }
    $ location_now = 'City_Shop'

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
