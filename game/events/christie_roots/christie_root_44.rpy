label christie_root_44:
    #Description: Купить подарочное издание «Дон Кихот» Мигеля Де Сервантеса.
    #"A Task" ""
    #Купить книгу в Магазине (150 долларов)

    #"Scene" ""
    $ events.pop('christie_root_44', 0)
    show GG Think
    "[gg]" "Замечательная вёрстка. Кристи будет в восторге. "
    
    #Tian_45
    $ descript_Christie = _("Подарить Кристи книгу «Дона Кихот» Мигеля Де Сервантеса.")
    

    $ Event('christie_root_45', location = 'Christie', need_items = [22,])

    
    jump main_interface_label