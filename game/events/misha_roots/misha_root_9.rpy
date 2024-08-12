image misha_root_9 1 = 'cg/misha_root/9_misha_sex/Misha_Sex_1.png'
image misha_root_9 2 = 'cg/misha_root/9_misha_sex/Misha_Sex_2.png'
image misha_root_9 3 = 'cg/misha_root/9_misha_sex/Misha_Sex_3.png'
image misha_root_9 4 = 'cg/misha_root/9_misha_sex/Misha_Sex_4.png'
image misha_root_9 5 = 'cg/misha_root/9_misha_sex/Misha_Sex_5.png'
image misha_root_9 end = 'cg/misha_root/9_misha_sex/Misha_Sex_End.png'

image misha_root_9 anim 1:

    "misha_root_9 1"
    .15
    "misha_root_9 2"
    .15

    "misha_root_9 3"
    .15

    "misha_root_9 4"
    .15

    "misha_root_9 5"
    .15

    "misha_root_9 4"
    .15

    "misha_root_9 3"
    .15

    "misha_root_9 2"
    .15

    repeat



image misha_root_9 anim 2:

    "misha_root_9 1"
    .1
    "misha_root_9 2"
    .1

    "misha_root_9 3"
    .1

    "misha_root_9 4"
    .1

    "misha_root_9 5"
    .1

    "misha_root_9 4"
    .1

    "misha_root_9 3"
    .1

    "misha_root_9 2"
    .1

    repeat



image misha_root_9 anim 3:

    "misha_root_9 1"
    .07
    "misha_root_9 2"
    .07

    "misha_root_9 3"
    .07

    "misha_root_9 4"
    .07

    "misha_root_9 5"
    .07

    "misha_root_9 4"
    .07

    "misha_root_9 3"
    .07

    "misha_root_9 2"
    .07

    repeat


image misha_root_9 anim 4:

    "misha_root_9 1"
    .05
    "misha_root_9 2"
    .05

    "misha_root_9 3"
    .05

    "misha_root_9 4"
    .05

    "misha_root_9 5"
    .05

    "misha_root_9 4"
    .05

    "misha_root_9 3"
    .05

    "misha_root_9 2"
    .05

    repeat




