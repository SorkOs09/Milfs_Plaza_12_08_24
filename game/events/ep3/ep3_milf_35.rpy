label ep3_milf_35:

    $ events.pop('ep3_milf_35', 0)

    $ descript = _("Написать Игорю СМС.")

    call show_all_images_label from _call_show_all_images_label_42
    with Dissolve(.5)



    $ sms_now = SmsBlock('Игорь', 'igor', "13", Jump('ep4_milf_36'))
    $ sms_now.add_sms(_('GG: Ну?!'))
    $ sms_now.add_sms(_('TT: Чувак, деньги у меня.'))
    $ sms_now.add_sms(_('GG: Шикарно. \nСколько там?'))
    $ sms_now.add_sms(_('TT: Дохренища. \n '))
    $ sms_now.add_sms(_('TT: Я взял только необходимое.'))
    $ sms_now.add_sms(_('GG: Когда пойдём к Жлобу?\n'))
    $ sms_now.add_sms(_('TT: Сам схожу. \nТы и так хорошо «поработал».\n'))
    $ sms_now.add_sms(_('GG: Что ты имеешь в виду? '))
    $ sms_now.add_sms(_('TT: Ничего. \nЯ сам схожу к Жлобу. \nНечего нам двоим рисковать.'))
    $ sms_now.add_sms(_('TT: Как только вернусь, напишу.\n\n'))
    $ sms_now.add_sms(_('GG: Окей. Буду ждать.'))

    $ phone_warning = True

    jump main_interface_label
label end_of_game:

    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()
    $ Hide('main_interface')()
    scene black
    with Dissolve(.5)

    "[gg]" "Конец эпизода"







    $ descript           = 'Конец эпизода 4.5'

    $ block_exit_home    = False

    $ block_time_forward = False

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
