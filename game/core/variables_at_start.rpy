init python:
    SavesText = [
'Обнаруженно устаревшее сохранение.',
'Мы крайне не рекомендуем использовать его.',
'Это сохранение может противоречить пройденным или будущим квестам в игре',
'И работает исключительно для тестирования.',
'Пожалуйста, если будете слать отчёты об ошибке',
'Уточняйте, что начали прохождение используя старый сейв-файл!']
    SavesTextEng = [
'Old save-file detected.',
'We strongly recommend do not use it.',
'This save may conflict with past or future quests in the game',
'And works only for testing purposes.',
'Please, if you send error reports',
'Specify that you started the passage using the old save-file!'

    ]
image _bg_frame_2_pool = Frame('interface/comic_v2/bg_frame_2.png', Borders(64, 64, 64, 64)) 
screen mp_player_pool_confirm:
    viewport:
        maximum (1350, 880)
        align (.5, .5)
        image '_bg_frame_2_pool'
        image '_bg_frame_2_pool'
        vbox:
            spacing 5
            align (.5, .5)
            hbox:
                text __('Любимый Типаж Девушек: '):
                    size 40
                    color '#fff'
                text __(mp.player_pool['Любимый Типаж Девушек']):
                    size 40
                    color '#fffa'

            hbox:
                text __('Любимый Размер Груди: '):
                    size 40
                    color '#fff'
                text __(mp.player_pool['Любимый Размер Груди']):
                    size 40
                    color '#fffa'

            hbox:
                text __('Любимое Занятие Вне Работы: '):
                    size 40
                    color '#fff'
                vbox:
                    for i in mp.player_pool['Любимое Занятие Вне Работы']:
                        text __(i) + ' ':
                            size 25
                            color '#fffa'
                            
                

            hbox:
                text __('Любимая Игра: '):
                    size 40
                    color '#fff'
                text mp.player_pool['Любимая Игра']:
                    size 25
                    color '#fffa'
                    ypos 12

            hbox:
                text __('Кем Бы Я Хотел Стать В Другой Жизни: '):
                    size 40
                    color '#fff'
                text mp.player_pool['Кем Бы Я Хотел Стать В Другой Жизни']:
                    size 25
                    color '#fffa'
                    ypos 12

            hbox:
                text __('Любимое время суток: '):
                    size 40
                    color '#fff'
                text __(mp.player_pool['Любимое время суток']):
                    size 40
                    color '#fffa'

            hbox:
                text __('Любимый напиток: '):
                    size 40
                    color '#fff'
                text mp.player_pool['Любимый напиток']:
                    size 25
                    color '#fffa'
                    ypos 12
        hbox:
            xalign .95 yalign .97
            spacing 20
            textbutton __("Пройти заново") text_outlines [(1, '#000c', 0, 0)] action Jump('player_pool_restart') 
            textbutton __("Сохранить") text_outlines [(1, '#000c', 0, 0)] action Return() 

screen fix_saves_23_6_23_screen:

    imagebutton:
        idle '#000d'
        hover '#000d'
        action NullAction()
   # text '18+' xalign .5 yalign .2
    vbox:
        xalign .5 yalign .5
        if mp.language == 'ENG':

            for i in SavesTextEng:
                text i xalign .5
        else:
            for i in SavesText:
                text i xalign .5
    viewport xalign .5 yalign .9:
        xmaximum 1185
        ymaximum 50
        add '#0000'
        button:
            add 'simple_button'
            action Return()
        text 'OK' xalign .5 ypos 5
    # viewport xalign .5 yalign .95:
    #     xmaximum 1185
    #     ymaximum 50
    #     add '#0000'
    #     button:
    #         add 'simple_button'
    #         action Quit()
    #     text 'EXIT' xalign .5 ypos 5
label player_pool_restart:

    $ mp.player_pool_name = None
    $ mp.player_pool = {
            'Любимый Типаж Девушек': 'Стройные',
            'Любимый Размер Груди' : '1',
            'Любимое Занятие Вне Работы':[],
            'Любимая Игра': "Milf's Plaza",
            'Кем Бы Я Хотел Стать В Другой Жизни':'',
            'Любимое время суток':'Утро',
            'Любимый напиток':'',


            }
    $ mp.save()
    $ renpy.game.log.block()
    jump player_pool_name

label player_pool_name:
    $ mp.player_pool_name = renpy.input('(0/7) '+__('Как я могу к вам обращаться?'), default='', exclude = " ", length = 15)

    $ from_say_screen = False
    if preferences.language in ('spn', None, 'eng', 'rus'):
        jump player_pool_1
    else:
        $ i = renpy.input(__("(1/7) Любимый Типаж Девушек?"), default='', length = 20)

        $ mp.player_pool['Любимый Типаж Девушек'] = i
        jump player_pool_2
label player_pool:
    $ renpy.pause(1.0, hard = True)
    #$ renpy.game.log.block()
    show black
    hide screen icons_interface
    with my_dissolve
    call hide_menu_label from _call_hide_menu_label
    #$ renpy.pause(1.5, hard = True)
    
    show image 'gui/game_menu.png'
    with my_dissolve
    if preferences.language in ('spn', 'eng', None, 'rus'):
    
        "Texic" "Перед началом игры пройдите небольшую анкету."
    if preferences.language in (None, 'rus'):
        "Texic" "Она поможет нам улучшить нашу игру."

        "Texic" "Заранее спасибо!"

    $ renpy.game.log.block()
    
    
    
    $ mp.player_pool = {
            'Любимый Типаж Девушек': 'Стройные',
            'Любимый Размер Груди' : '1',
            'Любимое Занятие Вне Работы':[],
            'Любимая Игра': "Milf's Plaza",
            'Кем Бы Я Хотел Стать В Другой Жизни':'',
            'Любимое время суток':'Утро',
            'Любимый напиток':'',


            }
    jump player_pool_name
    #//далее ответ будет отражать анкету, которую игрок заполняет перед началом игры


    menu player_pool_1:
        "(1/7) Любимый Типаж Девушек?"
        "Стройные":
            $ mp.player_pool['Любимый Типаж Девушек'] = "Стройные"
            
        "Атлетичные":
            $ mp.player_pool['Любимый Типаж Девушек'] = "Атлетичные"
        "Мясистые":
            $ mp.player_pool['Любимый Типаж Девушек'] = "Мясистые"
        "Худенькие":
            $ mp.player_pool['Любимый Типаж Девушек'] = "Худенькие"
        "{i}Пройти анкету заново{/i}":
            jump player_pool_restart
    
    menu player_pool_2:
        "(2/7) Любимый Размер Груди?"

        "0":
            $ mp.player_pool['Любимый Размер Груди'] = "0"
        "1":
            $ mp.player_pool['Любимый Размер Груди'] = "1"
            
        "2":
            $ mp.player_pool['Любимый Размер Груди'] = "2"
        "3":
            $ mp.player_pool['Любимый Размер Груди'] = "3"
        "4":
            $ mp.player_pool['Любимый Размер Груди'] = "4"

        "5":
            $ mp.player_pool['Любимый Размер Груди'] = "5"
        "{i}ГИГАНСТКИЕ{/i}!" if preferences.language in ('spn', 'eng', None, 'rus'):
            $ mp.player_pool['Любимый Размер Груди'] = "Гигантские"
        "{i}Пройти анкету заново{/i}":
            jump player_pool_restart
    if preferences.language in ('spn', None, 'eng', 'rus'):
        $ i = mp.player_pool['Любимое Занятие Вне Работы']
        menu player_pool_3:
            "(3/7) Любимое Занятие Вне Работы? (Можно выбрать несколько)"
            
            "Кино" if "Кино" not in i:
                $ i.append("Кино")
                jump player_pool_3
            "{b}Кино{/b}" if "Кино" in i:
                $ i.remove("Кино")
                jump player_pool_3

            "Сериалы" if "Сериалы" not in i:
                $ i.append("Сериалы")
                jump player_pool_3
            "{b}Сериалы{/b}" if "Сериалы" in i:
                $ i.remove("Сериалы")
                jump player_pool_3

            "Компьютерные игры" if "Компьютерные игры" not in i:
                $ i.append("Компьютерные игры")
                jump player_pool_3
            "{b}Компьютерные игры{/b}" if "Компьютерные игры" in i:
                $ i.remove("Компьютерные игры")
                jump player_pool_3
            

            "Аниме" if "Аниме" not in i:
                $ i.append("Аниме")
                jump player_pool_3
            "{b}Аниме{/b}" if "Аниме" in i:
                $ i.remove("Аниме")
                jump player_pool_3

            "Настольные игры" if "Настольные игры" not in i:
                $ i.append("Настольные игры")
                jump player_pool_3
            "{b}Настольные игры{/b}" if "Настольные игры" in i:
                $ i.remove("Настольные игры")
                jump player_pool_3

            "Спорт" if "Спорт" not in i:
                $ i.append("Спорт")
                jump player_pool_3
            "{b}Спорт{/b}" if "Спорт" in i:
                $ i.remove("Спорт")
                jump player_pool_3

            "Сон" if "Сон" not in i:
                $ i.append("Сон")
                jump player_pool_3
            "{b}Сон{/b}" if "Сон" in i:
                $ i.remove("Сон")
                jump player_pool_3
            "..." if not len(mp.player_pool['Любимое Занятие Вне Работы']):
                jump player_pool_3
            "{i}Далее{/i}" if len(mp.player_pool['Любимое Занятие Вне Работы']):
                pass
            "{i}Пройти анкету заново{/i}":
                jump player_pool_restart
    else:

        $ i = renpy.input(__("(3/7) Любимое Занятие Вне Работы?"), default='', length = 20)

        $ mp.player_pool['Любимое Занятие Вне Работы'] = i
