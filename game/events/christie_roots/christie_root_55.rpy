label christie_root_55_psi_talk_shake:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1300
        ypos 25
        xanchor 0.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.1 ypos 31
            easein 0.1 ypos 25
            easein 0.1 ypos 31
            easein 0.1 ypos 25
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return

label christie_root_55_psi_talk_shake_2:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1380
        ypos 25
        xanchor 0.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.1 ypos 31
            easein 0.1 ypos 25
            easein 0.1 ypos 31
            easein 0.1 ypos 25
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return
label christie_root_55_psi_talk_1:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1300
        ypos 75
        xanchor 0.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.2 ypos 25
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return

label christie_root_55_psi_talk_2:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1900
        ypos 75
        xanchor 1.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.2 ypos 25
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return

label christie_root_55_psi_talk_3:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1400
        ypos 540
        xanchor 0.0
        yanchor 1.0
        alpha .0
        parallel:
            easein 0.2 ypos 500
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return



label christie_root_55_psi_talk_4:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1450
        ypos 25
        xanchor 0.0
        yanchor 0.0
        alpha .0
        #parallel:
        #   easein 0.2 ypos 25
        #parallel:
        ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return



label christie_root_55_psi_talk_5:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1300
        ypos 25
        xanchor 0.0
        yanchor 0.0
        alpha .0
        #parallel:
        #   easein 0.2 ypos 25
        #parallel:
        ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return




label christie_root_55_psi_talk_6:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1300
        ypos 150
        xanchor 0.0
        yanchor 0.0
        alpha .0
        #parallel:
        #   easein 0.2 ypos 25
        #parallel:
        ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return



label christie_root_55_officer_talk_0:
#getattr(store, "comic_frame_v2_"+str(main_comic_frame_v2), "#0000")
    
    show image comic_frame_v2_master: #comic_frame_v2_0:
        
        zoom 1.0
        xpos 100
        ypos 25
        xanchor 0.0
        yanchor 0.0
        alpha .0
        parallel:
            easein .1 ypos 30
            easein .1 ypos 25
            easein .1 ypos 30
            easein .1 ypos 25

        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.4, hard = True)
    return

label christie_root_55_officer_talk_1:
#getattr(store, "comic_frame_v2_"+str(main_comic_frame_v2), "#0000")
    
    show image comic_frame_v2_master: #comic_frame_v2_0:
        
        zoom 1.0
        xpos 100
        ypos 25
        xanchor 0.0
        yanchor 0.0
        alpha .0
        ease .2 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return

label christie_root_55_officer_talk_2:
#getattr(store, "comic_frame_v2_"+str(main_comic_frame_v2), "#0000")
    
    show image comic_frame_v2_master: #comic_frame_v2_0:
        
        zoom .52
        xpos 8
        ypos 260
        xanchor 0.0
        yanchor 1.0
        alpha .0
        parallel:
            ease .2 alpha 1.0
        parallel:
            ease .2 ypos 285
    
    $ renpy.pause(.2, hard = True)
    return


label christie_root_55_officer_talk_shake_1_5:
#getattr(store, "comic_frame_v2_"+str(main_comic_frame_v2), "#0000")
    
    show image comic_frame_v2_master: #comic_frame_v2_0:
        
        zoom .52
        xpos 90
        ypos 260
        xanchor 0.0
        yanchor 1.0
        alpha .0
        parallel:
            ease .1 alpha 1.0
        parallel:
            ease .1 ypos 245
            ease .1 ypos 250
            ease .1 ypos 245
            ease .1 ypos 250
            
    $ renpy.pause(.4, hard = True)
    return


label christie_root_55_officer_talk_shake_2:
#getattr(store, "comic_frame_v2_"+str(main_comic_frame_v2), "#0000")
    
    show image comic_frame_v2_master: #comic_frame_v2_0:
        
        zoom .52
        xpos 8
        ypos 260
        xanchor 0.0
        yanchor 1.0
        alpha .0
        parallel:
            ease .1 alpha 1.0
        parallel:
            ease .1 ypos 245
            ease .1 ypos 250
            ease .1 ypos 245
            ease .1 ypos 250
            
    $ renpy.pause(.4, hard = True)
    return

label christie_root_55_officer_talk_shake:
#getattr(store, "comic_frame_v2_"+str(main_comic_frame_v2), "#0000")
    
    show image comic_frame_v2_master: #comic_frame_v2_0:
        
        zoom .52
        xpos 8
        ypos 260
        xanchor 0.0
        yanchor 1.0
        alpha .0
        parallel:
            ease .1 alpha 1.0
        parallel:
            ease .1 ypos 280
            ease .1 ypos 285
            ease .1 ypos 280
            ease .1 ypos 285
            
    $ renpy.pause(.4, hard = True)
    return

label christie_root_55_officer_talk_3:
#getattr(store, "comic_frame_v2_"+str(main_comic_frame_v2), "#0000")
    
    show image comic_frame_v2_master: #comic_frame_v2_0:
        
        zoom .52
        xpos 10
        ypos 280
        xanchor 0.0
        yanchor 1.0
        alpha .0
        parallel:
            ease .1 alpha 1.0
        parallel:
            ease .1 ypos 290
            ease .1 ypos 285
            ease .1 ypos 290
            ease .1 ypos 285
            ease .1 ypos 290
            
    
    $ renpy.pause(.5, hard = True)
    return
image ep9_christie_root_55_anim_1 0 = 'cg/ep9/psi/2/a1.png'

image ep9_christie_root_55_anim_2 5 =  'cg/ep9/psi/2/d5.png'

image christie_root_55_m 1 = "cg/ep9/psi/2/m1.png"


image christie_root_55_m 2 = "cg/ep9/psi/2/m2.png"

image ep9_christie_root_55_anim_2 6 =  'cg/ep9/psi/2/d6.png'



image ep9_christie_root_55_anim_2 1:


    'cg/ep9/psi/2/d1.png'
    .17

    'cg/ep9/psi/2/d2.png'
    .17

    'cg/ep9/psi/2/d3.png'
    .17

    'cg/ep9/psi/2/d4.png'
    .17


    'cg/ep9/psi/2/d3.png'
    .17

    'cg/ep9/psi/2/d2.png'
    .17
    repeat


image ep9_christie_root_55_anim_2 2:


    'cg/ep9/psi/2/d1.png'
    .12

    'cg/ep9/psi/2/d2.png'
    .12

    'cg/ep9/psi/2/d3.png'
    .12

    'cg/ep9/psi/2/d4.png'
    .12


    'cg/ep9/psi/2/d3.png'
    .12

    'cg/ep9/psi/2/d2.png'
    .12
    repeat

image ep9_christie_root_55_anim_2 3:


    'cg/ep9/psi/2/d1.png'
    .08

    'cg/ep9/psi/2/d2.png'
    .08

    'cg/ep9/psi/2/d3.png'
    .08

    'cg/ep9/psi/2/d4.png'
    .08


    'cg/ep9/psi/2/d3.png'
    .08

    'cg/ep9/psi/2/d2.png'
    .08
    repeat











