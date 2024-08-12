

label start:
    $ from_say_screen = False
    $ sex_name_box    = False
    $ fix_saves_23_6_23 = True
    call variables_at_start from _call_variables_at_start_1
    $ _after_load_from_start = True
    call after_load from _call_after_load
    python:
        try:
            del _after_load_from_start
        except:
            pass


    if persistent.from_main_menu_gallery:
        $ from_say_screen = True
        if mp.gg:
            $ gg = mp.gg
        else:
            if preferences.language in (None, 'rus'):
                $ gg = 'Семён'
            elif True:
                $ gg = 'Donald'
        $ player_name = gg
        $ nameboxes['GG'].name = gg
        $ nameboxes['GG'].text_obj = Text(
            gg, 
            color    = '#e5e349', 
            outlines = [(2, "#000a", 0, 0),], 
            size     = 30 
            )
        $ nameboxes['GG'].create_text_obj()
        $ renpy.jump(persistent.from_main_menu_gallery)




    $ not_survival = False

    $ tmp_menu_info = [
    __('Эта функция может противоречить пройденным или будущим квестам в игре, и работает исключительно для тестирования НОВОГО КОНТЕНТА. Пожалуйста, если будете слать отчёты об ошибке, уточняйте, что начали прохождение с помощью этого режима!'),
    
    __(''),


    ]
    scene image 'gui/game_menu.png'
    with Dissolve(.5)
    # menu:
    #     #"Начать с эпизода 0.9" if True:

    #          #$ custom_load_from_file('ep86')
            
    #     #    $ custom_load(ep09_line)

    #     "Начать с эпизода 1.0.7" if True:

    #          #$ custom_load_from_file('ep86')
            
    #         $ custom_load(ep_1_0_line)    

    #     "Начать с начала" if True:
    #         $ pass

    $ tmp_menu_info = [
    _('Тот самый симулятор свиданий, который вы ожидаете от игрового процесса. Чтобы чувствовать себя комфортно, вам необходимо будет кушать, спать и держать себя в чистоте. \nА девушки, с которыми вы планируете завести роман, потребуют от вас чуть больше внимания, прежде чем откроют вам своё сердце.  \nТолько в этом режиме достижение целей будет приносить вам истинное наслаждение от приложенных усилий.'),
    _('Это всё ещё песочница, но без необходимости "выживать" и "ухаживать" за дамами. Без каких-либо задержек вы активируете сюжетные сцены. \nРазве что деньги всё ещё нужно зарабатывать, поскольку добыча средства завязана на сюжете.'),


    ]
    menu:
        "Классика" if True:
            $ pass



        "История (Только сюжет)" if True:



            $ not_survival = True
    $ del tmp_menu_info









    'Texic' "Привет, ребята! Меня зовут Texic. Я автор веб-комиксов, наиболее известный по серии «Сладкий кексик»."

    'Texic' "Рад представить вам свою игру для взрослых в жанре «симулятор свиданий». На данный момент вы смотрите версию [version_now]."
    
    'Texic' "Впереди ещё много работы и много прекрасных историй."
    
    scene expression '#000' with Dissolve(1)

    $ renpy.pause(1, hard = True)
    #if preferences.language in (None, 'eng', 'rus'):
    call prologue from _call_prologue





    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(1, hard = True)




    scene expression 'locations/bg/'+str(locations[location_now].bg)+'/'+time.time_now+'.png'
    show GG B_Chagrin
    show GG B_Chagrin at go_from_left(xxalign = -.1, ttimer = 2)
    show Officer Normal
    show Officer Normal at go_from_left(xxalign = .2, ttimer=1.5)
    show Milf Normal
    show Milf Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    play music 'audio/game_start.mp3' fadein 1.5   
    'Офицер' "Вы позволите?"
    show GG B_Chagrin:
        xalign -.1

    show Officer Normal:
        xalign .2

    show Milf Surprise
    with my_dissolve
    'Марина' "Да-да, конечно, проходите. А что, простите, происходит?"
    'Офицер' "Вас зовут Марина?"
    show Milf Normal
    'Марина' "Верно."
    'Офицер' "Вам знаком этот молодой человек?"
    'Марина' "Конечно, это мой…"




    'Марина' "Это брат моего мужа. Он живёт со мной, пока Джеймс в командировке. "
    'Офицер' "Я так и думал."
   # show screen give_item_screen(i_path+'/items/ticket.png', _("Билеты"), [_("Билеты"), _("Театральные билеты на постановку «Кошки».")])

    'Офицер' "Полагаю, имя его вам тоже знакомо?"
    show Milf Angry
    'Марина' "Вы издеваетесь? "
    show Milf Normal
    'Офицер' "Назовите имя, пожалуйста."

    if preferences.language in (None, 'rus'):

        $ gg = renpy.input('Введите имя вашего Героя', default='Семён')
    elif True:

        $ gg = renpy.input('', default='Donald')


    if not len(gg):
        if preferences.language in (None, 'rus'):
            $ gg = 'Семён'
        elif True:

            $ gg = 'Donald'
    $ gg = gg.title()
    $ mp.gg = gg
    $ mp.save() 

    
    $ player_name = gg

    $ nameboxes['GG'].name = gg
    $ nameboxes['GG'].create_text_obj()
    
    'Марина' "Его зовут [gg]! "

    show Milf Angry
    'Марина' "Теперь вы можете сказать, что, чёрт возьми, здесь творится?!"
    'Офицер' "Данный гражданин обвиняется в мелкой краже."
    show Milf Surprise
    'Офицер' "Ваш друг и кто-то из его друзей, пытались незаметно вынести несколько дорогостоящих часов из ювелирного магазина. "
    'Марина' "Какой стыд… Это правда, [gg]?"
    show GG B_Embarrassment
    '[gg]' "Правда…"

    show Milf Chagrin
    'Офицер' "Как вы можете заметить, ваш деверь ещё не в тюрьме."
    show Milf Gipno
    "[gg]" "{i}Интересно, за какие такие заслуги?..{/i}"
    'Офицер' "Следовательно, его проступок не настолько страшен, но и не настолько мал, чтобы правосудие оставило его в покое."


    'Офицер' "К тому же, я живу по соседству, и знаю, что вы приличная и добропорядочная женщина. Хочется верить, что и брат вашего мужа всего-навсего немного оступился."
    
    
    'Марина' "И что же от меня требуется?"
    'Офицер' "Во-первых, следить за тем, чтобы такого больше не повторилось. "
    'Офицер' "Для надёжности, мы поставили его на учёт. И если он вновь будет замечен в нарушении закона, он отправится в тюрьму."
    show GG B_Angry
    show Milf Surprise
    'Марина' "А что во-вторых? "
    show Milf Gipno
    'Офицер' "В ближайшие несколько недель судья приговорил его к общественным работам. "
    'Офицер' "Но не волнуйтесь, никто его не принуждает копать окопы или отрабатывать грузчиком. [gg] будет поддерживать чистоту в местном парке: мести дорогу и подбирать мусор."
    show GG B_Chagrin
    'Офицер' "Когда он закончит, ему следует отчитаться."
    'Офицер' "На всякий случай я оставлю свой адрес и телефон. Звоните, если заметите, что ваш приятель нарушает назначенное ему предписание.  "
    show Milf Normal
    'Марина' "Спасибо вам, [gg] обязательно позвонит вам!"
    show GG B_Embarrassment
    '[gg]' "…"
    #hide window
    #with my_dissolve 



    show Officer Normal:
        easeout 1.5 xalign 1.6

    show GG B_Chagrin:
        easein 1.0 xalign .15
    $ renpy.pause(.5, hard = True)
    $ from_say_screen = False
    $ renpy.pause(1.0, hard = True)
    show Milf Angry
    'Марина' "Ну, и что ты молчишь?!"

    "[gg]" "Разве есть смысл оправдываться?"
    hide Officer

    show GG:
        xalign .15
    
    with my_vpunch
    "Марина" "Как хочешь!"

    "Марина" "Я тебе не мать. Можешь хоть сейчас валить на все четыре стороны."

    "Марина" "Но если в мой дом продолжат являться полицейские и допрашивать, я бы попросила тебя съехать!"
    
    "Марина" "Уверена, Джеймс меня поймёт."

    show GG B_Embarrassment
    with my_dissolve
    "[gg]" "Я не хотел, чтобы так случилось, извини…"

    "Марина" "…"

    "Марина" "Очередные извинения. Снова и снова. Как будто это что-то меняет."

    "[gg]" "…."

    show GG B_Chagrin
    with my_dissolve
    "[gg]" "Мне сложно подобрать слова."

    "Марина" "Зато легко быть полным придурком."

    show GG B_Angry
    with my_vpunch
    "[gg]" "Эй!.."

    "Марина" "Да что с тобой не так, [gg]?"

    show Milf Chagrin
    with my_dissolve

    "Марина"  "Джеймс доверяет тебе. "

    "Марина" "Он наивно полагает, что у тебя трудный период. Дескать, рано или поздно ты образумишься и пойдёшь по его стопам. Ха!"

    "Марина" "Но я не дура и не ослеплена к тебе «братской» любовью. "

    show GG B_Chagrin
    with my_dissolve
    "Марина" "Я согласилась на твоё пребывание здесь только по просьбе мужа."

    show Milf Angry
    with my_dissolve
    "Марина" "Ещё одна такая выходка, и чтоб ноги твоей здесь не было!"

    show GG B_WTF
    with my_dissolve
    "[gg]" "Да, мэм. "

    "Марина" "И приведи себя в порядок, наконец. "

    "Марина" "Ты выглядишь как оборванец, а мне неприятно видеть бомжа у себя дома."

    "[gg]" "Хорошо…"

    $ from_say_screen = False
    show GG:
        easeout 1.0 xalign .5
    show Milf Normal:
        xzoom -1
        easeout 1.0 xalign 1.6
    $ renpy.pause(.75, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_177
    with Dissolve(.5)
    $ descript = _('Сегодня я уже достаточно «нагулялся». Следует почистить зубы, побриться и лечь спать.')



    if getattr(store, 'not_survival', False):
        $ gigiena = 100
        $ sitost  = 100
        $ nastroi = 100
    #$ Event('ep1_prologue_milf', 'Milf')
    $ block_milf_events = 'ep1_prologue_milf'
    #$ block_milf_home = True
    call player_pool from _call_player_pool
    #show image 'interface/tutorial.png'
    # with my_dissolve
    # $ renpy.pause(.75, hard = True)
    if preferences.language in (None, 'eng', 'spn', 'rus'):
        call screen tutorial_screen

    jump main_interface_label

label ep1_prologue_milf:

    call show_bg_image_label from _call_show_bg_image_label_229 

    call show_additional_images_label from _call_show_additional_images_label_114 

    show Milf Night_Normal
    show Milf Night_Normal:
        xalign .75
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    show GG B_Chagrin

    show GG B_Chagrin at go_from_left
    "Марина" "Ты уже сделал, что я сказала?"    
    "[gg]" "Ещё нет."
    
    show Milf Night_Angry
    "Марина" "Тогда чего же ты меня донимаешь? Не мешай мне смотреть фильм."

    "[gg]" "Извини…"

    jump main_interface_label
label ep1_gg_crane_label:


   # show expression 'images/cg/gg_activities/gg_shave_restroom_4.png'

    show expression 'images/cg/gg_activities/gg_shave_restroom_1.png'
    with my_dissolve

    '[gg]' "Какой смысл чистить зубы перед сном, если утром их снова придётся драить? Ох уж эти дурацкие правила гигиены."

   # hide expression 'images/cg/gg_activities/gg_shave_restroom_4.png'



    #with my_dissolve
    "[gg]" "Воу…"

    "[gg]" "Я действительно выгляжу как кусок дерьма."

    #"[gg]" "Не то, чтобы внешность человека как-то отражала его внутренний мир, но в моём случае это именно так."

    "[gg]" "Вот бы измениться было бы так же легко, как сбрить бороду или подстричься…"

    "[gg]" "Что ж… Начну хотя бы с этого."

    hide expression 'images/cg/gg_activities/gg_shave_restroom_1.png'

    show expression 'images/cg/gg_activities/gg_shave_restroom_2.png'


    with Dissolve(.25)
    $ renpy.pause(.5, hard =True)
    hide expression 'images/cg/gg_activities/gg_shave_restroom_2.png'

    show expression 'images/cg/gg_activities/gg_shave_restroom_3.png'


    with Dissolve(.25)
    $ renpy.pause(.5, hard =True)
    hide expression 'images/cg/gg_activities/gg_shave_restroom_3.png'

    show expression 'images/cg/gg_activities/gg_shave_restroom_4.png'


    with Dissolve(.25)
    $ renpy.pause(.5, hard =True)

    "[gg]" "Хех, так-то намного лучше."

    "[gg]" "По крайней мере я не вызываю омерзения у самого себя."

    "[gg]" "Даже возникает вопрос… "

    "[gg]" "Это повод стать лучше или хорошая маскировка для подлости?"

    "[gg]" "…Ну да, самое время об этом думать, прежде чем меня укакошат или посадят в тюрячку."



    $ Event('ep1_1_first_talk_with_christie',     'Corridor')

    $ show_text_animation('+50 gigiena')

    $ gigiena       = min(100,  gigiena+50)
    $ block_gigiena = True

    $ block_milf_home = False

    $ locations['Restroom'].buttons[0]['Crane'] = (((1312, 560, 289, 70), [Jump('restroom_crane_label')]))

    $ time.time_now = 'night'
    $ block_milf_events = None
   # $ events.pop('ep1_prologue_milf', 0)
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
