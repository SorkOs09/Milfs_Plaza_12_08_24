
label christie_root_62:
    #Теперь мне нужно уложить приготовленные бутерброды в корзину и можно отправляться на пикник с Кристи. Бутерброды лежат в холодильнике.
    #"ext" "Активировать Холодильник на кухне."
    
    $ _refrigerator_items = []
    $ refrigerator_items = [
    'mini_games/refrigerator/sandwitch.png', 
    'mini_games/refrigerator/sandwitch.png', 
    'mini_games/refrigerator/sandwitch.png', 

    


    ]
    call refrigerator_mini_game_label from _call_refrigerator_mini_game_label
    show GG Think
    show GG Think:
        xalign .5
    with my_dissolve
    "[gg]" "Пришлось, конечно, изрядно уменьшить объёмы блюд..."
    show GG Think
    "[gg]" "В эту крошечную корзину даже бутылку не уместить."
    show GG Think
    "[gg]" "Так или иначе, времени на изменение плана у меня нет."
    show GG Think
    "[gg]" "Я уже пообещал Кристи, что проведу с ней время и больше откладывать нельзя."
    
    
    
    
    $ descript_Christie = __("Поговорить с Кристи о пикнике.")
    $ events.pop('christie_root_62')
    $ Event("christie_root_63", "Christie", button_name = "Пикник")
    $ location_now = "Kitchen"
    if time.time_now == "evening":
        $ sister_position['evening']  = ['Sister_Room',  'sister_room']
    jump main_interface_label