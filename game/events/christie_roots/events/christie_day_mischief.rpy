label christie_day_mischief_lvl_2_christie_talk:
    show image comic_frame_v2_master:
        zoom .7
        xpos 1000
        ypos 320
        xanchor .5
        yanchor 1.0
        alpha .0

        parallel:
            easein 0.2 ypos 360
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.21, hard = True)
    return 


label christie_night_mischief_lvl_2_christie_talk_shake_hide:
    $ j = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
    $ i = list(j.get_placement()) + [j.xzoom, j.yzoom, j.zoom, j.alpha, j.xanchor, j.yanchor]
    
    $ store.comic_frame_v2_slave  = store.comic_frame_v2_master

    show image comic_frame_v2_master:
        alpha 0.0
        xpos i[0]
        ypos i[1]
        xanchor i[2]
        yanchor i[3]
        xoffset i[4]
        yoffset i[5]
        subpixel i[6]
        xzoom i[7]
        yzoom i[8]
        zoom  i[9]
        xanchor i[11]
        yanchor i[12]
    show image comic_frame_v2_slave:
        xpos i[0]
        ypos i[1]
        xanchor i[2]
        yanchor i[3]
        xoffset i[4]
        yoffset i[5]
        subpixel i[6]
        xzoom i[7]
        yzoom i[8]
        zoom  i[9]
        alpha i[10]
        xanchor i[11]
        yanchor i[12]
        alpha 0.0
    #$ renpy.pause(.21, hard = True)
    return 
label christie_day_mischief_lvl_2_christie_talk_shake:
    show image comic_frame_v2_master:
        zoom .7
        xpos 1000
        ypos 350
        xanchor .5
        yanchor 1.0
        alpha .0

        parallel:
            ease .05 alpha 1.0
        parallel:
            ease .05 ypos 360
            ease .05 ypos 367
            ease .05 ypos 360
            ease .05 ypos 367
            ease .05 ypos 360
    $ renpy.pause(.27, hard = True)
    return 

label christie_day_mischief_lvl_2_gg_talk:
    show image comic_frame_v2_master:
        zoom .7
        xpos 540
        ypos 450
        xanchor 1.0
        yanchor 1.0
        alpha .0

        parallel:
            easein 0.2 ypos 500
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.21, hard = True)
    return 



label christie_day_mischief_lvl_2_gg_talk_2:
    show image comic_frame_v2_master:
        zoom .7
        xpos 540
        ypos 400
        xanchor 1.0
        yanchor 1.0
        alpha .0

        parallel:
            easein 0.2 ypos 450
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.21, hard = True)
    return 


image christie_day_mischief_lvl_2_squirt_1_s = Composite((1920, 1080),
    (-300, -150), Transform('cg/ep85/gg_milf_sex/1s.png', xzoom = -1.0),
    (-300, 150), Transform('cg/ep85/gg_milf_sex/1s.png', xzoom = -1.0, yzoom = -1.0),

    )

image christie_day_mischief_lvl_2_squirt_2_s = Composite((1920, 1080),
    (-300, -150), Transform('cg/ep85/gg_milf_sex/2s.png', xzoom = -1.0),
    (-300, 150), Transform('cg/ep85/gg_milf_sex/2s.png', xzoom = -1.0, yzoom = -1.0),

    )

image christie_day_mischief_lvl_2_squirt_3_s = Composite((1920, 1080),
    (-300, -150), Transform('cg/ep85/gg_milf_sex/3s.png', xzoom = -1.0),
    (-300, 150), Transform('cg/ep85/gg_milf_sex/3s.png', xzoom = -1.0, yzoom = -1.0),

    )

image christie_day_mischief_lvl_2_squirt_4_s = Composite((1920, 1080),
    (-300, -150), Transform('cg/ep85/gg_milf_sex/3s.png', xzoom = -1.0),
    (-300, 150), Transform('cg/ep85/gg_milf_sex/4s.png', xzoom = -1.0, yzoom = -1.0),
    )

image christie_day_mischief_lvl_2_squirt:
    #'#0000'
    #.17
    #.17
    'christie_day_mischief_lvl_2_squirt_1_s' with Dissolve(.1)
    .16
    'christie_day_mischief_lvl_2_squirt_2_s'
    .17
    'christie_day_mischief_lvl_2_squirt_3_s'
    .17
    'christie_day_mischief_lvl_2_squirt_4_s'
    .16
    '#0000' with Dissolve(.1)
    .17
    .17
    
    repeat


image christie_day_mischief_lvl_2_bg = 'cg/ep95/christie_day_mischief/bg.png'

image christie_day_mischief_lvl_2_water_drop = 'cg/ep95/christie_day_mischief/water_drop.png'

image christie_day_mischief_lvl_2 0 = 'cg/ep95/christie_day_mischief/1.png'


image christie_day_mischief_lvl_2 1_1:
    #'cg/ep95/christie_day_mischief/1.png'
    #.17
    'cg/ep95/christie_day_mischief/2.png'
    .17
    'cg/ep95/christie_day_mischief/3.png'
    .17
    'cg/ep95/christie_day_mischief/4.png'
    .17
    'cg/ep95/christie_day_mischief/5.png'
    .17
    'cg/ep95/christie_day_mischief/4.png'
    .17
    'cg/ep95/christie_day_mischief/3.png'
    .17
    #'cg/ep95/christie_day_mischief/2.png'
    #1.0
    repeat


