transform leaf_rotate_1:
    easein 90 rotate 360

image cg_ep9_picnic_t: 
    'cg/ep9/picnic/1t.png'
    .075
    'cg/ep9/picnic/2t.png'
    .075
    'cg/ep9/picnic/3t.png'
    .075
    'cg/ep9/picnic/4t.png'
    .075
    '#0000'
image cg_ep9_picnic 2t = 'cg/ep9/picnic/2t.png'
image cg_ep9_picnic 3t = 'cg/ep9/picnic/3t.png'
image cg_ep9_picnic 4t = 'cg/ep9/picnic/4t.png'


image cg_ep9_picnic_sex 1:
    'cg/ep9/picnic/sex/1.png'
    .17
    'cg/ep9/picnic/sex/2.png'
    .17
    'cg/ep9/picnic/sex/3.png'
    .17
    'cg/ep9/picnic/sex/4.png'
    .17
    'cg/ep9/picnic/sex/3.png'
    .17
    'cg/ep9/picnic/sex/2.png'
    .17
    repeat



image cg_ep9_picnic_sex 2:
    'cg/ep9/picnic/sex/1.png'
    .12
    'cg/ep9/picnic/sex/2.png'
    .12
    'cg/ep9/picnic/sex/3.png'
    .12
    'cg/ep9/picnic/sex/4.png'
    .12
    'cg/ep9/picnic/sex/3.png'
    .12
    'cg/ep9/picnic/sex/2.png'
    .12
    repeat



image cg_ep9_picnic_sex 3:
    'cg/ep9/picnic/sex/1.png'
    .08
    'cg/ep9/picnic/sex/2.png'
    .08
    'cg/ep9/picnic/sex/3.png'
    .08
    'cg/ep9/picnic/sex/4.png'
    .08
    'cg/ep9/picnic/sex/3.png'
    .08
    'cg/ep9/picnic/sex/2.png'
    .08
    repeat






image cg_ep9_picnic_sex 4:
    'cg/ep9/picnic/sex/1.png'
    .05
    'cg/ep9/picnic/sex/2.png'
    .05
    'cg/ep9/picnic/sex/3.png'
    .05
    'cg/ep9/picnic/sex/4.png'
    .05
    'cg/ep9/picnic/sex/3.png'
    .05
    'cg/ep9/picnic/sex/2.png'
    .05
    repeat

image cg_ep9_picnic_sex 5 = 'cg/ep9/picnic/sex/5.png'




image cg_ep9_picnic_kiss 2 = 'cg/ep9/picnic/kiss_scene/2.png'
image cg_ep9_picnic_kiss 1 = 'cg/ep9/picnic/kiss_scene/1.png'
image cg_ep9_picnic_kiss 3 = 'cg/ep9/picnic/kiss_scene/3.png'
image cg_ep9_picnic_kiss 4 = 'cg/ep9/picnic/kiss_scene/4.png'
image cg_ep9_picnic_kiss 5 = 'cg/ep9/picnic/kiss_scene/5.png'
image cg_ep9_picnic_kiss 6 = 'cg/ep9/picnic/kiss_scene/6.png'
image cg_ep9_picnic_kiss 7 = 'cg/ep9/picnic/kiss_scene/7.png'
image cg_ep9_picnic_kiss 8 = 'cg/ep9/picnic/kiss_scene/8.png'

image cg_ep9_picnic 1 = 'cg/ep9/picnic/1.png'
image cg_ep9_picnic 2 = 'cg/ep9/picnic/2.png'
image cg_ep9_picnic 2_5 = 'cg/ep9/picnic/2_5.png'
image cg_ep9_picnic 3 = 'cg/ep9/picnic/3.png'
image cg_ep9_picnic 4 = 'cg/ep9/picnic/4.png'

transform leaf_rotate_2:
    easeout 50 rotate 360

transform leaf_rotate_3:
    easeout 10 rotate 360
    easeout 10 rotate 0
    repeat