label player_pool_4:
    $ i = renpy.input('(4/7) '+__('Любимая Игра?'), default='', length = 15)

    $ mp.player_pool['Любимая Игра'] = i
    
label player_pool_5:
    $ i = renpy.input('(5/7) '+__('Кем Бы Я Хотел Стать В Другой Жизни'), default='', length = 25)

    $ mp.player_pool['Кем Бы Я Хотел Стать В Другой Жизни'] = i
    
    if preferences.language in ('spn', None, 'eng', 'rus'):
        menu player_pool_6:
            "(6/7) Любимое время суток?"

            "Утро":
                $ mp.player_pool['Любимое время суток'] = 'Утро'
            "День":
                $ mp.player_pool['Любимое время суток'] = 'День'
            "Вечер":
                $ mp.player_pool['Любимое время суток'] = 'Вечер'
            "Ночь":
                $ mp.player_pool['Любимое время суток'] = 'Ночь'
            "{i}Пройти анкету заново{/i}":
                jump player_pool_restart
    else:
        $ i = renpy.input(__("(6/7) Любимое время суток?"), default='', length = 20)

        $ mp.player_pool['Любимое время суток'] = i
label player_pool_7:
    $ i = renpy.input('(7/7) '+__('Любимый напиток?'), default='', length=25)

    $ mp.player_pool['Любимый напиток'] = i

    $ from_say_screen = False
    

label player_pool_end:
    #call screen mp_player_pool_confirm
    #"Texic" "Большое спасибо, твои ответы очень помогут нам улучшить сюжет!"
    #show black with my_dissolve
    #"Texic" "Возвращаемся к игре..."
    
    $ mp.save()

    $ smth_change_after_load = True

    $ print("smth_change_after_load : 206, false")
    hide black
    hide image 'gui/game_menu.png'
    with my_dissolve
    $ renpy.pause(.6, hard = True)
    $ renpy.game.log.block()
    return
    

    #//Любимый напиток

    #//Тут игрок должен вписать


label after_load:
    $ smth_change_after_load = False
    $ from_say_screen        = False
    if persistent.reload_for_update_sprites:
        $ persistent.reload_for_update_sprites = None
        $ Rollback()()
    call please_wait_for_load from _call_please_wait_for_load
    hide please_wait
    call variables_at_start from _call_variables_at_start
    call fixes_after_7_ep from _call_fixes_after_7_ep
    if hasattr(store, 'descript') and hasattr(store, 'old_descript') and descript == '' and old_descript == '':

        if hasattr(store, 'locations') and 'GG_Room' in locations:


            if hasattr(locations['GG_Room'], 'image_buttons_times'):


                if 'morning' in locations['GG_Room'].image_buttons_times:


                    if 'kat_on_bed_morning' in locations['GG_Room'].image_buttons_times['morning']:
                        if not hasattr(store, 'add_items_for_web_shop'):
                            $ smth_change_after_load = True
                            call milf_root_1_setup from _call_milf_root_1_setup_1

    if smth_change_after_load:

        $ renpy.game.log.block()

        $ smth_change_after_load = False

        $ print("smth_change_after_load : 49, false")

    if getattr(store, '_after_load_from_start', False) == False:
        if mp.player_pool_name is None:
            $ mp.player_pool = 0
        
            call player_pool from _call_player_pool_1
            $ mp.save()
    # if not mp.scale_tutorial:
    #     show image 'scale_tutorial.png'
    #     $ renpy.pause(9999)
    #     hide image 'scale_tutorial.png'
    #     $ mp.scale_tutorial = True
    #     $ mp.save()

    if not hasattr(store, 'fix_saves_23_6_23'):
        $ fix_saves_23_6_23 = True
        call screen fix_saves_23_6_23_screen
    return

