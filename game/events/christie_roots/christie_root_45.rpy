
image christie_root_45 1 = Composite(
    (1920, 1080),
    (0, 0), 'cg/ep89/christie/bg.png',
    (0, 0), "cg/ep89/christie/1.png"
    )

image christie_root_45 2 = Composite(
    (1920, 1080),
    (0, 0), 'cg/ep89/christie/bg.png',
    (0, 0), "cg/ep89/christie/2.png"
    )


image christie_root_45 3 = Composite(
    (1920, 1080),
    (0, 0), 'cg/ep89/christie/bg.png',
    (0, 0), "cg/ep89/christie/3.png"
    )


image christie_root_45 4 = Composite(
    (1920, 1080),
    (0, 0), 'cg/ep89/christie/bg.png',
    (0, 0), "cg/ep89/christie/4.png"
    )




image christie_root_45_sex_end_1_tmp = Composite(
    (1920, 1080),
    (0, 0), 'cg/ep89/christie/bg.png',
    (0, 0), 'cg/ep89/christie/7d.png'
    )

image christie_root_45_sex end_1:
    '#fff' with Dissolve(.1)

    .5
    'christie_root_45_sex_end_1_tmp' with Dissolve(.2)


image christie_root_45_sex end_2 = Composite(
    (1920, 1080),
    (0, 0), 'cg/ep89/christie/bg.png',
    (0, 0), 'cg/ep89/christie/8d.png'
    )



image christie_root_45_sex 1_tmp:






    'cg/ep89/christie/1d.png'
    .17
    'cg/ep89/christie/2d.png'
    .17
    'cg/ep89/christie/3d.png'
    .17
    'cg/ep89/christie/4d.png'
    .17
    'cg/ep89/christie/5d.png'
    .17
    'cg/ep89/christie/4d.png'
    .17
    'cg/ep89/christie/3d.png'
    .17
    'cg/ep89/christie/2d.png'
    .17


    repeat



image christie_root_45_sex 2_tmp:







    'cg/ep89/christie/1d.png'
    .12
    'cg/ep89/christie/2d.png'
    .12
    'cg/ep89/christie/3d.png'
    .12
    'cg/ep89/christie/4d.png'
    .12
    'cg/ep89/christie/5d.png'
    .12
    'cg/ep89/christie/6d.png'
    .12
    'cg/ep89/christie/5d.png'
    .12
    'cg/ep89/christie/4d.png'
    .12
    'cg/ep89/christie/3d.png'
    .12
    'cg/ep89/christie/2d.png'
    .12




    repeat


image christie_root_45_sex 3_tmp:







    'cg/ep89/christie/1d.png'
    .08
    'cg/ep89/christie/2d.png'
    .08
    'cg/ep89/christie/3d.png'
    .08
    'cg/ep89/christie/4d.png'
    .08
    'cg/ep89/christie/5d.png'
    .08
    'cg/ep89/christie/6d.png'
    .08
    'cg/ep89/christie/5d.png'
    .08
    'cg/ep89/christie/4d.png'
    .08
    'cg/ep89/christie/3d.png'
    .08
    'cg/ep89/christie/2d.png'
    .08



    repeat


image christie_root_45_sex 4_tmp:






    'cg/ep89/christie/1d.png'
    .06
    'cg/ep89/christie/2d.png'
    .06
    'cg/ep89/christie/3d.png'
    .06
    'cg/ep89/christie/4d.png'
    .06
    'cg/ep89/christie/5d.png'
    .06
    'cg/ep89/christie/6d.png'
    .06
    'cg/ep89/christie/5d.png'
    .06
    'cg/ep89/christie/4d.png'
    .06
    'cg/ep89/christie/3d.png'
    .06
    'cg/ep89/christie/2d.png'
    .06



    repeat





image christie_root_45_sex 1 = Composite(
    (1920, 1080),
    (0, 0), 'cg/ep89/christie/bg.png',
    (0, 0), 'christie_root_45_sex 1_tmp'
    )





image christie_root_45_sex 2 = Composite(
    (1920, 1080),
    (0, 0), 'cg/ep89/christie/bg.png',
    (0, 0), 'christie_root_45_sex 2_tmp'
    )



image christie_root_45_sex 3 = Composite(
    (1920, 1080),
    (0, 0), 'cg/ep89/christie/bg.png',
    (0, 0), 'christie_root_45_sex 3_tmp'
    )