image _test_kiss_leaf_1 = Composite(

    (900, 100),
    (0, 0), Solid("#0000"),
    #(0, 0), "cg/ep9/picnic/kiss_scene/leafs/1.png",

    (550, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/4.png"),
    (800, 0), "cg/ep9/picnic/kiss_scene/leafs/1.png",

    )


image _test_kiss_leaf_2 = Composite(

    (900, 100),
    (0, 0), Solid("#0000"),
    #(0, 0), "cg/ep9/picnic/kiss_scene/leafs/1.png",

    (800, 0), "cg/ep9/picnic/kiss_scene/leafs/2.png",
    

    (400, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/4.png"),

    #(600, -60), leaf_rotate_2(child="cg/ep9/picnic/kiss_scene/leafs/7.png"),

    )

image _test_kiss_leaf_3 = Composite(

    (900, 100),
    (0, 0), Solid("#0000"),

    (350, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/7.png"),

    (800, 0), "cg/ep9/picnic/kiss_scene/leafs/3.png",

    )

image _test_kiss_leaf_4 = Composite(

    (900, 100),
    (0, 0), Solid("#0000"),

    (200, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/5.png"),

    (800, 0), "cg/ep9/picnic/kiss_scene/leafs/4.png",

    )

image _test_kiss_leaf_5 = Composite(

    (900, 100),
    (0, 0), Solid("#0000"),
    #(0, 0), "cg/ep9/picnic/kiss_scene/leafs/1.png",

    (400, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/7.png"),
    (800, 0), "cg/ep9/picnic/kiss_scene/leafs/5.png",

    )



image _test_kiss_leaf_6 = Composite(

    (300, 100),
    (0, 0), Solid("#0000"),
    #(0, 0), "cg/ep9/picnic/kiss_scene/leafs/1.png",

    (400, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/5.png"),
    (200, 0), "cg/ep9/picnic/kiss_scene/leafs/6.png",

    )


image _test_kiss_leaf_7 = Composite(

    (300, 100),
    (0, 0), Solid("#0000"),
    #(0, 0), "cg/ep9/picnic/kiss_scene/leafs/1.png",

    (500, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/2.png"),
    (800, 0), "cg/ep9/picnic/kiss_scene/leafs/7.png",

    )























image _test_kiss_leaf_1_2 = Composite(

    (900, 100),
    (0, 0), Solid("#0000"),
    #(0, 0), "cg/ep9/picnic/kiss_scene/leafs/1.png",

    (550, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/4.png"),
    (800, 0), "cg/ep9/picnic/kiss_scene/leafs/1.png",

    )


image _test_kiss_leaf_2_2 = Composite(

    (900, 100),
    (0, 0), Solid("#0000"),
    #(0, 0), "cg/ep9/picnic/kiss_scene/leafs/1.png",

    (800, 0), "cg/ep9/picnic/kiss_scene/leafs/2.png",
    

    (400, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/4.png"),

    #(600, -60), leaf_rotate_2(child="cg/ep9/picnic/kiss_scene/leafs/7.png"),

    )

image _test_kiss_leaf_3_2 = Composite(

    (900, 100),
    (0, 0), Solid("#0000"),

    (350, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/7.png"),

    (800, 0), "cg/ep9/picnic/kiss_scene/leafs/3.png",

    )

image _test_kiss_leaf_4_2 = Composite(

    (900, 100),
    (0, 0), Solid("#0000"),

    (200, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/5.png"),

    (800, 0), "cg/ep9/picnic/kiss_scene/leafs/4.png",

    )

image _test_kiss_leaf_5_2 = Composite(

    (900, 100),
    (0, 0), Solid("#0000"),
    #(0, 0), "cg/ep9/picnic/kiss_scene/leafs/1.png",

    (400, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/7.png"),
    (800, 0), "cg/ep9/picnic/kiss_scene/leafs/5.png",

    )



image _test_kiss_leaf_6_2 = Composite(

    (300, 100),
    (0, 0), Solid("#0000"),
    #(0, 0), "cg/ep9/picnic/kiss_scene/leafs/1.png",

    (400, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/5.png"),
    (200, 0), "cg/ep9/picnic/kiss_scene/leafs/6.png",

    )


image _test_kiss_leaf_7_2 = Composite(

    (300, 100),
    (0, 0), Solid("#0000"),
    #(0, 0), "cg/ep9/picnic/kiss_scene/leafs/1.png",

    (500, 50), leaf_rotate_3(child="cg/ep9/picnic/kiss_scene/leafs/2.png"),
    (800, 0), "cg/ep9/picnic/kiss_scene/leafs/7.png",

    )















image _test_leaf_0 = Composite(

    (500, 500),
    (0, 0), Solid("#0000"),
    (0, 0), "mini_games/cleaning_mini_game/l_6.png",
    (150, 0), "mini_games/cleaning_mini_game/l_5.png",
    (300, 0), "mini_games/cleaning_mini_game/l_4.png",
    (450, 0), "mini_games/cleaning_mini_game/l_3.png",

    # (450, 0), leaf_rotate_1(child = "mini_games/cleaning_mini_game/l_2.png"),
    # (150, 150), leaf_rotate_1(child = "mini_games/cleaning_mini_game/l_5.png"),
    # (300, 300), leaf_rotate_2(child = "mini_games/cleaning_mini_game/l_3.png"),
    # (450, 450), leaf_rotate_1(child = "mini_games/cleaning_mini_game/l_4.png"),
    )


image _test_leaf_1 = Composite(

    (300, 200),
    (0, 0), Solid("#0000"),
    (300, 0), leaf_rotate_2(child = "mini_games/cleaning_mini_game/l_5.png"),
    # (450, 0), leaf_rotate_1(child = "mini_games/cleaning_mini_game/l_2.png"),
    # (150, 150), leaf_rotate_1(child = "mini_games/cleaning_mini_game/l_5.png"),
    # (300, 300), leaf_rotate_2(child = "mini_games/cleaning_mini_game/l_3.png"),
    # (450, 450), leaf_rotate_1(child = "mini_games/cleaning_mini_game/l_4.png"),
    )




# image _test_leaf_2 = Composite(

#     (100, 200),
#     (0, 0), Solid("#000a"),
#     (100, 0), "mini_games/cleaning_mini_game/l_5.png",
#     # (450, 0), leaf_rotate_1(child = "mini_games/cleaning_mini_game/l_2.png"),
#     # (150, 150), leaf_rotate_1(child = "mini_games/cleaning_mini_game/l_5.png"),
#     # (300, 300), leaf_rotate_2(child = "mini_games/cleaning_mini_game/l_3.png"),
#     # (450, 450), leaf_rotate_1(child = "mini_games/cleaning_mini_game/l_4.png"),
#     )


# image _test_leaf_1 = Composite(

#     (350, 120),
#     (0, 0), Solid("#0000"),
#     (0, 0), "mini_games/cleaning_mini_game/l_5.png",
#     (250, 0), "mini_games/cleaning_mini_game/l_6.png"

#     )

image _test_leaf_2 = Composite(

    (700, 120),
    (0, 0), Solid("#0000"),
    (550, 0), leaf_rotate_1(child = "mini_games/cleaning_mini_game/l_2.png"),
    (0, 0),  leaf_rotate_2(child = "mini_games/cleaning_mini_game/l_4.png"),
    (200, 0), "mini_games/cleaning_mini_game/l_3.png"

    )



image _test_leaf_3 = Composite(

    (350, 120),
    (0, 0), Solid("#0000"),
    (150, 0), leaf_rotate_1(child = "mini_games/cleaning_mini_game/l_1.png"),
    (0, 0),  leaf_rotate_2(child = "mini_games/cleaning_mini_game/l_2.png"),
    (250, 0), "mini_games/cleaning_mini_game/l_6.png"

    )




image _test_leaf_4 = Composite(

    (350, 120),
    (0, 0), Solid("#0000"),
    (0, 0),  leaf_rotate_2(child = "mini_games/cleaning_mini_game/l_5.png"),
    

    )



image _test_leaf_5 = Composite(

    (350, 120),
    (0, 0), Solid("#0000"),
    (0, 0),  leaf_rotate_1(child = "mini_games/cleaning_mini_game/l_5.png"),
    

    )



image _test_leaf_6 = Composite(

    (350, 120),
    (0, 0), Solid("#0000"),
    (0, 0),  "mini_games/cleaning_mini_game/l_2.png",
    

    )



image _test_leaf_7 = Composite(

    (350, 120),
    (0, 0), Solid("#0000"),
    (0, 0),  "mini_games/cleaning_mini_game/l_1.png",
    

    )


image _test_leaf_8 = Composite(

    (350, 120),
    (0, 0), Solid("#0000"),
    (0, 0),  "mini_games/cleaning_mini_game/l_2.png",
    

    )
label christie_root_63:
    if not from_gallery_check():
        $ events.pop('christie_root_63', 0)
    else:
        $ location_now = 'Corridor'
        $ time          = Time()
        $ time.time_now = 'evening'
        $ Location('City_Park')
    call show_bg_image_label from _call_show_bg_image_label_217
    call show_additional_images_label from _call_show_additional_images_label_109
    show Christie Normal
    show Christie Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Smile
    show GG Smile at go_from_left
    #Поговорить с Кристи о пикнике.
    #"ext" "Активировать Кристи Утром или Днём. "
    "[gg]" "Сегодня чудесный день, не правда ли?"
    show Christie Smile
    "Кристи" "Это ты так тонко подводишь к тому, чтобы пригласить меня на свидание? "
    show GG Normal:
        xalign .15
    with my_dissolve
    "[gg]" "Угадала."
    show Christie Laughs
    with my_vpunch
    "Кристи" "Уииииииииии!"
    show Christie Smile
    "Кристи" "Как же долго я этого ждала!"
    show Christie Smile
    "Кристи" "Дай минутку, я оденусь. "
    show GG Normal
    "[gg]" "Конечно, буду ждать тебя в коридоре."
    show GG:
        xzoom -1
        easein 3 xalign -1.5
    $ renpy.pause(1, hard = True)
    scene black with Dissolve(.3)
    $ renpy.pause(.3, hard = True)
    $ location_now = "Corridor"
    call show_bg_image_label from _call_show_bg_image_label_218

    show GG Think
    show GG Think at go_from_left(ttimer = 2.5)
    #"ext" "//Koridor_Day"
    #"ext" "//GG_Think"
    "[gg]" "Пожалуй, мне тоже стоит чего-нибудь накинуть на себя."
    #show GG Think
    "[gg]" "Если свидание затянется до заката, а я на это очень надеюсь, то вечером может быть довольно прохладно."
    #"ext" "//GG_Think уезжает влево"
    show Christie Street_Normal
    show Christie Street_Normal:
        xzoom -1
        xalign -1.5

    show GG:
        easein_cubic 4 xalign -1.5
    
    $ renpy.pause(1, hard = True)
    show GG Jaket_Normal:
        easein_cubic 3 xalign .8
        xzoom -1
    
    #"ext" "//GG_Street_Normal выезжает слева"
    
    "[gg]" "Вот, так-то лучше."
  
    show Christie Street_Normal:
        easein_cubic 1 xalign .1
    #show Christie Street_Normal
    "Кристи" "Ну что, пошли?"
    #show GG StreetNormal
    show GG Jaket_Normal:
        xalign .8 xzoom -1
    with my_dissolve
    #show city_icon_christie
    "[gg]" "Пойдём."
    show GG:
        easein .8 xalign .5 alpha .0
    show Christie:
        pause .5
        easein .8 xalign .5 alpha .0
    $ renpy.pause(1.5, hard = True)
    scene black with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    #"ext" "//
    $ time.time_now = "evening"


    scene image 'interface/city_interface/city_bg_evening.png'
    if mp.clouds_anim:
        show image _map_sky_mask
    #show image 'tests/clouds_2.png':
    #    xpos 0 alpha .5
    #    easein 350 xpos -1920 ypos 1080
    #show image 'interface/city_interface/city_icon_gg.png'
    #show image 'interface/city_interface/city_icon_christie.png'
    
    show city_icon_christie_gg_street:
        xpos 1570 ypos 620 alpha  .0

    

    #show city_icon_officer:
    #    xpos 1360 ypos 530
    with Dissolve(.15)
    $ renpy.pause(.2, hard = True)
    show city_icon_christie_gg_street:
        easein .25 alpha 1.0
        easein 1 xpos 1200 ypos 470 
        easeout 1 xpos 900 ypos 600 alpha .0
    show black:
        alpha .0
        pause 1.2
        easeout 1.5 alpha 1.0
    $ renpy.pause(2.4, hard = True)

    #scene image '#000' with Dissolve(.5)
    #"" "{color=#F00}Тут можно прикрутить анимацию перемещения в парк, как ты придумал ранее{/color}"
    
    # $ time.time_now = "evening"
    # $ location_now = "City_Park"

    # call show_bg_image_label
    #"ext" "//Park"
    #"ext" "//Kristy_Street_Normal выезжает справа"
    #"ext" "//GG_Street_Normal выезжает справа"
    #"ext" "//Как и в случае с прогулкой Мишвнды (продавщицы магаза), каждые несколько фразы герои будут чуть двигаться влево"
    $ location_now = "City_Park"
    call show_bg_image_label from _call_show_bg_image_label_219
    show GG Jaket_Normal
    show GG Jaket_Normal:
        xalign 1.5

    show Christie Street_Normal
    show Christie Street_Normal:
        xalign 1.5
    with my_dissolve
    show Christie at go_from_right(xxalign = .875, ttimer = 3)

    show GG at go_from_right(xxalign = 1.15, ttimer = 4, xxzoom = -1)
    #show Christie Street
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/full-moon-lofi-vibes-by-edikey20-from-filmmusic-io.mp3', fadein = 1.5)
    "Кристи" "Здесь так красиво и спокойно."
    #show GG Jaket_Normal #StreetSmile
    show Christie:
        ease 3.5 xalign .5
    show GG:
        ease 3.0 xalign 1.0
    
    "[gg]" "Ага."
    #show Christie Street
    

    
    "Кристи" "Лёгкий ветерок ласкает мою кожу..."
    show Christie:
        xalign .45 xzoom -1
    with my_dissolve
    "Кристи" "А рядом ты..."
    show Christie:
        easeout 6.0 xalign .85
    show GG:
        easeout 6.0 xalign 1.2
    "Кристи" "Тёплый..." 
    "Кристи" "Крепкий..."
    "Кристи" "И такой хороший."
    show GG Jaket_Embarrassment:
        easeout 2 xalign 1.2 ypos 1100
    "[gg]" "Ты вгоняешь меня в краску…"
    show Christie Street_Chagrin:
        xalign .85 xzoom 1
        pause 1.0
        parallel:
            ease 5.0 xalign .5
    "Кристи" "Вот только дрожу я не от ветра, [gg], а от страха, что кто-то из знакомых увидит нас и всё расскажет Маришке или твоему брату…"
    show GG Jaket_WTF:
        ease 1 xalign 1.15 ypos 1085
    
    "[gg]" "И что тогда?"
    "Кристи" "Скандал, истерики, конец отношениям."
    

    show GG:
        ease 2.0 xalign 1.0
    

    
    "[gg]" "Ты настроена негативно."
    show Christie:
        parallel:
            xzoom -1
    
    "Кристи" "Скорее реалистично."
    show GG:
        xalign 1.0
    with my_dissolve

    "[gg]" "Ну хорошо, с моим братом понятно, а почему ты решила, что Маришка будет против нас?"

    "Кристи" "Пусть я и не являюсь её дочерью, но она ощущает себя мой наставницей, что печётся о моём будущем. "

    show Christie:
        xzoom 1
        ease 3.0 xalign .25
    "Кристи" "И на это у неё имеются все основания."
    
    "Кристи" "Мои родители давно умерли, и кроме Марины у меня никого нет."

    "Кристи" "С её стороны было настоящим подвигом приютить меня. "


    "Кристи" "Как бы я не ссорилась с ней, Марина для меня герой. "
    "Кристи" "Самый дорогой человек в мире."

    "Кристи" "Я не могу не считать с её мнением."
    show Christie:
        xzoom 1
        xalign .25
    with my_dissolve
    "[gg]" "Справедливо. "
    "[gg]" "Но как на счёт нас с тобой?"

    "Кристи" "Вряд ли она обрадуется тому, что мы состоим в отношениях. "

    "Кристи" "И потому, что ты это ты, и потому, что она очень ревнивая."
    show GG Jaket_Smile:
        ease 2.0 xalign .7

    "[gg]" "Ха-ха-ха!"
    
    "[gg]" "Так к кому, по твоему, она будет ревновать? К тебе или ко мне?"
    show Christie Street_Smile
    "Кристи" "Хи-хи-хи!"
    #"ext" "//Парочка двигается чуть влево"
    #show Christie StreetSmile
    show GG:
        xalign .7
    show Christie:
        xzoom -1 xalign .22
    "Кристи" "Думаешь, у нас есть шансы избежать этого?"
    #show GG StreetNormal
    "[gg]" "Я думаю, что два взрослых человека сами могут решать, в каких отношениях им хочется пребывать."
    #show Christie StreetChagrin
    "Кристи" "Да, но… "
    #show GG StreetNormal
    "[gg]" "Реакция окружающих – как шум летнего ветра. Едва ли он потревожит нас."
    #
    show Christie Street_Chagrin
    "Кристи" "А если зима? А если это зимняя вьюга?"
    #show GG StreetSmile
    "[gg]" "Тогда мы укроемся в тихом, безлюдном месте, и согреем друг друга горячими телами."
    #
    show Christie Street_Embarrassment
    "Кристи" "Под стук наших сердец. "
    #show GG StreetPassion
    "[gg]" "Звучащих в унисон любовных ласк. "
    #show Christie StreetEmbarrassment
    "Кристи" "Тогда я готова. "
    #show GG StreetSmile
    "[gg]" "К любовным ласкам? "
    show Christie Street_Laughs
    "Кристи" "К последствиям, дурачок! "
    #"ext" "GG_Street_Chagrin "
    show shadow_full:
        alpha .85
    show Christie Street_Embarrassment:
        xzoom 1
    with my_dissolve
    "Кристи" "Ну и к ласкам тоже, разумеется. "
    #show Christie StreetSmile
    hide shadow_full
    show Christie Street_Laughs:
        xzoom -1
    with my_dissolve_fast
    
    "Кристи" "Хи-хи-хи!"
    #show GG StreetLaughs
    "[gg]" "Ха-ха-ха!"
    #"ext" "//Парочка двигается чуть влево"
    show Christie Street_Smile
    "Кристи" "Мне нравится, каким ты стал, [gg]."
    #show GG StreetNormal
    "[gg]" "Мне тоже."
    #show Christie Street
    "Кристи" "Даже если ты когда-нибудь снова изменишься, я никогда не забуду этот миг."
    show GG Jaket_WTF
    "[gg]" "Почему я должен поменяться? "
    show Christie Street_Chagrin:

        xzoom 1
    with my_dissolve
    "Кристи" "Это почти всегда неизбежно. "
    #show Christie Street
    show Christie:
        ease 2.0 xalign .17
    
    "Кристи" "Под давлением обстоятельств, которые, вполне возможно, никак не будут от нас зависеть. "
    show GG Jaket_Please:
        ease 1.0 xalign .52 zoom 1.025
    #show GG StreetNormal
    "[gg]" "Тогда давай надеяться на тот исход, при котором я и ты останемся прежними. "
    #show GG StreetNormal
    show GG Jaket_Please:
        xalign .52 zoom 1.025
        parallel:
            ease 2.0 xalign .6 
        parallel:
            ease 1.0 zoom 1.0
    "[gg]" "Такими, какими мы любим друг друга. "
    show Christie Street_Laughs:
        xalign .17
    with my_dissolve
    "Кристи" "Хи-хи-хи!"

    #show GG StreetNormal
    "[gg]" "Что тебя рассмешило?"
    show Christie Street_Smile:
        xzoom -1 xalign .17
    with my_dissolve
    "Кристи" "Ты… "
    #show Christie StreetSmile
    "Кристи" "Ты сказал, что любишь меня."
    show GG Jaket_Embarrassment
    "[gg]" "Это так."
    #show Christie StreetEmbarrassment
    show shadow_full:
        alpha .75
    show Christie Street_Surprise:
        xzoom 1
    with my_dissolve
    "Кристи" "Честно?.."
    #show Christie StreetSmile
    "[gg]" "Честно."
    #show Christie StreetEmbarrassment
    hide shadow_full
    show Christie Street_Smile:
        xzoom -1
    with my_dissolve
    "Кристи" "Я тоже тебя люблю. Очень-очень сильно люблю."
    #show GG StreetSmile
    "[gg]" "Значит ты рада будешь узнать, что у меня для тебя маленький сюрприз."
    #show Christie StreetSurprise
    show Christie Street_Surprise
    with my_dissolve
    "Кристи" "Вау!..Неожиданно. "
    show GG Jaket_Smile
    "[gg]" "Да, но нам нужно чуточку пройти. "
    #show GG StreetSmile
    show GG:
        ease 6.0 xalign -1.5
    show Christie:
        pause 2.0
        xzoom 1
        ease 4.0 xalign -1.5
    "[gg]" "Сюда, сразу за кустами."
    #show Christie StreetPassion
    "Кристи" "Хи-хи-хи. Я заинтригована. "
    scene black with Dissolve(.5)
    #"ext" "//Picnic_1"
    $ renpy.pause(.75, hard = True)
    scene image 'cg/ep9/picnic/bg.png'

    #show cg_ep9_picnic 1
   # show image "cg/ep9/picnic/2_5.png":
   #     alpha 1.0 xpos -500
        
            #     _radians   = math.atan(float(_a)/float(_b))

            # _angle_tmp = _radians * (180/math.pi);
    # show image Transform("_test_leaf_2", zoom = .6):
    #     rotate_pad True xpos -300 ypos -300 
    #     parallel:
    #         easeout 2.0 rotate 90
    #         easeout 6.0 rotate -360
    #         easeout 10.0 rotate 360
    #         easeout 20.0 rotate -360
    #         easeout 10.0 rotate 360
    #         easeout 20.0 rotate 0
    #         repeat
    #     parallel:

    #         easein 60 ypos 1080 xpos 400
    #         xpos -300 ypos -300
    #         repeat


    # show image Transform("_test_leaf_3", zoom = .5):
    #     rotate_pad True xpos -450 ypos 200 
    #     parallel:
    #         easein 10.0 rotate 180
    #         easeout 15.0 rotate 360
    #         repeat
    #     parallel:

    #         easeout 20 ypos 1300 xpos 2350
    #         xpos -500 ypos 100
    #         repeat

    # show image Transform("_test_leaf_2", zoom = .6):
    #     rotate_pad True xpos 0 ypos 0
    #     parallel:
    #         easein 15.0 rotate 180
    #         easeout 10.0 rotate 360
    #         easein 15.0 rotate 540
    #         easein 10.0 rotate 720
    #         easein 20.0 rotate 900
    #         easein 20.0 rotate 1080
    #         repeat
    #     parallel:

    #         easeout 15 ypos 1500 xpos 2500
    #         xpos -400 ypos 500
    #         repeat

    # show image Transform("_test_leaf_8", zoom = .5):
    #     rotate_pad True xpos -400 ypos 400
    #     parallel:
    #         easein 10.0 rotate 180
    #         easeout 15.0 rotate 360
            
    #         repeat
    #     parallel:

    #         easeout 25 ypos 1080 xpos 2350
    #         xpos -600 ypos 50
    #         repeat
    # show image Transform("_test_leaf_7", zoom = .5):
    #     rotate_pad True xpos -400 ypos 300
    #     parallel:
    #         easein 10.0 rotate 180
    #         easeout 15.0 rotate 360
            
    #         repeat
    #     parallel:

    #         easeout 20 ypos 900 xpos 2350
    #         xpos -600 ypos 500
    #         repeat

    # show image Transform("_test_leaf_6", zoom = .4):
    #     rotate_pad True xpos -500 ypos 500
    #     parallel:
    #         easein 10.0 rotate 180
    #         easeout 15.0 rotate 360
            
    #         repeat
    #     parallel:

    #         easeout 20 ypos 650 xpos 2350
    #         xpos -600 ypos 400
    #         repeat


    # show image Transform("_test_leaf_5", zoom = .6):
    #     rotate_pad True xpos -450 ypos 100
    #     parallel:
    #         easein 10.0 rotate 180
    #         easeout 15.0 rotate 360
            
    #         repeat
    #     parallel:

    #         easeout 15 ypos 1100 xpos 2350
    #         xpos -600 ypos 400
    #         repeat



    # show image Transform("_test_leaf_4", zoom = .6):
    #     rotate_pad True xpos -450 ypos 100
    #     parallel:
    #         easein 10.0 rotate 180
    #         easeout 15.0 rotate 360
            
    #         repeat
    #     parallel:

    #         easeout 22 ypos 1100 xpos 2350
    #         xpos -500 ypos -100
    #         repeat



    # show image Transform("_test_leaf_1", zoom = .6):
    #     rotate_pad True xpos -400 ypos 150 
    #     parallel:
    #         easein 10.0 rotate 180
    #         easeout 15.0 rotate 360
    #         repeat
    #     parallel:

    #         easeout 30 ypos 1300 xpos 2350
    #         xpos -500 ypos -200
    #         repeat

    # show image Transform("_test_leaf_2", zoom = .6):
    #     rotate_pad True xpos -1100 ypos 50 
    #     parallel:
    #         easein 10.0 rotate 180
    #         easeout 15.0 rotate 360
    #         easein 10.0 rotate 540
    #         easein 15.0 rotate 720
    #         easein 20.0 rotate 900
    #         easein 20.0 rotate 1080
    #         repeat
    #     parallel:

    #         easeout 25 ypos 900 xpos 2350
    #         xpos -500 ypos -500
    #         repeat


    # show image Transform("_test_leaf_0", zoom = .6):
    #     rotate_pad True xpos -900 ypos 200 
    #     parallel:
    #         easein 10.0 rotate 180
    #         easeout 15.0 rotate 360
    #         easein 10.0 rotate 540
    #         easein 15.0 rotate 720
    #         easein 20.0 rotate 900
    #         easein 20.0 rotate 1080
    #         repeat
    #     parallel:

    #         easeout 15 ypos 600 xpos 2350
    #         xpos -400 ypos -50
    #         repeat

    # show image Transform("_test_leaf_0", zoom = .5):
    #     rotate_pad True xpos 300 ypos 100
    #     block:
    #         easeout_cubic 10.0 rotate 360 xpos 1400 ypos 800
    #         easein_cubic 10.0 rotate 360 xpos 2300 ypos 1400

    #         xpos -400 ypos -400
    #         repeat
        # parallel:

        #     easeout 40 ypos 1400 xpos 600
        #     xpos 500 ypos -400
        #     repeat

    show GG Jaket_Normal
    show GG Jaket_Normal:
        xalign 1.5

    show Christie Street_Surprise
    show Christie Street_Surprise:
        xalign 1.5

    with my_dissolve
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/almost-bliss-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    show Christie at go_from_right(xxalign = .875, ttimer = 3)

    show GG at go_from_right(xxalign = 1.15, ttimer = 4, xxzoom = -1)
    "Кристи" "Чёрт!!! Откуда здесь всё это?!"
    "[gg]" "Хе-хе-хе!.."
    "[gg]" "Я, признаться, и сам несколько шокирован."
    "Кристи" "Ну ты и скромняга!"
    "Кристи" "Так круто подготовился, да ещё и в таком неожиданном месте!"
    "Кристи" "Как тебе пришло это в голову?"
    "[gg]" "Да так… Подсобил один пикап-мастер."
    scene image 'cg/ep9/picnic/bg_shadows.png'
    show cg_ep9_picnic 1
    show image "cg/ep9/picnic/2_5.png":
        alpha 1.0 xpos -500
    with my_dissolve
    "Кристи" "Это восхитительно, [gg]. "
    "Кристи" "Ещё никто и никогда не делал таких удивительных вещей для меня. "
    "Кристи" "Ты чертовски интересный человек. "
    "[gg]" "Эй, моя заслуга тут минимальная, говорю же тебе…"
    "Кристи" "Ну да, ну да. Никогда не знаешь, что от тебя ожидать."
    "Кристи" "Я то дрожу от страха, пока мы прячемся от офицера полиции, то взрываюсь от восторга при виде таких сюрпризов. "
    "Кристи" "Справляться с эмоциональными качелями становится всё сложнее и сложнее, но от этого не менее весело. "
    "Кристи" "Такими темпами мне придётся сесть на антидепрессанты, хи-хи-хи."
    "[gg]" "Если б я знал, что это на тебе так отразится…"
    "Кристи" "Можешь расслабиться. Я уже давно поехала крышей!"
    "Кристи" "Ха-ха-ха!!!"
    "[gg]" "Ха-ха-ха!"
    show cg_ep9_picnic 2
    with my_dissolve
    "Кристи" "Пиво?.. Ты же знаешь, я не пью алкогольные напитки."
    "[gg]" "Извини, организационная промашка."
    "[gg]" "Сейчас сбегаю за водой или…"
    "Кристи" "Стой. Не надо. Хватит лишний раз утруждаться."
    "Кристи" "Мне достаточно и того, что ты проявил такую заботу. "
    play audio 'audio/ep9_piknik_vfx.mp3'
    show cg_ep9_picnic_t
    show image "cg/ep9/picnic/2_5.png":
        parallel:
            easein .5 alpha 1.0
        parallel:
            easein .5 xpos 0
    
    $ renpy.pause(.5, hard = True)
    show image "cg/ep9/picnic/2_5.png":
        alpha 0.0
    hide cg_ep9_picnic_t
    show cg_ep9_picnic 3
    with my_dissolve
    $ renpy.pause(1, hard = True)
    show image "cg/ep9/picnic/2_5.png":
        alpha 1.0
        parallel:
            easein .75 alpha 0.0
        parallel:
            easein 1.0 xpos -500
    show cg_ep9_picnic 4
    with my_dissolve
    # with Dissolve(.1)
    # $ renpy.pause(1, hard = True)
    # show cg_ep9_picnic 2t
    # with Dissolve(.1)
    # $ renpy.pause(1, hard = True)
    # show cg_ep9_picnic 3t
    # with Dissolve(.1)
    # $ renpy.pause(1, hard = True)
    # show cg_ep9_picnic 4t
    # with Dissolve(.1)
    # $ renpy.pause(1, hard = True)
    #'cg/ep9/picnic/2_5.png'
    #"ext" "//Бубнило подкладывает бутылку сока"
    "[gg]" "Ой, кажется сок всё таки есть."
    "Кристи" "Офигеть!!!"
    hide image "cg/ep9/picnic/2_5.png"
    "Кристи" "Дэвид Блэйн, как ты это делаешь?!"
    "[gg]" "Уличная магия, хе-хе-хе."
    scene image 'cg/ep9/picnic/kiss_scene/bg.png'
    show cg_ep9_picnic_kiss 1

    with my_dissolve
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Кристи" "Боюсь спросить, что ещё ты припрятал у себя в «шляпе»."
    "[gg]" "Рано раскрывать секреты, хотя кое-что, пожалуй, я могу достать прямо сейчас."
    "Кристи" "Звучит супер-пошло, хи-хи-хи!"
    "[gg]" "Наверное, впервые за вечер я тебя разочарую. "
    "Кристи" "Оу…"
    "[gg]" "Мы достаточно долго гуляем и ты, наверняка, проголодалась."
    show cg_ep9_picnic_kiss 2

    with my_dissolve
    "[gg]" "Предлагаю перекусить."
    "Кристи" "Ха! Читаешь мысли…"
    "Кристи" "Но меня это не удивляет. "
    "[gg]" "Считаешь себя предсказуемой?"
    "Кристи" "Слишком много магии. "
    "Кристи" "Любовной магии, хи-хи-хи."
    "[gg]" "Хе-хе-хе."
    "Кристи" "Но, [gg], тебе не кажется, что эта корзинка слишком мала для еды?.. "
    "Кристи" "Или это очередной фокус, и ты сейчас достанешь свежезапечённую утку?!"
    "[gg]" "Ха-ха-ха! Очень вряд ли. "
    show cg_ep9_picnic_kiss 3

    with my_dissolve
    "[gg]" "Зато я вытащу оттуда маленький, но очень вкусный бутерброд."
    "Кристи" "Ух ты! Какой он крошечный и… клёвый!"
    "Кристи" "Ты сам это приготовил?"
    "[gg]" "Пришлось."
    show cg_ep9_picnic_kiss 4

    with my_dissolve
    "Кристи" "Спасибо, ом-ном-ном, очень вкусно. "
    "Кристи" "Такое ощущение, что размер диспропорционально влияет на вкус!"
    "[gg]" "Это что-то на умном?"
    "Кристи" "Ага. Комплимент называется. "
    "[gg]" "Тогда принимаю."

    "Кристи" "Даааааа…."
    "Кристи" "Фантастический момент. "
    show cg_ep9_picnic_kiss 1

    with my_dissolve
    "Кристи" "Знаешь, такое ощущение, словно время остановилось."
    "Кристи" "Кто знает, может, пока мы веселимся и ни о чём не подозреваем, все люди исчезли. Больше никого нет. Ни мачехи, ни друзей, никого…."
    "Кристи" "Только ты и я всём мире."
    "[gg]" "Значит, нам придётся заново возобновлять генофонд планеты?"

    "Кристи" "Хи-хи-хи! Ага!"
    "Кристи" "Внутри меня пылает страстное желание спасти человечество…"
    "Кристи" "И сейчас, как мне кажется, самый подходящий момент."
    show cg_ep9_picnic_kiss 5


    #"ext" "//Сверху падают лепестки"

    show image Transform("_test_kiss_leaf_1", yzoom = 1.0):
        rotate_pad True rotate 120
        parallel:
            block:
                ease 6.5 rotate 60
                pause 2.0
                ease  6.5 rotate 120
                pause 2.0
                
                repeat
        parallel:
            xpos -100 ypos -850  
            easein 20.0 xpos 0 ypos 1100
            repeat

    show image Transform("_test_kiss_leaf_1", yzoom = -1.0):
        rotate_pad True rotate 120
        parallel:
            block:
                ease 4.5 rotate 60
                pause 0.75
                ease  4.5 rotate 120
                pause 0.75
                
                repeat
        parallel:
            xpos 0 ypos -850  
            easein 20.0 xpos 200 ypos 1100
            repeat
    show image Transform("_test_kiss_leaf_1"):
        rotate_pad True  rotate 120
        parallel:
            block:
                ease 7.0 rotate 60
                pause 0.5
                ease 7.0 rotate 120
                pause 0.5
                
                repeat
        parallel:
            xpos 150 ypos -980 
            pause 2.0
            easein 20.0 xpos 150 ypos 1650
            repeat

    show image Transform("_test_kiss_leaf_2"):
        rotate_pad True rotate 120
        parallel:
            block:
                ease 5.0 rotate 60
                pause 1.75
                ease  5.0 rotate 120
                pause 1.75
                
                repeat
        parallel:
            xpos 300 ypos -850 
            pause 5.0
            easein 20.0 xpos 300 ypos 1100
            repeat



    show image Transform("_test_kiss_leaf_2", yzoom = -1.0):
        rotate_pad True xpos 450 ypos -850  rotate 120
        parallel:
            block:
                ease 10.0 rotate 60
                pause 0.5
                ease  10.0 rotate 120
                pause 0.5
                
                repeat
        parallel:
            easein 20.0 xpos 450 ypos 1100
            repeat



    show image Transform("_test_kiss_leaf_3", yzoom = -1.0):
        rotate_pad True  rotate 120
        parallel:
            block:
                ease 6.0 rotate 60
                pause 1.5
                ease  6.0 rotate 120
                pause 1.5
                
                repeat
        parallel:
            xpos 600 ypos -850 
            easein 20.0 xpos 600 ypos 1100
            repeat





    show image Transform("_test_kiss_leaf_3"):
        rotate_pad True   rotate 120
        parallel:
            block:
                ease 11.0 rotate 60
                pause 0.5
                ease  11.0 rotate 120
                pause 0.5
                
                repeat
        parallel:
            xpos 750 ypos -850
            pause 5.0
            easein 20.0 xpos 750 ypos 1100
            repeat



    show image Transform("_test_kiss_leaf_4", yzoom = -1.0):
        rotate_pad True   rotate 120
        parallel:
            block:
                ease 6.0 rotate 60
                pause 2.5
                ease  6.0 rotate 120
                pause 2.5
                
                repeat
        parallel:
            xpos 900 ypos -850
            pause 7.0
            easein 20.0 xpos 900 ypos 1100
            repeat




    show image Transform("_test_kiss_leaf_4"):
        rotate_pad True  rotate 120
        parallel:
            block:
                ease 7.0 rotate 60
                pause 0.3
                ease  7.0 rotate 120
                pause 0.3
                
                repeat
        parallel:
            xpos 1050 ypos -850 
            pause 7.0
            easein 20.0 xpos 1050 ypos 1100
            repeat



    show image Transform("_test_kiss_leaf_5", yzoom = -1.0):
        rotate_pad True rotate 120
        parallel:
            block:
                ease 5.0 rotate 60
                pause 0.25
                ease  5.0 rotate 120
                pause 0.25
                
                repeat
        parallel:
            xpos 1200 ypos -850  
            pause 4.0
            easein 20.0 xpos 1200 ypos 1100
            repeat





    show image Transform("_test_kiss_leaf_5"):
        rotate_pad True rotate 120
        parallel:
            block:
                ease 6.0 rotate 60
                pause 0.1
                ease  6.0 rotate 120
                pause 0.1
                
                repeat
        parallel:
            xpos 1350 ypos -850
            pause 6.0
            easein 20.0 xpos 1350 ypos 1100
            repeat







    show image Transform("_test_kiss_leaf_1_2", yzoom = 1.0):
        rotate_pad True rotate 120
        parallel:
            block:
                ease 6.5 rotate 60
                pause 2.0
                ease  6.5 rotate 120
                pause 2.0
                
                repeat
        parallel:
            xpos -100 ypos -1000
            pause 12.0
            easein 20.0 xpos 0 ypos 1100
            repeat

    show image Transform("_test_kiss_leaf_1_2", yzoom = -1.0):
        rotate_pad True rotate 120
        parallel:
            block:
                ease 4.5 rotate 60
                pause 0.75
                ease  4.5 rotate 120
                pause 0.75
                
                repeat
        parallel:
            xpos 0 ypos -1000
            pause 15.0
            easein 20.0 xpos 200 ypos 1100
            repeat
    show image Transform("_test_kiss_leaf_1_2"):
        rotate_pad True  rotate 120
        parallel:
            block:
                ease 7.0 rotate 60
                pause 0.5
                ease 7.0 rotate 120
                pause 0.5
                
                repeat
        parallel:
            xpos 150 ypos -1000
            pause 15.0
            easein 20.0 xpos 150 ypos 1650
            repeat

    show image Transform("_test_kiss_leaf_2_2"):
        rotate_pad True rotate 120
        parallel:
            block:
                ease 5.0 rotate 60
                pause 1.75
                ease  5.0 rotate 120
                pause 1.75
                
                repeat
        parallel:
            xpos 300 ypos -1000
            pause 12.0
            easein 20.0 xpos 300 ypos 1100
            repeat



    show image Transform("_test_kiss_leaf_2_2", yzoom = -1.0):
        rotate_pad True xpos 450 ypos -850  rotate 120
        parallel:
            block:
                ease 10.0 rotate 60
                pause 0.5
                ease  10.0 rotate 120
                pause 0.5
                
                repeat
        parallel:
            pause 13.0
            easein 20.0 xpos 450 ypos 1100
            repeat



    show image Transform("_test_kiss_leaf_3_2", yzoom = -1.0):
        rotate_pad True  rotate 120
        parallel:
            block:
                ease 6.0 rotate 60
                pause 1.5
                ease  6.0 rotate 120
                pause 1.5
                
                repeat
        parallel:
            xpos 600 ypos -1000
            pause 21.0
            easein 20.0 xpos 600 ypos 1100
            repeat





    show image Transform("_test_kiss_leaf_3_2"):
        rotate_pad True   rotate 120
        parallel:
            block:
                ease 11.0 rotate 60
                pause 0.5
                ease  11.0 rotate 120
                pause 0.5
                
                repeat
        parallel:
            xpos 750 ypos -1000
            pause 17.0
            easein 20.0 xpos 750 ypos 1100
            repeat



    show image Transform("_test_kiss_leaf_4_2", yzoom = -1.0):
        rotate_pad True   rotate 120
        parallel:
            block:
                ease 6.0 rotate 60
                pause 2.5
                ease  6.0 rotate 120
                pause 2.5
                
                repeat
        parallel:
            xpos 900 ypos -1000
            pause 21.0
            easein 20.0 xpos 900 ypos 1100
            repeat




    show image Transform("_test_kiss_leaf_4_2"):
        rotate_pad True  rotate 120
        parallel:
            block:
                ease 7.0 rotate 60
                pause 0.3
                ease  7.0 rotate 120
                pause 0.3
                
                repeat
        parallel:
            xpos 1050 ypos -1000 
            pause 21.0
            easein 20.0 xpos 1050 ypos 1100
            repeat



    show image Transform("_test_kiss_leaf_5_2", yzoom = -1.0):
        rotate_pad True rotate 120
        parallel:
            block:
                ease 5.0 rotate 60
                pause 0.25
                ease  5.0 rotate 120
                pause 0.25
                
                repeat
        parallel:
            xpos 1200 ypos -1000 
            pause 14.0
            easein 20.0 xpos 1200 ypos 1100
            repeat





    show image Transform("_test_kiss_leaf_5_2"):
        rotate_pad True rotate 120
        parallel:
            block:
                ease 6.0 rotate 60
                pause 0.1
                ease  6.0 rotate 120
                pause 0.1
                
                repeat
        parallel:
            xpos 1350 ypos -1000
            pause 13.0
            easein 20.0 xpos 1350 ypos 1100
            repeat

#########################################3

    # show image Transform("_test_kiss_leaf_2"):
    #     rotate_pad True xpos 0 ypos -1000  rotate 120
    #     parallel:
    #         block:
    #             ease 6.0 rotate 60
    #             pause 0.5
    #             ease  6.0 rotate 120
    #             pause 0.5
                
    #             repeat
    #     parallel:
    #         easein 100.0 xpos 300 ypos 1500
    #         #repeat
    #     # parallel:
    #     #     linear 1.5 xpos 50 ypos 0
    #     #     pause .5
    #     #     linear 1.5 xpos 300 ypos 200
            


    # show image Transform("_test_kiss_leaf_3"):
    #     rotate_pad True xpos 150 ypos -900  rotate 120
    #     parallel:
    #         block:
    #             ease 7.0 rotate 60
    #             pause 0.5
    #             ease  7.0 rotate 120
    #             pause 0.5
                
    #             repeat
    #     parallel:
    #         easein 100.0 xpos 450 ypos 1600



    # show image Transform("_test_kiss_leaf_4"):
    #     rotate_pad True xpos 500 ypos -850  rotate 120
    #     parallel:
    #         block:
    #             ease 4.0 rotate 60
    #             pause 0.5
    #             ease  4.0 rotate 120
    #             pause 0.5
                
    #             repeat
    #     parallel:
    #         easein 100.0 xpos 650 ypos 1300



    # show image Transform("_test_kiss_leaf_5"):
    #     rotate_pad True xpos 750 ypos -950  rotate 120
    #     parallel:
    #         block:
    #             ease 4.0 rotate 60
    #             pause 0.5
    #             ease  4.0 rotate 120
    #             pause 0.5
                
    #             repeat
    #     parallel:
    #         easein 100.0 xpos 900 ypos 1400
            #repeat
        # parallel:
        #     linear 1.5 xpos 50 ypos 0
        #     pause .5
        #     linear 1.5 xpos 300 ypos 200
            


    # show image Transform("_test_kiss_leaf_1", zoom = .6):
    #     rotate_pad True xpos 300 ypos 200 
    #     parallel:
    #         easein 10.0 rotate 180
    #         easeout 15.0 rotate 360
    #         easein 10.0 rotate 540
    #         easein 15.0 rotate 720
    #         easein 20.0 rotate 900
    #         easein 20.0 rotate 1080
    #         repeat
    #     parallel:

    #         easeout 15 ypos 600 xpos 2350
    #         xpos -400 ypos -50
    #         repeat

    with my_dissolve
    "Кристи" "О Боже…. "
    "Кристи" "Я едва сдерживаюсь, чтобы не закричать от удивления."
    "Кристи" "Это…"
    "Кристи" "Потрясающе!"
    "[gg]" "Я полностью разделяю твою реакцию…"
    "Кристи" "Мне кажется – это сон."
    "[gg]" "И кто из нас спит?"
    "Кристи" "Оба… Наверное."
    "Кристи" "И, раз уж мы в глубине своего сознания, то почему бы нам..."
    show cg_ep9_picnic_kiss 6
    with my_dissolve

    #"ext" "//Кристи снимает с себя одежду"
    #"ext" "//Мысли ГГ"
    "[gg]" "{i}Чёрт, это лучший момент в моей жизни, но если я займусь любовью с Кристи здесь и сейчас, то Зудило и Бубнило станут неотъемлемой частью этого мгновения.{/i}"
    "[gg]" "{i}Да к тому же, они наверняка заснимут наш секс…{/i}"
    "[gg]" "{i}Нет, я так не хочу.{/i}"
    show cg_ep9_picnic_kiss 7
    with my_dissolve
    "Кристи" "Ты замер от неожиданности или поражён моей развязностью, хи-хи-хи?"
    "[gg]" "Я…"
    "[gg]" "Слушай, мне кажется, этот чудесный вечер не стоит так заканчивать."
    "Кристи" "Ч-что?.. "
    "Кристи" "Ты серьёзно?!"
    "[gg]" "Не подумай ничего дурного. "
    "[gg]" "Я очень тебя хочу. "
    "[gg]" "И готов сорвать с тебя всю одежду…"
    "Кристи" "Ну и?"
    "[gg]" "Просто в любой момент сюда может явиться кто-то из прохожих…"
    "[gg]" "Заметит нас, подымится шумиха.."
    with my_vpunch
    "Кристи" "Плевать!"
    "Кристи" "Я готова к любым последствиям!"
    "Кристи" "Пусть сюда явится хоть вся съёмочная группа из местного телеканала!"
    "Кристи" "Давай сделаем это, [gg]!"
    "Кристи" "Мы так долго скрывались… Так долго жаждали этого момента…"
    "Кристи" "Возьми меня, [gg]."



    show image comic_frame_v2_master:
        zoom .5
        xpos 1800
        ypos 100
        xanchor 1.0
        yanchor .5
        alpha .0

    show image comic_frame_v2_slave:
        zoom .5
        xpos 1800
        ypos 100
        xanchor 1.0
        yanchor .5
        alpha .0
    
    with Dissolve(.2)


    #"ext" "//Зудило кричит сверху"
    if preferences.language in (None, 'eng', 'rus'):
        call comic_frame_v2_label((
            
            __("Дааа, [gg], возьми её уже наконец!!!"),
          
            ),
            say_image = Transform("comic_frame_say_1", yzoom = -1),
            say_pos = ["u", 700],
            #show_label = 'christie_root_52_christie_talk_move',

            plus_y = 50,

            line_spasing = -2, 


        ) from _call_comic_frame_v2_label_182
    else:
        "!" "Дааа, [gg], возьми её уже наконец!!!"
    show image comic_frame_v2_master
    show image comic_frame_v2_slave
    show cg_ep9_picnic_kiss 8
    

    show image comic_frame_v2_master:
        alpha .0
    with my_vpunch
    "Кристи" "Кто это?!!"
    "[gg]" "…."
    if preferences.language in (None, 'eng', 'rus'):
        call comic_frame_v2_label((
            
            __("Эээ… Троооопииииическииий мирааааж…."),
          
            ),
            say_image = Transform("comic_frame_say_1", yzoom = -1),
            say_pos = ["u", 700],
            #show_label = 'christie_root_52_christie_talk_move',

            plus_y = 50,

            line_spasing = -2, 


        ) from _call_comic_frame_v2_label_183
    else:
        "!" "Эээ… Троооопииииическииий мирааааж…."
    show image comic_frame_v2_master:
        alpha .0
    with my_vpunch
    "[gg]" "Ладно, придурки, слезайте и валите!"
    scene black with vpunch
    $ renpy.pause(.3, hard = True)
    $ location_now = "City_Park"
    
    scene image 'cg/ep9/picnic/bg.png'
    show Christie Street_Angry
    show Christie Street_Angry:
        xalign -1.5
        
    show GG Jaket_Please
    show GG Jaket_Please:
        xalign -1.5

    show Bob Normal
    show Bob Normal:
        xalign 1.3
        ypos 1085
        zoom 1.0-0.035

    show Jay Normal
    show Jay Normal:
        xalign 1.1
        ypos 1085
        zoom 1.0-0.035



    show Jay Normal
    show Jay Normal:
        xalign 1.7
        ypos 1085
        zoom 1.0-0.035
        
    show Bob Normal
    show Bob Normal:
        xalign 1.7
        ypos 1085
        zoom 1.0-0.035

    with my_dissolve
    show Jay:
        easein 1.5 xalign .8
    show Bob:
        easein 1.5 xalign 1.1
    show Christie at go_from_left(xxalign = 0.0, ttimer = 1, xxzoom = -1)

    show GG at go_from_left(xxalign = .22, ttimer = 1)
    #"ext" "//Бэк полянки"
    #"ext" "//JayBob"
    "Зудило" "Ёпт, чувак… Автопалево!"
    #show Christie Surpise
    show shadow_full:
        alpha .85
    with my_dissolve
    "Кристи" "Ты их знаешь, [gg]?!"
    #show GG Normal
    show GG:
        xalign .22 xzoom -1
    show Christie:
        xalign .0 xzoom -1
    show Bob:
        xalign 1.1
    show Jay:
        xalign .8
    with my_dissolve
    "[gg]" "Ага. Это они тут… магию создавали."
    #show Christie Smile
    show Christie Street_Smile
    with my_dissolve
    "Кристи" "Хи-хи-хи."
    show GG Jaket_Normal:
        xalign .22 xzoom 1
    hide shadow_full
    with my_dissolve
    "Зудило" "Вынуждены откланяться, мадумазэль!"
    show Jay:
        xzoom -1
    with my_dissolve
    "Зудило" "Не стой столбом, Бубнило. Видишь, чувак и его чувиха хотят уединиться. "
    "Зудило" "Без нас. "
    "Зудило" "К сожалению."
    #show GG Normal
    show Jay:
        xzoom 1
    with my_dissolve
    "[gg]" "Ну всё, всё. Спасибо за помощь. Увидимся в другой раз. "
    "Зудило" "Ага…."
    "Бубнило" "…."
    show Jay:
        xzoom -1
        easein 1.0 xalign 1.5
    show Bob:
        xzoom -1
        easein 1.0 xalign 1.5
    show GG:
        easein 1.0 xalign .8
        xzoom -1
    show Christie:
        easein 1.0 xalign .2
    show black:
        alpha .0
        easein .5 alpha 1.0
    $ renpy.pause(1.0, hard = True)
    scene image 'cg/ep9/picnic/bg_shadows.png'
    show cg_ep9_picnic 1
    with my_dissolve
    #"ext" "////JayBob исчезает вправо"
    #"ext" "//Снова ГГ и Кристи"
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Ну вот, теперь мы точно одни."
    # hide Jay
    # hide Bob
    # show GG:
    #     xalign .8
    #     xzoom -1
    # show Christie:
    #     xalign .2
    # with my_dissolve
    "Кристи" "Ты уверен?"
    "[gg]" "Если только они не остались чуть поодаль, и не подглядывают из кустов."
    "Кристи" "Ну и пусть."
    "Кристи" "Завистники, хи-хи."
    "[gg]" "Значит, наш вечер только начинается? "
    "Кристи" "В самом разгаре."
    scene image 'cg/ep9/picnic/kiss_bg.png'

    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    scene image 'cg/ep9/picnic/kiss.png'
    #show image 'cg/ep9/picnic/kiss_fg.png'
    with Dissolve(1.0)
    $ renpy.pause(.9, hard = True)


    #"ext" "//Поцелуй"
    #"ext" "//Kristy_Sex_Park_1"
    "Кристи" "Ты такой нежный…"
    "[gg]" "Тебе это нравится?"
    "Кристи" "Конечно."
    "Кристи" "Люблю твои прикосновения, твоё горячее дыхание..."
    "Кристи" "Твой член…"
    scene black with Dissolve(.3)
    $ renpy.pause(.5, hard = True)
    scene image 'cg/ep9/picnic/sex/bg.png'
    show cg_ep9_picnic_sex 1
    with my_dissolve
    #"ext" "//Cкорость х1"
    "Кристи" "Мммм…."
    "[gg]" "Всё хорошо?"
    "Кристи" "Да… Продолжай…"
    "[gg]" "У тебя очень выразительный взгляд сейчас."
    "Кристи" "Ты меня смущаешь…"
    "[gg]" "Мне нравится, как ты наслаждаешься процессом."
    "Кристи" "Как и ты, полагаю."
    "[gg]" "Несомненно."
    "[gg]" "Мы слишком долго шли к этому мгновению. "
    "Кристи" "Я знаю. "
    "Кристи" "Ахх… Ахх… Ахх.."
    "Кристи" "Что ты чувствуешь?"
    "[gg]" "Удовольствие."
    "Кристи" "О чём ты думаешь?.."
    "[gg]" "О тебе."
    "Кристи" "Хи-хи-хи!"
    menu christie_root_63_speed_up_1:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_root_63_speed_up_1
    show cg_ep9_picnic_sex 2
    with my_dissolve
    #"ext" "//Cкорость х2"
    "Кристи" "Афффф…. Оххххх…. !!"
    "Кристи" "Да-да-да!!"
    "Кристи" "Кажется, ты не на шутку увлёкся."
    "[gg]" "Это ты виновата"
    "Кристи" "Слишком плотно сжимаю твой член? Хи-хи-хи."
    "[gg]" "Ага… И громко вздыхаешь от удовольствия. "
    "Кристи" "Значит, тебя возбуждают мои придыхания? "
    "[gg]" "Я бы сказал… перевозбуждают, хе-хе."
    "Кристи" "Тогда, наверное, мне стоит быть ещё более развязной, а?"
    "[gg]" "Ха! Будь кем хочешь, Кристи. Главное, продолжай двигаться в такт со мной."
    "Кристи" "Оххх, [gg], какой ты напористый! "
    "Кристи" "В тебе столько бушующей энергии… Аффф!!! Уххх!!!"
    "Кристи" "Хочу больше! Больше! БОЛЬШЕ!!!"
    #"ext" "//Cкорость х3"
    menu christie_root_63_speed_up_2:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_root_63_speed_up_2
    show cg_ep9_picnic_sex 3
    with my_dissolve
    "[gg]" "Вот так, да?!"
    "Кристи" "Да-да-да!!!"
    "Кристи" "Ещё-ещё-ещё! Сильнее!!!"
    "[gg]" "Мой член так глубоко проникает, что буквально достаёт до твоей матки!"
    "Кристи" "Хех..!!! Я сделаю всё возможное, чтобы у тебя получилось!"
    "Кристи" "С меня буквально течёт вода. И снаружи, и внутри."
    "Кристи" "Я вся пылаю от удовольствия…"
    "Кристи" "Нам не стоило так долго откладывать это событие! "
    "[gg]" "Но мы же компенсируем это время, верно?"
    "Кристи" "Чрезмерным занятием сексом? "
    "[gg]" "Читаешь мои мысли!"
    "Кристи" "Сейчас моими мыслями управляет твой член, [gg]!"
    "[gg]" "Тогда ты полностью под моим контролем…"
    "Кристи" "Уже давно… Аххх! Оххх!..."
    "Кристи" "Я… Почти на грани, [gg]!.."
    "[gg]" "Я тоже… "
    "Кристи" "Хочу почувствовать как можно больше твоей горячей спермы, любимый! "
    "Кристи" "Кончи в меня! Кончи всё, до последней капли! "
    menu:
        "Кончить":
            $ pass
    show cg_ep9_picnic_sex 4
    with my_dissolve
    #"ext" "//Кончить"
    #"ext" "//Скорость х4"
    "Кристи" "Аххх!! "
    "Кристи" "Уффффф!!!"
    "Кристи" "Потрясающеееееее!!"
    "[gg]" "О дааааааааа, малышка!"
    "[gg]" "Сейчас я всю тебя заполню! "

    "[gg]" "Кончааааююююуу!!"
    "Кристи" "Я тоже, [gg], я тоже!!!"
    
    show white
    with Dissolve(.1)
    $ renpy.pause(.5, hard = True)
    scene image 'cg/ep9/picnic/sex/bg.png'
    show  cg_ep9_picnic_sex 5
    with Dissolve(.2)
    $ from_say_screen = False
    $ renpy.pause(.2, hard = True)
    $ renpy.pause(5)
    "Кристи" "Это так здорово… Я словно парю в облаках! "
    #"ext" "//Kristy_Sex_Park_3"

    "Кристи" "Я очень рада, что мой первый раз случился именно с тобой."
    "[gg]" "Но ведь последующие разы тоже будут только со мной."
    "Кристи" "Разумеется, хи-хи-хи!"

    scene black with Dissolve(.3)
    $ add_ach('ACH_15')
    $ time.time_now = "night"
    $ location_now = "City_Home"
    $ renpy.pause(.5, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_221
    show GG Jaket_Normal
    show GG Jaket_Normal:
        xalign 1.5

    show Christie Street_Normal
    show Christie Street_Normal:
        xalign 1.5
    with my_dissolve
    show Christie at go_from_left(xxalign = .8, ttimer = 2, xxzoom = -1)

    show GG at go_from_left(xxalign = .15, ttimer = 1)
    $ renpy.pause(.5, hard = True)
    #"ext" "//Park"
    #show Christie Street
    "Кристи" "Какой клёвый пикник."
    #show GG StreetNormal
    "[gg]" "Ага."
    #show Christie Street
    show GG:
        xalign .15
    show Christie Street_Normal:
        xalign .8 xzoom 1
    with my_dissolve
    "Кристи" "Теперь я буду думать только о том, чтобы повторить его."
    #show GG StreetNormal
    "[gg]" "Для этого нам необязательно выходить из дома."
    #show Christie StreetSmile
    "Кристи" "И даже вставать с кроватки, хи-хи!"
    #show GG StreetSmilel
    "[gg]" "Ха! Это точно."
   #"//Time" "Night"
    $ time.time_now = "night"
    

    
    
    scene black with Dissolve(.3)
    $ renpy.pause(.5, hard = True)
    
    $ add_to_gallery(37)
    if not from_gallery_check():
        $ descript_Christie = __("Наслаждаться отношениями с Кристи")
        $ Event("christie_root_64", "Corridor", day_start = time.day_now + 1)
    jump main_interface_label