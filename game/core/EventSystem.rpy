init python:



    def get_check_ev_buttons(check_ev,):
        
        global mp
        
        if type(check_ev) != type([1,]):
            return None
        
        return_events = [ ]
        
        
        return_names = [_('Говорить'), _('Спросить'), _('Помочь'), _('Действие'), _('Обратиться'), _('Слушай...')]
        
        for i in check_ev:

            if getattr(i, 'button_name', None):
                
                if preferences.language in (None, 'eng', 'rus'):
                    rdvvas = str(i.button_name)
                else:
                    
                    rdvvas = __("Активировать квест")
                return_events.append(rdvvas)
            
            else:
                
                if not len(return_names):
                    
                    return_names = [_('Говорить'), _('Спросить'), _('Помочь'), _('Действие'), _('Обратиться'), _('Слушай...')]
                
                
                return_events.append(return_names.pop(0))
        
        
        return return_events



    def finish_event(event_name):
        getattr(store, "events", {}).pop(event_name, 0)
        getattr(store, "fashion_store_events_items", {}).pop(event_name, 0)

        getattr(store, "mishwanda_store_events_items", {}).pop(event_name, 0)

    _events_need_costume = {
    "steam_bonus_1_0" : "cow",

    "steam_bonus_1" : "cow",

    }

    def get_all_events_from_location(location = None, only_first = False, allowed = False, ignore = False):
        
        global events, location_now
        
        #if location:
            
        #    location_now = location
        
        return_events = []
        
        for event in events:

            _event = events[event]
            enc    = store._events_need_costume
            if _event.name in enc:
                if getattr(store, 'milf_costume', 'n_body') != enc[_event.name]:
                    continue

            if ignore:
                if _event.name in ignore:
                    continue
            if allowed:
                if _event.name not in allowed:
                    continue
            if _event.check(check_loc=not location):
                
                if getattr(store, 'milf_costume', 'n_body') != 'n_body' or getattr(store, 'christie_costume', 'n_body') != 'n_body':

                    if any((
                        location and _event.location != location,
                        'milf_root_' in _event.label,
                        'ep1_' in _event.label,
                        'ep2_' in _event.label,
                        'ep3_' in _event.label,
                        'ep4_' in _event.label,
                        'ep45_' in _event.label,
                        'ep5_' in _event.label,
                        'final_act_' in _event.label,
                        'christie_root_' in _event.label,
                        )):
                        
                        pass

                    else:
                        return_events.append(_event)
                        if only_first:
                            return return_events
                
                else:
                    if location and _event.location != location:
                        pass
                    else:
                        return_events.append(_event)
                        if only_first:
                            return return_events
        
        return return_events



    def sort_events():
        global events, location_now, sorted_events
        
        
        sorted_events = [x[0] for x in sorted(events.items(), key = lambda item: item[1].priority)]

    def check_events(location = None):
        global events, location_now, sorted_events
        if location:
            location_now = location
        
        
        sort_events()
        
        for event in sorted_events:
            if event in events and events[event].check():
                if getattr(store, 'milf_costume', 'n_body') != 'n_body' or getattr(store, 'christie_costume', 'n_body') != 'n_body':
                    if 'christie_root_' in events[event].label:
                        pass
                    elif 'milf_root_' in events[event].label:
                        pass
                    elif 'ep1_' in events[event].label:
                        pass
                    elif 'ep2_' in events[event].label:
                        pass
                    elif 'ep3_' in events[event].label:
                        pass
                    elif 'ep4_' in events[event].label:
                        pass
                    elif 'ep45_' in events[event].label:
                        pass
                    elif 'ep5_' in events[event].label:
                        pass

                    else:
                
                        return events[event]
                


                else:
                
                    return events[event]


    def check_and_jump(event):
        global events
        if events.get(event):
            if events[event].check():
                if getattr(store, 'milf_costume', 'n_body') != 'n_body':

                    if 'milf_root_' in events[event].label:
                        pass
                    elif 'ep1_' in events[event].label:
                        pass
                    elif 'ep2_' in events[event].label:
                        pass
                    elif 'ep3_' in events[event].label:
                        pass
                    elif 'ep4_' in events[event].label:
                        pass
                    elif 'ep45_' in events[event].label:
                        pass
                    elif 'ep5_' in events[event].label:
                        pass

                    else:
                        events[event].jump()
                else:
                    events[event].jump()
                    


    class Event():
        # Создала доку для напоминалки себе
        """
        Event - это класс, представляющий событие. В нем имеются следующие атрибуты:
        - name: Название события. В 99% случав просто лейбл на который ивент будет прыгать
        - location: локация где происходит ивент (необязательно).
        - label: Лейбл куда прыгнет (необязательно), если не указано - то это name
        - time: время активации квеста (необязательно). может быть "morning" "afternoon" "evening" "night", либо списком из нескольких времен. Если передано None - то игнорится
        - button_name: как будет называться кнопка этого квеста в подменю (необязательно). иногда квестов несколько и после кнопки "говорить" вылазит подменю с выбором квеста
        - day_start: день активации ивента (необязательно). day_start = time.day_now + n, где n это через сколько исполнить. None -> игнорирует
        - priority: пока хз.
        - need_items: Так понимаю какие предметы нужно иметь.
        """
        def __init__(self, name, location = None, label = None, time = None, button_name = None, day_start = None, priority=0, need_items = [], skip_check = 0):
            
            global events
            
            self.name        = name
            
            self.location    = location
            if label:
                self.label   = label
            else:
                self.label   = name
            
            self.time        = time
            
            self.day_start   = day_start
            
            self.complete    = False
            
            self.button_name = button_name
            
            events[name]     = self
            
            self.priority    = priority
            
            self.need_items  = need_items

            self.skip_check   = skip_check
        
        
        
        def check(self, check_loc = True, check_time = True, check_day = True):
            
            global events, location_now, time, gigiena, allowed_events, inventory
            
            if len(getattr(store, "allowed_events", list())):
                if self.name not in allowed_events:
                    return False
            
            
            
            
            if self.complete:
                
                return False
            
            if getattr(self, 'skip_check', 0) > 0:
                self.skip_check -= 1

                return False
            
            
            
            
            if self.location and check_loc:
                if self.location is not None:
                    if str(location_now).lower() != str(self.location).lower():
                        
                        return False
            
            
            if self.day_start and check_day:
                
                if time.day_now < self.day_start:
                    
                    return False
            
            
            if self.time and check_time:
                
                if time.time_now not in self.time:
                    
                    return False
            
            for i in getattr(self, 'need_items', []):
                if not get_item_by_id(i, True, True):
                    return False
            
            

            return True
        
        
        
        def change_priority(new_priority=0):
            if new_priority == self.priority:
                return
            
            self.priority = new_priority
            
            sort_events()
        
        def __del__(self):
            
            
            global completed_events, my_debug_mode

            if self.name not in completed_events:
                completed_events.append(self.name)
        
        
        def jump(self, complete = True):
            self.complete = complete
            renpy.jump(self.label)


    def check_exist_event(event):
        if any((
        getattr(store, 'events', {1:1}).get(event),
        event in getattr(store, 'completed_events', [1, ]),
        )
        ):
            return True


    def events_pop(what_pop, rtrn=0):
        if (not hasattr(store, 'events')) or (not hasattr(store, 'completed_events')):
            return 'error'

        
        if what_pop not in store.completed_events:
            store.completed_events.append(what_pop)
        
        return dict.pop(store.events, what_pop, rtrn)
    

    # def check_where_we_at_root(what_root, number):
    #     for i in 

