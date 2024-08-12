
label ep2_11_sms:
    $ events.pop('ep2_11_sms', 0)

    call show_all_images_label from _call_show_all_images_label_17

    with Dissolve(.5)
    play sound 'audio/sms.ogg'

    '[gg]' "Я должен проверить СМС от друга."
    $ descript = _('Я должен проверить СМС от друга.')

    $ sms_now = SmsBlock('Игорь', 'igor', "5")
    $ sms_now.add_sms(_('TT: Ку-ку, ёпта!\n\n'))
    $ sms_now.add_sms(_('TT: Ты случайно не забыл про деньги?\n\n'))
    $ sms_now.add_sms(_('GG: Нет, скоро переведу.'))
    $ sms_now.add_sms(_('TT: Надеюсь. '))
    $ sms_now.add_sms(_('TT: Не хочу, чтобы мне отбили почки.'))

    $ phone_warning = True

    $ unlock_masturbation_together = True
    $ descript = _('Как только у меня будет 150 долларов, попросить Марину перечислить деньги Игорю. Нужно поговорить с ней на кухне.')


    $ block_change_milf_position = True
    $ milf_position['morning'] = ['Kitchen',   'milf_kitchen']
    $ milf_position['afternoon'] = ['Kitchen',   'milf_kitchen']
    $ Event('ep2_12_milf', 'Kitchen_Milf')
    $ Event('ep2_12_corridor',     'Corridor', time = ['morning', 'afternoon', 'evening'])


    $ unlock_shower_together = True
    $ new_events    = True
    $ help_ep5_milf = 1



    if not hasattr(store, 'allowed_events'):

        $ allowed_events = []

    # $ allowed_events.append('ep2_12_milf')
    
    # $ allowed_events.append('ep2_12_corridor')




    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
