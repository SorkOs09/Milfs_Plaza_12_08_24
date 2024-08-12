label biblio_8:
    # Description: Расшифровать новое послание, воспользовавшись своим рабочим столом.
    # Task: Активировать письменный стол ГГ.
    
    call show_bg_image_label
    show GG Think
    show GG Think at go_from_left(xxalign = .15)
    with my_dissolve
    
    
    # //После успеха мини-игры
    
    "[gg]" "«Я люблю ландыши.»"
    "[gg]" "Что ж, меня дважды просить не надо. Намёк понял!"
    "[gg]" "Нужно найти ландыши и подарить их Нэнси."
    "[gg]" "Правда, сейчас совсем не подходящая пара. Вряд ли я найду их в парке..."

    $ location_now = "GG_Room"
    
    $ events.pop("biblio_8", 0)
    $ Event("biblio_9", location = "JayBob")
    
    jump main_interface_label
