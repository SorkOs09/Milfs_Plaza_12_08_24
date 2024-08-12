label ep2_16_sms:
    $ events.pop('ep2_16_sms', 0)

    call show_all_images_label from _call_show_all_images_label_14

    with Dissolve(.5)
    play sound 'audio/sms.ogg'
    $ renpy.pause(.5, hard = True)
    $ descript = _('Я должен проверить СМС от друга.')
    '[gg]' "Я должен проверить СМС от друга."

    $ sms_now = SmsBlock('Игорь', 'igor', "7", Jump('ep2_16_glove'))
    $ sms_now.add_sms(_('TT: Каждый вечер. В парке. \nВ урне, рядом с местом, где я работаю.\n'))
    $ sms_now.add_sms(_('TT: Не забудь перчатки. '))
        
    $ phone_warning = True




    jump main_interface_label



label ep2_16_glove:

    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    show GG Think
    show GG Think:
        xalign .6
        ypos 1085
        zoom 1.0-0.035
    with my_dissolve
    '[gg]' "Перчатки?.."
    '[gg]' "Хорошо, куплю чёртовы перчатки."



    $ Event('talk_with_store_woman_label', 'StoreIn', 'in_store_gloves_ep2_1')

    $ locations['City_Park'].image_buttons.update({'trashbin' : [Jump('ep2_17_trashbin_stump')]})






    $ descript = _('Найти резиновые перчатки')




    $ Event('ep2_16_mother', 'Milf', time = ['afternoon',])


    $ milf_position['afternoon']   = ['Hall',      'milf_hall']



    $ block_change_milf_position_32432423 = copy.deepcopy(block_change_milf_position)
    $ block_change_milf_position = True



    jump main_interface_label
label in_store_gloves_ep2_1:
    $ Event('talk_with_store_woman_label', 'StoreIn')
    $ Event('in_store_gloves_ep2_2', 'City_Shop', time = ['afternoon', 'evening', 'morning'])
    $ location_now = 'StoreIn'
    jump main_interface_label

label in_store_gloves_ep2_2:
    $ events.pop('in_store_gloves_ep2_2', 0)
    $ location_now = 'StoreIn'
    call show_all_images_label from _call_show_all_images_label_15
    show GG Normal
    show GG Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    show GirlInStore Normal
    show GirlInStore Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with my_dissolve
    '[gg]' "Разве у вас нет резиновых перчаток в продаже?"

    'Продавщица' "Закончились, наверное."

    '[gg]' "А когда появятся? "

    'Продавщица' "Без понятия."

    '[gg]' "Завтра будут?"

    'Продавщица' "Я же сказала – не знаю."

    '[gg]' "Окей, спасибо…"

    'Продавщица' "Ага, давай."

    hide GirlInStore
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show GG Think:
        linear .5 xalign .5
    $ renpy.pause(.5, hard = True)
    '[gg]' "Хм, ну и где мне взять резиновые перчатки?"

    $ renpy.play('audio/Door.mp3')
    scene expression '#000' with Dissolve(.5)
    $ JumpToLocation('City_Shop')
    jump main_interface_label

label ep2_16_mother:

    $ Event('talk_with_store_woman_label', 'StoreIn')
    $ events.pop('ep2_16_mother', 0)
    $ events.pop('InStoreGloves_ep2_1', 0)
    $ events.pop('InStoreGloves_ep2_2', 0)

    $ events.pop('in_store_gloves_ep2_1', 0)
    $ events.pop('in_store_gloves_ep2_2', 0)
    call show_bg_image_label from _call_show_bg_image_label_14
    call show_additional_images_label from _call_show_additional_images_label_11
    show expression 'cg/ep2/table_ass_cg.png':
        xalign .5
    with Dissolve(.5)
    '[gg]' "Ого!"
    '[gg]' "Эти лосины так эротично облегают задницу Марины, что я едва сдерживаюсь, чтобы смачно не шлёпнуть её."
    '[gg]' "Супер-задница для супер-шлепка."

    $ block_change_milf_position = False
    call show_bg_image_label from _call_show_bg_image_label_15
    call show_additional_images_label from _call_show_additional_images_label_12

    show GG Normal
    show GG Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035

    show Milf Losi_What
    show Milf Losi_What:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    'Марина' " Ой, я не заметила, как ты вошёл. "
    show GG Laughs
    '[gg]' "Не обращай на меня внимание. Я просто…"
    '[gg]' "О, я вижу на тебе перчатки."
    show Milf Losi_WTF
    'Марина' "Ну да, я в них убираю."
    show GG Normal
    '[gg]' "Могу я попросить тебя одолжить мне их на время?"
    show Milf Losi_Normal
    'Марина' "Конечно. Я как раз заканчивала уже. "
    '[gg]' "Спасибо, ты лучшая!"
    show Milf Losi_Embarrassment
    'Марина' "Как мило."

    $ descript = _('Достать пистолет из мусорки вечером в парке')



    $ block_change_milf_position = False


    show screen give_item_screen(i_path+'/items/gloves.png', _('Перчатки'), [_('Оберегают руки при работе'), _('в хозяйственной сфере и не только.')])

    with Dissolve(.5)
    $ renpy.pause(999999)
    hide screen give_item_screen
    $ add_to_inventory(name = 'Резиновые перчатки')
    $ locations['City_Park'].image_buttons['trashbin'] = [Jump('ep2_17_trashbin')]

    $ block_change_milf_position = copy.deepcopy(block_change_milf_position_32432423)
    $ del block_change_milf_position_32432423


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
