image window_lvl_2_back   = 'cg/ep105/window_event/back.png'
image window_lvl_2_front  = 'cg/ep105/window_event/front.png'
image window_lvl_2_shadow = 'cg/ep105/window_event/shadow.png'
image window_lvl_2_shadow_tmp_1 = 'cg/ep105/window_event/shadow.png'
image window_lvl_2_shadow_tmp_2 = 'cg/ep105/window_event/shadow.png'
image window_lvl_2_shadow_tmp_3 = 'cg/ep105/window_event/shadow.png'

image window_lvl_2_text_1   = 'cg/ep105/window_event/text_1.png' #Text(__('Покажи\n  тоже'), bold = True, color = "#000a", size = 23, font = "fonts/ProximaNova-Light.ttf")







image window_lvl_2_sex_back    = 'cg/ep105/window_event/sex/back.png'
image window_lvl_2_sex_gg_back = 'cg/ep105/window_event/sex/gg_back.png'
image window_lvl_2_sex_sill    = 'cg/ep105/window_event/sex/sill.png'
image window_lvl_2_sex_house   = FlashLight('cg/ep105/window_event/sex/house.png')
image window_lvl_2_sex_front   = 'cg/ep105/window_event/sex/front.png'
image window_lvl_2_sex_shadow  = 'cg/ep105/window_event/sex/shadow.png'



image window_lvl_2_sex_gg 0 = 'cg/ep105/window_event/sex/1.png'

image window_lvl_2_sex_gg 1:
    'cg/ep105/window_event/sex/1.png'
    .17
    'cg/ep105/window_event/sex/2.png'
    .17
    'cg/ep105/window_event/sex/3.png'
    .17
    'cg/ep105/window_event/sex/4.png'
    .17
    'cg/ep105/window_event/sex/5.png'
    .17
    'cg/ep105/window_event/sex/4.png'
    .17
    'cg/ep105/window_event/sex/3.png'
    .17
    'cg/ep105/window_event/sex/2.png'
    .17
    repeat


image window_lvl_2_sex_gg 2:
    'cg/ep105/window_event/sex/6_1.png'
    .12
    'cg/ep105/window_event/sex/6_2.png'
    .12
    'cg/ep105/window_event/sex/6_3.png'
    .12
    'cg/ep105/window_event/sex/6_2.png'
    .12
    repeat



image window_lvl_2_sex_gg end = 'cg/ep105/window_event/sex/6_3.png'


image window_lvl_2_sex_gg_sperm_1:
    'cg/ep105/window_event/sex/sperm_1.png'
    .17
    'cg/ep105/window_event/sex/sperm_2.png'
    .17
    'cg/ep105/window_event/sex/sperm_3.png'
image window_lvl_2_sex_gg_sperm_2 = 'window_lvl_2_sex_gg_sperm_1'
image window_lvl_2_sex_gg_sperm_3 = 'window_lvl_2_sex_gg_sperm_1'


image window_lvl_2_sex_susan stand_0 =  'cg/ep105/window_event/sex/stand_1.png'


image window_lvl_2_sex_susan stand:
    'cg/ep105/window_event/sex/stand_1.png'
    .3
    'cg/ep105/window_event/sex/stand_2.png'
    .3
    'cg/ep105/window_event/sex/stand_3.png'
    .3
    'cg/ep105/window_event/sex/stand_2.png'
    .3
    repeat

image window_lvl_2_sex_susan ass:
    'cg/ep105/window_event/sex/ass_1.png'
    .3
    'cg/ep105/window_event/sex/ass_2.png'
    .3
    'cg/ep105/window_event/sex/ass_3.png'
    .3
    'cg/ep105/window_event/sex/ass_2.png'
    .3
    repeat



image window_lvl_2_sex_susan end = 'cg/ep105/window_event/sex/tits_3.png'




image window_lvl_2_sex_susan tits:
    'cg/ep105/window_event/sex/tits_1.png'
    .3
    'cg/ep105/window_event/sex/tits_2.png'
    .3
    'cg/ep105/window_event/sex/tits_3.png'
    .3
    'cg/ep105/window_event/sex/tits_2.png'
    .3
    repeat









image window_lvl_2_circle_btn = Composite((1920, 1080),
    (1015, 240), Composite((130, 70), (0, 0), Solid("#fff1"))
    )
