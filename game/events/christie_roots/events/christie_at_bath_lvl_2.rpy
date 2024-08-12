label christie_at_bath_lvl_2_christie_he_he:
    call comic_frame_v2_label((
        
        #_generate_text("Уффф...", size = 60), 
        #__("Что же это получается..."),
        __(" Хи-хи-хи! "),
        #__("я подольше ласкала тебя.")
        

        ), 
        size =  70,
        plus_y = 35,
        #line_spasing = -2, 
        say_image = Transform("comic_frame_say_2", xzoom = -1),
        say_pos = ["d", 20],
     show_label = "christie_at_bath_lvl_2_christie_talk_2_shake",        
    ) from _call_comic_frame_v2_label_311
    return
label christie_at_bath_lvl_2_gg_talk:

    show image comic_frame_v2_master:
        zoom .7
        xpos 480
        ypos 650
        xanchor 1.0
        yanchor 1.0
        alpha .0
        parallel:
            easein 0.2 ypos 625
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return


label christie_at_bath_lvl_2_gg_talk_2:

    show image comic_frame_v2_master:
        zoom .7
        xpos 680
        ypos 250
        xanchor 1.0
        yanchor 1.0
        alpha .0
        parallel:
            easein 0.2 ypos 225
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return

label christie_at_bath_lvl_2_christie_talk:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1850
        ypos 350
        xanchor 1.0
        yanchor 1.0
        alpha .0
        parallel:
            easein 0.2 ypos 325
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return


label christie_at_bath_lvl_2_christie_talk_2:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1400
        ypos 300
        xanchor 0.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.2 ypos 275
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return



label christie_at_bath_lvl_2_christie_talk_2_shake:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1400
        ypos 300
        xanchor 0.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.1 ypos 275
            easein 0.1 ypos 280
            easein 0.1 ypos 275
            easein 0.1 ypos 280
            easein 0.1 ypos 275

        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return

image christie_at_bath_lvl_2_bg = "cg/ep95/christie_bath/bg.png"


image christie_at_bath_lvl_2_christie 1 = "cg/ep95/christie_bath/christie/1.png"
image christie_at_bath_lvl_2_christie 2 = "cg/ep95/christie_bath/christie/2.png"
image christie_at_bath_lvl_2_christie 3 = "cg/ep95/christie_bath/christie/3.png"


image christie_at_bath_lvl_2_gg 1 = "cg/ep95/christie_bath/gg/1.png"
image christie_at_bath_lvl_2_gg 2 = "cg/ep95/christie_bath/gg/2.png"
image christie_at_bath_lvl_2_gg 3 = "cg/ep95/christie_bath/gg/3.png"
image christie_at_bath_lvl_2_gg 4 = "cg/ep95/christie_bath/gg/4.png"
image christie_at_bath_lvl_2_gg 5 = "cg/ep95/christie_bath/gg/5.png"
image christie_at_bath_lvl_2_gg 6 = "cg/ep95/christie_bath/gg/6.png"
image christie_at_bath_lvl_2_gg 7 = "cg/ep95/christie_bath/gg/7.png"
image christie_at_bath_lvl_2_gg 8 = "cg/ep95/christie_bath/gg/8.png"
image christie_at_bath_lvl_2_gg 9 = "cg/ep95/christie_bath/gg/9.png"

image christie_at_bath_lvl_2_sperm_3 = "cg/ep95/christie_bath/sperm/1/6.png"

image christie_at_bath_lvl_2_sperm_4 = "cg/ep95/christie_bath/sperm/1/6.png"

image christie_at_bath_lvl_2_sperm_5 = "cg/ep95/christie_bath/sperm/1/6.png"

image christie_at_bath_lvl_2_sperm_6 = "cg/ep95/christie_bath/sperm/2/7.png"

image christie_at_bath_lvl_2_sperm_7 = "cg/ep95/christie_bath/sperm/2/7.png"

image christie_at_bath_lvl_2_sperm_8 = "cg/ep95/christie_bath/sperm/2/7.png"



image christie_at_bath_lvl_2_sperm_9:
    2.4
    "cg/ep95/christie_bath/sperm/2/1.png"
    .1
    "cg/ep95/christie_bath/sperm/2/2.png"
    .1
    "cg/ep95/christie_bath/sperm/2/3.png"
    .1
    "cg/ep95/christie_bath/sperm/2/4.png"
    .1
    "cg/ep95/christie_bath/sperm/2/5.png"
    .1
    "cg/ep95/christie_bath/sperm/2/6.png"
    .1
    "cg/ep95/christie_bath/sperm/2/7.png"