init python:
    event_for_preview = 0



label choose_quest_hide_label:
    hide screen choose_quest_screen
    jump main_interface_label


label my_rollback_label:
    call show_bg_image_label from _call_show_bg_image_label_164# from _call_show_bg_image_label_98
    call show_additional_images_label from _call_show_additional_images_label_101# from _call_show_additional_images_label_83
    with Dissolve(.15)
    $ renpy.pause(.2, hard = True)
    $ Rollback()()
    return

init 1000 python:
    standart_adv_character = ADVCharacter()
    #persistent.event_for_preview = -1

    def check_for_probka_event(lbl):
        for xvsd in range(9):

            if 'milf_root_'+str(xvsd) in lbl:
                return True
                #text __('Пробка') font 'fonts/mini_game.ttf' xpos 155 size 35 yalign .5

    def check_for_shantash_event(lbl):
        for xvsd in range(9, 14):

            if 'milf_root_'+str(xvsd) in lbl:
                return True
    def jump_to_one_evnt_ignore_others():
        global check_ev, check_evnts 
        clltt    = copy.deepcopy(persistent.event_for_preview)
        check_ev = check_evnts[clltt]
        #persistent.event_for_preview = -1 
        if 'christie_root_' in check_ev.label and getattr(store, 'christie_costume', 'n_body') != 'n_body':
            pass
        elif 'milf_root_' in check_ev.label and getattr(store, 'milf_costume', 'n_body') != 'n_body':
            pass
        else:
            for i in range(len(check_evnts)):
                if i != clltt:
                    check_evnts[i].day_start = time.day_now + 1
            Hide('main_interface')()
            renpy.jump(check_ev.label)
