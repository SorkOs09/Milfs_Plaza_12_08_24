transform pot_fire_transform:
    
    easein .1 yzoom 1.02
    easeout .25 yzoom 1.0
    easein .1 yzoom 1.02
    easeout .25 yzoom 1.0
    easein .1 yzoom 1.02
    easeout .25 yzoom 1.0
    easein .1 yzoom 1.02
    easeout .25 yzoom 1.0

    easein .1 yzoom 1.02
    easeout .25 yzoom 1.0
    easein .1 yzoom 1.02
    easeout .25 yzoom 1.0
    easein .1 yzoom 1.02
    easeout .25 yzoom 1.0
    easein .1 yzoom 1.02
    easeout .25 yzoom 1.0

    easein .1 yzoom 1.02
    easeout .25 yzoom 1.0
    easein .1 yzoom 1.02
    easeout .25 yzoom 1.0
    easein .1 yzoom 1.02
    easeout .25 yzoom 1.0
    easein .1 yzoom 1.02
    easeout .25 yzoom 1.0
    
    

    repeat
transform pot_fire_fail_transform:
    
    
    easein .25 yzoom 1.02
    easeout .1 yzoom 1.0
    easein .25 yzoom 1.02
    easeout .1 yzoom 1.0
    easein .25 yzoom 1.02
    easeout .1 yzoom 1.0
    easein .25 yzoom 1.02
    easeout .1 yzoom 1.0

    easein .25 yzoom 1.02
    easeout .1 yzoom 1.0
    easein .25 yzoom 1.02
    easeout .1 yzoom 1.0
    easein .25 yzoom 1.02
    easeout .1 yzoom 1.0
    easein .25 yzoom 1.02
    easeout .1 yzoom 1.0

    easein .25 yzoom 1.02
    easeout .1 yzoom 1.0
    easein .25 yzoom 1.02
    easeout .1 yzoom 1.0
    easein .25 yzoom 1.02
    easeout .1 yzoom 1.0
    easein .25 yzoom 1.02
    easeout .1 yzoom 1.0
    
    
    repeat

transform pot_cover_transform:
    #ypos -50 xpos 12
    #at transform:
    rotate 0
    easein .25 rotate 5
    easein .25 rotate -5
    easein .15 rotate 0
    repeat
image christie_root_58_pot =     Composite(
    (200, 200),

    (0, -5), "mini_games/pot/pot_main.png",
    (0, 0), pot_fire_transform(child = "mini_games/pot/pot_fire.png"),
    (10, 5), pot_cover_transform(child = "mini_games/pot/pot_cover.png"),

    )

image christie_root_58_pot_fail =     Composite(
    (200, 200),

    (0, -5), "mini_games/pot/pot_main.png",
    (0, 0), pot_fire_transform(child = "mini_games/pot/pot_fire.png"),
    (-5, -10), pot_fire_fail_transform(child = "mini_games/pot/pot_fire.png"),
    (5, 10), pot_fire_transform(child = "mini_games/pot/pot_fire.png"),
    (-5, -20), pot_fire_fail_transform(child = "mini_games/pot/pot_fire.png"),
    #(5, -30), pot_fire_transform(child = "mini_games/pot/pot_fire.png"),
    
    (10, -5), pot_cover_transform(child = "mini_games/pot/pot_cover.png"),

    )
# screen christie_root_58_pot:

#     viewport:
#         xmaximum 200
#         ymaximum 200

#         xpos 515 ypos 440
#         image '#0000'
#         image "mini_games/pot/pot_main.png" yalign 1.0
#         image "mini_games/pot/pot_fire.png":
#             yalign 1.0
#             at transform:
                
#         image "mini_games/pot/pot_cover.png":
#             ypos -50 xpos 12
#             at transform:
#                 rotate 0
#                 easein .25 rotate 5
#                 easein .25 rotate -5
#                 easein .15 rotate 0
#                 repeat
label christie_root_58:
    $ events.pop('christie_root_58', 0)
    $ christie_root_58_fail_nums = 0