image christie_at_bath_lvl_2_sperm_10:
    3.7
    "cg/ep95/christie_bath/sperm/2/1.png"
    .1
    "cg/ep95/christie_bath/sperm/2/2.png"
    .1
    "cg/ep95/christie_bath/sperm/2/3.png"
    .1
    "cg/ep95/christie_bath/sperm/2/4.png"
    .1
    "cg/ep95/christie_bath/sperm/2/5.png"
    .1
    "cg/ep95/christie_bath/sperm/2/6.png"
    .1
    "cg/ep95/christie_bath/sperm/2/7.png"

image christie_at_bath_lvl_2_sperm_0:
    "cg/ep95/christie_bath/sperm/1/1.png"
    .1
    "cg/ep95/christie_bath/sperm/1/2.png"
    .1
    "cg/ep95/christie_bath/sperm/1/3.png"
    .1
    "cg/ep95/christie_bath/sperm/1/4.png"
    .1
    "cg/ep95/christie_bath/sperm/1/5.png"
    .1
    "cg/ep95/christie_bath/sperm/1/6.png"
image christie_at_bath_lvl_2_sperm_1:
    "cg/ep95/christie_bath/sperm/1/1.png"
    .1
    "cg/ep95/christie_bath/sperm/1/2.png"
    .1
    "cg/ep95/christie_bath/sperm/1/3.png"
    .1
    "cg/ep95/christie_bath/sperm/1/4.png"
    .1
    "cg/ep95/christie_bath/sperm/1/5.png"
    .1
    "#0000"
    1.0
    "cg/ep95/christie_bath/sperm/1/1.png"
    .1
    "cg/ep95/christie_bath/sperm/1/2.png"
    .1
    "cg/ep95/christie_bath/sperm/1/3.png"
    .1
    "cg/ep95/christie_bath/sperm/1/4.png"
    .1
    "cg/ep95/christie_bath/sperm/1/5.png"
    .1
    "#0000"
    1.0
    "cg/ep95/christie_bath/sperm/1/1.png"
    .1
    "cg/ep95/christie_bath/sperm/1/2.png"
    .1
    "cg/ep95/christie_bath/sperm/1/3.png"
    .1
    "cg/ep95/christie_bath/sperm/1/4.png"
    .1
    "cg/ep95/christie_bath/sperm/1/5.png"
    .1
    "cg/ep95/christie_bath/sperm/1/6.png"
    .1
image christie_at_bath_lvl_2_sperm_2:
    .6
    "cg/ep95/christie_bath/sperm/2/1.png"
    .1
    "cg/ep95/christie_bath/sperm/2/2.png"
    .1
    "cg/ep95/christie_bath/sperm/2/3.png"
    .1
    "cg/ep95/christie_bath/sperm/2/4.png"
    .1
    "cg/ep95/christie_bath/sperm/2/5.png"
    .1
    "cg/ep95/christie_bath/sperm/2/6.png"
    .1
    "cg/ep95/christie_bath/sperm/2/7.png"
    

image christie_at_bath_lvl_2_both 1:
    "cg/ep95/christie_bath/both/1.png"
    .17
    "cg/ep95/christie_bath/both/2.png"
    .17
    "cg/ep95/christie_bath/both/3.png"
    .17
    "cg/ep95/christie_bath/both/4.png"
    .17
    "cg/ep95/christie_bath/both/5.png"
    .17
    "cg/ep95/christie_bath/both/6.png"
    .17
    "cg/ep95/christie_bath/both/7.png"
    .17
    "cg/ep95/christie_bath/both/8.png"
    .17
    "cg/ep95/christie_bath/both/7.png"
    .17
    "cg/ep95/christie_bath/both/6.png"
    .17
    "cg/ep95/christie_bath/both/5.png"
    .17
    "cg/ep95/christie_bath/both/4.png"
    .17
    "cg/ep95/christie_bath/both/3.png"
    .17
    "cg/ep95/christie_bath/both/2.png"
    .17
    repeat

image christie_at_bath_lvl_2_both 2:
    "cg/ep95/christie_bath/both/1.png"
    .12
    "cg/ep95/christie_bath/both/2.png"
    .12
    "cg/ep95/christie_bath/both/3.png"
    .12
    "cg/ep95/christie_bath/both/4.png"
    .12
    "cg/ep95/christie_bath/both/5.png"
    .12
    "cg/ep95/christie_bath/both/6.png"
    .12
    "cg/ep95/christie_bath/both/7.png"
    .12
    "cg/ep95/christie_bath/both/8.png"
    .12
    "cg/ep95/christie_bath/both/7.png"
    .12
    "cg/ep95/christie_bath/both/6.png"
    .12
    "cg/ep95/christie_bath/both/5.png"
    .12
    "cg/ep95/christie_bath/both/4.png"
    .12
    "cg/ep95/christie_bath/both/3.png"
    .12
    "cg/ep95/christie_bath/both/2.png"
    .12

    repeat

