label tyan_falos_3_debug:
    $ location_now = 'City_Park'
    scene black
    show image Text('DEBUG: Переход к ивенту tyan_falos_3'):
        align (.5, .5)
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call wait_click_label from _call_wait_click_label_47
    call show_bg_image_label from _call_show_bg_image_label_187
label tyan_falos_3:
    hide  screen main_interface
    scene expression 'images/mini_games/search_cleaning_bg.png'
    $ nastroi   = max(0,  nastroi-5)
    with Dissolve(.5)
    $ search_game_ep5_all_items  = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    
    0, 0, 0, 0, 2, 2, 2, 2, 2, 2,

    9, 9, 9, 9, 9, 9, 11, 11, 11, 11,

    11, 11, 11, 11, 11, 1, 1, 1, 7, 7,
    
    
    7, 7, 7, 7, 0, 0, 0, 0, 0, 0,
    17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
    
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
       
        9:  ['Яблоко',  0, 0],

        11: ['Цветок', 0, 0],

        17: ['Лягушка', 0, 0],



        
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
        for i in xrange(min(30, inventory_drugs+search_game_ep5_need_find[2][2])):
            inventory_drugs += 1
            add_to_inventory('Товар', ncopy = True)
        for i in xrange(search_game_ep5_need_find[11][2]):
            add_to_inventory(name = 'Милый цветок', ncopy = True)



        for i in xrange(search_game_ep5_need_find[9][2]):
            add_to_inventory(name = 'Яблоко', ncopy = True)
        tmp_check_flower = get_item('Милый цветок', True)
        if tmp_check_flower and tmp_check_flower.quant >= 7:
            tmp_check_flower.quant = 0
            remove_from_inventory('Милый цветок')
            if not get_item('Букет из милых цветков', True):
                add_to_inventory(name = 'Букет из милых цветков')
            del tmp_check_flower





    if search_game_ep5_need_find[17][2]:
        $ events.pop('tyan_falos_3', 0)
        show GG Think
        with Dissolve(.5)
        "[gg]" "Ага, вот и лягушка."

        $ Event('tyan_falos_4', 'Christie', button_name = _("Лягушка"))
        $ tyan_falos_text = _("Отдать лягушку Кристи, чтобы та выменяла её на линейку-рулетку у «подружки».")     
        $ new_events_christie = True
    $ time.time_now = 'evening'
    jump main_interface_label