init -100:
    transform window_lvl_2_transform:
        pos (-600, 0)
        
        easein_cubic 1.75 pos (0, 0)
    transform window_lvl_2_transform_4:
        pos (0, 0)
        
        easein_cubic 1.75 pos (-600, 0)

    
init -100 python:
    window_lvl_2_transform_m   = window_lvl_2_transform(child='cg/ep105/window_event/s1.png')
    window_lvl_2_transform_m_5 = window_lvl_2_transform_4(child='cg/ep105/window_event/s4.png')
image window_lvl_2 s0 = Composite(
    (1920, 1080),
    (0, 0), 'window_lvl_2_back',
    (0, 0), 'window_lvl_2_front',
    )

# image window_lvl_2 s0 = Composite(
#     (1920, 1080),
#     (0, 0), 'window_lvl_2_s0_m',

#     (0, 0), Transform(AlphaMask('window_lvl_2_s0_m', 'cg/ep105/window_event/mask_1.png'), blur = 50),
#     )

image window_lvl_2 s1 = Composite(
    (1920, 1080),
    (0, 0), 'window_lvl_2_back',
    window_lvl_2_transform_m.pos, window_lvl_2_transform_m,
    (0, 0), 'window_lvl_2_front',
    ) 


image window_lvl_2 s5 = Composite(
    (1920, 1080),
    (0, 0), 'window_lvl_2_back',
    window_lvl_2_transform_m_5.pos, window_lvl_2_transform_m_5,
    (0, 0), 'window_lvl_2_front',
    ) 


image window_lvl_2 s2 = Composite(
    (1920, 1080),
    (0, 0), 'window_lvl_2_back',
    (0, 0), 'cg/ep105/window_event/s2.png',
    (0, 0), 'window_lvl_2_front',
    ) 

image window_lvl_2 s3 = Composite(
    (1920, 1080),
    (0, 0), 'window_lvl_2_back',
    (0, 0), 'cg/ep105/window_event/s3.png',
    (0, 0), 'window_lvl_2_front',
    ) 


image window_lvl_2 s4 = Composite(
    (1920, 1080),
    (0, 0), 'window_lvl_2_back',
    (0, 0), 'cg/ep105/window_event/s4.png',
    (0, 0), 'window_lvl_2_front',
    ) 
