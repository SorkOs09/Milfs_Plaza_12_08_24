screen ep4_milf_48_screen:

    add 'gradient_up'





    button ypos 20 xpos 130+130:
        add 'quest_button'
        action NullAction()
    if old_descript != descript:
        add 'warning_icon' xpos 340 ypos 100

    button ypos 20 xpos 130:
        add 'bag_button'
        action Show('bag_interface', transition = Dissolve(.5))


    button:
        add 'mobile_button'
        action NullAction()



    button:
        add time.time_now+'_button'
        xalign .5


        action NullAction()


    viewport:
        xmaximum 170
        ymaximum 195
        xalign .5
        imagebutton:
            idle '#0000'
            hover '#0000'
            action NullAction()

    add 'pause_icon' xalign .5










    add 'interface/Panel_Money.png' xalign 1.0
    text '$' + str(money) xalign .9 color '#000' ypos 40
    add 'interface/Panel_Day.png' xpos 587 ypos 30
    add 'interface/Panel_Day.png' xpos 1020 ypos 30 xzoom -1
    viewport:
        xmaximum 310
        ymaximum 90
        add '#0000'

        $ times = time.tdtd.title()
        text _(str(times)) color '#000' xalign .5 yalign .5 size 25
        xpos 587 ypos 30
    viewport:
        xmaximum 310
        ymaximum 90
        add '#0000'

        $ times = rus_time[time.time_now].title()
        text _(str(times)) xalign .5 yalign .5 color '#000' size 25
        xpos 1020 ypos 30

    add 'back_button'
    imagebutton:
        idle 'back_button_hover'
        hover 'back_button_hover'
        focus_mask True
        at ButtonEffect01
        action Return()


transform ep4_dance_transform():

    ypos 0 xpos -20

    linear 1 xpos 0 ypos 10
    linear 1 ypos 0 xpos 20



    linear 1 xpos 0 ypos 10
    linear 1 ypos 0 xpos -20



    repeat








































screen ep4_dance_screen:
    add str(ep4_tmp_dance_image) at ep4_dance_transform

image ep4_milf_48_Restaurant_2_5a_1:
    'cg/ep4/Restaurant_2/5a.png' with Dissolve(.75)
    1
    'cg/ep4/Restaurant_2/5b.png' with Dissolve(.75)
    1
    repeat


image ep4_milf_48_Restaurant_2_5a_2:
    'cg/ep4/Restaurant_2/5a.png' with Dissolve(.5)
    .5
    'cg/ep4/Restaurant_2/5b.png' with Dissolve(.5)
    .5
    repeat


image ep4_milf_48_Restaurant_2_5a_3:
    'cg/ep4/Restaurant_2/5a.png' with Dissolve(.25)
    .25
    'cg/ep4/Restaurant_2/5b.png' with Dissolve(.25)
    .25
    repeat


image ep4_milf_48_Restaurant_3_1a:

    'cg/ep4/Restaurant_3/a2.png' with Dissolve(.25)
    .5
    'cg/ep4/Restaurant_3/a3.png' with Dissolve(.25)
    .5
    repeat





image ep4_milf_48_Restaurant_3_2a:
    'cg/ep4/Restaurant_3/a2.png' with Dissolve(.15)
    .25
    'cg/ep4/Restaurant_3/a3.png' with Dissolve(.15)
    .25
    repeat




