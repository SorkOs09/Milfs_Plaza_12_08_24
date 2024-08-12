
label ep1_3_mother:
    $ events.pop('ep1_3_mother', 0)
    call show_bg_image_label from _call_show_bg_image_label
    call show_additional_images_label from _call_show_additional_images_label
    show Milf Angry
    if location_now == 'Hall' and time.time_now != 'evening':
        show Milf Losi_Angry:
            xalign .85
            ypos 1085
            zoom 1.0-0.035
    elif time.time_now == 'evening':
        show Milf Night_Angry:
            xalign .85
            ypos 1085
            zoom 1.0-0.035
    elif True:
        show Milf Angry:
            xalign .85
            ypos 1085
            zoom 1.0-0.035
    with Dissolve(.5)


    show GG Normal
    show GG Normal at go_from_left

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    $ renpy.pause(1)

    'Марина' "Даже не представляю, что ты можешь сказать в своё оправдание, [gg]!"
    show GG Smile:
        xalign .15
    with my_dissolve
    '[gg]' "Как на счёт «извини, пожалуйста» и «я больше так не буду»?.."
    'Марина' "Если твоей целью является вынудить меня прийти к тебе ночью и придушить, пока ты спишь, то ты практически добился её."
    show GG Surprise
    'Марина' "Мне казалось, ты достаточно хорошо меня знаешь, чтобы понять – словами вину не загладить."
    show GG Chagrin
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_33
    $ renpy.pause(.5, hard = True)

    hide Milf
    with my_dissolve
    $ renpy.pause(.3, hard = True)

    show GG:


        easein .75 xalign .5
    $ renpy.pause(.5, hard = True)

    show GG Think 
    with my_dissolve

    '[gg]' "Марина права. Вместо того, чтобы добиться её расположения, я веду себя как мудак."
  
    show GG:
        xalign .5
    with my_dissolve
    '[gg]' "Надеюсь, моя помощь по дому как-то исправит данное положение."

    $ descript                   = _('Я должен что-то сделать по дому, чтобы она перестала обижаться на меня. Помыть посуду, закинуть бельё в стирку, пропылесосить в Зале.')
    $ unlock_stirka              = True
    $ block_wash_posuda          = False
    $ block_stirka               = False
    $ block_uborka               = False



    $ Event('ep1_3_mother_2', 'Milf')

    $ locations['Restroom'].buttons[0].update({'washer': ((0, 650, 453, 429), [Jump('ep1_3_mother_washer')])})

    $ locations['Hall'].buttons[0].update({'clean_hall': ((1709, 630, 209, 467), [Jump('ep1_3_mother_clean_hall')])})

    $ locations['Kitchen'].buttons[0].update({'sink': ((932, 516, 171, 110), [Jump('ep1_3_mother_clean_kitchen')])})

    $ ep1_3_final_trig = 0





    jump main_interface_label



label ep1_3_mother_clean_kitchen:

    show GG Think
    show GG Think:
        xalign .5
        ypos 1085
        zoom 1.0-0.035
    if time.time_now == 'night':
        '[gg]' "Я слишком устал.. Нужно пойти поспать"



        jump main_interface_label

    if milf_position[time.time_now][0] == location_now:
        '[gg]' "Пока Марина на кухне, у меня не получится помыть посуду. Я буду ей мешать."


        jump main_interface_label
    hide GG
    show expression 'images/cg/gg_activities/gg_wash_kitchen.png'
    with Dissolve(.5)
    '[gg]' "Чёрт, мыть посуду не так уж и просто. Марина должна быть довольна!"
    if hasattr(store, 'ep1_3_final_trig'):
        $ ep1_3_final_trig += 1
    $ locations['Kitchen'].buttons[0].pop('sink', 0)
    $ locations['Kitchen'].buttons[0].update({'clean_kitchen': ((932, 516, 171, 110), [Jump('kitchen_sink_label')])})

    $ block_wash_posuda = True
    if hasattr(store, 'ep1_3_final_trig'):

        call ep1_3_mother_check_final from _call_ep1_3_mother_check_final

    $ time.time_forward()
    with Dissolve(.5)

    $ time.time_forward()
    jump main_interface_label




