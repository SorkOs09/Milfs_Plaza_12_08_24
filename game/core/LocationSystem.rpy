init -2000 python:
    old_location = None
    def JumpToLocation(location, need_time_forward = False):
        global old_location, location_now, block_time_forward, nastroi, gigiena, sitost, time, check_evnts
        
        if location.lower() == 'bed' and hasattr(store, 'block_time_forward') and block_time_forward:
            renpy.jump('bed_night_milf_35')
        if location in ('Milf_Room', 'Sister_Room', 'Restroom', 'Corridor', 'City_Home', 'Hall', 'City_Shop'):
            if any((
                location not in ('Corridor', 'City_Home', 'Hall', 'City_Shop'),
                location == 'Corridor' and location_now in ('Sister_Room', 'GG_Room', 'Restroom', 'City_Home'),
                location == 'City_Home' and location_now == 'Corridor',
                location == 'Hall' and location_now == 'Milf_Room', 
                location == 'City_Shop' and location_now == 'StoreIn',
                
                )): 
                renpy.play('audio/door.mp3')

        
        old_location = location_now
        location_now = location
        #check_ev = check_events()
        check_evnts = get_all_events_from_location()
        if need_time_forward:
            time.time_forward(jump_to_main_interface = False) 
        if len(check_evnts):
            if len(check_evnts) == 1: 
                check_ev = check_evnts[0]# check_events()
                Hide('main_interface')()
                renpy.jump(check_ev.label)
            else:
                persistent.first_show_choose_quest_screen_up = True
                persistent.event_for_preview = -1
                renpy.jump('choose_quest_show_label')
        #if check_ev:
        #    renpy.jump(check_ev.label)
        
        
        if hasattr(store, 'sitost'):
            
            sitost    = max(0,  sitost-1)
            gigiena   = max(0,  gigiena-1)
        renpy.jump('main_interface_label')
init -1000 python:

    class Location():
        def __init__(
    self, 
    name, 
    buttons = None, 
    image_buttons = None, 
    
    image_buttons_times = None,

    bg = None):
            
            global locations
            self.name              = name
            if not bg:
                self.bg            = name
            else:
                self.bg            = bg
            
            if buttons is None:
                self.buttons       = []
            
            else:
                self.buttons       = buttons
            
            if image_buttons is None:
                self.image_buttons = {}
            else:
                self.image_buttons = image_buttons
            

            if image_buttons_times is None:
                self.image_buttons_times = {
                'morning'   : {},
                'afternoon' : {},
                'evening'   : {},
                'night'     : {},
                }
            else:
                self.image_buttons_times = image_buttons_times
            
            self.image_buttons_times = copy.deepcopy(self.image_buttons_times)
            self.image_buttons = copy.deepcopy(self.image_buttons)
            self.buttons = copy.deepcopy(self.buttons)
            locations.update({self.name:self})


    def fix_for_buttons_at_locations():
        global locations
        if not hasattr(store, 'locations'):
            return
        for i in locations:
            loc = locations[i]

            if hasattr(loc, 'image_buttons_times'):

                tmp_copy = copy.deepcopy(loc.image_buttons_times)
            
                loc.image_buttons_times = copy.deepcopy(tmp_copy)

                for j in ('morning', 'afternoon', 'evening', 'night'):
                    if j in loc.image_buttons_times:
                        tmp_copy = copy.deepcopy(loc.image_buttons_times[j])
            
                        loc.image_buttons_times[j] = copy.deepcopy(tmp_copy)

            if hasattr(loc, 'image_buttons'):
                tmp_copy = copy.deepcopy(loc.image_buttons)

                loc.image_buttons = copy.deepcopy(tmp_copy)

            if hasattr(loc, 'buttons'):
                tmp_copy = copy.deepcopy(loc.buttons)
                loc.buttons = copy.deepcopy(tmp_copy)


    class FixStore():
        def __init__(self):
            self.coffe_50_percent  = None
            self.coffe_100_percent = None
            self.kat_on_bed_2      = None

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
