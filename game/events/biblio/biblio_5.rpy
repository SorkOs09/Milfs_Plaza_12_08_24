label biblio_5:
    # Description: Расшифровать фразу, воспользовавшись своим рабочим столом.
    # Task: Активировать письменный стол ГГ.
    
    call show_bg_image_label
    show GG Think
    show GG Think at go_from_left(xxalign = .15)
    with my_dissolve
    
    
    # //После успеха мини-игры
    
    "[gg]" "«Если я тебе понравилась, верни мне книгу в пятницу.»"
    "[gg]" "Ну и ну, я мог бы и сам догадаться."

    $ location_now = "GG_Room"
    
    $ events.pop("biblio_5", 0)
    $ Event("biblio_6", location = "City_Library_BiblioGirl", button_name="Вернуть книгу")
    
    jump main_interface_label
