label test_event_1:

    call show_bg_image_label from _call_show_bg_image_label_250
    show Igor Normal
    show Igor Normal:
        xalign .85
        ypos 1085
    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left

    "Игорь" "test_event_1"

    "[gg]" "test_event_1"

    $ events.pop("test_event_1", 0)
    $ Event("test_event_2", location = "Kitchen_Milf", button_name = "TEST EVENT 2")

    jump main_interface_label