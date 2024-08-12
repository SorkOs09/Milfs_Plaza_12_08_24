
label ep3_2_milf_kitchen:
    $ block_change_milf_position = False
    $ milf_position = {
        'morning'   : ('Restroom',  'milf_restroom'),
        'afternoon' : ('Kitchen',   'milf_kitchen'),
        'evening'   : ('None',      'milf_evening_hall'),
        'night'     : ('Milf_Room', 'milf_room'),
        }
    $ events.pop('ep3_2_milf_kitchen', 0)


    show GG Normal
    show GG Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    show Milf Normal
    show Milf Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    $ t('Марина', 'Как проходит твой день, [gg]?')
    $ t('[gg]', 'Просто бездельничаю. ')
    show Milf Smile
    $ t('Марина', 'Я не удивлена. ')
    hide GG
    show Milf Not_Nude
    with Dissolve(.5)
    $ renpy.pause(1, hard = True)
    with Dissolve(.5)
    show Milf Embarrassment
    with Dissolve(.5)
    $ t('Марина', 'Он снова проигнорировал…')
    $ t('Марина', 'Видел мою попку и даже ничего не предпринял.')
    $ t('Марина', 'Я совсем рехнулась.')
    show Milf Chagrin
    $ t('Марина', 'Между нами не может быть никаких отношений. ')
    $ t('Марина', 'Мы друзья. И точка. ')

    show Milf Angry
    $ t('Марина', 'Какая же ты дура, Марина. У тебя есть муж, и ты обязана его дождаться.')


    $ location_now = 'Kitchen'


    jump main_interface_label



label ep3_2_milf_hall:
    $ events.pop('ep3_2_milf_kitchen', 0)
    $ events.pop('ep3_2_milf_hall', 0)

    show GG Normal
    show GG Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    show Milf Night_Normal
    show Milf Night_Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035

    with Dissolve(.5)
    stop music fadeout 1.5
    play music 'audio/movie_event.mp3' fadein 1.5
    $ t('[gg]', 'Могу ли я составить тебе компанию?', False)
    $ t('Марина', 'Конечно, [gg], я буду только рада. ', False)
    scene expression 'cg/movie/cinema_screen_1.png' with Dissolve(.5)
    $ t('Серый', 'Лиза, разве ты не знаешь, что это раздевалка для мальчиков?', False)
    $ t('Лиза', 'Извини, но в женской ты не бываешь, а мне срочно нужно было увидеть тебя.', False)
    scene expression 'cg/movie/cinema_screen_2.png' with Dissolve(.5)
    $ t('Лиза', 'Я пришла угостить тебя сладким кексиком. ', False)
    $ t('Серый', 'С-спасибо.', False)
    $ t('Лиза', 'Кушай, Серёжка, силы тебе понадобятся. ', False)
    scene expression 'cg/movie/cinema_1.png' with Dissolve(.5)
    $ t('[gg]', 'Блин, этому сериалу уже целая вечность. Тебе он ещё не надоел?', False)
    $ t('Марина', 'Шутишь? Я его обожаю! ', False)
    scene expression 'cg/movie/cinema_2.png' with Dissolve(.5)
    $ t('Марина', 'И не беспокойся, тебе не нужно знать, что было в предыдущих сериях. Это ситком.', False)
    $ t('[gg]', 'Подруга, я знаю этот сериал не хуже тебя. Его показывали, ещё когда я был совсем ребёнком.', False)
    $ t('Марина', 'И он нисколько не устарел. ')
    $ t('[gg]', 'Особенно главная героиня, которая снимается здесь вот уже целых 5 лет. ', False)
    scene expression 'cg/movie/cinema_3.png' with Dissolve(.5)
    $ t('Марина', 'Ну всё, тихо, сейчас начинается самое интересное!', False)
    $ t('[gg]', 'Только ради тебя, подружка.', False)
    scene black with Dissolve(.5)
    $ t('[gg]', 'Это не самый интересный сериал, что мне приходилось смотреть, но его любит Марина, и я рад провести с ней время.', False)




    $ location_now = 'Hall'
    $ time.time_forward()
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
