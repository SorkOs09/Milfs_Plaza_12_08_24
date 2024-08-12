label christie_root_10:


    $ events.pop('christie_root_10', 0)

    call show_bg_image_label from _call_show_bg_image_label_120
    call show_additional_images_label from _call_show_additional_images_label_99
    with my_dissolve


























    $ Event('christie_root_10_shower', 'Restroom_shower')

    $ Event('christie_root_10_shower_bath', 'Restroom_bath')

    $ Event('christie_root_10_crane', 'Restroom_crane')

    $ locations['GG_Room'].image_buttons.update({
                'pants_christie_root': Jump('christie_root_10_costume'),

                })
    jump main_interface_label


label christie_root_10_shower:

    show expression 'cg/gg_activities/cg_surv_gg_dush.png'
    with Dissolve(.5)
    $ tmp_christie_root_10_shower = True

label christie_root_10_shower_bath:
    if hasattr(store, 'tmp_christie_root_10_shower'):
        python:
            try:
                del tmp_christie_root_10_shower
            except:
                pass    
    elif True:
        show expression 'cg/gg_activities/cg_surv_gg_vanna.png'
        with Dissolve(.5)

    $ gigiena  = 100

    $ events.pop('christie_root_10_shower_bath', 0)
    $ events.pop('christie_root_10_shower', 0)
    play audio 'audio/water_click.ogg'




    "[gg]" "Задача выполненна. Я чист, свеж и готов к платонической любви!"


    $ show_text_animation('+100 gigiena')
    $ location_now = 'Restroom'

    $ descript_Christie = descript_Christie.replace('Принять душ', '{s}Принять душ{/s}')










    jump main_interface_label

label christie_root_10_crane:
    $ events.pop('christie_root_10_crane', 0)

    show expression 'images/cg/gg_activities/gg_tooth_restroom.png'
    with Dissolve(.5)
    play audio 'audio/water_click.ogg'

    "[gg]" "Блестящая улыбка, приятный запах изо рта, но главное, расположить к себе собеседника. "

    $ descript_Christie = descript_Christie.replace('Почистить зубы', '{s}Почистить зубы{/s}')














    $ location_now = 'Restroom'
    jump main_interface_label
label christie_root_10_costume:
    if events.get("christie_root_10_crane") or events.get('christie_root_10_5') or events.get('christie_root_10_shower'):
        "[gg]" "Ещё рано! Сначала я должен подготовиться."
        jump main_interface_label

    show black with Dissolve(.5)
    $ renpy.pause(1.5, hard = True)

    $ locations['GG_Room'].image_buttons.pop('pants_christie_root', 0)
    call show_bg_image_label from _call_show_bg_image_label_136


    $ remove_from_inventory(name = 'Духи Марины')
    show GG Costume_Normal
    with my_dissolve
    "[gg]" "Что ж, теперь я выгляжу довольно подобающе. "
    show GG Costume_WTF
    "[gg]" "Надо лишь попшикаться духами… "
    show GG Costume_Normal
    "[gg]" "Вот здесь, и здесь, ну и там… на тот случай, если наше общение приобретёт романтический характер. "
    show GG Costume_Normal
    "[gg]" "Ну, всё. Теперь можно идти к продавщице магазина. "

    $ Event('christie_root_11', 'Store_Misha', priority = -1)

    $ descript_Christie= _("Я нашёл, где взять кофе для Кристи, но чтобы получить его, мне надо помочь Зудиле и Бубниле «соблазнить» продавщицу в магазине. Для этого я должен:\n1) {s}Принять душ{/s} \n2) {s}Почистить зубы{/s} \n3) {s}Взять у Марины какие-нибудь духи{/s} \n4) {s}Найти мой старый школьный костюм, чтобы выглядеть презентабельно.{/s}")

    $ location_now = 'GG_Room'

    jump main_interface_label


label christie_root_10_5:

    $ events.pop('christie_root_10_5', 0)

    call show_bg_image_label from _call_show_bg_image_label_43
    call show_additional_images_label from _call_show_additional_images_label_37


    show Milf Normal
    if time.time_now in ['evening', 'night']:
        show Milf Night_Normal:
            xalign .85
            ypos 1085
    elif True:
        show Milf Normal:
            xalign .85
            ypos 1085






    with Dissolve(.5)
    $ add_to_inventory(name = 'Духи Марины')
    show GG Laughs
    show GG Laughs at go_from_left

    $ renpy.pause(1, hard = True)

    "[gg]" "Марина, можно я воспользуюсь твоими духами? "
    
    "Марина" "Зачем? Они ведь женские."
    show GG Embarrassment:
        xalign .15
    "[gg]" "В данный момент это не так принципиально. "

    if time.time_now in ['evening', 'night']:
        show Milf Night_Embarrassment
    elif True:
        show Milf Embarrassment

    "Марина" "Как тебе угодно. "

    "Марина" "Ты что, на свидание собрался?"
    show GG Smile
    "[gg]" "Нет, собираюсь купить кофе для Кристи. "
    if time.time_now in ['evening', 'night']:
        show Milf Night_Surprise
    elif True:
        show Milf Surprise

    "Марина" "Эмм… Окей."
    if time.time_now in ['evening', 'night']:
        show Milf Night_Normal
    elif True:
        show Milf Normal

    "Марина" "Вот, держи мой «пробник». "
    show screen give_item_screen(i_path+'/items/duhi.png', _('Духи Марины'), ["Флакон с приторно-сладким ароматом фиалок"])
    with Dissolve(.75)
    $ renpy.pause(99999)

    hide screen give_item_screen
    show GG Smile
    with my_dissolve
    "[gg]" "Спасибо, ты супер!"

















    $ descript_Christie = descript_Christie.replace('Взять у Марины какие-нибудь духи', '{s}Взять у Марины какие-нибудь духи{/s}')












    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