label choose_quest_show_label:
    "choose_quest_context" "choose_quest_context"
    #"choose_quest_context_2" "choose_quest_context_2"
    
    #$ renpy.context()
    show screen choose_quest_screen
    with None
    if persistent.event_for_preview > -1:
        #"!" "?"
        $ jump_to_one_evnt_ignore_others()
            #renpy.jump(check_ev.label)
    


    call screen main_interface

    # viewport:
    #     #if persistent.first_show_choose_quest_screen_down:
    #     at transform:
    #         #on show:
    #         ypos 1080

    #         easein .5  ypos 0 
             
        
    #     ymaximum 1080
    #     #image '#fff'
    #     image "shadow_down" alpha 0.7 yalign 1.0
    #     viewport:
    #         xmaximum 541
    #         ymaximum 97
    #         xalign .5 yalign .95
    #         image 'text_info_bg'
    #         text str(_("!!")) xalign .5 yalign .5 size 30 color '#000'

image text_info_bg gray  = im.Grayscale('interface/text_info_bg.png')
image text_info_bg hover = im.MatrixColor('interface/text_info_bg.png', im.matrix.brightness(.3))

screen choose_quest_screen:
    
    key "rollback" action Function(my_rollback)
    default need_hide = False
    default event_now = -1
    zorder 15


    imagebutton: 
        idle  '#0000'
        hover '#0000'
        action NullAction()

    viewport:
        #if persistent.first_show_choose_quest_screen_down:

        if persistent.first_show_choose_quest_screen_up:
            at transform:
                on show:
                    ypos 300

                    easein .5  ypos 0 
                on hide:
                    ypos 0

                    easeout .5  ypos 300
        else:
            at transform:
                on hide:
                    ypos 0

                    easeout .5  ypos 300

                
             
        
        ymaximum 1080
        #image '#fff'
        image "shadow_down" alpha 0.7 yalign 1.0

        viewport:
            xmaximum 541
            ymaximum 97
            xalign .5 yalign .95
            if persistent.event_for_preview < 0:
                image "text_info_bg gray"
            else:
                imagebutton: 
                    idle  "text_info_bg"
                    hover "text_info_bg hover"
                    action Hide("choose_quest_screen")
            text _("Начать ивент") xalign .5 yalign .5 size 30: 
                if persistent.event_for_preview < 0:
                    color '#808080'
                else:
                    color '#000'
    viewport:
        if persistent.first_show_choose_quest_screen_up:
            at transform:
                on show:
                    ypos -300

                    easein .5 ypos 0
                on hide:
                    ypos 0

                    easeout .7  ypos -300
        else:

            at transform:
                on hide:
                    ypos 0

                    easeout .7  ypos -300

        ymaximum 300
        image '#fff0'
        #text str(event_now)

        image "shadow_up" # alpha .5

    
        # viewport xalign .95 yalign .2:
        #     ymaximum 90
        #     xmaximum 150
        #     add '#0000'
        #     add 'pc_back'
        #     imagebutton xalign .99 yalign .5:

        #         idle Text(_('Назад'), font = 'fonts/mini_game.ttf')
        #         hover Text(_('Назад'), font = 'fonts/mini_game.ttf')

        #         yanchor .5
        #         at PulseButtonXzoom09
        #         action SetScreenVariable("need_hide", True), Jump('choose_quest_hide_label')


    hbox:
        
        spacing 10
        if persistent.first_show_choose_quest_screen_up:
            at transform:
                on show:
                    yalign -1.5 xalign .5

                    easein .7 yalign .5
                on hide:
                    yalign .5 xalign .5

                    easeout .7  yalign -1.5
        else:
            at transform:
                on show:

                    xalign .5 yalign .5
                on hide:
                    yalign .5 xalign .5

                    easeout .7  yalign -1.5

        for i in range(len(check_evnts)):
            vbox:
                spacing -15
                viewport:
                    xmaximum 268
                    ymaximum 331
                    if persistent.event_for_preview == i:
                        imagebutton:
                            idle  'interface/evnt_button_hover.png'
                            hover 'interface/evnt_button_hover.png'
                            action NullAction()
                    else:

                        imagebutton:
                            idle  'interface/evnt_button.png'
                            hover 'interface/evnt_button_hover.png'
                            if persistent.event_for_preview < 0:
                                action [SetField(persistent, "first_show_choose_quest_screen_down", True), SetField(persistent, "first_show_choose_quest_screen_up", None), SetField(persistent, 'event_for_preview', i), Function(jump_to_one_evnt_ignore_others)]
                            else:
                                action [SetField(persistent, "first_show_choose_quest_screen_down", None), SetField(persistent, "first_show_choose_quest_screen_up", None), SetField(persistent, 'event_for_preview', i), Rollback()]#, SetScreenVariable('event_now', 0), Jump('milf_root_9')
                        
                    if 'christie_root_' in check_evnts[i].label or 'tyan_' in check_evnts[i].label:
                        image 'interface/evnt_ava_christie.png'
                    elif 'misha_root_' in check_evnts[i].label:
                        image 'interface/evnt_ava_misha.png'
                    elif 'cat_root_' in check_evnts[i].label:
                        image 'interface/evnt_ava_kat.png'

                    else:
                        image 'interface/evnt_ava_milf.png'

                    # if persistent.event_for_preview == i:
                    #     image '#fff5'
                        
                    # else:
                    #     imagebutton: 
                    #         idle  '#0000'
                    #         hover '#fff5'
                    #         if persistent.event_for_preview < 0:
                    #             action [SetField(persistent, "first_show_choose_quest_screen_down", True), SetField(persistent, "first_show_choose_quest_screen_up", None), SetField(persistent, 'event_for_preview', i), Jump(check_evnts[i].label)]
                    #         else:
                    #             action [SetField(persistent, "first_show_choose_quest_screen_down", None), SetField(persistent, "first_show_choose_quest_screen_up", None), SetField(persistent, 'event_for_preview', i), Rollback()]#, SetScreenVariable('event_now', 0), Jump('milf_root_9')
                        
                    if 'tyan_' in check_evnts[i].label:
                        text __('Кристи')  xalign .5 color '#000' size 35 yalign .77
                    elif 'milf_root_' in check_evnts[i].label:
                        text __('Марина')  xalign .5 color '#000'size 35 yalign .77
                    elif 'christie_root_' in check_evnts[i].label or 'tyan_' in check_evnts[i].label:
                        text __('Кристи')  xalign .5 color '#000' size 35 yalign .77
                    elif 'misha_root_' in check_evnts[i].label:
                        text __('Мишванда')  xalign .5 color '#000' size 35 yalign .77
                    elif 'cat_root_' in check_evnts[i].label:
                        text __('Кэт')  xalign .5 color '#000' size 35 yalign .77
                    else:
                        text __('Марина')  xalign .5 color '#000' size 35 yalign .77
                    



                    if 'tyan_' in check_evnts[i].label:
                        text __('Ночная услада') font store.mini_game_font xalign .5 color '#fff' size 35 yalign 1.0 outlines [(3, '#000c', 0, 0)]
                    elif 'milf_root_' in check_evnts[i].label:
                        if check_for_probka_event(check_evnts[i].label):

                            text __('Пробка') font store.mini_game_font xalign .5 color '#fff' size 35 yalign 1.0 outlines [(3, '#000c', 0, 0)]
                        elif check_for_shantash_event(check_evnts[i].label):
                            text __('Грязная игра') font store.mini_game_font xalign .5 color '#fff'size 35 yalign 1.0 outlines [(3, '#000c', 0, 0)]
                        else:
                            text __('Сюжет') font store.mini_game_font xalign .5 color '#fff'size 35 yalign 1.0 outlines [(3, '#000c', 0, 0)]
                    else:
                        text __('Сюжет') font store.mini_game_font xalign .5 color '#fff' size 35 yalign 1.0 outlines [(3, '#000c', 0, 0)]
            #image 'interface/evnt_ava_kat.png'
            #image 'interface/evnt_ava_misha.png'
    if need_hide:
        timer 0.01 action Hide('choose_quest_screen')
        imagebutton:
            idle  '#fffa'
            hover '#fffa'
            action NullAction()