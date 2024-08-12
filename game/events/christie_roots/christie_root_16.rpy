label christie_root_16_repeat:

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
    if not from_gallery_check():
        $ events.pop('christie_root_16_repeat', 0)

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



    jump christie_root_16_menu_2

label christie_root_16:
    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    scene expression 'cg/christie_root/Psi_Build.png'
    with Dissolve(.25)

    $ renpy.pause(.25, hard = True)

    call screen rtrn_screen('cg/christie_root/Psi_Build_Door.png')

    scene expression '#000' with Dissolve(.25)
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    scene expression 'cg/christie_root/psi_corridor.png'
    with Dissolve(.25)
    $ renpy.pause(.5, hard = True)
    call screen rtrn_screen

    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    if not from_gallery_check():
        $ events.pop('christie_root_16', 0)

    scene expression '#000' with Dissolve(.5)

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














label christie_root_16_menu:

    menu:
        "Особый сеанс" if True:








            $ pass
        "Уйти" if True:


            call check_gallery_label from _call_check_gallery_label_12
            $ location_now = 'Corridor'
            $ unlock_city_psi   = True


            $ Event('christie_root_16', 'City_Psi', time = ['morning', 'afternoon'])

            scene expression '#000' with Dissolve(.5)
            jump main_interface_label


    show GG Normal
    "[gg]" "Здравствуйте, Сьюзан, я пришёл на следующий сеанс. "
    show Psi Normal
    "Сьюзан" "Замечательно. "
    show Psi Normal
    "Сьюзан" "Я, признаться, совсем не ожидала, что наш разговор продолжится. "
    show GG Normal
    "[gg]" "Почему?"
    show Psi Normal
    "Сьюзан" "Первая, обобщающая беседа, часто становится последней, поскольку люди получают так много пищи для размышления, что им банально лень заниматься поиском путей выхода."
    show GG Normal
    "[gg]" "Я другой."
    show Psi Smile
    "Сьюзан" "Абсолютно."
    show Psi Normal
    "Сьюзан" "Ты подготовил денюжку?"