label ep4_milf_48:


    scene expression '#000' with Dissolve(.5)

    $ renpy.pause(.5, hard = True)

    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant/1t.png':
        ypos 0
    with Dissolve(.5)






    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "Марина" "Как думаешь, мы ещё сможем так провести время?"


    "[gg]" "Боишься, что брат выследит нас? "



    "Марина" "У него аллергия на ложь. Проще себя обмануть, чем его."


    "[gg]" "Тогда, возможно, нам стоит сразу ему признаться."


    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant/2t.png':
        ypos 0
    with Dissolve(.5)


    "Марина" "Ты с ума сошёл?! Ты хоть представляешь, как он отреагирует? "


    "[gg]" "Жить в постоянном страхе может быть невыносимо. Уж поверь, я знаю о чём говорю."


    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant/3t.png':
        ypos 0
    with Dissolve(.5)


    "Марина" "О каком страхе ты говоришь?"


    "[gg]" "Да так, не важно."


    "Марина" "Не о том ли страхе идёт речь, что я узнаю, как вы с Игорем вытащили все деньги из моего сейфа за картиной? "



    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant/4t.png':
        ypos 0
    with Dissolve(.5)



    "[gg]" "….!!!!!!!!!"


    "[gg]" "Кхе-кхе…. Кхе…."


    "[gg]" "Кажется…. Кхе-кхе… Кажется я подавился."


    "Марина" "Жуй-жуй, мой милый. Я подожду."




    "[gg]" "Кажется, я конкретно облажался…"


    "Марина" "Ещё как."


    "[gg]" "Значит, это последнее наше свидание, да?"


    "Марина" "Посмотрим."




    "[gg]" "Посмотрим?! У меня есть шанс оправдаться?! "


    "Марина" "Я узнала о краже в тот же вечер. Но, как видишь, мы не раз хорошо провели время."



    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant/5t.png':
        ypos 0
    with Dissolve(.5)


    "[gg]" "Я негодяй и подонок. "


    "[gg]" "Ты никогда меня не простишь…"


    "Марина" "Позволь мне самой это решать."


    "Марина" "Я хочу знать, зачем ты это сделал?"



    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant/6t.png':
        ypos 0
    with Dissolve(.5)

    "[gg]" "..."






    "[gg]" "Моё криминальное прошлое преследует меня. "


    "[gg]" "Я и Игорь задолжали одному бандиту крупную сумму. Очень крупную. Правда, как оказалось, не крупнее, чем та, что лежала у тебя в сейфе."


    "Марина" "Продолжай."


    "[gg]" "Именно поэтому мы и пытались совершить ту кражу в ювелирном магазине. Чтобы вернуть долг. Но, как видишь, я был пойман и поставлен на учёт."


    "[gg]" "А долг всё равно нужно отдавать…. Ну и вот."


    "Марина" "И тогда ты решил ограбить самого близкого человека."

    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant/7t.png':
        ypos 0
    with Dissolve(.5)





    "[gg]" "Да! Но не для того, чтобы поживиться. Честное слово, мы собирались вернуть эти деньги обратно. Заработать и вернуть. Копеечка к копеечке."


    "[gg]" "Я и сейчас не отказываюсь от своих слов. Просто…"


    "Марина" "Вы отдали долг?"


    "[gg]" "Нет."

    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant/2t.png':
        ypos 0
    with Dissolve(.5)

    "Марина" "Нет?!"


    "[gg]" "Игорь должен был отнести деньги Жлобу – так называют этого бандита. Но почему-то пропал."


    "Марина" "Ну да. Доверить пол миллиона долларов своему приятелю. Что могло пойти не так, верно?"

    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant/8t.png':
        ypos 0
    with Dissolve(.5)





    "[gg]" "Пол миллиона баксов?!"


    "Марина" "Тихо ты. Да, там была именно такая сумма. "


    "[gg]" "Но откуда у тебя такие деньги?"


    "Марина" "Деньги с работы Джеймса. Твой брат использует их в подставных сделках, чтобы ловить таких вот жуликов, как твой Жлоб."



    "Марина" "А деньги эти, между прочим, фальшивые и меченные. "


    "[gg]" "О Боже…."


    "Марина" "Ага. Очень скоро твоего приятеля найдут и посадят. "



    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant/9t.png':
        ypos 0
    with Dissolve(.5)


    "[gg]" "Нет, Марина, его убьют."



    "[gg]" "Он же отнёс эти деньги Жлобу! А тот не дурак! Он наверняка проверил эти деньги и выяснил, что это подстава. Понимаешь?"


    "Марина" "Ой… Значит, после того, как он убьёт твоего друга, то придёт за тобой?"


    "[gg]" "К гадалке не ходи. Мне крышка."


    "Марина" "Я предлагаю дождаться Джеймса и попросить его о помощи."


    "[gg]" "Ни в коем случае. Нет."


    "Марина" "Я не хочу, чтобы тебя убили."


    "[gg]" "У меня есть оружие."


    "Марина" "Пожалуйста. Позволь мне помочь. Это серьёзно."


    "[gg]" "Сперва мне нужно помочь своему другу. Не факт, что он мёртв. Вполне возможно, что его держат в заложниках."


    "Марина" "Но зачем?"


    "[gg]" "Ну, если деньги меченные, Жлоб может подумать, будто бы мы работаем с легавыми заодно. Убив Игоря, он лишь усугубит своё положение. "


    "[gg]" "Я предполагаю, он что он ждёт развития событий"


    "Марина" "И что ты собираешься делать?"


    "[gg]" "Если Игорь жив, попробую его вызволить. Если он ещё жив…"


    "[gg]" "Нет, я уверен, он жив! За мной бы давно уже пришли."


    "Марина" "Я так волнуюсь за тебя, [gg]. "


    "[gg]" " Всё будет хорошо."




    "Марина" "Пожалуйста, будь осторожен. Я прощаю тебя за кражу."


    "[gg]" "Спасибо. Ты настоящий ангел. "


    $ renpy.music.stop(fadeout=.5)

    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)

    if ep4_milf_47_tmp == 1:
        call ep4_milf_48_tmp_1 from _call_ep4_milf_48_tmp_1

    elif ep4_milf_47_tmp == 2:
        call ep4_milf_48_tmp_2 from _call_ep4_milf_48_tmp_2
    elif True:

        jump ep4_milf_48_tmp_3

    jump ep4_milf_48_tmp_end
