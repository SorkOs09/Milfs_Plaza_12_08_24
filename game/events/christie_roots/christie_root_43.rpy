image christie_root_43 lock_bg = 'cg/ep89/masha/lock_bg.png'


image christie_root_43_masha_sex 1z = 'cg/ep89/masha/sex/1z.png'
image christie_root_43_masha_sex 2z = 'cg/ep89/masha/sex/2z.png'
image christie_root_43_masha_sex 3z = 'cg/ep89/masha/sex/3z.png'



image christie_root_43_masha_sex 1c = 'cg/ep89/masha/sex/1c.png'
image christie_root_43_masha_sex 2c = 'cg/ep89/masha/sex/2c.png'
image christie_root_43_masha_sex 3c = 'cg/ep89/masha/sex/3c.png'
image christie_root_43_masha_sex 4c = 'cg/ep89/masha/sex/4c.png'
image christie_root_43_masha_sex 5c = 'cg/ep89/masha/sex/5c.png'
image christie_root_43_masha_sex 6c = 'cg/ep89/masha/sex/6c.png'
image christie_root_43_masha_sex 7c = 'cg/ep89/masha/sex/7c.png'
image christie_root_43_masha_sex 8c = 'cg/ep89/masha/sex/8c.png'



image christie_root_43_pen 1:






    'cg/ep89/masha/sex/1t.png'
    .25
    'cg/ep89/masha/sex/2t.png'
    .25
    'cg/ep89/masha/sex/3t.png'
    .25
    'cg/ep89/masha/sex/4t.png'
    .25
    'cg/ep89/masha/sex/5t.png'
    .25
    'cg/ep89/masha/sex/4t.png'
    .25
    'cg/ep89/masha/sex/3t.png'
    .25
    'cg/ep89/masha/sex/2t.png'
    .25


    repeat



image christie_root_43_pen 2:







    'cg/ep89/masha/sex/1t.png'
    .17
    'cg/ep89/masha/sex/2t.png'
    .17
    'cg/ep89/masha/sex/3t.png'
    .17
    'cg/ep89/masha/sex/4t.png'
    .17
    'cg/ep89/masha/sex/5t.png'
    .17
    'cg/ep89/masha/sex/4t.png'
    .17
    'cg/ep89/masha/sex/3t.png'
    .17
    'cg/ep89/masha/sex/2t.png'
    .17




    repeat


image christie_root_43_pen 3:







    'cg/ep89/masha/sex/1t.png'
    .12
    'cg/ep89/masha/sex/2t.png'
    .12
    'cg/ep89/masha/sex/3t.png'
    .12
    'cg/ep89/masha/sex/4t.png'
    .12
    'cg/ep89/masha/sex/5t.png'
    .12
    'cg/ep89/masha/sex/4t.png'
    .12
    'cg/ep89/masha/sex/3t.png'
    .12
    'cg/ep89/masha/sex/2t.png'
    .12



    repeat



image christie_root_43_pen 4:






    'cg/ep89/masha/sex/1t.png'
    .1
    'cg/ep89/masha/sex/2t.png'
    .1
    'cg/ep89/masha/sex/3t.png'
    .1
    'cg/ep89/masha/sex/4t.png'
    .1
    'cg/ep89/masha/sex/5t.png'
    .1
    'cg/ep89/masha/sex/4t.png'
    .1
    'cg/ep89/masha/sex/3t.png'
    .1
    'cg/ep89/masha/sex/2t.png'
    .1



    repeat






image christie_root_43_sex 1:






    'cg/ep89/masha/sex/1.png'
    .25
    'cg/ep89/masha/sex/2.png'
    .25
    'cg/ep89/masha/sex/3.png'
    .25
    'cg/ep89/masha/sex/2.png'
    .25


    repeat



image christie_root_43_sex 2:







    'cg/ep89/masha/sex/1.png'
    .17
    'cg/ep89/masha/sex/2.png'
    .17
    'cg/ep89/masha/sex/3.png'
    .17
    'cg/ep89/masha/sex/2.png'
    .17




    repeat


image christie_root_43_sex 3:







    'cg/ep89/masha/sex/1.png'
    .12
    'cg/ep89/masha/sex/2.png'
    .12
    'cg/ep89/masha/sex/3.png'
    .12
    'cg/ep89/masha/sex/2.png'
    .12



    repeat



image christie_root_43_sex 4:






    'cg/ep89/masha/sex/1.png'
    .1
    'cg/ep89/masha/sex/2.png'
    .1
    'cg/ep89/masha/sex/3.png'
    .1
    'cg/ep89/masha/sex/2.png'
    .1



    repeat




image christie_root_43 door_bg  = Composite(
    (1920, 1080),
    (0, 0), 'characters/Christie/emo/Normal.png',
    (0, 0), Transform('characters/Masha/emo/Normal.png', xzoom = -1),

    )




image christie_root_43 door_bg_2  = Composite(
    (1920, 1080),
    (0, 0), 'characters/Christie/emo/Normal.png',
    

    )


image christie_root_43 gg_masha_0 = 'cg/ep89/masha/gg_masha_0.png'


image christie_root_43 gg_masha_1 = 'cg/ep89/masha/gg_masha_1.png'


image christie_root_43 gg_masha_2 = 'cg/ep89/masha/gg_masha_2.png'


image christie_root_43 gg_bg = 'cg/ep89/masha/gg_bg.png'


