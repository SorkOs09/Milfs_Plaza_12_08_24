label biblio_21:
    # Description: Купить женские парики для Зудилы и Бубнилы.
    # Task: Купить женские парики в магазине одежды (60$)
    
    call show_bg_image_label
    show GG Think
    show GG Think at go_from_left(xxalign = .15)
    with my_dissolve
    
    "[gg]" "Пол дела сделано. Теперь надо возвращаться с Зудиле и Бубниле."
    
    $ events.pop("biblio_21", 0)
    $ Event("biblio_22", location = "JayBob")
    
    jump main_interface_label
