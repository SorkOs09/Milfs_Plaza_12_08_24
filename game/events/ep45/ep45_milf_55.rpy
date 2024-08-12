transform watering_can_blink_ep5:
    on idle:
        linear 1 alpha .7
        linear 1 alpha .0
        .5
        repeat
    on hover:
        linear .2 alpha 1.0









































































label ep45_milf_55:






















label ep45_milf_55_hall:

    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    $ Hide('watering_can_screen_ep5')()
    with Dissolve(.5)
    play audio 'audio/water_click.ogg'
    $ ep45_milf_55_hall_phr = renpy.random.choice([
        _("Хм, а в этом реально нет ничего сложного!"), 
        _("Поддерживая жизнь этих милых созданий, я поддерживаю хорошее настроение у своей женщины."),
        _("Порой мне кажется, что кислород, даваемый растениями, они больше потребляют сами."),
        _("Самая простая работа в мире! Нет, это лучшая работа в мире!"),
        ])
    "[gg]" "[ep45_milf_55_hall_phr]"
    $ del ep45_milf_55_hall_phr
    jump main_interface_label





label ep45_milf_55_1:

    $ locations['Corridor'].buttons[0].update({'home_plant': ((1401, 581, 176, 110,), [SetVariable('money_boost_label_now', 'corridor_home_plant_label'), Jump('money_boost_label')])})
    jump ep45_milf_55_hall
label ep45_milf_55_2:


    $ locations['Hall'].buttons[1]['home_plant_2'] = ((1729, 61, 190, 215),   Jump('hall_home_plant_2_label'))
    jump ep45_milf_55_hall

label ep45_milf_55_3:

    $ locations['Hall'].buttons[0]['home_plant_1'] = ((156, 140, 225, 249),   [SetVariable('money_boost_label_now', 'hall_home_plant_1_label'), Jump('money_boost_label')])

    jump ep45_milf_55_hall

label ep45_milf_55_4:

    $ locations['Hall'].buttons[0]['home_plant_3'] = ((636, 450, 105, 181),   [SetVariable('money_boost_label_now', 'hall_home_plant_3_label'), Jump('money_boost_label')])
    jump ep45_milf_55_hall