image ep9_christie_root_55_anim_1 1:


    'cg/ep9/psi/2/a1.png'
    .17

    'cg/ep9/psi/2/a2.png'
    .17

    'cg/ep9/psi/2/a3.png'
    .17

    'cg/ep9/psi/2/a4.png'
    .17

    'cg/ep9/psi/2/a5.png'
    .17

    'cg/ep9/psi/2/a6.png'
    .17

    'cg/ep9/psi/2/a7.png'
    .17

    'cg/ep9/psi/2/a8.png'
    .17

    'cg/ep9/psi/2/a9.png'
    .17


    repeat


image ep9_christie_root_55_anim_1 2:


    'cg/ep9/psi/2/a1.png'
    .12

    'cg/ep9/psi/2/a2.png'
    .12

    'cg/ep9/psi/2/a3.png'
    .12

    'cg/ep9/psi/2/a4.png'
    .12

    'cg/ep9/psi/2/a5.png'
    .12

    'cg/ep9/psi/2/a6.png'
    .12

    'cg/ep9/psi/2/a5.png'
    .12

    'cg/ep9/psi/2/a4.png'
    .12

    'cg/ep9/psi/2/a3.png'
    .12


    'cg/ep9/psi/2/a2.png'
    .12


    repeat





image ep9_christie_root_55_anim_1 3:


    'cg/ep9/psi/2/a1.png'
    .08

    'cg/ep9/psi/2/a2.png'
    .08

    'cg/ep9/psi/2/a3.png'
    .08

    'cg/ep9/psi/2/a4.png'
    .08

    'cg/ep9/psi/2/a5.png'
    .08

    'cg/ep9/psi/2/a4.png'
    .08

    'cg/ep9/psi/2/a3.png'
    .08



    'cg/ep9/psi/2/a2.png'
    .08


    repeat







