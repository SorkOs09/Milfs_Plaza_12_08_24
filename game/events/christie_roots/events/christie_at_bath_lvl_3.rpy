label christie_at_bath_lvl_3_christie_talk_1:

    show image comic_frame_v2_master:
        zoom 1.0
        xpos 1260
        ypos 10
        xanchor 0.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.2 ypos 90
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return



label christie_at_bath_lvl_3_christie_talk_2:

    show image comic_frame_v2_master:
        zoom .88
        xpos 1380
        ypos 10
        xanchor 0.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.2 ypos 100
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return




label christie_at_bath_lvl_3_christie_talk_2_shake:

    show image comic_frame_v2_master:
        zoom .88
        xpos 1380
        ypos 10
        xanchor 0.0
        yanchor 0.0
        alpha .0

        parallel:
            easein 0.1 ypos 100
            easein 0.1 ypos 95
            easein 0.1 ypos 100
            easein 0.1 ypos 95
            easein 0.1 ypos 100

        parallel:
            ease .1 alpha 1.0


    $ renpy.pause(.2, hard = True)
    return


label christie_at_bath_lvl_3_gg_talk_1:

    show image comic_frame_v2_master:
        zoom 1.0
        xpos 670
        ypos 10
        xanchor 1.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.2 ypos 50
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return




label christie_at_bath_lvl_3_gg_talk_2:

    show image comic_frame_v2_master:
        zoom .9
        xpos 1000
        ypos 0
        xanchor 1.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.2 ypos 10
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return



label christie_at_bath_lvl_3_gg_talk_3:

    show image comic_frame_v2_master:
        zoom .9
        xpos 750
        ypos 0
        xanchor 1.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.2 ypos 50
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return



image christie_at_bath_lvl_3_sperm_0:
    "cg/ep105/bath_event/sperm/1.png"
    .1
    "cg/ep105/bath_event/sperm/2.png"
    .1
    "cg/ep105/bath_event/sperm/3.png"
    .1
    "cg/ep105/bath_event/sperm/4.png"
    .1
    "cg/ep105/bath_event/sperm/5.png"
    .1
    "cg/ep105/bath_event/sperm/6.png"
    .1
    "cg/ep105/bath_event/sperm/7.png"

image christie_at_bath_lvl_3_sperm_1 = 'christie_at_bath_lvl_3_sperm_0'
image christie_at_bath_lvl_3_sperm_2 = 'christie_at_bath_lvl_3_sperm_0'
image christie_at_bath_lvl_3_sperm_3 = 'christie_at_bath_lvl_3_sperm_0'
image christie_at_bath_lvl_3_sperm_4 = 'christie_at_bath_lvl_3_sperm_0'
image christie_at_bath_lvl_3_sperm_5 = 'christie_at_bath_lvl_3_sperm_0'
image christie_at_bath_lvl_3_sperm_6 = 'christie_at_bath_lvl_3_sperm_0'
image christie_at_bath_lvl_3_sperm_7 = 'christie_at_bath_lvl_3_sperm_0'
image christie_at_bath_lvl_3_sperm_8 = 'christie_at_bath_lvl_3_sperm_0'
image christie_at_bath_lvl_3_sperm_9 = 'christie_at_bath_lvl_3_sperm_0'
image christie_at_bath_lvl_3_sperm_10 = 'christie_at_bath_lvl_3_sperm_0'
image christie_at_bath_lvl_3_sperm_11 = 'christie_at_bath_lvl_3_sperm_0'

image christie_at_bath_lvl_3_back   = 'cg/ep105/bath_event/back.png'
image christie_at_bath_lvl_3_shadow = 'cg/ep105/bath_event/shadow.png'

image christie_at_bath_lvl_3 0 = 'cg/ep105/bath_event/0.png'
image christie_at_bath_lvl_3 1 = 'cg/ep105/bath_event/1.png'
image christie_at_bath_lvl_3 cum = 'cg/ep105/bath_event/cum.png'

image christie_at_bath_lvl_3_bubbles_anim_1:
    'cg/ep105/bath_event/bubbles/1.png'
    .25
    'cg/ep105/bath_event/bubbles/2.png'
    .25
    'cg/ep105/bath_event/bubbles/3.png'
    .25
    'cg/ep105/bath_event/bubbles/4.png'
    .25
    'cg/ep105/bath_event/bubbles/5.png'
    .25
    'cg/ep105/bath_event/bubbles/6.png'
    .25
    '#0000'
    .5
    repeat
image christie_at_bath_lvl_3_bubbles_anim_2:
    'cg/ep105/bath_event/bubbles/1.png'
    .18
    'cg/ep105/bath_event/bubbles/2.png'
    .18
    'cg/ep105/bath_event/bubbles/3.png'
    .18
    'cg/ep105/bath_event/bubbles/4.png'
    .18
    'cg/ep105/bath_event/bubbles/5.png'
    .18
    'cg/ep105/bath_event/bubbles/6.png'
    .18
    '#0000'
    .36
    repeat
