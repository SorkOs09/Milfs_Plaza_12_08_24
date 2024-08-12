label christie_root_48:
    #Description: Купить отвёртку в Магазине.
    
    #Купить отвёртку. (30 баксов)

    $ events.pop('christie_root_48', 0)
    show GG Think
    show GG Think:
        xalign .5
    with my_dissolve
    "[gg]" "Отлично, готово. "
    show GG Think
    "[gg]" "Теперь пора заняться кондиционером. "
    
    #Tian_49


    $ Event('christie_root_49', location = 'Hall', need_items = [33,], time = ['night', ])


    $ descript_Christie = _("Вывести из строя кондиционер Ночью, пока никто не видит.")
    jump main_interface_label