image christie_day_mischief_lvl_2 2_1:
    #'cg/ep95/christie_day_mischief/1.png'
    #.08
    'cg/ep95/christie_day_mischief/6.png'
    .17
    'cg/ep95/christie_day_mischief/7.png'
    .17
    'cg/ep95/christie_day_mischief/8.png'
    .17
    'cg/ep95/christie_day_mischief/7.png'
    .17
    #'cg/ep95/christie_day_mischief/4.png'
    #.08
    #'cg/ep95/christie_day_mischief/3.png'
    #.08
    #'cg/ep95/christie_day_mischief/2.png'
    #.08
    repeat


image christie_day_mischief_lvl_2 1_2:
    #'cg/ep95/christie_day_mischief/1.png'
    #.12
    'cg/ep95/christie_day_mischief/2.png'
    .12
    'cg/ep95/christie_day_mischief/3.png'
    .12
    'cg/ep95/christie_day_mischief/4.png'
    .12
    'cg/ep95/christie_day_mischief/5.png'
    .12
    'cg/ep95/christie_day_mischief/4.png'
    .12
    'cg/ep95/christie_day_mischief/3.png'
    .12
    #'cg/ep95/christie_day_mischief/2.png'
    #.12
    repeat
image christie_day_mischief_lvl_2 2_2:

    'cg/ep95/christie_day_mischief/6.png'
    .12
    'cg/ep95/christie_day_mischief/7.png'
    .12
    'cg/ep95/christie_day_mischief/8.png'
    .12
    'cg/ep95/christie_day_mischief/7.png'
    .12

    repeat

image christie_day_mischief_lvl_2 1_3:
    'cg/ep95/christie_day_mischief/2.png'
    .08
    'cg/ep95/christie_day_mischief/3.png'
    .08
    'cg/ep95/christie_day_mischief/4.png'
    .08
    'cg/ep95/christie_day_mischief/5.png'
    .08
    'cg/ep95/christie_day_mischief/4.png'
    .08
    'cg/ep95/christie_day_mischief/3.png'
    .08
    repeat


image christie_day_mischief_lvl_2 2_3:
    #'cg/ep95/christie_day_mischief/1.png'
    #.08
    'cg/ep95/christie_day_mischief/6.png'
    .08
    'cg/ep95/christie_day_mischief/7.png'
    .08
    'cg/ep95/christie_day_mischief/8.png'
    .08
    'cg/ep95/christie_day_mischief/7.png'
    .08
    #'cg/ep95/christie_day_mischief/4.png'
    #.08
    #'cg/ep95/christie_day_mischief/3.png'
    #.08
    #'cg/ep95/christie_day_mischief/2.png'
    #.08
    repeat
image christie_day_mischief_lvl_2 4:
    'cg/ep95/christie_day_mischief/6.png'
    .06
    'cg/ep95/christie_day_mischief/7.png'
    .06
    'cg/ep95/christie_day_mischief/8.png'
    .06
    'cg/ep95/christie_day_mischief/7.png'
    .06
    repeat


image christie_day_mischief_lvl_2 end = 'cg/ep95/christie_day_mischief/9.png'
label christie_day_mischief:
    #Дневные шалости
    #Для этого комплекса ивентов будет такой общий диалог, который игрок сам активирует утром, днём, обращаясь к Кристи
    
    call show_bg_image_label from _call_show_bg_image_label_220
    call show_additional_images_label from _call_show_additional_images_label_105

    show Christie Normal
    show Christie Normal:
        xalign .85
        ypos 1085
    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left

    "[gg]" "Скучаю."
    show Christie Smile
    "Кристи" "Оно и заметно, ха-ха!"
    
    "[gg]" "Нет, ты не поняла."
    show GG Passion:
        xalign .15
    with my_dissolve
    "[gg]" "Я по тебе скучаю."
    show Christie Passion
    "Кристи" "Это взаимно, но Маришка дома."
    show GG Passion
    "[gg]" "С каких пор это может нас остановить?"
    show Christie Embarrassment
    "Кристи" "Тогда скажи «пароль»."
    show GG Passion
    "[gg]" "Разве у нас был пароль?"
    show Christie Embarrassment
    "Кристи" "Нет, но ты догадайся."
    #"//Выбор" ""
    if preferences.language in (None, 'eng', 'rus'):
        menu:
            "«Я люблю тебя»":
                $ pass
            "«Пароль»":
                $ pass
            "«Шалость или радость?»":
                $ pass
    else:
        "[gg]" "Хи-хи-хи!"
    #"//Любой Вариант Ответа" ""
    show Christie Smile
    "Кристи" "Правильно."
    show GG Normal
    "[gg]" "Я отгадал или ты просто забавляешься? "
    show Christie Smile
    "Кристи" "Хи-хи-хи!"
    show Christie Smile
    if location_now != 'Sister_Room':
        "Кристи" "Пошли, [gg]."
    #jump main_interface_label
    
    if location_now in ("Hall", 'Corridor', 'Milf_Room'):
        #$ pass
        show GG:
            xzoom -1
            easein 3.0 xalign -1.5

        show Christie:
            
            easein 3.0 xalign -1.5
        $ renpy.pause(1.5, hard = True)
    elif location_now != "Sister_Room":
        
        show GG:
           
            easein 3.0 xalign 1.5

        show Christie:
            xzoom -1
            easein 3.0 xalign 1.5
        $ renpy.pause(1.5, hard = True)
    $ _just_scene = 2

    call christie_root_45_2 from _call_christie_root_45_2

    $ _just_scene = False
    
    hide Christie
    hide GG
    with my_dissolve
    
    