label christie_root_16_menu_2:
    show GG Normal:
        xalign .15
    with my_dissolve

    if not hasattr(store, 'money') or from_gallery_check():
        $ money = 75
        
            
    menu:
        "!1. «Да, вот» (-75 долларов)" if money < 75:
            $ pass
        "1. «Да, вот» (-75 долларов)" if money >= 75:
            $ pass

        "2. «Нет, забыл»" if True:
            call check_gallery_label from _call_check_gallery_label_13
            $ location_now = 'Corridor'
            $ unlock_city_psi   = True


            $ Event('christie_root_16_repeat', 'City_Psi', time = ['morning', 'afternoon'])



            show Psi Chagrin
            "Сьюзан" "Очень жаль, [gg]. Надеюсь, в следующий раз у тебя будет нужная сумма. "
            show GG Smile
            "[gg]" "Обязательно!"
            scene black with Dissolve(.5)
            jump main_interface_label

    $ money -= 75
    $ show_text_animation('-'+str(75)+'$')















    show Psi Normal
    "Сьюзан" "[gg], теперь ты готов для нового сеанса?"


    "Сьюзан" "Прекрасно, проходи в кабинет."



    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "Сьюзен" "Располагайся."


    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Спасибо."
    "[gg]" "Я заметил, что ваш муж сегодня отсутствует. "


    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзен" "Едва ли это имеет отношение к нашему разговору. "
    "Сьюзен" "Он…"
    "Сьюзен" "Он очень занятой человек."
    "[gg]" "Вас это огорчает?"
    "Сьюзен" "Как и любую женщину, когда её муж проводит мало времени дома."
    "Сьюзен" "Давай лучше вернёмся к тебе."
    "[gg]" "Хорошо."
    "Сьюзен" "В первый день мы говорили о выборе жизненного пути."
    "Сьюзен" "И ты, как мне показалось, был полон энтузиазма, чтобы определиться с тем, кто ты, и куда собираешься идти. "
    "[gg]" "Так и есть."
    "Сьюзен" "Тогда расскажи мне об этом."


    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Сейчас у меня возникла потребность быть полезным."
    "[gg]" "К примеру, я помог Кристи."
    "[gg]" "Она не просила меня о помощи, и даже когда я сам проявил инициативу, нельзя сказать, что она надеялась, что я смогу её выручить."
    "[gg]" "Но я справился с задачей."
    "[gg]" "И хотя это было непросто, я помог ей, практически не нарушая закон. "


    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзен" "Практически?"


    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Да."
    "[gg]" "Я бы не хотел вдаваться в подробности происшествия, но, скажем так, я чуточку похулиганил. "
    "Сьюзен" "…."
    "[gg]" "Однако никто не пострадал! Ну, почти…"


    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзен" "Почти никто не пострадал?"


    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Когда вы так задаёте вопрос, я чувствую себя виноватым…"
    "[gg]" "Разве вы не должны быть на моей стороне?"


    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзен" "Я на твоей стороне, [gg]."
    "Сьюзен" "Просто ожидаю откровенности."


    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Я тоже. "


    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзен" "Что ты имеешь в виду?"


    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Когда я спросил вас про мужа, вы ушли от вопроса. "


    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзен" "Потому что это ты у меня на приёме, а не я у тебя."


    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Но как я могу быть честным с вами, если наши отношения чисто деловые, а не доверительные? "
    "[gg]" "А вдруг то, что я скажу, будет потом использоваться против меня?"
    "[gg]" "Поймите меня правильно, вы нравитесь мне, и я бы рад вам довериться, но вы – жена полицейского, а значит, в любой момент я могу оказаться под пятой закона."


    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзен" "…."
    "Сьюзен" "Полагаю, профессиональный этикет для тебя не авторитет."


    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve

    "[gg]" "Вы правильно понимаете. "
    "[gg]" "Я не хочу проверять вашу благонадёжность на прочность, рискуя собственной шкурой."


    show expression 'cg/christie_root/psi_scene_tits_2.png'
    "Сьюзен" "Справедливо."
    "Сьюзен" "Но ты позволишь мне заслужить твоё доверие? "
    "[gg]" "Попробуйте."
    "Сьюзен" "Поскольку ты боишься, что правда, озвученная здесь, может навредить тебе, я покажу тебе такое, что может навредить лично мне."
    "Сьюзен" "И тогда мы оба будем знать, что лучше нам держать язык за зубами."
    "[gg]" "И что же это?"
    "Сьюзен" "Что-то, на что ты не прекращаешь пялиться уже вторую нашу встречу. "


    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/past-sadness-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)

    scene expression 'cg/christie_root/psi_scene_tits_3.png'





    "[gg]" "Сьюзен?!"
    "Сьюзен" "Хи-хи-хи."
    "Сьюзен" "Меня забавляет твоя предсказуемая реакция. "
    "[gg]" "Вы… Ваша грудь. Вы великолепны. "
    "Сьюзен" "Оу, спасибо. Я люблю комплименты от молодых парней."
    "[gg]" "Могу я потрогать их?"
    "Сьюзен" "Полегче, жеребец. "


    scene expression 'cg/christie_root/psi_scene_tits_4.png'



    "Сьюзен" "Под одной из моих грудей располагается крошечное родимое пятно в виде сердечка. "
    "Сьюзен" "Об этом известно только моему мужу и никому более."
    "Сьюзен" "Теперь ты тоже знаешь."
    "[gg]" "Понял…"


    scene expression 'cg/christie_root/psi_scene_tits_3.png'


    "Сьюзен" "Если мой муж узнает, что ты в курсе об этой родинке, для него это будет означать, что у нас была интимная связь. "
    "[gg]" "Но…"
    "[gg]" "Но вы ведь могли сказать мне о ней. "
    "Сьюзен" "Верно. "


    scene expression 'cg/christie_root/psi_scene_4.png'
    show expression 'cg/christie_root/psi_scene_tits_2.png'
    with my_dissolve



    "Сьюзен" "Вот только тебе пришлось бы поверить мне на слово."
    "Сьюзен" "А тебе важно доверять мне, ведь так?"
    "[gg]" "Абсолютно. "


    scene expression 'cg/christie_root/psi_scene.png'

    with my_dissolve

    $ add_to_gallery(22)
    "Сьюзен" "Теперь я могу послушать, как именно ты помог Кристи?"


    scene expression 'cg/christie_root/psi_scene_2.png'

    with my_dissolve

    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "[gg]" "Да, я всё расскажу!"
    "[gg]" "Хотя, конечно, вряд ли моя история сравнится с демонстрацией ваших грудей, хе-хе."
    "Сьюзен" "…."
    "Сьюзен" "Прошу, говори."
    "[gg]" "Да-да, извините."
    "[gg]" "На днях у Кристи закончилось кофе, называется «Релакс». Редкий напиток в нашем городе."
    "[gg]" "И чтобы добыть его, мне пришлось помочь паре обкурышей. "
    "[gg]" "От меня требовалось отвлечь продавщицу в магазине, но она, унюхав мой одеколон, упала в обморок."
    "Сьюзен" "Бедная девушка!"
    "[gg]" "Не волнуйтесь. Она в полном порядке. "
    "[gg]" "Я быстро привёл её в чувства и покинул магазин."
    "Сьюзен" "А зачем ты её отвлекал? Те парни хотели что-то украсить?"
    "[gg]" "Нет. Они хотели отснять свои «нюдесы» в общественном месте для последующей продажи в интернете."


    scene expression 'cg/christie_root/psi_scene.png'

    with my_dissolve
    "Сьюзен" "Какие забавные ребята."
    "Сьюзен" "Но знаешь, в твоём поступке я не усмотрела ничего ужасного. Это лёгкое нарушение правопорядка и не более."


    scene expression 'cg/christie_root/psi_scene_2.png'

    with my_dissolve
    "[gg]" "Я так же подумал."
    "[gg]" "Но в другой жизни я не задумываясь вытянул бы деньги из кассы, или прихватил несколько продуктов с прилавка."


    scene expression 'cg/christie_root/psi_scene.png'

    with my_dissolve
    "Сьюзен" "Ты делаешь в своём успехи в переменах своей личности, [gg], ты молодец."
    "[gg]" "Спасибо."
    "Сьюзен" "И всё же ты согласился на авантюру, которая могла обернуться уголовным преступлением."
    "Сьюзен" "Вполне возможно, что кто-то из этих ребят, пока ты занимался продавщицей, прихватил несколько бутылочек пива, прежде чем покинуть магазин."
    "Сьюзен" "Ты предполагал такое?"


    scene expression 'cg/christie_root/psi_scene_2.png'

    with my_dissolve
    "[gg]" "Чёрт…."
    "[gg]" "А значит, если что-то такое случилось, я соучастник ограбления. "


    scene expression 'cg/christie_root/psi_scene.png'

    with my_dissolve
    "Сьюзен" "Поневоле."
    "[gg]" "Мне от этого не легче."
    "Сьюзен" "Ты боишься наказания или себя?"
    "[gg]" "Себя?"
    "Сьюзен" "Да, тебя гложет страх перед правосудием или тот факт, что ты снова можешь вернуться к прежней жизни?"
    "[gg]" "…."
    "[gg]" "Вы режете меня без ножа. "


    scene expression 'cg/christie_root/psi_scene_2.png'

    with my_dissolve
    "[gg]" "Я и так под «колпаком» вашего мужа, который в любой момент может посадить меня в тюрьму. "
    "[gg]" "И в тоже время я стараюсь отмыться от дерьма, в котором погряз по самую шею, пачкая своими проблемами родных и близких."
    "[gg]" "Это трудно, по-настоящему трудно, и это гложет меня."


    scene expression 'cg/christie_root/psi_scene.png'

    with my_dissolve
    "Сьюзен" "Ты словно чужой среди своих."


    scene expression 'cg/christie_root/psi_scene_2.png'

    with my_dissolve
    "[gg]" "Да!"
    "[gg]" "С годами ты привыкаешь к постоянному чувству азарта и необходимости его подпитывать. "
    "[gg]" "Адреналин начинает походить на кайф, дозу которого ты постоянно увеличиваешь."
    "[gg]" "Признаться, я люблю авантюры, но не хочу, чтобы это оборачивалось против меня такими последствиями как сейчас."


    scene expression 'cg/christie_root/psi_scene.png'

    with my_dissolve
    "Сьюзен" "Именно поэтому, вместо того, чтобы заказать кофе по интернету, ты решил помочь парням в магазине."
    "[gg]" "Да…"


    scene expression 'cg/christie_root/psi_scene_2.png'

    with my_dissolve
    "Сьюзен" "В этом нет ничего плохого, [gg]."
    "[gg]" "Разве?"
    "Сьюзен" "Ты всегда можешь найти подходящую работу, которая поддержит твою страсть к приключениям, но не будет нарушать закон в полной мере."
    "[gg]" "Звучит отлично. И что же это за работа такая?.."


    scene expression 'cg/christie_root/psi_scene.png'

    with my_dissolve
    "Сьюзен" "Если хочешь, мы поговорим об этом в следующий раз."
    "[gg]" "Эй, вы что, хотите оборвать нашу беседу на самом интересном, чтобы я снова явился?"
    "Сьюзен" "Ну, ты же любишь интригу?"
    "[gg]" "Вы коварная женщина. "
    "Сьюзен" "Я та, которая хочет помочь тебе чувствовать себя настоящим."
    "[gg]" "У вас отлично получается, я теперь не усну!"
    "Сьюзен" "Ха-ха-ха!"


    scene black with Dissolve(.75)
    $ renpy.pause(.5, hard = True)

    call check_gallery_label from _call_check_gallery_label_14

    scene expression 'cg/christie_root/psi_corridor.png'
    show Psi Normal
    show Psi Normal:
        xalign .5
        ypos 1085



    show GG Normal
    show GG Normal:
        xalign .15
        ypos 1085

    with Dissolve(.5)

    $ stnd_music_play()
  
    "Сьюзан" "Увидимся в другой день, [gg]."

    "[gg]" "Спасибо, что уделили мне время."

    "[gg]" "С нетерпением жду следующий встречи. "


    show Officer Normal
    show Officer Normal at go_from_right(xxzoom = -1, xxalign = .7)

    "Офицер" "Опять ты, парень?!"
    show GG Normal
    "[gg]" "Я уже ухожу."
    show Officer Normal:
        xalign .7
        xzoom -1.0 
    "Офицер" "Какого хрена ты снова припёрься? "

    "Офицер" "Разве я не говорил, что ты нежеланный гость?"
    show GG Angry
    "[gg]" "Я гостил не у вас, а у вашей жены."
    show Officer Angry
    "Офицер" "Вот именно!"
    show Psi Angry
    "Сьюзан" "Прекрати, милый!"
    show Psi Angry
    "Сьюзан" "Мы уже говорили – не вмешивайся в мою работу."
    show Psi Angry
    "Сьюзан" "Если ты ещё раз нахамишь моему клиенту, у нас возникнет ссора. "
    show Officer Hm
    "Офицер" "Ладно…."
    show Officer Normal
    "Офицер" "Только ради тебя, Сьюзен."
    show Psi Smile
    "Сьюзан" "Спасибо."
    show Psi Smile
    "Сьюзан" "Ещё раз до встречи, [gg]!"
    show GG Smile
    "[gg]" "Ага, скоро увидимся!"
    show Officer Angry
    "Офицер" "………………………………."

    scene black with Dissolve(.5)
    $ time.time_now   = "evening"
    $ location_now    = "City_Home"
    $ unlock_city_psi = False

    $ events.pop("christie_root_16", 0)

    $ events.pop("christie_root_16_repeat", 0)







    $ descript_Christie= _("Поговорить с Кристи Утром в Зале.")

    $ sister_position['morning']   = ['Hall',  'sister_hall']


    $ Event('christie_root_17', 'Christie', time = "morning")

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
