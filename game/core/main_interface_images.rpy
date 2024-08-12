

image main_menu_button:
   # 'gui/main_menu_button_idle.png' with Dissolve(.2)
    on idle:
        'gui/main_menu_button_idle.png' with Dissolve(.2)
    on hover:

        'gui/main_menu_button_hover.png' with Dissolve(.2)
    on selected_idle:

        'gui/main_menu_button_hover.png'
    on selected_hover:

        'gui/main_menu_button_hover.png'


image morning_button:
    on idle:
        i_path + "/Time_Morning.png" with Dissolve(.2)
    on hover:
        im.MatrixColor(i_path + "/Time_Morning.png", im.matrix.brightness(.3)) with Dissolve(.2)
image afternoon_button:
    on idle:
        i_path + "/Time_Afternoon.png" with Dissolve(.2)
    on hover:
        im.MatrixColor(i_path + "/Time_Afternoon.png", im.matrix.brightness(.3)) with Dissolve(.2)
image evening_button:
    on idle:
        i_path + "/Time_Evening.png" with Dissolve(.2)
    on hover:
        im.MatrixColor(i_path + "/Time_Evening.png", im.matrix.brightness(.3)) with Dissolve(.2)
image night_button:
    on idle:
        i_path + "/Time_Night.png" with Dissolve(.2)
    on hover:
        im.MatrixColor(i_path + "/Time_Night.png", im.matrix.brightness(.3)) with Dissolve(.2)


image bag_button:

    on idle:
        i_path + "/Icon_Bag.png" with Dissolve(.2)
    on hover:
        im.MatrixColor(i_path + "/Icon_Bag.png", im.matrix.brightness(.3)) with Dissolve(.2)



image map_button:

    on idle:
        i_path + "/Icon_Map.png" with Dissolve(.2)
    on hover:
        im.MatrixColor(i_path + "/Icon_Map.png", im.matrix.brightness(.3)) with Dissolve(.2)


image quest_button:

    on idle:
        i_path + "/Icon_Quest.png" with Dissolve(.2)
    on hover:
        im.MatrixColor(i_path + "/Icon_Quest.png", im.matrix.brightness(.3)) with Dissolve(.2)



image mobile_button:

    on idle:
        i_path + "/Icon_Mobile.png" with Dissolve(.2)
    on hover:
        im.MatrixColor(i_path + "/Icon_Mobile.png", im.matrix.brightness(.3)) with Dissolve(.2)



image warning_icon:

    'interface/warning.png' with Dissolve(.2)

    pause 5

    '#0000' with Dissolve(.2)

    pause .3

    'interface/warning.png' with Dissolve(.2)

    pause .3

    '#0000' with Dissolve(.2)

    pause .3

    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