image christie_at_bath_lvl_3_bubbles_anim_3:
    'cg/ep105/bath_event/bubbles/1.png'
    .1
    'cg/ep105/bath_event/bubbles/2.png'
    .1
    'cg/ep105/bath_event/bubbles/3.png'
    .1
    'cg/ep105/bath_event/bubbles/4.png'
    .1
    'cg/ep105/bath_event/bubbles/5.png'
    .1
    'cg/ep105/bath_event/bubbles/6.png'
    .1
    '#0000'
    .2
    repeat



    
image christie_at_bath_lvl_3 anim_1:
    'cg/ep105/bath_event/1.png'
    .25
    'cg/ep105/bath_event/2.png'
    .25
    'cg/ep105/bath_event/3.png'
    .25
    'cg/ep105/bath_event/4.png'
    .25
    'cg/ep105/bath_event/5.png'
    .25
    'cg/ep105/bath_event/4.png'
    .25
    'cg/ep105/bath_event/3.png'
    .25
    'cg/ep105/bath_event/2.png'
    .25
    repeat

image christie_at_bath_lvl_3 anim_2:
    'cg/ep105/bath_event/1.png'
    .18
    'cg/ep105/bath_event/2.png'
    .18
    'cg/ep105/bath_event/3.png'
    .18
    'cg/ep105/bath_event/4.png'
    .18
    'cg/ep105/bath_event/5.png'
    .18
    'cg/ep105/bath_event/4.png'
    .18
    'cg/ep105/bath_event/3.png'
    .18
    'cg/ep105/bath_event/2.png'
    .18
    repeat

image christie_at_bath_lvl_3 anim_3:
    'cg/ep105/bath_event/1.png'
    .1
    'cg/ep105/bath_event/2.png'
    .1
    'cg/ep105/bath_event/3.png'
    .1
    'cg/ep105/bath_event/4.png'
    .1
    'cg/ep105/bath_event/5.png'
    .1
    'cg/ep105/bath_event/4.png'
    .1
    'cg/ep105/bath_event/3.png'
    .1
    'cg/ep105/bath_event/2.png'
    .1
    repeat