label ep4_milf_48_tmp_1:




    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant/9t.png':
        ypos 0
    with Dissolve(.5)


    "Марина" "По твоему, Ангел делала бы с тобой..."

    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant_2/Chairs.png'
    show expression 'cg/ep4/Restaurant_2/1b.png'
    with Dissolve(.5)

    "Марина" "...Такое?"


    "[gg]" "Ты что, собираешься?.."

    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant_2/Chairs.png'
    show expression 'cg/ep4/Restaurant_2/2b.png'
    with Dissolve(.5)



    "Марина" "Ой, кажется я что-то уронила…"




    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant_2/Chairs.png'
    show expression 'cg/ep4/Restaurant_2/3b.png'

    "[gg]" "Ох…"


    "[gg]" "Не могу поверить, что ты решилась на такое…"


    "[gg]" "В людном месте. "


    "[gg]" "На нас могут смотреть… Точнее, на меня…."


    "[gg]" "Я чувствую себя крайне неловко. Это… Совсем не то, что я ожидал."


    "[gg]" "Но ты всё равно лучшая! Ах… Твой ротик восхитительный."
    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant_2/Chairs.png'
    show ep4_milf_48_Restaurant_2_5a_1

    show RestAdmin Normal
    show RestAdmin Normal:

        xpos -500
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)



    show RestAdmin Normal
    show RestAdmin Normal:
        xzoom -1
        linear 1 xpos 200
        ypos 1085
        zoom 1.0-0.035

    $ renpy.pause(1, hard = True)


    "Официант" "Молодой человек, вам плохо?"


    "[gg]" "…Что?!"

    "Официант" "Мне показалось, будто бы вам дурно, и я решила узнать, всё ли у вас в порядке."


    "[gg]" "Да-да… Да… Всё в порядке. Можете идти."

    "Официант" "Вы уверены? "


    "[gg]" "Мать твою, да свали ты уже!"

    "Официант" "Исчезаю. "


    show RestAdmin Normal:
        xzoom 1
        linear 1 xpos -400
        ypos 1085
        zoom 1.0-0.035

    $ renpy.pause(1, hard = True)

    hide RestAdmin




    $ ep4_milf_48_speed = 0
label ep4_milf_48_tmp_1_menu:
    window hide
    $ renpy.pause(9999)
    menu:
        "Пусть продолжает." if True:

            $ renpy.pause(9999)
            jump ep4_milf_48_tmp_1_menu
        "Ускориться" if not ep4_milf_48_speed:
            $ ep4_milf_48_speed = 1
            scene expression 'cg/ep4/Restaurant/Background.png'
            show expression 'cg/ep4/Restaurant_2/Chairs.png'
            show ep4_milf_48_Restaurant_2_5a_2
            jump ep4_milf_48_tmp_1_menu
        "Ускориться еще сильнее." if ep4_milf_48_speed == 1:
            $ ep4_milf_48_speed = 2
            scene expression 'cg/ep4/Restaurant/Background.png'
            show expression 'cg/ep4/Restaurant_2/Chairs.png'
            show ep4_milf_48_Restaurant_2_5a_3
            jump ep4_milf_48_tmp_1_menu
        "Кончить." if ep4_milf_48_speed == 2:
            $ pass












    scene expression '#FFF' with Dissolve(.5)

    "[gg]" "О даааа….."

    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant_2/Chairs.png'
    show expression 'cg/ep4/Restaurant_2/4b.png'
    with Dissolve(1)

    $ renpy.pause(9999)
    "[gg]" "Блаженство. "




    "Марина" "Люблю вкус твоей спермы, милый."







    return

label ep4_milf_48_tmp_2:





    "Марина" "Тогда, будь хорошим мальчиком, и не делай ничего дурного."
    scene expression 'cg/ep4/Restaurant_3/Background.png'
    show expression 'cg/ep4/Restaurant_3/Chairs.png':
        ypos 0
    show expression 'cg/ep4/Restaurant_3/Table.png':
        ypos 0
        alpha .5
    show expression 'cg/ep4/Restaurant_3/2k.png':
        ypos 0
    show expression 'cg/ep4/Restaurant_3/a5.png':
        ypos 0
    with Dissolve(.5)


    "[gg]" "Конечно, моя госпожа. "
    scene expression 'cg/ep4/Restaurant_3/Background.png'
    show expression 'cg/ep4/Restaurant_3/Chairs.png':
        ypos 0
    show expression 'cg/ep4/Restaurant_3/Table.png':
        ypos 0
        alpha .4
    show expression 'cg/ep4/Restaurant_3/2k.png':
        ypos 0
    show expression 'cg/ep4/Restaurant_3/a4.png':
        ypos 0
    with Dissolve(.5)





    "[gg]" "Кажется, я что-то уронил…"
    scene expression 'cg/ep4/Restaurant_3/Background.png'

    show expression 'cg/ep4/Restaurant_3/Chairs.png':
        ypos 0
    show expression 'cg/ep4/Restaurant_3/Table.png':
        ypos 0
        alpha .4
    show expression 'cg/ep4/Restaurant_3/3k.png':
        ypos 0

    show expression 'cg/ep4/Restaurant_3/a3.png':
        ypos 0

    with Dissolve(.5)




    "Марина" "Я не это имела в виду…"
    scene expression 'cg/ep4/Restaurant_3/Background.png'

    show expression 'cg/ep4/Restaurant_3/Chairs.png':
        ypos 0

    show expression 'cg/ep4/Restaurant_3/Table.png':
        ypos 0
        alpha .4

    show expression 'cg/ep4/Restaurant_3/3k.png':
        ypos 0

    show ep4_milf_48_Restaurant_3_1a:
        ypos 0

    with Dissolve(.5)



    "Марина" "Оххх…."


    scene expression 'cg/ep4/Restaurant_3/Background.png'

    show expression 'cg/ep4/Restaurant_3/Chairs.png':
        ypos 0
    show expression 'cg/ep4/Restaurant_3/Table.png':
        ypos 0
        alpha .4
    show expression 'cg/ep4/Restaurant_3/3k.png':
        ypos 0

    show ep4_milf_48_Restaurant_3_1a:
        ypos 0

    with Dissolve(.5)

    "Марина" "Но ты продолжай…"


    "Марина" "Проклятье, у тебя такой шаловливый язык. Я почти уже кончаю."