image christie_root_45_sex 4 = Composite(
    (1920, 1080),
    (0, 0), 'cg/ep89/christie/bg.png',
    (0, 0), 'christie_root_45_sex 4_tmp'
    )






label christie_root_45:

    $ add_items_for_storein_shop_fixed.remove(don_kihot_at_shop)

    $ del don_kihot_at_shop

    $ events.pop('christie_root_44', 0)

    $ events.pop('christie_root_45', 0)

    $ remove_from_inventory_by_id(22)
    #Description: Подарить Кристи книгу «Дона Кихот» Мигеля Де Сервантеса. 
    #"A Task" ""
    #Активировать спрайт Кристи Утром или Днём. 

   # "Scene" ""
    # 

    #//В этом квесте Кристи в благодарность ГГ сделает ему минет.

    
    #GG_Normal

    #Kristy_Normal

    call show_bg_image_label from _call_show_bg_image_label_181

    show Christie Normal
    show Christie Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left
    
    "[gg]" "Знаешь, Кристи, а ведь я даже не поблагодарил тебя за то, как сильно ты рисковала ради меня, ну и результат – выше всяческих похвал."
    show GG Normal:
        xalign .15
    with my_dissolve
    "[gg]" "Нам лишь остаётся надеяться, что на телефоне есть хотя бы одна фотка, где они целуются."
    show Christie Smile
    "Кристи" "Скромняга. Вжимаясь в угол толчка, ты рисковал не меньше!"
    
    show GG Embarrassment 

    show Christie Laughs
    "Кристи" "Ха-ха-ха!"
    #GG_Chagrin 

    show GG Chagrin 
    "[gg]" "Справедливо."
    show Christie Smile
    "Кристи" "Ладно, не обижайся. Я просто шучу."
    show GG Normal
    "[gg]" "А я нет."
    show GG Normal
    "[gg]" "И в качестве награды, хочу вручить тебе эту замечательную книгу. "
    show Christie Surprise
    "Кристи" "Вааааау!!! Хитроумный идальго Дон Кихот Ламанчский!"
    show GG Normal
    "[gg]" "Я знал, что тебе понравиться."
    show Christie Smile
    "Кристи" "Эксклюзивное издание в твёрдом перелёте. "
    show GG Smile
    "[gg]" "Ага."
    show Christie Smile
    "Кристи" "Уфффффффф!"
    show Christie Smile
    "Кристи" "Как замечательно пахнет свежая бумага. А какая качественная вёрстка, какой шрифт, и даже картинки!"
    show Christie Smile
    "Кристи" "Спасибо, [gg]. Это лучший сюрприз, который я только могла ожидать."
    show GG Embarrassment
    "[gg]" "Что ж… Ты это заслужила."
    show Christie Chagrin
    "Кристи" "Блин, а я вот о подарке не подумала."
    show GG Surprise
    "[gg]" "Разве это я добыл телефон?"
    show GG Surprise
    "[gg]" "Или, может, это я отвлекал продавщицу разговорами?"
    show GG Laughs
    "[gg]" "Моя участь ограничилась выжиданием в туалете, хе-хе."
    show Christie Embarrassment
    "Кристи" "Но…"
    show GG Angry
    "[gg]" "Прекращай оправдываться!"
    show GG Normal
    "[gg]" "Это полностью твоя заслуга, Кристи! И мне не хочется, чтобы ты чувствовала себя виноватой только потому, что я решил сделать тебе приятное."
    show Christie Smile
    "Кристи" "Хорошо-хорошо."
    show Christie Smile
    "Кристи" "Но я всё равно не успокоюсь, пока не отблагодарю тебя как следует! И на то у меня есть свои причины. "
    #GG_Smile

    show GG Smile

    show Christie Normal
    "Кристи" "Той ночью, согласившись переночевать в моей комнате, ты помог мне справиться с нахлынувшими страхами. "
    show Christie Normal
    "Кристи" "Я очень нуждалась в поддержке."
    show Christie Normal
    "Кристи" "Нуждалась в тебе…."
    show GG Embarrassment
    "[gg]" "…."
    show Christie Passion
    "Кристи" "Знаешь, [gg], на самом деле мне первой следовало выразить тебе признательность."
    show GG Embarrassment
    "[gg]" "Ты уже сделала это, Кристи. Та ночь для меня является высшей степенью благодарности. "
    show Christie Passion
    "Кристи" "О нет. Мы же оба знаем, что это была всего-навсего прелюдия. "
    show Christie Passion:
        easein_cubic 3 xalign .5
    show image 'images/cg/ep86/shadow.png':
        alpha 0.0
        easein_cubic 3 alpha 0.7
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/Erotic.mp3', fadein = 1.5)
    "Кристи" "Настоящая награда ждёт тебя здесь и сейчас."
    show GG Embarrassment
    "[gg]" "Звучит как нечто жутко ценное. "

    show image 'images/cg/ep86/shadow.png':
    
        easein_cubic 1 alpha 0.0
    if location_now != 'Sister_Room':
        show Christie Passion

        "Кристи" "Ещё бы. Пошли скорее в мою комнату."
        $ descript_Christie = _('Отправиться в комнату Кристи.')
        if location_now == 'Hall':
            show Christie:
                easein 2 xalign -1.5
            show GG:
                xzoom -1
                easein 2 xalign -1.5
            $ renpy.pause(1.5, hard = True)
        elif location_now == 'Kitchen':
            show Christie:
                xzoom -1
                easein 2 xalign 1.5
            show GG:
                
                easein 2 xalign 1.5
            $ renpy.pause(1.5, hard = True)
            

        if not hasattr(store, 'allowed_events'):
            $ allowed_events = []
        
        $ block_milf_home_christie_root_45    = copy.deepcopy(block_milf_home)
        $ block_time_forward_christie_root_45 = copy.deepcopy(block_time_forward)
        $ block_exit_home_christie_root_45    = copy.deepcopy(block_exit_home)
        $ block_sister_home_christie_root_45  = copy.deepcopy(block_sister_home)

        $ block_milf_home    = True
        $ block_sister_home  = True
        $ block_time_forward = True
        $ block_exit_home    = True
        $ Event('christie_root_45_2', 'Sister_Room')
        $ allowed_events.append('christie_root_45_2')
        
        jump main_interface_label
    else:

        $ christie_root_45_check = True