label ep45_milf_55_korridor:
    $ events.pop('ep45_milf_55_korridor', 0)
    # $ locations['Hall'].buttons[1]['home_plant_2'] = ((1729, 61, 190, 215),   Jump('hall_home_plant_2_label'))

    # $ locations['Hall'].buttons[0]['home_plant_1'] = ((156, 140, 225, 249),   [SetVariable('money_boost_label_now', 'hall_home_plant_1_label'), Jump('money_boost_label')])

    # $ locations['Hall'].buttons[0]['home_plant_3'] = ((636, 450, 105, 181),   [SetVariable('money_boost_label_now', 'hall_home_plant_3_label'), Jump('money_boost_label')])

    # $ locations['Corridor'].buttons[0].update({'home_plant': ((1401, 581, 176, 110,), [SetVariable('money_boost_label_now', 'corridor_home_plant_label'), Jump('money_boost_label')])})


    # $ locations['Corridor'].buttons[0].pop('ep45_milf_55_korridor', 0)

    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    $ Hide('watering_can_screen_ep5')()
    $ remove_from_inventory('Лейка')

    play audio 'audio/water_click.ogg'
    call show_bg_image_label from _call_show_bg_image_label_45
    with Dissolve(.5)

    show expression 'cg/ep45/flower/gg1.png'
    with Dissolve(.5)






    "[gg]" "Слишком маленькая табуретка."


    "[gg]" "Я едва достаю…."


    "[gg]" "Не очень удобно, конечно."


    $ locations['Corridor'].bg = 'Corridor_wt'

    call show_bg_image_label from _call_show_bg_image_label_52
    call show_additional_images_label from _call_show_additional_images_label_46
    show expression 'cg/ep45/flower/gg2.png'
    with vpunch
    "[gg]" "Твою мать!!!"


    "[gg]" "Мне хана!"











    scene expression '#000'
    with Dissolve(.5)
    call show_bg_image_label from _call_show_bg_image_label_53
    call show_additional_images_label from _call_show_additional_images_label_47
    with Dissolve(.5)
    show GG Chagrin
    show GG Chagrin:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    show Milf Surprise
    show Milf Surprise:
        xalign 1.5
        ypos 1085
        zoom 1.0-0.035
    $ renpy.pause(.05, hard = True)
    show Milf:
        linear 1 xalign .85
    $ renpy.pause(1, hard = True)

    show Milf Surprise:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with my_dissolve



    $ renpy.music.stop(fadeout=.5)

    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)




    "Марина" "Боже мой, что здесь произошло?!"
    show Milf Surprise
    "Марина" "[gg], ты в порядке? "
    show GG Chagrin
    "[gg]" "Да я…"
    show GG Chagrin
    "Марина" "О нет! Это что, моё любимое растение?!!"
    show GG Chagrin
    "Марина" "«Джими», мой бедненький ребёночек!"
    show GG Skepticism
    "[gg]" "Это что, новый сорт?"
    show Milf Angry
    "Марина" "Это его имя! "
    show Milf Angry
    "Марина" "У них у всех есть имена"
    show Milf Angry
    "Марина" "И ты убил его!"
    show GG Surprise
    "[gg]" "Эй, полегче! Это всего-навсего чёртово растение. "
    show GG Surprise
    "[gg]" "Я ж не хотел, понимаешь? "


    show Milf Chagrin
    "Марина" "Ну конечно. "
    show Milf Chagrin
    "Марина" "Так легко обесценить моё отношение к тому, что мне дорого. "
    show Milf Chagrin
    "Марина" "А ведь я просила тебя быть осторожным…"
    show GG Chagrin
    "[gg]" "Ну прости. Прости."
    show GG Chagrin
    "[gg]" "Я признаю свою вину."
    show GG Angry
    "[gg]" "Я попытаюсь всё исправить, честно!"
    show Milf Chagrin
    "Марина" "Ох, брось…"
    show Milf Chagrin
    "Марина" "Скоро я успокоюсь и жизнь наладится. "
    show GG Normal
    "[gg]" "Ты режешь мне сердце, Марина! "
    show GG Normal
    "[gg]" "Я что-то придумаю, честное слово. Я всё исправлю."
    show Milf Chagrin
    "Марина" "Извини меня, мне надо побыть одной… "



    show Milf Chagrin:
        xzoom -1
        linear 1 xalign 1.5
        ypos 1085
        zoom 1.0-0.035
    $ renpy.pause(1, hard = True)

    hide Milf

    show GG Think
    with my_vpunch


    $ renpy.music.stop(fadeout=.5)

    $ renpy.music.play('audio/thinking-music-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)



    "[gg]" "Охренеть!"
    #show GG Think
    "[gg]" "Я и не знал, что она так повёрнута на этих растениях. "
    #show GG Think
    "[gg]" "Хотя, конечно, откуда мне знать? Эгоисту чёртову…"
    #show GG Think
    "[gg]" "Не так давно меня интересовали только лёгкие деньги."
    #show GG Think
    "[gg]" "Нет уж, я не позволю Марине страдать из-за своего эгоизма. "
    #show GG Think
    "[gg]" "Надо найти замену этому «Джими»."
    #show GG Think
    "[gg]" "И, кажется, в нашем Парке я видел похожую растительность."
    #show GG Think
    "[gg]" "Надо поискать на досуге."


    $ renpy.music.stop(fadeout=.5)

    $ renpy.music.play('audio/thinking-music-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)




    # $ igor_position = {
    #     'morning'   : ('City_Park',  'igor_park'),
    #     'afternoon' : ('City_Park',  'igor_park'),
    #     'evening'   : ('None',       'None'),
    #     'night'     : ('None',       'None'),
        
    #     }

    $ korridor_without_tree_ep5 = True



    $ events.pop('ep45_milf_54_city_home', 0)


    scene black with Dissolve(.5)

    $ renpy.pause(.1, hard = True)

    $ renpy.pause(.4)

    $ time.time_now = 'night'

    $ descript = _("Найти замену растению по имени Джими. Поискать его в парке.")


    $ locations['City_Park'].image_buttons_times = {
    'morning'   : {'search_game_icon': Jump('ep45_milf_56')},
    'afternoon' : {'search_game_icon': Jump('ep45_milf_56')},
    'evening'   : {},
    'night'     : {},
    }
    $ events.pop('ep45_milf_52_skip', 0)



    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