label variables_at_start:
    python:

        create_nameboxes()
        #check_reports_start()
        #check_reports_from_json()
        try:
            if persistent.delete_bug_report_save:
                os.remove(os.path.join(renpy.config.gamedir, 'save_file-LT1.save'))
        except:
            pass

        persistent.delete_bug_report_save = False
        from_say_screen = False
        
        #sex_name_box = False
        
        if not hasattr(store, 'unlock_milf_costume'):

            milf_costume = 'n_body'
        if not hasattr(store, 'phone_sms_screen_update'):
            phone_sms_screen_update = True
            phone_sms_screen = {}

        if 'Мишванда' not in phone_sms_screen:
            phone_sms_screen['Мишванда'] = []

        if 'Марина' not in phone_sms_screen:
            phone_sms_screen['Марина'] = []

        if 'Игорь' not in phone_sms_screen:
            phone_sms_screen['Игорь'] = []
        if 'noname' not in phone_sms_screen:
            phone_sms_screen['noname'] = []
        if 'Кэт' not in phone_sms_screen:
            phone_sms_screen['Кэт'] = []
        if not hasattr(store, 'new_events_christie'):
            new_events_christie = False
        print("core/variables_at_start.rpy/line 29")
        Hide('text_animation')()
        Hide('info_panel')()
        # if getattr(store, 'milf_root_1_text', None) == _("Конец ивента") and not getattr(store, 'fix_milf_root_1_text', None):
        #     fix_milf_root_1_text = True
        #     block_milf_events = None
        #     add_to_gallery(20)
        #     smth_change_after_load = True
            
        #     print("smth_change_after_load : 65")


        if not hasattr(store, 'unlock_restroom'):
            
            unlock_restroom = False
            smth_change_after_load = True
            
            print("smth_change_after_load : 73")

        if not hasattr(store, 'unlock_milf_room'):
            
            unlock_milf_room = False
            smth_change_after_load = True
            
            print("smth_change_after_load : 80")

        if not hasattr(store, 'new_events'):
            new_events = True
            smth_change_after_load = True
            
            print("smth_change_after_load : 86")

        if not hasattr(store, 'descript_screen_3_list'):
            descript_screen_3_list = []
            smth_change_after_load = True
            
            print("smth_change_after_load : 92")

        if not hasattr(store, 'block_change_milf_position'):
            block_change_milf_position = 0
            smth_change_after_load = True
            
            print("smth_change_after_load : 98")


        if not hasattr(store, 'inventory'):
            inventory         = []
            smth_change_after_load = True
            print("smth_change_after_load : 104")
        if not hasattr(store, 'block_wash_posuda'):
            block_wash_posuda = True
            smth_change_after_load = True
            print("smth_change_after_load : 108")
        if not hasattr(store, 'block_stirka'):
            block_stirka      = True
            smth_change_after_load = True
            print("smth_change_after_load : 112")
        if not hasattr(store, 'block_uborka'):
            block_uborka      = True
            smth_change_after_load = True
            print("smth_change_after_load : 116")

        if not hasattr(store, 'relations_milf'):
            relations_milf   = 0
            smth_change_after_load = True
            print("smth_change_after_load : 121")

        if not hasattr(store, 'love_milf'):
            love_milf        = 0
            smth_change_after_load = True
            print("smth_change_after_load : 126")

        if not hasattr(store, 'milf_love_quests'):
            milf_love_quests = 0
            smth_change_after_load = True
            print("smth_change_after_load : 131")

        if not hasattr(store, 'block_gigiena'):
            block_gigiena = False
            smth_change_after_load = True
            print("smth_change_after_load : 136")
        if not hasattr(store, 'block_eat'):
            block_eat     = False
            smth_change_after_load = True
            print("smth_change_after_load : 140")
        if not hasattr(store, 'block_nastroi'):
            block_nastroi = False
            smth_change_after_load = True
            print("smth_change_after_load : 144")



        if not hasattr(store, 'love_sister'):
            love_sister = 0
            smth_change_after_load = True
            print("smth_change_after_load : 151")

        if not hasattr(store, 'relations_sister'):
            relations_sister = 0
            smth_change_after_load = True
            print("smth_change_after_load : 156")




        if not hasattr(store, 'money'):
            money         = 0
            smth_change_after_load = True
            print("smth_change_after_load : 164")
        if not hasattr(store, 'time'):
            time          = Time()
            time.time_now = 'evening'
            smth_change_after_load = True
            print("smth_change_after_load : 169")
        if not hasattr(store, 'location_now'):
            location_now = 'Corridor'
            smth_change_after_load = True
            print("smth_change_after_load : 173")

        if not hasattr(store, 'gigiena'):
            gigiena = 0
            smth_change_after_load = True
            print("smth_change_after_load : 178")

        if not hasattr(store, 'sitost'):
            sitost = 50
            smth_change_after_load = True
            print("smth_change_after_load : 183")


        if not hasattr(store, 'nastroi'):
            nastroi = 30
            smth_change_after_load = True
            print("smth_change_after_load : 189")

        if not hasattr(store, 'random_1_2_time'):
            random_1_2_time  = MyRandom(1, 2)
            smth_change_after_load = True
            print("smth_change_after_load : 194")

        if not hasattr(store, 'random_1_2_money'):
            random_1_2_money = MyRandom(1, 2)
            smth_change_after_load = True
            print("smth_change_after_load : 199")
        if not hasattr(store, 'random_1_3_time'):
            random_1_3_time  = MyRandom(1, 3)
            smth_change_after_load = True
            print("smth_change_after_load : 203")



        if not hasattr(store, 'igor_position'):
            
            igor_position = {
        'morning'   : ('City_Park',  'igor_park'),
        'afternoon' : ('City_Park',  'igor_park'),
        'evening'   : ('None',       'None'),
        'night'     : ('None',       'None'),
        
        }
            smth_change_after_load = True
            print("smth_change_after_load : 217")

        if not hasattr(store, 'milf_position'):
            milf_position = {
        'morning'   : ('Restroom',  'milf_restroom'),
        'afternoon' : ('Kitchen',   'milf_kitchen'),
        'evening'   : ('Hall',      'milf_evening_hall'),
        'night'     : ('Milf_Room', 'milf_room'),
        
        }
            smth_change_after_load = True
            print("smth_change_after_load : 228")
        if not hasattr(store, 'sister_position'):
            sister_position = {
            'morning'   : ['Hall',     'sister_hall'],
            'afternoon' : ['Restroom', 'sister_restroom'],
            'evening'   : ['None', '#0000'],
            'night'     : ['Sister_Room', 'sister_room_night'],
            

            } 
            smth_change_after_load = True
            print("smth_change_after_load : 239")

        if not hasattr(store, 'block_sister_home'):
            block_sister_home = False
            smth_change_after_load = True
            print("smth_change_after_load : 244")

        if not hasattr(store, 'block_milf_home'):
            block_milf_home   = False
            smth_change_after_load = True
            print("smth_change_after_load : 249")

        if not hasattr(store, 'block_time_forward'):
            block_time_forward = True
            smth_change_after_load = True
            print("smth_change_after_load : 254")

        if not hasattr(store, 'events'):
            events    = {}
            smth_change_after_load = True
            print("smth_change_after_load : 259")

        if not hasattr(store, 'completed_events'):
            print("starts from version 7")
            completed_events = []
            smth_change_after_load = True
            print("smth_change_after_load : 265")

        for i in events:
            tmp_event = events[i] 
            if not hasattr(tmp_event, "priority"):
                tmp_event.priority = 0
                smth_change_after_load = True
                print("smth_change_after_load : 272")

        if not hasattr(store, "sorted_events"):
            sorted_events = []
            smth_change_after_load = True
            print("smth_change_after_load : 277")


        if not hasattr(store, 'locations'):
            locations = {}
            smth_change_after_load = True
            print("smth_change_after_load : 283")

        if not hasattr(store, 'old_descript'):
            old_descript = '!'
            smth_change_after_load = True
            print("smth_change_after_load : 288")
        if not hasattr(store, 'old_descript_cat'):
            old_descript_cat = "!"
            old_descript_Cat = '!'
            smth_change_after_load = True
            print("smth_change_after_load : 292")

        if not hasattr(store, 'old_descript_Christie'):
            
            old_descript_Christie = '!'
            smth_change_after_load = True
            print("smth_change_after_load : 298")

        if not hasattr(store, 'descript_Christie'):
            descript_Christie = '!'
            smth_change_after_load = True
            print("smth_change_after_load : 303")


        if not hasattr(store, 'descript_Cat'):
            descript_Cat = '!'
            smth_change_after_load = True
            print("smth_change_after_load : 309")

        if not hasattr(store, 'descript_Misha'):
            descript_Misha = '!'
            smth_change_after_load = True
            print("smth_change_after_load : 314")

        if not hasattr(store, 'old_descript_Misha'):
            old_descript_Misha = '!'
            smth_change_after_load = True
            print("smth_change_after_load : 319")

        if not hasattr(store, 'descript'):
            descript = '!'
            smth_change_after_load = True
            print("smth_change_after_load : 324")

        if not hasattr(store, 'money_boost_labels_click_today'):
            money_boost_labels_click_today = []
            smth_change_after_load = True
            print("smth_change_after_load : 329")
        if not hasattr(store, 'money_boost_label_now'):
            money_boost_label_now          = 'money_boost_label'
            smth_change_after_load = True
            print("smth_change_after_load : 333")
        if not hasattr(store, 'set_locations_at_start'):
            smth_change_after_load = True
            print("smth_change_after_load : 336")
            set_locations_at_start = True
            Location(
                'Corridor',
                buttons = [{
                
                'Christie Room'      : ((330, 155, 172, 920,), Function(JumpToLocation, 'Sister_Room')),
                'Restroom'           : ((1221, 348, 78, 486,), Function(JumpToLocation, 'Restroom')),
                'Kitchen'            : ((0, 355, 290, 1079,),  Function(JumpToLocation, 'Kitchen')),
                'Hall'               : ((1710, 120, 209, 812,),Function(JumpToLocation, 'Hall')),
                'GG_Room'            : ((525, 280, 112, 640,), [Function(renpy.play, 'audio/door.mp3'), Function(JumpToLocation, 'GG_Room')]), 
                    
                }, ]
                )
            
            Location(
                'Sister_Room',
                buttons = []
                )
            
            Location(
                'Restroom',
                buttons = [{
                'Corridor'   : ((683, 995, 535, 80),  [Function(JumpToLocation, 'Corridor')]),
                'Crane'      : ((1312, 560, 289, 70), [Jump('ep1_gg_crane_label')]),
                'Locker'     : ((1651, 0, 252, 447,), [SetVariable('money_boost_label_now', 'restroom_locker_label'), Jump('money_boost_label')])
                
                },

                {
                'Shower Cabin' : ((407, 0, 390, 888,),   [Jump('restroom_shower_cabin_label')]),
                'Tumba Bath'   : ((1375, 806, 544, 273), [SetVariable('money_boost_label_now', 'restroom_tumba_bath_label'), Jump('money_boost_label')])
                }

                ]
                )
            
            Location(
                'Kitchen',
                buttons = [{
                'Corridor'     : ((1728, 0, 191, 1079), [Function(JumpToLocation, 'Corridor')]),
                }]
                )
            
            
            Location(
                'Hall',
                buttons = [{
                'Corridor'            : ((0, 77, 62, 901,), Function(JumpToLocation, 'Corridor')),
                'Milf Room'         : ((1370, 250, 100, 460,), Function(JumpToLocation, 'Milf_Room')),
                'tumba_under_tv'      :((1470, 725, 135, 180),   Jump('hall_tumba_under_tv_label')),
                'coffee_table_hairpin':((878, 705, 379, 173),   Jump('hall_coffee_table_hairpin_label')),
                },
                {'home_plant_2'   :((1729, 61, 190, 215),   Jump('hall_home_plant_2_label')),
                 'tv'             :((1480, 350, 270, 280),   Jump('hall_tv_label')),
                 'video_player'   :((1490, 699, 154, 45),   Jump('hall_video_player_label')),
                 },
                ]
                )
            
            Location(
                'Milf_Room',
                buttons = [{
                'Hall'     : ((683, 995, 535, 80), Function(JumpToLocation, 'Hall')),
                
                },
                
                 ])
            
            
            Location(
                'GG_Room',
                buttons = [{
                'Corridor'          : ((29, 98, 274, 866),    [Function(renpy.play, 'audio/door.mp3'), Function(JumpToLocation, 'Corridor')]),
                'Bed'               : ((470, 492, 666, 530),  [Jump('gg_room_bed')]),
                'PC'                : ((1388, 438, 166, 95,), [Jump('gg_room_pc')]),
                'Window'            : ((1744, 0, 175, 701),   [Jump('gg_room_window_label')]),
                'Systemist'         : ((1283, 613, 73, 161),  [Jump('gg_room_systemist_label')]),
                'Guitar'            : ((1378, 13, 334, 133,), [Jump('gg_room_guitar_label')]),
                
                'Picture'           : ((373, 180, 254, 240),  [Jump('gg_room_picture_label')]),
                

                },
                {
                'curbstone_hairpin' : ((675, 550, 200, 130,), [Jump('gg_room_curbstone_hairpin_label')]),
                }
                ]
                )
            
            for cor, lbl in [
            ((0, 650, 453, 429),     'washer'),
            ((717, 613, 710, 291,),  'bath')
                ]:
                locations['Restroom'].buttons[0].update({lbl: (cor, [Jump('restroom_'+lbl+'_label')])})
            
            
            
            
            for i in [

         ((27, 80, 322, 985),    'refrigerator'),
         ((1353, 504, 101, 143), 'coffee_maker'),
         ((1460, 590, 121, 68),  'toaster'),
            
                ]:
                locations['Kitchen'].buttons[0].update({i[1]:(i[0], [Jump('kitchen_'+i[1]+'_label')])})
            
            for cor, lbl in [
            ((784, 675, 90, 90),     'ottoman'),
            ((1381, 703, 223, 252,), 'tumba'),
            ((1401, 581, 176, 110,), 'home_plant'),
            ((641, 290, 145, 530,),  'cupboard'),
            ((1086, 378, 111, 351,), 'hanger'),
            ((102, 130, 145, 100,),  'picture_1'),
            ((35, 260, 167, 90,),    'picture_2'),
            ((1507, 231, 88, 270,),  'picture_3'),
                ]:
                locations['Corridor'].buttons[0].update({lbl: (cor, [SetVariable('money_boost_label_now', 'corridor_'+lbl+'_label'), Jump('money_boost_label')])})
            
            
            
            for cor, lbl in [
            ((1774, 260, 145, 310),  'books'),
            ((156, 140, 225, 249),   'home_plant_1'),
            ((636, 450, 105, 181),  'home_plant_3'),

            ((636, 450, 105, 181),  'home_plant_3'),
            
            ((400, 114, 70, 311), 'picture'),

                ]:
                locations['Hall'].buttons[0].update({lbl: (cor, [SetVariable('money_boost_label_now', 'hall_'+lbl+'_label'), Jump('money_boost_label')])})
                
                
                
                
                
                
                
                
                
                
                del cor    
                del lbl
            locations['Kitchen'].image_buttons = {
            'solar_oil': Jump('kitchen_solar_oil_label'),

            }
            
            locations['GG_Room'].image_buttons = {
            'bita' : Jump('gg_room_bita_label'),
            

            }
            
            locations['Restroom'].image_buttons = {
            'hair_pin' : Jump('restroom_hair_pin_label'),
            

            }
        if preferences.language not in (None, 'rus'):
            if getattr(store, 'gg', None):
                if gg == 'Семён':
                    gg = 'Donald' 







    return



