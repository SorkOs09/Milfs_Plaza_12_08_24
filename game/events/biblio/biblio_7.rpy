label biblio_7:
    # Description: Просмотреть книгу на наличие записок.
    # Task: Активировать книгу «Анжелика и Король».

    hide screen bag_interface
    
    call show_bg_image_label
    show GG Think
    show GG Think:
        xalign .15
    with my_dissolve
    
    "[gg]" "Ага, здесь тоже послание на эльфийском."
    "[gg]" "Но теперь я «учёный» и знаю, как всё расшифровывать."
    
    $ events.pop("biblio_7", 0)
    # biblio_8 Запускаем подругому, потому что это кнопка на экране
    $ Event("biblio_8", location = "gg_room_pc_enter")
    
    jump main_interface_label