label ep1_3_mother_clean_hall:



    if time.time_now == 'night':
        show GG Think
        show GG Think:
            xalign .5
            ypos 1085
            zoom 1.0-0.035
        '[gg]' "Я слишком устал.. Нужно пойти поспать"


        jump main_interface_label

    if milf_position[time.time_now][0] == location_now:
        '[gg]' "Я не могу сейчас пылесосить. Марина смотрит телевизор."
        jump main_interface_label


    show expression 'images/cg/gg_activities/gg_clean_hall.png'

    play sound 'audio/vacuum.ogg'
    $ renpy.pause(3, hard = True)


    hide expression 'images/cg/gg_activities/gg_clean_hall.png'


    show GG Think
    show GG Think:
        xalign .5
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    '[gg]' "Теперь этот ковёр должен быть чистым. Надеюсь, Марине это понравится!"


    $ locations['Hall'].buttons[0].update({'clean_hall': ((1709, 630, 209, 467), [Jump('hall_clean_label')])})

    $ block_uborka      = True

    $ ep1_3_final_trig += 1


    call ep1_3_mother_check_final from _call_ep1_3_mother_check_final_1

    $ time.time_forward()
    jump main_interface_label





label ep1_3_mother_washer:
    call check_restroom_block_milf_sister from _call_check_restroom_block_milf_sister



    $ block_stirka = True
    $ gigiena      = max(0,  gigiena-2)
    $ nastroi      = max(0,  nastroi-5)

    show expression 'images/cg/gg_activities/gg_clothes_restroom.png'
    with Dissolve(.5)
    '[gg]' "Постираю вещи, надеюсь это понравится Марине."
    play audio 'audio/rest.ogg'

    $ show_text_animation('+5 milf')

    $ ep1_3_final_trig += 1


    $ locations['Restroom'].buttons[0]['washer'] = ((0, 650, 453, 429), [Jump('restroom_washer_label')])

    call ep1_3_mother_check_final from _call_ep1_3_mother_check_final_2

    $ time.time_forward()

    jump main_interface_label


label ep1_3_mother_2:
    call show_bg_image_label from _call_show_bg_image_label_178
    show Milf Angry
    if location_now == 'Hall' and time.time_now != 'evening':
        show Milf Losi_Angry:
            xalign .85
            ypos 1085
            zoom 1.0-0.035
    elif time.time_now == 'evening':
        show Milf Night_Angry:
            xalign .85
            ypos 1085
            zoom 1.0-0.035
    elif True:
        show Milf Angry:
            xalign .85
            ypos 1085
            zoom 1.0-0.035
    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_left

    $ renpy.pause(1, hard = True)



    'Марина' "Извини, но я всё ещё слишком злюсь на тебя. Поговорим в другой раз."

    $ Event('ep1_3_mother_2', 'Milf')

    jump main_interface_label

label ep1_3_mother_check_final:
    if getattr(store, 'ep1_3_final_trig', 0) >= 3:
        if hasattr(store, 'ep1_3_final_trig'):
            $ del ep1_3_final_trig
        jump ep1_3_final
    return


label ep1_3_final:
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_34
    call show_all_images_label from _call_show_all_images_label_1
    show GG Think
    show GG Think:
        xalign .5
        ypos 1085
        zoom 1.0-0.035
    with my_dissolve
    $ descript = _('Вот и всё, я достаточно потрудился. Следует вновь поговорить с Мариной. Стоит сделать это на кухне или в коридоре.')
    '[gg]' "Вот и всё, я достаточно потрудился. Следует вновь поговорить с Мариной. Стоит сделать это на кухне или в коридоре."

    $ nude = 'morning_nude'

    $ events.pop('ep1_3_mother_2', 0)

    $ block_change_milf_position = True
    $ milf_position = {
        'morning'   : ['Restroom',  'milf_restroom'],
        'afternoon' : ['Kitchen',   'milf_nude_kitchen'],
        'evening'   : ['None',      'milf_evening_hall'],
        'night'     : ['Milf_Room', 'milf_room'],
        }



    $ Event('ep1_4_mother', 'Milf')

    $ time.time_forward()

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
