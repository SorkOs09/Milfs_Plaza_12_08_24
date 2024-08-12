label ep2_8_sms:
    $ check_and_jump('pre_ep3_night_girl')
    $ check_and_jump('ep3_night_girl')
    $ check_and_jump('night_girl')
    $ check_and_jump('talk_with_night_girl')
    
    $ locations['GG_Room'].image_buttons.update({
            'pants': Jump('ep2_8_pants'),

            })
    call show_all_images_label from _call_show_all_images_label_80

    with Dissolve(.5)

    $ events.pop('ep2_8_sms', 0)


    play sound 'audio/sms.ogg'

    $ renpy.pause(.5, hard = True)

    $ descript = _('Я должен проверить СМС от друга.')

    '[gg]' "Я должен проверить СМС от друга."


    $ sms_now = SmsBlock('Игорь', 'igor', "8")

    $ sms_now.add_sms(_('TT: Чувак, приходи сегодня ко мне в парк. \nКое-что обсудим.\n'))
    $ sms_now.add_sms(_('GG: Ты не поверишь, но я сам хотел поговорить с тобой.\n\n'))
    $ sms_now.add_sms(_('TT: Надеюсь, о чём-то, что нам поможет.'))
    $ sms_now.add_sms(_('GG: Разве что тебе…'))
    $ sms_now.add_sms( _('TT: ?'))
    $ sms_now.add_sms(_('GG: Расскажу при встрече.'))
    $ sms_now.add_sms(_('TT: Ок.'))

    $ phone_warning = True


    $ Event('ep2_8_corridor', 'Corridor')

    $ phone_warning = True

    jump main_interface_label

label ep2_8_corridor:
    $ Event('ep2_8_corridor', 'Corridor')
    $ location_now = 'GG_Room'
    '[gg]' "Я не собираюсь бродить по дому без штанов, смущая Марину и Кристи."
    jump main_interface_label

label ep2_8_pants:
    $ locations['GG_Room'].image_buttons.pop('pants', 0)
    $ events.pop('ep2_8_corridor', 0)

    menu:
        "Надеть штаны." if True:
            if 'ep2_8_corridor' in allowed_events:
                $ allowed_events.remove('ep2_8_corridor')
            
            if 'ep2_8_sms' in allowed_events:
                $ allowed_events.remove('ep2_8_sms')
            if 'night_girl' in events:
                if events['night_girl'].day_start == time.day_now:
                    $ events['night_girl'].day_start = time.day_now + 2

            $ descript = _('Обсудить свой план побега с Игорем лично. Каждое утро он работает в парке, выполняя за меня предписание судьи.')

            $ Event('ep2_9_igor', 'Igor')


















    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
