label already_did_it_today:
    "[gg]" "Я уже делал это сегодня."
    return
    
label money_boost_label:
    if random_1_2_money.get_n() == 1:
        $ money_boost_labels_click_today.append(money_boost_label_now)

    if money_boost_label_now in money_boost_labels_click_today:
        $ renpy.jump(money_boost_label_now)

    $ money_boost_labels_click_today.append(money_boost_label_now)
    if not getattr(store, 'cupon_zanachka', False):
        $ cupon_zanachka = True
        $ add_to_inventory(name = 'Купон «кекса»', ncopy = True)
        show screen give_item_screen(i_path+'/items/keks.png', _('Купон «кекса»'),[_('Коллекционный купон, '), _('Но сейчас эта самая ходовая валюта'), _('на чёрном рынке.')])
        with Dissolve(.5)
        $ renpy.pause(9999)
        hide screen give_item_screen
        with Dissolve(.5)
        jump main_interface_label
    $ plus   = renpy.random.randint(1, 5)
    $ money += plus

    play sound 'audio/money.ogg'

    $ show_text_animation(text = '+' +str(plus)+' money')

    '[gg]' "О, заначка!"

    $ del plus

    jump main_interface_label



label corridor_picture_1_label:

    '[gg]' "Ничем не примечательное изображение."
    jump main_interface_label


label corridor_picture_2_label:

    '[gg]' "Ничем не примечательное изображение."
    jump main_interface_label


label corridor_picture_3_label:

    '[gg]' "На картине изображён красивый небоскрёб. "
    jump main_interface_label





label corridor_tumba_label:

    '[gg]' "Здесь лежат рабочие инструменты и строительные детали на запас. "
    jump main_interface_label


label corridor_home_plant_label:

    '[gg]' "Источник кислорода. "
    jump main_interface_label


label corridor_cupboard_label:

    '[gg]' "Шкаф с одеждой, которую мы используем в холодные дни."
    jump main_interface_label


label corridor_ottoman_label:

    '[gg]' "Шкаф-табурет, где хранятся гуталин, щётка ложка для обуви."
    jump main_interface_label

label corridor_hanger_label:

    '[gg]' "Повседневная одежда. "
    jump main_interface_label























label hall_books_label:


    '[gg]' "Книги по психологии и прочая общеобразовательная литература"


    jump main_interface_label



label hall_clean_label:

    if time.time_now in ['evening', 'night'] or getattr(store, 'block_uborka', 0):
        '[gg]' "Сегодня я уже не буду этого делать."
        jump main_interface_label
    elif True:
        show expression 'images/cg/gg_activities/gg_clean_hall.png'

        with Dissolve(.5)

        play sound 'audio/vacuum.ogg'
        $ renpy.pause(3, hard = True)

        hide expression 'images/cg/gg_activities/gg_clean_hall.png'

        with Dissolve(.5)


        show GG Normal
        show GG Normal:
            xalign .1
            ypos 1085
            zoom 1.0-0.035
        with Dissolve(.5)
        '[gg]' "Теперь этот ковёр должен быть чистым. Надеюсь, Марине это понравится!"
        $ show_text_animation('+5 milf')
        $ gigiena   = max(0,  gigiena-2)
        $ nastroi   = max(0,  nastroi-5)

        $ block_uborka = True

    jump main_interface_label



label hall_tv_label:


    if time.time_now in ['morning', 'afternoon'] and sister_position[time.time_now][0] != location_now:


        menu:
            "1. Отдохнуть. (+50 ед. Настроения, -2 сытости)" if True:

                if getattr(store, 'block_nastroi', 0):
                    '[gg]' "Сегодня я уже не буду этого делать."
                    jump main_interface_label

                show expression 'cg/gg_activities/cg_surv_gg_tv.png'

                with Dissolve(.5)

                play audio 'audio/rest.ogg'
                $ show_text_animation('+50 nastroi')
                $ nastroi  = min(100, nastroi+50)
                $ sitost   = max(0,   sitost-2)

                $ location_now = 'Hall'
                $ block_nastroi = True
                "[gg]" "После продолжительного отдыха я начинаю чувствовать себя намного лучше."
                $ show_text_animation('-2 sitost')
                jump main_interface_label
            "Уйти." if True:
                $ pass
    elif True:

        '[gg]' " Это наш телевизор фирмы «Телевизор»."


    jump main_interface_label

