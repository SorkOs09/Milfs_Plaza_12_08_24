label ep3_3_pictures:


    scene expression '#000'
    show expression 'cg/ep3/cg_safe.png'
    with Dissolve(.5)
    '[gg]' "Так я и думал. Скрытый сейф за картиной."
    '[gg]' "Теперь мне нужен пароль от сейфа, но я понятия не имею, как его разузнать. Надо спросить у Игоря, он мозг в нашей команде недотёп. Напишу ему завтра с утра."


    $ sms_now = SmsBlock('Игорь', 'igor', "9", Jump('ep3_3_after_phone'))
    $ sms_now.add_sms(_('GG: Ку, бро!'))
    $ sms_now.add_sms(_('TT: И тебе того же.'))
    $ sms_now.add_sms(_('GG: Слушай, у меня к тебе крайне важное дело.'))
    $ sms_now.add_sms(_('TT: Ну-ну…'))
    $ sms_now.add_sms(_('GG: Кажется, я нашёл способ \nрасплатиться с нашим долгом!\n'))
    $ sms_now.add_sms(_('TT: Хочешь завалить Жлоба? :D'))
    $ sms_now.add_sms(_('GG: Никакого криминала. Ну… почти никакого.'))
    $ sms_now.add_sms(_('TT: Чувак, \nэто по-любому какая-то херня. \nНо так уж и быть, я выслушаю.\n'))
    $ sms_now.add_sms(_('TT: Приходи днём в парк, пообщаемся лично. \nПока ты прохлаждаешься, \nя вкалываю как Папо Карло.\n\n'))
    $ sms_now.add_sms(_('GG: Или как «Раб на галерах».'))
    $ sms_now.add_sms(_('TT: Иди нахуй.'))
    $ sms_now.add_sms(_('GG: Ладно, жди. Приду. '))
    $ sms_now.add_sms(_('TT: бб'))

    $ phone_warning = True

    $ descript = _('Теперь мне нужен пароль от сейфа, но я понятия не имею, как его разузнать. Надо спросить у Игоря, он мозг в нашей команде недотёп. Напишу ему завтра с утра.')

    $ locations['Milf_Room'].buttons[0].pop('pictures', 0)

    python:
        for i in [
        ((75, 0, 210, 255,), 'picture_1'),
        ((425, 0, 175, 235,), 'picture_2'),
        ((740, 395, 275, 200,), 'table'),
        ((1200, 0, 650, 900,), 'cupboard'),
       
        ]:
            locations['Milf_Room'].buttons[0].update({i[1]: [i[0], [SetVariable('money_boost_label_now', 'milf_room_'+i[1]+'_label'), Jump('money_boost_label')]]})


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
