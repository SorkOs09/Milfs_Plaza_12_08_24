label misha_root_3_5:
    
    call show_bg_image_label from _call_show_bg_image_label_174
    $ events.pop('misha_root_3_5', 0)
    $ phone_warning  = True
    $ descript_Misha = _('Прочесть СМС от Мишванды.')
    play sound 'audio/sms.ogg'

    "[gg]" "Новое SMS"
    $ renpy.pause(.5, hard   = True)
    $ Event('misha_root_3_75', 'Corridor', priority = -20)

    $ NPHOTO            = 'cg/misha_root/misha_photo_4_mini.png'



    $ sms_now = SmsBlock('Мишванда', 'misha', "22", Jump('misha_root_4'))
    $ sms_now.add_sms(_("TT: [NPHOTO]"))
    $ sms_now.add_sms(_("TT: Мне становится сложнее справляться со своей жаждой.\n\n"))
    $ sms_now.add_sms(_("GG: Есть ли смысл сопротивляться?\n\n"))
    $ sms_now.add_sms(_("TT: Тебе стоило быть более напористым, если ты хочешь получить желаемое.\n\n"))
    $ sms_now.add_sms(_("GG: Взять тебя силой?"))
    $ sms_now.add_sms(_("TT: Ну ты и дурак…\n"))
    $ sms_now.add_sms(_("TT: Встретишь меня?\n"))
    $ sms_now.add_sms(_("GG: Ага."))
    


    $ phone_warning = True
    jump main_interface_label
label misha_root_3_75:

    "[gg]" "Новое СМС от Мишванды... Нужно прочесть его, вдруг там что-то важное"


    $ sms_now = SmsBlock('Мишванда', 'misha', "22", Jump('misha_root_4'))
    $ sms_now.add_sms(_("TT: [NPHOTO]"))
    $ sms_now.add_sms(_("TT: Мне становится сложнее справляться со своей жаждой.\n\n"))
    $ sms_now.add_sms(_("GG: Есть ли смысл сопротивляться?\n\n"))
    $ sms_now.add_sms(_("TT: Тебе стоило быть более напористым, если ты хочешь получить желаемое.\n\n"))
    $ sms_now.add_sms(_("GG: Взять тебя силой?"))
    $ sms_now.add_sms(_("TT: Ну ты и дурак…\n"))
    $ sms_now.add_sms(_("TT: Встретишь меня?\n"))
    $ sms_now.add_sms(_("GG: Ага."))
    


    $ phone_warning = True
    $ location_now = "GG_Room"
    jump main_interface_label

label misha_root_4:











    $ locations['City_Shop'].image_buttons_times['night'] = {'misha':[Jump('misha_root_5')]}




    $ descript_Misha     = _("Встретить Мишванду после работы у магазина Ночью.")

    $ events.pop('misha_root_3_5', False)
    $ events.pop('misha_root_3_75', False)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
