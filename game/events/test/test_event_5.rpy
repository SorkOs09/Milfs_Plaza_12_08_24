label test_event_5:
    
    "[gg]" "test_event_5"
    $ events.pop("test_event_5", 0)
    $ Event("test_event_6", location = "Corridor", day_start=time.day_now+1) # На следующий день после прошлой цепочки ивентов

    jump main_interface_label
