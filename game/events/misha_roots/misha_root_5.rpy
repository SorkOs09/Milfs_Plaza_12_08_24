label misha_root_5:

    $ events.pop("misha_root_5", 0)

    $ locations['City_Shop'].image_buttons_times['night'].pop('misha', 0)



    scene black with Dissolve(.5)
    call show_bg_image_label from _call_show_bg_image_label_139

    show Misha Normal
    show Misha Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Smile
    show GG Smile at go_from_left



    "[gg]" "Привет, Миша. "
    show Misha Smile
    show GG:
        xalign .15
    with my_dissolve
    "Мишванда" "Привет."
    show GG Smile
    "[gg]" "Я вот не пойму, мы уже пара или нет?"
    show Misha Passion
    "Мишванда" "А сам как думаешь?"
    show GG Embarrassment
    "[gg]" "Не знаю."
    show Misha Smile
    "Мишванда" "Предлагаю это выяснить. Идём."
    show GG Embarrassment
    "[gg]" "Идём."


    scene black with Dissolve(.5)

    $ location_now  = 'City_Getto'

    $ renpy.pause(.5)


    show expression 'cg/misha_root/pereulok.png'

    with Dissolve(.5)

    show Misha Normal
    show Misha Normal at go_from_right(xxalign=.7)

    show GG Normal
    show GG Normal at go_from_right(xxalign=.99, xxzoom = -1)



    $ renpy.pause(.5, hard = True)



    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    show Misha Normal
    "Мишванда" "Наша встречи выглядят так, будто бы я определила тебя во «френдзону». "
    show Misha:
        xalign .7
    show GG:
        xalign .99
        xzoom -1.0
    with my_dissolve
    "[gg]" "С языка сняла."
    show Misha Normal
    "Мишванда" "Поэтому я хочу определиться с тем, стоит ли мне встречаться с тобой или нет."
    show GG Normal
    "[gg]" "Разве не проще было бы начать встречаться и уже в процессе отношений определяться, подходит тебе человек или нет? "
    show Misha Normal
    "Мишванда" "Хм…"
    show Misha Normal
    "Мишванда" "Наверное."


    $ renpy.pause(.4, hard = True)
    show Misha Smile:
        xzoom 1
    with my_dissolve

    $ renpy.pause(.3, hard = True)
    show GG Smile:
        ease 1.3 xalign .92

    show Misha Smile:

        ease 1.3 xalign .62
    $ renpy.pause(1.5, hard = True)
    show GG:
        xalign .92

    show Misha:

        xalign .62
    with my_dissolve
    "Мишванда" "Вот только, меня пугает твоё криминальное прошлое. "
    show GG Normal
    "[gg]" "Но я же сказал, что покончил с ним."
    show Misha Normal
    "Мишванда" "А оно с тобой покончило?"
    show GG Normal
    "[gg]" "…."
    show Misha Normal:
        xzoom -1
    with my_dissolve
    "Мишванда" "Ответь честно, пожалуйста."
    show GG Chagrin
    "[gg]" "Кое-какие трудности ещё имеются, это правда."

    "[gg]" "Однако я делаю всё возможное, чтобы вернуться к нормальной жизни. "
    show Misha Chagrin
    "Мишванда" "«Нормальной»…"



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
    "Мишванда" "Я всю жизнь живут в районе, где «норма» это когда ты оказываешься дома только с одним огнестрельным ранением, вместо двух."
    show Misha Chagrin
    "Мишванда" "Где не спиться, и не стать барыгой – это исключение из правил."
    show Misha Chagrin
    "Мишванда" "Вот, что у меня «норма»."
    show GG Normal
    "[gg]" "Я, разумеется, имею в виду другой способ жизни."
    show GG Normal
    "[gg]" "Без убийств, грабежей, обмана или наркотиков. "
    show GG Normal
    "[gg]" "Ходить на честную работу и быть уверенным в завтрашнем дне."
    show Misha Chagrin
    "Мишванда" "Да?"
    show GG Normal
    "[gg]" "Да!"

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
    show GG Smile:
        xalign .7

    show Misha Normal:
        xzoom -1
        xalign .35

    with my_dissolve
    "Мишванда" "И где ты работаешь?"
    show GG Normal
    "[gg]" "Эм…"
    show GG Normal
    "[gg]" "Ну, пока ещё нигде. Так, подрабатываю."
    show Misha Normal
    "Мишванда" "Ага, я видела, как ты фарцевал наркотиками возле моего магазина."
    show GG Embarrassment
    "[gg]" "…."
    show Misha Chagrin
    "Мишванда" "И это не единственное, что ещё держит тебя в криминальном мире, верно?"
    show GG Embarrassment
    "[gg]" "Верно."
    show Misha Chagrin
    "Мишванда" "Вот об этом я и говорю, [gg]."
    show Misha Chagrin
    "Мишванда" "Я хочу из этого вырваться, понимаешь?"
    show GG Chagrin
    "[gg]" "Честное слово, я борюсь со злом и внутри себя, и со внешним фактором."
    show Misha Chagrin
    "Мишванда" "От прошлого не убежишь, [gg]."
    show GG Chagrin
    "[gg]" "…."
    show GG Chagrin
    "[gg]" "Значит, у нас ничего не получится?"
    show Misha Embarrassment
    "Мишванда" "Я рискну."
    show GG Smile
    "[gg]" "Спасибо."
    show Misha Embarrassment
    "Мишванда" "Мы пришли."
    show GG Embarrassment
    "[gg]" "Могу я поцеловать тебя? "
    show Misha Embarrassment
    "Мишванда" "Хи-хи-хи."
    show Misha Embarrassment
    "Мишванда" "Только не в губы."
    show GG Smile
    "[gg]" "В щёчку?"
    show Misha:
        xzoom 1
    with Dissolve(.25)
    $ renpy.pause(.3)
    show Misha:
        easein 1.0 xalign 0.0
    $ renpy.pause(1.2,hard = True)
    show Misha:
        xzoom -1 xalign 0.0
    with Dissolve(.25)
    $ renpy.pause(.3)
    show Misha Tits_0
    show GG Surprise
    with my_vpunch

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "Мишванда" "Сюда."
    show GG Smile:
        easein 1.0 xalign .3
    "[gg]" "С превеликим удовольствием!"



    hide GG
    show Misha Tits_1
    with my_dissolve
    "Мишванда" "Оууууу!"
    "Мишванда" "Щекотно."
    "[gg]" "Мне остановиться?"
    "Мишванда" "Нет, продолжай."
    "Мишванда" "Мне очень нравится."
    "Мишванда" "Ты такой нежный, ласковый, мне нравится, как ты обращаешься с моими сиськами."
    "[gg]" "Мне только в радость тискать такую сладкую красивую грудь. "



    show Misha Tits_2
    with my_dissolve
    "Мишванда" "Ахххх!"
    "Мишванда" "Ты льстец и обманщик. "
    "Мишванда" "Наверняка ты говоришь это всем своим девушкам."
    "[gg]" "По твоему, все девушки предлагают целовать их грудь, вместо губ?"
    "Мишванда" "Нет…"
    "Мишванда" "Оххххххх!!!"
    "Мишванда" "Это моя фишка."
    "[gg]" "А моя фишка, делать комплименты твоим грудям, хе-хе."



    show Misha Tits_3
    with my_dissolve

    "Мишванда" "У тебя хорошо получается…"
    "Мишванда" "Да… Вот так."
    "Мишванда" "Покусывай их и соси."
    "Мишванда" "Ахххххх!!!"
    "Мишванда" "Дааааа, просто кайф."
    "[gg]" "Ом-ном-ном."
    "Мишванда" "Да-да-да…. Очень классно."
    "Мишванда" "Ещё…"



    "[gg]" "Мне нравится ласкать твои груди, но, может, продвинемся дальше?"
    "Мишванда" "Охххх!!.."
    show white with my_dissolve
    "Мишванда" "Аааахххххх…."
    show black with my_dissolve
    "Мишванда" "Нет, извини."
    "Мишванда" "Нам пора заканчивать. "
    $ renpy.pause(1, hard = True)
    show GG Passion

    show GG Passion:
        xzoom -1
        xalign .85








    hide white
    hide black
    show Misha Passion:
        xalign .15
    with my_dissolve
    "Мишванда" "До встречи, [gg]."
    show GG Passion
    "[gg]" "До скорого!"



    scene black with Dissolve(.5)

    $ location_now   = "City_Home"

    $ time.time_now  = "night"

    $ descript_Misha = _("Подкатывать к Мише дальше.")

    $ Event('misha_root_5_5', 'GG_Room', priority = 10, day_start = time.day_now + 1)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
