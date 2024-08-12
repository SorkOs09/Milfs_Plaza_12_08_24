image ep3_Milf_Hug_anim:


    'images/cg/ep3/Milf_Hug/3.png' with Dissolve(.5)
    1
    'images/cg/ep3/Milf_Hug/4.png' with Dissolve(.5)
    1

    repeat


label ep3_milf_30:

    






    $ remove_from_inventory("Билеты")

    if hasattr(store, 'milf_15_audio'):
        $ del milf_15_audio


    $ renpy.music.stop(fadeout=1)

    $ renpy.music.play('audio/funk-game-loop-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1)

    $ block_exit_home                = True
    $ events.pop('ep3_milf_30', 0)
    $ location_now = 'Corridor'
    hide screen main_interface
    call show_all_images_label from _call_show_all_images_label_72






    show GG Nude_Normal
    show GG Nude_Normal:
        xalign .15
        ypos 1085



    show Milf Street_Sad
    show Milf Street_Sad:
        ypos 1085

        xalign .65

    show Christie Street
    show Christie Street:
        xalign .5
        ypos 1085

        xalign 1.0
    with Dissolve(.5)







    "[gg]" "П-приветик."
    "Марина" "[gg], как тебе не стыдно? Ты же…"
    "Кристи" "Ага, он размахивает своим членом, Марина! "

    show Christie Street
    "Кристи" "Какого чёрта ты вытворяешь, [gg]?!"
    show GG Nude_Angry
    "[gg]" "Я был в душе и не успел одеться. Вы так трезвонили, будто бы что-то произошло! Я спешил и вот."
    show Christie Street
    "Кристи" "Да, произошло. Мы вернулись. Но это не повод размахивает своим детородным органом перед нашими лицами. "
    show Milf Street_Normal
    "Марина" "…."
    show GG Nude_Normal
    "[gg]" "Хе-хе… Будем считать, что я просто рад вас видеть. "

    "Кристи" "Ну ты и чудило, [gg] "


    "Кристи" "Ладно. Я иду в свою комнату. Увидимся завтра. "

    "[gg]" "До завтра. "
    hide Christie

    show Christie Street
    show Christie Street:
        ypos 1085

        xalign 1.0


    with Dissolve(.1)


    show Christie Street:

        linear .7 xalign -.1

    $ renpy.pause(.7, hard = True)

    hide Christie

    show Christie Street

    show Christie Street:
        ypos 1085

        xalign -.1


    with Dissolve(.1)



    hide Christie

    show Christie Street

    show Christie Street:
        ypos 1085

        xalign -.1
        xzoom -1


    with Dissolve(.1)








    "Кристи" "Ах да, спасибо за билеты на концерт."

    show GG:
        xzoom -1
    "[gg]" "Всегда пожалуйста. "

    hide Christie

    show Christie Street
    show Christie Street:
        ypos 1085

        xalign -.1


    with Dissolve(.1)


    show Christie Street:

        linear .2 xalign -.4

    $ renpy.pause(.2, hard = True)

    hide Christie

    show Christie Street

    show Christie Street:
        ypos 1085

        xalign -.4


    with Dissolve(.1)










    hide Christie

    show GG Nude_Normal:
        xzoom 1









    "[gg]" "Марина…"


    "Марина" "Да, милый? "
    show GG Nude_Normal
    "[gg]" "Тебе понравилось?"

    "Марина" "Ещё как. Он такой большой и… толстый."
    show GG Nude_OMG
    "[gg]" "Я про постановку в театре…"

    "Марина" "Оу… "
    show GG Nude_Chagrin
    "[gg]" "…."

    "Марина" "Кажется, мне тоже пора спать."


    show Milf Street_Normal:
        xzoom -1
    show GG Nude_Angry
    "[gg]" "(Нет, она найдёт Игоря!)"










    show GG Nude_OMG
    "[gg]" "Постой! "



    show Milf Street_Normal:

        xzoom 1






    "Марина" "Да?"

    show GG Nude_Normal

    "[gg]" "Я… Я скучал по тебе. "



    "Марина" "И я…"

    show GG Nude_OMG

    "[gg]" "Нет. Ты не понимаешь. Я очень сильно скучал."





    "Марина" "Послушай, в соседней комнате…"



    $ renpy.music.stop(fadeout=.5)

    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)

    call show_all_images_label from _call_show_all_images_label_73
    show expression 'images/cg/ep3/Milf_Hug/1.png'
    show GG Invis
    show GG Invis:
        xalign .35
    show Milf Invis
    show Milf Invis:
        xalign .55
    with Dissolve(.5)
    "[gg]" "Я так люблю тебя, Марина."

    "Марина" "Знаю."
    "[gg]" "И хочу тебя больше всех на свете."
    "Марина" "Знаю…"
    "[gg]" "Позволь мне…"
    "Марина" "Не сейчас, милый."

    call show_all_images_label from _call_show_all_images_label_74
    show expression 'images/cg/ep3/Milf_Hug/2.png'
    show GG Invis
    show GG Invis:
        xalign .35
    show Milf Invis
    show Milf Invis:
        xalign .55
    with Dissolve(.5)

    $ renpy.pause(9999)




    call show_all_images_label from _call_show_all_images_label_75
    show ep3_Milf_Hug_anim
    show GG Invis
    show GG Invis:
        xalign .35
    show Milf Invis
    show Milf Invis:
        xalign .55
    with Dissolve(.5)

    "Марина" "Ты переходишь границы."
    "[gg]" "Тогда скажи, когда?"
    "Марина" "Скоро…"
    "Марина" "Очень скоро…"
    "[gg]" "Врёшь."
    call show_all_images_label from _call_show_all_images_label_76
    show expression 'images/cg/ep3/Milf_Hug/2.png'
    show GG Invis
    show GG Invis:
        xalign .35
    show Milf Invis
    show Milf Invis:
        xalign .55
    with Dissolve(.5)

    $ renpy.pause(99999)
    scene expression '#000' with Dissolve(.5)
    call show_all_images_label from _call_show_all_images_label_77
    show Milf Street_Normal
    show Milf Street_Normal:
        ypos 1085
        xalign .95







    show GG Nude_Chagrin

    show GG Nude_Chagrin:


        ypos 1085
        xalign .15


    with Dissolve(.5)



    "Марина" "Ну всё. Хватит. "
    "[gg]" "Извини…"
    "Марина" "И одень штаны, пожалуйста."
    "[gg]" "Да, конечно."


    "Марина" "Ты ужинал?"
    "[gg]" "Нет."
    "Марина" "Покормить?"
    show GG Nude_Normal
    "[gg]" "Ага."

    "Марина" "Тогда мне нужно переодеться."
    show GG Nude_OMG
    "[gg]" "Эээ…"

    "Марина" "Домашние вещи в спальне. Я скоро вернусь."
    show GG Nude_OMG
    "[gg]" "Нет!"

    "Марина" "…?"

    "[gg]" "Я видел их в зале. Сам принесу! "

    "Марина" "Не помню, чтобы я оставляла их там."
    show GG Nude_Angry
    "[gg]" "Поверь мне, они там. Иди пока в душ, я скоро вернусь. "

    "Марина" "Спасибо…"


    $ descript = _("Сходить в спальню к Игорю и взять домашние вещи Марины.")




    $ Event('ep3_milf_31',       'Milf_Room')
    $ events.pop('ep3_milf_28', 0)
    $ Event('ep3_milf_30_stump', 'Restroom')

    $ add_to_gallery("11_1")
    jump main_interface_label

label ep3_milf_30_stump:
    $ location_now = 'Corridor'
    $ Event('ep3_milf_30_stump', 'Restroom')
    hide screen main_interface
    call show_all_images_label from _call_show_all_images_label_78
    with Dissolve(.5)

    "[gg]" "Мне пока незачем туда идти."

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
