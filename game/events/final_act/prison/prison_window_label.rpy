label prison_window_label:
    scene black
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    scene image '/cg/final_act/prison/police_station/'+str(time.time_now)+'.png'
    show final_act_cage_shadow
    with my_dissolve
    $ renpy.pause(.5, hard = True)

    call wait_click_label from _call_wait_click_label_16

    scene black
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    jump main_interface_label