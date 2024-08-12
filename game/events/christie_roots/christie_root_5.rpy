screen christie_root_5_city_screen:

    use ep4_main_city_screen


    imagebutton:

        idle 'city_psi_button'
        hover 'city_psi_button'

        at ButtonEffect01

        focus_mask True

        action Return()
label christie_root_5_repeat:

    




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

    $ events.pop('christie_root_5_repeat', 0)

    scene black with Dissolve(.5)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    $ renpy.pause(.5, hard = True)

    scene expression 'cg/christie_root/psi_corridor.png'
    show Psi Normal
    show Psi Normal:
        xalign .8
        ypos 1085

    with Dissolve(.5)


    show GG Normal
    show GG Normal at go_from_left


    show Officer Agr
    show Officer Agr at go_from_right(xxzoom = -1, xxalign = .5)



    "Офицер" "Снова ты?!"
    show GG Normal:
        xalign .15
    show Officer:
        xalign .5
        xzoom -1
    with my_dissolve
    "[gg]" "Снова я."
    "Сьюзан" "[gg], теперь ты готов для первого сеанса?"



    jump christie_root_5_menu

label christie_root_5:

    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()





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
    $ events.pop('christie_root_5', 0)

    scene black with Dissolve(.5)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    $ renpy.pause(.5, hard = True)

    scene expression 'cg/christie_root/psi_corridor.png'
    show Psi Normal
    show Psi Normal:
        xalign .8
        ypos 1085

    with Dissolve(.5)


    show GG Normal
    show GG Normal at go_from_left


    "[gg]" "Здравствуйте, меня зовут [gg]. Могу я вас потревожить?"
    
    "Сьюзан" "Моё имя Сьюзан. Приятно познакомиться. Как я могу быть вам полезна?"
    show GG Think:
        xalign .15
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .5
    with my_dissolve
    "[gg]" "{i}Мне кажется, или это та самая женщина что в окне напротив моей комнаты?{/i}"
    show Psi Normal
    hide expression 'cg/ep45/shower_3/shadow.png'
    with my_dissolve
    "Сьюзан" "Ну же, говорите, я вас слушаю."
    show GG Normal
    "[gg]" "Кристи, моя подруга, посоветовала мне вас как отличного специалиста по психологии. "
    show GG Normal
    "[gg]" "Могу ли я записаться к вам на приём? "
    show Psi Normal
    "Сьюзан" "Вау, как мило."
    show Psi Normal
    "Сьюзан" "Признаюсь, мне очень приятно слышать столь лестный отзыв о моих скромных способностях. "
    show Psi Normal
    "Сьюзан" "Я, скажем так, не совсем профи и занимаюсь этим скорее для души, чем для заработка. "
    show Psi Normal
    "Сьюзан" "Но, чтобы моя польза воспринималась клиентом более внушительной, чем просто дружеский совет, я, всё же, предпочитаю брать символичную плату."
    show Psi Normal
    "Сьюзан" "Если вы готовы платить, я готова вам помочь."


    show Officer Normal
    show Officer Normal at go_from_right(xxzoom = -1, xxalign = .7)
    show Psi:
        easein 1 xalign .97
    "Офицер" "Дорогая, кто к нам при…"
    show Officer Agr:
        xzoom -1 xalign .7
    with my_dissolve
    "Офицер" "[gg]?!!"
    show Officer Agr
    "Офицер" "Что ты забыл у меня дома, приятель?"
    show Psi Surprise:
        xalign .97
    with my_dissolve
    "Сьюзан" "Вы знакомы?"
    show GG Laughs
    "[gg]" "В каком-то роде…"
    show Officer Agr
    "Офицер" "Это особо опасный преступник. Вор. А может, чего и похуже. "
    show Psi Passion
    "Сьюзан" "Даааа?"
    show GG Angry
    "[gg]" "Странно. Когда вы говорили с Мариной, вы характеризовали меня в более благоприятном свете. "
    show Officer Normal
    "Офицер" "Я просто не хотел огорчать твою подругу, вот и всё. "
    show GG Skepticism
    "[gg]" "Лицемер!"
    show Officer Agr
    "Офицер" "Ты у меня дома, парень."
    show Officer Agr
    "Офицер" "Подбирай слова, пока я не скатил тебя с лестницы. "
    show Psi Passion
    "Сьюзан" "Какой напор! Какой накал страстей! И всё ради чего? Ради демонстрации своего мужского эго и примитивного самоутверждения?"
    show Psi Normal
    "Сьюзан" "Позволю себе остановить вашу перепалку."
    show Psi Normal
    "Сьюзан" "[gg] нуждается в моей профессиональной помощи и я не смею ему отказать. "
    show Officer Normal
    "Офицер" "Он же в курсе, что твои услуги платные? Денег-то у него нет, именно поэтому он и промышляет воровством."
    show GG Chagrin
    "[gg]" "Это было единожды, и вы сами хотели мне дать шанс на исправление."
    show Officer Normal
    "Офицер" "От своих слов я не отказываюсь, парень, но видеть тебя дома не желаю."
    show Psi Normal
    "Сьюзан" "Это и мой дом тоже, знаешь ли."
    show Psi Normal
    "Сьюзан" "И я сама решу, кого мне у себя принимать, поскольку моё дело – это мой личные границы, которые ты, как мой муж, должен уважать. "
    show Officer Agr
    "Офицер" "…."
    show Psi Smile
    "Сьюзан" "[gg], скажи пожалуйста, у тебя есть 75 долларов? Ровно столько стоит один мой сеанс. "
    show Officer Agr:
        xzoom 1
    "Офицер" "Но в последний раз ты брала 150!"
    show Psi Angry
    "Сьюзан" "Это уже моё дело, какую плату мне брать с клиентов. "
    show Psi Smile
    "Сьюзан" "Так что, [gg]? Ты готов для первого сеанса? "
    if not hasattr(store, "money"):
        $ money = 100



