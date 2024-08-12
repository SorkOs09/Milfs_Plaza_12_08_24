label christie_root_31:

    # if getattr(store, 'block_igor_position', False):

    #     $ descript_Christie = _("Проверить телефон.")

    #     $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")

    #     $ events['christie_root_31'].day_start = time.day_now + 1
    #     jump main_interface_label

    $ descript_Christie = _("Проверить телефон.")

    $ events.pop('christie_root_31', 0)
    $ Event('christie_root_31_0', 'Corridor')

    $ sms_now = SmsBlock('Игорь', 'igor', "2", Jump('christie_root_31_2'))

    
    $ sms_now.add_sms(_("TT: Ну и где, мать твою, фотка с Кристи?!!!\n"))

    $ sms_now.add_sms(_("GG: Бля, я забыл……….\n"))
    
    $ sms_now.add_sms(_("TT: Ещё бы! Легко забыть об обещании после того, \nкак твой друг сделал для тебя доброе дело!\n"))
    $ sms_now.add_sms(_("GG: Бро, всё будет. \nТолько не злись.\n"))
    $ sms_now.add_sms(_("TT: Я буду злиться столько, \nсколько посчитаю нужным.\n"))
    $ sms_now.add_sms(_("TT: И пока ты не вышлешь мне фотку с Кристи, \nты исключён из списка лучших друзей!\n"))
    $ sms_now.add_sms(_("GG: Но я твой единственный друг, ау…\n"))
    $ sms_now.add_sms(_("TT: Тем более!\n"))
    $ sms_now.add_sms(_("TT: Шли фотку и не беси меня!\n"))
    $ sms_now.add_sms(_("GG: Харош бузить. Я всё обязательно вышлю.\n"))
    $ sms_now.add_sms(_("GG: Она же не гуляет \nголой по дому и не устраивает стриптиз показы по вечерам. \n"))
    $ sms_now.add_sms(_("GG: Подожди ещё немного, окей?\n"))
    $ sms_now.add_sms(_("TT: …….\n"))
    $ sms_now.add_sms(_("TT: Активирую режим «Хатико».\n"))
    $ sms_now.add_sms(_("GG: Ыыыыыыыы!\n"))
    $ phone_warning = True



    $ events.pop('christie_root_31_0', 0)
    $ events.pop('christie_root_31', 0)



    
    #if 'christie_root_32' not in completed_events:
    $ descript_Christie = _("Поговорить со Сьюзен по поводу работы.")



    jump main_interface_label

label christie_root_31_0:
    $ location_now = "GG_Room"
    "[gg]" "Мне надо проверить телефон, вдруг там что-то важное."
    jump main_interface_label


label christie_root_31_2:
    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()










    # $ events.pop('christie_root_31_0', 0)
    # $ events.pop('christie_root_31', 0)



    
    # if 'christie_root_32' not in completed_events:
    #     $ descript_Christie= _("Поговорить со Сьюзен по поводу работы.")


    
    call christie_root_try_to_del_descript_christie_block_igor from _call_christie_root_try_to_del_descript_christie_block_igor_5
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
