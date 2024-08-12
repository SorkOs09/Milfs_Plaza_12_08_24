
label milf_root_4:


    $ events.pop('milf_root_4', 0)
    play sound 'audio/sms.ogg'
    $ milf_root_1_text = _("Проверить телефон.")

    $ new_events = True

    $ NPHOTO            = 'cg/milf_root/plg_photo_mini.png'
    if not hasattr(store, 'ACH_4_count'):
        $ ACH_4_count = 0
    $ ACH_4_count+=1
    if ACH_4_count>=3:
        $ add_ach('ACH_4')
    #$ phone_sms_screen_2_tmp = copy.deepcopy(phone_sms_screen)

    $ sms_now = SmsBlock('Марина', 'milf', "19", Jump('milf_root_4_1'))
    $ sms_now.add_sms(_("TT: Ты скоро вернёшься?"))
    $ sms_now.add_sms(_("GG: А что?"))
    $ sms_now.add_sms(_("TT: T__________________T"))
    $ sms_now.add_sms(_("GG: Бедняжка, ты так страдаешь." ))
    $ sms_now.add_sms(_("TT: ^/////////^"))
    $ sms_now.add_sms(_("GG: Ты хочешь меня, да?"))
    $ sms_now.add_sms(_("TT: Хочу твой 8=========D"))
    $ sms_now.add_sms(_("GG: Как сильно?"))
    $ sms_now.add_sms(_("TT: [NPHOTO]"))
    $ sms_now.add_sms(_("GG: Теперь верю."))
    $ sms_now.add_sms(_("GG: Вернусь как вернусь."))
    $ sms_now.add_sms(_("TT: L((((((("))

    $ phone_warning = True


    jump main_interface_label
label milf_root_4_1:
    #$ phone_sms_screen = copy.deepcopy(phone_sms_screen_2_tmp)
    


    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()

    $ renpy.music.stop(fadeout=1.5)
    $ milf_root_1_text = _("Марина уже на грани. Пожалуй, мне стоит ещё раз прогуляться и вернуться домой поздно ночью, прежде чем я позволю ей вынуть анальную пробку. ")
    $ Event('milf_root_4_2', 'City_Home', time = ['evening', 'night'])


    $ new_events = True


    jump main_interface_label

label milf_root_4_2:
    $ events.pop('milf_root_4_2', 0)

    $ Event('milf_root_5', 'Corridor')
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
