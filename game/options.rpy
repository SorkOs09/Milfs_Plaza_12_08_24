 




DSDFDFDF




image shadow_up   = Crop((0,0,1920,300), 'interface/shadow.png')    

image shadow_down = Crop((0,780,1920,300), 'interface/shadow.png')

image shadow_full = 'interface/shadow.png'

image button_no = 'images/interface/Button_No.png'

image button_no hover = im.MatrixColor('images/interface/Button_No.png', im.matrix.brightness(.3))

label check_gallery_label:
    if persistent.from_main_menu_gallery or persistent.from_pc_gallery:
        scene black 
        with my_dissolve

        $ persistent.from_main_menu_gallery = None
        $ persistent.from_pc_gallery        = None
        $ renpy.full_restart()




    return



define version_now = "steam_14"
#abcdefghijk lmnopqrstuvwxyz
define sub_version_now = "c"

define config.version = "steam_14c"

init -3000 python:
    import copy
    import pygame
    import datetime
    renpy.music.register_channel('ero', loop = True) 
    config.allow_underfull_grids = True
    config.image_cache_size      = 6000
    config.image_cache_size_mb   = 6000
    config.cache_surfaces        = False

    skip_loading                 = True
    from_test                    = False



    mp         = MultiPersistent("MilfsPlaza2022")
    list_files = renpy.list_files()
    i_path     = 'images/interface/'
    if mp.gallery is None:
        mp.gallery = [
         
        ]
        mp.save()

    mp.skip_loading = True
    
    if mp.interface_scale is None:
        mp.interface_scale = 10
        mp.interface_scale_number = 1.0

        mp.dialogue_interface_scale = 10
        mp.dialogue_interface_scale_number = 1.0
    mp.save()



    if mp.gallery_images is None:
        mp.gallery_images = [
         
        ]
        mp.save()


    def reset_perisistent_from_gallery():
        persistent.from_main_menu_gallery = None
        persistent.from_pc_gallery        = None


    def set_mp_tutorial(value):
        mp.tutorial = value
        mp.save()

    def from_gallery_check():
        global persistent
        if persistent.from_main_menu_gallery or persistent.from_pc_gallery:
            return True
    
    def get_store_lists():
        r = []
        for i in dir(store):
            if type(getattr(store, i, None)) in (dir, list):
                r.append(i)
        return r
    def fix_ep5_milf_68_0():
        try:
            if store.events.get('ep5_milf_68_0'):
                store.events.pop('talk_with_clothes_store_woman_menu')


        except:
            pass
            

    def fix_city_shop():
        try:
            i = 0
            times = store.locations['City_Shop'].image_buttons_times
            for j in times:
                if not len(times[j]):
                    i += 1
            if i >= 4:
                store.locations['City_Shop'].image_buttons_times = {
                'morning'   : {
                'jay_bob': Jump('talk_with_jay_bob_label'),
                'door' : [Function(JumpToLocation, 'StoreIn')],
                },
                'afternoon' : {
                'jay_bob': Jump('talk_with_jay_bob_label'),
                'door' : [Function(JumpToLocation, 'StoreIn')],
                },
                'evening'   : {
                'door' : [Function(JumpToLocation, 'StoreIn')],
                },
                'night'     : {

                },
                }
        except:
            pass
        
    
    def fix_refrigerator(): 

        locations['Kitchen'].buttons[0].update({
            'refrigerator':(
                (27, 80, 322, 985), [Jump('kitchen_refrigerator_label')])
            }
            )
            
    def add_to_gallery(i):
        if i not in mp.gallery:
            mp.gallery.append(i)
            mp.save()
            show_text_animation(__('Открыта новая сцена в галерее!'))

    def set_new_patch(patch = '1.0a'):
        global persistent 
        persistent.new_patch = patch


    def change_language(language):
        global mp
        mp.language = language
        mp.save()
        if language == 'RUS':
           renpy.change_language(None)
        else:
        
            renpy.change_language(language.lower())
        
        #create_nameboxes()
        renpy.reload_script()
    def get_custom_language_font(language):
        language = str(language)
        if language.lower() in ('chinese_trad', 'chinese_simpl', 'jap'):
            return "fonts/asian_font.ttc"
        
        elif language.lower() == "kor": 
            return "fonts/kor_font.ttf"


    def change_language_confirm(language):
        global mp, renpy, tmp_language
        tmp_language = language
        texts = {
        "RUS" :["Игра будет перезапущена", "Да", "Нет", ],

        "ENG" :["The game will restart", "Yes", "No", ],

        "FRENCH" :["Ce jeu va redémarrer", "Oui", "Non", ],

        "DUTCH" :["Het spel zal herstarten", "Ja", "Nee", ],

        "SPN" :["El juego reiniciará", "Sí", "No", ],


        "POR" :["O jogo ira reiniciar", "Sim", "Não", ],

        "GERM" :["Das Spiel wird neu gestartet", "Ja", "Nein", ],

        "POL" :["Gra zostanie zresetowana", "Tak", "Nie", ],

        "TURK" :["Oyun yeniden başlatılacak", "Evet", "Hayır", ],

        "JAP" :["ゲームが再開されます", "はい。", "いいえ。", ],

        "CHINESE_TRAD" :["遊戲將重新啟動", "是的。", "不。", ],

        "CHINESE_SIMPL" :["游戏将重新启动", "是的，退出。", "点错了。", ],

        "KOR" :["게임이 다시 시작됩니다", "예", "아니요", ],

        }
        
        texts = texts[tmp_language]

        note = texts[0]
        yes  = " " + texts[1] + " "
        no   = " " + texts[2] + " "


        font = get_custom_language_font(language) or "fonts/ProximaNova-Light.ttf"
        
        renpy.show_screen('confirm', 
            note, 
            Function(change_language, language), Hide('confirm'), 
            yes, no, font)





    def Ani(img_name, frames, delay=.1, loop=True, reverse=True, effect=None, start=1, ext='png', **properties):
        
        args = []
        
        
        
        if isinstance(delay, tuple):
            
            d0 = delay[0]
            
            d1 = delay[1]
            
            f = (frames - 1)
            
            if f <= 0:
                
                dp = 0
            
            else:
                
                dp = (d1 - d0) * 1.0 / f
            
            delay = d0
        
        else:
            
            dp = 0
        
        
        
        for i in range(start, start + frames):
            
            if ext:
                
                img = renpy.display.im.image(img_name + str(i) + "." + ext)
            
            else:
                
                img = renpy.easy.displayable(img_name + str(i))
            
            img = Transform(img, **properties)
            
            args.append(img)
            
            if reverse or loop or (i < start + frames - 1):
                
                args.append(delay)
                
                delay += dp
                
                
                
                args.append(effect)
        
        if reverse: 
            
            dp = -dp
            
            delay += dp
            
            for i in range(start + frames - 2, start, -1):
                
                if ext:
                    
                    img = renpy.display.im.image(img_name + str(i) + "." + ext)
                
                else:
                    
                    img = renpy.easy.displayable(img_name + str(i))
                
                img = Transform(img, **properties)
                
                args.append(img)
                
                if loop or (i > start + 1):
                    
                    args.append(delay)
                    
                    delay += dp
                    
                    args.append(effect)
        
        return anim.TransitionAnimation(*args)