label ep4_milf_48_tmp_2_menu:
    window hide
    menu:
        "Продолжить." if True:

            $ renpy.pause(9999)
            jump ep4_milf_48_tmp_2_menu
        "Кончить." if True:
            $ pass







    scene expression 'cg/ep4/Restaurant_3/Background.png'

    show expression 'cg/ep4/Restaurant_3/Chairs.png':
        ypos 0

    show expression 'cg/ep4/Restaurant_3/Table.png':
        ypos 0
        alpha .4

    show expression 'cg/ep4/Restaurant_3/4k.png':
        ypos 0

    show ep4_milf_48_Restaurant_3_2a:
        ypos 0

    with Dissolve(.5)





    "Марина" "Даааааааа!!.."

    scene expression '#fff' with Dissolve(.5)

    $ renpy.pause(.3, hard = True)

    scene expression 'cg/ep4/Restaurant_3/Background.png'

    show expression 'cg/ep4/Restaurant_3/Chairs.png':
        ypos 0
    show expression 'cg/ep4/Restaurant_3/Table.png':
        ypos 0
        alpha .4
    show expression 'cg/ep4/Restaurant_3/4k.png':
        ypos 0

    show expression 'cg/ep4/Restaurant_3/a1.png':
        ypos 0

    with Dissolve(1)

    $ renpy.pause(.2, hard = True)


    $ renpy.pause(99999999)







    "Марина" "Спасибо, малыш. Порадовал свою леди. "






    return

label ep4_milf_48_tmp_3:






    show expression '#000a'
    with Dissolve(.5)
    menu:
        "1. Дождаться её инициативы. (Минет)" if True:
            $ ep4_milf_48_tmp_end = True
            hide expression '#000a'
            with Dissolve(.5)
            call ep4_milf_48_tmp_1 from _call_ep4_milf_48_tmp_1_1
        "2. Ублажить свою женщину. (Куни)" if True:
            $ ep4_milf_48_tmp_end = True
            call ep4_milf_48_tmp_2 from _call_ep4_milf_48_tmp_2_1
        "3. Хватит" if hasattr(store, 'ep4_milf_48_tmp_end'):
            jump ep4_milf_48_tmp_end

    jump ep4_milf_48_tmp_3




label ep4_milf_48_tmp_end:




    $ add_to_gallery(14)
    if from_gallery_check():
        call check_gallery_label from _call_check_gallery_label_3





    scene expression 'cg/ep4/Restaurant/Background.png'
    with Dissolve(.5)

    show expression 'cg/ep4/Restaurant/1t.png':
        ypos 0
    with Dissolve(.5)
    play sound 'audio/sms.ogg'

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "[gg]" "…."


    $ sms_now = SmsBlock('noname', 'noname', "15")
    $ sms_now.add_sms(_("TT: Если хочешь вернуть свои деньги, \nжду тебя в первой туалетной кабинке для мальчиков.\n\n"))
    $ sms_now.add_sms(_("GG: Ты кто?"))
    $ sms_now.add_sms(_("TT: У тебя 5 минут или ты ничего не получишь. "))
    $ sms_now.add_sms(_("GG: Окей."))


    $ phone_warning = True

    show expression '#000a' with Dissolve(.5)
    call screen phone_sms_screen(text_now=sms_now.list, who = 'noname', len_text_now = 1, rtrn = True)