label christie_root_43:
    
    $ events.pop('christie_root_43', 0)

    scene image 'locations/bg/ClothesStore/afternoon.png'
    show image 'cg/ep89/shop/masha.png'
    with Dissolve(.5)
    show Christie Harly_Normal
    show Christie Harly_Normal at go_from_right(xxalign=.8)

    show GG Joker_Normal
    show GG Joker_Normal at go_from_right(xxalign=1.1, xxzoom = -1)

    #Description: 
    #Отправиться в магазин одежды. Желательно днём. Следует отвлечь продавщицу и проникнуть в туалетную комнату.
    # "A Task" ""


    # #Активировать продавщицу одежды (я сделаю спрайт, атвичаю!111)




    # "Scene" ""
    
    "Кристи" "Мы не слишком рано?"
    show GG:
        xalign 1.1
        xzoom -1
    show Christie:
        xalign .8
    with my_dissolve
    "[gg]" "Нет. Примерно через час, если я правильно всё рассчитал, явится муж Сьюзен."
    "Кристи" "Ухххх…"
    show Christie Harly_Chagrin:
        xzoom -1
    with my_dissolve
    "Кристи" "Я очень волнуюсь, [gg]."
    show GG Joker_WTF
    "[gg]" "Голос дрожит?"
    show Christie Harly_Embarrassment
    "Кристи" "Вроде бы нет…"
    show GG Joker_Please
    "[gg]" "Потливость?"
    show Christie Harly_Passion
    "Кристи" "Тяжело сказать…"
    show GG Joker_Smile
    "[gg]" "Первичный осмотр показывает, что ты в полном порядке, хе-хе."
    show Christie Harly_Normal
    "Кристи" "Ну спасибо, доктор. Вы меня успокоили."
    show GG Joker_Normal
    "[gg]" "Давай лучше сосредоточимся на нашей миссии."
    show Christie Harly_Normal
    "Кристи" "Хорошо…"
    show Christie Harly_Normal
    "Кристи" "Надеюсь, у меня всё получится."
    show GG Joker_Normal
    "[gg]" "Сто процентов!"
    show GG Joker_Normal
    "[gg]" "Обрати внимание, Кристи. Продавщица всё время у кассы. "
    show GG Joker_Normal
    "[gg]" "Хотя в основном она донимает всех своих клиентов."
    show Christie Harly_Skepticism
    "Кристи" "Часто тут бываешь?"
    show GG Joker_Embarrassment
    "[gg]" "Приходилось."
    show GG Joker_Smile
    "[gg]" "Могу точно сказать, что сегодня эта девица халтурит."
    show Christie Harly_Surprise
    "Кристи" "Дожидается полицейского?"
    show GG Joker_Normal
    show Christie Harly_Normal
    with my_dissolve
    "[gg]" "Ага."
    show GG Joker_Normal
    "[gg]" " Все её мысли поглощены предстоящей встречей."
    show GG Joker_Normal
    "[gg]" "А это значит, что тебе легко будет её разговорить."
    show Christie Harly_Normal
    "Кристи" "Эй, подкинь хотя бы пару тем для беседы!"
    show GG Joker_Normal
    "[gg]" " Ты что, серьёзно? Я понятия не имею, о чём треплятся девочки, и уж тем более - как с ними знакомиться!"
    show Christie Harly_Normal
    "Кристи" "Я не планирую с ней знакомиться."
    show Christie Harly_Normal
    "Кристи" "Спрошу её по одежде, возможно..."
    show GG Joker_Surprise
    "[gg]" "Нет! Ни в коем случае!"
    show GG Joker_WTF
    "[gg]" "Как только ты спросишь её по работе, она тут же сорвётся с места и пойдёт показывать тебе одежду."
    show GG Joker_WTF
    "[gg]" "Она может заметить меня."
    show Christie Harly_Normal
    "Кристи" "Хм..."
    show Christie Harly_Normal
    "Кристи" "Ладно. Что-то придумаю."
    show GG Joker_Normal
    "[gg]" " Так ты идёшь?"
    show Christie Harly_Normal
    "Кристи" "Иду-иду."
    
    #//Kristy_Black
    show Christie:
        xzoom 1
        easein 1 xalign .65

    "Кристи" "Простите..."

    hide image 'cg/ep89/shop/masha.png'
    with my_dissolve
    show Masha Normal
    show Masha Normal at go_from_left(xxalign = .0, xxzoom = -1)
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/bubnila.mp3', fadein = 1.5)
    "Маша" "О!"
    "Маша" "Да-да-да."
    show Masha Smile:
        xalign .0
        xzoom -1
    with my_dissolve
    "Маша" "Я в полном вашем распоряжении!"
    "Маша" "Я вас сразу приметила, ещё на входе."
    show Christie Harly_Surprise:
        xzoom 1
        xalign .65
    with my_dissolve
    "Маша" "Вы... Ну, я знакома с вашим родом деятельности и понимаю, как важно соответствовать правильному имиджу."
    "Маша" "Ведь ваша внешность - это ваша витрина. А всякий, кого она, то есть вы, заинтересовали, с радостью воспользуется вашими профессиональными услугами. "
    "Кристи" "Ч-чего?"
    show Christie Harly_Skepticism
    with my_dissolve
    show GG Joker_Smile
    with my_dissolve
    "Кристи" "Кем, по-вашему, я работаю?"
    show Masha Surprise
    with my_dissolve
    "Маша" "Тссссс."
    "Маша" "Простите ради Бога, я, наверное, говорила слишком громко!"
    "Маша" "Девушки вашей профессии явно не желают лишней огласки, я правильно понимаю?..."
    "Кристи" "Э...."
    "Кристи" "Неужели я настолько плохо одета?"
    "Маша" "О нет, что вы! Очень даже напротив."
    show Christie Harly_Smile
    with my_dissolve
    show Masha Passion
    with my_dissolve
    "Маша" "Вы выглядите неотразимо. Потрясающе. Со знанием вкуса. Стиля. С ярким отпечатком эпохи нашего времени."
    "Маша" "Точнее, даже - вашего времени!"
    "Маша" "Поверьте, вы по адресу!"
    
    show GG Joker_Normal
    "[gg]" "Что ж... Кажется, у Кристи неплохо получилось её заболтать."
    show GG Joker_Normal
    "[gg]" "Теперь мой выход."
    show GG:
        xzoom 1
        easein 1 xalign 1.7
    $ renpy.pause(1, hard = True)
    #//Normal исчезает вправо

    #//Спрайт со взломом двери
    scene black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)

    scene christie_root_43 lock_bg
    
    with my_dissolve
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Самый примитивный замок."
    "[gg]" "Хотя бы здесь повезло…"
    #//Мини-игра по взлому
    $ Hide('lock_pick_screen', transition = Dissolve(.5))()

    $ renpy.music.stop(fadeout=1.5)

    $ lockergame = LockerGame(lvl = 1, image_now = 'images/mini_games/lock_mini_game/locker.png')

    play music 'audio/mini_game.mp3' fadein 1.5

    call screen LockerGameScreen

    $ Hide('main_interface')()

    play sound 'audio/lock.ogg'

    $ renpy.pause(.5, hard = True)

    #//Туалет

    #//Туалет устроен так слева дверь, по центру унитаз, справа умывальник

    "[gg]" "Что ж, это было довольно просто."
    "[gg]" "Хм…"
    "[gg]" "Чёрт, ну и душно же здесь. "
    "[gg]" "Кажется, вентиляция совсем пришла в негодность. "
    "[gg]" "Придётся снять с тебя этот дурацкий костюм... хотя бы на время."
    
    scene black
    with Dissolve(.5)

    play sound 'audio/change_clothes.mp3'

    $ renpy.pause(.5)

    scene christie_root_43 gg_bg
    with my_dissolve
    
    "[gg]" "Где здесь выключатель?.. Ага. Вот."
    "[gg]" "Чёрт, лампочка перегорела."
    "[gg]" "Придётся сидеть впотьмах."
    "[gg]" "Как бы у меня после такого клаустрофобия не развилась…"
    #//От первого лица показать дверной проём, где ГГ наблюдает за беседой Кристи и Продавщицы.


    scene black with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    
    scene image 'locations/bg/ClothesStore/afternoon.png'
    
    show Christie Harly_Normal
    show Christie Harly_Normal:
        xalign .7

    show Masha Normal
    show Masha Normal:
        xzoom -1
        xalign .3

    show expression 'cg/christie_root/falos/0.png'
    show expression 'cg/christie_root/falos/1_0.png'
    with Dissolve(.5)

    hide expression 'cg/christie_root/falos/1_0.png'

    
    call screen christie_root_30_screen(1, 'cg/christie_root/falos/1_0.png')
    show expression 'cg/christie_root/falos/1_0.png'
    with None
    show expression 'cg/christie_root/falos/1_1.png':
        xpos 0
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    hide expression 'cg/christie_root/falos/1_0.png'
    call screen christie_root_30_screen(2, 'christie_root_43 door_bg')
    show expression 'cg/christie_root/falos/1_1.png':
        xpos 0
        easein_cubic 1.5 xpos -800
    $ renpy.pause(1.8, hard = True)
    show expression 'cg/christie_root/falos/1_1.png':
        xpos -800
    with my_dissolve
    # scene image 'locations/bg/ClothesStore/afternoon.png'
    
    # show Christie Harly_Normal
    # show Christie Harly_Normal:
    #     xalign .5

    # show Masha Normal
    # show Masha Normal:
    #     xzoom -1
    #     xalign .0

    # show expression 'cg/christie_root/falos/0.png'
    # with my_dissolve



    "" "Хе-хе-хе."
    "" "Воркуют, птички."


    "" "Кристи сработала идеально."

    "" "Скорее бы уже пришёл полицейский, здесь слишком душно…"
    
    #//
    # scene christie_root_43 door_bg_2
    # show Masha Normal
    # with my_dissolve
    # show Masha Normal:
    #     zoom 1.0
    #     xpos 0
    #     easein 10 zoom 20
    show Masha:
        easein .75 xalign .5
    show Christie:
        easein .75 xalign .8
    $ renpy.pause(.8, hard = True)
    show Christie:
        xalign .8
    show Masha Walk:
        xzoom 1 zoom 1.0 xalign .5
        
        .75
        xzoom -1 zoom 1.05
        
        .75
        xzoom 1 zoom 1.1
        
        .75
        xzoom -1 zoom 1.15
        
        .75
        xzoom 1 zoom 1.2
        
        .75
        xzoom -1 zoom 1.25
        
        .75
        xzoom 1 zoom 1.3
        
        .75
        xzoom -1 zoom 1.35
        
        .75
        xzoom 1 zoom 1.4
        
        .75
        xzoom -1 zoom 1.45
        
        .75
        xzoom 1 zoom 1.5
        
        .75
        xzoom -1 zoom 1.55
        
        .75
        xzoom 1 zoom 1.6
        
        .75
        xzoom -1 zoom 1.65
        
        .75
        
        
    with my_dissolve
    "" "Какого…?!!"
    
    "" "Она что, идёт сюда?!"


    "" "Этого я никак не предусмотрел!"



    scene black
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show image 'cg/ep89/masha/gg_0.png'
    show image 'cg/ep89/masha/gg_0.png':
        xpos 800
        alpha .0
    show image 'cg/ep89/masha/gg_1.png'
    show image 'cg/ep89/masha/gg_1.png':
        xpos 800
        alpha .0 
    show image 'cg/ep89/masha/gg_masha_0.png'
    show image 'cg/ep89/masha/gg_masha_0.png':
        xpos 800

    show image 'cg/ep89/masha/gg_masha_1.png'
    show image 'cg/ep89/masha/gg_masha_1.png':
        xpos 800 alpha 0.0

    show image 'cg/ep89/masha/gg_masha_2.png'
    show image 'cg/ep89/masha/gg_masha_2.png':
        xpos 800 alpha 0.0

    show image 'cg/ep89/masha/masha_0.png'
    show image 'cg/ep89/masha/masha_0.png':
        xpos 800 alpha 0.0

    show image 'cg/ep89/masha/masha_1.png'
    show image 'cg/ep89/masha/masha_1.png':
        xpos 800 alpha 0.0

    with my_dissolve



    $ renpy.pause(1.2, hard = True)


    show image 'cg/ep89/masha/gg_0.png':
        easeout .8 xpos 1370#alpha 0.0
    show image 'cg/ep89/masha/gg_1.png':
        easeout .8 xpos 1370#alpha 0.0
    show image 'cg/ep89/masha/gg_masha_0.png':
        easeout .8 xpos 1370#alpha 0.0
    show image 'cg/ep89/masha/gg_masha_1.png':
        easeout .8 xpos 1370 #alpha 1.0
    show image 'cg/ep89/masha/gg_masha_2.png':
        easeout .8 xpos 1370
    show image 'cg/ep89/masha/masha_0.png':
        easeout .8 xpos 1370
    show image 'cg/ep89/masha/masha_1.png':
        easeout .8 xpos 1370
    $ renpy.pause(.9, hard = True)

    show image 'cg/ep89/masha/gg_0.png':
        xpos 1370 #alpha 0.0
    show image 'cg/ep89/masha/gg_1.png':
        xpos 1370 #alpha 0.0
    
    show image 'cg/ep89/masha/gg_masha_0.png':
        xpos 1370 alpha 0.0
    show image 'cg/ep89/masha/gg_masha_1.png':
        xpos 1370 alpha 1.0
    show image 'cg/ep89/masha/gg_masha_2.png':
        xpos 1370
    show image 'cg/ep89/masha/masha_0.png':
        xpos 1370
    show image 'cg/ep89/masha/masha_1.png':
        xpos 1370
    with my_vpunch
    $ renpy.pause(1, hard = True)


    show image 'cg/ep89/masha/gg_masha_2.png':
        alpha .0
    show image 'cg/ep89/masha/gg_masha_1.png':
        alpha .0
    show image 'cg/ep89/masha/gg_masha_0.png':
        alpha .0
    
    show image 'cg/ep89/masha/gg_1.png':
        alpha 1.0
        
    show image 'cg/ep89/masha/masha_0.png':
        alpha 1.0

    with Dissolve(.25)

    $ renpy.pause(.5, hard = True)
    show image 'cg/ep89/masha/masha_0.png':
        easein 2 xpos 800 alpha 0.0

    show image 'cg/ep89/masha/masha_1.png':
        easein 2 alpha 1.0

    show image 'cg/ep89/masha/gg_0.png':
        easein .5 alpha 1.0
    show image 'cg/ep89/masha/gg_1.png':
        easein .5 alpha 0.0

    $ renpy.pause(2.5, hard = True)
    #//Тут я нарисую спрайт и увеличу несколько раз, 
    #чтобы ты потом сделал анимацию из 4-5 слайдов, будто бы она приближается

    #//Продавщица зашла, но незаметила ГГ, сидящего на унитазе в полном узумлении

    #//Снимает штаны

    #//Снимает снимает трусы

    #//Садится на ГГ
    scene image 'cg/ep89/masha/sex/0.png'
    with my_vpunch
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Маша" "Ай?!"

    "Маша" "Чёрт, ты меня испугал."
    "Маша" "Для копа ты ведёшь себя слишком развязно, тебе так не кажется?"
    "Маша" "Но мне нравится, как ты решил похулиганить сегодня."
    "Маша" "Подстеречь меня в уборной… ха! До такого мог додуматься или полный гений, или абсолютный извращенец. "
    "Маша" "Хотя мы оба знаем, кем являешься ты, хи-хи-хи."
    "Маша" "Мне импонирует твоя непредсказуемость."
    "Маша" "Ты такой интригующий.  "
    #//мысли
    show shadow_full with my_dissolve
    "[gg]" "{i}Кажется, она думает, будто бы я полицейский…{/i}"
    "[gg]" "{i}Мне ничего не остаётся кроме как подыграть ей.{/i}"
    #//конец мысли

    hide shadow_full with my_dissolve

    "Маша" "Если уж ты решил устроить мне сюрприз во время рабочего графика, будь добр не задерживать меня сильно."
    "Маша" "Клиенты ждут, знаешь ли…"
    "Маша" "Давай, снимай штаны. Мои киска желает полакомиться твоим дружком."
    #//мысли

    show shadow_full with my_dissolve
    "[gg]" "{i}Она серьёзно?!!{/i}"
    "[gg]" "{i}Не могу же я просто взять и… Или могу?{/i}"
    "[gg]" "{i}Раз уж она уверена, что я коп, то, вероятно, ожидает и соответствующих действий. {/i}"
    "[gg]" "{i}Противиться нельзя. Придётся идти до конца.{/i}"

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/aerosol-of-my-love-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    #//конец мысли
    show image '#000a'
    show christie_root_43_masha_sex 1z
    #show image 'cg/ep89/masha/sex/panel.png'
    with Dissolve(.5)
    $ renpy.pause(1, hard = True)

    show christie_root_43_masha_sex 2z
    with Dissolve(.5)
    $ renpy.pause(1, hard = True)
    show christie_root_43_masha_sex 3z
    with Dissolve(.5)
    $ renpy.pause(1, hard = True)
    # show image 'cg/ep89/masha/gg_1.png'
    # show image 'cg/ep89/masha/gg_1.png':
    #     xpos 1375 
    # show image 'cg/ep89/masha/masha_1.png'
    # show image 'cg/ep89/masha/masha_1.png':
    #     xpos 1375
    # with Dissolve(.5)

    # $ renpy.pause(1, hard = True)
    

    #//Продавщица приподнимается (то есть спрайт, где она снимала трусы)

    #//ГГ приспускает штаны, чтобы достать член

    #//Анимация, как женщина садится на член
    scene image 'cg/ep89/masha/sex/1.png'
    show christie_root_43_masha_sex 3z
    #show image 'cg/ep89/masha/sex/panel.png'
    with my_dissolve
    call screen comic_frame(__("Аххххх!!!"), 280, 150, -1)
    call screen comic_frame(__("Боже!"), 280, 150, -1)
    call screen comic_frame(__("Что ты сделал со своим членом?"), 280, 150, -1)
    call screen comic_frame(__("Он стал великанским!"), 280, 150, -1)
    #//Анимация секса
    scene christie_root_43_sex 1 
    show christie_root_43_pen 1
    show image 'cg/ep89/masha/sex/panel.png'
    with my_dissolve
    call screen comic_frame(__("Знаешь, так мне нравится куда сильнее."), 280, 150, -1)
    call screen comic_frame(__("И новый, большой размер, и твоя таинственность."), 280, 150, -1)
    call screen comic_frame(__("В тебе словно открылось второе дыхание."), 280, 150, -1)
    call screen comic_frame(__("Твоя развратность теперь выражается не только в похабных словечках, хи-хи."), 280, 150, -1)
    call screen comic_frame(__("Наконец, ты перешёл к практической реализации своих сумасшедших фантазий."), 280, 150, -1)
    call screen comic_frame(__("Хотя, признаться, я не помню, чтобы ты мечтах о внезапно сексе в туалете."), 280, 150, -1)
    call screen comic_frame(__("Ты даже боялся уединиться со мной в публичном месте."), 280, 150, -1)
    call screen comic_frame(__("И постоянно просишь выгнать всех посетителей в магазине. "), 280, 150, -1)
    call screen comic_frame(__("Мне уже начинало казаться, будто бы просто слабак, что прячется за понтами и статусом полицейского."), 280, 150, -1)
    call screen comic_frame(__("Но… Аххх… Да! Теперь ты доказал мне обратное."), 280, 150, -1)
    call screen comic_frame(__("Я ошибалась. Сильно ошибалась. И теперь должна поплатиться за свою дерзость, верно, милый?"), 280, 150, -1)
    call screen comic_frame(__("Ахххх, да-да-да."), 280, 150, -1)
    #//Скорость х2 