label debug_exit:
    scene black
    show image Text('DEBUG: Конец ивента, выход из игры.'):
        align (.5, .5)
    with my_dissolve_fast
    $ renpy.pause(.5, hard = True)
    $ renpy.pause(3)
    

    $ renpy.quit()

screen subscribe_buttons_screen:
    pass
    # if not preferences.language:
    #     add 'gui/boosty_button.png'
    #     imagebutton:
    #         idle 'gui/boosty_button.png'
    #         hover im.MatrixColor('gui/boosty_button.png', im.matrix.brightness(.3))
    #         focus_mask True
    #         at ButtonEffect01
    #         action OpenURL('https://boosty.to/texic')


    # else:
    #     add 'gui/subscribestar_button.png'
    #     imagebutton:
    #         idle 'gui/subscribestar_button.png'
    #         hover im.MatrixColor('gui/subscribestar_button.png', im.matrix.brightness(.3))
    #         focus_mask True
    #         at ButtonEffect01

    #         action OpenURL('https://subscribestar.adult/texic')

    #     add 'gui/patreon_button.png'
    #     imagebutton:
    #         idle 'gui/patreon_button.png'
    #         hover im.MatrixColor('gui/patreon_button.png', im.matrix.brightness(.3))
    #         focus_mask True
    #         at ButtonEffect01

    #         action OpenURL('https://patreon.com/Texic')


screen debug_check_sms_translate():
    pass
    imagebutton: 
        idle  '#000a'
        hover '#000a'
        action Hide('debug_check_sms_translate')
    default who = 'Игорь'


    zorder 20
    viewport:
        xalign .5
        ypos 150
        maximum (900, 800)
        image '#000a'
        hbox:
            xalign .5
            spacing 5
            for i in phone_sms_screen:
                textbutton i action SetScreenVariable('who', i)
    viewport:
        xalign .5
        ypos 200
        maximum (900, 750)
        scrollbars 'vertical'
        mousewheel True
        vbox:

            $ r = 0
            for i in phone_sms_screen[who]:
                for j in i.list:
                    if j == __(j):
                        text str(r) + '. ' + j size 25
                        $ r += 1