label hall_home_plant_1_label:



    '[gg]' " Я понятия не имею, что это за растение."


    jump main_interface_label

label hall_home_plant_2_label:



    '[gg]' " Всего-лишь домашнее растение. "


    jump main_interface_label

label hall_home_plant_3_label:



    '[gg]' " Такое же растение как и все. "


    jump main_interface_label

label hall_tumba_under_tv_label:



    '[gg]' " Здесь хранится какая-то макулатура и диски с фильмами. "


    jump main_interface_label

label hall_video_player_label:



    '[gg]' " Обычный видео-проигрывать для дисков."


    jump main_interface_label


label hall_coffee_table_hairpin_label:


    $ locations['Hall'].buttons[0].pop('coffee_table_hairpin', 0)


    $ locations['Hall'].buttons[0].update({'coffee_table': (
    (878, 705, 379, 173), [SetVariable('money_boost_label_now', 'hall_coffee_table_label'), Jump('money_boost_label')])})


    call get_hairpin_label from _call_get_hairpin_label

    jump main_interface_label



label hall_coffee_table_label:




    '[gg]' " Журнальный стол, на который я люблю класть ноги."


    jump main_interface_label

label hall_picture_label:



    '[gg]' " Картина, которую я купил с первой подработки. "


    jump main_interface_label





















label check_restroom_block_milf_sister:

    if (not getattr(store, "block_milf_home", False)) and milf_position[time.time_now][0]  == location_now:
        '[gg]' "Я не могу это сделать пока здесь Марина."
        jump main_interface_label

    if (not getattr(store, "block_sister_home", False)) and sister_position[time.time_now][0] == location_now:
        '[gg]' "Я не могу это сделать пока здесь Кристи."
        jump main_interface_label

    return


label get_hairpin_label:

    play sound 'audio/get_item.ogg'
    $ add_to_inventory(name = 'Шпилька')

    $ item_tmp = get_item('Шпилька', True)
    show expression '#000a'
    hide screen icons_interface
    show screen give_item_screen(i_path+'/items/hairpin.png', _('Шпилька'), _('Из трех таких можно сделать отмычку'))


    with Dissolve(.5)
    $ renpy.pause(9999)

    '[gg]' "Я нашёл шпильку. "

    if getattr(item_tmp, 'quant', 0) >= 3:
        jump hairpins_label
    elif getattr(item_tmp, 'quant', 0) >= 2:
        '[gg]' "Ещё одна такая же, и я наверняка смогу сделать отмычку."
    elif True:
        '[gg]' "Ещё пару таких же, и я наверняка смогу сделать отмычку."
    hide screen give_item_screen
    with Dissolve(.5)
    return


label restroom_hair_pin_label:


    $ locations['Restroom'].image_buttons.pop('hair_pin', 0)

    call get_hairpin_label from _call_get_hairpin_label_1

    jump main_interface_label



label hairpins_label:
    '[gg]' "Теперь я точно смогу сделать сделать отмычку."

    '[gg]' "Тааак-с. Здесь подогнуть, здесь изогнуть…"

    '[gg]' "Вуаля!"

    $ remove_from_inventory(name = 'Шпилька')
    $ remove_from_inventory(name = 'Шпилька')
    $ remove_from_inventory(name = 'Шпилька')
    $ remove_from_inventory(name = 'Шпилька')

    $ add_to_inventory(name = 'Отмычка')
    play sound 'audio/get_item.ogg'
    show expression '#000a'
    show screen give_item_screen(i_path+'/items/unlocker.png', _(' Отмычка'), [_('С помощью этого инструмента я смогу проникать'), _('в некоторые закрытые двери.')])


    with Dissolve(.5)
    $ renpy.pause(99999999999)
    hide screen give_item_screen
    with Dissolve(.5)


    jump main_interface_label