#1й уровень – это минет, который у нас был по сюжету
    $ i = _('Теперь я могу "Шалить" с Кристи хоть каждый день.')
    if getattr(store, 'tyan_mischief_text', False) != i:
        $ tyan_mischief_text  = copy.deepcopy(i) 
        $ new_events_christie = True
    menu:
        "1 уровень":
            $ _just_scene = True
            jump christie_root_45_2

        "2 уровень":
            pass
#2й уровень 
##Kristy_Minet_1
    

    call comic_frame_v2_predict_label(images=comic_frame_v2_predict_list+[
        'christie_day_mischief_lvl_2_bg', 
        'christie_day_mischief_lvl_2 0',
        'christie_day_mischief_lvl_2 1_1',
        'christie_day_mischief_lvl_2 1_2',
        'christie_day_mischief_lvl_2 1_3',
        'christie_day_mischief_lvl_2 2_1',
        'christie_day_mischief_lvl_2 2_2',
        'christie_day_mischief_lvl_2 2_3',
        'christie_day_mischief_lvl_2 4',
        'christie_day_mischief_lvl_2_water_drop'

        ]) from _call_comic_frame_v2_predict_label

    # show GG:
    #     easein .75 xalign .4 alpha .0
    # show Christie:
    #     easein .75 xalign .6 alpha .0
    # $ renpy.pause(1.0, hard = True)
    
    scene black with Dissolve(.3)
    
    $ renpy.pause(.5, hard = True)
    #$ renpy.pause(.8, hard = True)
    scene christie_root_45 1
    show GG Invis
    show GG Invis:
        xalign .3
    show Christie Invis
    show Christie Invis:
        xalign .8
    with my_dissolve
    "Кристи" "Это всегда так волнительно."
    "[gg]" "…."
    "Кристи" "Мы вновь оказываемся наедине, и вновь собираемся заняться чем-то, что может быть предосудительным. "
    "[gg]" "Нам уже нечего опасаться. "
    "Кристи" "Возможно."
    "Кристи" "А возможно, мы слишком самоуверенные, и просто хотим быть свободными."
    "[gg]" "Знаешь, говорят, свобода бывает «от» и «для»."
    "[gg]" "Какая из них наша?"

    "Кристи" "Для любви, конечно же."
    "Кристи" "Извини, если это прозвучит слишком пошло…"
    "Кристи" "Всё это время я думаю только о том, чтобы снова почувствовать твой член у себя во рту. "
    "Кристи" "У него такой приятный ванильный вкус."
    "[gg]" "Хех…"
    "[gg]" "Мне это льстит. Но могу ли я кое о чём попросить тебя?"
    "Кристи" "Ага."
    "[gg]" "Я очень хочу, чтоб удовольствие получал не только я. "
    "Кристи" "И что ты придумал?"
    "[gg]" "Я знаю одну позу, которая поможет нам удовлетворить друг друга."
    show christie_root_45 2


    show Christie Invis:
        xalign .62
    with my_vpunch
    "Кристи" "Кажется, я догадываюсь, о какой позе идёт речь…"
    "[gg]" "Значит, попробуем?"
    "Кристи" "Хорошо. "

    show shadow_full:
        alpha 0.0
        easein 1.0 alpha .8
    "Кристи" "Просто…"
    "[gg]" "Да?"
    "Кристи" "Она такая вульгарная и непривычная. "
    "Кристи" "Я очень стесняюсь, [gg]."

    "[gg]" "Зато наши ласки будут взаимными."

    show shadow_full:
        easein 1.0 alpha 0.0
    "Кристи" "Это справедливо, да."