label christie_at_bath_lvl_3:
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
    "Кристи" "Снова ты!"

    "[gg]" "Ага."
    show GG:
        xalign .05
    with my_dissolve
    show image "cg/ep95/christie_bath/sister_restroom_2.png":
        ypos 1080
        easein 1.0 ypos 1100
    "Кристи" "Мне стоит прочитать тебе лекцию о личных границах, [gg]…"

    "[gg]" "Не будь злюкой. Ванна одна, а время ограничено. Мне тоже надо покупаться. "

    "Кристи" "Но ведь душевая кабинке свободна!"

    "[gg]" "И почему ты сама в ней не моешься?.."

    "Кристи" "Хочу лежать, а не стоять."

    "[gg]" "Ну вот."

    "Кристи" "И что ты предлагаешь?"

    "[gg]" "Я могу присоединиться. "

    "Кристи" "Тут, вообще-то, очень тесно…"

    "[gg]" "Ага. Я заметил."

    "[gg]" "Но что-то мне подсказывает, мы найдём способ уместиться."
    show image "cg/ep95/christie_bath/sister_restroom_2.png":
        ypos 1080
        easein 1.0 ypos 1080
    "Кристи" "Ну ладно, умник."

    "Кристи" "Давай попробуем."



    scene black
    with Dissolve(.3)
    $ renpy.pause(.5, hard = True)
    scene christie_at_bath_lvl_3_back
    show christie_at_bath_lvl_3 0
    show christie_at_bath_lvl_3_shadow:
        alpha 0.0
    if preferences.language in ('eng', None, 'rus'):
        show image comic_frame_v2_master
        show image comic_frame_v2_slave

        with my_dissolve
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            "{size=10} {/size}",
            __("Хех…"),
            "{size=8} {/size}"

            ), 
            size =  50,
            #plus_y = 50,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_3_gg_talk_1",        
        ) from _call_comic_frame_v2_label_508

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            "{size=10} {/size}",
            "…",
            "{size=8} {/size}"

            ), 
            size =  50,
            #plus_y = 50,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_1",        
        ) from _call_comic_frame_v2_label_509
        call comic_frame_v2_label((
            

            __("Знаешь, Кристи,"),
            __("а тут и вправду"),
            __("мало места.")
            

            ), 
            size =  50,
            #plus_y = 50,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_3_gg_talk_1",        
        ) from _call_comic_frame_v2_label_510


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            "{size=10} {/size}",
            __(" Собираешься "),
            __(" улизнуть? "),
            "{size=8} {/size}"

            ), 
            size =  50,
            #plus_y = 50,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_1",        
        ) from _call_comic_frame_v2_label_511
    else:
        with my_dissolve
        "[gg]" "Хех…"
        "Кристи" "…"
        "[gg]" "Знаешь, Кристи, а тут и вправду мало места."
        "Кристи" "Собираешься улизнуть?"
    show christie_day_mischief_lvl_2_water_drop:
        xpos 740
        ypos 50
       # zoom .05
        zoom .9
        alpha .0
        easein .7 ypos 70 alpha 1.0
    show christie_at_bath_lvl_3_shadow:
        easein .7 alpha .6

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            

            __("Едва ли у меня"),
            __("получится."),
            __("Ты плотно на мне"),
            __("лежишь.")
            

            ), 
            size =  37,
            #plus_y = 50,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_3_gg_talk_1",        
        ) from _call_comic_frame_v2_label_512
    else:

        "[gg]" "Едва ли у меня получится. "
        "[gg]" "Ты плотно на мне лежишь."
    show christie_day_mischief_lvl_2_water_drop:
        easein .7 alpha 0.0
    show christie_at_bath_lvl_3_shadow:
        easein .7 alpha 0.0

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            "{size=10} {/size}",
            __(" Тогда сиди "),
            __(" спокойно… "),
            __("И наслаждайся."),
            "{size=8} {/size}"

            ), 
            size =  40,
            #plus_y = 50,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_1",        
        ) from _call_comic_frame_v2_label_513
    else:


        "Кристи" "Тогда сиди спокойно… "
        "Кристи" "И наслаждайся."
    hide christie_day_mischief_lvl_2_water_drop

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            

            "{size=15} {/size}",
            __("Попробую."),
            "{size=8} {/size}"
            
            ), 
            size =  50,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
         show_label = "christie_at_bath_lvl_3_gg_talk_1",        
        ) from _call_comic_frame_v2_label_514
    else:

        "[gg]" "Попробую."
    show image '#000'
    with Dissolve(.3)
    $ renpy.pause(.5, hard = True)
    hide image '#000'
    show christie_at_bath_lvl_3 anim_1
    show christie_at_bath_lvl_3_bubbles_anim_1
    show christie_at_bath_lvl_3_shadow:
        alpha 1.0
    with my_dissolve
    #//Christie_Vana_Sex_2anim"
    #//Скорость x1"

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            

            "{size=20} {/size}",
            __("Извини…"),
            "{size=8} {/size}"
            
            ), 
            size =  50,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_2", ),
            say_pos = ["d", 20],
         show_label = "christie_at_bath_lvl_3_gg_talk_2",        
        ) from _call_comic_frame_v2_label_515
        call comic_frame_v2_label((
            
            __("За устроенный тобою"),
            __("дискомфорт"),
            __("в ванной..."),
            "{size=1} {/size}"

            ), 
            size = 35,
            plus_y = 15,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_516

        call comic_frame_v2_label((
            
            __("...или за то, что"),
            __("твой член тычет"),
            __("мне в киску?"),
            "{size=1} {/size}"

            ), 
            size = 35,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_517
        

        call comic_frame_v2_label((
            

            "{size=20} {/size}",
            __("За всё, хех…"),
            "{size=8} {/size}"
            
            ), 
            size =  50,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_2", ),
            say_pos = ["d", 120],
         show_label = "christie_at_bath_lvl_3_gg_talk_2",        
        ) from _call_comic_frame_v2_label_518



        call comic_frame_v2_label((
            
            __("Что ж…"),
            __("Предлагаю тебе"),
            __("довести начатое"),
            __("дело до конца."),
            "{size=1} {/size}"

            ), 
            size = 35,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 70],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_519
        
        call comic_frame_v2_label((
            
            __("И тогда уж я решу,"),
            __("прощать тебя или нет."),
         #   "{size=1} {/size}"

            ), 
            size = 35,
            plus_y = 15,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 20],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_520



        call comic_frame_v2_label((
            

            "{size=20} {/size}",
            __("Хороший план."),
            "{size=8} {/size}"
            
            ), 
            size =  50,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_2", ),
            say_pos = ["d", 180],
         show_label = "christie_at_bath_lvl_3_gg_talk_2",        
        ) from _call_comic_frame_v2_label_521


        call comic_frame_v2_label((
            
            __("Странно, что не"),
            __("ты сам его"),
            __("предложил."),
            "{size=1} {/size}"

            ), 
            size = 35,
            plus_y = 15,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 50],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_522



        call comic_frame_v2_label((
            

            "{size=10} {/size}",
            __("Ты стала"),
            __("более"),
            __("напористой…"),
            "{size=8} {/size}"
            
            ), 
            size  = 30,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_2", ),
            say_pos = ["d", 50],
         show_label = "christie_at_bath_lvl_3_gg_talk_2",        
        ) from _call_comic_frame_v2_label_523


        call comic_frame_v2_label((
            "{size=20} {/size}",
            
            __("И властной."),
            "{size=1} {/size}"

            ), 
            size = 45,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_524


        call comic_frame_v2_label((
            

            "{size=20} {/size}",
            __("  Читаешь  "),
            __("  мысли.  "),
            "{size=8} {/size}"
            
            ), 
            size  = 40,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_2", ),
            say_pos = ["d", 50],
         show_label = "christie_at_bath_lvl_3_gg_talk_2",        
        ) from _call_comic_frame_v2_label_525

        call comic_frame_v2_label((
            
            __("Значит, я буду права,"),
            __("если предположу,"),
            __("что тебе охота"),
            __("ускориться?.."),
            "{size=1} {/size}"

            ), 
            size = 35,
            plus_y = 15,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_526

        call comic_frame_v2_label((
            

            "{size=20} {/size}",
            __("  Ага…  "),
            "{size=8} {/size}"
            
            ), 
            size  = 40,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_2", ),
            say_pos = ["d", 70],
         show_label = "christie_at_bath_lvl_3_gg_talk_2",        
        ) from _call_comic_frame_v2_label_527
    else:

        "[gg]" "Извини…"
        "Кристи" "За устроенный тобою дискомфорт в ванной или за то, что твой член тычет мне в киску?"
        "[gg]" "За всё, хех…"
        "Кристи" "Что ж…"
        "Кристи" "Предлагаю тебе довести начатое дело до конца. И тогда уж я решу, прощать тебя или нет."
        "[gg]" "Хороший план. "
        "Кристи" "Странно, что не ты сам его предложил."
        "[gg]" "Ты стала более напористой…"
        "Кристи" "И властной."
        "[gg]" "Читаешь мысли."
        "Кристи" "Значит, я буду права, если предположу, что тебе охота ускориться?.."
        "[gg]" "Ага…"


    show christie_at_bath_lvl_3 anim_2
    hide christie_at_bath_lvl_3_bubbles_anim_1
    show christie_at_bath_lvl_3_bubbles_anim_2
    with my_dissolve
    #//Скорость x2"


    if preferences.language in ('eng', None, 'rus'):
        show image comic_frame_v2_master:    
            easein .2 ypos 500 alpha 0.0
        $ renpy.pause(.1, hard = True)
    menu christie_at_bath_lvl_3_speed_up_1:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_at_bath_lvl_3_speed_up_1


    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            __("Ты стал таким"),
            __("милым и податливым."),
            "{size=1} {/size}"

            ), 
            size = 35,
            plus_y = 23,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 25],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_528

        call comic_frame_v2_label((
            

            "{size=3} {/size}",
            __("О, мне приятно,"),
            __("что мои старания"),
            __("не прошли даром."),
            "{size=8} {/size}"
            
            ), 
            size  = 25,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_2", ),
            say_pos = ["d", 120],
         show_label = "christie_at_bath_lvl_3_gg_talk_2",        
        ) from _call_comic_frame_v2_label_529

        call comic_frame_v2_label((
            
            __("Аххх… Получается,"),
            __("из меня чудесный"),
            __("мотиватор."),
            "{size=1} {/size}"

            ), 
            size = 37,
            plus_y = 17,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_530
        call comic_frame_v2_label((
            

            "{size=8} {/size}",
            __("Мне нравится"),
            __("твоя система"),
            __("поощрений,"),
            __("хе-хе-хе."),
            "{size=8} {/size}"
            
            ), 
            size  = 25,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_2", ),
            say_pos = ["d", 30],
         show_label = "christie_at_bath_lvl_3_gg_talk_2",        
        ) from _call_comic_frame_v2_label_531

        call comic_frame_v2_label((
            
            __("Если мужчин так легко"),
            __("подтолкнуть к"),
            __("действиям, можно ли"),
            __("считать, что женщины"),
            __("правят миром?"),
            "{size=1} {/size}"

            ), 
            size = 33,
            plus_y = 15,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_532


        call comic_frame_v2_label((
            

            "{size=10} {/size}",
            __("Не знаю,"),
            __("что касается"),
            __("прочих парней,"),
            __("но в моём мире"),
            __("у тебя самые"),
            __("высокие полномочия."),
            "{size=8} {/size}"
            
            ), 
            size  = 40,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_3", yzoom = -1.0),
            say_pos = ["r", 100],       
            show_label = "christie_at_bath_lvl_3_gg_talk_3",        
        ) from _call_comic_frame_v2_label_533


        call comic_frame_v2_label((
            
            __("Ха!…"),
            __("Как"),
            __("любопытно…"),

            "{size=1} {/size}"

            ), 
            size = 35,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_534
        

        call comic_frame_v2_label((
            
            __("Не пора ли"),
            __("внести коррективы"),
            __("в твоё сознание?"),

            "{size=1} {/size}"

            ), 
            size = 35,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_535

        call comic_frame_v2_label((
            

            "{size=17} {/size}",
            __("Не знаю,"),
            __("Попробуй…"),
            "{size=8} {/size}"
            
            ), 
            size  = 40,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_2", ),
            say_pos = ["d", 55],
         show_label = "christie_at_bath_lvl_3_gg_talk_2",        
        ) from _call_comic_frame_v2_label_536

        call comic_frame_v2_label((
            
            __("Аххх…"),
            __("Хи-хи-хи!"),

            "{size=1} {/size}"

            ), 
            size = 45,
            plus_y = 14,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2_shake",        
        ) from _call_comic_frame_v2_label_537

        call comic_frame_v2_label((
            
            __("Доведи меня"),
            __("до оргазма,"),
            __("[gg]!"),
            
            "{size=1} {/size}"

            ), 
            size = 35,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_538

        call comic_frame_v2_label((
            
            __("Сделай меня"),
            __("счастливой."),
            

            "{size=1} {/size}"

            ), 
            size = 35,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_539
    else:

        "Кристи" "Ты стал таким милым и податливым."
        "[gg]" "О, мне приятно, что мои старания не прошли даром."
        "Кристи" "Аххх… Получается, из меня чудесный мотиватор. "
        "[gg]" "Мне нравится твоя система поощрений, хе-хе-хе."
        "Кристи" "Если мужчин так легко подтолкнуть к действиям, можно ли считать, что женщины правят миром?"
        "[gg]" "Не знаю, что касается прочих парней, но в моём мире у тебя самые высокие полномочия."
        "Кристи" "Ха!... Как любопытно…"
        "Кристи" "Не пора ли внести коррективы в твоё сознание?"
        "[gg]" "Попробуй…"
        "Кристи" "Аххх… Хи-хи-хи!"
        "Кристи" "Доведи меня до оргазма, [gg]!"
        "Кристи" "Сделай меня счастливой."


    hide christie_at_bath_lvl_3_bubbles_anim_2
    show christie_at_bath_lvl_3_bubbles_anim_3
    show christie_at_bath_lvl_3 anim_3
    with my_dissolve
    #//Скорость x3"


    if preferences.language in ('eng', None, 'rus'):
        show image comic_frame_v2_master:    
            easein .2 ypos 500 alpha 0.0
        $ renpy.pause(.1, hard = True)
    menu christie_at_bath_lvl_3_speed_up_2:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_at_bath_lvl_3_speed_up_2

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            

            "{size=10} {/size}",
            __("Охххх!!!"),
            __("{size=60}Да…{/size}"),
            __("Да…"),
            "{size=8} {/size}"
            
            ), 
            size  = 80,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_3", yzoom = -1.0),
            say_pos = ["r", 40],
         show_label = "christie_at_bath_lvl_3_gg_talk_3",        
        ) from _call_comic_frame_v2_label_540


        call comic_frame_v2_label((
            
            __("Твои усилия"),
            __("не проходят напрасно,"),
            __("[gg]."),
            

            "{size=1} {/size}"

            ), 
            size = 33,
            plus_y = 7,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_541

        call comic_frame_v2_label((
            
            __("Меня штормит"),
            __("электрическими"),
            __("волнами…"),
            

            "{size=1} {/size}"

            ), 
            size = 35,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_542

        call comic_frame_v2_label((
            
            __("Каждое твоё"),
            __("проникновение терзает"),
            __("меня разрядом"),
            __("удовольствия."),
            

            "{size=1} {/size}"

            ), 
            size = 33,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_543



        call comic_frame_v2_label((
            

            "{size=10} {/size}",
            __("Твоё изнеженное"),
            __("тело заводит"),
            __("меня ещё"),
            __("сильнее."),
            "{size=8} {/size}"
            
            ), 
            size  = 60,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_3", yzoom = -1.0),
            say_pos = ["r", 100],       
         show_label = "christie_at_bath_lvl_3_gg_talk_3",        
        ) from _call_comic_frame_v2_label_544



        call comic_frame_v2_label((
            

            "{size=10} {/size}",
            __("Я становлюсь"),
            __("более быстрым"),
            __("и грубым."),
            "{size=8} {/size}"
            
            ), 
            size  = 40,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_3", yzoom = -1.0),
            say_pos = ["r", 100],       
         show_label = "christie_at_bath_lvl_3_gg_talk_3",        
        ) from _call_comic_frame_v2_label_545


        call comic_frame_v2_label((
            
            __("О да, просто"),
            __("чудесно!"),
            __("Мне нравится."),
            

            "{size=1} {/size}"

            ), 
            size = 45,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_546

        call comic_frame_v2_label((
            
            __("Продолжай ускоряться."),
            __("Продолжай выплёскивать"),
            __("свою энергию в меня."),
            

            "{size=1} {/size}"

            ), 
            size = 30,
            plus_y = 9,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_547


        call comic_frame_v2_label((
            
            __("Это лишь"),
            __("усиливает"),
            __("наслаждение."),
            

            "{size=1} {/size}"

            ), 
            size = 50,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_548


        call comic_frame_v2_label((
            

            "{size=10} {/size}",
            __("Чёрт…"),
            __("Какой же"),
            __("кайф!"),
            "{size=8} {/size}"
            
            ), 
            size  = 60,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_3", yzoom = -1.0),
            say_pos = ["r", 100],       
         show_label = "christie_at_bath_lvl_3_gg_talk_3",        
        ) from _call_comic_frame_v2_label_549



        call comic_frame_v2_label((
            

            "{size=10} {/size}",
            __("Я… "),
            __("Я хочу"),
            __("кончить, Кристи!"),
            "{size=8} {/size}"
            
            ), 
            size  = 70,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_3", yzoom = -1.0),
            say_pos = ["r", 100],       
         show_label = "christie_at_bath_lvl_3_gg_talk_3",        
        ) from _call_comic_frame_v2_label_550


        call comic_frame_v2_label((
            
            __("В меня?.."),
            __("Здесь?.."),
            __("Сейчас?.."),
            

            "{size=1} {/size}"

            ), 
            size = 50,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 40],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_551


        call comic_frame_v2_label((
            

            "{size=10} {/size}",
            __("Да. Детка."),
            __("Я хочу залить"),
            __("тебя всю,"),
            __("до самого верха!"),
            "{size=8} {/size}"
            
            ), 
            size  = 60,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_3", yzoom = -1.0),
            say_pos = ["r", 100],       
         show_label = "christie_at_bath_lvl_3_gg_talk_3",        
        ) from _call_comic_frame_v2_label_552

        call comic_frame_v2_label((
            
            __("Ах… "),
            __("Как приятно"),
            __("это слышать."),
            

            "{size=1} {/size}"

            ), 
            size = 40,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 40],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_553

        call comic_frame_v2_label((
            
            __("Ну давай, зайчонок."),
            __("Кончи в меня"),
            __("сколько сможешь."),
            __("Кошка хочет"),
            __("молока..."),
            

            "{size=1} {/size}"

            ), 
            size = 40,
            plus_y = 18,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 40],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_554




        call comic_frame_v2_label((

            "{size=4} {/size}",      
            __("хи-хи-хи!"),
            

            "{size=1} {/size}"

            ), 
            size = 80,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 40],
         show_label = "christie_at_bath_lvl_3_christie_talk_2_shake",        
        ) from _call_comic_frame_v2_label_555

        #//Кончить
        show image comic_frame_v2_master:    
            easein .2 ypos 300 alpha 0.0
        $ renpy.pause(.1, hard = True)
    else:

        "[gg]" "Охххх!!!"
        "[gg]" "Да… Да…"
        "Кристи" "Твои усилия не проходят напрасно, [gg]."
        "Кристи" "Меня штормит электрическими волнами…"
        "Кристи" "Каждое твоё проникновение терзает меня разрядом удовольствия."
        "[gg]" "Твоё изнеженное тело заводит меня ещё сильнее."
        "[gg]" "Я становлюсь более быстрым и грубым."
        "Кристи" "О да, просто чудесно! Мне нравится. "
        "Кристи" "Продолжай ускоряться. Продолжай выплёскивать свою энергию в меня. Это лишь усиливает наслаждение."
        "[gg]" "Чёрт… Какой же кайф!"
        "[gg]" "Я… "
        "[gg]" "Я хочу кончить, Кристи."
        "Кристи" "В меня?.. Здесь?.. Сейчас?.."
        "[gg]" "Да. Детка. Я хочу залить тебя всю, до самого верха! "
        "Кристи" "Ах… "
        "Кристи" "Как приятно это слышать."
        "Кристи" "Ну давай, зайчонок. Кончи в меня сколько сможешь. "
        "Кристи" "Кошка хочет молока, хи-хи-хи!"

    menu christie_at_bath_lvl_3_speed_up_3:
        "Кончить":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_at_bath_lvl_3_speed_up_3

    #//кончить"
    # "" "#//Скорость x3"

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            

            "{size=10} {/size}",
            __("Я на"),
            __("грааанииии…"),
            "{size=8} {/size}"
            
            ), 
            size  = 70,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_3", yzoom = -1.0),
            say_pos = ["r", 100],       
         show_label = "christie_at_bath_lvl_3_gg_talk_3",        
        ) from _call_comic_frame_v2_label_556

        call comic_frame_v2_label((
            
            __("Я тожеееее…"),
            __("Давай,"),
            __("[gg],"),
            __("сделай это!"),
            

            "{size=1} {/size}"

            ), 
            size = 43,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 40],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_557



        $ christie_at_bath_lvl_3_cum_1 = Composite((1050, 180), (0, 0), Solid("#000"))

        #////Kristy_Vana_Minet_3 Animation
        $ christie_at_bath_lvl_3_cum_2 = Composite((980, 180), 
            #(0, 0), Solid("#000"),
            (0, 0), Frame(Transform('interface/comic_v2/bg_frame_2.png', alpha = .8), Borders(64, 64, 64, 64)),
            (20, 50), Text(
                            __( "Кончааааааааюююююууууууууу!!!"), 
                            kerning  = 5,
                            size     = 70,
                            outlines = [(2, "#000a", 0, 0),],
                            font = "fonts/mango_comics_er.ttf",
                            
                            ),
            (1020, 60), Transform("comic_frame_say_3")
            )
        $ christie_at_bath_lvl_3_cum_3 = AlphaMask(christie_at_bath_lvl_3_cum_2, At(christie_at_bath_lvl_3_cum_1, christie_root_52_cum_transform))
        show image comic_frame_v2_master:    
            easein .2 ypos 500 alpha 0.0
        show image christie_at_bath_lvl_3_cum_3: #comic_frame_v2_0:
            
            zoom .7
            ypos  70
            xpos  100
            yanchor .5
            alpha 1.0

        #hide image comic_frame_v2_slave
        #show image christie_root_52_cum_2
        #show
        $ renpy.pause(.95)


        show christie_at_bath_lvl_3 cum
        hide image christie_at_bath_lvl_3_cum_3
        hide christie_at_bath_lvl_3_bubbles_anim_3
        #show image '#fff'
        with Dissolve(.5)
        $ renpy.pause(.7, hard = True)
        scene christie_at_bath_lvl_3_back
        show christie_at_bath_lvl_3 cum
        show christie_at_bath_lvl_3_shadow
        show christie_at_bath_lvl_3_sperm_0:
            pos (0, 0) alpha 1.0
            pause 1.0
            linear .7 pos (8, 8) alpha .5
        
        $ renpy.pause(.75, hard = True)

        show christie_at_bath_lvl_3_sperm_1:
            pos (200, -100) alpha 1.0 xzoom -1
            #pause 1.0
            linear .7 pos (203, -50) alpha .8

        $ renpy.pause(.75, hard = True)

        show christie_at_bath_lvl_3_sperm_2:
            pos (0, 0) alpha 1.0
            #pause 1.0
            linear .7 pos (50, 50) alpha .8

        $ renpy.pause(.75, hard = True)

        show christie_at_bath_lvl_3_sperm_3:
            pos (200, -100) alpha 1.0 xzoom -1
            #pause 1.0
            linear .7 pos (250, -50) alpha .8

        $ renpy.pause(.75, hard = True)
        # show christie_at_bath_lvl_3_sperm_4:
        #     pos (0, 0) alpha 1.0
        #     #pause 1.0
        #     linear .7 pos (12, 30) alpha .5
        # $ renpy.pause(.75, hard = True)
        # show christie_at_bath_lvl_3_sperm_5:
        #     pos (200, -100) alpha 1.0 xzoom -1
        #     #pause 1.0
        #     linear .7 pos (208, -92) alpha .5
        
        # show christie_at_bath_lvl_3_sperm_1:
        #     ypos 0 alpha 1.0
        #     linear .75 ypos 10 alpha .0


       # with Dissolve(.3)
        $ renpy.pause(.75, hard = True)
        show christie_at_bath_lvl_3_sperm_6:
            pos (0, 0) alpha 1.0
            linear .7 pos (8, 8+30) alpha .5
        
        show christie_at_bath_lvl_3_sperm_7:
            pos (200, -100) alpha 1.0 xzoom -1
            #pause 1.0
            linear .7 pos (203, -50+30) alpha .8

        show christie_at_bath_lvl_3_sperm_8:
            pos (0, 0) alpha 1.0
            #pause 1.0
            linear .7 pos (50, 50+30) alpha .8

        
        show christie_at_bath_lvl_3_sperm_9:
            pos (200, -100) alpha 1.0 xzoom -1
            #pause 1.0
            linear .7 pos (250, -50+30) alpha .8

        
        show christie_at_bath_lvl_3_sperm_10:
            pos (0, 0) alpha 1.0
            #pause 1.0
            linear .7 pos (12, 30+30) alpha .5
        
        show christie_at_bath_lvl_3_sperm_11:
            pos (200, -100) alpha 1.0 xzoom -1
            #pause 1.0
            linear .7 pos (208, -92+30) alpha .5
        $ renpy.pause(1.0, hard = True)
        show image comic_frame_v2_master
        show image comic_frame_v2_slave
        with my_dissolve
        call comic_frame_v2_label((
            
            __("Вау…"),
            __("Это было круто."),

            "{size=1} {/size}"

            ), 
            size = 40,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 40],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_558



        call comic_frame_v2_label((
            

            "{size=17} {/size}",
            __("Спасибо."),
            "{size=8} {/size}"
            
            ), 
            size  = 50,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_3", yzoom = -1.0),
            say_pos = ["r", 30],       
         show_label = "christie_at_bath_lvl_3_gg_talk_3",        
        ) from _call_comic_frame_v2_label_559

        call comic_frame_v2_label((
            
            __("Что ж… Я прощаю"),
            __("тебя за неудобства,"),
            __("который ты"),
            __("мне создал"),
            __("своим появлением"),
            __("здесь."),

            "{size=1} {/size}"

            ), 
            size = 35,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 40],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_560


        call comic_frame_v2_label((
            

            "{size=10} {/size}",
            __("Ха!"),
            __("Сколько в"),
            __("тебе милосердия."),
            "{size=8} {/size}"
            
            ), 
            size  = 40,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_3", yzoom = -1.0),
            say_pos = ["r", 30],       
         show_label = "christie_at_bath_lvl_3_gg_talk_3",        
        ) from _call_comic_frame_v2_label_561

        call comic_frame_v2_label((
            
            __("Ага."),
            __("Приходи ещё,"),
            __("грязнуля."),

            "{size=1} {/size}"

            ), 
            size = 43,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 40],
         show_label = "christie_at_bath_lvl_3_christie_talk_2",        
        ) from _call_comic_frame_v2_label_562


        call comic_frame_v2_label((
            

            "{size=20} {/size}",
            __("Обязательно."),
            "{size=8} {/size}"
            
            ), 
            size  = 40,
            #plus_y = 50,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_2", ),
            say_pos = ["d", 40],
         show_label = "christie_at_bath_lvl_3_gg_talk_2",        
        ) from _call_comic_frame_v2_label_563
    else:


        "[gg]" "Я на грааанииии….."
        "Кристи" "Я тожеееее…. Давай, [gg], сделай это!"
        "[gg]" "Кончааааааааюююююууууууууу!!!"
        call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_40
        show christie_at_bath_lvl_3 cum
        hide image christie_at_bath_lvl_3_cum_3
        hide christie_at_bath_lvl_3_bubbles_anim_3
        #show image '#fff'
        with my_dissolve
        $ renpy.pause(.7, hard = True)
        scene christie_at_bath_lvl_3_back
        show christie_at_bath_lvl_3 cum
        show christie_at_bath_lvl_3_shadow
        show christie_at_bath_lvl_3_sperm_0:
            pos (0, 0) alpha 1.0
            pause 1.0
            linear .7 pos (8, 8) alpha .5
        
        $ renpy.pause(.75, hard = True)

        show christie_at_bath_lvl_3_sperm_1:
            pos (200, -100) alpha 1.0 xzoom -1
            #pause 1.0
            linear .7 pos (203, -50) alpha .8

        $ renpy.pause(.75, hard = True)

        show christie_at_bath_lvl_3_sperm_2:
            pos (0, 0) alpha 1.0
            #pause 1.0
            linear .7 pos (50, 50) alpha .8

        $ renpy.pause(.75, hard = True)

        show christie_at_bath_lvl_3_sperm_3:
            pos (200, -100) alpha 1.0 xzoom -1
            #pause 1.0
            linear .7 pos (250, -50) alpha .8

        $ renpy.pause(.75, hard = True)

        $ renpy.pause(.75, hard = True)
        show christie_at_bath_lvl_3_sperm_6:
            pos (0, 0) alpha 1.0
            linear .7 pos (8, 8+30) alpha .5
        
        show christie_at_bath_lvl_3_sperm_7:
            pos (200, -100) alpha 1.0 xzoom -1
            #pause 1.0
            linear .7 pos (203, -50+30) alpha .8

        show christie_at_bath_lvl_3_sperm_8:
            pos (0, 0) alpha 1.0
            #pause 1.0
            linear .7 pos (50, 50+30) alpha .8

        
        show christie_at_bath_lvl_3_sperm_9:
            pos (200, -100) alpha 1.0 xzoom -1
            #pause 1.0
            linear .7 pos (250, -50+30) alpha .8

        
        show christie_at_bath_lvl_3_sperm_10:
            pos (0, 0) alpha 1.0
            #pause 1.0
            linear .7 pos (12, 30+30) alpha .5
        
        show christie_at_bath_lvl_3_sperm_11:
            pos (200, -100) alpha 1.0 xzoom -1
            #pause 1.0
            linear .7 pos (208, -92+30) alpha .5
        $ renpy.pause(1.0, hard = True)

        "Кристи" "Вау…"
        "Кристи" "Это было круто."
        "[gg]" "Спасибо."
        "Кристи" "Что ж…"
        "Кристи" "Я прощаю тебя за неудобства, который ты мне создал своим появлением здесь. "
        "[gg]" "Ха! Сколько в тебе милосердия."
        "Кристи" "Ага."
        "Кристи" "Приходи ещё, грязнуля."
        "[gg]" "Обязательно."
    scene black with Dissolve(.5)
    $ renpy.pause(1, hard = True)
    python:
        
        add_ach('ACH_7')
        
        try:
            del christie_at_bath_lvl_3_cum_1
        except:
            pass

        try:
            del christie_at_bath_lvl_3_cum_2
        except:
            pass

        try:
            del christie_at_bath_lvl_3_cum_3
        except:
            pass

        #achievement.grant("ACH_7")
        #achievement.sync()

    if not from_gallery_check():

        $ add_to_gallery(43)
        $ location_now = "Corridor"
            

        
        $ time.time_forward(jump_to_main_interface = False)

    jump main_interface_label