label ep4_milf_48_phone:
    if not from_gallery_check():
        if renpy.get_screen('CardGameScreen'):
            $ Hide('CardGameScreen')()
        $ Hide('main_interface')()

        $ Hide('empty_interface')()



        $ Hide('phone_sms_screen')()
        $ Hide('phone_contacts_screen')()
        $ Hide('phone_interface')()

        $ renpy.pause(.5, hard = True)
    elif True:


        scene expression 'cg/ep4/Restaurant/Background.png'


        show expression 'cg/ep4/Restaurant/1t.png':
            ypos 0
        with Dissolve(.5)


    "[gg]" "Кто это может быть?"
    "[gg]" "…."
    hide expression '#000a' with Dissolve(.5)

    "[gg]" "Марина, позволь мне на мгновение оставить тебя. Мне нужно перезвонить."
    "Марина" "Конечно."




    scene expression '#000' with Dissolve(.5)

    $ renpy.pause(.5, hard = True)


    scene expression 'cg/ep4/Restaurant_Tualet/Background.png' with Dissolve(.5)




    "[gg]" "Зря я не прихватил свой пистолет. Он бы пригодился мне сейчас…"





    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/loopster-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    scene expression 'cg/ep4/Restaurant_Tualet/Background_blur.png'
    show expression 'cg/ep4/Restaurant_Tualet/t1.png'

    with vpunch




    "Ночная гостья" "Привет, дружок-пирожок."


    "[gg]" "Мать твою, ты что тут делаешь?!"


    "Ночная гостья" "Готовлюсь перерезать тебе горло. "





    "[gg]" "Не… не стоит."


    "Ночная гостья" "Жлоб дал мне задание порешать тебя как сучку. Ты и твой дружок кинули его на бабки."


    "[gg]" "Не понимаю о чём ты."


    "Ночная гостья" "Вы подсунули Жлобу фальшивые бабки, теперь он в ярости. Ты труп, парень."


    "[gg]" "А Игорь, что с ним?"


    "Ночная гостья" "Пока ещё жив. Его держат в заброшке. Но я бы на твоём месте переживала не за него."


    "Ночная гостья" "Я так понимаю, деньги, что ты мне давал, тоже подделка?"


    "[gg]" "Нет. Тебе я платил честно нажитыми."


    scene expression 'cg/ep4/Restaurant_Tualet/Background_blur.png'
    show expression 'cg/ep4/Restaurant_Tualet/t3.png'

    with Dissolve(.5)

    "Ночная гостья" "С чего бы это?"





    "[gg]" "Ты мне нравишься. К тому же, твой образ злодейки делает тебя по-особенному обаятельной."


    "Ночная гостья" "Хорошая попытка, парень."


    "[gg]" "…."


    "[gg]" "Ну, тогда мне остаётся принять свою участь. Убивай."


    "Ночная гостья" "Не могу."


    "[gg]" "Значит, мы так и будем здесь стоять?"


    "Ночная гостья" "Чёрт, парень, ты…"


    "Ночная гостья" "Ты прав."


    "Ночная гостья" "Я не убийца. "


    "Ночная гостья" "К тому же, если честно, я несколько привязалась к тебе. Ты не такой уж и придурок."


    "[gg]" "И ты отпустишь меня?"


    "Ночная гостья" "Отпущу. Но это тебя не спасёт. Жлоб пришлёт кого-то другого, кто точно не станет церемониться. "


    "[gg]" "Ты очень добра. Спасибо."


    "Ночная гостья" "И это всё?"


    "[gg]" "Извини… Тебе нужны деньги?.."



    scene expression 'cg/ep4/Restaurant_Tualet/Background_blur.png'
    show expression 'cg/ep4/Restaurant_Tualet/t4.png'

    with Dissolve(.5)




    "Ночная гостья" "Ха! Оставь свои бумажки при себе. Сейчас меня интересует кое-что более ценное. "


    "[gg]" "А?.."


    "Ночная гостья" "Скоро тебя убьют, а я так и не узнала, насколько ты хорош в деле."


    "[gg]" "Хе-хе… Всегда готов исправиться."


    "Ночная гостья" "Вижу-вижу."
    scene expression '#000' with Dissolve(1)

    $ renpy.pause(.5, hard = True)

    scene expression 'cg/ep4/Restaurant_Tualet/Background_2.png'
    show Bar_Tualet_5_anim slo:
        xpos -50
    show expression 'cg/ep4/Restaurant_Tualet/Frontground.png'

    with Dissolve(.5)





    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "Ночная гостья" "У тебя здорово получается, жеребец."


    "[gg]" "Просто хочу отблагодарить тебя как следует."


    "Ночная гостья" "Значит, твоя поддружка не против твои похождений на сторону. "



    "[gg]" "Не вплетай её сюда. "


    "Ночная гостья" "Ахх…. Я задела за живое, так?"


    "[gg]" "Заткнись, иначе я буду ебать тебя жёстко."



    "Ночная гостья" "Пока твоя подружка скучает одна в зале, ты трахаешь незнакомку в туалете!"


label ep4_milf_48_bar_tualet_menu_1:
    window hide
    menu:
        "1. Продолжить." if True:
            $ renpy.pause(9999)
            jump ep4_milf_48_bar_tualet_menu_1
        "2. Ускориться." if True:
            $ pass
    scene expression 'cg/ep4/Restaurant_Tualet/Background_2.png'
    show Bar_Tualet_5_anim med:
        xpos -50
    show expression 'cg/ep4/Restaurant_Tualet/Frontground.png'

    with Dissolve(.5)



    "[gg]" "Ах ты ж сучка!"


    "Ночная гостья" "Любишь сублимировать, глазея на свою подружку, после чего удовлетворяешь себя втихаря в туалете? Верно? "



    "[gg]" "Дрянь!!!"


    "Ночная гостья" "Повезло тебе, что я оказалась рядом. Так бы и стоял тут, дроча в общественно сортире!"


    "[gg]" "Сука!!!"


    "[gg]" "Я трахну тебя так, что ты не сможешь ходить."





