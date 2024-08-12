label misha_root_3:

    $ events.pop("misha_root_3", 0)
    $ locations['City_Shop'].image_buttons_times['night'].pop('misha', 0)




    call show_bg_image_label from _call_show_bg_image_label_140

    show Misha Normal
    show Misha Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left

    "[gg]" "Заждалась? "
    show Misha Smile
    show GG:
        xalign .15
    "Мишванда" "Если надо, прожду и всю ночь. "
    show Misha Passion
    "Мишванда" "Главное, чтобы ожидание того стоили."
    show GG Embarrassment
    "[gg]" "…"
    show Misha Smile
    "Мишванда" "Пойдём, ковбой. "

    scene black with Dissolve(.5)
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    $ location_now  = 'City_Getto'

    $ renpy.pause(.5)

    show expression 'cg/misha_root/pereulok.png'

    with Dissolve(.5)

    show Misha Normal
    show Misha Normal at go_from_right(xxalign=.7)

    show GG Normal
    show GG Normal at go_from_right(xxalign=.99, xxzoom = -1)



    $ renpy.pause(.5, hard = True)

    show GG Normal
    "[gg]" "Как думаешь, в этот раз нас ожидают приключения?"
    show Misha:
        xalign .7
    show GG:
        xalign .99
        xzoom -1.0
    with my_dissolve
    "Мишванда" "Хотелось бы…"
    show GG Surprise
    "[gg]" "Чего?!"
    show Misha Passion
    "Мишванда" "Та ситуация раззадорила меня не на шутку."
    show Misha Passion
    "Мишванда" "Я так возбудилась, что чуть не отдалась тебе прям в переулке."
    show GG Surprise
    "[gg]" "Воу…"
    show GG Smile
    "[gg]" "И что тебя удержало?"
    show Misha Passion
    "Мишванда" "Здравый смысл."
    show Misha Passion
    "Мишванда" "Тогда бы ты решил, что я какая-то шалава, готовая трахаться с любым на первом свидании. "
    show GG Smile
    "[gg]" "Значит, это было свидание?"


    $ renpy.pause(.4, hard = True)
    show Misha Smile:
        xzoom 1
    with my_dissolve

    $ renpy.pause(.3, hard = True)
    show GG Smile:
        ease 1.3 xalign .85

    show Misha Smile:

        ease 1.3 xalign .55
    $ renpy.pause(1.5, hard = True)
    show GG Smile:
        xalign .85

    show Misha Smile:

        xalign .55
    with my_dissolve
    "Мишванда" "В определённой степени. "
    show Misha Passion:
        xzoom -1
    "Мишванда" "Когда ты был моим защитником, меня обуревала страсть и чувство благодарности, которая я жаждала выплеснуть на тебя."
    show GG Embarrassment
    "[gg]" "Эти чувства ещё в наличии?"
    show Misha Laugh
    "Мишванда" "Ха-ха-ха!"
    show Misha Passion
    "Мишванда" "Даю голову на отсечение, что у тебя в штанах уже пожар. "
    show GG Embarrassment
    "[gg]" "Ты сама завела этот разговор…"
    show Misha Passion
    "Мишванда" "Я люблю выводить людей из зоны комфорта."
    show GG Smile
    "[gg]" "У тебя отлично получается."
    show Misha Normal
    "Мишванда" "Так я проверяю человека на моральную устойчивость. "
    show Misha Normal
    "Мишванда" "Может я и не принцесса, но прежде чем впускать тебя в свою жизнь, я должна убедиться, что ты хороший человек"


    $ renpy.pause(.4, hard = True)
    show Misha Smile:
        xzoom 1
    with my_dissolve

    $ renpy.pause(.3, hard = True)
    show GG Smile:
        ease 1.3 xalign .7

    show Misha Smile:

        ease 1.3 xalign .35
    $ renpy.pause(1.5, hard = True)
    show GG Normal:
        xalign .7
    show Misha Laugh:
        xzoom -1
        xalign .35

    with my_dissolve

    "[gg]" "Разве защищая от бандитов, я не продемонстрировал насколько я хороший?"
    show Misha Normal
    "Мишванда" "Да. "
    show Misha Smile
    "Мишванда" "Ты смелый и отважный."
    show Misha Normal
    "Мишванда" "И всё же, позволь мне узнать тебя лучше."
    show GG Normal
    "[gg]" "Да, конечно."
    show GG Normal
    "[gg]" "Спрашивай что хочешь, я как открытая книга."
    show Misha Normal
    "Мишванда" "Не сегодня."
    show Misha Normal
    "Мишванда" "Мы уже пришли."
    show Misha Normal
    "Мишванда" "Как ты помнишь, я живу за углом."
    show Misha Embarrassment
    "Мишванда" "Увидимся в другой раз."
    show Misha Embarrassment
    "Мишванда" "Я надеюсь."
    show GG Embarrassment
    "[gg]" "Я тоже."



    show Misha:
        xzoom 1
        easeout_cubic 1.5 xalign -.6
    $ renpy.pause(2, hard = True)

    scene black
    with Dissolve(.5)





    $ location_now   = "City_Home"

    $ time.time_now  = "night"

    $ descript_Misha = _("Подкатывать к Мише дальше.")

    $ Event('misha_root_3_5', 'GG_Room', priority = 10, day_start = time.day_now + 1)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