label christie_root_45_2:
    if not getattr(store, '_just_scene', False):
        if not getattr(store, "from_tyan_mischief_event", False):
            $ location_now = 'Sister_Room'
            if not hasattr(store, 'christie_root_45_check'):
                if not from_gallery_check():

                    $ events.pop('christie_root_45_2', 0)
                    $ allowed_events.remove('christie_root_45_2')
                        
                    $ block_milf_home    = copy.deepcopy(block_milf_home_christie_root_45)
                    $ block_time_forward = copy.deepcopy(block_time_forward_christie_root_45)
                    $ block_exit_home    = copy.deepcopy(block_exit_home_christie_root_45)
                    $ block_sister_home  = copy.deepcopy(block_sister_home_christie_root_45)

                    $ del block_sister_home_christie_root_45

                    $ del block_milf_home_christie_root_45

                    $ del block_time_forward_christie_root_45

                    $ del block_exit_home_christie_root_45

                scene black

                with Dissolve(.5)

                $ renpy.pause(.5, hard = True)

                call show_bg_image_label from _call_show_bg_image_label_182
                with Dissolve(.5)

                $ renpy.pause(.5, hard = True)
                show GG Normal
                show GG Normal at go_from_left



                show Christie Normal 
                show Christie Normal at go_from_left(xxalign = .85, xxzoom = -1)

                $ renpy.pause(.75, hard = True)
                #// GG_Embarrassment выезжает слева

                #// Kristy_Embarrassment выезжает слева
                
            else:

                $ del christie_root_45_check
        else:

            $ location_now = 'Sister_Room'

            call show_bg_image_label from _call_show_bg_image_label_225 
            with Dissolve(.5)

            $ renpy.pause(.5, hard = True)
            show GG Normal
            show GG Normal at go_from_left



            show Christie Normal 
            show Christie Normal at go_from_left(xxalign = .85, xxzoom = -1)

            $ renpy.pause(.75, hard = True)
    elif location_now != "Sister_Room":

        scene black

        with Dissolve(.5)

        $ renpy.pause(.5, hard = True)
    


        $ location_now = 'Sister_Room'

        call show_bg_image_label from _call_show_bg_image_label_226
        with Dissolve(.5)

        $ renpy.pause(.5, hard = True)
        show GG Normal
        show GG Normal at go_from_left



        show Christie Normal 
        show Christie Normal at go_from_left(xxalign = .85, xxzoom = -1)

        $ renpy.pause(.75, hard = True)
    if getattr(store, "_just_scene", False) in (0, False, None, 2):
        show Christie Embarrassment        

        $ renpy.music.stop(fadeout=.5)
        $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
        "Кристи" "Запри дверь."
        show Christie:
            xzoom -1
            easein_cubic 2 xalign 2.5
        with None
        show GG:
            xalign .15
            xzoom -1

        show image 'images/cg/ep86/shadow.png':
            alpha .5
        with Dissolve(.3)
        $ renpy.pause(.75, hard = True)
        play sound 'audio/lock.ogg'
        show Christie:
            xzoom -1
            xalign 1.5
        $ renpy.pause(.5, hard = True)
        
        show Christie Night_Normal
        show Christie Night_Normal:
            xzoom 1 
            easein_cubic 1 xalign .85
        with None
        show GG Embarrassment:
            xzoom 1
        hide image 'images/cg/ep86/shadow.png'
        with my_dissolve
        
        #//GG_Embarrassment исчезает влево

        #//Kristy_Embarrassment исчезает вправо

        #// GG_Embarrassment выезжает слева

        #Kristy_Night_Normal _Embarrassment выезжает справа

        "[gg]" "…."
        show Christie Night_Normal:
            xzoom 1 xalign .85
        with my_dissolve
        "Кристи" "Прекрати на меня так пялиться и снимай одежду. "

        show GG:
            xzoom -1
            easein_cubic 3 xalign -1.5

        $ renpy.pause(1, hard = True)

        show GG Night_Embarrassment:
            xzoom 1
            easein_cubic 2 xalign .1 
        #$ renpy.pause(1, hard = True)

        "[gg]" "Готово…"
        show Christie Night_Passion:
            easein_cubic 3 xalign .5
        show image 'images/cg/ep86/shadow.png':
            alpha .0
            easein_cubic 3 alpha 0.7
        "Кристи" "Теперь присядем."
    if getattr(store, "_just_scene", False) == 2:
        return
    scene black
    with Dissolve(.5)

    $ renpy.pause(.65, hard = True)

    scene christie_root_45 1
    show GG Invis
    show GG Invis:
        xalign .32
    show Christie Invis
    show Christie Invis:
        xalign .72

    with my_dissolve

    #//Kristy_GG_Oral_0

    "[gg]" "Я давно мечтал об этом моменте. "
    "Кристи" "Я знаю, [gg]."
    "Кристи" "Наши желания взаимны."
    "Кристи" "Сейчас меня переполняют эмоции. "
    "Кристи" "Я в растерянности."
    "Кристи" "Боюсь поступить легкомысленно, слишком поспешно…"
    "[gg]" "Я не собираюсь на тебя давить, Кристи."
    "Кристи" "Спасибо…"
    "Кристи" "Я знаю, ты очень нуждаешься в том, чтобы перейти на новый уровень отношений."
    "[gg]" "А ты?"
    "Кристи" "Желаю этого больше всего на свете."
    "Кристи" "Но мне это даётся непросто."
    "Кристи" "Страх перед последствиями сковывает меня. "
    "[gg]" "Я всегда буду с тобой, Кристи. Моя близость, забота, поддержка, я никогда тебя не брошу."
    "Кристи" "Верю. Ты часто врёшь… Лгунишка. Но не сейчас."
    "Кристи" "И всё же, позволь мне сдерживать твои порывы."
    "[gg]" "Мне одеться?"
    "Кристи" "Глупенький. Я не это имела в виду."
    "Кристи" "Дело в том, что я…"
    "Кристи" "Девственница. "
    "Кристи" "И ещё не готова к…  Ну ты понял."
    "[gg]" "Ага."
    "Кристи" "Однако я очень хочу сделать тебе приятно. "
    "[gg]" "Но ведь удовольствие должны получить мы оба, верно?"
    "Кристи" "Свою порцию наслаждения я не упущу, [gg]."#/*братик
    "Кристи" "Отклонись пожалуйста назад."
    "[gg]" "Как скажешь…"
    #//Kristy_GG_Oral_1

    show christie_root_45 2
    with Dissolve(.5)

    $ renpy.pause(.75, hard = True)

    show christie_root_45 3
    with my_dissolve
    