label fixes_after_7_ep:

    # if getattr(store, 'descript_Christie', "~") == _("Конец рута Кристи для эпизода [version_now]"):

    #     call christie_root_8_0 from _call_christie_root_8_0

    #     $ smth_change_after_load = True

    #     $ print("core/variables_at_start.rpy : 520")

    if "City_Home" in getattr(store, "locations", [1, ]) and not getattr(store, "christie_get_root", False):
        
        $ unlock_sister_room = True

        $ descript_Christie = _("Найти подходящее время для беседы. Поговорить с Кристи Днём в Комнате.")

        $ Event('christie_root_1', 'Christie', time = ['afternoon'])

        $ sister_position['evening']   = ['None', 'sister_room']

        $ sister_position['afternoon'] = ['Sister_Room', 'sister_room']

        $ sister_position['night']     = ['Sister_Room', 'sister_room_night']

        $ locations['Sister_Room'].buttons = [{
        'Corridor'   : ((683, 995, 535, 80),  [Function(JumpToLocation, 'Corridor')]),},]


        $ christie_get_root      = True
        $ old_descript_Christie  = '!'
        $ unlock_sister_room     = True
        $ smth_change_after_load = True

        $ print("core/variables_at_start.rpy : 544")

    if hasattr(store, 'add_items_for_web_shop'):

        if get_item('Слабительное', True):
            $ remove_from_inventory('Слабительное')
            $ smth_change_after_load = True

            $ print("core/variables_at_start.rpy : 550")
    if hasattr(store, 'kat_shalost'):

        if get_item("Чёрные очки", True):
            $ smth_change_after_load = True

            $ print("core/variables_at_start.rpy : 557")

            $ remove_from_inventory("Чёрные очки")

    if not hasattr(store, 'add_items_for_web_shop_fixed'):
        $ smth_change_after_load = True
        $ add_items_for_web_shop_fixed = []

    if (
getattr(store, 'christie_root_26_end', False
) or getattr(store, 'descript_Christie', "~") == __("Конец рута Кристи для эпизода [version_now]")
) and not getattr(store, 'christie_root_27_start', False):


        call christie_root_27_activate from _call_christie_root_27_activate_1

        $ smth_change_after_load = True

        $ print("core/variables_at_start.rpy : 574")

    if getattr(store, 'milf_root_1_text', None) == _("Конец ивента") and not getattr(store, 'milf_root_9_text', None):


        $ print("smth_change_after_load : 583")
        $ smth_change_after_load = True
        call milf_root_9_0 from _call_milf_root_9_0
    if hasattr(store, 'gg'):
        $ nameboxes['GG'].name = gg
        $ nameboxes['GG'].create_text_obj()

    if hasattr(store, 'officer_name'):
        $ nameboxes['Officer'].name = officer_name
        $ nameboxes['Officer'].create_text_obj()
        

    if (hasattr(store, 'christie_root_38_end') or getattr(store, 'descript_Christie', "~") == _("Конец рута Кристи для эпизода [version_now]")) and not hasattr(store, 'tyan_falos_text'):

        
        call tyan_falos_0 from _call_tyan_falos_0
        $ smth_change_after_load = True
        $ print("core/variables_at_start.rpy : 594")
    
    if getattr(store, 'milf_root_9_text', None) == __("Конец ивента для эпизода [version_now]"):

        $ unlock_milf_costumes = True
        $ smth_change_after_load = True

        $ events.pop('milf_root_11', 0)
        $ events.pop('milf_root_13_end', 0)
        $ events.pop('milf_root_13', 0)
        $ events.pop('milf_root_12', 0)
        $ events.pop('milf_root_9', 0)

        $ print("smth_change_after_load : 688")
    if hasattr(store, 'events') and "milf_root_13_end" in events:

        $ events.pop('milf_root_11', 0)
        $ events.pop('milf_root_13', 0)
        $ events.pop('milf_root_12', 0)
        $ events.pop('milf_root_9', 0)
        $ print("core/variables_at_start.rpy : 652")

    python:
        if not hasattr(store, 'fix_for_completed_events'):
            if hasattr(store, 'completed_events'):
                completed_events_names = []
                for i in completed_events:
                    if type(i) == Event:
                        completed_events_names.append(i.name)

                completed_events = copy.deepcopy(completed_events_names)
                del completed_events_names
                fix_for_completed_events = True
                smth_change_after_load   = True
                print("core/variables_at_start.rpy : 652")
    
        if not all((
               hasattr(store, 'fix_ep2_12_trusi_bug_1'),
               hasattr(store, 'fix_ep2_12_trusi_bug_2'),
               hasattr(store, 'fix_ep2_12_trusi_bug_3'),
               hasattr(store, 'fix_ep2_12_trusi_bug_4'),
               )
               ):
        
            if 'ep2_12_corridor' in completed_events:
        
                if not hasattr(store, 'allowed_events'):
                    allowed_events = []
        
                if 'ep2_12_corridor' in allowed_events:
                    allowed_events.remove('ep2_12_corridor')
                    fix_ep2_12_trusi_bug_1 = True
        
                if 'ep2_12_milf' in allowed_events:
                    allowed_events.remove('ep2_12_milf')
                    fix_ep2_12_trusi_bug_2 = True

            if 'ep2_12_milf' in completed_events:
        
                if not hasattr(store, 'allowed_events'):
                    allowed_events = []
        
                if 'ep2_12_corridor' in allowed_events:
                    allowed_events.remove('ep2_12_corridor')
                    fix_ep2_12_trusi_bug_3 = True
        
                if 'ep2_12_milf' in allowed_events:
                    allowed_events.remove('ep2_12_milf')
                    fix_ep2_12_trusi_bug_4 = True
    
    if getattr(store, 'descript_Cat', '!') == _('Проследить за Кэт вечером у входа в дом.'):
        if not hasattr(store, 'kat_shalost'):
            $ Event('cat_root_4', 'City_Home', time = ['evening', ])
            $ smth_change_after_load = True

            $ print("smth_change_after_load : 750")
    
    if 'milf_root_10' in getattr(store, 'completed_events', (1, )):
        $ events.pop('milf_root_9', 0)
        $ smth_change_after_load = True

        $ print("smth_change_after_load : 754")
    python:
        if not hasattr(store, 'fix_for_completed_events_2'):
            completed_events_names = []
            for i in completed_events:
                if type(i) == Event:
                    if i.name not in completed_events_names:
                        completed_events_names.append(i.name)
                else:
                    if i not in completed_events_names:
                        completed_events_names.append(i)   
            completed_events = copy.deepcopy(completed_events_names)
            del completed_events_names
            fix_for_completed_events_2 = True
            smth_change_after_load   = True
            print("smth_change_after_load : 771")

        if len(getattr(store, 'completed_events', (1,))) > 220:
            
            if not hasattr(store, 'fix_for_image_buttons_at_locations_1'):
                fix_for_buttons_at_locations()
                fix_for_image_buttons_at_locations_1 = True
                smth_change_after_load   = True

        elif len(getattr(store, 'completed_events', (1,))) > 150:
            if not hasattr(store, 'fix_for_image_buttons_at_locations_2'):
                fix_for_buttons_at_locations()
                fix_for_image_buttons_at_locations_2 = True
                smth_change_after_load   = True
                print("smth_change_after_load : 784")


        elif len(getattr(store, 'completed_events', (1,))) > 80:
            if not hasattr(store, 'fix_for_image_buttons_at_locations_3'):
                fix_for_buttons_at_locations()
                fix_for_image_buttons_at_locations_3 = True
                smth_change_after_load   = True
                print("smth_change_after_load : 793")

        elif len(getattr(store, 'completed_events', (1,))) > 10:
            if not hasattr(store, 'fix_for_image_buttons_at_locations_4'):
                fix_for_buttons_at_locations()
                fix_for_image_buttons_at_locations_4 = True
                smth_change_after_load   = True
                print("smth_change_after_load : 800")


        
        if not hasattr(store, 'fix_for_hole_night'):

            if 'GG_Room' in getattr(store, 'locations', [1, ]):
                fix_for_buttons_at_locations()
                
                tmp_loc = locations['GG_Room']
                for tmp_time in ('morning', 'afternoon', 'evening', 'night'):

                    if "hole_night" in tmp_loc.image_buttons_times[tmp_time]:
                        
                        for i in locations:
                            tmp_loc = locations[i]
                            if i != 'GG_Room':
                                
                                if "hole_night" in tmp_loc.image_buttons_times[tmp_time]:
                                    
                                    tmp_loc.image_buttons_times[tmp_time].pop("hole_night", 0)
                    
                        fix_for_hole_night = True
                        smth_change_after_load = True
                        print("smth_change_after_load : 824")
                try:
                    del tmp_loc
                    del tmp_time
                    smth_change_after_load = True
                    print("smth_change_after_load : 828")
                except:
                    pass

    if hasattr(store, 'christie_root_38_end') and not hasattr(store, 'christie_root_39_start'):
        
        call christie_root_39_0 from _call_christie_root_39_0_1
        $ smth_change_after_load = True
        $ print("smth_change_after_load : 837")


    if not hasattr(store, 'city_click'):
        $ city_click = False
        $ smth_change_after_load = True
        $ print("smth_change_after_load : 843")

    if hasattr(store, 'christie_root_50_end') and not hasattr(store, 'christie_root_50_end_2'):
        call christie_root_50_end_label from _call_christie_root_50_end_label
        
        $ smth_change_after_load = True    
        $ print("smth_change_after_load : 849")
    if not hasattr(store, 'city_psi_loc_fix'):
        if hasattr(store, 'locations'):
            $ city_psi_loc_fix = True
            $ Location(
                    'City_Psi',
                    buttons = []
                    )
            $ smth_change_after_load = True
            $ print("smth_change_after_load : 858")

    if not hasattr(store, "fashion_store_events_items"):
        $ fashion_store_events_items   = {}
        $ mishwanda_store_events_items = {}
        $ smth_change_after_load = True
        $ print("smth_change_after_load : 864")
    python:
        if not hasattr(store, 'tyan_falos_7_fix'):
            if hasattr(store, 'events'):
                for j in range(1, 6):
                    i = 'tyan_falos_7_' + str(j)
                    if i in events:
                        if events[i].complete:
                            events.pop(i, 0)
                            tyan_falos_7_fix = True
                            smth_change_after_load = True
    if getattr(store, "christie_root_50_end_2", False) and not getattr(store, "christie_root_51_start", False):
        call christie_root_51_0 from _call_christie_root_51_0
        $ smth_change_after_load = True
        $ print("smth_change_after_load : 878")

    if not hasattr(store, "comic_frame_v3_swap"):
        $ comic_frame_v3_swap   = False
        $ comic_frame_v2_master = "#0000"
        $ comic_frame_v2_slave  = "#0000"
        $ comic_frame_v3_master = "#0000"
        $ comic_frame_v3_slave  = "#0000"
        $ smth_change_after_load = True
        $ print("smth_change_after_load : 885")
    
    if not hasattr(store, '_save_load_focus_on_show'):

        $ _save_load_focus_on_show = SaveLoadFocus()
        $ smth_change_after_load = True
        $ print("smth_change_after_load : 891")
    if hasattr(store, 'events') and events.get("christie_root_62"):
        $ fix_refrigerator()
        $ smth_change_after_load = True
        $ print("smth_change_after_load : 895")






    if not hasattr(store, '_events_pop_fix') and hasattr(store, 'events'):

        
        $ events.pop = events_pop

        $ _events_pop_fix = True
        $ smth_change_after_load = True
        
        $ print("smth_change_after_load : 910")



    if hasattr(store, 'events') and events.get("ep45_milf_54_hall"):
        if not events["ep45_milf_54_hall"].complete:


            #$ ep45_igor_fix = True
            $ smth_change_after_load = True
            $ descript = _("Марина предложила мне прогулять уборку и провести это время с ней.")
            $ print("smth_change_after_load : 927")
        else:
            $ events.pop('ep45_milf_54_hall', 0)
            $ ep45_milf_54_hall_complete_fix = True

    # if hasattr(store, 'ep45_igor_fix') and not hasattr(store, 'ep45_igor_fix_2'):
    #     $ ep45_igor_fix_2 = True

    #     $ igor_position = {
    #         'morning'   : ('City_Park',  'igor_park'),
    #         'afternoon' : ('City_Park',  'igor_park'),
    #         'evening'   : ('None',       'None'),
    #         'night'     : ('None',       'None'),
            
    #         }

    #     $ ep45_igor_fix = True
    #     $ smth_change_after_load = True
    #     $ print("smth_change_after_load : 935")

    # if not hasattr(store, 'christie_root_53_igor_fix') and events.get('christie_root_54'):
    #     if check_exist_event('ep45_milf_55_korridor'):
    #         #ИГОРЬ ФИКС 28_03_24__03_42
    #         $ christie_root_53_igor_fix = True

    #         $ igor_position = {
    #             'morning'   : ('City_Park',  'igor_park'),
    #             'afternoon' : ('City_Park',  'igor_park'),
    #             'evening'   : ('None',       'None'),
    #             'night'     : ('None',       'None'),
                
    #             }

    #         $ smth_change_after_load = True
    #         $ print("smth_change_after_load : 963")
    if not hasattr(store, 'igor_fix_block_igor_position'):
        if hasattr(store, 'completed_events'):
            if 'ep4_milf_37' in completed_events:
                $ igor_position = {
                    'morning'   : ('City_Park',  'igor_park'),
                    'afternoon' : ('City_Park',  'igor_park'),
                    'evening'   : ('None',       'None'),
                    'night'     : ('None',       'None'),
                    
                    }
                $ igor_fix_block_igor_position = True
    if not hasattr(store, 'block_igor_position'):
        if hasattr(store, 'completed_events'):

            if 'ep4_milf_37' in completed_events:
                if not check_exist_event('ep5_milf_72_2'):
                    call ep4_milf_37_block_igor from _call_ep4_milf_37_block_igor_1
                    $ igor_position = {
                    'morning'   : ('City_Park',  'igor_park'),
                    'afternoon' : ('City_Park',  'igor_park'),
                    'evening'   : ('None',       'None'),
                    'night'     : ('None',       'None'),
                    
                    }
                    #$ igor_fix_position_to_none = True
                    $ smth_change_after_load = True
                    $ print("smth_change_after_load : block_igor_position = True")

    if getattr(store, 'block_igor_position', False):
        if check_exist_event('ep5_milf_72_2'):
            $ block_igor_position = False
            $ igor_position = {
                    'morning'   : ('City_Park',  'igor_park'),
                    'afternoon' : ('City_Park',  'igor_park'),
                    'evening'   : ('None',       'None'),
                    'night'     : ('None',       'None'),
                    
                    }
            $ smth_change_after_load = True
            $ print("smth_change_after_load : block_igor_position = False")

    # if not hasattr(store, 'ep45_igor_fix') and any((
    #     check_exist_event('ep45_milf_55_korridor'), 
    #     hasattr(store, 'korridor_without_tree_ep5')

    #     )):

    #     $ igor_position = {
    #         'morning'   : ('City_Park',  'igor_park'),
    #         'afternoon' : ('City_Park',  'igor_park'),
    #         'evening'   : ('None',       'None'),
    #         'night'     : ('None',       'None'),
            
    #         }

    #     $ ep45_igor_fix = True
    #     $ smth_change_after_load = True
    #     $ print("smth_change_after_load : 914")


    if not hasattr(store, 'christie_night_mischief_text'):
        if hasattr(store, 'completed_events'):

            if 'christie_root_45_2' in completed_events:
                $ christie_night_mischief_text = _("Кристи мучают ночные кошмары. Стоит поговорить с ней об этом, может я смогу ей помочь.")
                $ tyan_mischief_text = _('Нужно попробовать "Пошалить" с Кристи днём, а не только ночью.')
                if not hasattr(store, 'christie_every_day_events_block'):
                    $ christie_every_day_events_block = []
                if not hasattr(store, 'christie_every_day_events'):
                    $ christie_every_day_events = []
                
                $ Event("christie_day_mischief", location = "Christie", button_name = "Дневные шалости", time = ["morning", "afternoon", "evening"])

                $ Event("christie_night_mischief", location = "Christie", button_name = "Ночные кошмары", time = ["morning", "afternoon", "evening"])
                $ christie_every_day_events.append('christie_night_mischief')
                $ christie_every_day_events.append('christie_day_mischief')
                $ new_events_christie = True
                $ smth_change_after_load = True
                $ print("smth_change_after_load : 952")


    if hasattr(store, 'christie_night_mischief_text'):
        if not hasattr(store, 'tyan_mischief_text'):

            $ tyan_mischief_text = _('Нужно попробовать "Пошалить" с Кристи днём, а не только ночью.')
            if not hasattr(store, 'christie_every_day_events_block'):
                $ christie_every_day_events_block = []
            if not hasattr(store, 'christie_every_day_events'):
                $ christie_every_day_events = []
            
            $ Event("christie_day_mischief", location = "Christie", button_name = "Дневные шалости", time = ["morning", "afternoon", "evening"])
            
            if 'christie_night_mischief' not in christie_every_day_events: 
                $ christie_every_day_events.append('christie_night_mischief')
            
            if 'christie_day_mischief' not in christie_every_day_events:
                $ christie_every_day_events.append('christie_day_mischief')
            
            $ new_events_christie    = True
            $ smth_change_after_load = True
            $ print("smth_change_after_load : 1379")






    if not hasattr(store, '_just_scene'):
        $ _just_scene = False
        $ smth_change_after_load = True
        $ print("smth_change_after_load : 966")
    
    if not hasattr(store, 'ep45_milf_54_hall_complete_fix_2'):

        if hasattr(store, 'ep45_milf_54_hall_complete_fix'):
            
            if 'ep5_milf_77' in completed_events:    
                
                $ descript     = ''
                $ old_descript = ''
                $ ep45_milf_54_hall_complete_fix_2 = True
                $ smth_change_after_load = True
                $ print("smth_change_after_load : 1006")
    if 'Гипноз' in descript_screen_3_list:
        $ descript_screen_3_list.remove('Гипноз')
        if 'Магия' not in descript_screen_3_list:
            $ descript_screen_3_list.append('Магия')
            $ smth_change_after_load = True
            $ print("smth_change_after_load : 1012")


    if 'Шантаж' in descript_screen_3_list:
        $ descript_screen_3_list.remove('Шантаж')
        if 'Грязная игра' not in descript_screen_3_list:
            $ descript_screen_3_list.append('Грязная игра')
            $ smth_change_after_load = True
            $ print("smth_change_after_load : 1020")
    
    $ j = get_item('Гипно-часы', True)
    
    if j:
        $ j.name  = 'Магические часы'
        $ j.image = 'images/interface/items/magic_clock_1.png'
        $ j.discription = ['Магические-часы, 1 ур.']
        $ j = None
        $ smth_change_after_load = True
        $ print("smth_change_after_load : 1030")

    if hasattr(store, 'christie_root_64_end') and not check_exist_event('christie_root_65'):
        
        $ descript_Christie = _("Поговорить со Сьюзен.")

        $ Event('christie_root_65', 'City_Psi', time = ['morning', 'afternoon'])
        
        $ smth_change_after_load = True
        
        $ print("smth_change_after_load : 1038")
    
    $ fix_city_shop()
    $ fix_ep5_milf_68_0()
    

    if hasattr(store, 'tyan_falos_text'):
        if 'Ванна' not in descript_screen_3_list:
            $ new_events_christie = True

            #$ smth_change_after_load = True
            
            #$ print("smth_change_after_load : 1081")
    
    if not hasattr(store, 'unlock_film_alexandr'): 
        if 'ep2_11_film' in getattr(store, 'completed_events', [1, ]):
            $ unlock_film_alexandr = True
            $ smth_change_after_load = True
            $ print("smth_change_after_load : 1082")
    
    if hasattr(store, 'milf_root_1_text'): 
        if not hasattr(store, 'gg_hungry_ep1075'):
            $ gg_hungry_ep1075 = True
            $ new_events = True
            $ smth_change_after_load = True
            
            $ print("smth_change_after_load : 1084")
        if not hasattr(store, 'unlock_film_kickboxer'):
            $ unlock_film_kickboxer = True
            
            $ smth_change_after_load = True
            
            $ print("smth_change_after_load : 1090")

    if "_public" in config.version:

        $ milf_costume = 'n_body'
        $ milf_night_costume_1 = "Night_Pose_1"
        $ milf_night_costume_2 = "Night_Pose_2"
        $ milf_night_costume_3 = "Night_Pose_3"

        $ smth_change_after_load = True
            
        $ print("smth_change_after_load : 1093")

    if not hasattr(store, 'special_loc_images_dir'):
        $ special_loc_images_dir = {}

        $ smth_change_after_load = True
            
        $ print("smth_change_after_load : 1309")

    if not from_gallery_check():

        if hasattr(store, 'gg') and mp.gg != gg:
            $ mp.gg = gg
            $ mp.save() 

            $ smth_change_after_load = True
                
            $ print("smth_change_after_load : 1102")
    if hasattr(store, 'christie_root_65_end') and hasattr(store, 'unlock_milf_costumes'):
        if not hasattr(store, 'final_act_start'):
            call final_act_setup from _call_final_act_setup_1
            $ smth_change_after_load = True
                
            $ print("smth_change_after_load : 1324")
            #$ christie_root_65_end = True
    if not hasattr(store, '_from_talk_with_milf'):
        $ _from_talk_with_milf = False

    if 'ep2_11_film' in completed_events and 'ep2_11_sms' not in events and 'ep2_11_sms' not in completed_events:

        $ Event('ep2_11_sms', 'GG_Room', time = ['morning'])
        $ smth_change_after_load = True
                
        $ print("smth_change_after_load : 1441")
            #$ christie_root_65_end = True
    if hasattr(store, 'gg'):
        $ player_name = gg
    python:
        i = getattr(store, 'events', (1,))
        if not hasattr(store, 'final_act_26_fix') and (
            'final_act_26_milf' in i or 'final_act_26_christie' in i or 'final_act_26_christie' in completed_events or 'final_act_26_milf' in completed_events):


            block_milf_events   = 'final_act_26_milf'
            block_sister_events = 'final_act_26_christie'
            

            block_change_milf_position_final_act_25 = copy.deepcopy(block_change_milf_position)
            block_change_milf_position   = True
            

            block_sister_home_final_act_25 = copy.deepcopy(block_sister_home)
            block_sister_home = False
            block_milf_home_final_act_25 = copy.deepcopy(block_milf_home)
            block_milf_home   = False

            block_time_forward_final_act_25 = copy.deepcopy(block_time_forward)
            block_time_forward = True

            block_exit_home_final_act_25 = copy.deepcopy(block_exit_home)
            block_exit_home = True


            milf_position['morning']     = ['Kitchen',   'milf_kitchen']
            milf_position['afternoon']   = ['Corridor',   'milf_corridor']
            milf_position['evening']     = ['Hall',   'milf_evening_hall']
            sister_position['morning']   = ['Hall', 'sister_hall']
            sister_position['afternoon'] = ['Hall', 'sister_hall']
            sister_position['evening'] = ['Sister_Room', 'sister_room']

            time.time_now  = 'morning'
            final_act_26_fix = True
            milf_costume     = 'n_body'
            gigiena        = 100
            sitost         = 100
            nastroi        = 100
            smth_change_after_load = True
            print("smth_change_after_load : 1543")

        if not hasattr(store, 'sex_name_box'):
            sex_name_box = False
            smth_change_after_load = True
            print("smth_change_after_load : 1567")
        
        # if mp.fix_achievement__30_04_24 is None:
        
        #     if hasattr(store, 'achievement'):
        #         achievement.clear_all()
        #         achievement.sync()
        #         smth_change_after_load = True
        #         print("smth_change_after_load : 1573")
        #         mp.fix_achievement__30_04_24 = True
        #         mp.save()

        if not hasattr(store, 'ACH_21_count'):
            ACH_21_count = 0
            smth_change_after_load = True
            print("smth_change_after_load : 1582")


        if not hasattr(store, 'ACH_5_count'):
            ACH_5_count = [False, False, False, False]
            smth_change_after_load = True
            print("smth_change_after_load : 1574")
    #if preferences.language in (None, 'eng'):
    if getattr(store, 'descript_Misha', None) == '!':
        if check_exist_event('christie_root_13'):
            call misha_root_0 from _call_misha_root_0_1
            $ smth_change_after_load = True
            $ print("smth_change_after_load : 1588")

    if 'final_act_27' in getattr(store, 'completed_events', (1, )):
        if not hasattr(store, 'final_act_27_end__30_04_24_19_00'):
            call final_act_27_python from _call_final_act_27_python_1
            $ smth_change_after_load = True
            $ print("smth_change_after_load : 1594")
    if not hasattr(store, 'cupon_buy_pc'):
        $ cupon_buy_pc = False
        $ smth_change_after_load = True
        $ print("smth_change_after_load : 1590")

    if not hasattr(store, 'cupon_search_game'):
        $ cupon_search_game = False
        $ smth_change_after_load = True
        $ print("smth_change_after_load : 1595")


    if not hasattr(store, 'cupon_zanachka'):
        $ cupon_zanachka = False
        $ smth_change_after_load = True
        $ print("smth_change_after_load : 1601")

    $ i = getattr(store, "locations", [1, ])
    if not hasattr(store, 'cupons_city_home_update'):
        if "City_Home" in i:
            $ cupons_city_home_update = True

            $ locations['City_Home'].image_buttons.update({'keks':Jump('keks_city_home')}) 

        $ smth_change_after_load = True
        $ print("smth_change_after_load : 1611")

    if not hasattr(store, 'cupons_corridor_update'):
        if "Corridor" in i:
            $ cupons_corridor_update = True

            $ locations['Corridor'].image_buttons.update({'keks':Jump('keks_corridor_home')}) 

        $ smth_change_after_load = True
        $ print("smth_change_after_load : 1620")


    if not hasattr(store, 'cupons_hall_update'):
        if "Hall" in i:
            $ cupons_hall_update = True

            $ locations['Hall'].image_buttons.update({'keks':Jump('keks_hall_home')}) 

        $ smth_change_after_load = True
        $ print("smth_change_after_load : 1630")


    if not hasattr(store, 'cupons_christie_room_update'):
        if "Sister_Room" in i:
            $ cupons_christie_room_update = True

            $ locations['Sister_Room'].image_buttons.update({'keks':Jump('keks_christie_room_home')}) 

        $ smth_change_after_load = True
        $ print("smth_change_after_load : 1640")

    if not hasattr(store, 'cupons_city_shop_update'):
        if "City_Shop" in i:
            $ cupons_city_shop_update = True

            $ locations['City_Shop'].image_buttons.update({'keks':Jump('keks_city_shop_home')}) 

        $ smth_change_after_load = True
        $ print("smth_change_after_load : 1650")


    if not hasattr(store, 'cupons_prison_update'):
        if "Prison" in i:
            $ cupons_prison_update = True

            $ locations['Prison'].image_buttons.update({'keks':Jump('keks_prison_home')}) 

        $ smth_change_after_load = True
        $ print("smth_change_after_load : 1650")

    if not hasattr(store, 'inventory_drugs_fix'):
        $ i = get_item('Товар', True)
        if i:
            $ j = i.quant
            $ inventory.remove(i)
            $ add_to_inventory(name = 'Товар', quant = j)
            $ inventory_drugs_fix = True
            $ smth_change_after_load = True
            $ print("smth_change_after_load : 1670")


    if not hasattr(store, 'inventory_keks_coupon_fix'):
        $ i = get_item('Купон «кекса»', True)
        if i:
            $ j = i.quant
            $ inventory.remove(i)
            $ add_to_inventory(name = 'Купон «кекса»', quant = j)
            $ inventory_keks_coupon_fix = True
            $ smth_change_after_load = True
            $ print("smth_change_after_load : 1680")
    
    if getattr(store, 'jun_2024_dlc', False):
    
        if not hasattr(store, 'steam_bonus_1_0_start'):
            if 'ep3_2_morning' in completed_events:
                $ steam_bonus_1_0_start = True
                $ Event('steam_bonus_1_0', location = 'Kitchen_Milf')
                $ smth_change_after_load = True
                $ print("smth_change_after_load : 1689")
    
        
        if not hasattr(store, 'steam_bonus_2'):
            if 'christie_root_17' in completed_events:
                $ steam_bonus_2 = True
                $ Event('steam_bonus_2', location = 'Hall_Milf', time = ["afternoon",])
                $ smth_change_after_load = True
                $ print("smth_change_after_load : 1697")
    
        if not hasattr(store, 'steam_bonus_3'):
            if 'christie_root_45' in completed_events:
                $ steam_bonus_3 = True
                $ Event('steam_bonus_3', location = 'gg_room_pc_enter', time = ["morning", "afternoon", "evening"])
                $ smth_change_after_load = True
                $ print("smth_change_after_load : 1704")
    

        if not hasattr(store, 'steam_bonus_4'):
            if 'christie_root_17' in completed_events:
                $ steam_bonus_4 = True
                $ Event('steam_bonus_4', location = 'Kitchen', time = ["evening",])
                $ smth_change_after_load = True
                $ print("smth_change_after_load : 1712")
        
        if hasattr(store, 'block_time_forward_final_act_1'):
            $ block_time_forward = False
            $ smth_change_after_load = True
            $ print("smth_change_after_load : 1717")
        if getattr(store, 'descript', None) == __('Конец ивента для эпизода [version_now]'):
            $ descript = __('Конец рута Марины.')
            $ smth_change_after_load = True
            $ print("smth_change_after_load : 1721")
        if getattr(store, 'descript_Misha', None) == __('Конец ивента для эпизода [version_now]'):
            $ descript_Misha= _("Конец рута Мишванды")
            $ smth_change_after_load = True
            $ print("smth_change_after_load : 1721")
    return
# Decompiled b




label keks_city_home:
    $ locations['City_Home'].image_buttons.pop('keks', 0)
    jump keks_main
label keks_corridor_home:
    $ locations['Corridor'].image_buttons.pop('keks', 0)
    jump keks_main
label keks_hall_home:
    $ locations['Hall'].image_buttons.pop('keks', 0)
    jump keks_main
label keks_christie_room_home:
    $ locations['Sister_Room'].image_buttons.pop('keks', 0)
    jump keks_main
label keks_city_shop_home:
    $ locations['City_Shop'].image_buttons.pop('keks', 0)
    jump keks_main
label keks_prison_home:
    $ locations['Prison'].image_buttons.pop('keks', 0)
    jump keks_main

label keks_main:

    $ add_to_inventory(name = 'Купон «кекса»', ncopy = True)
    show screen give_item_screen(i_path+'/items/keks.png', _('Купон «кекса»'),[_('Коллекционный купон, '), _('Но сейчас эта самая ходовая валюта'), _('на чёрном рынке.')])
    with Dissolve(.5)
    $ renpy.pause(9999)
    hide screen give_item_screen
    with Dissolve(.5)
    jump main_interface_label