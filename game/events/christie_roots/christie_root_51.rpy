label christie_root_51_0:
    
    $ fashion_store_events_items.update({"christie_root_51":[51, ]})

    $ Event("christie_root_51", location = "talk_with_clothes_store_woman_menu_after", need_items = [51, ])
    
    $ descript_Christie = __("Купить любой костюм для ролевых игр.")

    $ christie_root_51_start = True
    #$ tyan_mischief_text = _('Нужно попробовать "Пошалить" с Кристи днём, а не только ночью.')
    #$ tyan_sleep_text = _("Кристи мучают ночные кошмары. Стоит поговорить с ней об этом, может я смогу ей помочь.")
    #$ Event("tyan_sleep_0", location = "Christie", button_name = "Ночные кошмары", time = ["morning", "afternoon", "evening"])
    #$ new_events_christie = True
    #$ Event("tyan_mischief_0", location = "Christie", button_name = "Дневные шалости", time = ["morning", "afternoon", "evening"])

    #Купить любой костюм для ролевых игр.
    #"ext" "Купить «неизвестный» костюм. //в виде коробки, стоимость 125 баксов, продаются в магазине одежды"
    
    return

label christie_root_51:

    $ finish_event('christie_root_51')
    
    show GG Think
    show GG Think:
        xalign .5
    with my_dissolve

    show GG Think
    "[gg]" "Сойдёт, думаю."
    show GG Think
    "[gg]" "Теперь можно поговорить с Кристи."
    
    
    
    $ descript_Christie = __("Отдать костюм Кристи. Сделать это следует Утром или Днём.")


    $ sister_position['morning']  = ['Hall',  'sister_hall']


    $ Event('christie_root_52', 'Christie', button_name = "Отдать костюм", time = ["morning", "afternoon"])


    $ location_now = 'City_Home'
    
    $ renpy.play('audio/Door.mp3')
    scene black with Dissolve(.5)

    jump talk_with_clothes_store_woman_menu