#christie_root_45_sex 1_tmp
    "Кристи" "Как приятно он пахнет."
    "[gg]" "С-спасибо."
    "Кристи" "Я только прикоснулась к нему, как он задрожал, хи-хи."
    "Кристи" "Тебя это заводит, верно?"
    "[gg]" "Меня заводишь ты, Кристи."

    show christie_root_45 4
    with my_dissolve
    "Кристи" "Тогда держись крепче, [gg], сейчас я продемонстрирую, как завелась я."#/*братик
    #//Kristy_GG_Oral_Animation
    scene christie_root_45_sex 1
    show GG Invis
    show GG Invis:
        xalign .32
    show Christie Invis
    show Christie Invis:
        xalign .72

    with my_dissolve
    "[gg]" "Ох чёрт… Я чуть не кончил от счастья."
    "Кристи" "Мгл-мгл-мгл…"
    "[gg]" "Не торопись, Кристи, я буквально на грани."#/*сестрёнка
    "[gg]" "Ощущать членом твой рот непередаваемое блаженство."
    "[gg]" "Мне нужно время, чтобы сконцентрироваться и кончить раньше времени…"
    "[gg]" "Это слишком…  Слишком хорошо, чтобы быть правдой. "
    #//мысли
    show shadow_full with my_dissolve
    "Кристи" "{i}[gg] такой милый, когда стесняется.{/i}"
    "Кристи" "{i}Я рада, что он с таким энтузиазмом воспринял моё предложение.{/i}"
    "Кристи" "{i}Его перевозбуждённый член со стекающими соками из головки нежно ласкает мою нёбу.{/i}"
    "Кристи" "{i}Наверняка он сходит с ума от удовольствия, хи-хи.{/i}"
    "Кристи" "{i}Столько раз домогался меня и вот, наконец-то, я снизошла своим ротиком до его дружка.{/i}"
    "Кристи" "{i}Его дёрганные движения мне в горло такие забавные. Хочется глотать всё глубже и глубже.{/i}"
    #//мысли закончены

    hide shadow_full with my_dissolve
    #//Ускориться х2
