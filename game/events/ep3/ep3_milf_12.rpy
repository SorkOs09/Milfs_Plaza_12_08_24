








image Cinema_Horror_anim_0:
    'images/cg/ep3/CinemaHorror/1.png' with Dissolve(.35)
    1
    'images/cg/ep3/CinemaHorror/2.png' with Dissolve(.35)

    1

    repeat

image Cinema_Horror_anim_1:
    'images/cg/ep3/CinemaHorror/5.png' with Dissolve(.35)

    1

    'images/cg/ep3/CinemaHorror/6.png' with Dissolve(.35)

    1





    repeat


image Cinema_Horror_anim_2:
    'images/cg/ep3/CinemaHorror/8.png' with Dissolve(.35)
    1
    'images/cg/ep3/CinemaHorror/9_1.png' with Dissolve(.35)
    1

    repeat


image Cinema_Horror_anim_2_anus:
    'images/cg/ep3/CinemaHorror/8_9.png' with Dissolve(.35)
    1
    'images/cg/ep3/CinemaHorror/8_8.png' with Dissolve(.35)
    1

    repeat








label ep3_milf_12:
    $ location_now  = 'Hall'
    $ time.time_now = 'evening'
    call show_bg_image_label from _call_show_bg_image_label_24
    call show_additional_images_label from _call_show_additional_images_label_19
    $ events.pop('ep3_milf_12', 0)

    show GG Normal
    show GG Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    show Milf Night_Normal
    show Milf Night_Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
        
    with Dissolve(.5)


    "Марина" "Рада тебя видеть, [gg]! Спасибо, что решил составить мне компанию. "

    show GG Normal
    "[gg]" "Мне только в радость. Давай смотреть?"
    show Milf Night_Smile
    "Марина" "Конечно."
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/aquarium-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    scene expression 'images/cg/ep3/CinemaHorror/CinemaHorror_1.png'
    with Dissolve(.5)
    "Граф Дракула" "У вашей жены прекрасная шея."
    scene expression 'images/cg/ep3/CinemaHorror/CinemaHorror_2.png'
    with Dissolve(.5)
    "Граф Дракула" "Я бы хотел узнать её лучше."
    "Марина" "Мне страшно, [gg]…"
    "Марина" "Можно я сяду ближе? "
    "[gg]" "Хе-хе-хе. Давай."


    scene expression 'images/cg/ep3/CinemaHorror/0.png'
    with Dissolve(.5)


    "Марина" "Я думала, что мы будем веселиться, но этот фильм меня реально пугает."
    "[gg]" "Ещё бы! "
    "[gg]" "Ходят слухи, что это не постановка, и в кино действительно снимался вампир."
    "Марина" "Не пугай меня! "
    "[gg]" "А все, кто принимал участие в съёмках фильма, вскоре после премьеры умерли или исчезли. "
    "[gg]" "Коронер, что проводил расследование, утверждает, будто бы режиссёр умер от потери крови, и что…"

    scene expression 'images/cg/ep3/CinemaHorror/1.png'
    with vpunch
    "Марина" "Всё, хватит! Я боюсь! Прекрати, пожалуйста. "
    "[gg]" "Хорошо-хорошо. Давай продолжать смотреть кино."
    "Марина" "Нет, мне страшно. Теперь я до конца фильма будут так сидеть."
    "[gg]" "Как знаешь."


    scene Cinema_Horror_anim_0 with Dissolve(.5)
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/past-sadness-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "[gg]" "…."

    "[gg]" "….?"


    "[gg]" "{i}Мне кажется, или Марина пытается тереться об меня?{/i}"

    "[gg]" "{i}Эти движения.{i}"
    "[gg]" "{i}Плавные, нежные движения её бёдер…{/i}"
    "[gg]" "{i}Ох… Дааа, продолжай.{/i}"
    "[gg]" "{i}Господи, как приятно.{/i}"
    "[gg]" "{i}Мой член упирается в Марину, трясь об её паховую область.{/i} "

    scene expression 'images/cg/ep3/CinemaHorror/3.png'
    with Dissolve(.5)

    "[gg]" "{i}Я пытаюсь немного сдвинуть её, чтобы вытащить свой член из штанов, но Марина схватила меня ещё крепче. {/i}"

    "[gg]" "{i}Хорошо, мы поняли друг друга. Попробую сделать первый шаг иначе.{/i}"


    scene expression 'images/cg/ep3/CinemaHorror/4.png'
    with Dissolve(.5)

    "[gg]" "{i}Ага, её устраивает такой вариант.{/i}"

    scene expression 'images/cg/ep3/CinemaHorror/7.png' with Dissolve(.5)
    "[gg]" "{i}У неё такая большая, сочная задница.{/i}"
    scene Cinema_Horror_anim_1 with Dissolve(.5)
    "[gg]" "{i}Её приятно массировать. Чувствовать теплоту кожи. Ощущать объём…{/i}"
    "[gg]" "{i}Но, разве на это она намекала, когда начала это «представление»? Нет, мне нужно пойти дальше.{/i}"

    scene expression 'images/cg/ep3/CinemaHorror/8.png'
    with Dissolve(.5)

    "Марина" "Ммм…."
    "[gg]" "{i}Она молчит, однако её стоны говорят сами за себя.{/i}"


    menu:
        "Анус" if True:
            $ ep3_milf_12_anus = True
            scene Cinema_Horror_anim_2_anus with Dissolve(.5)
        "Киска" if True:





            scene Cinema_Horror_anim_2 with Dissolve(.5)

    "[gg]" "{i}Внутри Марины уже всё течёт. {/i}"

    "[gg]" "{i}Мой палец практически проскальзывает внутрь.{/i}"
    "[gg]" "{i}Не трудно заметить, как она наслаждаешься моим прикосновением. {/i}"
    "[gg]" "{i}Её учащённое дыхание и всхлипы ласкают мне слух, и я возбуждаюсь ещё больше.{/i}"
    "[gg]" "{i}Быть может, она разрешит мне достать мне член? {/i}"
    "Марина" "Ахххх…."
    "Марина" "Ахх"
    "Марина" "Ах-ах-ах!..."
    "[gg]" "{i}Нет, не успею. Я сейчас кончу вместе с ней.{/i}"
    "[gg]" "{i}Да-да, почти… уже совсем рядом.{/i}"












    "Марина" "*Глубокий вздох*"
    "[gg]" "{i}О дааааа, Боже, дааа, я кончаю.{/i}"

    scene expression '#fff' with Dissolve(.2)
    $ renpy.pause(.1, hard = True)
    if hasattr(store, 'ep3_milf_12_anus'):
        scene expression 'images/cg/ep3/CinemaHorror/8_7.png'
    elif True:

        scene expression 'images/cg/ep3/CinemaHorror/9.png'
    with Dissolve(1)

    "Марина" "Хах….."
    "Марина" "Хааааах…."
    "[gg]" "Марина.."

    "Марина" "Ничего не говори, [gg]. "

    "Марина" "Не сейчас."
    "[gg]" "Хорошо."

    scene expression '#000' with Dissolve(1.5)
    $ renpy.pause(.5, hard = True)
    $ location_now  = 'Hall'
    $ time.time_now = 'night'
    if hasattr(store, 'ep3_milf_12_anus'):
        $ del ep3_milf_12_anus

    call show_bg_image_label from _call_show_bg_image_label_25
    call show_additional_images_label from _call_show_additional_images_label_20
    with Dissolve(.5)
    show GG Normal
    show GG Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035

    show Milf Night_Embarrassment
    show Milf Night_Embarrassment:
        xalign .85
        ypos 1085
        zoom 1.0-0.035

    with Dissolve(.5)





    "Марина" "Я иду спать. До завтра"
    "[gg]" "Пока…"

    call show_bg_image_label from _call_show_bg_image_label_26
    call show_additional_images_label from _call_show_additional_images_label_21

    show GG Think
    show GG Think:
        xalign .5

    with Dissolve(.5)
    $ renpy.pause(.1, hard = True)
    "[gg]" "Чёрт, это было мега-круто. Значит, Марина хочет меня не меньше, чем я её."

    "[gg]" "Нельзя упускать свой шанс. Я должен сделать всё возможное, чтобы закрепить наши отношения. "

    "[gg]" "Как бы теперь заснуть сегодня…"
    $ add_to_gallery(8)

    $ help_ep3_milf_14 = 1

    $ descript = _('На сегодня с меня хватит, пора спать. ')


    $ Event('ep3_milf_14', 'GG_Room', 'ep3_milf_14', day_start = time.day_now + 1,)



    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