label christie_root_43_sex_2:

    menu:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            $ pass
            window hide
            $ renpy.pause(9999)
            jump christie_root_43_sex_2
    show christie_root_43_sex 2 
    show christie_root_43_pen 2
    with my_dissolve
    
    call screen comic_frame(__("Позволь мне чуточку ускориться, шлёпая задницей по твоим ляжкам. "), 280, 150, -1)
    call screen comic_frame(__("Дааа, вот так!"), 280, 150, -1)
    call screen comic_frame(__("Хочется небольшого драйва…"), 280, 150, -1)
    call screen comic_frame(__("Знаешь… Этот сюжет вызывает во мне фонтан разнообразных мыслей."), 280, 150, -1)
    call screen comic_frame(__("Похабных, естественно. Хи-хи-хи."), 280, 150, -1)
    call screen comic_frame(__("Ты всё обставил так, словно это непредвиденное стечение обстоятельств."), 280, 150, -1)
    call screen comic_frame(__("Тесная коморка, темнота, таинственный незнакомец."), 280, 150, -1)
    call screen comic_frame(__("Опасность! Страх! Адреналин в крови! В голове всё перемешалось."), 280, 150, -1)
    call screen comic_frame(__("Но тут я понимаю, что чувство риска заводит меня."), 280, 150, -1)
    call screen comic_frame(__("Что я рада случившемуся…"), 280, 150, -1)
    call screen comic_frame(__("На мгновение я даже решила, что это и не ты вовсе. "), 280, 150, -1)
    call screen comic_frame(__("Будто бы кто-то вздумал воспользоваться моментом, чтобы сделать ЭТО со мной…"), 280, 150, -1)
    call screen comic_frame(__("Охххх… да-да-да!"), 280, 150, -1)
    call screen comic_frame(__("Ты ведь и рассчитывал на такую реакцию, верно?"), 280, 150, -1)
    call screen comic_frame(__("Ахх… Да-да-да!"), 280, 150, -1)
    #//Скорость х3
