label ep3_milf_17:
    $ events.pop('ep3_milf_17', 0)


    $ locations['Milf_Room'].buttons[0]['picture_2'] = [(425, 0, 175, 235,), [SetVariable('money_boost_label_now', 'milf_room_picture_2_label'), Jump('money_boost_label')]]

    call show_all_images_label from _call_show_all_images_label_27

    show expression 'images/cg/ep3/cg_safe.png'

    with Dissolve(.25)
    show expression '#000a'
    with Dissolve(.25)


    $ ep3_milf_17_menu_array = [0, 0, 0, 0]
label ep3_milf_17_menu:
    if not all(ep3_milf_17_menu_array):

        menu:

            "1. Ввести дату рождения Марины в разных вариациях." if not ep3_milf_17_menu_array[0]:

                $ ep3_milf_17_menu_array[0] = 1

            "2. Ввести свою дату рождения в разных вариациях." if not ep3_milf_17_menu_array[1]:
                $ ep3_milf_17_menu_array[1] = 1

            "3. Ввести дату рождения Кристи в разных вариациях." if not ep3_milf_17_menu_array[2]:
                $ ep3_milf_17_menu_array[2] = 1

            "4. Ввести дату рождения брата в разных вариациях." if not ep3_milf_17_menu_array[3]:

                $ ep3_milf_17_menu_array[3] = 1




        hide expression '#000a'
        with Dissolve(.25)

        "[gg]" "Не подходит."
        show expression '#000a'
        with Dissolve(.25)

        jump ep3_milf_17_menu







    with Dissolve(.5)


    hide expression '#000a'
    with Dissolve(.5)

    if hasattr(store, 'ep3_milf_17_menu_array'):
        $ del ep3_milf_17_menu_array

    "[gg]" "Чёрт, ни один из вариантов не подошёл."
    "[gg]" "Это плохо, очень плохо… "

    $ ShowPhone = Show('phone_interface')

    $ sms_now = SmsBlock('Игорь', 'igor', "11")
    $ sms_now.check = True
    $ sms_now.add_sms(_("GG: Чувак, я перепробовал все варианты. \nЗадание провалено :(\n"))
    $ sms_now.add_sms(_("TT: Хорошо."))
    $ sms_now.add_sms(_("TT: Точнее – ничего хорошего."))
    $ sms_now.add_sms(_("TT: Как будет время, приходи в Парк,\n обсудим дальнейший план действий.\n"))
    $ sms_now.add_sms(_("GG: Извини, бро ("))
    $ sms_now.add_sms(_("TT: Я на тебя не злюсь. "))
    $ sms_now.add_sms(_("TT: бб"))
    $ sms_now.add_sms(_("GG: бб"))

    #$ phone_warning = True

    $ Event('ep3_milf_18', 'Hall')
    $ location_now = 'Milf_Room'
    call show_all_images_label from _call_show_all_images_label_28

    show expression '#000a'
    with Dissolve(.5)
    $ descript = _('Встретиться с Игорем. ')
    #$ set_sms_check(who = 'Игорь')

    $ renpy.call_screen('phone_sms_screen', text_now=sms_now.list, len_text_now = 1, rtrn = True)
label ep3_milf_17_sms_0:
    if hasattr(store, 'ep3_milf_16'):
        $ del ep3_milf_16
    $ block_time_forward = False
    $ block_milf_home    = False
    $ block_sister_home  = False
    $ block_exit_home    = False

    jump main_interface_label
label ep3_milf_17_sms:
    scene expression 'images/cg/Mobile_SMS_Igor.png'
    with Dissolve(.5)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
