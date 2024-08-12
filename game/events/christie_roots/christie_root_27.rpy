
label christie_root_27_activate:
    $ christie_root_27_start = True
    $ descript_Christie      = _("Сходить на сеанс к Сьюзан.")
    $ Event('christie_root_27', 'City_Psi', time = ['morning', 'afternoon'])
    $ events.pop('christie_root_21', 0)
    $ events.pop('christie_root_22', 0)
    $ events.pop('christie_root_23', 0)
    $ events.pop('christie_root_24', 0)
    $ unlock_city_psi   = True
    return

label christie_root_27_repeat:
    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    scene expression 'cg/christie_root/Psi_Build.png'
    with Dissolve(.25)

    $ renpy.pause(.25, hard = True)

    call screen rtrn_screen('cg/christie_root/Psi_Build_Door.png')

    scene black with Dissolve(.25)
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    scene expression 'cg/christie_root/psi_corridor.png'
    with Dissolve(.25)
    $ renpy.pause(.5, hard = True)
    call screen rtrn_screen

    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    $ events.pop('christie_root_27_repeat', 0)

    scene black with Dissolve(.5)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    $ renpy.pause(.5, hard = True)

    scene expression 'cg/christie_root/psi_corridor.png'
    show Psi Normal
    show Psi Normal:
        xalign .5
        ypos 1085

    with Dissolve(.5)


    show GG Normal
    show GG Normal at go_from_left


    "Сьюзан" "[gg], теперь ты готов для первого сеанса?"



    jump christie_root_27_menu_1


label christie_root_27:




    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    scene expression 'cg/christie_root/Psi_Build.png'
    with Dissolve(.25)

    $ renpy.pause(.25, hard = True)

    call screen rtrn_screen('cg/christie_root/Psi_Build_Door.png')

    scene black with Dissolve(.25)
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    scene expression 'cg/christie_root/psi_corridor.png'
    with Dissolve(.25)
    $ renpy.pause(.5, hard = True)
    call screen rtrn_screen

    if not from_gallery_check():
        $ events.pop('christie_root_27', 0)
    show Psi Normal
    show Psi Normal:
        xalign .5
        ypos 1085

    with Dissolve(.5)


    show GG Smile
    show GG Smile at go_from_left

    
    "[gg]" "Здравствуйте, Сьюзан. Я снова к вам!"
    show GG:
        xalign .15
    with my_dissolve
    "Сьюзан" "Всегда добро пожаловать, [gg]. "

    "Сьюзан" "Ты подготовил денюжку?"



