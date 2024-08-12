label ep45_milf_52_skip:
    $ Hide('main_interface')()
    $ Hide('main_city_screen')()

    call show_bg_image_label from _call_show_bg_image_label_40
    call show_additional_images_label from _call_show_additional_images_label_34
    with Dissolve(.5)

    show GG Normal
    show GG Think:
        xalign .5
        ypos 1085
        zoom 1.0-0.035

    with Dissolve(.5)
    "[gg]" "Если я и дальше продолжу прогуливать уборку в Парке, это может закончиться для меня крайне плачевно. "

    $ locations['City_Park'].image_buttons_times = {
    'morning'   : {'search_game_icon': Jump('search_game_label'), 'clean_game_icon':  Jump('ep45_milf_52_2')},
    'afternoon' : {'search_game_icon': Jump('search_game_label'), 'clean_game_icon':  Jump('ep45_milf_52_2')},
    'evening'   : {},
    'night'     : {},
    }
    $ Event('ep45_milf_52_skip', None,    'ep45_milf_52_skip', day_start = time.day_now + 1, time = ['evening', 'night'])

    jump main_interface_label

label ep45_milf_52_2:
    with Dissolve(.5)




    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085
        zoom 1.0-0.035
    show GG Normal
    with Dissolve(.5)


















    show GG Normal
    "[gg]" "Чёрт, я уже ненавижу эту работу. "








    scene expression '#000' with Dissolve(.75)
    $ renpy.pause(.1, hard = True)
    $ renpy.pause(.4)
    scene expression 'images/mini_games/search_cleaning_bg.png'

    with Dissolve(.5)
    $ clean_game_ep5_arr = [
        CleaningLeafEp5(0, 0,    'l_1'), 
        CleaningLeafEp5(100, 0,  'l_2'),
        CleaningLeafEp5(300, 0,  'l_3'), 
        CleaningLeafEp5(400, 0,  'l_4'), 
        CleaningLeafEp5(500, 0,  'l_5'), 
        CleaningLeafEp5(600, 0,  'l_6'),
        CleaningLeafEp5(600, 0,  'l_1'),
        CleaningLeafEp5(700, 0,  'l_4'),
        CleaningLeafEp5(800, 0,  'l_3'),
        CleaningLeafEp5(900, 0,  'l_2'),
        
        CleaningLeafEp5(1000, 0,  'l_1'),
        CleaningLeafEp5(1100, 0,  'l_2'),
        CleaningLeafEp5(1200, 0,  'l_3'),
        CleaningLeafEp5(1100, 0,  'l_4'),
        CleaningLeafEp5(1200, 0,  'l_5'),
        CleaningLeafEp5(1200, 0,  'l_6'),

CleaningLeafEp5(0, 100,    'l_1'), 
        CleaningLeafEp5(100, 100,  'l_2'),
        CleaningLeafEp5(300, 100,  'l_3'), 
        CleaningLeafEp5(400, 100,  'l_4'), 
        CleaningLeafEp5(500, 100,  'l_5'), 
        CleaningLeafEp5(600, 100,  'l_6'),
        CleaningLeafEp5(600, 100,  'l_1'),
        CleaningLeafEp5(700, 100,  'l_6'),
        CleaningLeafEp5(800, 100,  'l_3'),
        CleaningLeafEp5(900, 100,  'l_4'),
        
        CleaningLeafEp5(1000, 100,  'l_1'),
        CleaningLeafEp5(1100, 100,  'l_5'),
        CleaningLeafEp5(1200, 100,  'l_2'),
        CleaningLeafEp5(1300, 100,  'l_5'),
        CleaningLeafEp5(1200, 100,  'l_4'),
        CleaningLeafEp5(1400, 100,  'l_2'),


        CleaningLeafEp5(0, 200,    'l_1'), 
        CleaningLeafEp5(100, 200,  'l_5'),
        CleaningLeafEp5(300, 200,  'l_3'), 
        CleaningLeafEp5(400, 200,  'l_4'), 
        CleaningLeafEp5(500, 200,  'l_5'), 
        CleaningLeafEp5(600, 200,  'l_6'),
        CleaningLeafEp5(600, 200,  'l_5'),
        CleaningLeafEp5(700, 200,  'l_4'),
        CleaningLeafEp5(800, 200,  'l_3'),
        CleaningLeafEp5(900, 200,  'l_2'),
        
        CleaningLeafEp5(1000, 200,  'l_1'),
        CleaningLeafEp5(1100, 200,  'l_6'),
        CleaningLeafEp5(1100, 200,  'l_5'),
        CleaningLeafEp5(850, 200,  'l_4'),
        CleaningLeafEp5(900, 200,  'l_3'),
        CleaningLeafEp5(1400, 200,  'l_2'),


        CleaningLeafEp5(0, 300,    'l_1'), 
        CleaningLeafEp5(100, 300,  'l_2'),
        CleaningLeafEp5(300, 300,  'l_3'), 
        CleaningLeafEp5(400, 300,  'l_4'), 
        CleaningLeafEp5(500, 300,  'l_5'), 
        CleaningLeafEp5(600, 300,  'l_6'),
        CleaningLeafEp5(600, 300,  'l_1'),
        CleaningLeafEp5(700, 300,  'l_2'),
        CleaningLeafEp5(800, 300,  'l_1'),
        CleaningLeafEp5(900, 300,  'l_2'),
        
        CleaningLeafEp5(1000, 300,  'l_4'),
        CleaningLeafEp5(1100, 300,  'l_3'),
        CleaningLeafEp5(900, 300,  'l_6'),
        CleaningLeafEp5(950, 300,  'l_5'),
        CleaningLeafEp5(850, 300,  'l_4'),
        CleaningLeafEp5(1300, 300,  'l_3'),


        CleaningLeafEp5(0, 400,    'l_2'), 
        CleaningLeafEp5(100, 400,  'l_1'),
        CleaningLeafEp5(300, 400,  'l_6'), 
        CleaningLeafEp5(400, 400,  'l_5'), 
        CleaningLeafEp5(500, 400,  'l_4'), 
        CleaningLeafEp5(600, 400,  'l_3'),
        CleaningLeafEp5(600, 400,  'l_2'),
        CleaningLeafEp5(700, 400,  'l_3'),
        CleaningLeafEp5(800, 400,  'l_2'),
        CleaningLeafEp5(900, 400,  'l_3'),
        
        CleaningLeafEp5(1000, 400,  'l_4'),
        CleaningLeafEp5(1100, 400,  'l_5'),
        CleaningLeafEp5(1050, 400,  'l_6'),
        CleaningLeafEp5(1200, 400,  'l_5'),
        CleaningLeafEp5(1300, 400,  'l_4'),
        CleaningLeafEp5(1200, 400,  'l_3'),


CleaningLeafEp5(0, 500,    'l_1'), 
        CleaningLeafEp5(100, 500,  'l_2'),
        CleaningLeafEp5(300, 500,  'l_1'), 
        CleaningLeafEp5(400, 500,  'l_3'), 
        CleaningLeafEp5(500, 500,  'l_4'), 
        CleaningLeafEp5(600, 500,  'l_5'),
        CleaningLeafEp5(600, 500,  'l_6'),
        CleaningLeafEp5(700, 500,  'l_5'),
        CleaningLeafEp5(800, 500,  'l_4'),
        CleaningLeafEp5(900, 500,  'l_3'),
        
        CleaningLeafEp5(1000, 500,  'l_2'),
        CleaningLeafEp5(1050, 500,  'l_1'),
        CleaningLeafEp5(1350, 500,  'l_3'),
        CleaningLeafEp5(1450, 500,  'l_4'),
        CleaningLeafEp5(1450, 550,  'l_5'),
        CleaningLeafEp5(980, 500,  'l_6'),

        CleaningLeafEp5(50, 0,  'l_3'),
        CleaningLeafEp5(100, 100,  'l_4'),
        CleaningLeafEp5(50, 100,  'l_5'),
        CleaningLeafEp5(0, 100,  'l_6'),

        ]
    call screen clean_game_ep5


    $ clean_game_ep5_arr = []
    show expression '#000a'

    hide screen clean_game_ep5_tmp
    show screen clean_game_ep5
    show search_cleaning_end
    with Dissolve(.5)

    call screen end_2_search_game_ep5

    hide screen search_cleaning_end
    hide screen clean_game_ep5
    hide screen end_2_search_game_ep5

    $ time.time_now = 'evening'
    call show_bg_image_label from _call_show_bg_image_label_41
    call show_additional_images_label from _call_show_additional_images_label_35
    show Officer Normal
    show Officer Normal:

        xalign 1.5
        ypos 1085
        zoom 1.0-0.035


    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085
        zoom 1.0-0.035
    show GG Normal
    with Dissolve(.5)
    show Officer Normal:

        xzoom -1
        linear 1 xalign .85
        ypos 1085
        zoom 1.0-0.035
    $ renpy.pause(1, hard = True)










    show Officer Normal:
        xalign .85
    with my_dissolve
    "Офицер" "Я слежу за тобой, ничтожество. "

    "[gg]" "Ваше старпёрское брюзжание меня не проймёт."
    show Officer Normal
    "Офицер" "Посмотрим, [gg], посмотрим. "
    scene expression '#000' with Dissolve(.75)

    $ renpy.pause(.25, hard = True)

    $ renpy.pause(.3)

    $ time.time_now = 'evening'

    if not events.get('ep45_milf_54_hall'):
        $ Event('ep45_milf_park', 'Corridor', 'ep45_milf_53', day_start = time.day_now + 1, time = ['morning', 'afternoon'])



    $ Event('ep45_milf_52_skip', None, 'ep45_milf_52_skip', day_start = time.day_now + 1, time = ['evening', 'night'])












    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