label ep4_milf_48_bar_tualet_menu_2:
    window hide
    menu:
        "1. Продолжить." if True:
            $ renpy.pause(9999)
            jump ep4_milf_48_bar_tualet_menu_2
        "2. Кончить." if True:
            $ pass

    scene expression 'cg/ep4/Restaurant_Tualet/Background_2.png'
    show Bar_Tualet_5_anim fast:
        xpos -50
    show expression 'cg/ep4/Restaurant_Tualet/Frontground.png'

    with Dissolve(.5)



    $ renpy.pause(.5, hard = True)

    $ renpy.pause(9999)


    scene expression '#fff' with Dissolve(.5)





    $ renpy.pause(.5, hard = True)
    scene expression 'cg/ep4/Restaurant_Tualet/Background_2.png'
    show expression 'cg/ep4/Restaurant_Tualet/final.png'

    show expression 'cg/ep4/Restaurant_Tualet/Frontground.png'

    with Dissolve(.5)

    "Ночная гостья" "Каааайф."

    $ add_ach('ACH_3')

    scene expression 'cg/ep4/Restaurant_Tualet/Background_2.png'
    show expression 'cg/ep4/Restaurant_Tualet/final_2.png'

    show expression 'cg/ep4/Restaurant_Tualet/Frontground.png'

    with Dissolve(.5)

    "[gg]" "…."


    "Ночная гостья" "После такого, пожалуй, мне стоило бы представиться."


    "[gg]" "Согласен."


    "Ночная гостья" "Зови меня Кэт."


    "[gg]" "Постараюсь запомнить."


    "Кэт" "Оривидерчи, смертник. "
    $ add_to_gallery(15)
    if from_gallery_check():
        call check_gallery_label from _call_check_gallery_label_4
    scene expression '#000' with Dissolve(.5)

    $ renpy.pause(.5, hard = True)


    scene expression 'cg/ep4/Restaurant_Tualet/Background.png' with Dissolve(.5)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    call screen ep4_milf_48_screen
    scene expression '#000' with Dissolve(.5)
    scene expression 'cg/ep4/Restaurant/Background.png'
    show expression 'cg/ep4/Restaurant/1t.png':
        ypos 0
    with Dissolve(1)

    $ renpy.pause(.5, hard = True)





    "[gg]" "Извини, что так долго."


    "Марина" "Всё хорошо, милый. Я готова ждать, сколько нужно."


    "[gg]" "Ты прелестна. Могу я пригласить тебя на танец?"


    "Марина" "С удовольствием. "

    scene expression '#000' with Dissolve(.5)

    $ renpy.pause(.5)

    scene expression 'cg/ep4/ep4_restaurant_bg.png'
    $ ep4_tmp_dance_image = 'cg/ep4/Dance/1a.png'
    show screen ep4_dance_screen

    with Dissolve(.5)




    "Марина" "Мне так хорошо с тобой, [gg]."


    "[gg]" "И мне."


    "Марина" "Это волшебный вечер. Я просто таю в твоих руках."


    "[gg]" "Обожаю, когда ты говоришь нечто подобное."


    "Марина" "Тогда придвинься поближе, милый, я хочу прощебетать тебе на ушко."




    $ ep4_tmp_dance_image = 'cg/ep4/Dance/2a.png'
    "Марина" "Я хочу, чтобы ты трахнул меня."

    "[gg]" "Я хочу этого не меньше, любимая."



    "Марина" "Я жажду с тобой грязный, похабный секс."
    "Марина" "Со стекающей спермой их всех моих дырочек."
    "Марина" "Чтобы моё тело закипало от малейшего твоего прикосновения."


    "[gg]" "О Боги…"


    "Марина" "Хочу, чтобы ты запомнил эту ночь на всю жизнь."

    "Марина" "Чтобы ты выплеснул всё, что копилось в тебе все эти годы."
    "Марина" "Я впитаю каждую каплю твоего юношеского зелья."


    "[gg]" "Я так возбуждён, что если мы разойдёмся, все увидят, что у меня безумный стояк. "


    "Марина" "А ты не отходи, мой родной."
    "Марина" "Лучше крепче ухвати меня за попку."



    window hide
    $ ep4_tmp_dance_image = 'cg/ep4/Dance/3a.png'
    $ renpy.pause(999)
    "[gg]" "Охх… Блаженство."


    "Марина" "Наслаждайся, родной. Наслаждайся."

    window hide











label ep4_milf_48_milf_dance:
    window hide




    menu:
        "Продолжать танец." if True:
            $ renpy.pause(9999)
            jump ep4_milf_48_milf_dance
        "Закончить." if True:
            $ pass












    scene expression '#000'

    hide screen ep4_dance_screen

    with Dissolve(1)

    $ renpy.pause(.5, hard = True)


    $ renpy.pause(.5)



    if getattr(store, 'ep4_tmp_dance_image'):
        $ del ep4_tmp_dance_image


    scene expression 'cg/ep4/ep4_restaurant_bg.png'
    with Dissolve(.5)
    show GG Costume_Normal
    show GG Costume_Normal:
        xalign .1
        ypos 1085
        zoom 1.0-0.035



    show Milf Dress
    show Milf Dress_Smile:
        xalign .85
        ypos 1085
        zoom 1.0-0.035

    with Dissolve(1)


    "[gg]" "Предлагаю поскорее отправиться домой."

    "Марина" "Абсолютно согласна. "

    window hide

    $ renpy.pause(.1, hard = True)


    show GG Costume_Normal:
        xzoom -1

    $ renpy.pause(.1, hard = True)

    show GG Costume_Normal:
        xzoom -1
        linear 1.5 xalign -1.5
        ypos 1085
        zoom 1.0-0.035

    $ renpy.pause(1.3, hard = True)

    show Milf Dress_Smile:

        linear 1.3 xalign -1.5
        ypos 1085
        zoom 1.0-0.035

    $ renpy.pause(1.3, hard = True)
