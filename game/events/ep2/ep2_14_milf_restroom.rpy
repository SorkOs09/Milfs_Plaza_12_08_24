label ep2_14_milf_restroom:
    $ events.pop('ep2_14_milf_restroom', 0)

    $ block_change_milf_position    = False


    scene expression '#000' with Dissolve(.5)
    scene expression 'cg/ep2/shower/bg_blur.png'


    show GG Normal
    show GG Pancu_4:
        xalign .25
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)

    "[gg]" "О да…"


    "[gg]" "Потрясающе!"


    "[gg]" "Какой завораживающий, манящий запах женского тела."









    show Milf Polu_1
    show Milf Polu_1:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    hide GG

    show GG Surprise
    show GG Surprise:
        xalign .25
    with vpunch

    $ renpy.music.stop(fadeout=.5)

    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)


    "Марина" "Ты что здесь делаешь, [gg]?!!"

    "[gg]" "{i}Когда она успел так быстро выйти?{/i}"

    "[gg]" "{i}Хорошо, что я успел спрятать её трусики в карман.{/i}"

    "[gg]" "Дверь была открыта…"

    "[gg]" "Я решил, что здесь никого не и…"

    "Марина" "Живо уходи отсюда! "

    "[gg]" "Да-да, конечно! "

    "[gg]" "Я не…"

    window hide
    hide GG
    show GG Surprise
    show GG Surprise:
        xalign .25
    show GG Surprise:
        linear 1 xalign 0.0

    show Milf Polu_1:
        linear 1 xalign .5

    $ renpy.pause(1, hard = True)



    show Milf Polu_1:
        xalign .5







    show GG Falldown:
        xzoom -1

        xpos -200

    with Dissolve(.2)
    "[gg]" "Скользкоооооо!!!..."

    show Milf Polu_2








    hide GG Falldown
    with vpunch

    show expression 'cg/ep2/shower/left_gg.png'
    with Dissolve(.5)

    $ renpy.music.stop(fadeout=.5)

    $ renpy.music.play('audio/your-call-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)




    "[gg]" "Аучч….."


    "Марина" "Ты как, сильно ушибся? "


    "[gg]" "Ещё не знаю…"

    show expression 'cg/ep2/shower/right_milf_1.png'
    with Dissolve(.5)


    "Марина" "Давай помогу подняться."


    "[gg]" "Подожди…"


    "[gg]" "Голова идёт кругом."


    "[gg]" "Пока не трогай меня."


    "Марина" "Хорошо…"


    "Марина" "{i}Кажется, этот негодник разглядывает мою писечку!{/i}"


    "Марина" "{i}Но…{/i}"

    show expression 'cg/ep2/shower/right_milf_2.png'
    with Dissolve(.5)
    "Марина" "{i}Вместо злости, я испытываю сексуальное волнение. {/i}"


    "Марина" "{i}Мне начинает нравится, как его влечёт ко мне.{/i}"


    "Марина" "{i}О нееет… От этих мыслей я перевозбудилась.{/i}"


    "Марина" "{i}И вся теку….{/i}"


    "Марина" "{i}Нет-нет, нельзя допустить, чтобы он видел это!{/i}"



    hide expression 'cg/ep2/shower/right_milf_1.png'
    hide expression 'cg/ep2/shower/right_milf_2.png'
    hide expression 'cg/ep2/shower/left_gg.png'
    show Milf Polu_1
    show GG Surprise

    show GG Surprise:
        xalign .1


    with vpunch



    "Марина" "Хватит, вставай и уходи! "



    "[gg]" "Звучит грубовато…"


    "Марина" "Я хочу спокойно принять душ."


    "[gg]" "Ладно-ладно, ухожу."

    scene expression '#000' with Dissolve(.5)

    $ location_now = 'Corridor'

    call show_all_images_label from _call_show_all_images_label_81
    with Dissolve(.5)

    show GG Surprise

    show GG Surprise:
        xalign .5

    with Dissolve(.5)





    "[gg]" "После такого представления, я уже не смогу просто так уснуть. "


    "[gg]" "Надо срочно посмотреть порно."


    "[gg]" "Это успокоит меня на время."
    $ add_to_gallery(3)
    if not from_gallery_check():
        $ unlock_masturbation_restroom = 0
        $ new_events                   = True
        $ descript = _('Надо срочно посмотреть порно. Это успокоит меня на время. Время: Ночь')

        $ watch_porn_ep2 = True



        $ time.time_forward()
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
