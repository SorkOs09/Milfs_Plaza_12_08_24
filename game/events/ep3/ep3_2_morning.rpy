


image ep3_divan_7a:
    'cg/ep3/DIVAN/7_1.png' with Dissolve(.25)
    1
    'cg/ep3/DIVAN/7_2.png' with Dissolve(.25)
    1
    repeat


image ep3_divan_7a2:
    'cg/ep3/DIVAN/7_1.png' with Dissolve(.25)
    .5
    'cg/ep3/DIVAN/7_2.png' with Dissolve(.25)
    .5
    repeat



image ep3_divan_7a3:
    'cg/ep3/DIVAN/7_1.png' with Dissolve(.25)
    .25
    'cg/ep3/DIVAN/7_2.png' with Dissolve(.25)
    .25
    repeat

label ep3_2_morning:
    scene expression '#000' with Dissolve(.5)
    $ location_now  = 'GG_Room'
    $ time.time_now = 'morning'
    call comic_frame_v2_predict_label(images=[
        "cg/ep3/DIVAN/background.png",
        "cg/ep3/DIVAN/1.png",
        "cg/ep3/DIVAN/2.png",
        "cg/ep3/DIVAN/3.png",
        "cg/ep3/DIVAN/4.png",
        "cg/ep3/DIVAN/4a.png",
        "cg/ep3/DIVAN/5.png",
        "cg/ep3/DIVAN/6.png",
        "cg/ep3/DIVAN/7_1.png",
        "cg/ep3/DIVAN/7_2.png",
        "cg/ep3/DIVAN/8.png",
        ]) from _call_comic_frame_v2_predict_label_7
    $ events.pop('ep3_2_morning', 0)

    $ renpy.play('audio/Door.mp3')

    call show_all_images_label from _call_show_all_images_label_25

    show Milf Normal
    show Milf Normal:
        xzoom -1
        xalign -0.7
        ypos 1085
        zoom 1.0-0.035


    show GG Normal
    show GG Normal:
        xzoom -1
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)

    $ renpy.pause(.05, hard = True)

    show Milf Normal:

        linear .5 xalign 0.3


    $ renpy.pause(.5, hard = True)

    show Milf Normal:

        xalign 0.3















    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)



    $ unlock_masturbation_restroom = 1
    show Milf Normal
    $ unlock_shower_together_2 = True
    $ new_events              = True
    "Марина" "Мы можем поговорить? "
    show GG Normal
    "[gg]" "Да, конечно. "
    show GG Smile
    "[gg]" "Хотя врываться без стука не вежливо."
    show Milf Angry
    "Марина" "Мять мои сиськи без спросу тоже, знаешь ли, поступок сомнительный! "
    show GG Surprise
    "[gg]" "Ты!..."

    "[gg]" "Так ты не спала?!.."
    show Milf Chagrin
    "Марина" "Нет. Но я пришла сюда не осуждать тебя. "

    "[gg]" "…."
    show Milf Chagrin
    "Марина" "Давай присядем и поговорим об этом"

    "[gg]" "Д-давай…"


    scene expression '#000'

    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    scene expression "cg/ep3/DIVAN/background.png"
    show expression "cg/ep3/DIVAN/1.png"

    with Dissolve(.5)






    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)



    "Марина" "Я тебя понимаю, [gg]."


    "Марина" "Ты сейчас переживаешь особенный период своей жизни и многие женщины могут казаться тебе чрезмерной… сексуальными."


    "[gg]" "Возможно."


    "Марина" "И тебе сложно сдерживать свою юношескую, пылающую энергию, которой нужен своевременный выход. "


    "[gg]" "Верно…"


    "Марина" "Я не хочу, чтобы ты испытывал стресс при виде меня, или трясся от перевозбуждения, когда я нахожусь рядом."


    scene expression "cg/ep3/DIVAN/background.png"
    show expression "cg/ep3/DIVAN/2.png"

    with Dissolve(.5)



    "[gg]" "Извини…"


    "Марина" "Нет-нет. Не извиняйся. Это нормально."

    scene expression "cg/ep3/DIVAN/background.png"
    show expression "cg/ep3/DIVAN/1.png"

    with Dissolve(.5)



    "Марина" "Я просто хочу помочь тебе. "


    "[gg]" "Помочь?.."


    "Марина" "Да."


    "Марина" "Я позволю тебе выплёскивать свою… бурлящую энергию, а ты, в свою очередь, будешь спокойно относится ко мне, как женщине, и не сходить с ума. "


    "Марина" "Но в пределах разумного, конечно! "


    "[gg]" "!!!..."


    "[gg]" "Ты имеешь в виду, что я…"


    "[gg]" "Нет, лучше ты скажи."

    scene expression "cg/ep3/DIVAN/background.png"
    show expression "cg/ep3/DIVAN/3.png"

    with Dissolve(.5)



    "Марина" "Я лучше покажу."

    scene expression "cg/ep3/DIVAN/background.png"
    show expression "cg/ep3/DIVAN/4.png"

    with Dissolve(.5)



    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "Марина" "Тебе нравится?"


    "[gg]" "Чёрт!!.."


    "[gg]" "Я…"


    "[gg]" "Я потрясён…"

    scene expression "cg/ep3/DIVAN/background.png"
    show expression "cg/ep3/DIVAN/4a.png"

    with Dissolve(.5)



    "Марина" "Вижу. "


    "Марина" "Наверное, тебе сейчас крайне неловко, верно?"


    "[gg]" "Ещё бы… "


    "[gg]" "Твои груди, твоё тело… Я на седьмом небе от счастья!"


    "Марина" "Хорошо, милый."

    scene expression "cg/ep3/DIVAN/background.png"
    show expression "cg/ep3/DIVAN/5.png"

    with Dissolve(.5)



    "Марина" "Тогда позволь мне сделать то, зачем именно я сюда пришла. "


    "[gg]" "Ты имеешь в виду «ту самую помощь»? "


    "Марина" "Именно. "


    "[gg]" "Делай всё, что считаешь нужным. "

    scene expression "cg/ep3/DIVAN/background.png"
    show expression "cg/ep3/DIVAN/6.png"

    with Dissolve(.5)



    "Марина" "Такой горячий…"


    "Марина" "И пульсирующий."


    "Марина" "Мне нравится."


    "[gg]" "Я сейчас уже ко…"


    scene expression "cg/ep3/DIVAN/background.png"
    show ep3_divan_7a

    with Dissolve(.5)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)






    "Марина" "Нет, нельзя."


    "Марина" "Я хочу, чтобы ты вобрал в этот миг всю свою накопившуюся страсть."


    "Марина" "Чтобы ты испытал неподдельное счастье, и был абсолютно свободен от похабных мыслей."


    "[gg]" "Через секунду я стану самым «свободным» человеком, чёрт меня дери!"


    scene expression "cg/ep3/DIVAN/background.png"
    show ep3_divan_7a2

    with Dissolve(.5)



    "Марина" "Твой член стал таким мокрым и липким. "


    "Марина" "Мне нравятся ощущать его у себя в руке."


    "Марина" "Особенно волнительно наблюдать за твоей покорностью моей воли. "


    "Марина" "Я словно овладела твоим разумом, а ты даже не в состоянии пошевелиться."


    "[gg]" "О даа…"


    "Марина" "И только твой член пытается сопротивляться, выскакивая из моих ладоней и прытко устремляясь вверх. "





    $ milf_8_morning_menu = 1
