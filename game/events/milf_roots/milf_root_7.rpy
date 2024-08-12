label milf_root_7:



    $ milf_root_1_text = _("Проверить телефон.")
    $ new_events = True
    $ phone_sms_screen_2_tmp = copy.deepcopy(phone_sms_screen)


    $ sms_now = SmsBlock('Марина', 'milf', "20", Jump('milf_root_7_1'))
    $ sms_now.add_sms(_("GG: Марина, ты где?!"))
    $ sms_now.add_sms(_("TT: В парке."))
    $ sms_now.add_sms(_("GG: И что ты там забыла?"))
    $ sms_now.add_sms(_("TT: Тебя так долго не было, \nчто я решила сама тебя поискать.\n" ))
    $ sms_now.add_sms(_("GG: Стой там, где стоишь, я сейчас прибуду."))
    $ sms_now.add_sms(_("TT: Слушаюсь ^_^"))


    $ phone_warning = True




    jump main_interface_label
label milf_root_7_1:


    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()

    $ renpy.music.stop(fadeout=1.5)

    $ milf_root_1_text = _("Отправиться в парк")
    $ new_events = True

    $ Event('milf_root_8', 'City_Park')
    $ block_exit_home    = False
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
