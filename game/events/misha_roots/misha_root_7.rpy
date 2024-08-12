label misha_root_7:
    $ events.pop("misha_root_7", 0)

    $ locations['City_Shop'].image_buttons_times['night'].pop('misha', 0)




    $ location_now = 'City_Shop'
    call show_bg_image_label from _call_show_bg_image_label_123

    show Misha Surprise
    show Misha Surprise:
        xalign .85
        ypos 1085
    with Dissolve(.5)


    show GG Normal
    show GG Normal at go_from_left


    $ renpy.pause(.85)
    show Misha Surprise:
        ease .5 xalign .95
    show Officer Normal
    show Officer Normal:
        xzoom -1
        xalign .65
        ypos 1085
    with my_vpunch
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)




    "Офицер" "[gg]?!"
    show Misha:
        xalign .95
    show GG Surprise:
        xalign .15
    with my_dissolve
    "[gg]" "Офицер?!"
    show Misha:
        xzoom -1
        ease 1.0 xalign 1.7
    show Officer Surprise:
        ease 1.0 xalign .8
    "Офицер" "Что ты забыл ночью у магазина?"
    show GG Skepticism
    "[gg]" "Разве я должен перед вами оправдываться? "
    show Officer Angry:
        xalign .8
    hide Misha
    with my_dissolve
    "Офицер" "Ясное дело!"
    show Officer Angry
    "Офицер" "В предписании суда ясно значится, что ты обязан отчитываться о ходе своего испытательного периода перед участковым полицейским, то есть, перед мной!"
    show Officer Angry
    "Офицер" "А ещё там сказано об ограничении перемещения в виде комендантского часа, не покидать жилище позднее девяти вечера."
    show GG Skepticism
    "[gg]" "Да вы издеваетесь? У меня встреча!"
    show Officer Normal
    "Офицер" "Да, со мной, и теперь я веду тебя по адресу проживания. "
    show Officer Normal
    "Офицер" "Вздумаешь сопротивляться или бежать – за последствия не ручаюсь. "
    show GG Angry
    "[gg]" "Будьте вы человеком! "
    show GG Angry
    "[gg]" "У меня свидание с девушкой."
    show Officer Normal
    "Офицер" "Какое чудовищное стечение обстоятельств."
    show Officer Normal
    "Офицер" "Но не смертельное."
    show Officer Normal
    "Офицер" "Отправь ей смс или позвони, и предложи перенести встречу на более ранее время."
    show GG Angry
    "[gg]" "Вы не понимаете…"
    show GG Chagrin
    "[gg]" "Уже те, что я стою здесь вами, для неё будет шоком."
    show Officer Normal
    "Офицер" "Ей не нравятся преступники?"
    show Officer Normal
    "Офицер" "Какое совпадение. Мне тоже."
    show Officer Normal
    "Офицер" "Пошли, парень. Пока я не разозлился окончательно."
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .5

    show GG Chagrin

    with my_dissolve
    "[gg]" "(шёпотом) Мудак…"

    $ renpy.pause(.3, hard = True)



    hide expression 'cg/ep45/shower_3/shadow.png'
    with my_dissolve
    show GG:
        xzoom -1
        ease 1.5 xalign -1.0
    show Officer:
        ease 1.5 xalign -1.0

    $ renpy.pause(1.75, hard = True)

    hide Officer
    hide GG
    show Misha Chagrin
    show Misha Chagrin:
        xalign 1.85

    with None

    show Misha Chagrin:
        ease 1.2 xalign .85


    $ renpy.pause(2.2, hard = True)





    scene black with Dissolve(.5)

    $ renpy.pause(.75, hard = True)



    $ renpy.music.stop(fadeout=.5)
    $ stnd_music_play()

    $ time.time_now = 'night'
    $ location_now  = 'Corridor'

    $ renpy.pause(.5)

    call show_all_images_label from _call_show_all_images_label_96

    with Dissolve(.5)

    show Officer Normal
    show Officer Normal at go_from_left(xxalign=.1)

    show GG Angry
    show GG Angry at go_from_left(xxalign=.5)
    "Офицер" "Доброй ночи, [gg]."
    show Officer:
        xalign .1

    "Офицер" "И придерживайся предписания, пожалуйста."
    show GG Chagrin:
        xzoom -1
        xalign .5
    with my_dissolve
    "[gg]" "…."


    show Officer Normal:
        xzoom -1
        ease 1 xalign -1.0

    $ renpy.pause(.5, hard = True)

    show GG Think:
        ease .5 xalign .5
    $ renpy.pause(.5, hard = True)
    hide Officer
    show GG:
        xalign .5
    with my_dissolve
    "[gg]" "Миша видела, как меня встретил легавый."

    "[gg]" "Теперь она точно уверена, что я в дерьме по самые уши."

    "[gg]" "Напишу ей смс, попробую хоть как-то пояснить ситуацию…"




    $ descript_Misha= _("Написать СМС Мишванде.")
    jump misha_root_7_5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
