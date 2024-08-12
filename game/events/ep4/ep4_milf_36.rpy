label ep4_milf_36:

    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()



    $ descript = _('Дождаться новостей от Игоря. Если за день он так ничего и не напишет, написать ему самому.')
    if getattr(store, 'help_ep5_milf', 0)  < 2:
        $ help_ep5_milf = 2
    $ events.pop('ep4_milf_36', 0)
    
    $ block_igor_position = True
    $ Event('ep4_milf_36_2', None, time = ['evening'])
    $ Event('ep4_milf_36_3', None, 'ep4_milf_36_2', day_start = time.day_now + 7, time = ['morning'])



    jump main_interface_label

label ep4_milf_36_2:
    $ time.time_now = 'evening'
    if location_now  in ['gg_room_bed', 'gg_room_pc']:
        $ location_now = 'GG_Room'
    $ events.pop('ep4_milf_36_2', 0)
    $ events.pop('ep4_milf_36_3', 0)
    $ events.pop('ep4_milf_36', 0)

    $ sms_now = SmsBlock('Игорь', 'igor', "14", Jump('ep4_milf_36_3'))
    $ sms_now.add_sms('GG: Бро, ну как там?')
    $ sms_now.add_sms('GG: ...')


    jump main_interface_label

label ep4_milf_36_3:
    if renpy.get_screen('CardGameScreen'):
        $ Hide('CardGameScreen')()
    $ Hide('main_interface')()

    $ Hide('empty_interface')()

    $ events.pop('ep4_milf_36_2', 0)

    $ events.pop('ep4_milf_36_3', 0)

    call show_all_images_label from _call_show_all_images_label_67
    


    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()

    $ renpy.pause(.5, hard = True)
    show GG Think
    show GG Think:
        ypos 1085

        xalign .5

    with my_dissolve



    "[gg]" " Хм… У него выключен телефон."

    "[gg]" " В такой ответственный момент он просрал зарядное?! Не верю."

    "[gg]" " Проведаю его лично. "

    $ events.pop('night_girl', 0)



    $ descript = _("Встретиться с Игорем в Парке Утром или Днём.")



    $ Event('ep4_milf_37', 'City_Park', time = ['morning', 'afternoon'])


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
