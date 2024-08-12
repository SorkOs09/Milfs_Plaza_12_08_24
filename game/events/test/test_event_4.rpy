label test_event_4_hall:
    
    "[gg]" "test_event_4_hall"
    $ events.pop("test_event_4_hall", 0)

    jump test_event_4_end

label test_event_4_kitchen:
    
    "[gg]" "test_event_4_kitchen"
    $ events.pop("test_event_4_kitchen", 0)
    jump test_event_4_end

label test_event_4_end:

    if "test_event_4_hall" in completed_events and "test_event_4_kitchen" in completed_events:
        $ Event("test_event_5", location = "Corridor", day_start=time.day_now+1, button_name = "TEST EVENT 5")

    jump main_interface_label