label christie_root_45_menu:

    menu:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            $ pass
            window hide
            $ renpy.pause(9999)
            jump christie_root_45_menu
    scene christie_root_45_sex 2
    show GG Invis
    show GG Invis:
        xalign .32
    show Christie Invis
    show Christie Invis:
        xalign .72
        
    with my_dissolve
    "[gg]" "Оооо даааа! Продолжай! Кажется, я словил необходимый ритм."
    "[gg]" "У тебя настоящий талант, Кристи."#/*сестрёнка
    "[gg]" "Твои влажные губы словно растекаются по моему члену, а внутри я ощущаю нирвану…"
    #//мысли

    show shadow_full with my_dissolve
    "Кристи" "{i}Хи-хи-хи!{/i}"
    "Кристи" "{i}Его щенячья благодарность не знает границ.{/i}"
    "Кристи" "{i}В такой момент можно просить его о чём угодно, едва ли ему хватит силы воли отказать.{/i}"
    "Кристи" "{i}Но мне незачем это делать. Я люблю его, и мне приятно удовлетворять его разбушевавшуюся похоть.{/i}"
    "Кристи" "{i}Он столько трудился, чтобы добиться моего расположения…{/i}"
    "Кристи" "{i}Так старался угождать и аккуратно следовал моим напутствиям…{/i}"
    "Кристи" "{i}Прислушивался к моему мнению…{/i}"
    "Кристи" "{i}Он на всё готов ради меня.{/i}"
    "Кристи" "{i}А я – ради него.{/i}"
    "Кристи" "{i}Глотать его сладкий член, трепетно вылизывая каждый миллиметр его кожи, мне только в удовольствие.{/i}"
    "Кристи" "{i}Оу!…{/i}"
    "Кристи" "{i}И судя по тому, как он усиливает свои импульсы у меня во рту, [gg] полностью согласен с моей точкой зрения.{/i}"#/*братик
    #//мысли закончены

    hide shadow_full with my_dissolve
    #//Скорость х3