label misha_root_9:
    if not from_gallery_check():
        $ events.pop("misha_root_9", 0)




    $ location_now = 'StoreIn'
    scene expression 'locations/bg/StoreIn/afternoon_without_girl.png'

    show Misha Normal
    show Misha Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left

    "[gg]" "Привет, Миша."
    show GG Please:
        xalign .15
    with my_dissolve
    "[gg]" "Я понимаю, как всё вчера выглядело, но позволь мне…"
    show Misha Chagrin
    "Мишванда" "Прекрати!"
    show Misha Normal
    "Мишванда" "Я сейчас ухожу на перерыв, и хочу тебе кое-что подарить."
    show GG Surprise
    "[gg]" "Подарить?"
    show Misha Passion
    "Мишванда" "Ага. "
    show Misha:
        easein 1.5 xalign .0


    $ renpy.pause(1.6, hard = True)
    show Misha:
        xzoom -1

    show GG:
        xzoom -1
        ease 1 xalign .3
    with my_dissolve

    $ renpy.pause(1.2, hard = True)
    show Misha:
        ease 3 xalign -1.5
    show GG:
        ease 3 xalign -1.5
    show black:
        alpha .0
        ease 1.5 alpha 1.0

    $ renpy.pause(1.75, hard = True)



    scene misha_root_9 1
    with my_vpunch

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)

    "Мишванда" "Давай, ковбой, возьми меня!"
    "[gg]" "Ничего себе подарочек."
    "Мишванда" "У нас мало времени, [gg]."
    "Мишванда" "Трахни меня! Иначе я сама тебя трахну."
    "[gg]" "Никогда бы не подумала, что буду так радоваться угрозам."
    "[gg]" "Но вызов принимаю!"


    scene misha_root_9 2
    with my_vpunch
    "Мишванда" "Уффф, ты вошёл!"
    "[gg]" "Всё в порядке?"
    "Мишванда" "Да. Продолжай."
    scene misha_root_9 anim 1
    "[gg]" "Внутри тебя так влажно и тепло…"
    "Мишванда" "Ты любишь озвучивать свои вульгарные мысли, да?"
    "[gg]" "Хех... Я думал, что не произношу их вслух."
    "Мишванда" "Надеюсь, трахаешься ты так же, как и умеешь лгать."
    "[gg]" "Это повод мне ускориться."
    "Мишванда" "И усилить напористость. "

    "{i}Звук входа в магазин{/i}"

    "Мишванда" "А?..."
    "Мишванда" "Кажется кто-то стоит у кассы…"
    "[gg]" "Разве у тебя не перерыв?!"
    "Мишванда" "Да, но видимо я забыла закрыть дверь."
    "Мишванда" "Плевать! Пусть слушаю мои крики!"
    "[gg]" "Наши крики!"

    menu:
        "Ускориться" if True:
            $ pass
    scene misha_root_9 anim 2

    "Мишванда" "Аххххх!!!"
    "Мишванда" "Дааа, твой член знает, как завести мою киску."
    "Мишванда" "Охххх, ахххххх!!!"
    "Мишванда" "Будь грубее со мной, [gg]."
    "Мишванда" "Трахай меня что есть мочи, трахай меня сильнее! "
    "Мишванда" "Хочу, чтобы моя дырочка дрожала от проникновения твоего толстого жилистого члена!"
    "Мишванда" "Уффффф, я схожу с ума от восторга."
    "[gg]" "Ты внутри такая узкая и сочная."
    "[gg]" "Это возбуждает меня не на шутку…"
    "Мишванда" "Да?"
    "[gg]" "Ещё бы. Мне охота проникать в тебя как можно сильнее, желая дотянуться до самой матки."
    "Мишванда" "Меня прельщает твоя обезумевшая похотью, [gg]!"
    "Мишванда" "Внутри меня пульсируют сотни взрывов наслаждения!"

    "Мишванда" "Давай, сильнее, ещё сильнее. "

    "Мишванда" "Я хочу чувствовать твою неумолимую животную силу. "

    menu:
        "Ускориться" if True:
            $ pass
    scene misha_root_9 anim 3


    "[gg]" "Вот так, сучка."
    "[gg]" "Нравится погрубее, да?"
    "Мишванда" "Аххааа… Дааа…."
    "Мишванда" "Ещё-ещё-ещё!"
    "Мишванда" "Забудь про нежности и ласки, сделай больно и жёстко. "
    "[gg]" "Тогда моли о пощаде, детка!"
    "[gg]" "Ты сама напросилась"
    "Мишванда" "Разве я похожа на ту, что так легко сломить?!"
    "[gg]" "Мой член чуть ли не разрывает твою киску, Миша, ещё немного, и ты расплачешься. "
    "Мишванда" "Аххххх, даааа! Дааааа! Разорви меня! Кончи в меня как следует. "
    "Мишванда" "Если я и заплачу, то только от радости, [gg]."
    "Мишванда" "Не вздумай снижать скорость!"
    "Мишванда" "Я хочу, чтобы ты выплеснул в меня как можно больше своей горячей спермы!"
    "[gg]" "Всё к этому идёт, Мишенька!"
    "[gg]" "Я уже на грани!"

    menu:
        "Кончить" if True:
            $ pass
    scene misha_root_9 anim 4





    "Мишванда" "Оооооо даааа!!!"
    "Мишванда" "В твоих буйствующих завершающих движения столько бешенной страсти. "
    "Мишванда" "Моя киска вопит от радости вместе со мной, даааааа!!!"
    scene expression '#fff' with my_dissolve

    "[gg]" "Я кончааааюююю!!!!"

    scene misha_root_9 end with Dissolve(1.3)
    $ renpy.pause(1.5, hard = True)
    "[gg]" "Получииии, сучкаааааааа!"
    "Мишванда" "Аааааххххххх…."
    "Мишванда" "Обожаааааюююю!!!!"
    "[gg]" "Я выжат как лимон…."
    $ stnd_music_play()
    "Мишванда" "А я изрядно насытилась, хех…"
    "Мишванда" "Спасибо, [gg], ты был просто супер."
    "[gg]" "Мне тоже понравился секс с тобой."
    "Мишванда" "Ну всё, вали. Мне ещё надо прибраться "








    call check_gallery_label from _call_check_gallery_label_11
    scene expression '#000' with Dissolve(.5)
    $ add_to_gallery(27)
    $ renpy.pause(.5, hard = True)




    $ time.time_now = "evening"

    $ location_now = 'StoreIn'


    scene expression 'locations/bg/StoreIn/afternoon_without_girl.png'

    show Misha Passion
    show Misha Passion:
        xalign 1.5
        ypos 1085

    show GG Passion
    show GG Passion:
        xalign 1.5
        ypos 1085

    with Dissolve(.5)
    show Misha:
        ease 1 xalign .85
    show GG:
        xzoom -1
        ease 1 xalign .2
    $ renpy.pause(1.3, hard = True)

    show GG:
        xzoom 1
    with my_dissolve

    "[gg]" "Значит, ты не в обиде за меня после того вечера?"
    show Misha Passion
    "Мишванда" "Нет, конечно."
    show GG Normal
    "[gg]" "Теперь мы пара?"
    show Misha Passion
    "Мишванда" "Не-а."
    show GG Surprise
    "[gg]" "Не понимаю тебя."
    show Misha Passion
    "Мишванда" "Расслабься, [gg]."


    show Misha Passion
    "Мишванда" "Я работаю с самого утра до позднего вечера. "

    show GG Normal

    show Misha Passion
    "Мишванда" "У меня нет времени на отношения, а тем более с парнем, у которого трудности с законом, но ты мне очень нравишься и я думаю, что мы всегда можем не плохо провести время."
    show Misha Passion
    "Мишванда" "Что скажешь?"
    show GG Passion
    "[gg]" "Звучит как дружба, в которой преобладает секс."
    show Misha Passion
    "Мишванда" "Тогда приходи ко мне, если, вдруг, ты сильно заскучаешь. "
    show GG Passion
    "[gg]" "Разве можно отказаться от такого предложения?"
    show Misha Laugh
    "Мишванда" "Хи-хи-хи."


    scene expression '#000' with Dissolve(.5)

    $ misha_shalost = True






    $ add_ach('ACH_10')
    $ descript_Misha= _("Конец рута Мишванды")
    $ location_now  = "City_Shop"
    $ time.time_forward()

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