label christie_root_5_menu:
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/happy-days-in-summer-by-musiclfiles-from-filmmusic-io.mp3', fadein = 1.5)

    menu:
        "!1. «Да, готов!» (-75 долларов)." if money < 75:
            $ pass
        "1. «Да, готов!» (-75 долларов)." if money >= 75:
            $ pass
        "2. «Пока нет, к сожалению»." if True:

            $ location_now = 'Corridor'
            $ unlock_city_psi   = True
            $ Event('christie_root_5_repeat', 'City_Psi', 'christie_root_5_repeat', time = ['morning', 'afternoon'])

            show Psi Chagrin
            "Сьюзан" "Очень жаль, [gg]. Надеюсь, в следующий раз у тебя будет нужная сумма. "
            show GG Smile
            "[gg]" "Обязательно!"
            scene black with Dissolve(.5)
            jump main_interface_label

















label christie_root_5_after_menu:

    $ money -= 75
    $ show_text_animation('-75 money')
    show Psi Smile
    "Сьюзан" "Вот и замечательно, я рада, что ты настроен серьёзно."
    show Officer Normal:
        xzoom -1
    "Офицер" "Ладно, можешь идти, парень, но я предупреждаю! Ни к чему не касайся, ничего не трогай и… никуда не смотри!"
    show GG Please
    "[gg]" "Понятно…"
    show Officer Normal:
        xzoom 1
    "Офицер" "Любимая."

    "Сьюзан" "Да, дорогой?"
    show Officer Normal
    "Офицер" "Я отправлюсь на работу, буду ближе к вечеру. "
    show Officer Normal
    "Офицер" "Пожалуйста, будь повнимательнее с этим типом, он не так наивен, как может показаться с виду."
    show Psi Normal
    "Сьюзан" "Я буду Сама Наблюдательность, не волнуйся, можешь идти. Удачного дня, дорогой. "

    show Officer Normal:
        xzoom -1
        linear 1.5 xalign -1.5

    $ renpy.pause(1.5, hard = True)

    hide Officer
    show Psi Normal:
        xzoom 1
    with my_dissolve
    "Сьюзан" "Прошу, [gg], проходи в мой кабинет."
    show GG Normal
    "[gg]" "Ага."
    show Psi Normal:
        xzoom -1 xpos 2400
        linear 1.5 xpos 3500
    show GG Normal:
        linear 1.5 xalign 1.5
    $ renpy.pause(1.6, hard = True)
    scene black with Dissolve(.5)
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/full-moon-lofi-vibes-by-edikey20-from-filmmusic-io.mp3', fadein = 1.5)

    $ renpy.pause(.5, hard = True)

    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзан" "Тут ходят слухи, что вы, не иначе как особо опасный преступник, хи-хи-хи."
    "[gg]" "Не такой уж и опасный, хех."
    "Сьюзан" "О, не скромничайте. Любите себя таким, какой вы есть."
    "[gg]" "Если бы всё так было легко, я бы не пришёл к вам, верно?"
    "Сьюзан" "Вы совершенно правы."
    "Сьюзан" "Надеюсь, вы комфортно себя чувствуете."
    "[gg]" "Да, спасибо."
    "Сьюзан" "Вы ответили это из вежливости или вам действительно удобно?"
    "[gg]" "Хех…"
    "[gg]" "Ну, если честно, кресло несколько странной формы, и мне пока трудно сказать наверняка."
    "Сьюзан" "Но вы всё равно ответили удовлетворительно, [gg]. "
    "Сьюзан" "Значит ли это, что и на все прочие вопросы вы будете отвечать так же? "
    "[gg]" "Я постараюсь быть искренним, честное слово."
    "Сьюзан" "Важно понимать…"
    "Сьюзан" "Хоть вы и пришли на сеанс, и это уже большой прогресс для любого, кто хочет решить свои проблемы, но моя задача не решать их, а помочь вам обозначить трудности, с которыми вам предстоит бороться. "

    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Понятно…"

    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзан" "В первую очередь, вам следует быть честным с самим собой, поскольку это не собеседование на работу, я не оцениваю вас, и моё мнение никак не должно влиять на вашу самооценку."

    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Хорошо…"
    "Сьюзан" "А во-вторых, вам стоит быть со мной откров… бла-бла-бла…."
    scene expression 'cg/christie_root/psi_scene_3.png'
    with my_dissolve
    "Сьюзан" "Бла-бла-бла…."
    "Сьюзан" "В то время как бла-бла-бла…. Ну и конечно же Бла-бла-бла…."

    show expression 'cg/christie_root/psi_scene_tits_1.png'
    "Сьюзан" "Сам понимаешь, ведь бла-бла-бла…. Бла-бла-бла…. Бла-бла-бла…."
    "Сьюзан" "И чем дольше ты продолжишь пялиться на мои объёмные, сочные груди, думая только о том, чтобы раздеть меня и заняться безудержным сексом, тем дольше эта ситуация будет становиться неловкой."

    scene expression 'cg/christie_root/psi_scene_4.png'
    show expression 'cg/christie_root/psi_scene_tits_2.png'
    with my_dissolve
    "[gg]" "Ой… Я не… Извините!!.."
    "Сьюзан" "Всё в порядке, [gg]."
    "Сьюзан" "Я в курсе, что у меня довольная большая и красивая грудь."
    "Сьюзан" "И раз уж я привлекла своё внимание телом, позволь мне продемонстрировать и ум, хорошо?"

    scene expression 'cg/christie_root/psi_scene_4.png'

    with my_dissolve


    "[gg]" "Да, безусловно."
    "[gg]" "Извините, что так вышло."

    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзан" "Давайте лучше поговорим о тебе."
    "[gg]" "Хорошо, давайте."
    "Сьюзан" "Почему вы пришли сюда? "

    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Хм…"
    "[gg]" "Моя подруга, это она меня побудила на этот шаг. Мне кажется, я теряю её. "
    "[gg]" "Как вы уже слышали, Сьюзан, я не в ладах с законом, и мой отрицательный образ жизни претит Кристи. "
    "[gg]" "Мне и самому сейчас стыдно…"
    "[gg]" "Длительное время я обманывал её, использовал в своих интересах и был настоящим эгоистом."
    "[gg]" "Понятное дело, что она сложила обо мне крайне отрицательное мнение, и я полностью потерял доверие."
    "[gg]" "Не так давно я осознал это… Как раз теперь, когда мне грозит тюрьма."
    "[gg]" "И пока не поздно, хочу измениться в лучшую сторону, а не принимать себя таким, какой я есть."
    "[gg]" "Хотя бы потому, что я не хочу терять близких мне людей."

    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзан" "Вы хотите поменяться под конкретного человека или, возможно, изменить своё отношение к жизни в целом? "

    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "И то, и то, наверное."

    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзан" "О нет, [gg], так не получится. "
    "Сьюзан" "Быть положительным, добропорядочным, или даже уважаемым гражданином в глазах общества не значит быть хорошим или любимым в глазах конкретного человека. "
    "[gg]" "Чёрт…. В ваших словах есть смысл."
    "Сьюзан" "Так что же вы выбираете?"
    "[gg]" "Не знаю, надо подумать."
    "Сьюзан" "Если позволите, пока вы будете размышлять, я постараюсь направить вашу мысль в нужное русло."
    "[gg]" "Я готов принять любую помощь."
    "Сьюзан" "Я хочу сказать, что конструировать свою личность под кого-либо, значит не иметь личности вообще. "
    "Сьюзан" "Но это не значит, что данное решение невозможно реализовать."
    "Сьюзан" "Многие существуют в таком состоянии всю жизнь, подстраиваясь под родителей, мужей, жён, под начальника на работе или стараясь угодить обществу."
    "Сьюзан" "Кто-то делает это искренне, кто-то использует данный способ для достижения конкретных целей. "
    "Сьюзан" "Но никто из них никогда не чувствует и не будет чувствовать себя тем, кем он есть на самом деле."
    "Сьюзан" "А это чревато постоянным стрессом, депрессией, которую такие люди стараются заглушить любыми доступными способами, от наркотиков до любовниц, лишь бы сдержать свою форму «хамелеона». "
    "Сьюзан" "И всё же, как бы вопиюще это не выглядело, многие из них достигают желаемого результата. "
    "Сьюзан" "Главное осознавать цену, которые ты платишь."

    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Кого-то мне это напоминает…"

    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзан" "Говоря же о другом выборе – о единении с самим собой, о принятии своей парадигмы мира и ощущении внутренней свободы, - явление тоже не без изъянов. "
    "Сьюзан" "Но в первую очередь это любовь к себе. Ты не просыпаешься в холодном поту, не стыдишься своих вкусов, уверен в своём выборе и не опираешься на чужую точку зрения. "
    "Сьюзан" "Ты, как я уже говорила ранее, честен с самим собой, а значит, эта жизнь принадлежит тебе, и все решения, как и последствия, зависит только от тебя."
    "Сьюзан" "Естественно, что далеко не все будут готовы принимать твою индивидуальность. Ведь твой выбор может полностью противоречить культуре общества. "
    "Сьюзан" "Включая и твоих близких, и дорогих тебе людей."
    "Сьюзан" "И чтобы наладить с ними отношение, выстроив взаимосвязь в нужном ключе, вам придётся искать компромиссы."
    "Сьюзан" "Не притворяться, не ломать себя под кого-либо, а именно искать точки соприкосновения. Обоим. В равнозначной пропорции. "
    "Сьюзан" "Теперь ты готов сказать своё слово, [gg]?"

    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "Знаете, Сьюзан, вы дали мне понять одну важную вещь. "
    "[gg]" "Последние годы я жил совсем не так, как мне того хотелось бы."
    "[gg]" "Я пытался соответствовать брату и загнал себя в тупик."
    "[gg]" "Теперь я хочу жить так, как велит мне сердце и я надеюсь, вы мне в этом поможете."

    scene expression 'cg/christie_root/psi_scene.png'
    with my_dissolve
    "Сьюзан" "Сделаю всё от меня зависящее. "
    "Сьюзан" "А на сегодня наш сеанс окончен. Увидимся в следующий раз."

    scene expression 'cg/christie_root/psi_scene_2.png'
    with my_dissolve
    "[gg]" "До скорой встречи!"
    $ time.time_now = 'evening'
    $ location_now  = 'Corridor'
    scene black with Dissolve(.5)

    # if getattr(store, 'block_igor_position', False):


    #     $ descript_Christie = _("Спросить Игоря как идут дела с замком Кристи.")

    #     $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")

    #     $ Event('christie_root_5_sms', 'GG_Room',  time = ['morning'], day_start = time.day_now + 1,)
        
    #     jump main_interface_label
        