label christie_root_43_sex_3:

    menu:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            $ pass
            window hide
            $ renpy.pause(9999)
            jump christie_root_43_sex_3
    show christie_root_43_sex 3
    show christie_root_43_pen 3
    with my_dissolve
    call screen comic_frame(__("За дверью полно клиентов…"), 280, 150, -1)
    call screen comic_frame(__("Они могут услышать нас. Подумать, что со мной случилась беда и позвать кого-нибудь на помощь…"), 280, 150, -1)
    call screen comic_frame(__("Но обнаружат только меня, вопящую от удовольствия и полицейского, что трахает продавщицу магазина."), 280, 150, -1)
    call screen comic_frame(__("Или, что ещё хуже, сразу поймут, чем мы здесь занимаемся и пожалуются директору."), 280, 150, -1)
    call screen comic_frame(__("Меня могут уволить, а мне нужно будет искать новое место работы. "), 280, 150, -1)
    call screen comic_frame(__("Но ты провернёшь этот приём вновь, а я… конечно я поддамся на соблазн. "), 280, 150, -1)
    call screen comic_frame(__("Это порочный круг, который нам предстоит пройти вместе."), 280, 150, -1)
    call screen comic_frame(__("Главное…"), 280, 150, -1)
    call screen comic_frame(__("Главное только, чтобы об этом не узнала твоя жена, верно, милый?"), 280, 150, -1)
    call screen comic_frame(__("Ха-ха-ха!"), 280, 150, -1)
    call screen comic_frame(__("Охххх, какое наслаждение, обожаю твой член!"), 280, 150, -1)
    call screen comic_frame(__("Ещё-ещё-ещё!"), 280, 150, -1)
    #//Кончить (Скорость х4)