label milf_8_morning_menu_1:
    window hide
    $ renpy.pause(9999)
    menu:
        "Продолжать." if True:
            jump milf_8_morning_menu_1


        "Снизить скорость." if not milf_8_morning_menu:

            scene expression "cg/ep3/DIVAN/background.png"
            show ep3_divan_7a2

            with Dissolve(.5)
            $ milf_8_morning_menu = 1
            jump milf_8_morning_menu_1

        "Повысить скорость." if milf_8_morning_menu:
            scene expression "cg/ep3/DIVAN/background.png"
            show ep3_divan_7a3
            with Dissolve(.5)

            $ milf_8_morning_menu = 0
            jump milf_8_morning_menu_1
        "Кончить." if True:

            $ pass











    if hasattr(store, 'ep3_divan_7a3'):
        $ del ep3_divan_7a3
    if hasattr(store, 'milf_8_morning_menu'):
        $ del milf_8_morning_menu
    scene expression "cg/ep3/DIVAN/background.png"
    show ep3_divan_7a3

    with Dissolve(.5)


    "[gg]" "Я уже почти на грани…"


    "Марина" "Вижу, мой хороший, вижу."


    "[gg]" "Уххх…"


    $ renpy.pause(.2, hard = True)

    scene expression '#FFF' with Dissolve(.5)

    $ renpy.pause(.75, hard = True)

    scene expression "cg/ep3/DIVAN/background.png"
    show expression "cg/ep3/DIVAN/8.png"


    with Dissolve(.5)



    "[gg]" "Обалдееееть…."


    "Марина" "Приятно слышать."


    "[gg]" "Ты потрясающая."


    scene expression '#000' with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    call comic_frame_v2_predict_label(action=renpy.stop_predict,
        images=[
        "cg/ep3/DIVAN/background.png",
        "cg/ep3/DIVAN/1.png",
        "cg/ep3/DIVAN/2.png",
        "cg/ep3/DIVAN/3.png",
        "cg/ep3/DIVAN/4.png",
        "cg/ep3/DIVAN/4a.png",
        "cg/ep3/DIVAN/5.png",
        "cg/ep3/DIVAN/6.png",
        "cg/ep3/DIVAN/7_1.png",
        "cg/ep3/DIVAN/7_2.png",
        "cg/ep3/DIVAN/8.png",
        ]

        ) from _call_comic_frame_v2_predict_label_8
    $ add_to_gallery(7)
    call show_all_images_label from _call_show_all_images_label_26


    show Milf Normal
    show Milf Normal:
        xzoom -1
        xalign 0.3
        ypos 1085
        zoom 1.0-0.035


    show GG Normal
    show GG Normal:
        xzoom -1
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)

    "Марина" "Наши отношение несколько… скрепились, но я всё ещё твоя подруга, и ты должен об этом помнить."

    show GG Normal
    "[gg]" "Разумеется. "
    show Milf Passion
    "Марина" "Кое-что, конечно, я позволю тебе делать со мной, но если ты перейдёшь черту, эти отношения тут же прекратятся."
    show GG Embarrassment
    "[gg]" "Согласен. "
    show Milf Passion
    "Марина" "Чудесного тебе дня, [gg]. "
    show GG Embarrassment
    "[gg]" "И тебе, Маришка."

    show Milf Normal:
        xzoom 1
        linear 1 xalign -0.7
        ypos 1085
        zoom 1.0-0.035

    $ renpy.pause(1, hard = True)

    show GG Think
    hide Milf
    with my_dissolve
    "[gg]" "Она определённо играет со мной."
    show GG Think
    "[gg]" "Проверяет меня на моральную устойчивость."
    show GG Think
    "[gg]" "Хочет знать, как далеко я готов пойти, чтобы быть с ней."
    show GG Think
    "[gg]" "О, нет, Маришка, я тебя не разочарую."
    show GG Think
    "[gg]" "Я готов на всё!"

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
