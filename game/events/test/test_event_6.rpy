label hide_phone_sms:
    python:
        renpy.hide_screen("phone_sms_screen")
        renpy.hide_screen("phone_contacts_screen")
        renpy.hide_screen("phone_interface")

    return

label test_event_6:
    python:
        sms_now = SmsBlock("Офицер", "officer", "test_event_6", Jump("test_event_6_end"))
        
        sms_now.add_sms(_('TT: Чувак, ну как ты там? Обошлось?')) # Продублировала существующие
        sms_now.add_sms(_('GG: Дали пару недель общественных работ.'))
        sms_now.add_sms(_('TT: Хреново.'))
        sms_now.add_sms(_('TT: А я теюе говорил, надо было через переулок гнать!\n\n'))
        sms_now.add_sms(_('GG: Уже не важно. Лучше скажи, тебе удалось что-нибудь стащить?\n\n'))
        sms_now.add_sms(_('TT: Не, извини...'))
        sms_now.add_sms(_('GG: Отлично. Долг общий, а выкручиваться одному мне?\n\n'))
        sms_now.add_sms(_('TT: Могв вместо тебя дворы мести.'))
        sms_now.add_sms(_('GG: Согласен.'))
        sms_now.add_sms(_('TT: А что по деньгам? придумал, где достать?'))
        sms_now.add_sms(_('GG: Придержи коней! Ничего еще не думал. Давай, до связи.\n\n'))
        sms_now.add_sms(_('TT: ББ'))

        phone_warning = True
        events.pop("test_event_6", 0)
    
    jump main_interface_label

label test_event_6_end:
    $ Event("test_event_7", location = "Milf", day_start=time.day_now+1, button_name = "Нижние пупки")
    call hide_phone_sms from _call_hide_phone_sms
    "Тестируем завершение смссок"
    jump main_interface_label


label test_event_7:

    call show_bg_image_label from _call_show_bg_image_label_249
    show Milf Normal
    show Milf Normal:
        reflect
        xalign .15
        ypos 1085
    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_right, reflect

    "Марина" "Поехали в Нижние Пупки!"

    show screen give_item_screen(i_path+'items/ticket.png', _('Еще билет'), _('Билет в Нижние Пупки.'))
    "ПРЕДМЕТЫ ВЫДАНЫ"
    hide screen give_item_screen


    "Марина" "Теперь иди возьми сумку для поездки!"

    $ locations['GG_Room'].image_buttons["bag"] = Jump("test_event_8")

    jump main_interface_label

screen qte_test_game(): #TODO вызываю через консоль пока что (call screen qte_test_game)

    modal True

    default time_left = 10

    default arrows = [renpy.random.choice(("LEFT", "RIGHT", "UP", "DOWN")) for i in range(10)]
    default current_arrow = 0

    if time_left <= 0:
        textbutton "Вы проиграли!" align (0.5, 0.5) text_color "#F00" text_size 70 action Return(False)
    elif current_arrow >= len(arrows):
        textbutton "Вы победили!" align (0.5, 0.5) text_color "#0F0" text_size 70 action Return(True)
    else:
        timer .01 action SetScreenVariable("time_left", time_left-.01) repeat True
        key "K_"+arrows[current_arrow] action SetScreenVariable("current_arrow", current_arrow+1)
        vbox:
            spacing 20
            xalign 0.5
            ypos 300
            bar value AnimatedValue(time_left, 10.0, .01, time_left+.01) xsize 900 xalign .5

            hbox:
                spacing 5
                xalign .5
                for i, a in enumerate(arrows):

                    add "images/interface/key_%s.png"%a[0].lower():
                        zoom 0.5
                        if i < current_arrow:
                            alpha .7
                            
