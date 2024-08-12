init python:
    SplashScreenText = [
'Данная игра содержит насилие;', 
'Откровенные, непристойные сцены, грубый юмор, кровь, употребление алкоголя, грубые выражения и прочие непотребства.',

'Команда разработчиков - это многонациональная команда, которая не несёт целей кого-то оскорбить или обидеть.',

'Все герои вымышлены, все события плод фантазии.',

'Все персонажи совершеннолетние.',

'',


'{size=50}Игра предназначена для лиц строго {color=#B20000}18+{/color} лет.{/size}' 

]
    SplashScreenTextEng = [
'This game contains income;', 
'Explicit, obscene scenes, crude humor, blood, alcohol consumption, coarse language and other obscenities.',

'The development team is a multinational team that does not intend to offend or offend anyone.',

'All characters are fictitious, all events are the fruits of fantasy.',

'All characters are adults.',
'',
'{size=50}The game is intended for persons strictly {color=#B20000}18+{/color} years of age.{/size}'
    ]


screen ScreenSplashScreenScale:
    zorder 1000
    imagebutton:
        idle '#000'
        hover '#000'
        action NullAction()
    text __('Сбросить скейл интерфейса до значения по умолчанию?'): 
        align (.5, .5)
        font gui.interface_text_font


    viewport xalign .5 yalign .9:
        xmaximum 1185
        ymaximum 50
        add '#0000'
        button:
            add 'simple_button'
            action Return(True)
        text __("Да"): 
            align (.5, .5)
            font gui.interface_text_font
    viewport xalign .5 yalign .95:
        xmaximum 1185
        ymaximum 50
        add '#0000'
        button:
            add 'simple_button'
            action Return(False)
        text __("Нет"): 
            align (.5, .5)
            font gui.interface_text_font


image simple_button:

    on idle:
        'gui/button/choice_hover_background.png'
    on hover:

        im.MatrixColor('gui/button/choice_hover_background.png', im.matrix.brightness(.5)) with Dissolve(.2)
screen ScreenSplashScreen:
    
    if mp.language == 'RUS':
        default _text = SplashScreenText
    else:
        default _text = SplashScreenTextEng
    zorder 1000
    imagebutton:
        idle 'black'
        hover 'black'
        action NullAction()
    #text '18+' xalign .5 yalign .2
    vbox:
        xalign .5 yalign .5
        
        for i in _text:
            text i xalign .5 size 30
        # text '' xalign .5 size 30
        # text "The game currently has some problems with other languages (not English)." xalign .5 size 40 font gui.interface_text_font color '#F00c'
        # text "We quickly fix bugs, we apologize for the inconvenience!" xalign .5 size 40 font gui.interface_text_font color '#F00c'
    vbox:
        align (.5, .85)
        spacing 15
        viewport:
            xmaximum 1185
            ymaximum 50
            image 'alpha_solid'
            button:
                add 'simple_button'
                action Return()
            text 'OK' xalign .5 ypos 5 font gui.interface_text_font
        viewport:
            xmaximum 1185
            ymaximum 50
            image 'alpha_solid'
            button:
                add 'simple_button'
                action Quit()
            text 'EXIT' xalign .5 ypos 5 font gui.interface_text_font
label splashscreen:


    #$ from_say_screen = False
    #"" "?!"
    # menu:

    #     "Test Mary scene 1":
    #         $ persistent.from_main_menu_gallery =  "steam_bonus_1_0"

    #     "Test Mary scene 2":
    #         $ persistent.from_main_menu_gallery =  "steam_bonus_2_0"

    #     "Test Christie scene 1":
    #         $ persistent.from_main_menu_gallery =  "steam_bonus_3"
           
    #     "Test Christie scene 2":
    #         $ persistent.from_main_menu_gallery =  "steam_bonus_4"

    #     "Test Christie scene 3":
    #         $ persistent.from_main_menu_gallery =  "tyan_falos_9"


    # return
    python:
        if store.test_debug_mod:
            i = os.path.join(renpy.config.gamedir, "save_file-LT1.save")
            if os.path.isfile(i):
                load_bug_report("save_file", delete_after = False)

    call please_wait_for_splashscreen from _call_please_wait_for_splashscreen

    $ persistent.from_pc_gallery        = None
    $ persistent.from_main_menu_gallery = None

    if mp.set_first_language_fix is None:
        $ mp.language = 'ENG'
        $ mp.set_first_language_fix = True
        $ mp.save()
        $ renpy.change_language('eng')


    # show expression 'images/logo.png':
    #     xalign .5
    #     yalign .5
    # with Dissolve(1.5)
  #  $ renpy.pause(.5, hard = True)
   # $ renpy.pause(999999999999)

   # hide expression 'images/logo.png'
 #   with Dissolve(.5)
    $ renpy.pause(.5, hard = True)

    call screen ScreenSplashScreen with Dissolve(.5)

    # show image 'images/new_patch.png'
    # with Dissolve(1.0)
    # $ renpy.pause(.5, hard = True)
    # $ renpy.pause(999999999999)

    # hide expression 'images/new_patch.png'
    # with Dissolve(.5)




    $ renpy.pause(.1, hard = True)
    if mp.interface_scale_number != 1.0 or mp.dialogue_interface_scale_number != 1.0:
        if renpy.call_screen('ScreenSplashScreenScale'):
            $ mp.interface_scale = 10
            $ mp.interface_scale_number = 1.0
            $ mp.dialogue_interface_scale = 10
            $ mp.dialogue_interface_scale_number = 1.0
            $ mp.save()
    $ set_new_patch('del')
    hide screen predict_load_screen
    hide screen please_wait_screen
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

#label main_menu:
#    pass
#    return