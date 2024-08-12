
screen ep45_milf_54_sms_screen:

    imagebutton:
        idle '#0000'
        hover '#0000'

        action NullAction()


    default sms_two = True

    add 'phone_sms_bg'

    viewport ypos 232 xpos 790:
        ymaximum 64
        xmaximum 240
        add '#0000'
        text _('Марина') outlines [(2, "#000", 0, 0)] xalign .5 yalign .5

    viewport ypos 300 xpos 810:
        xmaximum 100000
        ymaximum 534
        scrollbars 'vertical'
        mousewheel True
        add '#0000'

        vbox yalign .99 ypos 534:
            spacing 10

            hbox:
                vbox:
                    add Crop((0,   0,  320, 40), 'interface/chat.png') xzoom -1
                    viewport:
                        xmaximum 320
                        ymaximum 65
                        add Frame(Crop((0,   40, 320, 100), 'interface/chat.png')) xzoom -1
                        viewport xpos 10:
                            xmaximum 300

                            text '...' yalign .5 color '#000' size 25


                    add Crop((0,   200, 320, 20), 'interface/chat.png') xzoom -1
                add 'interface/phone_interface/SMS_ava_noname.png'
            if sms_two:
                hbox:
                    vbox:
                        add Crop((0,   0,  320, 40), 'interface/chat.png') xzoom -1
                        viewport:
                            xmaximum 320
                            ymaximum 200
                            add Frame(Crop((0,   40, 320, 100), 'interface/chat.png')) xzoom -1
                            hbox xalign .5 yalign .5:
                                text "•" at delayed_blink(0.0, 1.0) style "skip_triangle" color '#000'
                                text "•" at delayed_blink(0.2, 1.0) style "skip_triangle" color '#000'
                                text "•" at delayed_blink(0.4, 1.0) style "skip_triangle" color '#000'

                        add Crop((0,   200, 320, 20), 'interface/chat.png') xzoom -1
                    add 'interface/phone_interface/SMS_ava_noname.png'


            else:
                hbox:
                    vbox:
                        add Crop((0,   0,  320, 40), 'interface/chat.png') xzoom -1
                        viewport:
                            xmaximum 320
                            ymaximum 200
                            add Frame(Crop((0,   40, 320, 100), 'interface/chat.png')) xzoom -1
                            viewport xalign .5:
                                xmaximum 200
                                ymaximum 300
                                add '#000a'
                                add 'cg/ep5/Photo_Milf.png' zoom .5 xpos -400 ypos -115
                                imagebutton:
                                    idle '#0000'
                                    hover '#000a'
                                    action Return()


                        add Crop((0,   200, 320, 20), 'interface/chat.png') xzoom -1
                    add 'interface/phone_interface/SMS_ava_noname.png'

            viewport:
                xmaximum 100
                ymaximum 30
    add 'phone_frame_bg'

    if sms_two:
        imagebutton:
            idle '#0000'
            hover '#0000'
            action SetScreenVariable('sms_two', False)






label ep45_milf_54_city_home:
    $ Hide('main_interface')()
    $ events['ep45_milf_54_city_home'].complete = True

































    scene expression 'images/interface/city_interface/city_bg_'+time.time_now+'.png'

    with Dissolve(.5)






    play sound 'audio/sms.ogg'





    "[gg]" "…."


    show expression '#000a' with Dissolve(.5)
    call screen ep45_milf_54_sms_screen

    show expression 'cg/ep5/Photo_Milf.png'
    with Dissolve(.5)

    $ renpy.pause(99999)




label ep45_milf_54_phone:






    "[gg]" "Провокаторша! Она что, хочет, чтобы меня посадили?!"


    "[gg]" "Держи себя в руках, [gg]!"


    "[gg]" "Её роскошные буфера никуда не денутся, пока я на свободе."

    '[gg]' "Нет...!!!"
    '[gg]' "Это невыносимо!"
    '[gg]' "Я возвращаюсь домой!!!"

    scene expression '#000'

    with Dissolve(.5)
    jump main_interface_label















































