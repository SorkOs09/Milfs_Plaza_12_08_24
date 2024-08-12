label biblio_4:
    # Description: Дать Кристи время, прежде чем она разберётся с переводом.
    # Task: Ждать 2 дня и оказаться в любой комнате Утром, Днём или Вечером, кроме собственной Комнаты.
    
    call show_bg_image_label
    show GG Smile
    show GG Smile at go_from_left(xxalign = .15)
    show Christie Normal
    show Christie Normal:
        xalign .85
    with my_dissolve
    
    "Кристи" "Всё готово, [gg]!"
    "[gg]" "Ты смогла перевести фразу?"
    "Кристи" "Слушай, при всём уважении, я не могу делать за тебя всю работу."
    show GG Chagrin with my_dissolve
    "Кристи" "Я составила правила и сделала выписку всех словосочетаний, которые тебе пригодятся для перевода фразы."
    "Кристи" "Просто воспользуйся моими наработками и ты легко расшифруешь текст."
    show GG Normal with my_dissolve
    "[gg]" "Хорошо-хорошо. Ты и так сильно меня выручила."

    hide Christie with my_dissolve
    
    show screen give_item_screen(i_path+'items/ticket.png', _('Правила Синдарина'), _('Вся необходимая информация для расшифровки.'))
    $ add_to_inventory('Правила Синдарина')
    pause
    hide screen give_item_screen

    hide GG with my_dissolve
    show GG Think with my_dissolve
    "[gg]" "Чёрт, я надеялся избежать гемороя..."
    "[gg]" "Всё таки Игорь ошибался, и мой интеллект, хочу я этого или нет, таки пройдёт вынужденную проверку."
    
    $ events.pop("biblio_4", 0)
    $ Event("biblio_5", location = "gg_room_pc_enter")
    
    jump main_interface_label