image christie_at_bath_lvl_2_both 3:
    "cg/ep95/christie_bath/both/1.png"
    .08
    "cg/ep95/christie_bath/both/2.png"
    .08
    "cg/ep95/christie_bath/both/3.png"
    .08
    "cg/ep95/christie_bath/both/4.png"
    .08
    "cg/ep95/christie_bath/both/5.png"
    .08
    "cg/ep95/christie_bath/both/6.png"
    .08
    "cg/ep95/christie_bath/both/7.png"
    .08
    "cg/ep95/christie_bath/both/8.png"
    .08
    "cg/ep95/christie_bath/both/7.png"
    .08
    "cg/ep95/christie_bath/both/6.png"
    .08
    "cg/ep95/christie_bath/both/5.png"
    .08
    "cg/ep95/christie_bath/both/4.png"
    .08
    "cg/ep95/christie_bath/both/3.png"
    .08
    "cg/ep95/christie_bath/both/2.png"
    .08
    repeat

image christie_at_bath_lvl_2_both 4:
    "cg/ep95/christie_bath/both/1.png"
    .05
    "cg/ep95/christie_bath/both/2.png"
    .05
    "cg/ep95/christie_bath/both/3.png"
    .05
    "cg/ep95/christie_bath/both/4.png"
    .05
    "cg/ep95/christie_bath/both/5.png"
    .05
    "cg/ep95/christie_bath/both/6.png"
    .05
    "cg/ep95/christie_bath/both/7.png"
    .05
    "cg/ep95/christie_bath/both/8.png"
    .05
    "cg/ep95/christie_bath/both/7.png"
    .05
    "cg/ep95/christie_bath/both/6.png"
    .05
    "cg/ep95/christie_bath/both/5.png"
    .05
    "cg/ep95/christie_bath/both/4.png"
    .05
    "cg/ep95/christie_bath/both/3.png"
    .05
    "cg/ep95/christie_bath/both/2.png"
    .05
    repeat    

image christie_at_bath_lvl_2_both end = "cg/ep95/christie_bath/both/9.png"

    


image christie_at_bath_lvl_2_circle_btn = Composite((1920, 1080),
    (150, 250), Composite((200, 200), (0, 0), Solid("#fff1"))
    )

# image christie_at_bath_lvl_2_christie = Composite((1920, 1080),
#     (0, 0), 'images/locations/bg/Restroom/morning.png',
#     (0, 0), "cg/milf_and_sister_activities/sister_restroom.png",
    