label ep4_milf_48_home:
    scene expression '#000' with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    $ location_now  = 'Corridor'
    $ time.time_now = 'night'

    call show_bg_image_label from _call_show_bg_image_label_36
    call show_additional_images_label from _call_show_additional_images_label_30













    show GG Costume_Normal
    show GG Costume_Normal:
        xalign .1
        ypos 1085
        zoom 1.0-0.035



    show Milf Dress_Normal
    show Milf Dress_Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035

    with Dissolve(.5)



    "Марина" "Пошли ко мне. Только тихо. Иначе Кристи услышит."

    "[gg]" "Ага…"
    show Milf Dress_Normal:
        xzoom -1

    $ renpy.pause(.2, hard = True)

    show Milf Dress_Normal:
        linear .85 xalign 1.5
        ypos 1085
        zoom 1.0-0.035

    $ renpy.pause(.85, hard = True)

    show GG Costume_Normal:
        linear .85 xalign 1.5
        ypos 1085
        zoom 1.0-0.035

    $ renpy.pause(.85, hard = True)







    scene expression '#000' with Dissolve(.5)

    $ renpy.pause(1, hard = True)
    scene expression 'cg/ep4/anim_frames/GG_Milf_First_Sex_1.png' with Dissolve(.5)

    $ renpy.music.stop(fadeout=.5)

    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)

    "Марина" "Наконец-то, мой милый, мой самый хороший, самый замечательный человечек в мире."
    "Марина" "Я так рада, что эта ночь принадлежит только нам. "
    "Марина" "Нам больше не нужно стыдливо уводить взгляд друг от друга."
    "Марина" "Притворяться, будто бы нас сдерживают какие-то нравственные преграда."
    "Марина" "Ругать себя за вульгарные мысли, искушение. "
    "Марина" "Теперь мы можем исполнить наши самые заветные фантазии. "
    "Марина" "Вкусить запретный плод и предаться страстной любви."

    scene expression 'cg/ep4/anim_frames/GG_Milf_First_Sex_start.png' with Dissolve(.5)

    "Марина" "Пожалуйста, войди в меня. Не заставляй меня дрожать от нетерпения."

    scene expression 'cg/ep4/anim_frames/GG_Milf_First_Sex_1_ass_bg.png'

    show GG_Milf_First_Sex_1_anim slo

    with Dissolve(.5)




    "Марина" "О даааа, мой хорошенький. Засунь свой член как можно глубже."


    "Марина" "Хочу чувствовать тебя всего."


    "Марина" "Охххх, потрясающее чувство."


    "Марина" "Я всегда о тебе фантазировала, милый, всегда мечтала, что когда-то ты окажешься внутри меня."


    "Марина" "Твой член такой пульсирующий, большой и жгучий. "


    "Марина" "Всё моё тело дрожит от наслаждения…."


    "Марина" "Я вся теку и сгораю от блаженства. Ты великолепен, [gg]."



    "Марина" "Продолжай. Продолжай трахать меня что есть мочи… Не позволяй мне даже думать о том, что когда это ощущение может прекратиться!"


    "Марина" "Ещё! Ещё! Ещё!!!"





label ep4_milf_48_sex_menu_end:
    window hide
    menu:
        "Сменить позу" if True:



            scene expression 'cg/ep4/anim_frames/GG_Milf_First_Sex_1_vagina_bg.png'

            show Milf_Sex_GG_3 slo
            with Dissolve(.5)
            "Марина" "Аххх… Да-да-да."

            "Марина" "Мне нравится, как ты пружинишь об мою попку."


            "Марина" "Мы так вспотели. Нам так хорошо вместе."

            "Марина" "Как же сильно мы любим друг друга. Я хочу, чтобы это продолжалось вечность!"

            "Марина" "О даа, дааа!"

            $ ep4_milf_48_sex_menu_end_cum = True
            jump ep4_milf_48_tmp_end_pose_2
        "Ускориться" if True:


            scene expression 'cg/ep4/anim_frames/GG_Milf_First_Sex_1_ass_bg.png'

            show GG_Milf_First_Sex_1_anim med

            with Dissolve(.5)

            $ ep4_milf_48_sex_menu_end_cum = True

        "Кончить." if hasattr(store, 'ep4_milf_48_sex_menu_end_cum'):
            scene expression 'cg/ep4/anim_frames/GG_Milf_First_Sex_1_ass_bg.png'
            show GG_Milf_First_Sex_1_anim fast

            with Dissolve(.5)

            "[gg]" "Я на пределе!!!"


            "[gg]" "Уже почти!"

            "Марина" "Давай, кончай! Кончай в меня!"
            "[gg]" "Кончааааююююююю!"
            scene expression '#FFF' with Dissolve(1.5)
            $ renpy.pause(1, hard = True)

            scene expression 'cg/ep4/anim_frames/GG_Milf_First_Sex_finish_vagina.png'
            with Dissolve(.5)
            "Марина" "Аххххх…. Как горячо…. И приятно."
            jump ep4_milf_48_end
    $ ep4_milf_48_sex_menu_end_cum = True
    jump ep4_milf_48_sex_menu_end