label christie_root_43_sex_4:

    menu:
        "Кончить":
            $ pass
        "Продолжить в том же темпе":
            $ pass
            window hide
            $ renpy.pause(9999)
            jump christie_root_43_sex_4
    show christie_root_43_sex 4
    show christie_root_43_pen 4
    with my_dissolve
    call screen comic_frame(__("Да-да-да! Я чувствую, как ты дрожишь в нетерпении!"), 280, 150, -1)
    call screen comic_frame(__("Я тоже собираюсь кончить, милый, я тоже!"), 280, 150, -1)
    call screen comic_frame(__("Мой киска стонет от счастья, ожидая поток твоей горячей спермы внутри!"), 280, 150, -1)
    #//Продавщица кончила
    $ renpy.pause(1, hard = True)

    #scene image '#fff' with Dissolve(.15, hard = True)

    #$ renpy.pause(1, hard = True)
    scene image 'cg/ep89/masha/sex/4.png'
    show image 'cg/ep89/masha/sex/0c.png'
    show image 'cg/ep89/masha/sex/panel.png'
    with my_vpunch
    $ renpy.pause(.3, hard = True)
    show christie_root_43_masha_sex 1c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 2c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 3c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 4c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 5c
    $ renpy.pause(.1, hard = True)
    show image 'cg/ep89/masha/sex/6c.png'
    show christie_root_43_masha_sex 6c
    $ renpy.pause(.1, hard = True)
    show image 'cg/ep89/masha/sex/7c.png'
    show christie_root_43_masha_sex 7c
    $ renpy.pause(.1, hard = True)
    show image 'cg/ep89/masha/sex/6c.png'
    show image 'cg/ep89/masha/sex/7c.png'
    show image 'cg/ep89/masha/sex/8c.png'
    $ renpy.pause(.6, hard = True)
    show christie_root_43_masha_sex 1c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 2c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 3c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 4c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 5c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 6c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 7c
    $ renpy.pause(.3, hard = True)
    show christie_root_43_masha_sex 1c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 2c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 3c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 4c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 5c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 6c
    $ renpy.pause(.1, hard = True)
    show christie_root_43_masha_sex 7c
    $ renpy.pause(.1, hard = True)


    
    #//мысли
    show shadow_full 
    with my_dissolve
    call screen comic_frame(__("{i}Без комментариев…{/i}"), 1400, 200, end_img = 'interface/comic_frame_think.png')#ГГ
    #//конец мысли

    hide shadow_full with my_dissolve
    call screen comic_frame(__("Мне пора, дорогой."), 280, 150, -1)
    #//Обратную сторону одевается

    call screen comic_frame(__("Не выходи сразу после меня, пожалуйста, не хочу, чтобы клиенты пялились на нас."), 280, 150, -1)
    call screen comic_frame(__("По крайней мере не сейчас."), 280, 150, -1)
    call screen comic_frame(__("Мгу…"), 1400, 200, end_img = 'interface/comic_frame_think.png')#ГГ
    $ add_ach('ACH_14')

    # python:
    #     achievement.grant("ACH_14")
    #     achievement.sync()

    #//От первого лица показать дверной проём

    #// masha_Normal выезжает слева

    #// Normal стоит заранее

    scene image '#000'
    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)

    $ add_to_gallery(34)
    
    scene image 'locations/bg/ClothesStore/afternoon.png'
    show Officer Normal
    show Officer Normal:
        xalign 1.5
    show Masha Normal
    show Masha Normal:
        xalign -1.5
    show Christie Harly_Normal
    show Christie Harly_Normal:
        xalign .7

    show expression 'cg/christie_root/falos/0.png'
    show expression 'cg/christie_root/falos/1_1.png':
        xpos -800
    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    
    

    show Masha Normal at go_from_left(xxalign = .3, xxzoom = -1)
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Маша" "Извините, что задержалась."
    show Christie Harly_Normal
    "Кристи" "Всё в порядке."

    show Christie:
        easein_cubic 5 xalign -1.5
    #//Officer_Normal выезжает справа

    #//Normal уезжает влево и исчезает
    show Officer
    show Officer Normal at go_from_right(xxalign = .74, xxzoom = -1)

    "Офицер" "Скучаешь? "
    show Masha Surprise:
        xalign .3
        xzoom -1
    with my_dissolve
    "Маша" "М-милый?!"
    show Officer Hm:
        xalign .74
        xzoom -1
    hide Christie
    with my_dissolve
    "Офицер" "Ты выглядишь так, словно увидела призрака. "
    show shadow_full with my_dissolve
    "[gg]" "Пока они болтают, я успею напялить свой костюм Джокера обратно."
    
    play sound 'audio/change_clothes.mp3'

    hide shadow_full 
    show Officer Chagrin
    with my_dissolve
    "Офицер" "Ты что, не рада меня видеть?"
    show Masha Surprise
    "Маша" "Р-рада?.. Да, конечно. Конечно рада!!!"
    show Masha Chagrin
    "Маша" "Просто я думала, что мы только что… Что ты.."
    show Masha Surprise
    "Маша" "О боже!.."
    "[gg]" "Вот дерьмо! Она всё поняла!"
    "[gg]" "Я точно умру не своей смертью."
    show Masha Chagrin
    "Маша" "Я… "
    show Officer Say
    "Офицер" "Что-то случилось?"
    show Masha Smile
    "Маша" "Просто не ожидала себя так рано увидеть."
    show Officer Hm
    "Офицер" "Рано? Я пришёл ровно в тоже время, что и всегда."
    show Masha Normal
    "Маша" "Я имею в виду… Ну, я планировала подготовиться к твоему прибытию. Как-нибудь интересно одеться и всё такое, а вот ты пришёл. "
    show Masha Normal
    "Маша" "Я в полной растерянности."
    show Officer Normal
    "Офицер" "Зря. "
    show Officer Smile
    "Офицер" "Я смотрю сквозь твою одежду, крошка. Хе-хе-хе."
    show Masha Embarrassment
    "Маша" "Да но... Сегодня тяжёлый день, милый."
    show Masha Normal
    "Маша" "Я вся забегалась и… давай перенесём на завтра, пожалуйста?"
    show Officer Hm
    "Офицер" "Ты странно себя ведёшь, Элейн."
    show Masha Normal
    "Маша" "Да, согласна. Голова идёт кругом. Слишком много работы. Позвони мне, окей?"
    show Officer Angry
    "Офицер" "Я не привык принимать отказы, ты же знаешь, крошка."
    show Masha Embarrassment
    "Маша" "Это не отказ, милый. Я просто переношу свидание на завтра."
    show Officer Hm
    "Офицер" "Кхм…."
    show Officer Normal
    "Офицер" "Ладно. Я удовлетворю твою просьбу."
    show Masha Laughs
    "Маша" "Спасибо-спасибо-спасибо! А теперь позволь мне вернуться к своим обязанностями. "
    show Officer Say
    show Masha Normal
    "Офицер" "Хорошо…"
    #// Officer_Normal исчезает влево
    show Officer:
        easein_cubic 3 xalign -1.5
    $ renpy.pause(.5, hard = True)
    show Masha Angry:
        easein .75 xalign .5
    $ renpy.pause(.8, hard = True)
    show Masha Walk:

        xzoom 1 zoom 1.0 xalign .5
        
        .75
        xzoom -1 zoom 1.05
        
        .75
        xzoom 1 zoom 1.1
        
        .75
        xzoom -1 zoom 1.15
        
        .75
        xzoom 1 zoom 1.2
        
        .75
        xzoom -1 zoom 1.25
        
        .75
        xzoom 1 zoom 1.3
        
        .75
        xzoom -1 zoom 1.35
        
        .75
        xzoom 1 zoom 1.4
        
        .75
        xzoom -1 zoom 1.45
        
        .75
        xzoom 1 zoom 1.5
        
        .75
        xzoom -1 zoom 1.55
        
        .75
        xzoom 1 zoom 1.6
        
        .75
        xzoom -1 zoom 1.65
        
        .75
        
        
    with my_dissolve
    
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/daily-beetle-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Маша" "Выходи."

    show expression 'cg/christie_root/falos/1_1.png':
        easein 1 xpos 0 alpha 1.0
    "[gg]" "…."
    hide Officer
    show expression 'cg/christie_root/falos/1_1.png':
        easein .3 xpos -1000 alpha 0.0
    with my_vpunch
    "Маша" "Выходи, я сказала!"
    #//Магазин

    #masha_Normal

    #Normal
    scene black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)

    scene image 'locations/bg/ClothesStore/afternoon.png'
    show Masha Angry
    show Masha Angry:
        xalign .24
        xzoom -1
    show GG Joker_Chagrin
    show GG Joker_Chagrin:
        xalign .74
        xzoom -1
    with my_dissolve
    "Маша" "Чёрт…"
    
    "Маша" "Мать твою, ты что, клоун?"
    
    "[gg]" "Д-джокер…"

    "Маша" "А похож на аниматора с детских праздников. "
    
    "[gg]" "Знаю…"
    
    "Маша" "Не трудно догадаться, я изумлена случившимся. "
    
    "[gg]" "Поверьте, я тоже. "
    
    show Masha Surprise
    with my_dissolve
    "Маша" "Да ну?!"
    
    "[gg]" "Мне очень жаль, я поступил край-крайне…"
    show Masha Smile
    with my_dissolve
    "Маша" "Оригинально."
    show GG Joker_Surprise
    "[gg]" " Ориги… Что?!"
  
    show Masha Passion
    with my_dissolve
    "Маша" "Ты поступил оригинально, малыш. "
  
    "Маша" "И, как ты заметил в процессе, я была в восторге от случившегося. "
    show GG Joker_Embarrassment
    "[gg]" " …."
    show GG Joker_Embarrassment
    "[gg]" "Мне, если честно, тоже очень понравилось."
  
    "Маша" "Ха! Ещё бы."
  
    show GG Joker_Smile
    with my_dissolve
    "Маша" "Моя задница, как касания Гермеса, делает всех счастливыми. "
  
    "Маша" "У меня только один вопрос. "
  
    show GG Joker_Surprise
    with my_dissolve
    show Masha Angry
    with my_dissolve
    "Маша" "Что ты делал на моём туалете?.."
    show GG Joker_Please
    "[gg]" "Ну… Э…"
    #//мысли

    show shadow_full with my_dissolve
    show GG Joker_Chagrin
    "[gg]" "{i}Чтобы я не сказал, едва ли она поверит в мою историю.{/i}"
    show GG Joker_Normal
    "[gg]" "{i}Но что-то же я должен сказать. Какая у меня может быть причина взломать замок уборной в магазине одежды?!{/i}"
    #//конец мысли

    hide shadow_full with my_dissolve
    show Masha Laughs
    show GG Joker_WTF
    with my_dissolve
    "Маша" "Ха-ха-ха."
  
    "Маша" "Дай угадаю, ты мастурбировал, подглядывая за клиентками в дверной проём!"
    show GG Joker_Surprise
    "[gg]" "Вау!"

    "[gg]" "Вы поймали меня с поличным. "
    show Masha Smile
    "Маша" "Так и знала, чёртов извращенец. Так и знала. "
    show Masha Angry
    show GG Joker_Embarrassment
    with my_dissolve
    "Маша" "За минутку удовольствия спасибо, конечно, но лучше тебе больше не возвращаться, парень. "
    show Masha Normal
    show GG Joker_Smile
    with my_dissolve
    "Маша" "А то мало ли, вдруг я захочу ещё. Ха-ха-ха."
    show GG Joker_Normal
    "[gg]" "Хе-хе…"
    #// Normal исчезает влево
    show GG:
        easein_cubic 3 xalign -1.5

    $ renpy.pause(.75, hard = True)
    scene black
    with Dissolve(.5)
    $ location_now = 'City_Home'
    $ descript_Christie = _("Вернуться домой.")
    $ Event('christie_root_43_1', 'Corridor')
    jump main_interface_label