label window_lvl_2:
    #scene image '#000'
    #with Dissolve(.3)
    #$ renpy.pause(.5, hard = True)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    scene window_lvl_2 s0:
        blur 50
        pause .3
        easein_cubic .2 blur 0
    show window_lvl_2_shadow
    with my_dissolve
        
    $ from_say_screen = False
    $ renpy.pause(.5, hard = True)
    scene window_lvl_2 s1
    show window_lvl_2_shadow
    with my_dissolve

    "[gg]" "Она снова стоит напротив окна…"
    "[gg]" "Любопытно."
    "[gg]" "О чём она думает сейчас?"
    "[gg]" "На сеансе с ней я чувствую себя скованным."
    "[gg]" "Но сейчас, когда я наблюдая за ней из дома, и в полной безопасности…"
    scene window_lvl_2 s2 
    show window_lvl_2_shadow
    #with Dissolve(.25)
    with my_vpunch
    $ from_say_screen = False
    $ renpy.pause(.35, hard = True)

    "[gg]" "Это она мне?!"
    "[gg]" "Вау!"
    "[gg]" "Обратила на меня внимание, но даже не думает скрываться из вида."
    "[gg]" "Да и чего ей стесняться, она же в одежде! "
    "[gg]" "Ну и… Мы уже знакомы, верно?"
    "[gg]" "Хотя постой-ка!"
    "[gg]" "Сьюзен вряд может рассмотреть меня с такого расстояния. Она понятия не имеет, что я это я."
    "[gg]" "Она просто видит какого-то парня с биноклем. Но кто он? Почему он так пристально следит за ней? Хе-хе-хе."
    "[gg]" "Он… То есть я, определённо её заинтересовал."
    scene window_lvl_2 s3 
    show window_lvl_2_shadow
    show image "mini_games/circle_mini_game_red.png":
        anchor (.5, .5)
        xpos 250 ypos 350 zoom .5 alpha .0
        easein .5 alpha .7
    
    
    #//Kristy_Vana_Minet_1
    
    show image "mini_games/circle_mini_game_red.png":
        anchor (.5, .5)
        xpos 1080 ypos 280 alpha .7
        block:
            zoom .3
            pause .2
            easeout .25 zoom .4
            easein .25 zoom .25
            easeout .25 zoom .4
            easein .25 zoom .3
            pause 1.0
            repeat
   
    with my_dissolve

    call screen rtrn_screen("window_lvl_2_circle_btn", "window_lvl_2_circle_btn", show_icons_interface = False)
    
    hide image "mini_games/circle_mini_game_red.png"
    show window_lvl_2_text_1:
        #pos (1030, 220)
        #rotate -8
        blur 15
        easein_cubic 1.0 blur 12
        pause .5
        easein_cubic 1.0 blur 10
        easein_cubic 1.0 blur 7
        #pause 1.0
        #easein_cubic 1.0 blur 17
    show window_lvl_2_shadow_tmp_1:
        alpha 0.0
        easein_cubic 1.0 alpha 1.0
        #pause 2.0
        #easein_cubic 0.5 alpha 0.0
        #easein_cubic .5 alpha 0.0
        #easein_cubic .5 alpha 1.0
        #easein_cubic .5 alpha 0.0
    show window_lvl_2_shadow_tmp_2:
        alpha 0.0
        pause 1.5
        easein_cubic 1.0 alpha 1.0
        #pause .5
        #easein_cubic 0.5 alpha 0.0

    show window_lvl_2_shadow_tmp_3:
        alpha 0.0
        pause 2.5
        easein_cubic 1.0 alpha 1.0 
        #easein_cubic 0.5 alpha 0.0    
    with my_dissolve
    $ from_say_screen = False
    $ renpy.pause(3.5, hard = True)
    scene window_lvl_2 s3
    show window_lvl_2_shadow
    


    if not get_item('Мощный Бинокль', True):
        show window_lvl_2_text_1:
            #pos (1030, 220)
            #rotate -8
            blur 9
            
        with my_dissolve
        "[gg]" "Чёрт, не могу разобрать..."
        "[gg]" "Мне нужен бинокль помощнее."
        $ i = ('Мощный Бинокль', 300)
        if i not in add_items_for_web_shop_fixed:
            $ add_items_for_web_shop_fixed.append(i)
        jump main_interface_label



    show window_lvl_2_text_1#:
        #pos (1030, 220)
        #rotate -8
        
    with my_dissolve
    "[gg]" "«Покажи мне»?"

    "[gg]" "Что она имеет в виду? "
        
    "[gg]" "…."
        
    "[gg]" "Ха, она решила поиграть со мной. "
        
    "[gg]" "Почему бы и нет? Будет честно, если я покажу ей член, раз мне посчастливилось уже видеть её груди. "
    menu:
        "Снять штаны.":
            $ pass
        "Не снимать.":
            jump window_lvl_2_pants_on