screen change_language_debug:
    zorder 4500
    image '#000b'
    style_prefix "choice"
    #default text_now = ''
    viewport:
        image 'alpha_solid'
        imagebutton: 
            idle  'alpha_solid'
            hover 'alpha_solid'
            action Hide('change_language_debug')
    viewport:
        image 'alpha_solid'
        align (.5, .5)
        maximum (800, 870)
        imagebutton: 
            idle  'alpha_solid'
            hover 'alpha_solid'
            action NullAction()
    vbox yalign .5:
        spacing 10
        for i in (
('RUSSIAN'     , 'rus'),
('ENGLISH'    , 'eng'),
('CHINESE (SIMPL)' ,  "chinese_simpl"),
('CHINESE (TRAD)' , "chinese_trad"),    
('FRENCH'     , 'french'),  
('DUTCH'      , 'dutch'),   
('SPANISH'    , 'spn'), 
('PORTUGUESE' , 'por'),
('GERMAN'   , 'germ'),  
('POLISH'   , 'pol'),  
('TURKISH'  , 'turk'), 
#('THAI'     , 'thai'),    
#('ITALIAN'  , 'ital'), 
('JAPANESE' , 'jap'),    
('KOREAN' , 'kor'),

        ):
            
            textbutton i[0]:
                
                action Function(renpy.change_language, i[1]), Hide('change_language_debug')


screen debug_screen:
    pass


    # if store.test_debug_mod:

    #(20, 280)
    #(380, 300) 
    #(1060, 218)
    #(1250, 280)
    #

screen debug_say_screen:
    pass
    if store.test_debug_mod:
        vbox:
            ypos 800
            xalign 1.0
            textbutton "Test biblio_1" text_outlines [(3, '#000c', 0, 0)] action Jump('biblio_mini_games_test_start')  xalign 1.0
            
        #     textbutton str(preferences.language) + " (Change)" action Show('change_language_debug')
        #     textbutton "Test Jump" text_outlines [(3, '#000c', 0, 0)] action Jump('final_act_25_0')  xalign 1.0
        
        #     textbutton "Test SMS" text_outlines [(3, '#000c', 0, 0)]  action  Show('debug_check_sms_translate') xalign 1.0
        
        text str(renpy.game.context().next_node.filename.replace('game', '')) + " : " + str(renpy.game.context().next_node.linenumber):
            outlines [(3, '#000c', 0, 0)]
            align (.5, 1.0)
        vbox:

            xalign 1.0
            ypos 20
                
            for name in renpy.get_showing_tags():
                $ attributes = " ".join(renpy.get_attributes(name))
                

                if name in store.custom_sprites:
                    hbox:
                        text _("[name] [attributes] ") outlines [(3, '#000c', 0, 0)] 
                        textbutton "change" text_outlines [(3, '#000c', 0, 0)] ypos -5 action Show('change_sprite_screen', sprite = name, attributes = attributes) #NullAction()# Function(sprites_variants[name].set_sprite), SetVariable("show_sprite_editor", name)
                        xalign 1.0
                

            hbox:
                ypos 20
                
                textbutton "change music" text_outlines [(3, '#000c', 0, 0)] ypos -5 action Function(open_change_music_screen) #Show("change_music_screen")


init -3000 python:
    store.patreon_cheats       = False
    store.test_debug_mod       = True
    store.test_debug_mod_exit  = False
    store.test_debug_mod_next  = False
    store.test_debug_mod_ach   = True

    store.test_debug_mod_ach_test = False
    
    store.test_debug_mod_unren = False
    
    if store.test_debug_mod_ach:
        if hasattr(store, 'achievement'):
            if hasattr(store.achievement, 'register'):
                for i in range(24):

                    achievement.register("ACH_"+str(i))


    def debug_exit():
        if store.test_debug_mod_exit:
            renpy.jump('debug_exit')

    def debug_next(label):
        if store.test_debug_mod_next:
        
            renpy.jump(label)

    def add_ach(name):
        pass
        if store.test_debug_mod_ach:
            if mp.fix_achievement__30_04_24_2 is None:
            
                if hasattr(store, 'achievement'):
                    achievement.clear_all()
                    achievement.sync()
                    mp.fix_achievement__30_04_24_2 = True
                    mp.save()

            if '_test' in name:
                if store.test_debug_mod_ach_test:
                    name = name.replace('_test', '')
                else:
                    return
            achievement.grant(name)
            achievement.sync()
    

define config.name = _("MilfsPlaza")



define config.steam_appid = 2706300

define achievement.steam_position = "bottom right"

define gui.show_name = True

define my_dissolve_fast = { "master" : Dissolve(.1) }

