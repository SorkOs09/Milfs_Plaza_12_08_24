label christie_root_31b:
    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    scene expression 'cg/christie_root/Psi_Build.png'
    with Dissolve(.25)

    $ renpy.pause(.25, hard = True)

    call screen rtrn_screen('cg/christie_root/Psi_Build_Door.png')

    scene black with Dissolve(.25)






    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    if not from_gallery_check():
        $ events.pop('christie_root_31b', 0)

    scene black with Dissolve(.5)
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    $ renpy.pause(.5, hard = True)

    scene expression 'cg/christie_root/psi_corridor_open_door.png'

    show GG Normal
    show GG Normal at go_from_left
    $ renpy.pause(.75, hard = True)
    show GG Think:
        xalign .15
    with my_dissolve
    "[gg]" "Странно, Сьюзан всегда встречает меня в коридоре. "
    #show GG Normal
    "[gg]" "Если у неё сейчас приём, то почему дверь приоткрыта?"
    #show GG Normal
    "[gg]" "Забыла запереть?"
    #show GG Normal
    "[gg]" "Что ж, тогда я сам сделаю доброе дело и за…"

    show GG Surprise
    show Christie Invis
    show Christie Invis:
        xalign 1.0
    show Psi Invis
    show Psi Invis:
        xalign .8
    with my_vpunch
    "Кристи" "Я просила помочь тебя, а не втягивать нас в свои разборки с мужем!"
    "Сьюзан" "Это и есть помощь!"
    "Кристи" "Да ну?"
    show GG WTF
    "[gg]" "Это что, Кристи?"

    show GG:
        easein_cubic 1.5 xalign 1.0
    $ renpy.pause(1.6, hard = True)
    scene black with Dissolve(.25)

    $ renpy.pause(.3, hard = True)

    scene expression 'cg/christie_root/GG_See_PsiKri.png'
    show expression 'cg/christie_root/GG_See_PsiKri_0.png'
    with my_dissolve


    call screen christie_root_30_screen(2)
    scene expression 'cg/christie_root/GG_See_PsiKri.png'
    show expression 'cg/christie_root/GG_See_PsiKri_0.png':

        xpos 0
        easein_cubic 1.5 xpos -780
    $ renpy.pause(1.6, hard = True)

    show GG Invis
    show GG Invis:
        xalign 1.0
    show Christie Invis
    show Christie Invis:
        xalign .2
    show Psi Invis
    show Psi Invis:
        xalign .5
    with my_dissolve



    "Кристи" "Если твой муж поймает нас, то [gg] тут же окажется за решёткой!"
    "Сьюзан" "Это сблизит вас!"
    "Кристи" "Куда уж ближе?.."
    "Кристи" "[gg]… Он…"
    scene expression 'cg/christie_root/GG_See_PsiKri.png'

    show GG Invis
    show GG Invis:
        xalign 1.0
    show Christie Invis
    show Christie Invis:
        xalign .2
    show Psi Invis
    show Psi Invis:
        xalign .5
    with my_dissolve
    "Кристи" "Ты должна прекратить сеансы. "
    "Кристи" "Я ожидала, что наши отношения наладятся, но он, судя по всему, ожидает куда большего."
    "Сьюзан" "А я слышала, что ты и не против."
    "Кристи" "Я?.. К чему ты клонишь? "
    "Сьюзан" "К тому, Кристи, что ты просто ревнуешь меня."
    "Сьюзан" "И нет, не надо препираться! "
    "Сьюзан" "Ты проходила у меня терапию, и я прекрасно знаю все твои переживания на этот счёт."
    "Кристи" "Ах так?! И теперь ты хочешь использовать эти знания против?!"
    "Сьюзан" "Нет конечно!"
    "Сьюзан" "Я тебе друг, Кристи."
    "Сьюзан" "Я понимаю твои переживания."
    "Сьюзан" "Это нормально, что ты ревнуешь, ведь я тоже женщина. "
    "Сьюзан" "И, хочется думать, очень желанная. "
    "Кристи" "Ещё бы, с такими-то грудьми…"
    "Сьюзан" "Эй… Не завидуй, хи-хи."
    "Кристи" "Ну да…"
    "Сьюзан" "Поверь, Кристи, тебе не о чем волноваться. [gg] меня не интересует."
    "Сьюзан" "По крайней мере, в качестве мужа."
    "Кристи" "Боже, мне так стыдно…"
    "Кристи" "Я постоянно думаю о нём."
    "Кристи" "Стараясь гнать эти мысли, но постоянно ловлю его жадные взгляды на себе."
    "Кристи" "А недавно…"
    "Сьюзан" "Говори быстрее, [gg] должен явиться с минуты на минуту. "
    "Кристи" "А недавно я притворилась, будто застряла в стиральной машине."
    "Сьюзан" "Ахахахаха!!!"
    "Кристи" "…."
    "Сьюзан" "Извини, вырвалось."
    "Кристи" "Я не в обиде. "
    "Кристи" "Да, это было очень глупо. "
    "Кристи" "Зачем-то захотелось разыграть его, но… Не смогла остановиться. "
    "Кристи" "Он так ухватил за мои бёдра, что я…"

    "Кристи" "Тяжело было сопротивляться этому чувству… Оно увлекло меня за собой."

    "Сьюзан" "Оу… Вы что, воспроизвели сцену из порнофильма?"
    "Кристи" "Типа того… Но без… Ну ты поняла."
    "Сьюзан" "Понимаю. "
    "Кристи" "Теперь я даже не знаю, зачем сюда пришла… "
    "[gg]" "Кажется, Кристи собирается уходить, надо срочно отойти подальше, будто бы я только вошёл. "
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_39
    scene black
    with my_dissolve
    $ renpy.pause(.95, hard = True)
    scene expression 'cg/christie_root/psi_corridor.png'
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show GG Normal
    show GG Normal:
        xalign .1
    show Christie Surprise
    show Christie Surprise:
        xalign .65
    show Psi Normal
    show Psi Normal:
        xalign .9
    with my_dissolve
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/loopster-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)









    show Christie Street
    "Кристи" "Ах… [gg]? П-привет."
    show GG Smile
    "[gg]" "Привет! Не ожидал тебя здесь увидеть."
    #show Christie Embarrassment
    "Кристи" "Да это я так, зашла на чай Сьюзан."
    show Psi Normal
    "Сьюзан" "Но теперь Кристи уходит и мы можем начать наш сеанс."
    show Psi Normal
    "Сьюзан" "Ведь ты не против, Кристи?"
    #show Christie Embarrassment
    "Кристи" "Нет, вовсе нет. Хорошего вам… времяпровождения."

    show Christie:
        linear 1.0 xalign -1.0

    $ renpy.pause(1.2, hard = True)
    hide Christie
    show GG Silence
    with my_dissolve
    "Сьюзан" "Проходи. Сегодня не нужно платить. Я знаю твоё решение по моей просьбе."
    show GG Normal
    "[gg]" "Удобно."

    show Psi:
        xzoom -1 #xpos 3000
        easein_cubic 2 xalign 1.6

    show GG:

        easein_cubic 2 xalign 1.6

    $ renpy.pause(2.1, hard = True)

    scene black with Dissolve(.5)
    $ renpy.pause(1, hard = True)


    scene expression 'cg/christie_root/psi_scene.png'
    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15
    
    with my_dissolve

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/full-moon-lofi-vibes-by-edikey20-from-filmmusic-io.mp3', fadein = 1.5)
    "Сьюзан" "Ну и что думаешь?"
    "[gg]" "А?"
    "Сьюзан" "Не валяй дурака, ты же прекрасно слышал, о чём мы говорили с Кристи."
    "[gg]" "У вас что, локаторы вместо ушей?"
    "Сьюзан" "Ну так что?"

    scene expression 'cg/christie_root/psi_scene_2.png'

    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15
    
    with my_dissolve

    "[gg]" "А что вы хотите услышать?"
    "Сьюзан" "Правду, разумеется. "


    scene expression 'cg/christie_root/psi_scene.png'

    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15

    with my_dissolve

    "Сьюзан" "Например, как ты истолковываешь розыгрыш Кристи? "
    "[gg]" "Сложно сказать."

    scene expression 'cg/christie_root/psi_scene_2.png'

    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15

    with my_dissolve

    "[gg]" "Я озадачен и взволнован. "
    "Сьюзан" "Мгу."
    "[gg]" "Теперь я могу быть уверен, что моё влечение взаимно. "
    "Сьюзан" "Мгу."
    "[gg]" "Хотя и опасаюсь того, что своей навязчивостью могу отдалить её от себя."
    "Сьюзан" "Почему?"
    "[gg]" "Ну вы же слышали, Сьюзан, она боятся своих чувств. Боится того же, чего и я – давления извне. "
    "[gg]" "Но я готов пойти на этот риск."
    "[gg]" "В силу темперамента, наверное… "

    scene expression 'cg/christie_root/psi_scene.png'

    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15

    with my_dissolve

    "Сьюзан" "Рискнуть всем или погибнуть, да?"
    "[gg]" "Такой я человек."
    "Сьюзан" "И это ещё одна черта, что делает тебя уникальным. "
    "[gg]" "Вы мне льстите."
    "Сьюзан" "Я лишь хочу, чтобы ты использовал свои преимущества."

    scene expression 'cg/christie_root/psi_scene_2.png'

    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15

    with my_dissolve

    "[gg]" "Вы намекаете на вашу просьбу с мужем?"
    "Сьюзан" "Конечно."

    scene expression 'cg/christie_root/psi_scene.png'

    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15

    with my_dissolve

    "Сьюзан" "Кристи оценит твои позитивные качества, смекалку, проницательность, твои таланты авантюриста, который можно использовать во благо."
    "Сьюзан" "Она увидит в тебе то, что вижу я."
    "Сьюзан" "Не анархиста, объявляющий вызов всему человечеству, а хорошего парня, друга или даже… нечто большее."
    "[gg]" "..?"
    "Сьюзан" "Героя."

    scene expression 'cg/christie_root/psi_scene_2.png'

    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15

    with my_dissolve

    "[gg]" "Вы точно издеваетесь."
    "Сьюзан" "Ты или спасёшь мой брак, или освободишь от сковывающих уз."
    "Сьюзан" "Разве это не благородный поступок?"
    "[gg]" "Ну… Наверное. "
    "[gg]" "По крайней мере так это звучит с ваших уст. "

    scene expression 'cg/christie_root/psi_scene.png'

    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15

    with my_dissolve

    "Сьюзан" "И это же, замечу, поможет и тебе лучше рассмотреть Кристи."
    "Сьюзан" "Она не идеальна. "
    "Сьюзан" "Как и все люди, разумеется."
    "Сьюзан" "Она может испугаться, испортить работу или… довериться."

    scene expression 'cg/christie_root/psi_scene_2.png'

    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15

    with my_dissolve

    "[gg]" "Доверие, значит."

    scene expression 'cg/christie_root/psi_scene.png'

    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15

    with my_dissolve

    "Сьюзан" "Да. Не попытка услужить, а настоящие доверие в экстремальной ситуации. "
    "Сьюзан" "Женщине важно, чтобы человек был надёжный, прочный, добрый…"
    "Сьюзан" "Может показаться, что я говорю стереотипами. "
    "[gg]" "Именно так это и выглядит."
    "Сьюзан" "Но мы и есть сборник этих самых стереотипов. "
    "Сьюзан" "И я, в том числе, не лишена предрассудков, заблуждений и прочих ошибок, привитых мне обществом и воспитанием."
    "Сьюзан" "Это тоже очень важно учитывать. "

    scene expression 'cg/christie_root/psi_scene_2.png'

    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15

    with my_dissolve

    "[gg]" "Я надеюсь, вы всё это говорите не для того, чтобы промыть мне мозги, принудив следить за своим мужем."
    "[gg]" "Тем более что я, вроде как, уже дал согласие… И в этом просто нет необходимости. "

    scene expression 'cg/christie_root/psi_scene.png'

    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15

    with my_dissolve

    "Сьюзан" "Понимаю, [gg]."
    "Сьюзан" "Твоей натуре свойственно критическое мышление. "
    "Сьюзан" "Я это уважаю. "
    "[gg]" "Ну и хорошо. Я не хотел вас обидеть своими мнением на этот счёт."
    "Сьюзан" "Замечательно."
    "Сьюзан" "Наша беседе подошла к концу, [gg]."
    "[gg]" "Хорошо."
    "Сьюзан" "Буду ждать от тебя новостей. "

    scene expression 'cg/christie_root/psi_scene_2.png'

    show Psi Invis
    show Psi Invis:
        xalign .85

    show GG Invis
    show GG Invis:
        xalign .15

    with my_dissolve

    "[gg]" "Не беспокойтесь. "
    "[gg]" "Мне приходилось выслеживать людей. Своё дело я знаю. "
    "Сьюзан" "Приятно слышать."






    scene expression 'cg/christie_root/psi_corridor.png'
    show Officer Normal
    show Officer Normal:

        xalign .1

    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    
    show Psi Normal
    show Psi Normal at go_from_right(xxalign = 1.0)
    show GG Normal
    show GG Normal at go_from_right(xxzoom = -1, xxalign = .7)



    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/your-call-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Офицер" "Не дом, а проходной двор какой-то."
    show GG Normal:
        xalign .7
    show Psi Normal:
        xalign 1.0
    with my_dissolve
    "Сьюзан" "Мы уже говорили на этот счёт, милый."
    show Officer Angry:
        xzoom 1
    "Офицер" "Мы многое о чём говорим в последнее время, МИЛАЯ, но ты должна уважать и моё мнение тоже. "
    #show Psi Normal
    "Сьюзан" "Я и уважаю."
    #show Psi Normal
    "Сьюзан" "Я ведь не являюсь к тебе в участок и не учу тебя делать твою работу."
    show Officer Normal
    "Офицер" "Обсудим этом, когда твой…"
    show GG Please

    show Officer Normal:
        easein_cubic 1 xalign .25
    show expression "cg/ep45/shower_3/shadow.png":
        alpha .0
        easein_cubic 1 alpha .5
    "Офицер" "КЛИЕНТ исчезнет с моих глаз."
    show GG:
        xzoom 1
    hide expression "cg/ep45/shower_3/shadow.png"
    with my_dissolve
    "[gg]" "До свидание, Сьюзан."
    show Psi Normal
    show Officer:
        xalign .25
    with my_dissolve
    "Сьюзан" "До встречи, [gg]."

    $ time.time_now = 'evening'
    show GG:
        xzoom -1
    with None

    $ renpy.pause(.1, hard = True)

    show GG:
        easein_cubic 2.5 xalign -1.5

    $ renpy.pause(1.5, hard = True)


    scene black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)


    scene expression 'images/interface/city_interface/city_bg_'+time.time_now+'.png'

    with my_dissolve








    "[gg]" "Решено. Я принял заказ Сьюзан на слежку за её мужем. "
    "[gg]" "Для этого мне нужна подходящая маскировка. "
    "[gg]" "Какой-нибудь презентабельный образ, чтобы офицер не обратил на меня внимания. "
    "[gg]" "Нужно сходить в магазин одежды в поисках такого костюма."
    "[gg]" "Но сперва я обсужу свой план с Кристи. "
    $ debug_exit()

    scene black with Dissolve(.5)

    $ location_now = 'City_Home'

    $ unlock_city_psi = False

    $ descript_Christie= _("Обговорить с Кристи заказ Сьюзан.")

    $ sister_position['morning']   = ['Hall',  'sister_hall']

    $ Event('christie_root_32', 'Christie', time = ["morning", "afternoon"])

    $ events.pop('christie_root_31b', 0)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
