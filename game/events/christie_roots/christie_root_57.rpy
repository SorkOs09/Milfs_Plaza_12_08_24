
label christie_root_57:

    $ finish_event('christie_root_57')
    #Купить продукты.
    #"ext" "Купить «Продукты» в магазине. (120 долларов)"
    show GG Think
    show GG Think:
        xalign .5
    with my_dissolve
    "[gg]" "Всё, этого должно хватить."
    
    "[gg]" "Теперь пора на кухню, готовить!"
    
    #"ext" "//
    #"" "{color=#F00}Mobile_SMS{/color}"
    if 'Сьюзан' not in phone_sms_screen:
        $ phone_sms_screen.update({'Сьюзан' : []})

    $ sms_now = SmsBlock('Сьюзан', 'Susan', "57", Jump('christie_root_57_1'))

    
    $ sms_now.add_sms(_("TT: Мы должны встретиться, [gg]."))
    $ sms_now.add_sms(_('GG: Нет, извините, но я сделал\nвсё, что от меня требовалось.\n'))
    $ sms_now.add_sms(_("TT: Я очень нуждаюсь в тебе.\n"))
    $ sms_now.add_sms(_("GG: Нет."))

    $ location_now = 'StoreIn'
    call show_all_images_label from _call_show_all_images_label_110
    with my_dissolve
    #$ check_ev = True
    $ descript_Christie = __("Прочесть смс.")

    jump talk_with_store_woman_label_menu_2
    
    #jump main_interface_label



label christie_root_57_1:
    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    show GG Think
    show GG Think:
        xalign .5
    with my_dissolve
    "[gg]" "Так и знал, что она не оставит меня в покое!"
    
    "[gg]" "Нужно просто игнорировать её, и она успокоится."
    
    "[gg]" "Это ведь так работает, правда?.."
    
    
    
    $ descript_Christie = __("Приготовить салаты и бутерброды.")

    $ Event("christie_root_58", location = "Kitchen", time = ["morning", "afternoon", "evening"])

    #$ location_now = 'StoreIn'
    call show_all_images_label from _call_show_all_images_label_19
    with my_dissolve
   # $ check_ev = None

    
    jump main_interface_label