label restroom_shower_cabin_label:



    call check_restroom_block_milf_sister from _call_check_restroom_block_milf_sister_1
    python:
        location_now = 'Restroom_shower'
        check_ev = check_events()

        if check_ev:
            renpy.jump(check_ev.label)

        location_now = 'Restroom'
    menu:
        "Принять душ (+100 ед. Гигиена)" if True:
            $ store.ACH_5_count[3] = True
            
            if getattr(store, 'block_gigiena', 0):
                '[gg]' "Сегодня я уже не буду этого делать."
                jump main_interface_label

            $ ACH_21_count = 0

            show expression 'cg/gg_activities/cg_surv_gg_dush.png'
            with Dissolve(.5)

            $ block_gigiena = True

            $ gigiena  = 100
            $ show_text_animation('+100 gigiena')
            play audio 'audio/water_click.ogg'
            "[gg]" "Чистый телом – чистый духом. Главное, ухи не забыть помыть."

        "Уйти." if True:


            $ pass
    jump main_interface_label

label restroom_bath_label:

    call check_restroom_block_milf_sister from _call_check_restroom_block_milf_sister_2
    python:
        location_now = 'Restroom_bath'
        check_ev = check_events()

        if check_ev:
            renpy.jump(check_ev.label)

        location_now = 'Restroom'

    menu:
        "Принять ванну (+100 Гигиена)" if True:
            $ store.ACH_5_count[3] = True
            
            if getattr(store, 'block_gigiena', 0):
                '[gg]' "Сегодня я уже не буду этого делать."
                jump main_interface_label

            show expression 'cg/gg_activities/cg_surv_gg_vanna.png'
            with Dissolve(.5)

            $ block_gigiena = True

            $ ACH_21_count = 0


            $ gigiena  = 100


            play audio 'audio/water_click.ogg'
            $ pass
            $ show_text_animation('+100 gigiena')
            "[gg]" "Чистый телом – чистый духом. Главное, ухи не забыть помыть."
        "Уйти." if True:


            $ pass
    jump main_interface_label

label restroom_crane_label:
    call check_restroom_block_milf_sister from _call_check_restroom_block_milf_sister_3
    python:
        location_now = 'Restroom_crane'
        check_ev = check_events()

        if check_ev:
            renpy.jump(check_ev.label)

        location_now = 'Restroom'
    menu:
        "Почистить зубы (+50 Гигиена)" if True:


            if getattr(store, 'block_gigiena', 0):
                '[gg]' "Сегодня я уже не буду этого делать."
                jump main_interface_label


            $ block_gigiena = True
            $ ACH_21_count = 0


            show expression 'images/cg/gg_activities/gg_tooth_restroom.png'
            with Dissolve(.5)

            $ gigiena  = min(100, gigiena+50)




            play audio 'audio/water_click.ogg'
            $ pass
            $ show_text_animation('+50 gigiena')
            "[gg]" "Чистый телом – чистый духом. Главное, ухи не забыть помыть."
        "Уйти." if True:

            $ pass
    jump main_interface_label

label restroom_locker_label:

    '[gg]' "Шкафчик с медикаментами. "

    jump main_interface_label


label restroom_tumba_bath_label:
    '[gg]' "Здесь полно стиральных средств, и кое-какие инструменты для уборки по дому."

    jump main_interface_label
label restroom_washer_label:
    call check_restroom_block_milf_sister from _call_check_restroom_block_milf_sister_4

    if getattr(store, 'block_stirka', False) or time.time_now == 'Night':
        '[gg]' "Здесь я стираю свои вещи."
        jump main_interface_label



    $ block_stirka = True
    $ gigiena      = max(0,  gigiena-2)
    $ nastroi      = max(0,  nastroi-5)

    show expression 'images/cg/gg_activities/gg_clothes_restroom.png'
    with Dissolve(.5)
    '[gg]' "Постираю вещи, надеюсь это понравится Марине."
    play audio 'audio/rest.ogg'

    $ show_text_animation('+5 milf')




    jump main_interface_label
























