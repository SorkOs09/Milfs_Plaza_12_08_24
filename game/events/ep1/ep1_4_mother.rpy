label ep1_4_mother:
    $ events.pop('ep1_4_mother', 0)
    $ block_change_milf_position = False
    $ milf_position = {
        'morning'   : ('Restroom',  'milf_restroom'),
        'afternoon' : ('Kitchen',   'milf_kitchen'),
        'evening'   : ('Hall',      'milf_evening_hall'),
        'night'     : ('Milf_Room', 'milf_room'),
        
        }
    call show_bg_image_label from _call_show_bg_image_label_32
    call show_additional_images_label from _call_show_additional_images_label_27
    show Milf Normal
    show Milf Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_left
    $ renpy.pause(1, hard = True)






    '[gg]' "Ну как, мы всё ещё враги?"
    show Milf Laughs at hehe_transform()
    show GG:
        xalign .15

    'Марина' "Какой же ты дурачок, [gg]!"
    show GG Smile
    show Milf Normal
    'Марина' "Да, я заметила твою помощь по дому."
    'Марина' "Ты молодец. Когда хочешь."
    'Марина' "Но это не значит, что в ближайшее время наши отношения будут как прежде."
    show GG Normal
    '[gg]' "Но ты уже не злишься, верно?"
    'Марина' "Конечно нет, [gg]. Ведь я люблю тебя."
    '[gg]' "Я тоже тебя люблю…"
    hide GG Normal
    with Dissolve(.5)
    if 'kitchen' in location_now.lower():

        $ renpy.pause(.5,hard = True)
        show Milf Not_Nude
        with Dissolve(.5)
        'Марина' "О Боже! Моё платье закатилось! Теперь понятно, откуда этот ветерок продувает мне трусики. "
        'Марина' "[gg] видел это и ничего не сказал?.."
        show Milf Embarrassment
        'Марина' "Как неловко…"

    $ descript = _('Полагаю, наши отношения с Мариной возвращаются в прежнее русло. Если я хочу, чтобы она снова доверяла мне, следует чаще проводить с ней время.')
    $ Event('ep1_5_mother_evening', 'Hall_Milf', time = ['evening',])
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
