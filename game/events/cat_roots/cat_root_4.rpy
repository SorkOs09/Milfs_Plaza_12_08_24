label cat_root_4:
    $ location_now = 'City_Home'
    $ events.pop('cat_root_4', 0)
    $ remove_from_inventory("Чёрные очки")
    #show Kat Embarrassment
    #show Kat Embarrassment at go_from_right
    scene image 'cg/cat_root/cat_go_out.png'
    with Dissolve(.5)
    "Кэт" "Чёрт, я уже опаздываю."
   # show Kat Embarrassment
    "Кэт" "На автобус уже не успеваю, а такси ждать времен нет. Придётся бежать…"

    #show Kat Embarrassment:
    #    linear 1.0 xalign -1.5
    #$ renpy.pause(1, hard = True)

    call show_bg_image_label from _call_show_bg_image_label_109
    with Dissolve(.5)

    show GG Black
    show GG Black at go_from_right(xxalign = .5, xxzoom = -1)

    "[gg]" "А она быстрая!"
    show GG Black
    "[gg]" "Нужно срочно догнать её!"
    show GG:
        linear 1.0 xalign -1.5
    $ renpy.pause(1, hard = True)
    scene expression 'interface/city_interface/city_bg_night.png'
    with Dissolve(.5)



    "[gg]" "Чёрт, кажется я потерял её…"
    "[gg]" "Судя по тому, как быстро она скрылась из виду, она где-то в этом районе."
    "[gg]" "Нужно проверить все известные мне места и найти её."
    scene expression '#000' with Dissolve(.5)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    scene expression 'cg/ep4/ep4_restaurant_bg_blur.png'
    with Dissolve(.5)









    show GG Black
    show GG Black at go_from_left


    "[gg]" "Что ж…"
    show GG Black
    "[gg]" "Кажется и здесь её тоже нет."
    show GG Black
    "[gg]" "Да и что ей здесь делать?"
    show RestAdmin Normal
    show RestAdmin Normal at go_from_right


    show RestAdmin Normal
    "Официант" "Здравствуйте, сэр, вы желаете заказать столик? "
    show GG Black
    "[gg]" "Нет, я просто проходил мимо."
    show RestAdmin Normal
    "Официант" "Вы уверены? Это лучший ресторан в городе."
    show RestAdmin Normal
    "Официант" "Наши повара настоящие чародеи кулинарного искусства, а официанты мастера в обслуживании, и крайне угодливы за самые скромные чаевые."
    show RestAdmin Normal
    "Официант" "Вам у нас понравиться, поверьте."
    show RestAdmin Normal
    "Официант" "И так, вы всё ещё собираетесь уходить?"
    show GG Black
    "[gg]" "Что ж… Я ещё постою, подумаю."



    show RestAdmin Normal:
        xzoom -1
        linear 1 xalign 1.5
    $ renpy.pause(1, hard = True)
    show Kat Off_Normal
    show Kat Off_Normal at go_from_right
    "Кэт" "Сэр, позвольте мне пройти, мне нужно обслужить столик позади вас. "
    show GG Black
    "[gg]" "Твою мать…"
    show Kat Off_Normal
    "Кэт" "Сэр?.."

    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/aerosol-of-my-love-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    show GG Smile
    with my_dissolve
    "[gg]" "Тебе идёт эта форма."
    show Kat Off_Surprise
    "Кэт" "Ублюдок, как ты здесь оказался?!"
    show Kat Off_Angry
    "Кэт" "Говноед сраный, да ты же следил за мной!"
    show GG Laughs
    "[gg]" "…мастера обслуживания, говорили они."

    "Кэт" "Какие ещё мастера, мудак ты недобитый, я сейчас вылью тебе этот суп за шиворот! "
    show GG Normal
    "[gg]" "Успокойся, наконец, дурочка."
    show GG Normal
    "[gg]" "Я здесь не для того, чтобы насмехаться над тобой. "

    "Кэт" "Да ну?!"
    show GG Normal
    "[gg]" "Наоборот, я горжусь тобой. Ты большая молодец."
    show GG Normal
    "[gg]" "Ты являешься для меня позитивным примером. Понимаешь?"

    "Кэт" "Батрачить официантом это, по твоему, позитив?!"
    show GG Normal
    "[gg]" "Зарабатывать честным трудом – вот, что я вижу. "
    show Kat Off_Skepticism
    "Кэт" "Приходится…"
    show GG Normal
    "[gg]" "Кажется, твоя начальница возвращается."


    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    show GG Black
    with Dissolve(.5)
    show Kat Off_Normal:
        linear .5 xalign .5
    $ renpy.pause(.5, hard = True)
    show RestAdmin Normal at go_from_right






    "Официант" "О, сэр, вы всё ещё здесь."
    show RestAdmin Normal
    "Официант" "Я слышала какие-то крики. Эта официантка докучает вам?"
    show GG Black
    "[gg]" "Нет, наоборот. "
    show GG Black
    "[gg]" "Она восхитительна. "
    show RestAdmin Normal
    "Официант" "Значит, вы таки остаётесь? "
    show GG Black
    "[gg]" "К сожалению, у меня дела. Но я ещё вернусь. "
    show RestAdmin Normal
    "Официант" "Рада это слышать. "
    show RestAdmin Normal
    "Официант" "Катерина, пожалуйста, займись своим заказом."
    show Kat Off_Normal
    "Кэт" "Да, конечно."


    show Kat Off_Normal:
        linear .5 xalign .3
    $ renpy.pause(.5, hard = True)
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .5
    with my_dissolve
    "Кэт" "Пссс!"
    show Kat Off_Smile
    "Кэт" "Завтра утром пошалим. Хи-хи."
    show GG Black
    "[gg]" "Замётано. "
    $ location_now  = 'Corridor'
    $ time.time_now = 'night'
    $ old_descript_Cat = 's'
    $ descript_Cat  = _('Пошалить с Кэт')

    $ events.pop('cat_root_2', 0)

    $ events.pop('cat_root_3', 0)

    $ events.pop('cat_root_4', 0)

    #$ Event('cat_root_5_0', 'Corridor', day_start = time.day_now + 1,)



    # $ locations['GG_Room'].image_buttons_times = {
    # 'morning'   : {'kat_on_bed_2': Jump('cat_root_5'),},
    # 'afternoon' : {'kat_on_bed_2': Jump('cat_root_5'),},
    # 'evening'   : {'kat_on_bed_2': Jump('cat_root_5'),},
    # 'night'     : {}
    # }


    scene expression '#000' with Dissolve(.5)

    jump cat_root_5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