# label christie_root_5_sms:

#     if getattr(store, 'block_igor_position', False):


#         $ descript_Christie = _("Спросить Игоря как идут дела с замком Кристи.")

#         $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")

#         $ events['christie_root_5_sms'].day_start = time.day_now + 1
#         jump main_interface_label

    
    if not hasattr(store, 'ACH_4_count'):
        $ ACH_4_count = 0
    $ ACH_4_count+=1
    if ACH_4_count>=3:
        $ add_ach('ACH_4')
    $ events.pop('christie_root_5_sms', 0)
    $ descript_Christie = _("Проверить телефон.")
    $ NPHOTO            = 'cg/christie_root/psi_photo_mini.png'
    #$ phone_sms_screen_2_tmp = copy.deepcopy(phone_sms_screen)
      
    $ sms_now = SmsBlock('Игорь', 'igor', "3", Jump('christie_root_5_2'))
    $ sms_now.add_sms(_("TT: Дверь исправлена, можешь не благодарить."))
    $ sms_now.add_sms(_("GG: Это почему же?"))
    $ sms_now.add_sms(_("TT: Это уже сделала Кристи! "))
    $ sms_now.add_sms(_("TT: ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ!!!"))
    $ sms_now.add_sms(_("GG: Чивооо?"))

    $ sms_now.add_sms(_("TT: [NPHOTO]"))

    $ sms_now.add_sms(_("GG: Мудак, я же просил без приколов!"))
    $ sms_now.add_sms(_("TT: Всё под контролем, бро, она даже не заметила."))
    $ sms_now.add_sms(_("GG: Ты чуть не подставил меня своим идиотизмом. "))
    $ sms_now.add_sms(_("TT: У каждого свои загоны, \nя же тебя за твои не осуждаю.\n\n "))
    $ sms_now.add_sms(_("GG: Больше я тебя о помощи просить не стану. "))
    $ sms_now.add_sms(_("TT: Это мы ещё посмотрим. "))


    $ phone_warning = True

    $ unlock_city_psi = False
    $ sister_position['morning']   = ['Hall',  'sister_hall']

    $ sister_position['afternoon'] = ['Hall',  'sister_hall']


    $ descript_Christie = _("Рассказать Кристи о походе к психологу.")

    $ Event('christie_root_6', 'Christie')
    jump main_interface_label



label christie_root_5_2:
    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    show expression 'cg/christie_root/psi_photo.png'
    with Dissolve(.5)

    $ renpy.pause(.5)
    "[gg]" "Чёрт её дери, а у неё реально классная задница."
    "[gg]" "Как раз в моём вкусе."



    call christie_root_try_to_del_descript_christie_block_igor from _call_christie_root_try_to_del_descript_christie_block_igor_6
    
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