label christie_root_58_1:

    #Приготовить салаты и бутерброды.
    #"ext" "Активировать кухонный стол / или зайти на кухню"
    #"ext" "GG_Povar"
    call show_bg_image_label from _call_show_bg_image_label_205
    #show screen christie_root_58_pot
    show christie_root_58_pot:
        xpos 515 ypos 440
    with my_dissolve
    $ christie_root_58_xzoom = -1
    show GG Think
    show GG Think at go_from_right(xxalign = .75, xxzoom = -1)
    
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/mini_game.mp3', fadein = 1.5)
    #"" "{color=#F00}GG_Povar{/color}"
   # "[gg]" 

    "[gg]" "Что ж…"
    $ i = renpy.call_screen('circle_mini_game_screen', xp = 300, yp = 500, tm = 5)
    if not i:
        jump christie_root_58_fail
    $ christie_root_58_xzoom = 1
    show GG:
        xzoom 1
        easein .5 xalign -.05
    "[gg]" "Варим картошку и яйца…"
    "[gg]" "Нарезаем колбасу, огурцы, морковь…"

    $ i = renpy.call_screen('circle_mini_game_screen', xp = 1450, yp = 500, tm = 4)
    if not i:
        jump christie_root_58_fail
    $ christie_root_58_xzoom = -1
    show GG:
        xzoom -1
        easein .5 xalign .8
    "[gg]" "Добавляем зелёный горошек…"
    "[gg]" "Заливаем майонезом и перемешиваем эту хрень…"

    $ i = renpy.call_screen('circle_mini_game_screen', xp = 300, yp = 500, tm = 3)
    if not i:
        jump christie_root_58_fail
    $ christie_root_58_xzoom = 1
    show GG:
        xzoom 1
        easein .5 xalign -.05
    "[gg]" "Перец, соль, листья петрушки… "
    "[gg]" "Теперь сделаю пару тостов…"

    $ i = renpy.call_screen('circle_mini_game_screen', xp = 1450, yp = 500, tm = 2)
    if not i:
        jump christie_root_58_fail
    $ christie_root_58_xzoom = -1
    show GG:
        xzoom -1
        easein .5 xalign .8
    "[gg]" "Чесночную намазочку, рыбка в масле… Уххх бля, вот это хрючево получается!"
label christie_root_58_end:
    hide christie_root_58_pot_fail
    hide christie_root_58_pot
    show screen give_item_screen(i_path+'/items/sandwitch.png', _('Закуска для пикника'), [_('Я готовил это весь день!')])
    with my_dissolve
    "[gg]" "Бэлиссимо! "
    

    $ remove_from_inventory_by_id(57)

    $ add_to_inventory_by_id(58, False)

    $ Event("christie_root_59", "JayBobTalk")
    
    $ descript_Christie = __("Купить красивую корзину, куда можно будет положить бутерброды и салат. Но что-то мне подсказывает, в магазине я вряд ли её смогу найти.")
    hide screen give_item_screen
    with my_dissolve
    python:
        try:
            del christie_root_58_xzoom
        except:
            pass

        try:
            del christie_root_58_fail_nums
        except:
            pass
        
        time.time_forward()
    jump main_interface_label


label christie_root_58_fail:
    hide christie_root_58_pot
    hide GG
    show GG Falldown
    show christie_root_58_pot_fail:
        xpos 515 ypos 440
        easein .1 ypos 445
        easein .1 ypos 440
        repeat
    with my_vpunch
    if christie_root_58_xzoom == -1:
        show GG Falldown:
            ypos 1085 xpos 1600
            xzoom .9 yzoom .9
            parallel: 
                easeout 3.0 xpos 2300
            parallel:
                easein .1 ypos 1090
                easein .1 ypos 1080
                repeat
    
    else:
        show GG Falldown:
            ypos 1085 xpos 300
            xzoom -.9 yzoom .9
            parallel:
                easeout 3.0 xpos -400
            parallel:
                easein .1 ypos 1090
                easein .1 ypos 1080
                repeat
    $ renpy.pause(.5)
    scene image "#000" with my_dissolve

    "" "Вы не уследили за блюдом и оно сгорело."
    "" "Попробовать снова?"
    
    menu:
        "Да":
            
            $ christie_root_58_fail_nums += 1
            jump christie_root_58_1
        "Нет":
            $ renpy.full_restart()
            jump christie_root_58_1
        "Пропуск" if christie_root_58_fail_nums > 3:
            call show_bg_image_label from _call_show_bg_image_label_206
            show christie_root_58_pot:
                xpos 515 ypos 440
            with my_dissolve
            show GG Think
            show GG Think at go_from_right(xxalign = .75, xxzoom = -1)
            jump christie_root_58_end
    jump christie_root_58_1