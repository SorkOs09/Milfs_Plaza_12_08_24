label misha_root_5_5:

    $ events.pop('misha_root_5_5', 0)
    $ phone_warning  = True
    $ descript_Misha = _('Прочесть СМС от Мишванды.')
    play sound 'audio/sms.ogg'

    "[gg]" "Новое SMS"
    $ renpy.pause(.5, hard   = True)
    $ Event('misha_root_5_75', 'Corridor', priority = -20)

    $ NPHOTO            = 'cg/misha_root/misha_photo_3_mini.png'


    $ sms_now = SmsBlock('Мишванда', 'misha', "23", Jump('misha_root_6'))
    $ sms_now.add_sms(_("TT: [NPHOTO]"))

    $ sms_now.add_sms(_("TT: Хочу пригласить тебя на чай.\n\n"))
    $ sms_now.add_sms(_("GG: Встретить тебя там же, где и всегда?\n\n"))
    $ sms_now.add_sms(_("TT: Ага."))
    $ sms_now.add_sms(_("GG: Горю от нетерпения."))
    $ sms_now.add_sms(_("TT: Не туши этот пожар, пока мы не увидимся.\n"))
    
    $ phone_warning = True
    jump main_interface_label
label misha_root_5_75:
    
    "[gg]" "Новое СМС от Мишванды... Нужно прочесть его, вдруг там что-то важное"

    $ location_now = "GG_Room"
    $ sms_now = SmsBlock('Мишванда', 'misha', "23", Jump('misha_root_6'))
    $ sms_now.add_sms(_("TT: [NPHOTO]"))

    $ sms_now.add_sms(_("TT: Хочу пригласить тебя на чай.\n\n"))
    $ sms_now.add_sms(_("GG: Встретить тебя там же, где и всегда?\n\n"))
    $ sms_now.add_sms(_("TT: Ага."))
    $ sms_now.add_sms(_("GG: Горю от нетерпения."))
    $ sms_now.add_sms(_("TT: Не туши этот пожар, пока мы не увидимся.\n"))
    
    $ phone_warning = True
    jump main_interface_label

label misha_root_6:




    $ locations['City_Shop'].image_buttons_times['night'] = {'misha':[Jump('misha_root_7')]}




    $ descript_Misha     = _("Встретить Мишванду после работы у магазина ночью.")
    $ events.pop('misha_root_5_5', False)
    $ events.pop('misha_root_5_75', False)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
