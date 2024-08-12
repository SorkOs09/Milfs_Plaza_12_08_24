
label search_game_ep3_milf_21_label:

    hide  screen main_interface
    scene expression 'images/mini_games/search_cleaning_bg.png'
    $ nastroi   = max(0,  nastroi-5)
    with Dissolve(.5)
    $ search_game_ep5_all_items  = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    
    0, 0, 0, 0, 2, 2, 2, 2, 2, 2,

    9, 9, 9, 9, 9, 9, 11, 11, 11, 11,

    11, 11, 11, 11, 11, 1, 1, 1, 7, 7,
    
    
    7, 7, 7, 7, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
    
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    
    ]







    $ search_game_ep5_arr = []

    python:
        for i in xrange(7):
            search_game_ep5_arr.append([])
            for j in xrange(7):
                tmtmtmtmt = renpy.random.choice(search_game_ep5_all_items)
                search_game_ep5_all_items.remove(tmtmtmtmt)
                search_game_ep5_arr[i].append(tmtmtmtmt)










    $ search_game_ep5_arr_tmp = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    
    ]
    python:
        renpy.random.shuffle(search_game_ep5_arr)
        for i in search_game_ep5_arr:
            renpy.random.shuffle(i)

    $ search_game_ep5_need_find = {
        2:  ['Товар',   0, 0],
        4:  ['Роза', 0, 0],
        9:  ['Яблоко',  0, 0],
        11: ['Цветок', 0, 0],



        
        }

    call screen search_game_ep5
    show screen search_game_ep5
    with None


    hide screen search_game_ep5
    hide screen end_search_game_ep5
    hide screen end_2_search_game_ep5
    hide screen text_animation_sell
    hide screen clean_game_ep5_tmp_list
    hide screen clean_game_ep5_tmp
    with Dissolve(.5)

    python:

        if not hasattr(store, 'inventory_drugs'):
            inventory_drugs = 0
        for i in xrange(min(100, inventory_drugs+search_game_ep5_need_find[2][2])):
            inventory_drugs += 1
            add_to_inventory('Товар', ncopy = True)
        for i in xrange(search_game_ep5_need_find[11][2]):
            add_to_inventory(name = 'Милый цветок', ncopy = True)
        for i in xrange(search_game_ep5_need_find[4][2]):
            
            add_to_inventory(name = 'Роза')

        for i in xrange(search_game_ep5_need_find[9][2]):
            add_to_inventory(name = 'Яблоко', ncopy = True)
        tmp_check_rosa   = get_item('Роза', True)
        tmp_check_flower = get_item('Милый цветок', True)
        if tmp_check_flower and tmp_check_flower.quant >= 7:
            tmp_check_flower.quant = 0
            if not get_item('Букет из милых цветков', True):
                add_to_inventory(name = 'Букет из милых цветков')
            del tmp_check_flower
        if tmp_check_rosa and tmp_check_rosa.quant >= 12:
            tmp_check_rosa.quant = 0
            remove_from_inventory(name = 'Роза')
            
            add_to_inventory(name = 'Букет роз')
            del tmp_check_rosa
            
            locations['City_Park'].image_buttons_times = {
            'morning'   : {'search_game_icon': Jump('search_game_label'),},
            'afternoon' : {'search_game_icon': Jump('search_game_label'),},
            'evening'   : {},
            'night'     : {},
            }
            Event('ep3_milf_21_2',     'JayBob')
            renpy.jump('ep3_milf_21_get_rose')






    $ time.time_now = 'evening'
    jump main_interface_label


label ep3_milf_21_get_rose:


    show screen give_item_screen(i_path+'/items/buket.png', _("Букет роз"), [_("Букет роз"), _("Собранные вместе цветы для подарка.")])

    $ locations['City_Park'].image_buttons_times = {
    'morning'   : {'search_game_icon': Jump('search_game_label')},
    'afternoon' : {'search_game_icon': Jump('search_game_label')},
    'evening'   : {},
    'night'     : {},
    }
    with Dissolve(.5)

    "[gg]" "Всё, я собрал необходимое количество цветов, чтобы из них получился какой-никакой букет. "

    $ time.time_now = 'evening'
    hide screen give_item_screen
    with Dissolve(.5)

    jump main_interface_label



label ep3_milf_21_2:

    $ events.pop('ep3_milf_21_2', 0)


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











    "Зудило" "Молодец, ботаник. Сейчас я прикреплю к букету романтическую открытку, и ты вручишь его продавщице. "
    show GG Normal
    "[gg]" "А сам ты это сделать не можешь?"
    "Зудило" "Слыш, кому билеты нужны, тебе или мне?"
    show GG Skepticism
    "[gg]" "Окей…"

    $ Event('talk_with_store_woman_label', 'StoreIn', 'ep3_milf_22')
    $ descript = _("Вручить букет продавщице.")
    
    $ location_now = 'City_Shop'
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
