label misha_root_1_5:
    $ events.pop('misha_root_1_5', 0)
    $ phone_warning  = True
    $ descript_Misha = _('Прочесть СМС от Мишванды.')
    play sound 'audio/sms.ogg'
    if preferences.language in (None, 'rus'):
        "Новое смс"


    $ renpy.pause(.5, hard   = True)
    $ Event('misha_root_1_75', 'Corridor', priority = -20)
    $ NPHOTO            = 'cg/misha_root/misha_photo_1_mini.png'
    $ NPHOTO_2          = 'cg/misha_root/misha_photo_2_mini.png'


    $ sms_now = SmsBlock('Мишванда', 'misha', "21", Jump('misha_root_2'))
    $ sms_now.add_sms(_("TT: [NPHOTO]"))
    $ sms_now.add_sms(_("TT: Если хочешь, можешь провести меня домой снова.\n\n"))
    $ sms_now.add_sms(_("TT: [NPHOTO_2]"))

    $ sms_now.add_sms(_("GG: Это способ мотивации или благодарность?\n\n"))
    $ sms_now.add_sms(_("TT: ^______^"))
    $ sms_now.add_sms(_("TT: Угадай. "))
    $ sms_now.add_sms(_("GG: Я не хочу угадывать, я хочу их потрогать.\n\n"))
    $ sms_now.add_sms(_("TT: Ха-ха-ха-ха-ха!"))
    $ sms_now.add_sms(_("TT: Жду тебя у магазина после девяти.\n\n"))
    

    $ phone_warning = True



    jump main_interface_label
label misha_root_1_75:
    "[gg]" "Новое СМС от Мишванды... Нужно прочесть его, вдруг там что-то важное"
    $ NPHOTO            = 'cg/misha_root/misha_photo_1_mini.png'
    $ NPHOTO_2          = 'cg/misha_root/misha_photo_2_mini.png'

    $ sms_now = SmsBlock('Мишванда', 'misha', "21", Jump('misha_root_2'))
    $ sms_now.add_sms(_("TT: [NPHOTO]"))
    $ sms_now.add_sms(_("TT: Если хочешь, можешь провести меня домой снова.\n\n"))
    $ sms_now.add_sms(_("TT: [NPHOTO_2]"))

    $ sms_now.add_sms(_("GG: Это способ мотивации или благодарность?\n\n"))
    $ sms_now.add_sms(_("TT: ^______^"))
    $ sms_now.add_sms(_("TT: Угадай. "))
    $ sms_now.add_sms(_("GG: Я не хочу угадывать, я хочу их потрогать.\n\n"))
    $ sms_now.add_sms(_("TT: Ха-ха-ха-ха-ха!"))
    $ sms_now.add_sms(_("TT: Жду тебя у магазина после девяти.\n\n"))


    $ phone_warning = True
    $ location_now = "GG_Room"
    jump main_interface_label

label misha_root_2:
    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()



    
    call show_bg_image_label from _call_show_bg_image_label_175



    show GG Think
    show GG Think:
        xalign .5
    with my_dissolve
    if not hasattr(store, 'ACH_4_count'):
        $ ACH_4_count = 0
    $ ACH_4_count+=1
    if ACH_4_count>=3:
        $ add_ach('ACH_4')
    "[gg]" "Эта девчонка играет со мной."
    "[gg]" "Но разве я против?"
    "[gg]" "Посмотрим, во что это выльется."

    $ locations['City_Shop'].image_buttons_times['night'] = {'misha':[Jump('misha_root_3')]}



    $ descript_Misha     = _("Встретить Мишванду после работы у магазина Ночью.")
    $ events.pop('misha_root_1_5', False)
    $ events.pop('misha_root_1_75', False)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