label christie_root_45_menu_2:

    menu:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            $ pass
            window hide
            $ renpy.pause(9999)
            jump christie_root_45_menu_2
    scene christie_root_45_sex 3
    show GG Invis
    show GG Invis:
        xalign .32
    show Christie Invis
    show Christie Invis:
        xalign .72
        
    with my_dissolve
    "[gg]" "Охххх… Да-да-да!"
    "[gg]" "Такой бодрый темп мне по душе!"
    "[gg]" "Пожалуй, глотай его глубже. Ещё! Ещё сильнее!"
    "[gg]" "Катарсис уже близко…"
    #//мысли

    show shadow_full with my_dissolve
    "Кристи" "{i}Ещё немного, и он залетит мне членом в самую глотку.{/i}"
    "Кристи" "{i}И раз уж таково его желание, то почему бы и нет.{/i}"
    "Кристи" "{i}Я уже чувствую, как сильно пульсирует его головка. Ещё мгновение, и он зальёт мне спермой весь рот.{/i}"
    "Кристи" "{i}Нужно продолжать сосать, и чем сильнее, тем яростней он кончит.{/i}"
    "Кристи" "{i}Хочу поскорее испробовать его молочко на вкус.{/i}"
    hide shadow_full with my_dissolve
    #//мысли закончены