label christie_root_55:
    #Отправиться к Сьюзен и показать ей доказательства измены мужа. 
    #"ext" "Активировать Сьюзен дома Утром или Днём."
    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    scene expression 'cg/christie_root/Psi_Build.png'
    with Dissolve(.25)

    $ renpy.pause(.25, hard = True)

    call screen rtrn_screen('cg/christie_root/Psi_Build_Door.png')

    scene black with Dissolve(.25)
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    scene expression 'cg/christie_root/psi_corridor.png'
    with Dissolve(.25)
    $ renpy.pause(.5, hard = True)
    call screen rtrn_screen

    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    if not from_gallery_check():
        $ events.pop('christie_root_16', 0)

    scene black with Dissolve(.5)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    $ renpy.pause(.5, hard = True)

    scene expression 'cg/christie_root/psi_corridor.png'
    show Psi Normal
    show Psi Normal:
        xalign .8
        ypos 1085

    with Dissolve(.5)

    $ events.pop('christie_root_55', 0)

    show GG Normal
    show GG Normal at go_from_left

    "[gg]" "Здравствуйте, Сьюзен."
    
    "Сьюзан" "Привет, [gg]."
    show GG Normal:
        xalign .15
    with my_dissolve
    "[gg]" "Сегодня мне есть что вам поведать."
    show Psi Normal
    "Сьюзан" "Тогда жду тебя в своём кабинете. "

    show Psi:
        xzoom -1

        easein_cubic 2 xalign 1.5
    
    show GG:
        easein_cubic 3 xalign 1.5
    $ renpy.pause(1.5, hard = True)
    #"ext" "Psi_1"


    scene expression 'cg/christie_root/psi_scene.png'
    show Psi Invis
    show Psi Invis:
        xalign .85
    show GG Invis
    show GG Invis:
        xalign .15
    with my_dissolve

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "Сьюзен" "Вне зависимости от того, что ты собираешься мне рассказать, мы можем начать сеанс с тебя."
    #"ext" "Psi_2"
    scene expression 'cg/christie_root/psi_scene_2.png'
    show Psi Invis
    show Psi Invis:
        xalign .85
    show GG Invis
    show GG Invis:
        xalign .15
    with my_dissolve

    "[gg]" "Извините, но я больше не нуждаюсь в вашей помощи, Сьюзен."
    #"ext" "Psi_1"

    scene expression 'cg/christie_root/psi_scene.png'
    show Psi Invis
    show Psi Invis:
        xalign .85
    show GG Invis
    show GG Invis:
        xalign .15
    with my_dissolve

    "Сьюзен" "Аххх… Занимательно."
    "Сьюзен" "Твои отношения с Кристи достигли апогея?"
    "[gg]" "Чтобы там ни было, я всецело удовлетворён текущим положением вещей."
    "Сьюзен" "Радостно это слышать, [gg]."
    "Сьюзен" "Надеюсь, моя скромная помощь тебе пригодилась."
    "[gg]" "Пригодилась. И я благодарен вам за это."
    "[gg]" "Сейчас я собираюсь завершить наше сотрудничество, выполнив свою часть сделки. "
    "Сьюзен" "Хм… Как странно."
    "Сьюзен" "Я слышу нотки недоверия в твоём голосе. Ты боишься меня?"
    "[gg]" "В какой-то степени."
    "Сьюзен" "И что не так?"
    "[gg]" "Я считаю, что вы не до конца откровенны со мной."
    "Сьюзен" "Возможно и так."
    "Сьюзен" "А возможно, ты предвзят ко мне из-за влияния Кристи."
    "[gg]" "Давайте вы просто взглянете на запись и мы разойдёмся."
    "Сьюзен" "Хорошо-хорошо. Не хочу тебя задерживать."
    "[gg]" "Я бы посоветовал смотреть это видео наедине с собой."
    "Сьюзен" "Всё в порядке, [gg]. Я готова к худшему."
    "[gg]" "Ну ладно…"
    #"ext" "Psi_2Mobile"
    #scene image '#000' with my_dissolve
    #"" "{color=#F00}Psi_2Mobile{/color}"
    #"ext" "//
    #"" "{i}Какофония звуков, состоящих из бурных вздохов и шлепков{/i}"
    "Сьюзен" "Я до последнего надеялась, чтобы всё окажется куда прозаичнее… Но это."
    "Сьюзен" "Это…."
    "Сьюзен" "Просто тяжело осознать…"
    "Сьюзен" "Подтвердились мои худшие опасения."
    #"ext" "Psi_2"
    scene expression 'cg/christie_root/psi_scene_2.png'
    show Psi Invis
    show Psi Invis:
        xalign .85
    show GG Invis
    show GG Invis:
        xalign .15
    with my_dissolve
    "[gg]" "Сочувствую."

    scene expression 'cg/christie_root/psi_scene.png'
    show Psi Invis
    show Psi Invis:
        xalign .85
    show GG Invis
    show GG Invis:
        xalign .15
    with my_dissolve
    #"ext" "Psi_1"
    "Сьюзен" "Спасибо, [gg]."
    "Сьюзен" "Мне очень приятна твоя поддержка."
    "[gg]" "Что вы собираетесь теперь делать?"
    "Сьюзен" "Не знаю, если честно."
    "Сьюзен" "Это многое меняет…"
    "Сьюзен" "Мне нужно переосмыслить эту ситуацию. Понять, чего я на самом деле хочу и к чему это может привести."
    "[gg]" "Понимаю."
    "[gg]" "Теперь, если позволите, я покину вас."

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)

    scene image 'cg/ep9/psi/Psi_Nice_Tits.png'
    show Psi Invis
    show Psi Invis:
        xalign .85
    show GG Invis
    show GG Invis:
        xalign .15
    with my_vpunch
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/aerosol-of-my-love-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Сьюзен" "Нет, пожалуйста, останься."
    "[gg]" "А?"
    "Сьюзен" "Не оставляй меня одну в такой ситуации."
    "Сьюзен" "Я боюсь натворить глупостей."
    scene image "cg/ep9/psi/1/1.png"
    show Psi Invis
    show Psi Invis:
        xalign .85
    show GG Invis
    show GG Invis:
        xalign .15
    with my_dissolve
    "[gg]" "Извините, но я должен идти…"
    #"ext" "Psi_SexTits_1"
    scene image "cg/ep9/psi/1/2.png"
    show Psi Invis
    show Psi Invis:
        xalign .85
    show GG Invis
    show GG Invis:
        xalign .15
    with my_vpunch
    "Сьюзен" "Нет, не сейчас. Молю."
    "[gg]" "Вы совершаете ошибку, Сьюзен."
    scene image '#000' with Dissolve(.3)
    $ renpy.pause(.5, hard = True)
    scene image "cg/ep9/psi/1/3.png"



    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/aerosol-of-my-love-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    if preferences.language in (None, 'eng', 'rus'):

        show image comic_frame_v2_master
        show image comic_frame_v2_slave

        show image comic_frame_v2_master:
            zoom .7
            xpos 900
            ypos 250
            xanchor 1.0
            yanchor .5
            alpha .0

        show image comic_frame_v2_slave:
            zoom .7
            xpos 900
            ypos 250
            xanchor 1.0
            yanchor .5
            alpha .0
        
        with Dissolve(.2)
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Теперь, когда я знаю"),
            __("тайну своего мужа,"),
            __("я вольна совершать"),
            __("любые проступки.")

            ), 
            size =  50,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3", yzoom = -1),
            say_pos = ["r", 100],
            
        ) from _call_comic_frame_v2_label   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Позволь мне"),
            __("отблагодарить тебя,"),
            "[gg]."

            ), 
            size =  50,
            plus_y = 20,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3", yzoom = -1),
            say_pos = ["r", 100],
            
        ) from _call_comic_frame_v2_label_1   



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Ты оказал мне"),
            __("неоценимую услугу."),
            

            ), 
            size =  50,
            plus_y = 5,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3", yzoom = -1),
            say_pos = ["r", 20],
            
        ) from _call_comic_frame_v2_label_2   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Только если это навсегда"),
            __("поставит точку в нашем"),
            __("сотрудничестве…")
            

            ), 
            size =  50,
            plus_y = 10 ,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", xzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_3   

    else:

        show Psi Invis
        show Psi Invis:
            xalign .75
        show GG Invis
        show GG Invis:
            xalign .15
        with my_dissolve
        "Сьюзен" "Теперь, когда я знаю тайну своего мужа, я вольна совершать любые проступки."
        "Сьюзен" "Позволь мне отблагодарить тебя, [gg]."
        "Сьюзен" "Ты оказал мне неоценимую услугу."
        "[gg]" "Только если это навсегда поставит точку в нашем сотрудничестве…"


    scene image "cg/ep9/psi/2/bg.png"
    show ep9_christie_root_55_anim_1 0
    #show christie_root_55_m 1
    show image "cg/ep9/psi/2/wall.png"

    #show image "cg/ep9/psi/2/fg.png"

    if preferences.language in (None, 'eng', 'rus'):

        show image comic_frame_v2_master:
            zoom .7
            xpos 1300
            ypos 25
            xanchor 0.0
            yanchor 0.0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .7
            xpos 1300
            ypos 25
            xanchor 0.0
            yanchor 0.0
            alpha .0
        
        with my_dissolve
    

        call comic_frame_v2_label(
            
            __("Оххх.. Мы поставим эту\nточку вместе."),
            
            size =  50,
            plus_y = 10,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 250],
            
        ) from _call_comic_frame_v2_label_4   


        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Жирную."),
            __("Длинную."),
            __("И тооооолстую.")
            

            ), 
            size =  50,
            plus_y = 10,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 200],
            
        ) from _call_comic_frame_v2_label_5   





        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Родная, я дома."),

            ), 
            size =  40,
            plus_y = 50,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", xzoom = -1),
            say_pos = ["l", 30],
         show_label = "christie_root_55_officer_talk_0",        
        ) from _call_comic_frame_v2_label_6   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Чёрт!"),

            ), 
            size =  60,
            plus_y = 50,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", xzoom = -1),
            say_pos = ["l", 30],
         show_label = "christie_root_55_psi_talk_1",        
        ) from _call_comic_frame_v2_label_7   

        

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60),
            __("Он вернулся раньше,"),
            __("чем я ожидала."),
            # "Жирную."),
            # "Длинную."),
            # "И тооооолстую.")
            

            ), 
            size =  50,
            plus_y = 10,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 250],
            
        ) from _call_comic_frame_v2_label_8   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Сьюзен, ты у себя?.."),

            ), 
            size =  40,
            plus_y = 50,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", xzoom = -1),
            say_pos = ["l", 30],
         show_label = "christie_root_55_officer_talk_1",        
        ) from _call_comic_frame_v2_label_9   
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            "     ....     ",

            ), 
            size   =  60,
            plus_y = 10,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 250],   

         show_label = "christie_root_55_psi_talk_1",      
        ) from _call_comic_frame_v2_label_10   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Вы не можете"),
            __("не ответить…")

            ), 
            size =  60,
            plus_y = 12,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", xzoom = -1),
            say_pos = ["l", 30], 
        ) from _call_comic_frame_v2_label_11   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Д..Да, милый."),
            __('Я дома.')

            ), 
            size =  50,
            plus_y = 10,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 250],   
        ) from _call_comic_frame_v2_label_12   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("В данный момент у меня"),
            __("ещё длится сеанс"),
            __("с клиентом.")
            #, ",

            ), 
            size =  45,
            plus_y = 15,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 250],   
        ) from _call_comic_frame_v2_label_13   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("И я бы попросила"),
            __("Не тревожить нас"),
            __("какое-то время.")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  45,
            plus_y = 15,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 250],   
        ) from _call_comic_frame_v2_label_14   
    else:
        show Psi Invis
        show Psi Invis:
            xalign .92
        show GG Invis
        show GG Invis:
            xalign .6
        show Officer Invis
        show Officer Invis:
            xalign .0
        
        with my_dissolve


        "Сьюзен" "Оххх.. Мы поставим эту точку вместе. Жирную. Длинную. И тооооолстую. "
        "Офицер" "Родная, я дома. "
        "[gg]" "Чёрт!"
        "Сьюзен" "Он вернулся раньше, чем я ожидала. "
        "Офицер" "Сьюзен, ты у себя?.."
        "Сьюзен" "…."
        "[gg]" "Вы не можете не ответить…"
        "Сьюзен" "Д..Да, милый. Я дома."
        "Сьюзен" "В данный момент у меня ещё длится сеанс с клиентом, и я бы попросила не тревожить нас какое-то время."
    
    scene image "cg/ep9/psi/2/bg.png"
    show ep9_christie_root_55_anim_1 0
    show christie_root_55_m 1
    show image "cg/ep9/psi/2/wall.png"

    if preferences.language in (None, 'eng', 'rus'):

        show image comic_frame_v2_master:
            zoom .7
            xpos 1300
            ypos 25
            xanchor 0.0
            yanchor 0.0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .7
            xpos 1300
            ypos 25
            xanchor 0.0
            yanchor 0.0
            alpha .0
        
        with my_dissolve

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Разве ты не"),
            __("планировала"),
            __("сегодня"),
            __("отдыхать?")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  50,
            plus_y = 15,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_15   
        show ep9_christie_root_55_anim_1 1
        with my_dissolve
        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Ну... Это"),
            __("особый случай.")

            ), 
            size   =  60,
            plus_y = 10,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 250],   

         show_label = "christie_root_55_psi_talk_1",      
        ) from _call_comic_frame_v2_label_16   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("П-прекратите!…"),

            ), 
            size =  60,
            plus_y = 42,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", xzoom = -1),
            say_pos = ["l", 30], 
        ) from _call_comic_frame_v2_label_17
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Мы не можем этого"),
            __("делать сейчас."),
            __("Да и вообще когда-либо.")

            ), 
            size =  45,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1),
            say_pos = ["l", 30], 
        ) from _call_comic_frame_v2_label_18   
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Вы там что, на"),
            __("повышенных"),
            __("тонах"),
            __("общаетесь?")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  45,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 130],  
            show_label = "christie_root_55_officer_talk_3" 
        ) from _call_comic_frame_v2_label_19   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Милая, у тебя"),
            __("там всё"),
            __("в порядке?")
            
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 120],  
            show_label = "christie_root_55_officer_talk_3" 
        ) from _call_comic_frame_v2_label_20   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __(" Да, дорогой… "),

            ), 
            size   =  55,
            plus_y = 50,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 250],   

         show_label = "christie_root_55_psi_talk_1",      
        ) from _call_comic_frame_v2_label_21   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
        
        __("Это такая необходимая"),
        __("терапия для разгрузки"),
        __("нервной системы."),

            ), 
            size   =  35,
            plus_y = 30,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

         show_label = "christie_root_55_psi_talk_1",      
        ) from _call_comic_frame_v2_label_22   




        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Ааа…"),
            __("Ну раз так.")
            
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  60,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 80],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_23   
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Тогда"),
            __("оставляю"),
            __("вас наедине."),
            

            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 80],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_24   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
        
        __("Дааа…"),
        __("Оставь нас.")

            ), 
            size   =  55,
            plus_y = 30,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

         show_label = "christie_root_55_psi_talk_1",      
        ) from _call_comic_frame_v2_label_25   



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
        
        __("Позволь мне провести со"),
        __("своим клиентом весь спектр"),
        __("физических задач.")

            ), 
            size   = 40,
            plus_y = 30,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

         show_label = "christie_root_55_psi_talk_1",      
        ) from _call_comic_frame_v2_label_26   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Физических?!"),
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  50,
            plus_y = 50,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 20],  
            show_label = "christie_root_55_officer_talk_3" 
        ) from _call_comic_frame_v2_label_27   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
        
        __("Тебе послышалось,"),
        __("милый. Речь идёт о"),
        __("психологических задачах.")
        

            ), 
            size   = 40,
            plus_y = 30,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

         show_label = "christie_root_55_psi_talk_1",      
        ) from _call_comic_frame_v2_label_28   


        show image 'cg/christie_root/restroom/shadow.png':
            xzoom -1.05
            alpha .0
            easein 1.0 alpha .9

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Пожалуйста, он же"),
            __("раскусит вас сейчас.")

            ), 
            size =  50,
            plus_y = 5,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
         show_label = "christie_root_55_psi_talk_1",        
        ) from _call_comic_frame_v2_label_29   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Прекратите"),
            __("это немедленно.")

            ), 
            size =  50,
            plus_y = 5,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],

            
        ) from _call_comic_frame_v2_label_30   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
        
        __("Чем быстрее ты получишь"),
        __("свою порцию наслаждения,"),
        __("тем скорее это прекратится.")
        

            ), 
            size   = 42,
            plus_y = 30,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   


         
        ) from _call_comic_frame_v2_label_31   
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Вы хотите, чтобы я"),
            __("поскорее кончил?")

            ), 
            size =  50,
            plus_y = 5,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
           
        ) from _call_comic_frame_v2_label_32   
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
        
            __("И желательно на меня,"),
            "[gg]."
            ), 
            size   = 50,
            plus_y = 30,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   


         
        ) from _call_comic_frame_v2_label_33   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Я хочу не только видеть,"),
            __("но и чувствовать"),
            __("торжество твоего тела.")


            ), 
            size   = 45,
            plus_y = 30,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   


         
        ) from _call_comic_frame_v2_label_34   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Тогда прекратите"),
            __("общаться с мужем…")
            #"поскорее кончил?"

            ), 
            size =  50,
            plus_y = 5,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_shake"
           
        ) from _call_comic_frame_v2_label_35   
        

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Опасность не особо"),
            __("заводит меня."),
            
            #"поскорее кончил?"

            ), 
            size =  50,
            plus_y = 5,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],

            show_label = "christie_root_55_psi_talk_shake"

           
        ) from _call_comic_frame_v2_label_36   
        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Хи-хи-хи."),

            ), 
            size   = 55,
            plus_y = 50,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

            show_label = "christie_root_55_psi_talk_shake"


         
        ) from _call_comic_frame_v2_label_37   


        show image comic_frame_v2_master:    
            easein .2 ypos 300 alpha 0.0
        $ renpy.pause(.1, hard = True)
    else:
        show Psi Invis
        show Psi Invis:
            xalign .92
        show GG Invis
        show GG Invis:
            xalign .6
        show Officer Invis
        show Officer Invis:
            xalign .12
        
        with my_dissolve
        "Офицер" "Разве ты не планировала сегодня отдыхать?"
        "Сьюзен" "Ну… Это особый случай. "
        "[gg]" "П-прекратите!…"
        "[gg]" "Мы не можем этого делать сейчас."
        "[gg]" "Да и вообще когда-либо."
        "Офицер" "Вы там что, на повышенных тонах общаетесь? "
        "Офицер" "Милая, у тебя там всё в порядке?"
        "Сьюзен" "Да, дорогой… "
        "Сьюзен" "Это такая необходимая терапия для разгрузки нервной системы."
        "Офицер" "Ааа… Ну раз так."
        "Офицер" "Тогда оставляю вас наединет."
        "Сьюзен" "Дааа… Оставь нас. Позволь мне провести со своим клиентом весь спектр физических задач."
        "Офицер" "Физических?!"
        "Сьюзен" "Тебе послышалось, милый. Речь идёт о психологических задача."

        show image 'cg/christie_root/restroom/shadow.png':
            xzoom -1.05
            alpha .0
            easein 1.0 alpha .9

        "[gg]" "Пожалуйста, он же раскусит вас сейчас. "
        "[gg]" "Прекратите это немедленно. "
        "Сьюзен" "Чем быстрее ты получишь свою порцию наслаждения, тем скорее это прекратиться."
        "[gg]" "Вы хотите чтобы я поскорее кончил?"
        "Сьюзен" "И желательно на меня, [gg]. "
        "Сьюзен" "Я хочу не только видеть, но и чувствовать торжество твоего тела."
        "[gg]" "Тогда прекратите общаться с мужем… Опасность не особо заводит меня."
        "Сьюзен" "Хи-хи-хи."


    menu christie_root_56_speed_up_1:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_root_56_speed_up_1
    #hide image 'cg/christie_root/restroom/shadow.png'

    show ep9_christie_root_55_anim_1 2
    with my_dissolve
    if preferences.language in (None, 'eng', 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Эй, дорогой!!!"),

            ), 
            size   = 55,
            plus_y = 50,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

            show_label = "christie_root_55_psi_talk_shake"

        ) from _call_comic_frame_v2_label_38   



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Да вы издеваетесь…"),

            ), 
            size   = 55,
            plus_y = 50,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
        ) from _call_comic_frame_v2_label_39   

        hide image 'cg/christie_root/restroom/shadow.png'

        with my_dissolve

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Да, милая?"),
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  60,
            plus_y = 42,
            line_spasing = -2, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_40   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Ты ещё не ушёл?"),

            ), 
            size   = 55,
            plus_y = 50,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

            show_label = "christie_root_55_psi_talk_1"

        ) from _call_comic_frame_v2_label_41   
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Нет… Но"),
            __("собирался."),
            # "Ты же сама"),
            # "просила меня"),
            # "не мешать вам")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  60,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 80],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_42   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            

            __("Ты же сама"),
            __("просила меня"),
            __("не мешать вам.")


            ), 
            size =  43,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 80],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_43   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Оу, как ты пунктуален."),
            __("Настоящий джентльмен.")

            ), 
            size   = 48,
            plus_y = 14,
            line_spasing = 9, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

            show_label = "christie_root_55_psi_talk_1"

        ) from _call_comic_frame_v2_label_44   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Быть может, ты"),
            __("тогда купишь нам"),
            __("еды на ужин?")


            ), 
            size   = 48,
            plus_y = 10,
            line_spasing = 7, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

            show_label = "christie_root_55_psi_talk_1"

        ) from _call_comic_frame_v2_label_45   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Хорошо."),
            

            # "Ты же сама"),
            # "просила меня"),
            # "не мешать вам")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  80,
            plus_y = 30,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 20],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_46   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #"Хорошо."),
            __("А разве у"),
            _generate_text(__("нас ничего"), size = 42), 
            _generate_text(__("не осталось"), size = 42),
            _generate_text(__("со вчерашнего"), size = 42),
            __("дня?")
            
            # "Ты же сама"),
            # "просила меня"),
            # "не мешать вам")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  45,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 180],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_47   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Я хочу что-то азиатское."),
            __("Возможно, суши,"),
            __("или онигири…")



            ), 
            size   = 48,
            plus_y = 14,
            line_spasing = 7, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

            show_label = "christie_root_55_psi_talk_1"

        ) from _call_comic_frame_v2_label_48   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Да, как"),
            __("скажешь.")
            

            # "Ты же сама"),
            # "просила меня"),
            # "не мешать вам")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  80,
            plus_y = 30,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 80],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_49   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #"Хорошо."),
            __("Но… Твой"),
            __("голос. Он"),
            __("какой-то"),
            __("уставший…")
            # "Ты случаем"),
            # "не заболела?"


            ), 
            size =  55,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 180],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_50   




        call comic_frame_v2_label((
            
            

            __("Ты случаем"),
            __("не заболела?")


            ), 
            size =  52,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 50],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_51   



        # "Офицер" 
        # "Сьюзен" 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Нет, что ты!"),
            __("Я чувствую себя"),
            _generate_text(__("потрясающе."), size = 50)

            ), 
            size   = 40,
            plus_y = 15,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

            show_label = "christie_root_55_psi_talk_shake"


         
        ) from _call_comic_frame_v2_label_52   



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #"Хорошо."),
            _generate_text(__("Извини, но"), size = 50),
            
            __("твой голос"),
            __("мне говорит"),
            __("куда больше,"),
            _generate_text(__("чем твои слова."), size = 36)

            # "Ты случаем"),
            # "не заболела?"


            ), 
            size =  48,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 180],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_53   


        call comic_frame_v2_label((
            __("Позволь мне"),
            __("зайти и"),
            __("самому"),
            __("убедиться.")

            ), 
            size =  52,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 180],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_54   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Я против."),

            ), 
            size   = 55,
            plus_y = 50,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

            show_label = "christie_root_55_psi_talk_shake"


         
        ) from _call_comic_frame_v2_label_55   

        call comic_frame_v2_label((
            __("Ты странно"),
            _generate_text(__("звучишь, Сьюзен…"), size = 36),
            __("Будто бы… ")

            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 90],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_56   




        call comic_frame_v2_label((
            __("В общем,"),
            __("позволь мне"),
            __("войти на"),
            __("минутку.")


            ), 
            size =  48,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 100],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_57   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("О боже,"),
            __("нам пиздец..."),
            
            #"поскорее кончил?"

            ), 
            size =  50,
            plus_y = 5,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],

            show_label = "christie_root_55_psi_talk_shake"

           
        ) from _call_comic_frame_v2_label_58   
        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Вы спровоцировали"),
            __("его!..")
            #"поскорее кончил?"

            ), 
            size =  50,
            plus_y = 5,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],

            show_label = "christie_root_55_psi_talk_shake"

           
        ) from _call_comic_frame_v2_label_59   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Извини, любимый, но"),
            __("в данный момент я"),
            __("делаю пациенту массаж..."),
            # "и будет не тактично"),
            # "впускать тебя в кабинет."



            ), 
            size   = 48,
            plus_y = 14,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

            show_label = "christie_root_55_psi_talk_1"

        ) from _call_comic_frame_v2_label_60   
        

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("...и будет не тактично"),
            __("впускать тебя в кабинет.")



            ), 
            size   = 48,
            plus_y = 12,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

            show_label = "christie_root_55_psi_talk_1"

        ) from _call_comic_frame_v2_label_61   
        
        call comic_frame_v2_label((
            __("Что?"),
            _generate_text(__("Массаж?!"), size = 70),
            
            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 90],  
            show_label = "christie_root_55_officer_talk_shake" 
        ) from _call_comic_frame_v2_label_62   


        call comic_frame_v2_label((
            __("С каких пор"),
            __("ты стала"),
            
            _generate_text(__("оказывать"), size = 38),
            _generate_text(__("{i}такие{/i}"), size = 92),
            __("услуги?")
            

            ), 
            size =  46,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 140],  
            show_label = "christie_root_55_officer_talk_shake" 
        ) from _call_comic_frame_v2_label_63   




        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Это новая,"),
            __("экспериментальная"),
            __("практика.")



            ), 
            size   = 48,
            plus_y = 12,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

            show_label = "christie_root_55_psi_talk_1"

        ) from _call_comic_frame_v2_label_64   



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Но уверяю тебя…"),
            __("Клиент очень"),
            __("доволен.")



            ), 
            size   = 48,
            plus_y = 12,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

            show_label = "christie_root_55_psi_talk_1"

        ) from _call_comic_frame_v2_label_65   
        

        call comic_frame_v2_label((
            __("Пффф…!!"),
            __("Даже не"),
            __("сомневаюсь!")
            

            ), 
            size =  46,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 140],  
            show_label = "christie_root_55_officer_talk_shake" 
        ) from _call_comic_frame_v2_label_66   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Хочу так же добав…"),
            ), 
            size   = 48,
            plus_y = 50,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = 1.0),
            say_pos = ["d", 100],   

            show_label = "christie_root_55_psi_talk_1"

        ) from _call_comic_frame_v2_label_67   
    else:

        "Сьюзен" "Эй, дорогой!!!"
        "[gg]" "Да вы издеваетесь…"

        hide image 'cg/christie_root/restroom/shadow.png'

        with my_dissolve
        "Офицер" "Да, милая?"
        "Сьюзен" "Ты ещё не ушёл?"
        "Офицер" "Нет… Но собирался. Ты же сама просила меня не мешать вам."
        "Сьюзен" "Оу, как ты пунктуален. Настоящий джентльмен."
        "Сьюзен" "Быть может, ты тогда купишь нам еды на ужин?"
        "Офицер" "Хорошо. А разве у нас ничего не осталось со вчерашнего дня?"
        "Сьюзен" "Я хочу что-то азиатское. Возможно, суши, или онигири…"
        "Офицер" "Да, как скажешь."
        "Офицер" "Но… Твой голос. Он какой-то уставший… Ты случаем не заболела?"
        "Сьюзен" "Нет, что ты! Я чувствую себя потрясающе."
        "Офицер" "Извини, но твой голос мне говорит куда больше, чем твои слова. "
        "Офицер" "Позволь мне зайти и самому убедиться."
        "Сьюзен" "Я против."
        "Офицер" "Ты странно ты звучишь, Сюзен… Будто бы… "
        "Офицер" "В общем, позволь мне войти на минутку."
        "[gg]" "О боже, нам пиздец…."
        "[gg]" "Вы спровоцировали его!.."
        "Сьюзен" "Извини, любимый, но в данный момент я делаю пациенту массаж и будет не тактично впускать тебя в кабинет."
        "Офицер" "Что? Массаж?!"
        "Офицер" "С каких пор ты стала оказывать такие услуги?"
        "Сьюзен" "Это новая, экспериментальная практика. "
        "Сьюзен" "Но уверяю тебя… Клиент очень доволен."
        "Офицер" "Пффф…!!"
        "Офицер" "Даже не сомневаюсь!"
        "Сьюзен" "Хочу так же добав…."
    show image 'cg/christie_root/restroom/shadow.png':
        xzoom -1.05
        alpha .0
        easein .3 alpha .9


    hide image 'cg/christie_root/restroom/shadow.png'
    hide image "cg/ep9/psi/2/wall.png"
    hide ep9_christie_root_55_anim_1
    show ep9_christie_root_55_anim_2 3
    show image "cg/ep9/psi/2/wall.png"
    show image 'cg/christie_root/restroom/shadow.png':
        xzoom -1.05
        alpha .9
    with my_vpunch


    if preferences.language in (None, 'eng', 'rus'):

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Извините, но я вынужден"),
            __("заткнуть вас хотя бы"),
            __("на время!")
            #"поскорее кончил?"

            ), 
            size =  43,
            plus_y = 20,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_shake_2"
           
        ) from _call_comic_frame_v2_label_68   
        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Ваш муж уже во всю"),
            __("подозревает неладное..."),
            
            
            #"поскорее кончил?"

            ), 
            size =  43,
            plus_y = 2,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_shake_2"
           
        ) from _call_comic_frame_v2_label_69   
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("...а я, знаете ли,"),
            __("ещё планирую пожить.")
            #"поскорее кончил?"

            ), 
            size =  43,
            plus_y = 2,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_shake_2"
           
        ) from _call_comic_frame_v2_label_70   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("    К тому же…    "),
            #"поскорее кончил?"

            ), 
            size =  70,
            plus_y = 30,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_2"
           
        ) from _call_comic_frame_v2_label_71   


        call comic_frame_v2_label((
            
            __("Так у"),
            __("вас благодарить"),
            __("получается"),
            __("значительно"),
            _generate_text(__("{i}лучше.{/i}"), size = 110),

            ), 
            size =  67,
            plus_y = 30,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_2"
           
        ) from _call_comic_frame_v2_label_72   


        call comic_frame_v2_label((
            __("Надеюсь, вы не против"),
            __("небольшого экспромта"),
            __("с моей стороны.")


            ), 
            size =  45,
            plus_y = 30,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_2"
           
        ) from _call_comic_frame_v2_label_73   



        call comic_frame_v2_label((
            __("раз уж вы, Сьюзен, сами"),
            __("предложили столь щедро"),
            __("отблагодарить меня.")

            ), 
            size =  40,
            plus_y = 30,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_2"
           
        ) from _call_comic_frame_v2_label_74   



        call comic_frame_v2_label((
            __("{i}*Хлюп-хлюп-хлюп*{/i}"),

            ), 
            size =  50,
            plus_y = 50,
            line_spasing = 5, 
            say_image =  Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 30],
            show_label = "christie_root_55_psi_talk_3"
           
        ) from _call_comic_frame_v2_label_75   
        hide image 'cg/christie_root/restroom/shadow.png' 
        with my_dissolve
        call comic_frame_v2_label((
        
            _generate_text(__("Эй, "), size = 60),
            __("у вас в"),
            __("порядке?")
            # "Я слышу какие-то"),
            # _generate_text("почмокивания!", size = 45)
            

            ), 
            size =  70,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 140],  
            show_label = "christie_root_55_officer_talk_shake" 
        ) from _call_comic_frame_v2_label_76   

        call comic_frame_v2_label((
        
            

            _generate_text(__("Я слышу"), size = 50),
            __("какие-то..."),
            __("{i}почмокивания!{/i}")

            ), 
            size =  45,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 140],  
            show_label = "christie_root_55_officer_talk_shake" 
        ) from _call_comic_frame_v2_label_77   


        call comic_frame_v2_label((
            __("Ваша жена"),
            __("выдавливает"),
            __("масло, офицер…"),
            

            ), 
            size =  65,
            plus_y = 5,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_2"
           
        ) from _call_comic_frame_v2_label_184

        call comic_frame_v2_label((
        
            

            __("Чего?"),
            __("Это ты,"),
            "[gg]?!!"
            ), 
            size =  70,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 140],  
            show_label = "christie_root_55_officer_talk_shake" 
        ) from _call_comic_frame_v2_label_78   


        call comic_frame_v2_label((
            __("Да, я…"),
            __("Вы же знаете,"),
            __("я клиент вашей жены.")
            

            ), 
            size =  50,
            plus_y = 5,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_2"
           
        ) from _call_comic_frame_v2_label_185

        #""[gg]" ""

        call comic_frame_v2_label((
        
            

            __("Хм…"),
            __("Правильно ли"),
            __("я понимаю...")
            # "моя жена намазала тебя маслом"),
            # "И делает тебе массаж?")
            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 140],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_79   


        call comic_frame_v2_label((
        
            

            

            __("моя жена"),
            __("намазала"),
            __("тебя маслом"),
            __("и делает тебе..."),
            
            ), 
            size =  40,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 140],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_80   

        call comic_frame_v2_label((
        
            

            
            __("{i}массаж?!{/i}"),
            ), 
            size =  70,
            plus_y = 30,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
            show_label = "christie_root_55_officer_talk_shake" 
        ) from _call_comic_frame_v2_label_81   





        call comic_frame_v2_label((
            _generate_text("", size = 35),
            __("Выходит, что так!..."),


            ), 
            size =  50,
            plus_y = 30,
            line_spasing = -30, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_2"
           
        ) from _call_comic_frame_v2_label_186
        call comic_frame_v2_label((
        
            

            

            __("Скажу честно,"),
            "[gg],",
            __("мне это совсем"),
            __("не нравится.")
            #, и я буду настаивать, чтобы это было в первый и в последний раз!!")
            #"намазала"),
            #"тебя маслом"),
            #"и делает тебе..."),
            
            ), 
            size =  40,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 140],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_82   

        call comic_frame_v2_label((
        
            

            

            __("и я буду"),
            __("настаивать..."),
            # "чтобы это"),
            # "было в"),
            # "первый и в"),
            # "последний раз!!!")
            #"намазала"),
            #"тебя маслом"),
            #"и делает тебе..."),
            
            ), 
            size =  40,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
            show_label = "christie_root_55_officer_talk_2" 
        ) from _call_comic_frame_v2_label_83   


        call comic_frame_v2_label((
        
            

            

           
            __("чтобы это"),
            __("было в"),
            __("первый и в"),
            __("последний раз!!!")


            ), 
            size =  40,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 130],  
            show_label = "christie_root_55_officer_talk_shake" 
        ) from _call_comic_frame_v2_label_84   

        #"Офицер" "


        show image comic_frame_v2_master:    
            easein .2 ypos 300 alpha 0.0
        $ renpy.pause(.1, hard = True)
    else:

        show GG Invis
        show GG Invis:
            xalign .575
        with my_dissolve
        "[gg]" "Извините, но я вынужден заткнуть вас хотя бы на время!"
        "[gg]" "Ваш муж уже во всю подозревает неладное, а я, знаете ли, ещё планирую пожить."
        "[gg]" "К тому же… Так у вас благодарить получается значительно лучше."
        "[gg]" "Надеюсь, вы не против небольшого экспромта с моей стороны, раз уж вы, Сьюзен, сами предложили столь щедро отблагодарить меня."
        "Сьюзен" "Хлюп-хлюп-хлюп!"
        hide image 'cg/christie_root/restroom/shadow.png' 
        with my_dissolve
        "Офицер" "Эй, у вас в порядке? Я слышу какие-то почмокивания!"
        "[gg]" "Ваша жена выдавливает масло, офицер…"
        "Офицер" "Чего? Это ты, [gg]?!!"
        "[gg]" "Да, я… Вы же знаете, я клиент вашей жены."
        "Офицер" "Хм……"
        "Офицер" "Правильно ли я понимаю, моя жена намазала тебя маслом и делает тебе массаж?"
        "[gg]" "Выходит что так!..."
        "Офицер" "Скажу честно, [gg], мне это совсем не нравится, и я буду настаивать, чтобы это было в первый и в последний раз!!"


    menu:
        "Кончить":
            pass
    show ep9_christie_root_55_anim_2 3
    #"ext" "//Кончить "
    #"ext" "//Скорость х4"

    if preferences.language in (None, 'eng', 'rus'):
        call comic_frame_v2_label((
            __("Я с вами полностью"),
            __("согласен, офицер!"),
            

            ), 
            size =  50,
            plus_y = 5,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_2"
           
        ) from _call_comic_frame_v2_label_85   


        call comic_frame_v2_label((
            __("Это…"),
            

            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_4"
           
        ) from _call_comic_frame_v2_label_86   


        call comic_frame_v2_label((
            __("Это…"),
            __("Долго…"),
            

            ), 
            size =  50,
            plus_y = 5,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_4"
           
        ) from _call_comic_frame_v2_label_87   


        call comic_frame_v2_label((
            __("Это…"),
            __("Долго…"),

            __("Терпеть…"),
            

            ), 
            size =  50,
            plus_y = 5,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_4"
           
        ) from _call_comic_frame_v2_label_88   

        # "[gg]" 
        # "[gg]" 
        # "[gg]" "Долго…"
        # "[gg]" "Терпеть…"


        $ christie_root_55_cum_1 = Composite((1050, 180), (0, 0), Solid("#000"))
        #$ renpy.pause(.1, hard = True)
        # show image christie_root_52_cum_1:
        #     ypos  800
        #     xpos  100
        #     yanchor .5
        #     alpha 1.0

        $ christie_root_55_cum_2 = Composite((1020, 180), 
            #(0, 0), Solid("#000"),
            (0, 0), Frame(Transform('interface/comic_v2/bg_frame_2.png', alpha = .8), Borders(64, 64, 64, 64)),
            (20, 50), Text(
                            __("Невозможноооооооооо!!!"), 
                            kerning  = 5,
                            size     = 50,
                            outlines = [(2, "#000a", 0, 0),],
                            font = "fonts/mango_comics_er.ttf",
                            
                            ),
            (1020, 60), Transform("comic_frame_say_3")
            )

        show image AlphaMask(christie_root_55_cum_2, At(christie_root_55_cum_1, christie_root_52_cum_transform)): #comic_frame_v2_0:
            
            zoom .7
            ypos  70
            xpos  1400
            yanchor .5
            alpha 1.0
        hide image comic_frame_v2_master
        hide image comic_frame_v2_slave
        #show image christie_root_52_cum_2
        #show
        with my_dissolve
        $ renpy.pause(.9)
        #show ep9_strip_gg 7
        $ renpy.pause(.1)
        
        
        show image '#fff'
        with Dissolve(.3)
        $ renpy.pause(.7, hard = True)

        #"[gg]" "Невозможноооооооооо!!!"
        #"ext" "Psi_Minet_END"

        #show image '#fff'
        #with Dissolve(.3)
        #$ renpy.pause(.7, hard = True)
        scene image "cg/ep9/psi/2/bg.png"
        
        show ep9_christie_root_55_anim_2 5
        show christie_root_55_m 2
        show image "cg/ep9/psi/2/wall.png"
        show image comic_frame_v2_master
        show image comic_frame_v2_slave



        show image comic_frame_v2_master:
            zoom .7
            xpos 900
            ypos 250
            xanchor 1.0
            yanchor .5
            alpha .0

        show image comic_frame_v2_slave:
            zoom .7
            xpos 900
            ypos 250
            xanchor 1.0
            yanchor .5
            alpha .0
        
        with my_vpunch
        call comic_frame_v2_label((
        
            

            

           
            __("Эээ!"),


            ), 
            size =  140,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
            show_label = "christie_root_55_officer_talk_shake_1_5" 
        ) from _call_comic_frame_v2_label_89   

        show ep9_christie_root_55_anim_2 6
        with my_dissolve
        call comic_frame_v2_label((
        
            



            __("Почему вы"),
            __("умолкли? Что"),

            __("Произошло?..")
            
            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
            show_label = "christie_root_55_officer_talk_shake_2" 
        ) from _call_comic_frame_v2_label_90   

        call comic_frame_v2_label((
            __("    Уфффффффф…      "),

            ), 
            size =  60,
            plus_y = 40,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_5"
           
        ) from _call_comic_frame_v2_label_91   



        #"Сьюзен" 
            
        call comic_frame_v2_label((
            
            __("Мммм,"),
            __("белковое наслаждение"),
            __("от юной кровушки."),
            _generate_text("", size = 35),


            ), 
            size =  50,
            plus_y = 40,
            line_spasing = 5, 
            say_image =  Transform("comic_frame_say_2",),
            say_pos = ["d", 30],
            show_label = "christie_root_55_psi_talk_6"
           
        ) from _call_comic_frame_v2_label_92   
        call comic_frame_v2_label((
            __("Я…"),
            __("Ненавижу вас,"),
            __("Сьюзен.")

            ), 
            size =  60,
            plus_y = 20,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_5"
           
        ) from _call_comic_frame_v2_label_93   

        call comic_frame_v2_label((
            
            __("Ты рано хоронишь"),
            __("нашу дружбу"),
            "[gg].",
            _generate_text("", size = 10),


            ), 
            size =  50,
            plus_y = 40,
            line_spasing = 5, 
            say_image =  Transform("comic_frame_say_2",),
            say_pos = ["d", 30],
            show_label = "christie_root_55_psi_talk_6"
           
        ) from _call_comic_frame_v2_label_94   


        call comic_frame_v2_label((
            
            __("Ещё увидимся."),
            _generate_text("", size = 10),


            ), 
            size =  60,
            plus_y = 40,
            line_spasing = 5, 
            say_image =  Transform("comic_frame_say_2",),
            say_pos = ["d", 100],
            show_label = "christie_root_55_psi_talk_6"
           
        ) from _call_comic_frame_v2_label_95   
        
        #"Сьюзен" 
        #"Сьюзен" 
        
        call comic_frame_v2_label((
            __("Надеюсь, что нет."),

            ), 
            size =  60,
            plus_y = 40,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1.0),
            say_pos = ["l", 30],
            show_label = "christie_root_55_psi_talk_5"
           
        ) from _call_comic_frame_v2_label_96   
        with my_vpunch
        call comic_frame_v2_label((
        
            

            

           
            __("Ну всё!"),


            ), 
            size =  65,
            plus_y = 30,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 40],  
            show_label = "christie_root_55_officer_talk_shake_1_5" 
        ) from _call_comic_frame_v2_label_97   

        call comic_frame_v2_label((
        
            

            

           
            __("или вы"),
            __("открываете,"),
            __("или я сейчас"),
            __("выломаю дверь!"),


            ), 
            size =  40,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_3"),
            say_pos = ["r", 70],  
            show_label = "christie_root_55_officer_talk_shake_2" 
        ) from _call_comic_frame_v2_label_98 
    else:


        "[gg]" "Я с вами полностью согласен, офицер!"
        "[gg]" "Это…. "
        "[gg]" "Долго…"
        "[gg]" "Терпеть…"
        "[gg]" "Невозможноооооооооо!!!"
        scene image "cg/ep9/psi/2/bg.png"
        
        show ep9_christie_root_55_anim_2 5
        show christie_root_55_m 2
        show image "cg/ep9/psi/2/wall.png"
        with my_dissolve
        $ renpy.pause(.5, hard = True)
        "Офицер" "Эээ!"
        show ep9_christie_root_55_anim_2 6
        with my_dissolve
        "Офицер" "Почему вы умолкли? Что произошло?.."
        "[gg]" "Уфффффффф….."
        "Сьюзен" "Мммм, белковое наслаждение от юной кровушки. "
        "[gg]" "Я… Ненавижу вас, Сьюзен."
        "Сьюзен" "Ты рано хоронишь нашу дружбу, [gg]."
        "Сьюзен" "Ещё увидимся."
        "[gg]" "Надеюсь, что нет."
        "Офицер" "Ну всё, или вы открываете, или я сейчас выломаю дверь!"


    scene black with Dissolve(.2)
    $ renpy.pause(.3, hard = True)
    #"ext" "//Psi_Room"
    #"ext" "//Officer_Normal"
    #"ext" "//GG_Surprise рядом со Сьюзен"