label window_lvl_2_pants_off:
    # scene image '#000'
    # with Dissolve(.3)
    # $ renpy.pause(.5, hard = True)

    scene expression 'cg/window_event/woman_1.png'
    with my_dissolve
    "[gg]" "Судя по всему Сьюзен довольна тем, что я подыграл ей."
    "[gg]" "А её провокационная поза явно намекает на то, чтобы я оценил сладкие формы подобающим образом."
    scene image '#000'
    with Dissolve(.3)
    $ renpy.pause(.5, hard = True)
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    scene window_lvl_2_sex_back
    show window_lvl_2_sex_susan stand
    show window_lvl_2_sex_sill:
        alpha 1.0
    show window_lvl_2_sex_house
    show window_lvl_2_sex_shadow
    show window_lvl_2_sex_gg_back
    show window_lvl_2_sex_gg 1:
        alpha 0.0
        easein_cubic 2.0 alpha 1.0
    show window_lvl_2_sex_front

    if preferences.language in (None, 'eng', 'rus'):
        show image comic_frame_v2_master:
            zoom .65
            xpos 570
            ypos 265
            xanchor 0.0
            yanchor 0.0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .65
            xpos 570
            ypos 265
            xanchor 0.0
            yanchor 0.0
            alpha .0

        with my_dissolve
        

        call comic_frame_v2_label((
            
          
            __("Мне нравится"),
            __("ход её мыслей."),

            ), 
            size   = 60,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_480 

            

        call comic_frame_v2_label((
            
          
            __("Особенно теперь,"),
            __("когда мы познакомились"),
            __("друг с другом"),
            __("в таком амплуа.")

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_481 



        call comic_frame_v2_label((
            
          
            __("Для обычного психолога"),
            __("она довольно развязанная"),
            __("и… неординарная."),

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_482 

        call comic_frame_v2_label((
            
          
            __("Уверен, её чертовски"),
            __("тянет на приключения."),
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_483 


        call comic_frame_v2_label((
            
          
            __("А уж как тянет мой член…"),
            __("{size=55}уффф{/size}, это расстояние!"),
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_484 



        call comic_frame_v2_label((
            
          
            __("Вот бы оказаться"),
            __("сейчас рядом с ней."),
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_485 



        call comic_frame_v2_label((
            
          
            __("Возле ей {color=#d23a2a}сочных{/color},"),
            __("красивых сисек…"),
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_486 

        call comic_frame_v2_label((
            
          
            __("И этими"),
            __("сногсшибательными"),
            __("бёдрами…")
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_487 



        call comic_frame_v2_label((
            
          
            __("Весь мой разум"),
            __("поглощён эрогенными"),
            __("зонами её тела.")
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_488 


        call comic_frame_v2_label((
            
          
            __("Мне нравится моя"),
            __("новая роль"),
            __("наблюдателя.")
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_489 
    else:

        "[gg]" "Мне нравится её ход мыслей."
        "[gg]" "Особенно теперь, когда мы познакомились друг с другом в таком амплуа."
        "[gg]" "Для обычного психолога она довольно развязанная и… неординарная."
        "[gg]" "Уверен, её чертовские тянет на приключения."
        "[gg]" "А уж как тянет мой член… уффф, это расстояние! "
        "[gg]" "Вот бы оказаться сейчас рядом с ней. "
        "[gg]" "Возле ей сочных, красивых сисек…"
        "[gg]" "И этими сногсшибательными бёдрами…."
        "[gg]" "Весь мой разум поглощён эрогенными зонами её тела."
        "[gg]" "Мне нравится моя новая роль наблюдателя."

    menu:
        "Ускориться":
            pass
    show window_lvl_2_sex_susan ass
    show window_lvl_2_sex_sill:
        alpha 0.0
    with my_dissolve
    #Скорость 2



    if preferences.language in (None, 'eng', 'rus'):
        call comic_frame_v2_label((
            
          
            __("Как жаль, что"),
            __("я не слышу"),
            __("её придыхания.")
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_490 







        call comic_frame_v2_label((
            
          
            __("Глубоко дыша и лаская"),
            __("себя, она додумывает"),
            __("мой образ у себя"),
            __("в голове.")
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_491 



        call comic_frame_v2_label((
            
          
            __("Фантазирует о сексе,"),
            __("которого нет,"),
            __("и об ощущениях..."),
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_492 


        call comic_frame_v2_label((
            
          
            __("...которые мы бы"),
            __("могли доставить"),
            __("друг другу."),
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_493 



        call comic_frame_v2_label((
            
          
            __("Её сексуальность"),
            __("настолько притягательная,"),
            __("что я уже почти забыл о том,"),
            __("на каком расстоянии мы"),
            __("находимся друг от друга.")
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_494 




        call comic_frame_v2_label((
            
          
            __("Мне хватит одного"),
            __("неудачного рывка,"),
            __("чтобы полететь"),
            __("головой вниз…"),


            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_495 





        call comic_frame_v2_label((
            
          
            __("С мыслями"),
            __("о сиськах Сьюзен."),


            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_496 
    else:


        "[gg]" "Как жаль, что я не слышу её придыхания."
        "[gg]" "Глубоко дыша и лаская себя, она додумывает мой образ у себя в голове."
        "[gg]" "Фантазирует о сексе, которого нет, и об ощущения, которые мы бы могли доставить друг другу."
        "[gg]" "Её сексуальность настолько притягательная, что я уже почти забыл о том, на каком расстоянии мы находимся друг от друга."
        "[gg]" "Мне хватит одного неудачного рывка, чтобы полететь головой вниз…"
        "[gg]" "С мыслями о сиськах Сьюзен."
    menu:
        "Ускориться":
            pass
    show window_lvl_2_sex_susan tits
    show window_lvl_2_sex_sill:
        alpha 1.0
    with my_dissolve
    #Скорость 3

    if preferences.language in (None, 'eng', 'rus'):
        call comic_frame_v2_label((
            
          
            __("Она из тех женщин,"),
            __("что знает, как"),
            __("удовлетворить свою"),
            __("{size=65}похоть.{/size}")
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_497 



        call comic_frame_v2_label((
            
          
            __("Уверен, окажись я рядом,"),
            __("она бы обязательно"),
            __("выступила доминантом"),
            __("нашего секса.")
            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_498 




        call comic_frame_v2_label((
            
          
            __("Ухватилась за мой член,"),
            __("дрочила его,"),
            __("сосала…"),

            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_499 




        call comic_frame_v2_label((
            
          
            __("Тёрлась бы половыми губами"),
            __("об головку члена, касаясь"),
            __("краешка клитора и хлипко"),
            __("стоная от удовольствия.")

            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_500 




        call comic_frame_v2_label((
            
          
            __("Думая об этом, я даже"),
            __("легко могу представить,"),
            __("как именно бы она"),
            __("пахла в этот момент.")

            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_501 




        call comic_frame_v2_label((
            
          
            __("Я бы вылизывал её"),
            __("тело и трогал"),
            __("мягкие груди..."),

            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_502 




        call comic_frame_v2_label((
            
          
            __("Уффф…"),
            __("Я вот-вот кончу"),
            __("от этих переживаний."),

            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_503 
        show image comic_frame_v2_master:    
            easein .2 ypos 300 alpha 0.0
        $ renpy.pause(.1, hard = True)
    else:

        "[gg]" "Она из тех женщин, что знает, как удовлетворить свою похоть."
        "[gg]" "Уверен, окажись я рядом, она бы обязательно выступила доминантом нашего секса. "
        "[gg]" "Ухватилась за мой член, дрочила его, сосала…."
        "[gg]" "Тёрлась бы половыми губами об головку члена, касаясь краешка клитора и хлипко стоная от удовольствия. "
        "[gg]" "О да. Думая об этом, я даже легко могу представить, как именно бы она пахла в этот момент."
        "[gg]" "Я бы вылизывал её тело и трогал мягкие груди."
        "[gg]" "Уффф… "
        "[gg]" "Я вот-вот кончу от этих переживаний."
    menu window_lvl_2_end:
        "Поза 1":
            show window_lvl_2_sex_susan stand
            show window_lvl_2_sex_sill:
                alpha 1.0
            with my_dissolve
            $ renpy.pause(9999)
            jump window_lvl_2_end
        "Поза 2":
            show window_lvl_2_sex_susan ass
            show window_lvl_2_sex_sill:
                alpha 0.0
            with my_dissolve
            $ renpy.pause(9999)
            jump window_lvl_2_end
        "Поза 3":
            show window_lvl_2_sex_susan tits
            show window_lvl_2_sex_sill:
                alpha 1.0
            with my_dissolve
            $ renpy.pause(9999)
            jump window_lvl_2_end
        "Кончить":
            pass


    show window_lvl_2_sex_susan tits
    show window_lvl_2_sex_sill:
        alpha 1.0
    
    show window_lvl_2_sex_gg 2
    with my_dissolve
    #Кончить

    if preferences.language in (None, 'eng', 'rus'):
        call comic_frame_v2_label((
            
          
            __("Да, я вижу,"),
            __("она тоже близка"),
            __("к завершению."),

            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_504 


        call comic_frame_v2_label((
            
          
            __("Сьюзен стала"),
            __("чаще и продолжительней"),
            __("вздрагивать."),

            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_505 



        call comic_frame_v2_label((
            
          
            __("Количество оргазмов"),
            __("практически сбивают"),
            __("её с ног."),

            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_506 




        $ window_lvl_2_cum_1 = Composite((900, 180), 
            #(0, 0), Solid("#000"),
            (0, 0), Frame(Transform('interface/comic_v2/bg_frame_2.png', alpha = .8), Borders(64, 64, 64, 64)),
            (50, 50), Text(
                            __("{i}Сьюзееееееееен!!!{/i}"), 
                            kerning  = 5,
                            size     = 70,
                            outlines = [(2, "#000a", 0, 0),],
                            font = "fonts/mango_comics_er.ttf",
                            
                            ),
            #(1020, 60), Transform("comic_frame_say_3")
            )

        show image window_lvl_2_cum_1: #comic_frame_v2_0:
            zoom .7
            xpos 900
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
        $ renpy.pause(1.0, hard = True)
        #show image '#fff'
        #with Dissolve(.15)
        #$ renpy.pause(.85, hard = True)
        scene window_lvl_2_sex_back
        show window_lvl_2_sex_susan end
        show window_lvl_2_sex_sill
        show window_lvl_2_sex_house
        show window_lvl_2_sex_shadow
        show window_lvl_2_sex_gg_back
        show window_lvl_2_sex_gg end
        show window_lvl_2_sex_front
        
        with Dissolve(.15)
        $ renpy.pause(.15, hard = True)
        show window_lvl_2_sex_gg_sperm_1:
            alpha 1.0 pos(0, 0)

            easein_cubic 1.0 alpha .75 pos (0+8, 20)
            #easein_cubic 1.0 pos (0, 15) alpha .5
        $ renpy.pause(1.0, hard = True)

        show window_lvl_2_sex_gg_sperm_2:
            alpha 1.0 pos(-1020, -30) xzoom -1
            easein_cubic 1.5 alpha .6 pos(-1020+8, 5)
        $ renpy.pause(1.0, hard = True)

        show window_lvl_2_sex_gg_sperm_3:
            alpha 1.0 pos (0, 0)
            parallel:
                easein_cubic .5 alpha .8
            parallel:
                easein_cubic .5 pos (-17+8, -10)
        $ renpy.pause(1.0, hard = True)
            
        show image comic_frame_v2_master:
            zoom .65
            xpos 570
            ypos 265
            xanchor 0.0
            yanchor 0.0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .65
            xpos 570
            ypos 265
            xanchor 0.0
            yanchor 0.0
            alpha .0
        with my_dissolve
        call comic_frame_v2_label((
            
          
            __("Даааааааа!...."),
            __("Такие забавы мне"),
            __("определённо нравятся.")


            

            ), 
            size   = 45,
            plus_y = 14,
            line_spasing = 6, 
            say_image = Transform("comic_frame_say_4", xzoom = -1, yzoom = -1),
            say_pos = ["l", 20],
            
        ) from _call_comic_frame_v2_label_507 


    else:

        "[gg]" "Да, я вижу, она тоже близка к завершению."
        "[gg]" "Сьюзен стала чаще и продолжительней вздрагивать."
        "[gg]" "Количество оргазмов практически сбивают её с ног."

        "[gg]" "Сьюзееееееееен!!!"
        #show image '#fff'
        #with Dissolve(.15)
        #$ renpy.pause(.85, hard = True)
        scene window_lvl_2_sex_back
        show window_lvl_2_sex_susan end
        show window_lvl_2_sex_sill
        show window_lvl_2_sex_house
        show window_lvl_2_sex_shadow
        show window_lvl_2_sex_gg_back
        show window_lvl_2_sex_gg end
        show window_lvl_2_sex_front
        
        with my_dissolve
        $ renpy.pause(.15, hard = True)
        show window_lvl_2_sex_gg_sperm_1:
            alpha 1.0 pos(0, 0)

            easein_cubic 1.0 alpha .75 pos (0+8, 20)
            #easein_cubic 1.0 pos (0, 15) alpha .5
        $ renpy.pause(1.0, hard = True)

        show window_lvl_2_sex_gg_sperm_2:
            alpha 1.0 pos(-1020, -30) xzoom -1
            easein_cubic 1.5 alpha .6 pos(-1020+8, 5)
        $ renpy.pause(1.0, hard = True)

        show window_lvl_2_sex_gg_sperm_3:
            alpha 1.0 pos (0, 0)
            parallel:
                easein_cubic .5 alpha .8
            parallel:
                easein_cubic .5 pos (-17+8, -10)
        $ renpy.pause(1.0, hard = True)

        "[gg]" "Даааааааа!...."
        "[gg]" "Такие забавы мне определённо нравятся. "
        

    $ add_ach('ACH_12')
    python:
        if not from_gallery_check():

            add_to_gallery(44)
        try:
            del window_lvl_2_cum_1
        except:
            pass
    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.6, hard = True)
    if not from_gallery_check():
        $ time.time_forward()
    jump main_interface_label







label window_lvl_2_pants_on:
    scene window_lvl_2 s4
    show window_lvl_2_shadow
    
        
    with my_dissolve
    "[gg]" "Хм…"
    "[gg]" "Кажется, она разочарована моим решением."
    scene window_lvl_2 s5
    show window_lvl_2_shadow
    "[gg]" "Я ей больше не интересен."

    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.6, hard = True)
    jump main_interface_label

