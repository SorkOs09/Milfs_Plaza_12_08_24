image christie_root_41_jaybob 1 = Composite(
    (1920, 1080),
    (0, 0), 'locations/bg/City_Shop/morning.png',
    (0, 0), 'locations/bg/City_Shop/morning.png',
    (0, 0),'cg/ep89/shop/jaybob_1.png'
    )

image christie_root_41_jaybob 2 = Composite(
    (1920, 1080),
    (0, 0), 'locations/bg/City_Shop/morning.png',
    (0, 0), 'locations/bg/City_Shop/morning.png',
    (0, 0),'cg/ep89/shop/jaybob_2.png'
    )

image christie_root_41_jaybob 3 = Composite(
    (1920, 1080),
    (0, 0), 'locations/bg/City_Shop/morning.png',
    (0, 0), 'locations/bg/City_Shop/morning.png',
    (0, 0),'cg/ep89/shop/jaybob_3.png'
    )


image christie_root_41_officer_store_in = 'cg/ep89/shop/officer_store_in.png'

image christie_root_41_officer_masha 1 = 'cg/ep89/shop/officer_masha_1.png'

image christie_root_41_officer_masha 2 = 'cg/ep89/shop/officer_masha_2.png'


label christie_root_41:
    $ events.pop('christie_root_41', 0)


    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    scene black with Dissolve(.5)
    $ renpy.pause(.6, hard = True)

    scene expression 'cg/christie_root/Psi_Build.png'
    show expression 'cg/christie_root/officer_on_psi_build.png'

    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show Christie Harly_Normal
    show Christie Harly_Normal at go_from_right(xxalign=.65)

    show GG Joker_Normal
    show GG Joker_Normal at go_from_right(xxalign=1.0, xxzoom = -1)

    #Description: Пока не ясно, как скоро мы поймаем офицера на измене жене, зато можно запечатлеть его «грязные» поступки, которые, вероятно, нам тоже пригодятся.
    # "A Task" ""
    # #Активировать спрайт Офицера Утром у Дома Психолога.

    # "Scene" ""
    
    # "Scene" ""
    #Sprite_Officer

    #// Joker_Normal выезжают cправа

    #// Harly_Normal выезжают справа
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Кристи" "Он пунктуален как часы."
    show GG:
        xalign 1.0
        xzoom -1
    show Christie:
        xalign .65
    with my_dissolve
    "[gg]" "Так бывает, если дома тебе не рады."
    show Christie Harly_Chagrin:
        xzoom -1
    with my_dissolve
    "Кристи" "Мне начинает казаться, что он грешен во всём, кроме измены Сьюзен. "
    show GG Joker_WTF
    "[gg]" "Возможно, но с сегодняшнего дня мы станем фиксировать его поведение. "
    show Christie Harly_Normal
    "Кристи" "И почему мы раньше до этого не додумались?"
    show GG Joker_Normal
    "[gg]" "Ага."
    show Christie:
        xzoom 1
    
    hide expression 'cg/christie_root/officer_on_psi_build.png'
    show Officer Normal
    show Officer Normal:
        xalign .1
    with Dissolve(.5)
    if time.time_now == "evening":
        $ time.time_now = "afternoon"
    
    $ renpy.pause(.9, hard = True)

    show Officer:
        xzoom -1
        easein 1.2 xalign -1.0
    show GG:
        ease .8 xalign .3

    show Christie:
        ease .8 xalign .8
    $ renpy.pause(1, hard = True)


    show GG Joker_Surprise:
        xalign .3
        ease .8 xalign -1.6

    show Christie:
        xalign .8
        ease .8 xalign -1.8
    $ renpy.pause(.85)

