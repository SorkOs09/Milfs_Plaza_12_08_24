

label ep5_milf_68:





    call show_bg_image_label from _call_show_bg_image_label_60
    call show_additional_images_label from _call_show_additional_images_label_54
    show Milf Normal
    show Milf Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left
    $ renpy.pause(.5)
    show Milf Normal
    "Марина" "Ну как, уже пора приглашать офицера полиции на ужин? "

    menu:
        "Да." if True:
            $ pass
        "Нет." if True:

            show Milf Normal
            show GG:
                xalign .15
            with my_dissolve
            "Марина" "Буду ждать."
            call show_all_images_label from _call_show_all_images_label_82
            with Dissolve(.5)
            jump talk_with_milf_label


    $ events.pop('ep5_milf_68', 0)

    show Milf Normal
    show GG:
        xalign .15
    with my_dissolve
    "Марина" "Хорошо, сейчас же займусь за готовку."
    show GG Smile
    "[gg]" "Только сильно не старайся, хе-хе."
    show Milf Smile
    "Марина" "Яйца курицу не учат."
    show GG Surprise
    "[gg]" "Минуточку!"
    show Milf Laughs
    "Марина" "Ха-ха-ха!"

    show Milf Laughs:
        xzoom -1
        linear 1 xalign 1.5
    $ renpy.pause(.7, hard = True)
    $ renpy.pause(9999)
    hide Milf
    show GG Think:
        linear .5 xalign .5

    "[gg]" "Так-с! "
    #show GG Think
    "[gg]" "Первую половину плана я реализовал."
    #show GG Think
    "[gg]" "Пора спасать Игоря!"


    play sound 'audio/sms.ogg'
    $ renpy.pause(.5, hard = True)
    $ descript = _('Я должен проверить СМС от друга.')

    '[gg]' "Я должен проверить СМС от друга."

    $ sms_now = SmsBlock('Кэт', 'kat', "16", Jump('ep5_milf_68_after_sms'))
    $ sms_now.add_sms(_('TT: Я устала ждать.'))

    $ sms_now.add_sms(_('GG: Ты вовремя, я как раз готов.'))
    $ sms_now.add_sms(_('TT: Тогда каков план?'))
    $ sms_now.add_sms(_('GG: Люди Жлоба нас хорошо знают.\nСперва нам нужно добыть маскировку.\n\n'))
    $ sms_now.add_sms(_('TT: ???'))
    $ sms_now.add_sms(_('GG: Я куплю нам пару подходящим костюмов, чтобы нас не заметили.\n\n '))
    $ sms_now.add_sms(_('TT: Звучит бредово, но хозяин-барин.\n\n'))
    $ sms_now.add_sms(_('TT: Как мы проникнем внутрь?'))
    $ sms_now.add_sms(_('GG: Расскажу на месте.'))
    $ sms_now.add_sms(_('TT: Мы идём на смертельную миссию,\nа о плане я смогу узнать только за минуту до начала?!\n\n'))
    $ sms_now.add_sms(_('GG: Ты уже согласилась мне помочь,\nа я согласился на твои условия.\n\n'))
    $ sms_now.add_sms(_('TT: …'))
    $ sms_now.add_sms(_('GG: До связи.'))
    $ sms_now.add_sms(_('TT: Оривидерчи.'))

    $ phone_warning = True


    jump main_interface_label
label ep5_milf_68_after_sms:




    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()


    $ descript = _('Купить два костюма: себе и Кэт.')
    $ storein_costumes_shop_items = ['Костюм 1', 'Костюм 2']

    $ events.pop('talk_with_clothes_store_woman_menu', 0)
    $ Event('ep5_milf_68_0', 'ClothesStore')

    $ Location('ClothesStore',
            buttons       = [],
            image_buttons = {
            }
            )
    jump main_interface_label
label ep5_milf_68_0:
    $ events.pop('ep5_milf_68_0', 0)
    $ Event('talk_with_clothes_store_woman_menu', 'ClothesStore')
    #"!" "!"
    $ Event('ep5_milf_68_2', 'City_Home')

    $ location_now = 'ClothesStore'
    jump talk_with_clothes_store_woman_menu

label ep5_milf_68_2:

    $ location_now = 'City_Home'
    $ renpy.play('audio/Door.mp3')
    scene expression '#000' with Dissolve(.5)
    $ events.pop('ep5_milf_68_2', 0)
    if get_item('Костюм 1', True, True) and get_item('Костюм 2', True, True):

        $ pass
    elif True:
        $ location_now = 'City_Home'
        $ events.pop('talk_with_clothes_store_woman_menu', 0)
        $ Event('ep5_milf_68_0', 'ClothesStore')


        $ JumpToLocation('City_Home')
        jump main_interface_label
    $ events.pop('ep5_milf_68_0', 0)
    call show_all_images_label from _call_show_all_images_label_83
    with Dissolve(.5)

    play sound 'audio/sms.ogg'
    $ renpy.pause(.5, hard = True)
    $ descript = _('Я должен проверить СМС от друга.')

    '[gg]' "Я должен проверить СМС от друга."


    $ sms_now = SmsBlock('Кэт', 'kat', "17", Jump('ep5_milf_68_sms'))

    $ sms_now.add_sms(_('GG: Время пришло, детка.'))
    $ sms_now.add_sms(_('TT: Я тебе не детка.'))
    $ sms_now.add_sms(_('GG: Ладно, сумасшедшая бандитка со сбитыми морально-нравственными ориентирами.\n\n'))
    $ sms_now.add_sms(_('TT: Зарежу, падлу!'))
    $ sms_now.add_sms(_('GG: Главное явись.\n '))
    $ sms_now.add_sms(_('TT: >_<\n'))
    
    #$ phone_sms_screen['Кэт']['Check'] = False
    
    $ phone_warning = True
    jump main_interface_label
label ep5_milf_68_sms:


    $ descript = _("Дождаться Кэт у себя в комнате.")

    $ Event('ep5_milf_69', 'GG_Room', time = ['evening', 'night'])
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
