label final_act_1_empty_hide_label:

    $ j = renpy.display.core.displayable_by_tag("master", "comic_frame_v3_master")
    $ i = list(j.get_placement()) + [j.xzoom, j.yzoom, j.zoom, j.alpha, j.xanchor, j.yanchor]
    
    $ store.comic_frame_v3_slave  = store.comic_frame_v3_master

    show image comic_frame_v3_master:
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
    show image comic_frame_v3_slave:
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
    return


label final_act_1_ease_back:
#getattr(store, "comic_frame_v2_"+str(main_comic_frame_v2), "#0000")
    
    show image comic_frame_v3_master: #comic_frame_v2_0:
        
        zoom 1.0
        xpos 2500
        ypos 214
        xanchor 0.0
        yanchor 0.0
        alpha .0
        parallel:
            easein .1 alpha 1.0 ypos 50
        parallel:
            ease_back .8 xpos 1499
    $ renpy.pause(.2, hard = True)
    return
label _final_act_1_wtf_comic:


    call comic_frame_v3_label(LiveComposite(
(195, 175),
(0, 0), Transform('comic_v3_frame', size=(163, 175)),
(30, 45), Text('{b}?!!{/b}', size = 80, font = _v3_font, ),
(159, 65), Transform('interface/comic_v2/comic_frame_tail_2.png', xzoom = 1.5, yzoom = 1.5)), 

show_label = "final_act_1_shake",
) from _call_comic_frame_v3_label_12 
    return
label final_act_1_shake:
#getattr(store, "comic_frame_v2_"+str(main_comic_frame_v2), "#0000")
    
    show image comic_frame_v3_master: #comic_frame_v2_0:
        
        zoom 1.0
        xpos 400
        ypos 410
        xanchor 0.0
        yanchor 0.0
        alpha .0
        parallel:
            ease .1 alpha 1.0 
        parallel:
            easein .5 xpos 200
        parallel:
            easein 0.1 ypos 435
            easein 0.1 ypos 431
            easein 0.1 ypos 435
            easein 0.1 ypos 431
            easein 0.1 ypos 435
            easein 0.1 ypos 431
            easein 0.1 ypos 435
            easein 0.1 ypos 431
            easein 0.1 ypos 435
            easein 0.1 ypos 431
            easein 0.1 ypos 435
            easein 0.1 ypos 431
            easein 0.1 ypos 435
    $ renpy.pause(.2, hard = True)
    return



label final_act_1_shake_2:
#getattr(store, "comic_frame_v2_"+str(main_comic_frame_v2), "#0000")
    
    show image comic_frame_v3_master: #comic_frame_v2_0:
        
        zoom 1.0
        xpos 200
        ypos 410
        xanchor 0.0
        yanchor 0.0
        alpha .0
        parallel:
            ease .1 alpha 1.0 
        #parallel:
        #    easein .5 xpos 200
        parallel:
            easein 0.1 ypos 435
            easein 0.1 ypos 431
            easein 0.1 ypos 435
            easein 0.1 ypos 431
            easein 0.1 ypos 435
            easein 0.1 ypos 431
            easein 0.1 ypos 435
            easein 0.1 ypos 431
            easein 0.1 ypos 435
            easein 0.1 ypos 431
            easein 0.1 ypos 435
            easein 0.1 ypos 431
            easein 0.1 ypos 435
    $ renpy.pause(.2, hard = True)
    return
image final_act_1 gg_on_bed = "cg/final_act/start/gg_on_bed.png"
image final_act_1_pistol    = "cg/final_act/start/pistol.png"

image final_act_1 james_christie = 'cg/final_act/start/james_christie.png'

label final_act_test:
    call final_act_setup from _call_final_act_setup_2
    jump main_interface_label 