label christie_root_41_mini_game:

    scene black with Dissolve(.5)


    $ renpy.pause(.5)

    scene image 'interface/city_interface/city_bg_'+time.time_now+'.png'
    #show image 'interface/city_interface/city_icon_gg.png'
    #show image 'interface/city_interface/city_icon_christie.png'
    
    show city_icon_jokers normal:
        xpos 1360 ypos 530 alpha .0
    
    show city_icon_officer:
        xpos 1360 ypos 530
    with Dissolve(.5)

    show city_icon_jokers normal:
        1.0
        linear .5 ypos 580 alpha 1.0
        easein 1.5 xpos 1200 ypos 540
    
    show city_icon_officer:
        linear .5 ypos 580

        easein_cubic 2.5 xpos 1000 ypos 400
    $ renpy.pause(2, hard = True)

    with vpunch
    if not renpy.call_screen('qte_mini_game', ttimer = 10, qte_line = 'rrr', shake = True):

        show city_icon_officer:
            xzoom -1
        with my_vpunch
        "Офицер" "Вы что, опять следите за мной?"
        "Офицер" "Ну всё, теперь вы просто так не отделаетесь..."

        scene image '#000' with my_dissolve
        
        menu:
            "Попробовать снова":

                jump christie_root_41_mini_game
            "Вернуться в главное меню":
                $ renpy.full_restart()

    show city_icon_jokers normal:
        
        easein .1 xpos 1260 ypos 500
    
    show city_icon_officer:
        xzoom -1

    
    with my_vpunch
    
    $ renpy.pause(1, hard = True)

    show city_icon_officer:
        xzoom 1
        easein_cubic 1 xpos 600 ypos 200 alpha 0.0

    show city_icon_jokers normal:
        .5
        easein .1 xpos 1200 ypos 540
        easein_cubic 1 xpos 600 ypos 200 alpha 0.0
    $ renpy.pause(.75, hard = True)

    


    scene black with Dissolve(.5)
    $ location_now  = 'City_Shop'
        

    call show_bg_image_label from _call_show_bg_image_label_189

    

    show christie_root_41_jaybob 2
    show christie_root_41_jaybob 2:
        xalign .5 yalign .5

    with Dissolve(.5)
    show Christie Harly_Skepticism
    show Christie Harly_Skepticism at go_from_right(xxalign=.8)


    show GG Joker_WTF
    show GG Joker_WTF at go_from_right(xxalign=1.15, xxzoom = -1)

    show shadow_full 
    with my_dissolve

    #//Спрайт Officer_JayBob

    #//Говорит с Зудилой и Бубнилой

    
    "Кристи" "С кем это он болтает?"
    
    "[gg]" "Зудило и Бубнило."
    show GG:
        xalign 1.15
        xzoom -1
    show Christie:
        xzoom -1
        xalign .8
    with my_dissolve
    "Кристи" "Ты знаешь этих ребят?"
    
    "[gg]" "В какой-то степени."
    show Christie:
        xzoom 1
    with my_dissolve
    "Кристи" "...."
    hide shadow_full 
    with my_dissolve
    if preferences.language in (None, 'eng', 'rus'):
        call screen comic_frame(__("Рыбный день, работяги?"), 170, 700, -1)
        call screen comic_frame(__("Раз на раз не приходится, офицер."), 300, 715, -1)
        
        call screen comic_frame(__("Прискорбно слышать это, мои дорогие друзья."), 170, 700, -1)
        call screen comic_frame(__("Надеюсь, ваши успехи никак не скажутся на нашем договоре."), 170, 700, -1)
        call screen comic_frame(__("Ну..."), 300, 715, -1)
        call screen comic_frame(__('Никаких "но". Жду полагающегося вознаграждения.'), 170, 700, -1)
    show christie_root_41_jaybob 3
    show shadow_full 
    with my_dissolve

    "Кристи" "Это же взятка! Взятка!"
    
    "Кристи" "Снимай!"
    
    "[gg]" "Снимаю-снимаю."
    
    hide shadow_full with my_dissolve
    
    call screen qte_mini_game_photo('christie_root_41_jaybob 3')

    show white with Dissolve(.05)


    play sound 'audio/photo_click.mp3'
    $ renpy.pause(1, hard = True)

    hide white with Dissolve(1)

    $ renpy.pause(1.25, hard = True)
    if preferences.language in (None, 'eng', 'rus'):
        call screen comic_frame(__("Здесь пятьдесят."), 300, 715, -1)
    show christie_root_41_jaybob 2
    with my_dissolve
    if preferences.language not in (None, 'eng', 'rus'):
        $ renpy.pause(9999)
    else:
        call screen comic_frame(__("Мне пересчитать?"), 170, 700, -1)
        call screen comic_frame(__("Как вам будет угодно."), 300, 715, -1)
        call screen comic_frame(__("Ха-ха-ха!"), 170, 700, -1)
        call screen comic_frame(__("Да верю я. Знаю, что не обманешь."), 170, 700, -1)
        call screen comic_frame(__("Ведь я могу вернуться, верно? И наказание за ложь будет жестокой."), 170, 700, -1)
        call screen comic_frame(__("Честнее нас только национальный банк, сэр!"), 300, 715, -1)
        call screen comic_frame(__("Хе-хе-хе. Жирного улова, господа."), 170, 700, -1)
        call screen comic_frame(__("Ага..."), 300, 715, -1)
    show christie_root_41_jaybob 1
    if preferences.language not in (None, 'eng', 'rus'):
        $ renpy.pause(9999)
    #//Officer_Normal исчезает влево

    hide expression 'cg/christie_root/officer_on_psi_build.png'
    show Officer Normal
    show Officer Normal:
        xalign .1
    with Dissolve(.5)
    
    $ renpy.pause(.9, hard = True)
    

    show Officer:
        xzoom -1
        easein 1.2 xalign -1.0

    $ renpy.pause(1, hard = True)

    hide Officer
    with my_dissolve
    
    "Кристи" "Куда это он?"
    show GG Joker_Surprise
    "[gg]" "Давай выяснять."
    #// Joker_Normal исчезает влево

    #// Harly_Normal исчезает влево

    show GG Joker_Surprise:
        ease .8 xalign -1.6

    show Christie:
        ease .8 xalign -1.8
    $ renpy.pause(.85)

    scene black with Dissolve(.5)

    $ renpy.pause(.75, hard = True)

    $ location_now = 'StoreIn'

    scene christie_root_41_officer_store_in
    with Dissolve(.5)


    #//Магазин

    #//Officer_Misha

    #//Joker_Normal выезжает слева

    #//Harly_Normal выезжает слева

    #show Christie Harly_Normal
    show GG Joker_WTF
    show Christie Harly_Skepticism
    show shadow_full 
    with my_dissolve
    show Christie Harly_Skepticism at go_from_left(xxalign=.01, xxzoom = -1)
    show GG Joker_WTF at go_from_left(xxalign=.2)
    "Кристи" "Он что, выбивает деньги у кассира?"
    #show GG Joker_Normal
    "[gg]" "Не похоже."
    show GG:
        xalign .2
    show Christie:
        xalign .01
        xzoom -1
    with my_dissolve
    #show GG Joker_Normal
    "[gg]" "Кажется, он покупает коробку конфет."
    #show Christie Harly_Normal
    with my_vpunch
    "Кристи" "Коробку конфет?!"
   # show GG Joker_Normal
    "[gg]" "Ага. И вполне вероятно не для Сьюзен."
   # show Christie Harly_Normal
    "Кристи" "Наконец-то!"
    #//Officer_Flower  
    hide shadow_full with Dissolve(.5)
    $ renpy.pause(.5, hard = True)


    call screen qte_mini_game_photo(
        'christie_root_41_officer_store_in', 
        x_pos = 1310, 
        y_pos = 200, 
        x_align = .87, 
        y_align = .62)

    show white with Dissolve(.05)


    play sound 'audio/photo_click.mp3'
    $ renpy.pause(1, hard = True)

    hide white with Dissolve(1)

    $ renpy.pause(1.25, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_190 

    show Officer Normal
    show Officer Normal:
        xalign .8
    show GG Joker_Normal
    show GG Joker_Normal:
        xalign .2
    show Christie Harly_Normal
    show Christie Harly_Normal:
        xzoom -1 xalign .01
    with Dissolve(.5)

    
    $ renpy.pause(.9, hard = True)
    
    show Officer:
        easein 1.2 xalign 2.2
    #//Officer_Flower исчезает вправо
    $ renpy.pause(.5, hard = True)
    hide Officer
    show GG Joker_Surprise:
        ease .8 xalign 1.6

    show Christie:
        ease .8 xalign 1.8

    $ renpy.pause(1, hard = True)

label christie_root_41_mini_game_2:

    scene black with Dissolve(.5)


    $ renpy.pause(.5)

    scene image 'interface/city_interface/city_bg_'+time.time_now+'.png'
    #show image 'interface/city_interface/city_icon_gg.png'
    #show image 'interface/city_interface/city_icon_christie.png'
    
    show city_icon_jokers normal:
        xpos 650 ypos 150 alpha 0.0

    
    show city_icon_officer:
        xzoom -1
        xpos 600 ypos 200
    with Dissolve(.25)

    $ renpy.pause(.25, hard = True)
    show city_icon_jokers normal:
        .25
        
        easein 1.5 xpos 620 ypos 240 alpha 1.0
    
    show city_icon_officer:
        easein 1.5 xpos 770 ypos 315
    $ renpy.pause(1, hard = True)

    with vpunch
    if not renpy.call_screen('qte_mini_game', ttimer = 13, qte_line = 'udrrlll', shake = True, invis = True):

        show city_icon_officer:
            xzoom 1
        with my_vpunch
        "Офицер" "Вы что, опять следите за мной?"
        "Офицер" "Ну всё, теперь вы просто так не отделаетесь..."

        scene black with my_dissolve
        
        menu:
            "Попробовать снова":

                jump christie_root_41_mini_game_2
            "Вернуться в главное меню":
                $ renpy.full_restart()

    show city_icon_jokers normal:
        
        easein .1 xpos 550 ypos 270 alpha 1.0
    
    show city_icon_officer:
        xzoom 1

    
    with my_vpunch
    
    $ renpy.pause(1, hard = True)

    show city_icon_officer:
        xzoom -1
        easein_cubic .5 xpos 770 ypos 300 alpha 0.0

    show city_icon_jokers normal:
        .5
        easein .1 xpos 620 ypos 240 alpha 1.0
        easein_cubic .5 xpos 770 ypos 300 alpha 0.0
    $ renpy.pause(1, hard = True)

    


    scene black with Dissolve(.5)
    #// Joker_Normal исчезает вправо

    #// Harly_Normal исчезает вправо

    
    #//Магазин одежды

    #//Officer_Flow_Woman

    #// Joker_Normal выезжают cправа

    #// Harly_Normal выезжают справа
    $ renpy.pause(1, hard = True)

    scene christie_root_41_officer_masha 2
    with my_dissolve
    show GG Joker_WTF
    show GG Joker_WTF at go_from_right(xxalign=1.1, xxzoom = -1)
    show Christie Harly_Skepticism
    show Christie Harly_Skepticism at go_from_right(xxalign=.9)

    call screen comic_frame(__("Я всю неделю сходил с ума, грезя о нашей встречи."), 870, 260)#офицеп
    call screen comic_frame(__("Хи-хи-хи!"), 80, 270, -1)
    call screen comic_frame(__("Люблю, когда ты сгораешь от нетерпения."), 80, 270, -1)
    call screen comic_frame(__("Надеюсь, мои страдания будут компенсированы с лихвой."), 870, 260)#офицеп
    call screen comic_frame(__("А то!"), 80, 270, -1)
    call screen comic_frame(__("Разве я когда-то разочаровывала тебя?"), 80, 270, -1)
    call screen comic_frame(__("Никогда. "), 870, 260)#офицеп
    call screen comic_frame(__("Хи-хи-хи. Твой возбуждённый голос так забавно дрожит."), 80, 270, -1)
    call screen comic_frame(__("Потрогай меня, фараон, я соскучилась по твоим ласкам. "), 80, 270, -1)

    call screen comic_frame(__("П-пожалуйста… Давай отойдём."), 870, 260)#офицеп
    call screen comic_frame(__("Ну… Не торопись. Разве ожидания того не стоят?"), 80, 270, -1)
    call screen comic_frame(__("Хватит этих прелюдий, шоколадка, я хочу перейти к делу. "), 870, 260)#офицеп
    call screen comic_frame(__("Люблю твою напористость!"), 80, 270, -1)
    #show Christie Harly_Normal
    
    show GG:
        xalign 1.1
        xzoom -1
    
    show Christie:
        xalign .9
    

    show shadow_full 
    with my_dissolve
    "Кристи" "Эй, гляди, мне кажется или полицейский реально флиртует с продавщицей одежды?"
    #show GG Joker_Normal
    "[gg]" "Вроде того."
    hide shadow_full with my_dissolve
    
    call screen qte_mini_game_photo(
        'christie_root_41_officer_masha 2',
        x_pos = 600, 
        y_pos = 200, 
        x_align = .4, 
        y_align = .62)

    show white with Dissolve(.05)


    play sound 'audio/photo_click.mp3'
    $ renpy.pause(1, hard = True)

    hide white with Dissolve(1)

    $ renpy.pause(1.25, hard = True)

    show shadow_full 
    with my_dissolve

    "Кристи" "Поймался, голубчик!"
    #show GG Joker_Normal
    "[gg]" "Заснять, как он просто болтает с девушкой мало. Нужно запечатлеть хотя бы поцелуй."
    #show Christie Harly_Normal
    "Кристи" "Тогда ждём."
    #// Officer_Flow_Woman исчезает
    scene image 'images/locations/bg/ClothesStore/afternoon.png'
    show GG Joker_WTF
    show GG Joker_WTF: 
        xalign 1.1 xzoom -1 ypos 1085

    show Christie Harly_Skepticism
    show Christie Harly_Skepticism: 
        xalign .9 ypos 1085

    with Dissolve(.5)
    #//BlackW_Normal

    #show Blackw Normal
    show Masha Normal
    show Masha Normal at go_from_left(xxalign=.2, xxzoom = -1)

    
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Маша" "Извините, но мы уже закрываемся."
    #show GG Joker_Normal
    "[gg]" "Но ещё довольно рано."
    
    show Masha Angry:
        xalign .2
        xzoom -1
    with my_dissolve
    #show Blackw Normal
    "Маша" "У нас переучёт. Прошу вас покинуть помещение."
    #show GG Joker_Normal
    "[gg]" "Как скажете..."
    show Christie Harly_Normal:
        xzoom 1
        easein_cubic 4 xalign -2.0

    show GG Joker_Normal:
        xzoom -1
        easein_cubic 4 xalign -2.0
    $ renpy.pause(1, hard = True)
    #//Joker_Normal исчезает влево

    #//Harly_Normal исчезает влево
    scene black
    with Dissolve(.5)
    $ location_now = 'City_Home'
    $ time.time_now = 'evening'
    $ renpy.pause(.5, hard = True)

    call show_bg_image_label from _call_show_bg_image_label_191

    with Dissolve(.5)
    
    show GG Joker_Normal
    show GG Joker_Normal at go_from_left(xxalign=.15)

    show Christie Harly_Normal
    show Christie Harly_Normal at go_from_left(xxalign=.85, xxzoom = -1)
    #"Time" "Evening"
    $ renpy.pause(1, hard = True)

    #//

    #//Joker_Normal выезжает слева

    #//Harly_Normal выезжает слева

    "[gg]" "Да, теперь мы наверняка знаем, с кем у него роман."
    show GG Joker_Passion:
        xalign .15
    with my_dissolve
    "[gg]" "Остаётся лишь заснять, как они лебезятся друг с другом."
    show Christie Harly_Surprise:
        xalign .85 xzoom 1
    with my_dissolve
    "Кристи" "Проникнуть в закрытое помещение?"
    show Christie Harly_Chagrin
    show GG Joker_Chagrin
    with my_dissolve
    "Кристи" "Это... Противозаконо."
    show Christie Harly_Normal
    "Кристи" "[gg], пожалуйста, только без криминала."
    show GG Joker_Normal
    "[gg]" "Понимаю."
    show GG Joker_Normal
    "[gg]" "Поэтому и думаю над тем, чтобы избежать этой участи."
    show Christie Harly_Skepticism
    "Кристи" "Но разве у нас есть выход?"
    show GG Joker_Smile
    "[gg]" "Выход есть всегда."
    show Christie Harly_Normal
    "Кристи" "Хм..."
    show Christie Harly_Normal
    "Кристи" "Ты прав, сдаваться так легко нельзя."
    show Christie Harly_Smile
    "Кристи" "А что, если мы заранее спрячемся в одной из комнат для переодевания?"
    show GG Joker_Normal
    "[gg]" "Звучит как план. Только вот..."
    show Christie Harly_Angry
    "Кристи" "Ну что опять?! Неужели я настолько тупая, что не в состоянии даже план придумать?"
    #Joker_Normal 
    show GG Joker_Please
    with my_dissolve
    "[gg]" "Нет. Дело в другом."

    show GG Joker_Normal
    show Christie Harly_Embarrassment
    with my_dissolve
    "[gg]" "Велик шанс, что прежде чем магазин закроют, продавщица перепроверит все коморки."
    show Christie Harly_Normal
    "Кристи" "А если туалет?"
    show GG Joker_WTF
    "[gg]" "А вот это уже более реально, но всё ещё довольно рисковано."
    show Christie Harly_Laughs
    "Кристи" "Насколько рисковано? Они что, в туалете уеденяться будут?"
    show Christie Harly_Normal
    show GG Joker_Smile
    with my_dissolve
    "Кристи" "В их распоряжении целый магазин!"
    show GG Joker_Normal
    "[gg]" "Вау, спокойно. Кажется ты словила кураж."
    show Christie Harly_Angry
    "Кристи" "Не томи. Я стараюсь помочь."
    show GG Joker_Normal
    "[gg]" "Даже если дверь не окажется скрипучим дерьмом, оповещающей о новом посетителе за десять километров..."
    show GG Joker_Normal
    "[gg]" "А замок или слишком лёгкий, или вообще не нуждается во взломе..."
    show GG Joker_Normal
    "[gg]" "Да и сама дверь буквально на распашку..."
    show Christie Harly_Normal
    "Кристи" "Нууууууу?"
    show GG Joker_Normal
    "[gg]" "Чтобы зайти туда незаметно, кто-то должен отвлечь продавщицу, а это значит, внутри сможет оказаться только один."
    show Christie Harly_Smile
    show GG Joker_Surprise
    with my_dissolve
    "Кристи" "Всего-то? Я отвлеку, а ты проникнешь."
    show GG Joker_Please
    "[gg]" "Уверена?"
    show Christie Harly_Skepticism
    "Кристи" "Боишься, что не справлюсь?"
    show GG Joker_Embarrassment
    "[gg]" "Формально, ты будешь соучастницей преступления."
    show GG Joker_Normal
    show Christie Harly_Smile
    with my_dissolve
    "[gg]" "Это, конечно, в том случае, если меня поймают и позже перепроверят камеры наблюдения."
    show Christie Harly_Normal
    "Кристи" "Умеешь же ты всё вывернуть..."
    show GG Joker_Normal
    "[gg]" "Ввожу в курс дела, Кристи."
    show GG Joker_WTF
    "[gg]" "Да, это не взлом с проникновением, но тоже... сомнительная деятельность с точки зрения закона."
    show GG Joker_WTF
    "[gg]" "Я не хочу манипулировать тобой, вот и говорю как есть."
    show Christie Harly_Laughs
    "Кристи" "Мило."
    show Christie Harly_Passion
    with my_dissolve
    "Кристи" "Но оставим вопросы морали на потом. Я готова отвлечь!"
    show GG Joker_Smile
    "[gg]" "Тогда по рукам."
    show Christie Harly_Normal
    "Кристи" "По рукам и ногам! Хи-хи-хи!"
    #// Harly_Normal исчезает вправо

    show Christie Harly_Normal: 
        xzoom -1
        easein_cubic 2 xalign 1.5 

    show GG Joker_Normal:
        easein_cubic 1.5 xalign .5
    $ renpy.pause(1, hard = True)
    
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "[gg]" "Прежде чем продолжать нашу слежку, нужно навестить Игоря в Парке."
    "[gg]" "В тот раз мент обошёлся с ним довольно грубо, а я так и не поддержал его в трудную минуту. "
    hide Christie
    show GG Joker_Normal:
        xalign .5
    with my_dissolve
    
    "[gg]" "Ему определённо не помешает моральная поддержка. "
    
    "[gg]" "Да и запись, где полицейский берёт взятку обрадует моего друга. "

    $ descript_Christie = _('Проведать Игоря в Парке и показать ему запись с продажным копом.')
    if getattr(store, 'block_igor_position', False):

        $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")


    $ Event('christie_root_42', 'Igor', day_start = time.day_now + 1, time = ['morning', 'afternoon'])

    jump main_interface_label