image ep1_movie_cinema 1 = 'cg/ep1/movie/cinema_1.png'
image ep1_movie_cinema 2 = 'cg/ep1/movie/cinema_2.png'
image ep1_movie_cinema 3 = 'cg/ep1/movie/cinema_3.png'
label ep1_5_mother_evening:
    $ events.pop('ep1_5_mother_evening', 0)
    call show_bg_image_label from _call_show_bg_image_label_88
    call show_additional_images_label from _call_show_additional_images_label_74
    show Milf Night_Normal
    show Milf Night_Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_left
    $ renpy.pause(1, hard = True)
    stop music fadeout 1.5
    play music 'audio/movie_event.mp3' fadein 1.5
    '[gg]' "Могу ли я составить тебе компанию?"
    show GG:
        xalign .15
    'Марина' "Конечно, [gg], я буду только рада. "
    scene black with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    scene expression 'cg/ep1/movie/cinema_screen_1.png' with Dissolve(.5)
    'Серый' "Лиза, разве ты не знаешь, что это раздевалка для мальчиков?"
    'Лиза' "Извини, но в женской ты не бываешь, а мне срочно нужно было увидеть тебя."
    scene expression 'cg/ep1/movie/cinema_screen_2.png' with Dissolve(.5)
    'Лиза' "Я пришла угостить тебя сладким кексиком. "
    'Серый' "С-спасибо."
    'Лиза' "Кушай, Серёжка, силы тебе понадобятся. "
    scene ep1_movie_cinema 1 
    show GG Invis
    show GG Invis:
        xalign .15
    show Milf Invis
    show Milf Invis:
        xalign .85
    with my_dissolve
    '[gg]' "Блин, этому сериалу уже целая вечность. Тебе он ещё не надоел?"
    'Марина' "Шутишь? Я его обожаю! "
    show ep1_movie_cinema 1
    with my_dissolve 
    'Марина' "И не беспокойся, тебе не нужно знать, что было в предыдущих сериях. Это ситком."
    '[gg]' "Подруга, я знаю этот сериал не хуже тебя. Его показывали, ещё когда я был совсем ребёнком."
    'Марина' "И он нисколько не устарел. "
    '[gg]' "Особенно главная героиня, которая снимается здесь вот уже целых 5 лет. "
    show ep1_movie_cinema 3
    with my_dissolve 
    'Марина' "Ну всё, тихо, сейчас начинается самое интересное!"
    '[gg]' "Только ради тебя, подруга."

    '[gg]' "Это не самый интересный сериал, что мне приходилось смотреть, но его любит Марина, и я рад провести с ней время."
    scene black with Dissolve(.5)
    $ renpy.pause(.5, hard = True)


    call show_bg_image_label from _call_show_bg_image_label_89
    call show_additional_images_label from _call_show_additional_images_label_75


    show GG
    show GG Think:
        ypos 1085
        zoom 1.0-0.035
        xalign .5

    with Dissolve(.5)

    $ descript = _('Полагаю, наши отношения с Мариной возвращаются в прежнее русло. Если я хочу, чтобы она снова доверяла мне, следует чаще проводить с ней время.')

    '[gg]' "Полагаю, наши отношения с Мариной возвращаются в прежнее русло. Если я хочу, чтобы она снова доверяла мне, следует чаще проводить с ней время."

    $ Event('ep1_6_morning', 'GG_Room', time = ['morning'])

    $ location_now = 'Hall'
    $ time.time_forward()
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
