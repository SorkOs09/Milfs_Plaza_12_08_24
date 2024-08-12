label ep2_4_5_igor:
    $ events.pop('ep2_4_5_igor', 0)


    call show_bg_image_label from _call_show_bg_image_label_117
    call show_additional_images_label from _call_show_additional_images_label_96
    with Dissolve(.5)

    show Igor Normal
    show Igor Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)




    show GG Angry
    show GG Angry at go_from_left

    '[gg]' "Чувак, у меня тут проблема кое с кем возникла…"
    'Игорь' "Бро, и ты пришёл, чтобы повесить её на меня? "
    show GG Please:
        xalign .15
    with my_dissolve
    '[gg]' "Нет, но я рассчитывал, что ты поможешь мне. "
    '[gg]' "Двое чудаков заняли моё место у магазина. Давай отмудохаем их."
    show Igor Bad
    'Игорь' "Извини, приятель, но я и так делаю твою работу."
    show GG Think
    '[gg]' "Окей. Тогда, может, посоветуешь что-нибудь?"
    show Igor Normal
    'Игорь' "Воспользуйся чем-то, чем можно хорошенько приложить по голове. "
    show GG WTF
    '[gg]' "Я так и думал."
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