label kitchen_solar_oil_label:
    '[gg]' "Да, это подсолнечное масло."
    if hasattr(store, 'solar_milf_room'):
        $ locations['Kitchen'].image_buttons.pop('solar_oil', 0)
        play sound 'audio/get_item.ogg'


        show screen give_item_screen('images/interface/items/solar_oil.png', _('Солнечное масло'), [_('Это можно использовать в качестве смазки'), _('для петель двери')])


        with Dissolve(.5)
        $ renpy.pause(99999999)
        hide screen give_item_screen
        $ solar_milf_room = True
        with Dissolve(.5)
        $ add_to_inventory(name = 'Солнечное масло')

        jump main_interface_label
    jump main_interface_label

























label kitchen_refrigerator_label:
    python:
        location_now = 'Kitchen_refrigerator'
        check_ev = check_events()

        if check_ev:
            renpy.jump(check_ev.label)

        location_now = 'Kitchen'
    menu:
        "Покушать. (+100 ед. Сытость, -2 Гигиена)" if True:

            $ ACH_5_count[0] = True

            if getattr(store, 'block_eat', 0):
                '[gg]' "Сегодня я уже не буду этого делать."
                jump main_interface_label
            $ sitost  = 100
            $ gigiena   = max(0,   gigiena-2)
            #$ ACH_21_count = 0


            $ pass
            $ show_text_animation('+100 sitost')
            play audio "audio/eat.ogg"

            show expression 'cg/gg_activities/cg_surv_gg_eat.png'
            with Dissolve(.5)

            "[gg]" "Чавк! Чавк! Чавк! Физические силы возвращаются ко мне. Если, конечно, они у меня вообще были."
            $ show_text_animation('-2 gigiena')




            $ block_eat = True
        "Уйти." if True:
            $ pass
    jump main_interface_label

label kitchen_top_lockers_label:
    '[gg]' " Здесь хранятся крупы, специи, чай, кофе и куча всего по мелочи, что дополняет основное блюдо."
    jump main_interface_label


label kitchen_bottom_lockers_label:
    call show_empty_screen from _call_show_empty_screen_32
    '[gg]' "Здесь лежит посуда, столовые инструменты, тряпки, отдел для мусорного ведра и прочее. "
    jump main_interface_label


label kitchen_sink_label:


    if getattr(store, 'block_wash_posuda', False) or time.time_now == 'Night':
        '[gg]' "Сегодня я уже не буду этого делать."
        jump main_interface_label

    if milf_position[time.time_now][0] == 'Kitchen':
        '[gg]' "Здесь можно помыть посуду. "
        jump main_interface_label

    menu:
        "Мыть руки (+50 Гигиена)" if True:
            if getattr(store, 'block_gigiena', 0):
                '[gg]' "Сегодня я уже не буду этого делать."
                jump main_interface_label


            $ block_gigiena = True
            $ ACH_21_count = 0

            $ gigiena  = min(100, gigiena+50)
            $ show_text_animation('+50 gigiena')
            play audio 'audio/water_click.ogg'
            jump main_interface_label
        "Мыть посуду" if True:
            $ pass
        "Уйти." if True:
            jump main_interface_label
    show expression 'images/cg/gg_activities/gg_wash_kitchen.png'
    with Dissolve(.5)

    '[gg]' "Помою посуду, надеюсь это понравится Марине."
    play audio 'audio/rest.ogg'

    $ show_text_animation('+5 milf')
    $ gigiena   = max(0,  gigiena-2)
    $ nastroi   = max(0,  nastroi-5)

    $ block_wash_posuda = True
    jump main_interface_label


label kitchen_coffee_maker_label:

    '[gg]' "С помощью этой штуки я могу заварить зерновое кофе."
    jump main_interface_label


label kitchen_toaster_label:

    '[gg]' "Да, это тостер."
    jump main_interface_label






