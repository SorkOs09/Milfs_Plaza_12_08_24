label test_event_2:
    
    #Кухня!
    call show_bg_image_label from _call_show_bg_image_label_247
    show Milf Normal
    show Milf Normal:
        reflect
        xalign .15
        ypos 1085
    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_right, reflect

    "Марина" "test_event_2"

    "[gg]" "test_event_2"

    $ events.pop("test_event_2", 0)
    $ Event("test_event_3", location = "Christie", button_name = "TEST EVENT 3")

    jump main_interface_label