label christie_root_45_menu_3:

    menu:
        "Кончить":
            $ pass
        "Продолжить в том же темпе":
            $ pass
            window hide
            $ renpy.pause(9999)
            jump christie_root_45_menu_3
    scene christie_root_45_sex 4
    show GG Invis
    show GG Invis:
        xalign .32
    show Christie Invis
    show Christie Invis:
        xalign .72
        
    with my_dissolve
    #//Кончить

    #//Скорость х4

    "[gg]" "Я готов. Я уже совсем готов!"
    "[gg]" "Позволь мне кончить тебе в рот, Кристи!"#/*сестрёнка
    "Кристи" "Мгл-мгл!"
    
    
    scene christie_root_45_sex end_1
    show GG Invis
    show GG Invis:
        xalign .32
    show Christie Invis
    show Christie Invis:
        xalign .72
    with my_dissolve
    "[gg]" "Даааааааааааа!!!!"
    #//Kristy_GG_Oral_2
    "[gg]" "Просто невероятно…"

    scene christie_root_45_sex end_2
    show GG Invis
    show GG Invis:
        xalign .32
    show Christie Invis
    show Christie Invis:
        xalign .72
    
    #//мысли
    show shadow_full 
    with my_dissolve
    "Кристи" "{i}Вау!{/i}"
    "Кристи" "{i}Он влил в меня литр спермы, чёрт возьми! Просто обалдеть!{/i}"
    "Кристи" "{i}Ммммм… Такая густая и вкусная.{/i}"
    "Кристи" "{i}Я определённо довольна результатом.{/i}"
    #//мысли закончены
    hide shadow_full with my_dissolve
    #//Kristy_GG_Oral_3

    "Кристи" "Ты как, [gg]?"#/*братик
    "[gg]" "У меня нет слов… Это нужно обязательно повторить. И не раз. Если ты не против, конечно."
    "Кристи" "Хи-хи-хи."
    "Кристи" "Я только за!"
    if getattr(store, '_just_scene', False):
        $ _just_scene = False
        scene black with Dissolve(.25)
        $ renpy.pause(.25, hard = True)
        $ renpy.pause(.5)

        $ location_now = "Corridor"
        
        $ time.time_forward(jump_to_main_interface = False)
        jump main_interface_label

    scene black with Dissolve(.5)

    if getattr(store, "from_tyan_mischief_event", False):
        $ from_tyan_mischief_event = False
        return

    $ renpy.pause(1, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_183
    show GG Night_Normal
    show GG Night_Normal:
        xalign .2
    show Christie Night_Normal
    show Christie Night_Normal:
        xalign .8
    with Dissolve(.5)
    #//KristyRoom

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/full-moon-lofi-vibes-by-edikey20-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Пора одеваться."
    show Christie Night_Normal 
    "Кристи" "Ага."
    #//Стук в дверь
    play sound 'audio/door_knock.mp3'

    #Тук-тук-тук!
    $ renpy.pause(.75, hard = True)
    #Milf_Normal выезжает справа

    #//GG_Night_Normal _Embarrassment перемещается к спрайту Кристи вправо и поворачивается лицом к Милфе

    show Milf Normal
    show Milf Normal: 
        xzoom -1 xalign -0.5
        easein_cubic 1 xalign .15

    show GG Night_Embarrassment:
        easein 2 xalign .7
        xzoom -1
    
    show Christie:
        easein 2 xalign .95
    
    "Марина" "Можно войти? "
    show Christie Night_Angry 
    "Кристи" "Ты уже вошла, Марина!"
    show Milf Normal: 
        xzoom -1 xalign .15
        
    "Марина" "Да, извини, просто хотела попросить тебя сходить в магазин за продуктами."
    show GG:
        xzoom -1
        easein 1 xalign .95
    show Christie Night_Angry:
        easein 1 xalign .7

    "Кристи" "По твоему, нарушив мои личные границы, я стану помогать тебе?"
    show Milf Angry
    "Марина" "Слушай, деточка, я уже извинилась."
    show Milf Angry
    "Марина" "И если ты не хочешь остаться без ужина, я советую мигом сгонять в супермаркет!"
    show GG:
        xzoom -1
        xalign .95
    show Christie Night_Angry:
        xalign .7

    with my_dissolve
    "Кристи" "Ладно!!!"
    show Milf Laughs
    "Марина" "Ну вот, другое дело."
    show Milf Surprise
    "Марина" "И кстати, почему вы нижнем белье?"
    #Kristy_Night_Normal _Surprise

    show Christie Night_Surprise:

        easein 1 xalign .95

    show GG:

        easein 1 xalign .7 
    "[gg]" "Я собирался идти в душ и зашёл к Кристи попросить у неё полотенце, а оказалось, что она и сама собирается пойти искупаться. "
    show Milf Normal
    "Марина" "Хм… "
    show Milf Normal
    "Марина" "Какое нелепое совпадение."
    
    show GG Night_Normal:
        xalign .7 
    show Christie:

        xalign .95
    with my_dissolve
    "[gg]" "Вот и я так подумал. "
    show Milf Normal
    "Марина" "Хорошо, я пошла…"
    show Milf:
        xzoom 1
        easein 2 xalign -1.5
    show GG:
        easein 1 xalign .2
        xzoom 1
    show Christie:
        easein 1 xalign .7
    $ renpy.pause(1, hard = True)
    #//Milf_Normal  исчезает влево

    #//GG_Night_Normal _Normal двигается на место Милфы
    hide Milf
    show Christie:
        xalign .7
    show GG Night_Normal:
        xalign .2
        xzoom 1
    with my_vpunch
    "[gg]" "Чуть не попались!"
    show Christie Night_Normal:
        xzoom 1 xalign .7 
    show GG:
        xzoom 1 xalign .2 
    "Кристи" "Ага, нам повезло, что она не заметила твои разбросанные вещи на полу. "
    show Christie Night_Laughs
    show GG Night_Surprise:
        xalign .2
    with my_vpunch
    
    "[gg]" "Чёрт!!! А ведь и вправду!"
    show Christie Night_Chagrin:
        xalign .7
    with my_dissolve
    "Кристи" "Вот этого я и боюсь, [gg]. "
    #GG_Night_Normal _Normal

    show Christie Night_Chagrin
    "Кристи" "Рано или поздно всё тайное станет явным. "
    show GG Night_Normal 
    "[gg]" "И когда это случится, мы будем готовы. Верно я говорю?"
    show Christie Night_Embarrassment
    "Кристи" "Надеюсь…."
    #//GG_Night_Normal _Normal исчезает влево
    show GG:
        xzoom -1
        easein 1 xalign -.5
    show Christie:
        xzoom -1
        easein 1 xalign 1.5
    $ renpy.pause(1.5, hard = True)
    #//GG_Normal появляется слева (типа переоделся)
    show GG Normal:
        xzoom 1
        easein 1 xalign .2
    show Christie Normal:
        xzoom 1
        easein 1 xalign .8
        
    "[gg]" "Ну, я пошёл. Нужно разобраться с телефоном. "
    show GG Normal:
        xalign .2
    show Christie Normal:
        xalign .8 xzoom 1
    with my_dissolve
    "Кристи" "Ага, увидимся. "
    
    
    #"Time" "Evening"
    
    #Tian_46

    if not from_gallery_check() and not getattr(store, '_just_scene', False):

        $ add_to_gallery(35)
        scene black with Dissolve(.5)

        $ renpy.pause(.5, hard = True)
        $ descript_Christie = _("Сходить к Игорю к Парк и попросить его взломать телефон продавщицы.")
        if getattr(store, 'block_igor_position', False):

            $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")

        #$ events['christie_root_42'].day_start = time.day_now + 1
        #jump main_interface_label
        if not getattr(store, 'block_time_forward', False):
            $ time.time_now = 'evening'

        $ location_now = 'Corridor'

        
        
        
        $ Event('christie_root_46', location = 'Igor')

    else:
        $ _just_scene = False

    jump main_interface_label