#Kristy_Minet_Kuni_1
    scene image '#000' with Dissolve(.3)
    $ renpy.pause(.7, hard = True)
    scene christie_day_mischief_lvl_2_bg
    show christie_day_mischief_lvl_2 0

    show shadow_full:
        alpha 0.0
    show image comic_frame_v2_master:
        zoom .7
        xpos 550
        ypos 465
        xanchor 1.0
        yanchor 1.0
        alpha .0

    show image comic_frame_v2_slave:
        zoom .7
        xpos 550
        ypos 465
        xanchor 1.0
        yanchor 1.0
        alpha .0
    with my_dissolve

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
          
            __("У тебя шикарный"),
            __("вид сзади.")

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 320],
           hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",#
           show_label  = "christie_day_mischief_lvl_2_gg_talk"

        ) from _call_comic_frame_v2_label_187 
        call comic_frame_v2_label((
            

            
            __("{size=10} {/size}"),

            __("  Прекрати!  "),

            __("{size=10} {/size}"),


            


            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 200],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk_shake",


        ) from _call_comic_frame_v2_label_188

        call comic_frame_v2_label((
            

            __("{size=10} {/size}"),
            __("Из-за твоих слов"),

            __("я впаду в ступор."),


            
            __("{size=10} {/size}"),


            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 300],
            hide_label = "christie_night_mischief_lvl_2_christie_talk_shake_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk_shake",


        ) from _call_comic_frame_v2_label_189

        


        call comic_frame_v2_label((
            
          
            __("Извини, но ты"),
            __("и вправду"),
            __("классная.")

            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 350],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk"
            
        ) from _call_comic_frame_v2_label_190 
        if preferences.language in (None, 'rus'):
            $ i = 520
        else:
            $ i = 180

        call comic_frame_v2_label((
            
          
            __("Я не могу"),
            __("сдерживаться"),
            __("в комплиментах.")

            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", i],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk"
            
        ) from _call_comic_frame_v2_label_191 

        call comic_frame_v2_label((
            

            __("Хорошо…"),

            __("Спасибо."),


            


            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 200],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_192
        call comic_frame_v2_label((
            

            __("{size=10} {/size}"),

            __("Ты готов?"),

            __("{size=10} {/size}"),



            


            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 200],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_193


        call comic_frame_v2_label((
            
            __("{size=10} {/size}"),

            __("   Ага.   "),

            __("{size=10} {/size}"),

            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 110],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk"
            
        ) from _call_comic_frame_v2_label_194 
    else:


        "[gg]" "У тебя шикарный вид сзади. "

        "Кристи" "Прекрати!"

        "Кристи" "Из-за твоих слов я впаду в ступор."

        "[gg]" "Извини, но ты и вправду классная."

        "[gg]" "Я не могу сдерживаться в комплиментах."

        "Кристи" "Хорошо…"

        "Кристи" "Спасибо."

        "Кристи" "Ты готов? "

        "[gg]" "Ага."




#//#Kristy_Minet_Kuni_2 Animation
#//Скорость х1
    show christie_day_mischief_lvl_2 1_1
    with my_dissolve
    show shadow_full:
        alpha .0
        easein 1 alpha .75

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Боже, её запах{/i}"),
            __("{i}сводит меня{/i}"),
            __("{i}с ума.{/i}")
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -.75, yzoom = .75),
            say_pos = ["d", 320],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
            
        ) from _call_comic_frame_v2_label_195 
       # "[gg]" 

        show shadow_full:
            easein 1 alpha 1.0
        call comic_frame_v2_label((
            


            __("{i}  [gg] так  {/i}"),

            __("{i}резко возбудился!{/i}"),



            


            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9",),
            say_pos = ["d", 300],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_196


        call comic_frame_v2_label((
            

            __("{i}Держать Кристи{/i}"),

            __("{i}за задницу, уткнувшись{/i}"),
            __("{i}лицом в вагину просто{/i}"),
            __("{i}{size=75}улёт!{/size}{/i}")
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 2, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 520],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
            
        ) from _call_comic_frame_v2_label_197 

        call comic_frame_v2_label((
            

            __("{i}Давно следовало{/i}"),
            __("{i}испробовать эту позу{/i}"),
            __("{i}с ней...{/i}")
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 520],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
            
        ) from _call_comic_frame_v2_label_198 

        show image comic_frame_v2_master:    
            easein .2 alpha 0.0
        show shadow_full:
            easein .2 alpha .0

        $ renpy.pause(.21, hard = True)
    else:

        "[gg]" "Боже, её запах сводит меня с ума."

        "Кристи" "[gg] так резко возбудился!"

        "[gg]" "Держать Кристи за задницу, уткнувшись лицом в вагину – просто улёт!"

        "[gg]" "Давно следовало испробовать эту позу с ней. "



    $ christie_day_mischief_pose = 0
    menu:
        "Ускориться":
            $ christie_day_mischief_pose = 1
            show christie_day_mischief_lvl_2 2_1
            with Dissolve(.5)
        "Продолжить в том же темпе":
            $ pass


    if preferences.language in ('eng', None, 'rus'):
        $ renpy.pause(.2, hard = True)
        $ christie_day_mischief_nyam_1 = Composite((370, 180), 
            #(0, 0), Solid("#000"),
            (0, 0), Frame(Transform('interface/comic_v2/bg_frame_2.png', alpha = .8), Borders(64, 64, 64, 64)),
            (20, 50), Text(
                            __("{i}*Ням*{/i}"), 
                            kerning  = 5,
                            size     = 100,
                            outlines = [(2, "#000a", 0, 0),],
                            font = "fonts/mango_comics_er.ttf",
                            
                            ),
            #(1020, 60), Transform("comic_frame_say_3")
            )

        $ christie_day_mischief_nyam_2 = copy.deepcopy(christie_day_mischief_nyam_1)

        $ christie_day_mischief_nyam_3 = copy.deepcopy(christie_day_mischief_nyam_1)

        show image christie_day_mischief_nyam_1:
            zoom .7
            xpos 570
            ypos 460
            xanchor 1.0
            yanchor 1.0
            alpha 1.0

            parallel:
                easein 1.0 ypos 400 alpha .0
                #easeout 0.2 ypos 200

                #easeout .2 alpha 0.0


        #"COMIC_TEST" "COMIC_TEST"
        $ renpy.pause(1.0)
        show image christie_day_mischief_nyam_2:
            zoom .7
            xpos 500
            ypos 480
            xanchor 1.0
            yanchor 1.0
            alpha 1.0

            parallel:
                easein 1.0 ypos 400 alpha .0
                #easeout 0.2 ypos 200

                #easeout .2 alpha 0.0

        $ renpy.pause(1.0)


        show image christie_day_mischief_nyam_3:
            zoom .7
            xpos 550
            ypos 500
            xanchor 1.0
            yanchor 1.0
            alpha 1.0

            parallel:
                easein 1.0 ypos 400 alpha .0
                #easeout 0.2 ypos 200

                #easeout .2 alpha 0.0

        $ renpy.pause(1.0)
        if preferences.language in (None, 'rus'):
            $ i = 520
        else:
            $ i = 230
        call comic_frame_v2_label((
            

            __("{i}Какая же у неё сладкая,{/i}"),
            __("{i}сочная киска.{/i}"),
            


            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", i],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
            
        ) from _call_comic_frame_v2_label_199 

        if preferences.language in (None, 'rus'):
            $ i = 520
        else:
            $ i = 445
        call comic_frame_v2_label((
            

            __("{i}Каждым касанием языка{/i}"),
            __("{i}я чувствую,{/i}"),
            __("{i}как она {size=55}вздрагивает{/size}{/i}"),
            __("{i}от удовольствия...{/i}"),

            
            

            ), 
            size   = 43,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", i],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
            
        ) from _call_comic_frame_v2_label_200 



        call comic_frame_v2_label((
            

            __("{i}А всякий раз, когда{/i}"),
            __("{i}я стараюсь проникнуть{/i}"),
            __("{i}как можно глубже...{/i}"),
            #__("{i}от удовольствия...{/i}"),

            
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 520],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
            
        ) from _call_comic_frame_v2_label_201 




        call comic_frame_v2_label((
            

            __("{i}...Кристи с большей{/i}"),
            __("{i} охотой садится{/i}"),
            __("{i}мне на лицо.{/i}"),
            #__("{i}от удовольствия...{/i}"),

            
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 460],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
            
        ) from _call_comic_frame_v2_label_202 



        call comic_frame_v2_label((
            

            __("{i}Я на седьмом небе{/i}"),


            __("{i}от счастья!{/i}"),

            __("{i}В который раз{/i}"),

            __("{i}в своей жизни!!!{/i}"),

            

            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 460],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
            
        ) from _call_comic_frame_v2_label_203 

        show image comic_frame_v2_master:    
            easein .2 ypos 200 alpha 0.0

        show shadow_full:
            easein .4 alpha .0

        $ renpy.pause(.5, hard = True)
    else:


        "[gg]" "Ням-ням-ням!"

        "[gg]" "Какая же у неё сладкая, сочная киска."

        "[gg]" "Каждое касание языка я чувствую, как она вздрагивает от удовольствие."

        "[gg]" "А всякий раз, когда я стараюсь проникнуть как можно глубже, Кристи с большей охотой садится мне на лицо. "

        "[gg]" "Я на седьмом небе от счастья! В который раз в своей жизни!!!"


    menu christie_day_mischief_speed_up_1:
        "Ускориться":
            if christie_day_mischief_pose:
                $ christie_day_mischief_pose = 0
                show christie_day_mischief_lvl_2 1_2
            else:
                $ christie_day_mischief_pose = 1
                show christie_day_mischief_lvl_2 2_2
            
            with my_dissolve
        "Продолжить в том же темпе":
            $ pass
        #"Ускориться":
        #    $ pass
        #"Продолжить в том же темпе":
        #    window hide
        #    $ renpy.pause(9999)
        #    jump christie_day_mischief_speed_up_1
    #show christie_day_mischief_lvl_2 2
    #with my_dissolve
#//Скорость х2


    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            


            __("{i}[gg] так{/i}"),

            __("{i}усердно вылизывает{/i}"),

            __("{i}мою киску.{/i}"),


            


            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9",),
            say_pos = ["d", 400],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_204


        call comic_frame_v2_label((
            


            __("{i}Судя по всему, он в{/i}"),

            __("{i}{size=40}полнейшем восторге от того,{/size}{/i}"),

            __("{i}что я позволила ему{/i}"),

            __("{i}удовлетворить себя.{/i}"),



            


            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9",),
            say_pos = ["d", 480],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_205

        #show image 'cg/ep95/christie_day_mischief/water_drop.png'
        show christie_day_mischief_lvl_2_water_drop:
            xpos 1130
            ypos 450
           # zoom .05
            alpha .0
            easein .4 ypos 500 alpha 1.0


        show shadow_full:
            easein .4 alpha 1.0

        call comic_frame_v2_label((
            



            __("{size=10} {/size}"),
            __("{i}И хотя я испытываю неловкость...{/i}"),


            __("{size=10} {/size}"),


            


            ), 
            size   = 55,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 600],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_206


        show shadow_full:
            easein .4 alpha .0
        show christie_day_mischief_lvl_2_water_drop:
            
            easein .4 ypos 520 alpha .0


        call comic_frame_v2_label((
            

            __("{size=3} {/size}"),

            __("{i}...в такой позе, мне{/i}"),

            __("{i}это жутко нравится.{/i}"),


            __("{size=3} {/size}"),


            


            ), 
            size   = 55,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 400],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_207



        call comic_frame_v2_label((
            


            __("{size=3} {/size}"),

            __("{i}Но особенно мне{/i}"),

            __("{i}нравится его член.{/i}"),

            __("{size=3} {/size}"),

            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 400],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_208



        call comic_frame_v2_label((
            


            __("{size=3} {/size}"),

            __("{i}Возбуждаясь, он вырастает{/i}"),

            __("{i}прямо у меня во рту.{/i}"),

            __("{size=3} {/size}"),

            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 600],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_209





        call comic_frame_v2_label((
            


            __("{size=3} {/size}"),

            __("{i}Вены становятся более плотными,{/i}"),

            __("{i}сам орган мощно пульсирует...{/i}"),

            __("{size=3} {/size}"),

            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 600],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_210


        if preferences.language in (None, 'rus'):
            $ i = 600
        else:
            $ i = 400


        call comic_frame_v2_label((
            


            __("{size=3} {/size}"),

            __("{i}...а головка фонтанирует{/i}"),

            __("{i}приятными на вкус выделениями.{/i}"),




            __("{size=3} {/size}"),

            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", i],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_211



        if preferences.language in (None, 'rus'):
            $ i = 600
        else:
            $ i = 400

        call comic_frame_v2_label((
            


         #   __("{size=3} {/size}"),

            __("{i}Наши времяпрепровождения{/i}"),

            __("{i}обретают новые{/i}"),

            __("{i}границы разврата…{/i}"),




          #  __("{size=3} {/size}"),

            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", i],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_212



    #//Скорость х3

        show image comic_frame_v2_master:    
            easein .2 ypos 290 alpha 0.0



        $ renpy.pause(.21, hard = True)
    else:


        "Кристи" "[gg] так усердно вылизывает мою киску. "

        "Кристи" "Судя по всему, он в полнейшем восторге от того, что я позволила ему удовлетворить себя. "

        "Кристи" "И хотя я испытываю неловкость в такой позе, мне это жутко нравится… "

        "Кристи" "Но особенно мне нравится его член."

        "Кристи" "Возбуждаясь, он вырастает прям у меня во рту. "

        "Кристи" "Вены становятся более плотными, сам орган мощно пульсирует, а головка фонтанирует приятными на вкус выделениями. "

        "Кристи" "Наше время провождения обретают новые границы разврата…"


    menu christie_day_mischief_speed_up_2:
        "Ускориться":
            if christie_day_mischief_pose:
                $ christie_day_mischief_pose = 0
                show christie_day_mischief_lvl_2 1_3
            else:
                $ christie_day_mischief_pose = 1
                show christie_day_mischief_lvl_2 2_3
            
            with my_dissolve
        "Продолжить в том же темпе":
            $ pass
    #show christie_day_mischief_lvl_2 3
    #with my_dissolve

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            

            __("{i}Наши тела{/i}"),

            __("{i}основательно{/i}"),

            __("{i}покрылись потом.{/i}"),

            

            ), 
            size   = 55,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 510],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
            
        ) from _call_comic_frame_v2_label_213

        call comic_frame_v2_label((
            

            __("{i}Мои руки уже{/i}"),
            __("{i}скользят по{/i}"),
            __("{i}её заднице…{/i}"),

            

            ), 
            size   = 55,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 320],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
        ) from _call_comic_frame_v2_label_214

        call comic_frame_v2_label((
            

            __("{i}Мы оба подошли{/i}"),
            __("{i}к вопросу ласок с{/i}"),
            __("{i}фанатичной{/i}"),
            __("{i}самоотдачей.{/i}"),


            

            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 500],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
        ) from _call_comic_frame_v2_label_215



        if preferences.language in (None, 'rus'):
            $ i = 530
        else:
            $ i = 400

        call comic_frame_v2_label((
            

            __("{i}Делать Кристи{/i}"),
            __("{i}приятно - значит делать{/i}"),
            __("{i}приятно себе...{/i}"),

            

            ), 
            size   = 43,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", i],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
        ) from _call_comic_frame_v2_label_216

        call comic_frame_v2_label((
            

            __("{i}И чем более{/i}"),


            __("{i}самоотверженно{/i}"),

            __("{i}{size=42}я вылизываю её вагину,{/size}{/i}"),
            __("{i}тем более жадно она{/i}"),

            __("{i}заглатывает член...{/i}"),

            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 470],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
        ) from _call_comic_frame_v2_label_217

        call comic_frame_v2_label((
            

            __("{i}Её громкие чмокания{/i}"),
            __("{i}заполонили всю комнату!{/i}"),


            

            ), 
            size   = 41,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 470],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
        ) from _call_comic_frame_v2_label_218

        call comic_frame_v2_label((
            

            __("{i}Я уже не могу{/i}"),
            __("{i}сдерживаться{/i}"),
            __("{i}и вот-вот выплесну{/i}"),
            __("{i}всю сперму{/i}"),
            __("{i}{size=110}ей в рот!{/size}{/i}"),

            

            ), 
            size   = 42,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 460],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2"
        ) from _call_comic_frame_v2_label_219



        call comic_frame_v2_label((
            


         #   __("{size=3} {/size}"),

            __("{i}Я уже который раз{/i}"),

            __("{i}вздрагиваю, кончая{/i}"),

            __("{i}от его шаловливого язычка.{/i}"),




          #  __("{size=3} {/size}"),

            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 450],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_220



        call comic_frame_v2_label((
            


         #   __("{size=3} {/size}"),

            __("{i}[gg] беспрестанно касается{/i}"),

            __("{i}моего клитора, доводя{/i}"),

            __("{i}меня до оргазма.{/i}"),




          #  __("{size=3} {/size}"),

            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 450],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_221

        call comic_frame_v2_label((
            


         #   __("{size=3} {/size}"),



            __("{i}Кажется, он нашёл{/i}"),

            __("{i}мою «ахиллесову пяту»,{/i}"),

            __("{i}и делает всё возможное,{/i}"),

            __("{i}чтобы я взорвалась от счастья.{/i}"),




          #  __("{size=3} {/size}"),

            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 450],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_222


        call comic_frame_v2_label((
            

            
            __("{size=10} {/size}"),

            __("  Аххх!..  "),

            __("{size=10} {/size}"),


            


            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 200],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk_shake",


        ) from _call_comic_frame_v2_label_223
        call comic_frame_v2_label((
            


         #   __("{size=3} {/size}"),



            __("{i}Он заслуживает{/i}"),

            __("{i}самого лучшего{/i}"),

            __("{i}отсоса в мире.{/i}"),




          #  __("{size=3} {/size}"),

            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 300],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_224



        show image comic_frame_v2_master:    
            easein .2 ypos 200 alpha 0.0

        $ christie_day_mischief_nyam_1 = Composite((420, 180), 
            #(0, 0), Solid("#000"),
            (0, 0), Frame(Transform('interface/comic_v2/bg_frame_2.png', alpha = .8), Borders(64, 64, 64, 64)),
            (10, 32), Text(
                            __("{i}*Чмок*{/i}"), 
                            kerning  = 5,
                            size     = 100,
                            outlines = [(2, "#000a", 0, 0),],
                            font = "fonts/mango_comics_er.ttf",
                            
                            ),

            )



        show image christie_day_mischief_nyam_1: 
            zoom .7
            xpos 1250
            ypos 420
            xanchor 1.0
            yanchor 1.0
            alpha 0.0

            parallel:
                easeout .15 ypos 320 alpha 1.0
                easein  .5  ypos 280 alpha .0
                ypos 420
                repeat

        $ renpy.pause(.48, hard = True)
            

        # show image comic_frame_v2_master:    
        #     easein .2 ypos 200 alpha 0.0


    else:


        "[gg]" "Наши тела основательно покрылось потом."

        "[gg]" "Мои руки уже скользят по её заднице…"

        "[gg]" "Мы оба подошли к вопросу ласок с фанатичной самоотдачей. "

        "[gg]" "Делать Кристи приятно – значит делать приятно себе."

        "[gg]" "И чем более самоотверженно я вылизываю её вагину, тем более жадно она заглатывает член."

        "[gg]" "Её громкие чмокания и заполонили всю комнату. "

        "[gg]" "Я уже не могу сдерживаться, и вот-вот выплесну всю сперму ей в рот."

        "Кристи" "Чмок-чмок-чмок!"

        "Кристи" "Я уже который раз вздрагиваю, кончая от его шаловливого язычка."

        "Кристи" " [gg] беспрестанно касается моего клитера, доводя меня до оргазма. "

        "Кристи" "Кажется, он нашёл мою «ахиллесову пяту», и делает всё возможное, чтобы я взорвалась от счастья. "

        "Кристи" "Аххх..!!! Чмок-чмок-чмок!!"

        "Кристи" "Он заслуживает самого лучшего отсоса в мире."

#    $ renpy.pause(.25, hard = True)
    menu christie_day_mischief_speed_up_3:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_day_mischief_speed_up_3
    hide image christie_day_mischief_nyam_1
    show christie_day_mischief_lvl_2 4
    with my_dissolve
#//Кончить
#//Скорость х4


    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            


            __("{size=3} {/size}"),



            __("{i}Ага… Я уже чувствую.{/i}"),

            __("{i}Он вот-вот кончит.{/i}"),





            __("{size=3} {/size}"),

            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 300],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_225



        call comic_frame_v2_label((
            


         #   __("{size=3} {/size}"),


            __("{size=3} {/size}"),

            __("{i}И я… Чёрт, я тоже{/i}"),

            __("{i}кончаю уже в который раз.{/i}"),




            __("{size=3} {/size}"),

          #  __("{size=3} {/size}"),

            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_9", xzoom = -1),
            say_pos = ["d", 300],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_226

        call comic_frame_v2_label((
            

            
            __("{size=10} {/size}"),

            __("  *Ах!*  "),

            __("{size=10} {/size}"),


            


            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 200],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk_shake",


        ) from _call_comic_frame_v2_label_227

        call comic_frame_v2_label((
            

            __("{size=10} {/size}"),

            __("  *Аххх!*  "),

           
            
            __("{size=10} {/size}"),


            ), 
            size   = 90,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 300],
            hide_label = "christie_night_mischief_lvl_2_christie_talk_shake_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk_shake",


        ) from _call_comic_frame_v2_label_228




        #$ renpy.pause(.1, hard = True)
        # show image christie_root_52_cum_1:
        #     ypos  800
        #     xpos  100
        #     yanchor .5
        #     alpha 1.0

        $ christie_day_mischief_cum_1 = Composite((1020, 180), 
            #(0, 0), Solid("#000"),
            (0, 0), Frame(Transform('interface/comic_v2/bg_frame_2.png', alpha = .8), Borders(64, 64, 64, 64)),
            (200, 25), Text(
                            __("{i}*Аахххх!*{/i}"), 
                            kerning  = 5,
                            size     = 120,
                            outlines = [(2, "#000a", 0, 0),],
                            font = "fonts/mango_comics_er.ttf",
                            
                            ),
            #(1020, 60), Transform("comic_frame_say_3")
            )

        show image christie_day_mischief_cum_1: #comic_frame_v2_0:
            zoom .7
            xpos 1000
            ypos 350
            xanchor .5
            yanchor 1.0
            alpha .0

            parallel:
                ease .05 alpha 1.0
            parallel:
                ease .05 ypos 360
                ease .05 ypos 367
                repeat
        hide image comic_frame_v2_master
        hide image comic_frame_v2_slave
        #show image christie_root_52_cum_2
        #show
        with my_dissolve
        $ renpy.pause(.5)

        show image '#fff'
        with Dissolve(.15)
        $ renpy.pause(.85, hard = True)
        scene christie_day_mischief_lvl_2_bg
        show christie_day_mischief_lvl_2 end
        show christie_day_mischief_lvl_2_squirt
        with Dissolve(.15)
        $ renpy.pause(.5, hard = True)

        show image comic_frame_v2_master:
            zoom .7
            xpos 550
            ypos 465
            xanchor 1.0
            yanchor 1.0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .7
            xpos 550
            ypos 465
            xanchor 1.0
            yanchor 1.0
            alpha .0
        with my_dissolve
        # call comic_frame_v2_label((
            

        #     __("{size=10} {/size}"),

        #     __("  *Ахххх!!!*  "),

           
            
        #     __("{size=10} {/size}"),


        #     ), 
        #     size   = 110,
        #     plus_y = 20,
        #     line_spasing = 6, 

        #     say_image = Transform("comic_frame_say_2"),
        #     say_pos = ["d", 300],
        #     hide_label = "christie_night_mischief_lvl_2_christie_talk_shake_hide",
        #     show_label  = "christie_day_mischief_lvl_2_christie_talk_shake",


        # )

    #Kristy_Minet_Kuni_3
        call comic_frame_v2_label((
            

            __("Вау!... Это же"),
            
            __("настоящий сквирт!!!"),


            ), 
            size   = 55,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 540],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2",

        ) from _call_comic_frame_v2_label_229
        hide christie_day_mischief_lvl_2_squirt
        with my_dissolve
        call comic_frame_v2_label((
            

            __("Большая редкость"),
            
            __("даже для самых"),

            __("искушённых женщин"),
            __("в сексе.")



            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 475],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2",


        ) from _call_comic_frame_v2_label_230

        if preferences.language in (None, 'rus'):
            $ i = 400
            $ j = -1.0
        else:
            $ i = 350
            $ j = 1.0

        call comic_frame_v2_label((
            

            __("Извини, [gg],"),

            __("кажется, я слишком"),

            __("сильно перевозбудилась."),
            

            


            ), 
            size   = 47,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2", xzoom = j),
            say_pos = ["d", i],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_231

        if preferences.language in (None, 'rus'):
            $ i = 475

        else:
            $ i = 350

        call comic_frame_v2_label((
            

            __("{size=10} {/size}"),
            __("Ты была потрясающей!"),
            

            __("{size=10} {/size}"),

            ), 
            size   = 45,
            plus_y = 18,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", i],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2",


        ) from _call_comic_frame_v2_label_232
        call comic_frame_v2_label((
            
            __("{size=3} {/size}"),

            __("Ты правда"),

            __("так думаешь?"),


            
            __("{size=3} {/size}"),


            ), 
            size   = 47,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2",),
            say_pos = ["d", 170],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_233

        call comic_frame_v2_label((
            

            
            __("Если ты сомневаешься,"),
            __("я начну вылизывать"),
            __("твою попку!"),


            


            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 475],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_gg_talk_2",


        ) from _call_comic_frame_v2_label_234
        call comic_frame_v2_label((
            
            __("{size=3} {/size}"),

            __("Ладно-ладно."),

            __("Я верю, хи-хи-хи!"),


            
            __("{size=3} {/size}"),


            ), 
            size   = 47,
            plus_y = 20,
            line_spasing = 6, 

            say_image = Transform("comic_frame_say_2",),
            say_pos = ["d", 200],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label  = "christie_day_mischief_lvl_2_christie_talk",


        ) from _call_comic_frame_v2_label_235

    else:
        

        "Кристи" "Ага… Я уже чувствую. Он вот-вот кончит."

        "Кристи" "И я… Чёрт, я тоже кончаю уже в который раз. Аххх!"

        "Кристи" "Ах! Аххх! Ахххх!!!"

        show image '#fff'
        with Dissolve(.15)
        $ renpy.pause(.85, hard = True)
        scene christie_day_mischief_lvl_2_bg
        show christie_day_mischief_lvl_2 end
        show christie_day_mischief_lvl_2_squirt
        with Dissolve(.15)
        $ renpy.pause(.5, hard = True)

        "[gg]" "Вау!..."

        "[gg]" "Это же настоящий сквирт!!!"

        "[gg]" "Большая редкость даже для самых искушённых женщин в сексе."

        "Кристи" "Извини, [gg], кажется, я слишком сильно перевозбудилась."

        "[gg]" "Ты была потрясающей."

        "Кристи" "Ты правда так думаешь? "

        "[gg]" "Если ты сомневаешься, я начну вылизывать твою попку!"

        "Кристи" "Ладно-ладно. Я верю, хи-хи-хи!"

    call comic_frame_v2_predict_label(action=renpy.stop_predict,images=comic_frame_v2_predict_list+[
        'christie_day_mischief_lvl_2_bg', 
        'christie_day_mischief_lvl_2 0',
        'christie_day_mischief_lvl_2 1_1',
        'christie_day_mischief_lvl_2 1_2',
        'christie_day_mischief_lvl_2 1_3',
        'christie_day_mischief_lvl_2 2_1',
        'christie_day_mischief_lvl_2 2_2',
        'christie_day_mischief_lvl_2 2_3',
        'christie_day_mischief_lvl_2 4', 
        'christie_day_mischief_lvl_2_water_drop'

        ]) from _call_comic_frame_v2_predict_label_1
    
    python:

        try:
            del christie_day_mischief_cum_1
        except:
            pass
        try:
            del christie_day_mischief_nyam_1
        except:
            pass
        try:
            del christie_day_mischief_nyam_2
        except:
            pass
        try:
            del christie_day_mischief_nyam_3
        except:
            pass
        

    if not from_gallery_check():
        
        
        $ add_to_gallery(39)
        #$ events.pop('christie_night_mischief_day', 0)

        scene black with Dissolve(.25)
        $ renpy.pause(.25, hard = True)
        $ renpy.pause(.5)

        $ location_now = "Corridor"
        
        $ time.time_forward(jump_to_main_interface = False)


    jump main_interface_label