label gg_room_window_event_1_label:


    if time.time_now == 'afternoon':

        if hasattr(store, 'window_event_1'):
            scene expression 'cg/window_event/afternoon.png' with Dissolve(.5)
            if preferences.language in (None, 'eng', 'rus'):
                '[gg]' "Бессмысленно. Меня уже заметили. "
            else:
                call wait_click_label from _call_wait_click_label_21
        elif True:
            $ window_event_1 = 1

            scene expression 'cg/window_event/woman_1.png' with Dissolve(.5)
            if preferences.language in (None, 'eng', 'rus'):
                '[gg]' "Боже, что это за красотка живёт напротив? "
                '[gg]' "У неё отличное тело... "
            else:
                call wait_click_label from _call_wait_click_label_22
            scene expression 'cg/window_event/woman_2.png' with Dissolve(.5)
            if preferences.language in (None, 'eng', 'rus'):
                '[gg]' "и сиськи."
            else:
                call wait_click_label from _call_wait_click_label_23
            scene expression 'cg/window_event/woman_3.png' with Dissolve(.5)
            if preferences.language in (None, 'eng', 'rus'):
                '[gg]' "Проклятье, она засекла меня!"
            else:
                call wait_click_label from _call_wait_click_label_24
    elif time.time_now == 'morning':


        if not hasattr(store, 'window_event_1'):
            scene expression 'cg/window_event/afternoon.png' with Dissolve(.5)
            '[gg]' "Нужно будет глянуть в другое время."
        elif True:
            jump window_lvl_2
    elif time.time_now == 'evening':
        if not hasattr(store, 'window_event_1'):
            scene expression 'cg/window_event/evening.png' with Dissolve(.5)
            $ renpy.pause(1, hard = True)
            '[gg]' "Нужно будет глянуть в другое время."
        elif True:
            jump window_lvl_2
    elif time.time_now == 'night':
        scene expression 'cg/window_event/night.png' with Dissolve(.5)
        $ renpy.pause(1, hard = True)
        '[gg]' "Нужно будет глянуть в другое время."

        #if not hasattr(store, 'window_event_1'):
        #elif True:
        #    jump window_lvl_2
    scene expression '#000' with Dissolve(.5)
    jump main_interface_label




label gg_room_window_label:
    '[gg]' "Вид из окна смотрит ровно на такой же дом по соседству."
    scene window_lvl_2 s0: 
        blur 50
    with my_dissolve
    menu:
        "!Использовать бинокль" if not get_item('Бинокль', True):
            $ pass
        "Использовать бинокль" if get_item('Бинокль', True):
            jump gg_room_window_event_1_label
        "Назад" if True:
            $ pass
    jump main_interface_label

label gg_room_systemist_label:

    '[gg]' "Одно слово – RTX 3090."
    jump main_interface_label




label gg_room_picture_label:

    '[gg]' "Моя любимая картина, которую мне подарила подруга."
    jump main_interface_label






label gg_room_guitar_label:

    '[gg]' "Эту гитару мне подарила Марина, но я так и не научился на ней играть."

    jump main_interface_label



label gg_room_curbstone_hairpin_label:

    show expression '#000a'

    with Dissolve(.3)

    $ locations['GG_Room'].buttons[1].pop('curbstone_hairpin', 0)


    $ locations['GG_Room'].buttons[1].update({'curbstone': (
    (675, 550, 200, 130,), [SetVariable('money_boost_label_now', 'gg_room_curbstone_label'), Jump('money_boost_label')])})


    call get_hairpin_label from _call_get_hairpin_label_2

    jump main_interface_label



label gg_room_curbstone_label:

    '[gg]' "Куча безделушек, вроде йо-йо, курительной трубки, старое PSP и так далее."

    jump main_interface_label





label gg_room_bita_label:

    '[gg]' "Бейсбольная бита для пробивания человеческих черепов."


    jump main_interface_label








label milf_room_picture_1_label:
    '[gg]' "Картина с обыкновенным пейзажем. "
    jump main_interface_label



label milf_room_picture_2_label:
    '[gg]' "Картина с красивым закатом. "
    jump main_interface_label


label milf_room_table_label:

    '[gg]' "Тумба, на которой стоит светильник. "
    jump main_interface_label


label milf_room_cupboard_label:
    '[gg]' "Куча шмоток на все случаи жизни."
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
