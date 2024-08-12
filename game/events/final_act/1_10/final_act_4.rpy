# image final_act_4_cg 1 = LiveComposite(
#     (1920, 1080),
#     (0, 0), 'black',
#     (600, 600), Text('final_act_4_cg 1', color = '#F00a'),
#     )
image final_act_4_blinds_1_1  = Crop((0, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_2  = Crop((100, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_3  = Crop((200, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_4  = Crop((300, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_5  = Crop((400, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_6  = Crop((500, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_7  = Crop((600, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_8  = Crop((700, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_9  = Crop((800, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_10 = Crop((900, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_11 = Crop((1000, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_12 = Crop((1100, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_13 = Crop((1200, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_14 = Crop((1300, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_15 = Crop((1400, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_16 = Crop((1500, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_17 = Crop((1600, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_18 = Crop((1700, 0, 100, 1080), '/cg/final_act/prison/0.png')
image final_act_4_blinds_1_19 = Crop((1800, 0, 120, 1080), '/cg/final_act/prison/0.png')

transform final_act_4_blinds_transform(xp=0, dur=.3, xzoom_start = 0.0, xzoom_finish=1.0, xp_fin=0):
    xpos xp
    xzoom xzoom_start
    easein dur xzoom xzoom_finish xpos xp_fin
label final_act_4_debug:
    scene black
    show image Text("DEBUG: переход к final_act_4"):
        align(.5, .5)
    with my_dissolve 
    call wait_click_label from _call_wait_click_label_29
label final_act_4:    #Final_Act_4 
    $ events.pop('final_act_4', 0)
    $ events['talk_with_store_woman_label'].complete = False
    #$ renpy.play('audio/Door.mp3')
    #scene expression '#000' with Dissolve(.3)
    #$ renpy.pause(.4, hard=True)
    $ location_now = 'City_Shop'
    call show_all_images_label from _call_show_all_images_label_69 
    show GG Normal
    show GG Normal at go_from_left(xxalign=.5, ttimer=1.7)
    with my_dissolve
    $ renpy.pause(.35, hard = True)
    show Prostitute Normal
    show Prostitute Normal at go_from_right(
        xxalign_start = 1.7, xxalign=-.1, ttimer=1.2)
    #Активировать магазин.


    $ renpy.pause(.57, hard = True)
    show white:
        alpha 1.0
        ease .1 alpha 0.0
    show GG Falldown:
        xalign .5
        xzoom -1
        parallel:
            easein 1.5 xalign -.2  
        parallel:
            easein .1 ypos 1110+75
            easein .1 ypos 1080+75
            easein .1 ypos 1100+75
            easein .1 ypos 1070+75
            easein .1 ypos 1090+75
            easein .1 ypos 1060+75
            easein .1 ypos 1080+75
            easein .1 ypos 1050+75
    show Prostitute Falldown:
        xalign .65
        parallel:
            easein 1.5 xalign 1.1  
        parallel:
            easein .1 ypos 1110+75
            easein .1 ypos 1080+75
            easein .1 ypos 1100+75
            easein .1 ypos 1070+75
            easein .1 ypos 1090+75
            easein .1 ypos 1060+75
            easein .1 ypos 1080+75
            easein .1 ypos 1050+75

    $ renpy.pause(1.5, hard = True)
    #show GG:
    #    easein .175 ypos 2000
    #show Prostitute:
    #    easein .175 ypos 2000
    #show black:
    #    alpha .0
    #    easein .12 alpha 1.0
    #with my_vpunch

    #$ renpy.pause(.5, hard = True)

    # scene black
    # show image Text('final_act_4_cg 1', color = '#F00', size = 45):
    #     align(.5, .5)
    # with my_dissolve

    #GG_Normal

    #//Bitch_Normal стремительно направляется с ГГ, ТИПА сшибая его с ног

    #//Встряска экрана

    #//Bitch_GG_Earth
    show GG Please:
        xzoom 1
        xalign .25
    show Prostitute Normal:
        xalign .8 ypos 1080
    with my_dissolve  
    "Проститутка" "Ой, простите!"
    "Проститутка" "Извините!"
    "Проститутка" "Я такая неуклюжая! Это всё моя вина!"
    show GG Laughs
    "[gg]" "Эй, эй, успокойся!"
    #show GG Normal
    "[gg]" "Я совсем не ушибся."
    #//предыдущий арт исчезает

    # scene black
    # show image Text('final_act_4_cg 2', color = '#F00', size = 45):
    #     align(.5, .5)
    # with my_dissolve
    #GG_Bitch_Help_1
    show Prostitute Normal:
        easein 1.0 xalign .5
    "Проститутка" "О нет-нет-нет, позвольте я осмотрю вас. "
    show GG Angry
    with my_vpunch
    "[gg]" "Прекратите меня лапать! "
    "[gg]" "Я в полном порядке."
    #GG_Bitch_Help_2 

    # scene black
    # show image Text('final_act_4_cg 3', color = '#F00', size = 45):
    #     align(.5, .5)
    # with my_dissolve
    "Проститутка" "И здесь? Здесь тоже всё хорошо?"
    "Проститутка" "Я ощущаю здесь какое-то… беспокойство."
    "Проститутка" "Может, я могла бы вам как-то помочь или компенсировать свою оплошность? "
    show GG Please:
        easein .3 xalign .1
    "[gg]" "Прошу вас, уберите руки…"
    "Проститутка" "Пожалуйста, только не обижайтесь на дурёху!"
    "Проститутка" "Я умею признавать свою вину, но лучше всего, я умею её заглаживать, хи-хи."
    "Проститутка" "Что скажете?.."
    "[gg]" "Женщина, уверяю вас, мне ничего от вас не нужно."
    "[gg]" "Позвольте мне отправиться по своим делам!"
    #//Игрок лишается всех денег
    $ money = 0
    #GG_Normal

    #show Prostitute Normal
    "Проститутка" "Хорошо-хорошо. Ещё раз извините, что сбила вас с ног."
    #show GG Normal
    "[gg]" "Да-да, хорошего вам дня."
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_17
    show Prostitute:
        easein 1.0 xalign -1.2
    show GG Think:
        easein 1.0 xalign .5
    $ from_say_screen = False
    $ renpy.pause(.5, hard = True)
    #show GG Think

    "[gg]" "Хм… У этой проститутки знакомая внешность."
    
    "[gg]" "Не та ли это женщина, у которой муж Сьюзен выбивал деньги в гетто?.."
    
    "[gg]" "Да, точно. Это она."
    
    "[gg]" "И что она здесь забыла? Да ещё днём."
    
    "[gg]" "Наверное, обслуживала местного жителя и теперь торопится в родной район."
    
    "[gg]" "Ну и пусть. Какое мне до этого дело?"
    #//Магазин

    #//GG_Normal выезжает слева, и остаётся в левой части экрана 
    #(но не сильно впритык)
    scene expression '#000' with Dissolve(.3)
    $ location_now = "StoreIn"
    $ renpy.pause(.4, hard=True)
    call show_all_images_label from _call_show_all_images_label_70 
    show GG Normal
    show GG Normal at go_from_left(xxalign=.045, ttimer=1.7)
    with my_dissolve
    $ renpy.pause(.35, hard = True)
    
    "[gg]" "Так… "
    
    "[gg]" "Пора бы выбрать подходящее вино для чудесного вечера с Мариной."
    
    "[gg]" "В этот раз я предпочту белое и сладкое."
    
    "[gg]" "Не то, чтобы я слыл экспертом в алкоголе, но красивая бутылка всегда украсит томный вечер."
    #//Встряска
    show GG Skepticism
    with my_vpunch
    "[gg]" "Эм…"
    show GG Surprise
    with my_vpunch
    "[gg]" "А где мои деньги?!"
    show GG Angry
    with my_vpunch
    "[gg]" "Вот же шлюха!!!"
    show GG Chagrin
    with my_dissolve
    "[gg]" "Она ограбила меня..."
    show GG Normal
    with my_dissolve
    "[gg]" "Что ж. Не страшно. Благо, я знаю где её искать. "
    
    "[gg]" "Но пока я доберусь до гетто, пока я отыщу эту суку…"
    show GG Think
    with my_dissolve
    "[gg]" "Нет, сейчас у меня другие планы."
    
    "[gg]" "Есть идея!"
    # show GG:
    #     xzoom -1.0
    #     ease .75 xalign .1 alpha .0
    # show black:
    #     alpha 0.0
    #     ease .75 alpha 1.0
    # $ renpy.pause(1.0, hard = True)

    
    # scene black with my_dissolve
    # $ location_now = 'City_Shop'
    # $ renpy.pause(.5, hard = True)
    #call show_bg_image_label
    show GG Normal
    show GG Normal:
        #xalign 0.0
        ease .75 xalign .3
    $ renpy.pause(.25, hard = True) 
    show Misha Normal
    show Misha Normal:
        alpha 0.0 ypos 1080
        xalign .87
        ease .5 alpha 1.0
    $ from_say_screen = False
    $ renpy.pause(.25, hard = True) 
    #//GG_Normal перемещается ближе к центру

    #Misha_Normal

    "[gg]" "Привет. "
    show GG Normal:
        xalign .3
    show Misha Normal:
        xalign .87 alpha 1.0
    with my_dissolve
    "Мишванда" "Давно не виделись."
    show GG Normal
    "[gg]" "Я понимаю, это не очень корректная просьба, но могу ли я одолжить у тебя бутылочку белого вина до завтра? "
    show GG Normal
    "[gg]" "Даю слово, я верну деньги уже завтра."
    show Misha Normal
    "Мишванда" "Нет."
    show GG Chagrin
    "[gg]" "Нет?"
    show Misha Normal
    "Мишванда" "Я же ясно сказала – нет, значит нет."
    show GG Embarrassment
    "[gg]" "Ну пожалуйста!"
    show Misha Chagrin:
        parallel:
            easein .1 ypos 1080
            easein .1 ypos 1085
            easein .1 ypos 1080
            easein .1 ypos 1085
            easein .1 ypos 1080
            easein .1 ypos 1085
            easein .1 ypos 1080
        parallel:
            easein 1.25 xalign .5
    show GG:
        
        easein 1.25 xalign .0
    "Мишванда" "Слушай, красавчик, у нас нет охранника, это правда, но поверь, если ты сейчас же не свалишь, я самолично отпинаю тебя до самой двери!"
    show GG Embarrassment
    "[gg]" "Понял, извини."
    show GG Embarrassment:
        xzoom -1
        easein 1.25 xalign -.7
    $ renpy.pause(.4, hard = True)
    scene black with my_dissolve
    $ location_now = 'City_Shop'
    $ renpy.pause(.5, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_233 
    show Jay Normal
    show Jay Normal:
        xalign .35
        ypos 1085
        xalign .65
    show Bob Normal
    show Bob Normal:
        xalign .65
        ypos 1085
        xalign .95
    show GG WTF
    show GG WTF at go_from_left(xxalign=.12, ttimer=1.3)
    with my_dissolve

    $ renpy.pause(.5, hard = True)
    #//На входе Магазина

    #//GG_Chagrin 

    #//Jay_Bob

    "Зудило" "Эй, Чувачело, да на тебе лица нет!"
    "Бубнило" "….."
    show GG Smile:
        xalign .12
    with my_dissolve
    "[gg]" "О, вы во как раз вовремя!"
    show GG Smile
    "[gg]" "Не займёте мне сорок баксов?"
    show Jay OMG
    with my_dissolve
    "Зудило" "Нихера себе у тебя приветствие! "
    show GG Smile
    "[gg]" "Очень надо, очень! Я бы не стал просить без нужды. Вы же знаете, я надёжный как скала. Отдам в кратчайшие сроки!"
    "Зудило" "Вот это пацан загоняет, а! "
    show shadow_full:
        alpha .75
    show Jay Silence:
        xzoom -1
    with my_dissolve
    "Зудило" "Ты слышишь тоже, что и я, Бубнило?"
    "Бубнило" "…."
    hide shadow_full
    show Jay Normal:
        xzoom 1
    with my_dissolve
    "Зудило" "Похоже, ты на мели, чувачок. "
    show GG WTF
    with my_dissolve
    "[gg]" "Просто неудачный день."
    show GG Please
    with my_dissolve
    "[gg]" "Меня ограбили на пути в магазин, и теперь мне не на что купить продукты."
    "Зудило" "Ограбили? В этом районе? "
    "Зудило" "Если кто и грабит здесь, то только легавые."
    "Бубнило" "…."
    show GG WTF
    with my_dissolve
    "[gg]" "Ну так что, вы выручите меня?"
    "Зудило" "А как же."
    "Зудило" "Хоть мы и не внуки Джона Рокфеллера, но кореша в беде не оставим."
    show GG Smile
    with my_dissolve
    "[gg]" "Дичайше спасибо, чуваки! Вы очень выручите меня!"
    show Jay Silence
    with my_dissolve
    "Зудило" "Ага…"
    "Зудило" "Правда, вот, денег у нас нет."
    show GG Skepticism
    with my_dissolve
    "[gg]" "Ну и как же вы мне поможете?"
    "Зудило" "У нас есть лучше, чем деньги - «удочка», с помощью которой можно их добыть!"
    "[gg]" "Чо?.."
    show Jay Normal
    with my_dissolve
    "Зудило" "Товар, чувак, у нас есть товар. "
    "Зудило" "Продашь его, и половина денег твоих."
    show GG Please
    with my_dissolve
    "[gg]" "Идея, конечно, толковая…."
    "Зудило" "И какие тут могут быть аргументы против? "
    "Зудило" "Никакого кидалова. Мы честные бизнесмены."
    show GG WTF
    with my_dissolve
    "[gg]" "Вы не поймёте, пацаны."
    
    "[gg]" "Я планирую выйти из этого дерьма. "
    
    "[gg]" "Окончательно."
    show Jay Silence
    with my_dissolve
    "Зудило" "Хм…"
    "Зудило" "Разве это возможно?"
    show Jay Silence:
        xzoom -1
    with my_dissolve
    "Зудило" "Бубнило, ты бы хотел завязать?"
    show shadow_full:
        alpha 0.0
        easein .3 alpha .75

    show christie_day_mischief_lvl_2_water_drop:
        xpos 1520
        ypos 270
        zoom .75
        alpha .0
        easein .3 ypos 290 alpha 1.0
    "Бубнило" "……"

    show Jay OMG
    with my_dissolve
    "Зудило" "Чёрт, братишка, я плохо тебя знаю."
    show Bob:
        easein .3 ypos 1100
    show christie_day_mischief_lvl_2_water_drop:
        easein .3 alpha 0.0
    show shadow_full:
        easein .3 alpha .9
    "Бубнило" "……………"
    show Jay Normal
    with my_dissolve
    "Зудило" "Поговорим об этом позже."
    hide shadow_full
    hide christie_day_mischief_lvl_2_water_drop
    show Bob:
        ypos 1080
    show Jay Silence:
        xzoom 1.0
    with my_dissolve
    "Зудило" "Ну так что, чувачок, берёшь товар? "
    
    "[gg]" "…."
    show GG Please
    "[gg]" "Нет. Пожалуй, я откажусь."
    show Jay Normal:
        xzoom 1.0
    with my_dissolve
    "Зудило" "Какая собака тебя укусила? Бери, пока дают. Беги, пока не бьют."
    show GG Angry:
        easein .1 ypos 1080
        easein .1 ypos 1085
        easein .1 ypos 1080
        easein .1 ypos 1085
        easein .1 ypos 1080
        easein .1 ypos 1085
    "[gg]" "Хватит. Я больше не стану этим заниматься. "
    "Зудило" "Да что с тобой не так?.."
    hide GG
    show Officer Normal
    show Officer Normal at go_from_left(xxalign=.03,)# ttimer=1.7)
    show GG Surprise
    show GG Surprise:
        ypos 1085
        xalign .12
        easein 1.0 xalign .4
    show Jay:
        easein 1.0 xalign .8
    show Bob:
        easein 1.0 xalign 1.1
    #//Officer_Normal выеззжает слева 

    #//GG_Normal остаётся по центру

    "Офицер" "Вот ты и попался, дружок."
    show GG WTF:
        xzoom -1
        xalign .46
    show Officer:
        xalign .03
    with my_dissolve
    "[gg]" "Я… Что?!"
    #show Officer Normal
    "Офицер" "А я предупреждал."
    show GG Angry
    with my_dissolve
    "[gg]" "Что? Я ничего не делал!!"
    #//GG поворачивается к Зудиле

    show GG Angry:
        xzoom 1.0
    with my_vpunch
    "[gg]" "Вы подставили меня!!!"
    show Jay OMG
    with my_dissolve
    "Зудило" "Пошёл ты нахрен! Мы здесь ни при делах!"
    show GG:
        easein .8 xalign .75
       # xzoom -1.0
    show Jay Normal:
        xzoom -1
        easein 1.5 xalign 1.5
    show Bob:
        xzoom -1
        easein 1.5 xalign 1.5
    show Officer Laughs at hehe_transform()
    "Офицер" "Ха-ха-ха!"
    #//GG поворачивается к Офицеру 
    show GG:
        xzoom -1.0
        xalign .75
    show Officer Smile:
        xalign .03
    with my_dissolve
    "Офицер" "Как бы не так, гадёнышь. Ты сам себя подставил, когда решил, что со мной можно играть на равных."
    
    hide Bob
    hide Jay
    "[gg]" "Пошёл в задницу! У тебя нет никаких доказательств против меня."
    show Officer Normal
    "Офицер" "Это мы ещё посмотрим, говнюк. "
    
    "[gg]" "В чём меня обвиняют?!"
    
    "Офицер" "Список слишком длинный, чтобы я имел желания его здесь зачитывать."
    
    "Офицер" "Да не трясись ты. Я отведу тебя в участок и там всё узнаешь."
    
    "[gg]" "Как на счёт того, чтобы зачитать мои права?"
    
    "Офицер" "Не сейчас."
    
    "[gg]" "Это ещё почему?"
    
    "Офицер" "Подозреваемый решил сопротивляться аресту."
    show GG Surprise
    with my_dissolve
    "[gg]" "Чего?.."
    show white:
        alpha 1.0
        ease .1 alpha 0.0
    show Officer Kick:
        easein 1.0 xalign .1
    show GG Falldown:
        xzoom 1.0
        easein 1.0 xalign .9
    $ renpy.pause(1.2, hard = True)
    show GG:
        easein .175 ypos 2000
    with my_vpunch
    $ renpy.pause(.7, hard = True)
    #//Officer_Kick (такой спрайт есть, но называется иначе. Можно взять тот, где мент бьёт бандитов в Гетто) 

    #//GG_Padaet (такой спрайт есть, но называется иначе. Можно взять тот, где ему делает пощёчину Кристи)

    #//GG_Padaet исчезает

    #//Jay_Bob исчезают вправо

    show Officer Smile
    with my_dissolve
    "Офицер" "Давно следовало это сделать. "
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_30 
    $ renpy.pause(.5, hard = True)

    call final_act_blind_transition_to_black_label from _call_final_act_blind_transition_to_black_label_6
    python:
        for i in range(1, 20):
            n = (i-1)*102
            j = Crop((n, 0, 102, 1080), '/cg/final_act/prison/police_station/evening.png')
            

            dur = .2+i*.1,
            renpy.show('final_act_4_police_station_evening_'+str(i), what = j, 
                at_list=[
                final_act_4_blinds_transform(
                    xp  = n,
                    dur = .2+i*.1,
                    xp_fin = n,
                    )
                ])

    
        renpy.pause(2.5, hard = True)

        for i in range(1, 20):
            n = (i-1)*102
            j = Crop((n, 0, 102, 1080), 'cg/final_act/prison/0.png')
            

            dur = .2+i*.1,
            renpy.show('final_act_4_prison_0_'+str(i), what = j, 
                at_list=[
                final_act_4_blinds_transform(
                    xp  = n,
                    dur = .15+i*.1,
                    xp_fin = n,
                    )
                ])

        renpy.pause(2.5, hard = True)

    
    #"//Наверное Впервые Мы Сделаем Нестандартный Переход – Можно Сделаь 
    #Переход В Виде Жалуюзи? Но Не Горизонтально, 
    #А Вертикально? Такой, Пожалуйста " "3"

    #//Kamera

   # "//Данный Бэкграунд Комплексный, И Будет Состоять, Вероятно Из Нескольких Слоёв (2-3)" "само пространство, включающее место и место, где держат подозремого, и место коридора, откуда с ним могут говорить посетители, а уже другим слоём тюремная решётка на всю стену, чтобы можно было видеть спрайт посетителя."
    #//Поэтому я просто пишу Kamera, но имею в виду всё, кроме спрайтов персонажей.

    #//Kamera_Day

    #//Время - утро

    #//GG_Kamera_1
    scene image 'cg/final_act/prison/0.png'
#     show image comic_frame_v3_master:
    
#         zoom 1.0
#         xpos 1900
#         ypos 380
#         xanchor 0.0
#         yanchor 0.0
#         alpha .0

        

#     show image comic_frame_v3_slave:
#         zoom 1.0
#         xpos 300
#         ypos 380
#         xanchor 0.0
#         yanchor 0.0
#         alpha .0


#     with my_dissolve
#     call comic_frame_v3_label(LiveComposite(
#     (195, 194),
#     (0, 0), Transform('comic_v3_frame', size=(175, 194)),
#     (52, 35), Text('Вот', size = 35, font = _v3_font, ),
#     (41, 78), Text('И всё', size = 35, font = _v3_font, ),
#     (35, 121), Text('Нахуй.', size = 35, font = _v3_font, ),
#     (171, 74), 'interface/comic_v2/comic_frame_tail_2.png'), 
#     m_xpos = 611, 
#     m_ypos = 181) 
#     call comic_frame_v3_label(LiveComposite(
# (271, 108),
# (0, 0), Transform('comic_v3_frame', size=(252, 108)),
# (35, 35), Text('Приехали...', size = 35, font = _v3_font, ),
# (247, 42), 'interface/comic_v2/comic_frame_tail_2.png'), 
# m_xpos = 535, 
# m_ypos = 214) 
#     call comic_frame_v3_label(LiveComposite(
# (439, 194),
# (0, 0), Transform('comic_v3_frame', size=(420, 194)),
# (35, 35), Text('Стоило мне только', size = 35, font = _v3_font, ),
# (105, 78), Text('оступиться', size = 35, font = _v3_font, ),
# (87, 121), Text('на миллиметр', size = 35, font = _v3_font, ),
# (415, 74), 'interface/comic_v2/comic_frame_tail_2.png'), 
# m_xpos = 367, 
# m_ypos = 181) 
#     call comic_frame_v3_label(LiveComposite(
# (358, 323),
# (0, 0), Transform('comic_v3_frame', size=(338, 323)),
# (35, 35), Text('Как ответочка', size = 35, font = _v3_font, ),
# (86, 78), Text('за былые', size = 35, font = _v3_font, ),
# (74, 121), Text('проступки', size = 35, font = _v3_font, ),
# (92, 164), Text('настигла', size = 35, font = _v3_font, ),
# (38, 207), Text('меня в полной', size = 35, font = _v3_font, ),
# (119, 250), Text('мере.', size = 35, font = _v3_font, ),
# (334, 101), 'interface/comic_v2/comic_frame_tail_2.png'), 
# m_xpos = 448, 
# m_ypos = 155) 
#     call comic_frame_v3_label(LiveComposite(
# (455, 224),
# (0, 0), Transform('comic_v3_frame', size=(434, 224)),
# (51, 35), Text('Да так мощно,', size = 45, font = _v3_font, ),
# (39, 88), Text('что аж челюсть', size = 45, font = _v3_font, ),
# (35, 141), Text('раскалывается.', size = 45, font = _v3_font, ),
# (431, 81), 'interface/comic_v2/comic_frame_tail_2.png'), 
# m_xpos = 351, 
# m_ypos = 175)
    
#     call comic_frame_v3_label(LiveComposite(
# (623, 340),
# (0, 0), Transform('comic_v3_frame', size=(602, 340)),
# (95, 35), Text('И тело продирает', size = 47, font = _v3_font, ),
# (94, 90), Text('холодная дрожь,', size = 47, font = _v3_font, ),
# (35, 145), Text('пока смрад тюремной', size = 47, font = _v3_font, ),
# (63, 200), Text('камеры заполоняет', size = 47, font = _v3_font, ),
# (164, 255), Text('мои лёгкие.', size = 47, font = _v3_font, ),
# (599, 157), 'interface/comic_v2/comic_frame_tail_2.png'), 
# m_xpos = 182, 
# m_ypos = 136)  
    $ add_ach('ACH_9')

    #python:
    #    achievement.grant("ACH_9")
    #    achievement.sync()
    show GG Invis
    show GG Invis:
        xalign .5
    "[gg]" "Вот и всё нахуй."
    "[gg]" "Приехали..."
    "[gg]" "Стоило мне только оступиться на миллиметр как ответочка за былые проступки настигла меня в полной мере."
    "[gg]" "Да так мощно что аж челюсть раскалывается."
    "[gg]" "И тело продирает холодная дрожь, пока смрад тюремной камеры заполоняет мои лёгкие." 
    "[gg]" "Хэппи Энд, сука."
    "[gg]" "Я уж было решил, что могу изменить себя… "
    "[gg]" "Убежать от прошлого и начать новую жизнь… Ха!"
    "[gg]" "Покажите мне того счастливчика, кому это удавалось!"
    "[gg]" "Наивный идиот."
    "[gg]" "Чтобы я там себе не фантазировал, а за свои поступки придётся отвечать. "
    "[gg]" "Вот она - достойная награда за недостойную жизнь."
    "[gg]" "Не так уж и плохо, если хорошо подумать."
    "[gg]" "А мог бы лежать где-то в земле, с обмотанной головой в целлофановый пакет, и пожираемый трупными червями."
    "[gg]" "Уф…"
    "[gg]" "Сраный философ. Надо было раньше думать."
    "[gg]" "Сейчас я чертовски голоден."
    "[gg]" "И ослаб настолько, что буквально падаю от обезвоживания. "
    "[gg]" "Надо выбираться отсюда."
    
    $ Location(
        'Prison',
        buttons = [
        {

        }
        ]
        )
    $ location_now = 'Prison'

    $ time.time_now = "afternoon"
    

    $ special_loc_images_dir.update({'Prison':'special_prison_images_label'})

    $ i = Function(renpy.show, 'final_act_prison_action_arrow_bed', what = 'final_act_prison_action_arrow', 
                at_list=[
                final_act_7_action_arrow_transform(
                     pos_finish=(1440, 540),
                     dur = .15, 
                     rot = 0.0,
                     alpha_finish = 1.0,
                     )
                ])
    
    $ j = Function(renpy.show, 'final_act_prison_action_arrow_bed', what = 'final_act_prison_action_arrow', 
                at_list=[
                final_act_7_action_arrow_transform(
                     pos_finish=(1420, 480),
                     dur = .15, 
                     rot = 0.0,
                     alpha_finish = 0.0,
                     )
                ])

    $ locations['Prison'].buttons[0].update({
        'bed':{
            'cords'  : (1365, 380, 545, 630), 
            'hovered': i,
            'unhovered': j,
            'action' : [j, Jump('prison_bed_label')],
            }
            }
            )

    $ i = Function(renpy.show, 'final_act_prison_action_arrow_window', what = 'final_act_prison_action_arrow', 
                at_list=[
                final_act_7_action_arrow_transform(
                     pos_finish=(1600, 250),
                     dur = .15, 
                     rot = -75,
                     alpha_finish = 1.0,
                     )
                ])
    
    $ j = Function(renpy.show, 'final_act_prison_action_arrow_window', what = 'final_act_prison_action_arrow', 
                at_list=[
                final_act_7_action_arrow_transform(
                     pos_finish=(1900, 250),
                     dur = .15, 
                     rot = -75,
                     alpha_finish = 0.0,
                     )
                ])


    $ locations['Prison'].buttons[0].update({
        'window':{
            'cords'  : (1640, 0, 280, 240), 
            'hovered': i,
            'unhovered': j,
            'action' : [j, Jump('prison_window_label')],
            }
            }
            )



    $ locations['Prison'].image_buttons_times = {
        'morning'   : {
        'officer': Jump('final_act_6'),
        },
        'afternoon' : {
        #'officer': Jump('final_act_6'),
        },
        'evening'   : {
        
        },
        'night'     : {

        },
        }
    $ descript = _("Я в тюрьме…")
    $ final_act_sitost = 20 
    $ final_act_power  = 0
    $ final_act_prison_start = True
    
    $ debug_next('final_act_6_debug',)
    python:
        for i in range(1, 20):
            n = (i-1)*100
            j = Crop((0, 0, 120, 1080), 'black')
            renpy.show('black_'+str(i), what = j, 
                at_list=[
                final_act_4_blinds_transform(
                    xp  = n,
                    dur = i*.075,
                    xp_fin = n,
                    )
                ])
        
        renpy.pause(1.5, hard = True)

        
        for i in range(1, 20):
            n = (19-i)*102
            j = Crop((n, 0, 102, 1080), 'locations/bg/Prison/afternoon.png')
            

            dur = .2+i*.1,
            renpy.show('final_act_4_prison_afternoon_'+str(i), what = j, 
                at_list=[
                final_act_4_blinds_transform(
                    xp  = n+102,
                    dur = .25+i*.08,
                    xp_fin = n,
                    )
                ])

    
        renpy.pause(2.5, hard = True)
        
    $ block_time_forward = False
    $ not_survival_final_act_4 = copy.deepcopy(not_survival)
    $ not_survival = True
    $ time.time_now = 'morning'

        
    jump main_interface_label #final_act_6
    #//Officer_Kamera

    #//На спрайт офицера НАДО КЛИКНУТЬ, чтоб начать диалог

    #//У игрока в этот момент, отображается весь интерфейс, но нельзя нажат 
    #(чтоб нихера не сломал, но интерфейс нужен, чтобы дать понять игроку – 
    #ему наддо чёта кликнуть, иначе непонятно)

    #//Время пропускать МОЖНО!

    #//Спрайт офицера стоит УТРОМ и ДНЁМ, вечером и ночью его нет.

    #//Пропускать время можно как на кровати, так и на кнопку суток



    #//НЮАНС


    #В Заключении У Нас, Вне Игровых Сценок, 
    #Когда Отображается Интерфейс, Добавится Ещё Два Показателя" 
    #"СИЛА и ВЫНОСЛИВОСТЬ."
    #Мы реализуем небольшой квестик.

    #В камере будет расположен унитаз. 
    #Его можно будет активировать и узнать из фразы ГГ, что так и так, 
    #судя по царапинам по полу, его активно двигали, и болты, 
    #которыми он прикручен, закручены неплотно. 
    #Если расшатать унитаз, то болты отваляться и можно будет отодвинуть санузел. 

    #Как ты уже догадался, чтобы отхуячить унитаз, нужно будет накачать силу. 
    #Позволим игроку отжиматься на полу, тем самым повышая стату. 
    #Но отжимаясь, игрок тратит выносливость. 
    #А выносливость пополняется едой. 
    #Еду он будет восполнять каждую ночь, принимая пищу, 
    #которую ему будет приносить одна из сотрудниц полиции. ОТАКЭ!


    # "Механика" ""
    # "Сила" "0 из 100"
    # "Выносливость" "20 из 100"

    #"Сила" "Отжимаясь 1 раз 
    #(и тратя 1 ед. времени, кроме ночи, ночью отжиматься нельзя), 
    #игрок тратит 20 выносливости, и получает 10 силы."

    #"Выносливость" "Восполняется до 50 при помощи функции «Покушать». 
    #ДО ЭТОГО, ОН ВЫНОСЛИВОСТЬ НЕ ВОСПОЛНЯЕТ! 
    # Функция «Покушать» появляется ПОСЛЕ квеста Final_Act_12"

    #Унитаз можно тискать ТОЛЬКО НОЧЬЮ. То есть, 1 раз в сутки.

    #Унитаз делится на 3 уровня сложности (ЫЫЫЫЫЫЫЫ!)

    #Каждый уровень сложности требует определённое число силы.

    #Уровень требует 30 силы

    #Уровень требует 70 силы

    #Уровень требует 100 силы