#     )
label christie_at_bath_lvl_2:
    #В ванной

    #2й уровень 


    #//При нажатии на спрайт с купающейся Кристи

    #//Kristy_Vana //спрайт где она из ванны обращается к ГГ
    scene image '#0000'
    show image 'images/locations/bg/Restroom/morning.png'
    show image "cg/ep95/christie_bath/sister_restroom_2.png"
    show image "cg/ep95/christie_bath/sister_restroom_2.png":
        alpha .0
    show image "cg/milf_and_sister_activities/sister_restroom.png"
    show image 'cg/ep95/christie_bath/bath.png'

    show Christie Invis
    show Christie Invis:
        xpos 550
    show GG Embarrassment
    show GG Embarrassment at go_from_left(xxalign = .05)

    $ renpy.pause(.8, hard = True)
    show image "cg/milf_and_sister_activities/sister_restroom.png":
        alpha .0
    
    show image "cg/ep95/christie_bath/sister_restroom_2.png":
        ypos 1080 alpha 1.0
        easein 0.1 ypos 1085
        easein 0.1 ypos 1080
        easein 0.1 ypos 1085
        easein 0.1 ypos 1080
        easein 0.1 ypos 1085
        easein 0.1 ypos 1080
        
        
        #easein 0.1 ypos -5
        #easein 0.1 ypos 5
        #easein 0.1 ypos -5
        #easein 0.1 ypos 5
        #easein 0.1 ypos 0
    "Кристи" "[gg]?!"
    show GG: 
        xalign .05
    with my_dissolve
    "[gg]" "Да, это я."
    show image "cg/ep95/christie_bath/sister_restroom_2.png":
        ypos 1080
        easein 1.0 ypos 1100
    "Кристи" "Ты разве не видишь, что я принимаю ванну?! Выходи быстрее! "
    "[gg]" "Знаю, поэтому и зашёл поглазеть на тебя."
    hide image "cg/ep95/christie_bath/sister_restroom_2.png"
    show image "cg/milf_and_sister_activities/sister_restroom.png":
        ypos 1100 alpha 1.0
        easein .1 ypos 1103
        easein .1 ypos 1100
        easein .1 ypos 1103
        easein .1 ypos 1100
    "Кристи" "Ха-ха-ха! "
    show image "cg/milf_and_sister_activities/sister_restroom.png":
        ypos 1100
        easein .8 ypos 1080
    "Кристи" "Ну раз так, тогда подай мне полотенце. "
    "[gg]" "С удовольствием."
    show GG:
        ease .45 xalign .25
        xzoom -1
        ease .4 alpha .0
    show image "mini_games/circle_mini_game_red.png":
        anchor (.5, .5)
        xpos 250 ypos 350 zoom .5 alpha .0
        easein .5 alpha .7
    show screen icons_interface(with_transform=True)
    $ renpy.pause(.9)
    #//Kristy_Vana_Minet_1
    hide screen icons_interface
    show GG:
        xalign .25
        xzoom -1
        alpha .0
    show image "mini_games/circle_mini_game_red.png":
        anchor (.5, .5)
        xpos 250 ypos 350 alpha .7
        block:
            zoom .5
            pause .2
            easeout .25 zoom .6
            easein .25 zoom .45
            easeout .25 zoom .6
            easein .25 zoom .5
            pause 1.0
            repeat
   

    call screen rtrn_screen("christie_at_bath_lvl_2_circle_btn", "christie_at_bath_lvl_2_circle_btn")
    
    hide image "mini_games/circle_mini_game_red.png"
    with my_dissolve
    call screen rtrn_screen("cg/milf_and_sister_activities/sister_restroom.png")

    #//GG_Dick выезжает слева
    menu:
        "Отдать полотенце":
            pass
    scene black with Dissolve(.3)
    $ renpy.pause(.5, hard = True)
    scene christie_at_bath_lvl_2_bg 
    show christie_at_bath_lvl_2_christie 1
    with my_dissolve
    show christie_at_bath_lvl_2_gg 1:
        xpos -1500
        #pause .2
        easein 1.0 xpos 0
    $ renpy.pause(1.0, hard = True)
    show christie_at_bath_lvl_2_gg 2:
        xpos 0
    with Dissolve(.25)

    $ renpy.pause(.3)


    show christie_at_bath_lvl_2_gg 3:
        xpos 0
    #with Dissolve(.005)
    $ renpy.pause(.005)
    show christie_at_bath_lvl_2_gg 4:
        xpos 0
    #with Dissolve(.005)
    $ renpy.pause(.005)
    show christie_at_bath_lvl_2_gg 5:
        xpos 0
    #with Dissolve(.005)
    $ renpy.pause(.005)
    show christie_at_bath_lvl_2_gg 6:
        xpos 0
   # with Dissolve(.005)
    $ renpy.pause(.005)
    show christie_at_bath_lvl_2_gg 7:
        xpos 0
  #  with Dissolve(.005)
    $ renpy.pause(.005)
    show christie_at_bath_lvl_2_gg 8:
        xpos 0
  #  with Dissolve(.005)
    $ renpy.pause(.005)
    show image comic_frame_v2_master
    show image comic_frame_v2_slave

    show christie_at_bath_lvl_2_christie 2

    with my_dissolve
    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Я просила полотенце,"),
            __("а не вот это вот…")

            ), 
            size =  50,
            #plus_y = 50,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk",        
        ) from _call_comic_frame_v2_label_312
    else:
        "Кристи" "Я просила полотенце, а не вот это вот…"


    show christie_at_bath_lvl_2_gg:
        easein .5 xpos -20 ypos 20
    
    show shadow_full:
        
        alpha .0
        easein 1.0 alpha .7
    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Это случилось"),
            __("непреднамеренно.")

            ), 
            size =  50,
            #plus_y = 50,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk",        
        ) from _call_comic_frame_v2_label_313

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Из-за меня?"),

            ), 
            size =  60,
            plus_y = 50,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_314
    else:

        "[gg]" "Это случилось непреднамеренно. "

        "Кристи" "Из-за меня?"

    show shadow_full:
        
        easein .5 alpha .9
    show christie_at_bath_lvl_2_gg:
        easein .5 xpos -30 ypos 30
    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("  Угу...  "),

            ), 
            size   = 60,
            plus_y = 50,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk",        
        ) from _call_comic_frame_v2_label_315


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Что же это"),
            __("получается...")
            # __("малейший взгляд в мою сторону,"),
            # __("и у тебя деревянный стояк?"),

            ), 
            size =  50,
            plus_y = 10,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_316
    else:

        "[gg]" "Угу."

        "Кристи" "Что же это получается, малейший взгляд в мою сторону, и у тебя деревянный стояк? "

    show christie_at_bath_lvl_2_christie 3
    with my_dissolve

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("...малейший взгляд"),
            __("в мою сторону,"),
            __("и у тебя"),
            __("деревянный стояк?")

            ), 
            size =  40,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_317
    show shadow_full:
        
        easein .1 alpha .0
    show christie_at_bath_lvl_2_gg:
        easein .4 xpos 0 ypos 0

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Тебе не стоило"),
            __("рождаться такой"),
            __("красивой!")

            ), 
            size   = 45,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk",        
        ) from _call_comic_frame_v2_label_318

        call christie_at_bath_lvl_2_christie_he_he from _call_christie_at_bath_lvl_2_christie_he_he
    else:

        "[gg]" "Тебе не стоило рождаться такой красивой. "

        "Кристи" "Хи-хи-хи!"

    show christie_at_bath_lvl_2_christie 1
    with my_dissolve

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("И долго он"),
            __("так будет стоять?")

            ), 
            size =  40,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_319

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Пока я не кончу."),


            ), 
            size   = 45,
            plus_y = 60,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk",        
        ) from _call_comic_frame_v2_label_320

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Обязательно надо"),
            __("кончить?")

            ), 
            size =  45,
            plus_y = 25,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_321
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("По-другому"),
            __("никак.")


            ), 
            size   = 55,
            plus_y = -10,
            #line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk",        
        ) from _call_comic_frame_v2_label_322
    else:

        "Кристи" "И долго он так будет стоять?"

        "[gg]" "Пока я не кончу."

        "Кристи" "Обязательно надо кончить?"

        "[gg]" "По другому никак."

    show christie_at_bath_lvl_2_christie 2
    with my_dissolve

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Хех…"),

            ), 
            size =  70,
            plus_y = 40,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_323
    else:

        "Кристи" "Хех…"

    show christie_at_bath_lvl_2_christie 3
    with my_dissolve

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Хорошо, я помогу,"),
            __("только не вздумай "),
            __("шуметь.")

            ), 
            size =  40,
            plus_y = 15,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_324

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Молчу."),


            ), 
            size   = 45,
            plus_y = 55,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk",        
        ) from _call_comic_frame_v2_label_325
    else:

        "Кристи" "Хорошо, я помогу, только не вздумай шуметь. "

        "[gg]" "Молчу."


    show christie_at_bath_lvl_2_christie 1
    with my_dissolve
    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("И это останется"),
            __("только между нами."),
            

            ), 
            size =  40,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_326


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Само"),
            __("собой.")


            ), 
            size   = 70,
            plus_y = 0,
            #line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk",        
        ) from _call_comic_frame_v2_label_327
    else:

        "Кристи" "И это останется только между нами."

        "[gg]" "Само собой. "

    #//Kristy_Vana_Minet_2 Animation

    #//Скорость х1
    scene image "#000" with Dissolve(.3)
    $ renpy.pause(.5, hard = True)
    scene christie_at_bath_lvl_2_bg 
    show christie_at_bath_lvl_2_both 1
    show image comic_frame_v2_master
    show image comic_frame_v2_slave
    with my_dissolve
    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Ну как?.."),
            

            ), 
            size =  70,
            plus_y = 30,
            #line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_328

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Безрезультатно."),


            ), 
            size   = 45,
            plus_y = 55,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk_2",        
        ) from _call_comic_frame_v2_label_329


        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("А может, ты просто"),
            __("сдерживаешь себя,"),
            __("лишь бы я подольше"),
            __("ласкала тебя.")
            

            ), 
            size =  40,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_330


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Думаешь, в таком"),
            __("напряженном состоянии"),
            __("это возможно сделать?")


            ), 
            size   = 45,
            plus_y = 12,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk_2",        
        ) from _call_comic_frame_v2_label_331




        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Остаётся только"),
            __("верить на слово."),
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  40,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_332

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("У нас, девушек,"),
            __("всё обстоит иначе."),
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  40,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_333


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Тем вы и хороши для"),
            __("нас, мужчин."),



            ), 
            size   = 50,
            plus_y = 10,
            #line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk_2",        
        ) from _call_comic_frame_v2_label_334



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("А конкретно для"),
            __("меня - ты.")
            

            ), 
            size   = 55,
            plus_y = 2,
            #line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk_2",        
        ) from _call_comic_frame_v2_label_335



         
        call christie_at_bath_lvl_2_christie_he_he from _call_christie_at_bath_lvl_2_christie_he_he_1
        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Пожалуй, мне"),
            __("стоит ускориться."),
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  45,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_336


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Согласен."),
            
            
            ), 
            size   = 70,
            plus_y = 40,
            #line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk_2",        
        ) from _call_comic_frame_v2_label_337



        show image comic_frame_v2_master:    
            easein .2 ypos 500 alpha 0.0
        $ renpy.pause(.1, hard = True)
    else:

        "Кристи" "Ну как?.."

        "[gg]" "Безрезультатно."

        "Кристи" "А может ты просто сдерживаясь себя, лишь бы я подольше ласкала тебя."

        "[gg]" "Думаешь, в таком напряженном состоянии это возможно сделать? "

        "Кристи" "Остаётся только верить на слово."

        "Кристи" "У нас, девушек, всё обстоит иначе."

        "[gg]" "Тем вы и хороши для нас, мужчин."

        "[gg]" "А конкретно для меня – ты."

        "Кристи" "Хи-хи-хи!"

        "Кристи" "Пожалуйста, мне стоит ускориться. "

        "[gg]" "Согласен."
    menu christie_at_bath_lvl_2_speed_up_1:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_at_bath_lvl_2_speed_up_1
    #//Скорость х2
    #scene christie_at_bath_lvl_2_bg 
    #show image comic_frame_v2_master
    #show image comic_frame_v2_slave
    show christie_at_bath_lvl_2_both 2
    
    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Такое ощущение, что"),
            __("он только больше стал."),
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  42,
            plus_y = 20,
          #  line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_338


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Мне сложно"),
            __("оценить объективно.")
            
            
            ), 
            size   = 57,
            plus_y = 14,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk_2",        
        ) from _call_comic_frame_v2_label_339


        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Если он стал больше,"),
            __("то значит это ещё"),
            __("не предел…")
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  45,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_340

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("А если это"),
            __("не предел, то"),
            __("работы предстоит"),
            __("много…")
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  45,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_341


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Что ты хочешь"),
            __("этим сказать?")
            
            
            ), 
            size   = 55,
            plus_y = 10,
            line_spasing = -10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk_2",        
        ) from _call_comic_frame_v2_label_342





        call christie_at_bath_lvl_2_christie_he_he from _call_christie_at_bath_lvl_2_christie_he_he_2
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Ничего."),
            __("Просто это"),
            __("забавно.")
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  60,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_343


        
        show image comic_frame_v2_master:    
            easein .2 ypos 300 alpha 0.0
        $ renpy.pause(.1, hard = True)
    else:


        "Кристи" "Такое ощущение, что он только больше стал."

        "[gg]" "Мне сложно оценить объективно."

        "Кристи" "Если он стал больше, то значит это ещё не предел…"

        "Кристи" "А если это не предел, то работы предстоит много…"

        "[gg]" "Что ты хочешь этим сказать?"

        "Кристи" "Хи-хи-хи! Ничего."

        "Кристи" "Просто это забавно."

    menu christie_at_bath_lvl_2_speed_up_2:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_at_bath_lvl_2_speed_up_2
    #//Скорость х3
    #scene christie_at_bath_lvl_2_bg 
    #show image comic_frame_v2_master
    #show image comic_frame_v2_slave
    #show image comic_frame_v2_master

    #show image comic_frame_v2_slave
    show christie_at_bath_lvl_2_both 3
    with my_dissolve

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Обалдеть!"),
            
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  75,
            plus_y = 30,
            #line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_344


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Я прям рукой"),
            __("чувствую, как"),
            __("он расширяется…")
            
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  50,
            plus_y = 15,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_345



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("А я чувствую, что"),
            __("вот-вот {size=70}кончу{/size}…")
            
            
            ), 
            size   = 52,
            plus_y = 1,
            line_spasing = -10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk_2",        
        ) from _call_comic_frame_v2_label_346


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("И куда это"),
            __("всё полетит?")
            
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  50,
            #plus_y = 20,
            #line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_347




        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("А куда бы ты хотела?"),
            
            
            ), 
            size   = 45,
            plus_y = 55,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk_2",        
        ) from _call_comic_frame_v2_label_348



        call christie_at_bath_lvl_2_christie_he_he from _call_christie_at_bath_lvl_2_christie_he_he_3
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Давай мне на"),
            __("груди!")
            
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  60,
            plus_y = 10,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_349


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Этой фразой ты"),
            __("буквально приблизила"),
            __("мою эякуляцию.")
            
            ), 
            size   = 55,
            plus_y = 10,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk_2",        
        ) from _call_comic_frame_v2_label_350



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Какой ты"),
            __("восприимчивый,"),
            __("хи-хи-хи!")
            
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  55,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_351

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Готов уже, да?"),
            __("{i}Почти-почти?{/i}")
            
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  55,
            plus_y = 1,
            #line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_352


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Ага. Что-то типа того…"),
            __("Ещё совсем чуточку."),
            
            ), 
            size   = 50,
            plus_y = 10,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk_2",        
        ) from _call_comic_frame_v2_label_353



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Твой член уже"),
            __("выскакивает из руки."),
            
            
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  47,
            plus_y = 10,
            #line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_354

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __( "Постарайся, ну же…"),
            __("{size=70}Я уже на грани!{/size}"),
            
            ), 
            size   = 45,
            plus_y = 2,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk_2",        
        ) from _call_comic_frame_v2_label_355



        #//Кончить
        show image comic_frame_v2_master:    
            easein .2 ypos 300 alpha 0.0
        $ renpy.pause(.1, hard = True)
    else:


        "Кристи" "Обалдеть!"

        "Кристи" "Я прям рукой чувствую, как он расширяется…"

        "[gg]" "А я чувствую, что вот-вот кончу…"

        "Кристи" "И куда это всё полетит?"

        "[gg]" "А куда бы ты хотела?"

        "Кристи" "Хи-хи-хи!"

        "Кристи" "Давай мне на груди!"

        "[gg]" "Этой фразы ты буквально приблизила мою эякуляцию. "

        "Кристи" "Какой ты восприимчивый, хи-хи-хи!"

        "Кристи" "Готов уже, да? Почти-почти?"

        "[gg]" "Ага. Что-то типа того…"

        "[gg]" "Ещё совсем чуточку."

        "Кристи" "Твой член уже выскакивает из руки."

        "[gg]" "Постарайся, ну же… Я уже на грани!"
    menu christie_at_bath_lvl_2_speed_up_3:
        "Кончить":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_at_bath_lvl_2_speed_up_3

    #//Скорость х4
    #scene christie_at_bath_lvl_2_bg 
    #show image comic_frame_v2_master
    #show image comic_frame_v2_slave
    show christie_at_bath_lvl_2_both 4

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Вот так!"),
            __("{size=65}Вот так!{/size}"),
            __("{size=70}{i}Вот так!{/i}{/size}")
            
            
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  50,
            plus_y = 10,
            #line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_356

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Давай,"),
            __("обкончай мои"),
            __("сиськи!")

            
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  60,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_357
        

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Вымажи меня в своей"),
            __("{size=70}{i}горячей{/i}{/size} сперме!")
            
            
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  40,
            plus_y = 5,
            #line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_358


        $ christie_at_bath_lvl_2_cum_1 = Composite((1050, 180), (0, 0), Solid("#000"))

        #////Kristy_Vana_Minet_3 Animation
        $ christie_at_bath_lvl_2_cum_2 = Composite((980, 180), 
            #(0, 0), Solid("#000"),
            (0, 0), Frame(Transform('interface/comic_v2/bg_frame_2.png', alpha = .8), Borders(64, 64, 64, 64)),
            (20, 50), Text(
                            __("Каааааааааааайааааайф!"), 
                            kerning  = 5,
                            size     = 70,
                            outlines = [(2, "#000a", 0, 0),],
                            font = "fonts/mango_comics_er.ttf",
                            
                            ),
            (1020, 60), Transform("comic_frame_say_3")
            )

        show image comic_frame_v2_master:    
            easein .2 ypos 500 alpha 0.0
        show image AlphaMask(christie_at_bath_lvl_2_cum_2, At(christie_at_bath_lvl_2_cum_1, christie_root_52_cum_transform)): #comic_frame_v2_0:
            
            zoom .7
            ypos  70
            xpos  100
            yanchor .5
            alpha 1.0

        #hide image comic_frame_v2_slave
        #show image christie_root_52_cum_2
        #show
        $ renpy.pause(.95)
        show christie_at_bath_lvl_2_both end
        with my_dissolve
        $ renpy.pause(.5)
        
        
        show image '#fff'
        with Dissolve(.3)
        $ renpy.pause(.7, hard = True)
        scene christie_at_bath_lvl_2_bg 
        show christie_at_bath_lvl_2_both end
        with Dissolve(.1)
        $ renpy.pause(.15, hard = True)

        show christie_at_bath_lvl_2_sperm_1

        show christie_at_bath_lvl_2_sperm_2
        show christie_at_bath_lvl_2_sperm_9:
            pause 3.0
            linear .2 alpha .1
        # show christie_at_bath_lvl_2_sperm_10:
        #     pause 4.4
        #     linear .2 alpha .1
        $ renpy.pause(.5, hard = True)    

        show christie_at_bath_lvl_2_sperm_3:
            ypos 0 alpha 1.0
            linear .75 ypos 10 alpha .0

        $ renpy.pause(.7, hard = True)

        show christie_at_bath_lvl_2_sperm_6:
            ypos 0 alpha 1.0
            linear .75 ypos 10 alpha .3
        $ renpy.pause(1.5, hard = True)

        show christie_at_bath_lvl_2_sperm_4:
            ypos 0 alpha 1.0
            linear .75 ypos 10 alpha .0
        $ renpy.pause(.5)


        show christie_at_bath_lvl_2_sperm_7:
            ypos 0 alpha 1.0# rotate 0
            #pause 1.0
            linear 2.0 ypos 6 xpos -10 alpha .2
            #linear .75 rotate 10
        $ renpy.pause(.15, hard = True)

        show christie_at_bath_lvl_2_sperm_5:
            ypos 0 alpha 1.0
            linear .5 alpha .5
        $ renpy.pause(.1, hard = True)    

        show image comic_frame_v2_master
        show image comic_frame_v2_slave
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Вау! Как много…"),
            __("И такая приятная"),
            __("на ощупь.")
            
            
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  50,
            #plus_y = 5,
            #line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_359


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Спасибо."),
            
            ), 
            size   = 70,
            plus_y = 30,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_2_gg_talk_2",        
        ) from _call_comic_frame_v2_label_360

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #__("Что же это получается..."),
            __("Обращайся!"),

            
            #__("я подольше ласкала тебя.")
            

            ), 
            size =  70,
            plus_y = 30,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_2_christie_talk_2",        
        ) from _call_comic_frame_v2_label_361

        call christie_at_bath_lvl_2_christie_he_he from _call_christie_at_bath_lvl_2_christie_he_he_4
    else:


        "Кристи" "Вот так! Вот так! Вот так!"

        "Кристи" "Давай, обкончай мои сиськи! "

        "Кристи" "Вымажи меня в своей горячей сперме!"

        "[gg]" "Кааааааайф!"
        show christie_at_bath_lvl_2_both end
        with my_dissolve
        $ renpy.pause(.5)
        
        
        show image '#fff'
        with Dissolve(.3)
        $ renpy.pause(.7, hard = True)
        scene christie_at_bath_lvl_2_bg 
        show christie_at_bath_lvl_2_both end
        with Dissolve(.1)
        $ renpy.pause(.15, hard = True)

        show christie_at_bath_lvl_2_sperm_1

        show christie_at_bath_lvl_2_sperm_2
        show christie_at_bath_lvl_2_sperm_9:
            pause 3.0
            linear .2 alpha .1
        # show christie_at_bath_lvl_2_sperm_10:
        #     pause 4.4
        #     linear .2 alpha .1
        $ renpy.pause(.5, hard = True)    

        show christie_at_bath_lvl_2_sperm_3:
            ypos 0 alpha 1.0
            linear .75 ypos 10 alpha .0

        $ renpy.pause(.7, hard = True)

        show christie_at_bath_lvl_2_sperm_6:
            ypos 0 alpha 1.0
            linear .75 ypos 10 alpha .3
        $ renpy.pause(1.5, hard = True)

        show christie_at_bath_lvl_2_sperm_4:
            ypos 0 alpha 1.0
            linear .75 ypos 10 alpha .0
        $ renpy.pause(.5)


        show christie_at_bath_lvl_2_sperm_7:
            ypos 0 alpha 1.0# rotate 0
            #pause 1.0
            linear 2.0 ypos 6 xpos -10 alpha .2
            #linear .75 rotate 10
        $ renpy.pause(.15, hard = True)

        show christie_at_bath_lvl_2_sperm_5:
            ypos 0 alpha 1.0
            linear .5 alpha .5
        $ renpy.pause(.1, hard = True)    

        "Кристи" "Вау! Как много… И такое приятное на ощупь."

        "[gg]" "Спасибо."

        "Кристи" "Обращайся, хи-хи-хи!"


    scene black with Dissolve(.5)
    $ renpy.pause(1, hard = True)
    python:
        try:
            del christie_at_bath_lvl_2_cum_2
        except:
            pass
        try:
            del christie_at_bath_lvl_2_cum_1
        except:
            pass

    if not from_gallery_check():

        $ add_to_gallery(41)
        $ location_now = "Corridor"
            

        
        $ time.time_forward(jump_to_main_interface = False)

    jump main_interface_label