label christie_root_55_end:
    
    $ add_to_gallery(38)
    scene expression 'cg/christie_root/psi_corridor.png'
    show Officer Normal
    show Officer Normal:
        xalign .1
        ypos 1080
    with Dissolve(.5)
    show Psi Normal
    show Psi Normal at go_from_right(xxalign = .65)

    show GG Normal
    show GG Normal at go_from_right(xxzoom = -1, xxalign = 1.0)

    "Сьюзан" "Не надо. Мы уже кончили. "
    show Psi Normal:
        xalign .7 xzoom -1
    with my_dissolve
    "Сьюзан" "Верно я говорю, [gg]?"
    show GG Embarrassment:
        xzoom -1 xalign 1.0
        easein 1 ypos 1100
    show shadow_full:
        alpha .0
        easein 1 alpha .7
    #with my_dissolve
    "[gg]" "Да, это был мой последний сеанс."
    show Psi Normal
    "Сьюзан" "Наш сеанс, хи-хи-хи."
    show Officer Normal
    "Офицер" "Что ж, я очень рад, что больше не увижу тебя здесь."
    show GG Normal:
        easein 1 ypos 1085
    with None
    hide shadow_full
    show Psi:
        xzoom 1
    with my_dissolve
    "[gg]" "Хотел бы я так же сказать и про вас, офицер. "
    show Officer Normal
    "Офицер" "Давай, мальчик. Ступай подобру-поздорову. "
    show Officer Normal
    "Офицер" "Пока я не воспользовался правом хозяина дома, и не спустил тебя с лестницы. "
    show Psi Normal
    with my_vpunch
    "Сьюзан" "Ты хамишь, дорогой!"
    show Officer Normal
    "Офицер" "Извини, но…"
    show Psi Normal:
        easein_cubic 2 xalign .5 zoom 1.05
    show Officer Surprise:
        easein_cubic 2 xalign .0  ypos 1110

    show image 'images/cg/ep86/shadow.png':
        alpha .0
        easein_cubic 3 alpha 0.7
    "Сьюзан" "Тогда заткнись, пожалуйста, пока я перебила всю посуду и не сломала твои новые рыбацкие снасти!"
    #show Officer Hm
    #with my_dissolve
    "Офицер" "….."
    hide image 'images/cg/ep86/shadow.png'
    show Officer Hm:
        xalign .0  ypos 1110
    show Psi Normal:
        xzoom -1 zoom 1.0
    with my_dissolve
    "Сьюзан" "До встречи, [gg]."
    "[gg]" "Прощайте, Сьюзен."
    $ add_ach('ACH_11')
    show GG:
        easein_cubic 3 xalign -1.5
    $ renpy.pause(1, hard = True)

    scene black with Dissolve(.5)

    $ debug_exit()
    
    $ sister_position['morning']  = ['Hall',  'sister_hall']

    $ sister_position['evening']  = ['Sister_Room',  'sister_room']


    $ Event('christie_root_56', 'Christie', button_name = "Сьюзан")
    
    $ descript_Christie = __("Вернуться к Кристи.")
    
    $ location_now = "City_Home"

    jump main_interface_label