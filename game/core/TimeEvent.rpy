init -100 python:

    eng_tdtd = {
     'Понедельник' : 'Monday',
     'Вторник' : 'Tuesday',
     'Среда' : 'Wednesday',
     'Четверг' : 'Thursday',
     'Пятница' : 'Friday',
     'Суббота' : 'Saturday',
     'Воскресенье' : 'Sunday'

    }

    rus_time = {
    'morning'   : 'Утро',
    'afternoon' : 'День',
    'evening'   : 'Вечер',
    'night'     : 'Ночь',

    }

    def get_prev_time():
        global time

        if time.time_now == 'afternoon':
            return 'morning'
        
        elif time.time_now == 'evening':
            return 'afternoon'
        
        elif time.time_now == 'night':
            return 'evening'

        return 'night'

    def get_next_time():
        global time
        
        if time.time_now == 'morning':
            return 'afternoon'
        
        elif time.time_now == 'afternoon':
            return 'evening'
        
        elif time.time_now == 'evening':
            return 'night'
        
        return 'morning'

    class Time():
        def __init__(self):
            self.time_now = 'morning'
            self.day_now  = 1
            self.times    = ['morning', 'afternoon', 'evening', 'night']
            self.tdtd     = 'Воскресенье'
            self.block    = False
        def time_forward(self, jump_to_main_interface = True, block_to_next_day = False, need_check_ev = True):
            
            global milf_drunk, block_time_forward
            global events, milf_position, sister_position
            global random_1_3_time, random_1_2_time
            global nastroi, gigiena, sitost, store
            
            
            if hasattr(store, 'sitost'):
                nastroi  = max(0,  nastroi-3)
            
            
            if getattr(store, 'block_time_forward', False):
                return self.time_forward
            indx = self.times.index(self.time_now)
            if indx != len(self.times)-1:
                self.time_now = self.times[indx+1]
            elif not block_to_next_day:
                
                if not hasattr(store, 'milf_drunk'):
                    milf_drunk = False
                
                
                
                self.time_now = self.times[0]
                self.day_now += 1
                if self.tdtd == 'Воскресенье':
                    self.tdtd = 'Понедельник'
                elif self.tdtd == 'Понедельник':
                    self.tdtd = 'Вторник'
                elif self.tdtd == 'Вторник':
                    self.tdtd = 'Среда'
                elif self.tdtd == 'Среда':
                    self.tdtd = 'Четверг'
                elif self.tdtd == 'Четверг':
                    self.tdtd = 'Пятница'
                elif self.tdtd == 'Пятница':
                    self.tdtd = 'Суббота'
                elif self.tdtd == 'Суббота':
                    self.tdtd = 'Воскресенье'
                if getattr(store, 'block_change_milf_position', False):
                    pass
                else:
                    
                    if sister_position['morning'][0] == 'Kitchen':
                        milf_position['morning'] = ['Restroom',  'milf_restroom']
                    elif random_1_3_time.get_n() == 1:
                        milf_position['morning'] = ['Kitchen',   'milf_kitchen']
                    
                    else:
                        
                        milf_position['morning'] = ['Restroom',  'milf_restroom']
                    
                    
                    if random_1_2_time.get_n() == 1:
                        
                        milf_position['afternoon']   = ['Corridor', 'milf_corridor']
                        sister_position['afternoon'] = ['Sister_Room', 'sister_room']
                    else:
                        
                        milf_position['afternoon']   = ['Hall',      'milf_hall']
                        sister_position['afternoon'] = ['Restroom',  'sister_restroom']

            if need_check_ev:
                check_ev = check_events()
                if check_ev:
                    return Jump(check_ev.label)()
            
            if jump_to_main_interface:
                return Jump('main_interface_label')()

            return self.time_forward
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