label final_act_setup:
    if not hasattr(store, 'final_act_start'):
        $ descript = _("Вот и всё. Мои отношения с Мариной и Кристи достигли своего пика. Остаётся лишь наслаждаться жизнью и стараться не попадать в переделки.")
        $ Event(
            'final_act_1',  
            'GG_Room', 
            day_start = time.day_now + 1,
            time      = ['morning',], 
            )    
        $ final_act_start = True
    return

label final_act_1:    #Final_Act_1 (пусть будет в квесте Милфы)

    $ events.pop('final_act_1', 0)
    scene black
    show final_act_1 gg_on_bed
    show final_act_1 gg_on_bed:
        align (0.0, 0.0)

    if preferences.language in ('eng', 'spn', None, 'rus'):
        show image comic_frame_v3_master:
        
            zoom 1.0
            xpos 1900
            ypos 380
            xanchor 0.0
            yanchor 0.0
            alpha .0

            

        show image comic_frame_v3_slave:
            zoom 1.0
            xpos 300
            ypos 380
            xanchor 0.0
            yanchor 0.0
            alpha .0


    with my_dissolve
    $ renpy.pause(9999,)
    show final_act_1_pistol:
        alpha 0.0
        parallel:
            easein_cubic .75 alpha 1.0
        parallel:
            pos (0, 0)
            easein .1 pos (10, -5)
            easein .1 pos (5, 0)
            easein .1 pos (0, -5)
            easein .1 pos (10, -5)
            easein .1 pos (5, 0)
            easein .1 pos (0, -5)
            easein .1 pos (10, -5)
            easein .1 pos (5, 0)
            easein .1 pos (0, 0)
            repeat
    with my_vpunch
    #Руты Кристи и Марины должны быть завершены

    #Должно пройти 3 дня.

    #Активировать «лечь» спать ночью.



    #Brat_Return_1

    #//Звук натягивающегося курка


    if preferences.language in ('eng', 'spn', 'rus'):
        call comic_frame_v3_label(LiveComposite(
        (400, 224),
        (0, 0), Transform('comic_v3_frame', size=(378, 224)),
        (57, 35), Text("you doesn't", size = 45, font = _v3_font, ),
        (103, 88), Text('deserve', size = 45, font = _v3_font, ),
        (35, 141), Text('a quick death.', size = 45, font = _v3_font, ),
        (376, 73), 'interface/comic_v2/comic_frame_tail_2.png'), 
        m_xpos = 1428, 
        m_ypos = 527) from _call_comic_frame_v3_label 

        call comic_frame_v3_label(LiveComposite(
(380, 224),
(0, 0), Transform('comic_v3_frame', size=(358, 224)),
(35, 35), Text('You took my', size = 45, font = _v3_font, ),
(64, 88), Text('wife from', size = 45, font = _v3_font, ),
(132, 141), Text('me...', size = 45, font = _v3_font, ),
(356, 76), 'interface/comic_v2/comic_frame_tail_2.png'), 
m_xpos = 1448, 
m_ypos = 525) from _call_comic_frame_v3_label_2 

        call comic_frame_v3_label(LiveComposite(
(321, 118),
(0, 0), Transform('comic_v3_frame', size=(299, 118)),
(35, 35), Text('{i}Christie{/i}...', size = 45, font = _v3_font, ),
(297, 45), 'interface/comic_v2/comic_frame_tail_2.png'), 
m_xpos = 1485, 
m_ypos = 499) from _call_comic_frame_v3_label_4 

        call comic_frame_v3_label(LiveComposite(
(403, 224),
(0, 0), Transform('comic_v3_frame', size=(382, 224)),
(35, 35), Text('You trampled', size = 45, font = _v3_font, ),
(124, 88), Text('on my', size = 45, font = _v3_font, ),
(116, 141), Text('{i}{b}honor{/b}{/i}.', size = 45, font = _v3_font, ),
(379, 84), 'interface/comic_v2/comic_frame_tail_2.png'), 
m_xpos = 1451, 
m_ypos = 512) from _call_comic_frame_v3_label_6 

    elif preferences.language in (None, 'rus'):
        call comic_frame_v3_label(LiveComposite(
        (493, 300),
        (0, 0), Transform('comic_v3_frame', size=(405, 300)),
        (55, 45), Text('Быстрая смерть', size = 35, font = _v3_font, ),
        (128, 88), Text('была бы', size = 35, font = _v3_font, ),
        (45, 131), Text('слишком гуманна', size = 35, font = _v3_font, ),
        (100, 174), Text('для такого', size = 35, font = _v3_font, ),
        (57, 217), Text('подонка как ты.', size = 35, font = _v3_font, ),
        (402, 30), Transform('interface/comic_v2/comic_frame_tail_2.png', xzoom = 1.3, yzoom = 1.3)), 
        m_xpos = 1368, 
        m_ypos = 541) from _call_comic_frame_v3_label_1 

        call comic_frame_v3_label(LiveComposite(
(391, 204),
(0, 0), Transform('comic_v3_frame', size=(302, 204)),
(45, 40), Text('Ты отобрал', size = 35, font = _v3_font, ),
(90, 83), Text('у меня', size = 35, font = _v3_font, ),
(95, 126), Text('жену...', size = 35, font = _v3_font, ),
(300, 61), Transform('interface/comic_v2/comic_frame_tail_2.png', xzoom = 1.3, yzoom = 1.3)), 
m_xpos = 1470, 
m_ypos = 506) from _call_comic_frame_v3_label_3 
        
        call comic_frame_v3_label(LiveComposite(
(267, 138),
(0, 0), Transform('comic_v3_frame', size=(233, 138)),
(45, 50), Text('{i}Кристи{/i}...', size = 35, font = _v3_font, ),
(231, 42), Transform('interface/comic_v2/comic_frame_tail_2.png', xzoom = 1.5, yzoom = 1.5)), 
m_xpos = 1511, 
m_ypos = 504) from _call_comic_frame_v3_label_5 

        call comic_frame_v3_label(LiveComposite(
(280, 184),
(0, 0), Transform('comic_v3_frame', size=(246, 184)),
(45, 30), Text('И попрал', size = 35, font = _v3_font, ),
(81, 73), Text('мою', size = 35, font = _v3_font, ),
(69, 116), Text('{i}{b}честь{/b}{/i}.', size = 35, font = _v3_font, ),
(244, 53), Transform('interface/comic_v2/comic_frame_tail_2.png', xzoom = 1.5, yzoom = 1.5)), 
m_xpos = 1508, 
m_ypos = 518) from _call_comic_frame_v3_label_7 
    else:
        "None" "Быстрая смерть была бы слишком гуманна для такого подонка как ты."
        "None" "Ты отобрал у меня жену, Кристи и…"
        "None" "Попрал мою честь."



    show final_act_1 james_christie:
        align (0.0, 0.5)
        zoom 1.53
    hide final_act_1_pistol
    with my_dissolve


    if preferences.language in ('eng', 'spn'):
        call comic_frame_v3_label(LiveComposite(
(348, 277),
(0, 0), Transform('comic_v3_frame', size=(326, 277)),
(35, 35), Text('I probably', size = 45, font = _v3_font, ),
(58, 88), Text("should've", size = 45, font = _v3_font, ),
(38, 141), Text('beaten you', size = 45, font = _v3_font, ),
(44, 194), Text('to a pulp…', size = 45, font = _v3_font, ),
(324, 116), 'interface/comic_v2/comic_frame_tail_2.png'), 
m_xpos = 1507, 
m_ypos = 480) from _call_comic_frame_v3_label_8 

        call comic_frame_v3_label(LiveComposite(
    (394, 267),
    (0, 0), Transform('comic_v3_frame', size=(359, 267)),
    (92, 35), Text("But it's", size = 45, font = _v3_font, ),
    (81, 88), Text('not what', size = 45, font = _v3_font, ),
    (35, 141), Text("you're going", size = 45, font = _v3_font, ),
    (101, 194), Text('to do...', size = 45, font = _v3_font, ),
    (358, 39), Transform('interface/comic_v2/comic_frame_tail_2.png', xzoom = 1.5, yzoom = 1.5)), 
    
    show_label = "final_act_1_ease_back",
    hide_label = "final_act_1_empty_hide_label",
    ) from _call_comic_frame_v3_label_10 

    elif preferences.language in (None, 'rus'):
        call comic_frame_v3_label(LiveComposite(
(435, 220),
(0, 0), Transform('comic_v3_frame', size=(401, 220)),
(63, 30), Text('Мне стоило', size = 47, font = _v3_font, ),
(45, 85), Text('бы вышибить', size = 47, font = _v3_font, ),
(49, 140), Text('тебе мозги…', size = 47, font = _v3_font, ),
(399, 120), Transform('interface/comic_v2/comic_frame_tail_2.png', xzoom = 1.5, yzoom = 1.5)), 
m_xpos = 270, 
m_ypos = 535,

) from _call_comic_frame_v3_label_9 

    #Brat_Return_2

   
        call comic_frame_v3_label(LiveComposite(
    (394, 267),
    (0, 0), Transform('comic_v3_frame', size=(359, 267)),
    (116, 30), Text('Но ты', size = 45, font = _v3_font, ),
    (45, 83), Text('приготовил', size = 45, font = _v3_font, ),
    (96, 136), Text('что-то', size = 45, font = _v3_font, ),
    (112, 189), Text('иное...', size = 45, font = _v3_font, ),
    (358, 39), Transform('interface/comic_v2/comic_frame_tail_2.png', xzoom = 1.5, yzoom = 1.5)), 
    
    show_label = "final_act_1_ease_back",
    hide_label = "final_act_1_empty_hide_label",
    ) from _call_comic_frame_v3_label_11 
    else:
        "None" "Мне стоило бы вышибить тебе мозги…"

    show final_act_1 james_christie:
        parallel:
            easein_cubic 1.5 align (0.0, 0.0)
        parallel:
            easein_cubic .75 zoom 1.0 
    



    #//MyRoom_Night

    if preferences.language in ('eng', 'spn'):
        call comic_frame_v3_label(LiveComposite(
    (252, 128),
    (0, 0), Transform('comic_v3_frame', size=(252, 128)),
    (45, 40), Text('Right?', size = 45, font = _v3_font, ),
    (-31, 60), Transform('interface/comic_v2/comic_frame_tail_2.png', xzoom = -1.5, yzoom = 1.5)), 
    m_xpos = 1506, 
    m_ypos = 214,


    ) from _call_comic_frame_v3_label_13 

        call _final_act_1_wtf_comic from _call__final_act_1_wtf_comic
    elif preferences.language in (None, 'rus'):

        call comic_frame_v3_label(LiveComposite(
    (252, 128),
    (0, 0), Transform('comic_v3_frame', size=(252, 128)),
    (45, 40), Text('Верно?', size = 45, font = _v3_font, ),
    (-31, 60), Transform('interface/comic_v2/comic_frame_tail_2.png', xzoom = -1.5, yzoom = 1.5)), 
    m_xpos = 1506, 
    m_ypos = 214,


    ) from _call_comic_frame_v3_label_14 
    #//Catwoman_Window
    
        call _final_act_1_wtf_comic from _call__final_act_1_wtf_comic_1
    else:
        show Kat Invis
        show Kat Invis:
            xalign .85
        "Кристи" "Но ты приготовил что-то иное, верно?"
    scene black
    with my_vpunch
    $ time.time_now = 'night'
    $ renpy.pause(.75, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_239

    show Kat Normal
    
    show Kat Normal:
        xalign .85

    show Nikolaya Normal
    
    show Nikolaya Normal:
        xalign .1
        ypos 1080
        zoom .95
        xzoom -1
    
    with my_dissolve
    "Джеймс" "Ты ещё кто такая?!"
    ##show James Skepticism
    "Джеймс" "Очередная шлюшка моего брата?"
    show Kat Embarrassment
    with my_dissolve
    "Кэт" "Полегче, дядя."
    "Кэт" "Я считаю себя непревзойдённой и дико страстной шлюшкой!"
    ##show James Skepticism
    show shadow_full:
        alpha .0
        easein 3.5 alpha 1.0
    show Nikolaya:
        easein 5.5 zoom 1.0 xalign .5
    show Kat:
        easein 5.5 xalign 1.1
    "Джеймс" "Ну и что забыла здесь?"
    show shadow_full:
        easein .5 alpha 0.0
    show Nikolaya:
        parallel:
            easein_cubic 0.7 xalign .15 zoom .95
        parallel:
            easein .1 ypos 1089
            easein .1 ypos 1080
            easein .1 ypos 1089
            easein .1 ypos 1080
            easein .1 ypos 1089
            easein .1 ypos 1080
            
             
    show Kat:
        easein_cubic .7 xalign .5
        easeout .8 xalign .85
    "Кэт" "Слежу за тем, чтобы тупой мудак в смокинге держал себя в руках."
    ##show James Angry
    "Джеймс" "Отсюда возникает следующий вопрос - зачем? "
    "Кэт" "Ха!"
    "Кэт" "Сама задаюсь этим вопросом."
    "Кэт" "Можешь считать, что так я искупаю свою вину за былые грешки."
    ##show James Normal
    "Джеймс" "Защитница, получается."
    "Кэт" "Получается, что так."
    ##show James Normal
    "Джеймс" "По твоему, туша этого подлеца стоит того, чтобы впрягаться за него?"
    "Кэт" "Я прожила не менее сволочную жизнь, мистер Обиженка. "
    "Кэт" "Но [gg] другой."
    "Кэт" "Он вовремя одумался и сделал то, на что я не могла решиться долгие годы - завязал с криминальным миром.  "
    "Кэт" "Его сила воли вдохновила меня. И я последовала его примеру."
    "Кэт" "Теперь мы свободны, но умирать не планируем."

    "Кэт" "Так что иди своей дорогой, дядя. Оставь его в покое."
    ##show James Normal
    "Джеймс" "Вообще-то это мой дом."
    #show James Normal
    "Джеймс" "И я могу оставаться здесь столько, сколько пожелаю нужным."
    #show James Angry
    with my_vpunch
    "Джеймс" "Даже выгнать вас всех нахер!"
    "Кэт" "Ну так выгони наконец. "
    "Кэт" "Или прекрати этот спектакль."
    #show James Skepticism
    "Джеймс" "Это было бы слишком легко."
    "Кэт" "И что же ты собираешься делать?"
    #show James Skepticism
    "Джеймс" "Хех…"
    #show James Skepticism
    show shadow_full:
        alpha .5
    show Nikolaya:
        xzoom 1
    with my_dissolve
    "Джеймс" "Об этом [gg] узнает вскоре сам."
    "Кэт" "Какой грозный. "
    #show James Normal
    show shadow_full:
        easein 1.0 alpha 0.0
    show Nikolaya:
        xzoom 1
        easeout 3.5 xalign -1.2
    "Джеймс" "Не стану прощаться."
    "Кэт" "Пффф!"
    scene black
    with my_dissolve
    $ renpy.pause(1.5, hard = True)

    $ time.time_now = "morning"
 #   $ descript = _("Поспал и хватит.")
    $ block_time_forward_final_act_1 = copy.deepcopy(block_time_forward)
    $ block_time_forward = True
    $ Event(
        'final_act_2',  
        'Corridor', 
        )    

    $ debug_next('final_act_2_debug',)
    jump main_interface_label