label ep45_milf_54_hall:
    $ events['ep45_milf_54_hall'].complete = True


    $ Hide('main_interface')()
    call show_bg_image_label from _call_show_bg_image_label_51
    call show_additional_images_label from _call_show_additional_images_label_45


    show Milf Normal
    show Milf Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_left



    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)



    show Milf Normal
    "Марина" "Да, мой милый?"
    show GG Normal:
        xalign .15
    with my_dissolve
    "[gg]" "Ты меня убедила. "
    show Milf Passion
    "Марина" "Оу, значит сегодня ты принадлежишь только мне. "
    show GG Normal
    "[gg]" "Ага. С чего начнём?"
    show Milf Smile
    "Марина" "С уборки."
    show GG Surprise
    "[gg]" "Чего?!!"
    show GG Skepticism
    "[gg]" "Это шутка?"
    show Milf Smile
    "Марина" "Нет, милый, мне нужна твоя помощь в наведении порядка. "
    show GG Skepticism
    "[gg]" "Но ведь ты сказала, что мы проведём «незабываемый день»."
    show Milf Smile
    "Марина" "Именно. "
    show Milf Laughs
    "Марина" "У нас впереди столько дел, что я уверена, ты этого никогда не забудешь. "
    show GG Angry
    "[gg]" "Это надувательство!"
    show Milf Chagrin
    "Марина" "Ах…"
    show Milf Chagrin
    "Марина" "Значит, ты не хочешь помогать мне, да?.."
    show GG Angry
    "[gg]" "И манипуляция на моих чувствах к тебе!"
    show Milf Normal
    "Марина" "Так ты поможешь или нет?"
    show GG Angry
    "[gg]" "Конечно, помогу! И ты прекрасно это знаешь!"
    show Milf Smile
    "Марина" "Как неожиданно и прияяяяятноооо."
    show GG Embarrassment
    "[gg]" "Форменная издёвка."

    "Марина" "Не огорчайся, мой хороший. Я не потребую от тебя то, с чем ты не справишься."

    "Марина" "Я ценю твою заботу."
    show GG Normal
    "[gg]" "Ладно-ладно. С чего начнём? "
    show Milf Normal
    "Марина" "С поливки растений. "
    show Milf Normal
    "Марина" "Воспользуйся моей лейкой."
    show Milf Normal
    "Марина" "И пожалуйста, будь осторожен. "
    show Milf Normal
    "Марина" "Я очень люблю свою домашнюю растительность, и надеюсь, ты отнесёшься к ним с таким же пиететом, как и ко мне. "
    show GG Laughs
    "[gg]" "Эй, я не стану вылизывать лепестки! "
    show Milf Passion
    "Марина" "Пошляк."
    show GG Smile
    "[gg]" "Давай лейку и я начну. "
    show Milf Normal
    "Марина" "Держи."





    $ add_to_inventory(name = 'Лейка')

    show screen give_item_screen(i_path+'/items/watering_can.png', _('Лейка'), ['Сосуд для', 'поливки растений.'])


    with Dissolve(.5)
    $ renpy.pause(9999)






    # $ locations['Corridor'].buttons[0].update({'ep45_milf_55_korridor': ((1350, 250, 230, 145), [Jump('ep45_milf_55_korridor')])})











    # $ locations['Corridor'].buttons[0].update({'home_plant': ((1401, 581, 176, 110,), [Jump('ep45_milf_55_1')])})

    # $ locations['Hall'].buttons[1]['home_plant_2'] = ((1729, 61, 190, 215),   Jump('ep45_milf_55_2'))

    # $ locations['Hall'].buttons[0]['home_plant_1'] = ((156, 140, 225, 249),   Jump('ep45_milf_55_3'))

    # $ locations['Hall'].buttons[0]['home_plant_3'] = ((636, 450, 105, 181),   Jump('ep45_milf_55_4'))




    $ descript = _("Ну что тебе не понятно, [gg]? Просто полей цветы! ")



    $ locations['City_Park'].image_buttons_times = {
    'morning'   : {'search_game_icon': Jump('search_game_label')},
    'afternoon' : {'search_game_icon': Jump('search_game_label')},
    'evening'   : {},
    'night'     : {},
    }
    hide screen give_item_screen

    $ Event('ep45_milf_55_korridor', 'Corridor', 'ep45_milf_55_korridor')

    $ events.pop('ep45_milf_52_skip', 0)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