label christie_root_43_1:
    $ events.pop('christie_root_43_1', 0)
    
    #//Korridor_Evening
    #$ location_now  = 'Corridor'
    #$ time.time_now = 'evening'
    call show_bg_image_label from _call_show_bg_image_label_185
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show GG Joker_Normal
    show GG Joker_Normal at go_from_left(xxalign = .2)
    show Christie Normal
    show Christie Normal at go_from_right(xxalign = .8)
    
    #// Normal появляется слева

    #// Kristy_Normal появляется справа

    "Кристи" "Где тебя носило?"
    show GG Joker_Normal:
        xalign .2
    show Christie Surprise
    "[gg]" "Сама знаешь где."
    show Christie Normal:
        xalign .8
    with my_dissolve
    "Кристи" "Ну и как, получилось заснять измену?"
    show GG Joker_Chagrin
    "[gg]" "Нет. План полностью провалился."
    show Christie Surprise
    "Кристи" "Но почему? Я ведь видела, как в магазин зашёл муж Сьюзен. "
    show GG Joker_Chagrin
    "[gg]" "Продавщица дала ему отворот поворот."
    show Christie Skepticism
    "Кристи" "Неожиданно. И очень странно. "

    "[gg]" "Попытаемся в другой раз."
    show Christie Angry
    "Кристи" "Ну да, конечно…"
    show Christie Skepticism
    "Кристи" "Ты лучше скажи, как ты умудрился быть незамеченным в туалете, когда туда зашла продавщица?!"
    show GG Joker_Smile

    "[gg]" "Аха-ха-ха-ха!"
    
    "[gg]" "Забавный случай, не правда ли?"
    show Christie Skepticism
    "Кристи" "Ну и?"
    show GG Joker_Embarrassment

    "[gg]" "Просто повезло, Кристи."
    
    "[gg]" "В туалете не работала лампочка. Окон там нет. Внутри кромешная тьма."
    
    "[gg]" "На всякий случай я притаился в самом углу, сбоку от сливного бачка.  "
    
    "[gg]" "Входная дверь располагается напротив умывальника, так что свет, когда женщина вошла, на меня не попал. "
    
    "[gg]" "Короче говоря, продавщица сделала своё дело и даже не заметила меня."
    #//мысли
    show shadow_full with my_dissolve
    "[gg]" "{i}Почти не соврал.{/i}"
    #//мысль закончена

    hide shadow_full 
    show Christie Normal
    with my_dissolve
    "Кристи" "Складно рассказываешь. "
    show GG Joker_Normal
    "[gg]" "Ага. Но план состоял в другом, так что ситуация никак не сыграла нам на руку."
    show Christie Smile
    "Кристи" "А вот и нет."
    show Christie Smile
    "Кристи" "Пока ты наблюдал за тем, как женщина справляла нужду, я обыскала её рабочее место, нашла там её сумочку и стащила телефон."
    show GG Joker_Surprise
    "[gg]" "Но ведь это противозаконно, Кристи!!!"
    show Christie Angry
    "Кристи" "Да не ори ты так. Знаю я."
    #Joker_Skepticism

    show Christie Embarrassment
    "Кристи" "Это всё из-за страха."
    show Christie Embarrassment
    "Кристи" "Когда я увидела, что продавщица пошла в туалет, где ты скрывался, я решила, что это конец."
    show Christie Embarrassment
    "Кристи" "Думала, тебя сейчас застукают. Начнётся скандал!"
    show Christie Embarrassment
    "Кристи" "План рушился на глазах…"
    show Christie Embarrassment
    "Кристи" "Нужен был выход из положения."
    show Christie Embarrassment
    "Кристи" "Мне нужна была улика, любая зацепка измены полицейского, но не для Сьюзен, а для меня."
    #Joker_Surprise 
    
    show Christie Embarrassment
    "Кристи" "Если в этом телефоне хранятся совместные фото копа и продавщицы, я могла бы пригрозить ему обнародовать их, чтобы он отпустил тебя. "
    show Christie Chagrin
    "Кристи" "Я поступила опрометчиво, да?.. Нельзя воровать чужие вещи."
    show GG Joker_Normal
    "[gg]" "Ты совершила благородный поступок, Кристи."
    show Christie Chagrin
    "Кристи" "Воровство не может быть благородным…"
    
    "[gg]" "А как же Робин Гуд?"
    show Christie Chagrin
    "Кристи" "Он обычный бандит. "
    show Christie Chagrin
    "Кристи" "Пытался купить симпатию и благосклонность некоторых горожан. Политический пиар, не более."
    
    "[gg]" "Ну хорошо. Но ты же не руководствовалась материальной наживой."
    show Christie Chagrin
    "Кристи" "Нет."
    
    "[gg]" "Ты делала это во имя моего спасения, правда?"
    show Christie Embarrassment
    "Кристи" "Правда. "
    
    "[gg]" "Ну, а разве закон стоит выше человеческой жизни? "
    show Christie Skepticism
    "Кристи" "Смотря о какой жизни речь…"
    
    "[gg]" "О моей, чёрт возьми!"
    show Christie Passion
    "Кристи" "Хи-хи-хи."
    show Christie Passion
    "Кристи" "Мне ты дороже, конечно."
    show GG Joker_Smile
    "[gg]" "Значит, ты поступился правильно. "
    show Christie Smile
    "Кристи" "Наверное так."
    show GG Joker_Normal
    "[gg]" "Дай мне пожалуйста телефон, Кристи, я знаю, кто сможет его взломать."
    show Christie Normal
    "Кристи" "Вот, держи."
    #//Сцена закрывается

    show screen give_item_screen(i_path+'/items/phone.png', _('Телефон Продавщицы'), [_('Обыкновенный смартфон.')])
    with Dissolve(.5)
    $ renpy.pause(9999)
    #//Сцена закрывается
    scene black
    hide screen give_item_screen
    with Dissolve(.5)

    $ add_to_inventory(name = 'Телефон Продавщицы')

    $ block_exit_home_christie_root_43 = copy.deepcopy(block_exit_home)
    $ block_milf_home_christie_root_43 = copy.deepcopy(block_milf_home)
    $ block_sister_home_christie_root_43 = copy.deepcopy(block_sister_home)
    $ block_time_forward_christie_root_43 = copy.deepcopy(block_time_forward)
    


    $ block_exit_home    = True
    $ block_milf_home    = True
    $ block_sister_home  = True
    $ block_time_forward = True

    if not hasattr(store, 'allowed_events'):
        $ allowed_events = []
    $ allowed_events.append('christie_root_43_2')
    $ Event('christie_root_43_2', 'GG_Room')

    $ descript_Christie = _("Вернуться в комнату.")
    jump main_interface_label