label christie_root_27_menu_1:


    show GG:
        xalign .15
    with my_dissolve



    menu:
        "!1. «Да, вот» (-75 долларов)" if money < 75:
            $ pass
        "1. «Да, вот» (-75 долларов)" if money >= 75:
            $ pass

        "2. «Нет, забыл»" if True:
            call check_gallery_label from _call_check_gallery_label_16
            $ location_now = 'Corridor'
            $ unlock_city_psi   = True


            $ Event('christie_root_27_repeat', 'City_Psi', time = ['morning', 'afternoon'])



            show Psi Chagrin
            "Сьюзан" "Очень жаль, [gg]. Надеюсь, в следующий раз у тебя будет нужная сумма. "
            show GG WTF
            "[gg]" "Обязательно!"
            scene black with Dissolve(.5)
            jump main_interface_label
    $ money -= 75
    $ show_text_animation('-75$')
    scene black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "[gg]" "В последний раз вы упоминали о какой-то работе для меня."
    "Сьюзан" "Да, но прежде я хочу послушать тебя."
    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve

    "Сьюзан" "Признаюсь, я очень соскучилась по нашим сеансам."
    "[gg]" "К сожалению, Сьюзан, сейчас я нуждаюсь в них как никогда кстати."
    "Сьюзан" "Оу. Я польщена. Дай угадаю, это из-за Кристи?"
    "[gg]" "Да..."
    "[gg]" "Но как вы догадались?"
    "Сьюзан" "Ну, во-первых, результат нашей терапии ты расходуешь не на личностный рост, а на отношения с Кристи, и только с ней у тебя могут возникнуть проблемы."
    "[gg]" "А во-вторых?"
    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "Сьюзан" "Я квалифицированный психолог, как никак."
    "Сьюзан" "Ха-ха-ха!"
    "[gg]" "Хех... Вы правы."
    "[gg]" "Пожалуй, всё куда сложнее, чем я думал."
    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "[gg]" "Мне стыдно признаваться в этом и хочется верить, что всё здесь услышанное вы унесёте с собой в могилу"
    "Сьюзан" "Ох, клянусь, как только я допишу свои мемуары, то тут же сожгу все рукописи."
    "[gg]" "Вы издеваетесь?"
    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "Сьюзан" "Ты у психолога, [gg], ясное дело, что я никому ничего не выдам."
    "[gg]" "Даже если я убил человека?"
    "Сьюзан" "А ты убил?"
    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "[gg]" "Нет, чёрт возьми!"
    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "Сьюзан" "Ну вот, тебе нечего бояться."
    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "[gg]" "Да уж..."
    "[gg]" "Ладно, держать себе это становится невыносимо."
    "Сьюзан" "Я заинтригована."
    "[gg]" "Я это почувствовал ещё после первой нашей встречи, и чем дальше, тем сильнее меня преследовали эти чувства..."
    "Сьюзан" "...."
    "[gg]" "И теперь, когда я здесь, с вами наедине, меня распирает чисто сердечно признаться...."
    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "Сьюзан" "Уверяю тебя, [gg], ты можешь быть полностью откровенен со мной."

    "[gg]" "Короче говоря, меня тянет к Кристи. Вот!"
    "Сьюзан" "Хм..."
    "Сьюзан" "Полагаю, речь идёт не о платонической тяге. Я верно тебя понимаю?"
    "[gg]" "Верно."
    "Сьюзан" "Как интересно..."
    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "[gg]" "Интересно?! Это ужасно! Как на это отреагирует Марина?! А мой брат?.."
    "[gg]" "Я пропал."
    "Сьюзан" "Не кори себя раньше времени, [gg], ты ещё не сделал ничего дурного."
    "[gg]" "В том-то и дело - сделал!"
    "Сьюзан" "Оу!"
    "[gg]" "Ага."
    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "Сьюзан" "Значит, у вас уже была интимная связь?"
    "[gg]" "Ну, в какой-то степени."
    "Сьюзан" "Что-то вроде прелюдий?"
    "[gg]" "Типа того."
    "Сьюзан" "А Кристи? Она отвечает тебе взаимностью?"
    "[gg]" "И да, и нет. Она боится этих чувств ровно так же, как и я. Мы оба понимаем, что это неправильно."
    "Сьюзан" "Почему ты считаешь, что ваш роман будет воспринят отрицательно?"
    "[gg]" "Ну, хотя бы потому, что она дочка жены моего брата."
    "Сьюзан" "Приёмная, насколько мне известно."
    "[gg]" "Да."
    "Сьюзан" "Полагаю, твой брат будет против вашего... романа."
    "[gg]" "Все, кого я знаю, выступили бы против."
    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзан" "Хм..., Пожалуй, ты прав, ситуация сложная."
    "Сьюзан" "Мы часть социума, разумеется, и нормы культуры и даже аспекты бытовой жизни определяется большинством."
    "Сьюзан" "Как, например, положение женщин в 18м веке, или рабство, отменённое буквально сто лет назад."
    "Сьюзан" "Но мир изменчив. Не говоря уж о том, что все эти \"нормы\" абсолютно иллюзорны, и держатся исключительно на лицемерии, мнимом ощущении безопасности."
    "Сьюзан" "А некоторые из этих \"норм\" даже обрамляют в уголовные законы, принуждая людей, что никак не нарушают права и свободы другого человека, исполнять волю большинства."
    "Сьюзан" "При этом, как мы ежедневно наблюдаем, даже самые нравственные представители общества, с лёгкостью нарушают собственные принципы, установки и, конечно же, закон."
    "[gg]" "Как я? Хе-хе."
    "Сьюзан" "Или мой муж."
    "[gg]" "Что!?"
    "Сьюзан" "Теперь и я тебя заинтриговала."
    "[gg]" "Ваш муж нарушает закон?"
    "Сьюзан" "Ах, если бы."
    "Сьюзан" "Он изменяет мне."
    "[gg]" "Воу... Сочувствую."
    "Сьюзан" "Спасибо, [gg]."
    "Сьюзан" "Ну вот, теперь мы можем обсудить работу."
    "Сьюзан" "Которая, напомню, сможет поддержать в тебе здоровый потенциал авантюриста, не превращая тебя в бандита или, если рассматривать через призму общества - не делая тебя плохим человеком."


    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Смотря с какой стороны общества."
    "Сьюзан" "Сторону общества, поощряющую или оправдывающую измену я не рассматриваю."
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .5
    with my_dissolve
    "[gg]" "{i}Хотел бы сказать \"Удобно\", но промолчу. {/i}"
    "[gg]" "{i}Судя по всему она чертовски зла на мужа. {/i}"
    hide expression 'cg/ep45/shower_3/shadow.png'
    with my_dissolve
    "Сюзен" "Я с радостью готова принимать тебя бесплатно, [gg], если, конечно, ты готов оказать мне маленькую услугу."

    "[gg]" "Какую?"
    "Сюзен" "Мне нужно, чтобы ты проследил за моим мужем и запечатлел на фото, с кем именно у него роман."
    "Сьюзан" "Это, я уверена, хорошо поспособствует твоей самореализации авантюриста."

    "Сьюзан" "А если ты ещё решишь взять с собой Кристи, то сможешь на практике продемонстрировать ей, твоя метаморфоза пошла на пользу обществу."

    "[gg]" "То есть вам."
    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзан" "То есть мне."

    "[gg]" "Звучит чрезвычайно любопытно."
    "[gg]" "Такая работа меня прельщает."
    "Сьюзан" "Прекрасно."
    "Сьюзан" "Я хочу подать на развод, но не могу это сделать необоснованно."
    "[gg]" "Вы не знаете, с кем изменяет ваш муж?"
    "Сьюзан" "К сожалению, нет."

    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Тогда как вы можете быть уверены?"
    "Сьюзан" "Ну, во-первых, у нас за плечами 15 лет брака."


    "[gg]" "А во-вторых, вы квалифицированный психолог."
    "Сьюзан" "Ха! Ты схватываешь на лету."
    "Сюзен" "Ну так что, идёт?"
    "[gg]" "Надо подумать...."
    "Сьюзан" "Подумай-подумай."
    "Сьюзан" "Дай мне пожалуйста ответ на следующем сеансе. Сегодня, пожалуй, наша беседа подошла к концу."
    "[gg]" "Да, конечно."

    scene expression '#000' with Dissolve(.5)
    $ time.time_now   = "evening"
    $ location_now    = "City_Home"
    $ unlock_city_psi = False

    $ events.pop("christie_root_27", 0)

    $ events.pop("christie_root_27_repeat", 0)


    $ sister_position['morning']   = ['Hall',  'sister_hall']

    $ Event('christie_root_28', 'Christie', time = ["morning", "afternoon"])


    $ descript_Christie= _("Обсудить предложение Сьюзан с Кристи.")
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
