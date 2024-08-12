label christie_root_35:


    $ events.pop('christie_root_31_0', 0)
    # if getattr(store, 'block_igor_position', False):
    #     if 'christie_root_31' in events:
    #         $ events.pop('christie_root_31', 0)
   
    #     $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")

        
    #     $ events['christie_root_35'].day_start = time.day_now + 1
    #     jump main_interface_label
    #$ descript_Christie = _("Проверить телефон.")
    $ events.pop('christie_root_31', 0)
    #$ Event('christie_root_35_1', 'Corridor')

    $ sms_now = SmsBlock('Игорь', 'igor', "christie_root_35", Jump('christie_root_35_2'))

    $ sms_now.add_sms(_("TT: Глянул фотку."))
    $ sms_now.add_sms(_("TT: 12 из 10!!!"))
    $ sms_now.add_sms(_("GG: Знаю, бро! \nВедь я это видел собственными глазами.\n"))

    $ sms_now.add_sms(_("TT: Ах ты ж сука, \nрешил поиздеваться надо мной?!\n"))
    $ sms_now.add_sms(_("GG: Всего лишь факт.\n"))
    $ sms_now.add_sms(_("GG: Как, по твоему, \nя бы сделал эту фотку?"))
    $ sms_now.add_sms(_("TT: Пока что я слишком впечатлён красотой богини, \nи твои комментарии тут излишне. \n\n"))
    $ sms_now.add_sms(_("GG: Ну ладно. Удачного дня.\n"))
    $ sms_now.add_sms(_("TT: И тебе не горевать.\n"))

    $ events.pop('christie_root_35_1', 0)
   
    $ phone_warning = True
    $ events.pop('christie_root_35_1', 0)
    $ descript_Christie= _("Отправиться на слежку. Лучше всего начать это делать с самого утра, начав с дома Сьюзен.")
    $ Event('christie_root_36', 'City_Psi', time = ['morning', 'afternoon'])


    jump main_interface_label

label christie_root_35_1:
    $ location_now = "GG_Room"
    "[gg]" "Мне надо проверить телефон, вдруг там что-то важное."
    jump main_interface_label


label christie_root_35_2:

    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()
    $ events.pop('christie_root_35_1', 0)


    
    call christie_root_try_to_del_descript_christie_block_igor from _call_christie_root_try_to_del_descript_christie_block_igor
    
    
    $ unlock_city_psi   = True
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