label ep4_milf_48_end:

    if hasattr(store, 'ep4_milf_48_sex_menu_end_cum'):
        $ del ep4_milf_48_sex_menu_end_cum

    scene expression 'cg/ep4/anim_frames/GG_Milf_First_Sex_finish.png' with Dissolve(.5)







    "Марина" "Ты такой хорошенький. Я люблю тебя, [gg]. Больше всех на свете."



    "[gg]" "И я тебя, Марина."



    "Марина" "Ты же останешься со мной спать, верно?"


    "[gg]" "Конечно."


    "Марина" "Ахх… Не верю, что мне так хорошо."


    "[gg]" "Сладких снов, любимая."


    "Марина" "Сладких снов, любимый."




    scene expression '#fff'
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    $ add_to_gallery(16)
    $ add_ach('ACH_8_test')
    
    if not from_gallery_check():
        call check_gallery_label from _call_check_gallery_label_5
    else:
        jump main_interface_label
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/morning.mp3', fadein = 1.5)

    $ location_now  = 'Milf_Room'
    $ time.time_now = 'morning'
    call show_bg_image_label from _call_show_bg_image_label_37
    call show_additional_images_label from _call_show_additional_images_label_31
    with Dissolve(1)

    $ renpy.pause(1, hard = True)








    show GG Normal
    show GG Normal:
        xzoom -1
        xalign .5
        ypos 1085
        zoom 1.0-0.035
    with my_dissolve
    "[gg]" "Марина уже проснулась?"

    #$ phone_sms_screen = {}
    $ sms_now.check = True
    $ descript = _('Конец эпизода.')


    "[gg]" "Видимо, я слишком долго спал. "

    call ep45_milf_49_05 from _call_ep45_milf_49_05
    $ Event('end_ep4_korridor', 'Hall')

    jump main_interface_label

label end_ep4_korridor:
    $ events.pop('end_ep4_korridor', 0)
    call show_bg_image_label from _call_show_bg_image_label_38
    call show_additional_images_label from _call_show_additional_images_label_32
    hide screen main_interface

    show GG Normal
    show GG Normal:
        xzoom -1
        xalign 1.85
        ypos 1085
        zoom 1.0-0.035
    show Christie Normal
    show Christie Normal:
        xzoom -1
        xalign -1.32
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)

    show GG Normal:
        linear .85 xalign .85
        ypos 1085
        zoom 1.0-0.035

    $ renpy.pause(.2, hard = True)

    show Christie Skepticism:
        linear .85 xalign .32
        ypos 1085
        zoom 1.0-0.035
    $ renpy.pause(1, hard = True)


    show Christie Skepticism:
        xzoom -1
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    show GG Normal:
        xzoom -1
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "Кристи" "Опять ты вываливаешься из комнаты Марины!"

    show GG Normal
    "[gg]" "Кристи, пожалуйста. Давай не сейчас."
    show Christie Skepticism
    "Кристи" "Чего?! А если я расскажу Марине, что видела тебя у неё?!"

    show GG Normal
    "[gg]" "Делай, что хочешь."
    show Christie Surprise
    "Кристи" "Что, чёрт возьми, происходит в этом доме?"
    show GG Normal
    "[gg]" "Поговорим позже, Кристи."
    show Christie Surprise
    "Кристи" "…."
    $ ep5_test = True

    $ events.pop('ep4_milf_45', 0)

    jump ep45_milf_49_0












label ep4_milf_48_tmp_end_pose_2:


    menu:
        "Сменить позу" if True:

            scene expression 'cg/ep4/anim_frames/GG_Milf_First_Sex_1_ass_bg.png'

            show GG_Milf_First_Sex_1_anim slo
            with Dissolve(.5)

            $ renpy.pause(.2, hard = True)

            $ renpy.pause(9999)
            $ ep4_milf_48_sex_menu_end_cum = True
            jump ep4_milf_48_sex_menu_end
        "Ускориться" if True:




            scene expression 'cg/ep4/anim_frames/GG_Milf_First_Sex_1_vagina_bg.png'

            show Milf_Sex_GG_3 med

            with Dissolve(.5)
            $ ep4_milf_48_sex_menu_end_cum = True
            jump ep4_milf_48_tmp_end_pose_2


        "Кончить." if hasattr(store, 'ep4_milf_48_sex_menu_end_cum'):

            scene expression 'cg/ep4/anim_frames/GG_Milf_First_Sex_1_vagina_bg.png'

            show Milf_Sex_GG_3 fast

            with Dissolve(.5)

            "[gg]" "Я на пределе!!!"


            "[gg]" "Уже почти!"

            "Марина" "Давай, кончай! Кончай в меня!"
            "[gg]" "Кончааааююююююю!"


            scene expression '#FFF' with Dissolve(1.5)
            $ renpy.pause(1, hard = True)

            scene expression 'cg/ep4/anim_frames/GG_Milf_First_Sex_finish_ass.png'
            with Dissolve(.5)


            "Марина" "Аххххх…. Как горячо…. И приятно."
            jump ep4_milf_48_end


    jump ep4_milf_48_tmp_end_pose_2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
