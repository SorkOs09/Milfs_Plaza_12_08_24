label test_event_3:

    call show_bg_image_label from _call_show_bg_image_label_248
    show Christie Normal
    show Christie Normal:
        xalign .85
        ypos 1085
    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left

    "Кристина" "test_event_3"

    "[gg]" "test_event_3"

    python:
        events.pop("test_event_3", 0)
        Event("test_event_4_kitchen", location = "Kitchen", button_name = "TEST EVENT 4 K", time=["afternoon"])
        Event("test_event_4_hall", location = "Hall", button_name = "TEST EVENT 4 H", time=["evening"])

    jump main_interface_label