define my_dissolve = { "master" : Dissolve(.3) }


define my_dissolve_long = { "master" : Dissolve(.7) }




define my_dissolve_very_long = { "master" : Dissolve(1.0) }


define my_vpunch = { "master" : vpunch }





define gui.about = _p("""
""")






define build.name = "MilfsPlaza"








define config.has_sound = True
define config.has_music = True
define config.has_voice = True













define config.main_menu_music = "audio/menu.mp3"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"

define config.has_autosave = True
define config.autosave_on_choice = True



define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0

default gg = ' Donald '
default milf_costume = 'n_body'
default christie_costume = 'n_body'
default milf_night_costume_1 = "Night_Pose_1"
default milf_night_costume_2 = "Night_Pose_2"
default milf_night_costume_3 = "Night_Pose_3"


default preferences.afm_time = 15
















define config.save_directory = "MilfsPlaza_new_0_5-1659188210"






define config.window_icon = "gui/window_icon.png"






init -1000 python:









    try:
        platform = str(renpy.platform)
    except:
        platform = "os unknown"
    #try:
     #   pl




    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    if not store.test_debug_mod_unren:
        build.classify('game/core/unreen/unren-dev.rpyc', None)



        build.classify('game/core/unreen/unren-quick.rpy', None)

        build.classify('game/core/unreen/unren-quick.rpyc', None)

        build.classify('game/core/unreen/unren-rollback.rpy', None)

        build.classify('game/core/unreen/unren-rollback.rpyc', None)

        build.classify('game/core/unreen/unren-skip.rpy', None)

        build.classify('game/core/unreen/unren-skip.rpyc', None)

    build.archive("scripts", "all")

    build.archive("images", "all")

    build.archive("live2d", "renpy")


    build.archive("videos", "all")

    build.archive("audios", "all")

    build.archive("others", "all")

    build.archive("tl", "all")



    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify('game/**.mp4', None)

    build.classify('game/**.xlsx', None)
    build.classify('game/**.py', None)

    build.classify('game/dev.rpyc', None)
    build.classify('game/**.rpy', None)
    build.classify('game/**.zip', None)
    build.classify("game/**.psd", None)

    build.classify(".for_pc/**", None)
    
    build.classify(".for_android/**", None)
    
    build.classify("game/**.mov", None)

    build.classify("game/test_saves/**.**", None)


    # build.classify("game/images/cg/ep85/officer_milf_sex/1.png", None)
    # build.classify("game/images/cg/ep85/officer_milf_sex/1.png", None)
    # build.classify("game/images/cg/ep85/officer_milf_sex/2.png", None)
    # build.classify("game/images/cg/ep85/officer_milf_sex/3.png", None)
    # build.classify("game/images/cg/ep85/officer_milf_sex/4.png", None)
    # build.classify("game/images/cg/ep85/officer_milf_sex/5.png", None)
    # build.classify("game/images/cg/ep85/officer_milf_sex/6.png", None)
    # build.classify("game/images/cg/ep85/officer_milf_sex/7.png", None)


    images_exts_list = ('png', 'jpg', 'jpeg', 'webp')

    for i in images_exts_list:

        build.classify('game/images/*.'+i,  'images')
        
        build.classify('game/gui/**.'+i,  'images')
        
        for j in ('cg', 'for_android', 'for_web', 'interface', 'locations', 'mini_games', 'tests'):
            build.classify('game/images/'+j+'/**.'+i,  'images')
        




    build.classify("game/images/characters/M1.png", "images")

    build.classify("game/presplash.png", "images")

    for i in (
    'GG',
    'BlackGuy',
    'Officer',
    'Christie',
    'Jay',
    'Bob',
    'Igor',
    'Misha',
    'Psi',
    'GirlInStore',
    'WomanTrade',
    'RestAdmin',
    'RestFamily',
    'Nikolaya',
    'Kat',
    'Bandit',
    'Masha',
    'BandtiWithPistol',
    'BiblioGirl',
    ):


        build.classify('game/images/characters/' + i + '**.png',  'images')
        build.classify('game/images/characters/' + i + '**.jpg',  'images')
        build.classify('game/images/characters/' + i + '**.jpeg', 'images')
        build.classify('game/images/characters/' + i + '**.webp', 'images')


    build.classify('game/Resources/**.**', 'live2d')

    build.classify('game/**.webm', 'videos')
    build.classify('game/**.ogg',  'audios')
    build.classify('game/**.ogg',  'audios')
    build.classify('game/**.mp3',  'audios')
    build.classify('game/**.mp3',  'audios')




    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/**.rpyc', 'scripts')

    build.classify('game/**.ttf',  'others')
    build.classify('game/**.ttf',  'others')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