label christie_root_43_2:
    $ events.pop('christie_root_43_2', 0)
    $ allowed_events.remove('christie_root_43_2')


    
    $ block_exit_home    = copy.deepcopy(block_exit_home_christie_root_43)
    $ block_sister_home  = copy.deepcopy(block_sister_home_christie_root_43)
    $ block_milf_home    = copy.deepcopy(block_milf_home_christie_root_43)
    $ block_time_forward = copy.deepcopy(block_time_forward_christie_root_43)


    $ del block_exit_home_christie_root_43 
    $ del block_milf_home_christie_root_43
    $ del block_sister_home_christie_root_43 
    $ del block_time_forward_christie_root_43



    #//Korridor_Evening
    #$ location_now  = 'Corridor'
    #$ time.time_now = 'evening'
    $ location_now  = 'GG_Room'

    call show_bg_image_label from _call_show_bg_image_label_186
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show GG Joker_Normal
    show GG Joker_Normal at go_from_left(xxalign = .2)

    #//MyRoom_Evening

    #// Normal выезжает слева


    "[gg]" "Пора снять с себя этот дебильный наряд."
    #//Normal уезжает вправо и возвращается оттуда в обычной одежде
    show black
    with Dissolve(.5)

    play sound 'audio/change_clothes.mp3'

    $ renpy.pause(.5)
    
    hide black
    
    show GG Normal:
        xalign .2
    with my_dissolve
    
    "[gg]" "Так-то лучше."
    show GG Think
    "[gg]" "Кристи отлично постаралась."
    show GG Think
    "[gg]" "С моей стороны было бы преступлением никак не отблагодарить её."
    show GG Think
    "[gg]" "Куплю ей книгу в подарочном издании. "
    show GG Think
    "[gg]" "Её любимую."
    
    #Tian_44

    scene black with Dissolve(.5)


    $ descript_Christie = _("Купить подарочное издание «Дон Кихот» Мигеля Де Сервантеса.")
    

    $ don_kihot_at_shop = 22
    if not hasattr(store, 'add_items_for_storein_shop_fixed'):
        $ add_items_for_storein_shop_fixed = []
    $ add_items_for_storein_shop_fixed.append(don_kihot_at_shop)

    $ Event('christie_root_44', location = 'City_Shop', need_items = [22,])

    $ Event('christie_root_45', location = 'Christie', need_items = [22,])

    jump main_interface_label