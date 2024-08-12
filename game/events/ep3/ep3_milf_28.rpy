label ep3_milf_28:







    hide screen main_interface
    $ location_now = 'Hall'
    call show_all_images_label from _call_show_all_images_label_57

    with Dissolve(.5)


















    "Игорь" "Прекрати меня отвлекать, чувак. Я работаю!"

    "[gg]" "Хорошо-хорошо."

    $ location_now = 'Hall'
    $ Event('ep3_milf_28',     'Milf_Room')

    jump main_interface_label




label ep3_milf_28_2:



    $ events.pop('ep3_milf_28', 0)

    $ events.pop('ep3_milf_28_2', 0)

    hide screen main_interface
    $ location_now = 'GG_Room'
    call show_all_images_label from _call_show_all_images_label_58
    with Dissolve(.5)





    show GG Think
    show GG Think:
        xalign .5
        ypos 1085

    with my_dissolve
    "[gg]" "Не могу избавиться от мысли, что всё, что мы делаем насмарку."
    "[gg]" "Жлоб, которому мы должны деньги, редкостный ублюдок. "
    "[gg]" "Где гарантии, что вернув свой долг, он не захочет ещё? К примеру, проценты. "
    "[gg]" "Или, видя, как мы смогли добыть такую крупную сумму, решит выведать, откуда они взялись. Тогда он сможет шантажировать нас снова… Или только меня."
    "[gg]" "Чую, одними деньгами мы не обойдёмся…"







    play sound 'audio/zvonok.mp3'

    $ block_exit_home    = False

    show GG Surprise

    "[gg]" "Что за?!.."
    $ Event('ep3_milf_28_officer_1',     'Corridor')
    $ Event('ep3_milf_28',     'Milf_Room')

    jump main_interface_label
label ep3_milf_28_officer_1:
    $ events.pop('ep3_milf_28_officer_1', 0)








    $ location_now  = 'Corridor'
    $ time.time_now = 'evening'

    hide screen main_interface

    call show_all_images_label from _call_show_all_images_label_59







    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085


    show Igor Spec_Normal_1
    show Igor Spec_Normal_1:
        ypos 1085

        xalign 1.8


    with Dissolve(.5)


    show Igor Spec_Normal_1:

        linear .7 xalign .95

    $ renpy.pause(.7, hard = True)

    hide Igor

    show Igor Spec_Normal_1

    show Igor Spec_Normal_1:
        ypos 1085

        xalign .95


    with my_dissolve


    "Игорь" "Какого хера, чувак?! Ты же сказал, что у меня будет куча времени!"
    "[gg]" "Спокуха, чувак. Спрячься пока. "



    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085


    show Igor Spec_Normal_1
    show Igor Spec_Normal_1:
        ypos 1085

        xalign .95


    with my_dissolve

    "Игорь" "Не хватало ещё в тюрьму загреметь… "

    show Igor Spec_Normal_1:

        xzoom -1
        linear .1 xalign 1.6

    $ renpy.pause(.1, hard = True)

    hide Igor

    show Igor Spec_Normal_1

    show Igor Spec_Normal_1:
        xzoom -1
        ypos 1085

        xalign 1.8


    with Dissolve(.5)
    $ Event('ep3_milf_28_officer_2',     'City_Home')

    play sound 'audio/zvonok.mp3'


    jump main_interface_label

label ep3_milf_28_officer_2:
    $ events.pop('ep3_milf_28_officer_2', 0)








    $ location_now  = 'Corridor'
    $ time.time_now = 'evening'

    hide screen main_interface

    call show_all_images_label from _call_show_all_images_label_60

















    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085



    hide Igor

    show Officer Normal

    show Officer Normal:
        xzoom -1
        ypos 1085


        xalign .95


    with Dissolve(.5)

    "Офицер" "Доброго времени суток, [gg]."
    show GG Angry
    "[gg]" "Д-добрейшего вечерочка, офицер. "
    show GG Normal
    "[gg]" "Я вас не ждал, если честно. "
    "Офицер" "Зря. Твой опекун дома? "
    "[gg]" "Нет. Она и Кристи пошли в театр."
    "Офицер" "Понятно. Значит, ты дома один? "
    "[gg]" "Ну да. Только я и… никого."
    "Офицера" "Хм… Как интересно. И Марина не боится оставлять квартиру в твоём распоряжении?"
    show GG Laughs
    "[gg]" "Я быстро вернул доверие. "

    "Офицер" "Это похвально. "
    "Офицер" "Именно поэтому я здесь. Хотел убедиться, что твоя адаптация проходит в правильном русле. "
    show GG Normal
    "[gg]" "Как видите. "
    "Офицер" "Что ж. Тогда до встречи. Зайду в другой раз."
    "[gg]" "Ага. До свидания."

    hide Officer with Dissolve(.5)

    $ renpy.pause(.5, hard = True)

    show GG Think:
        xalign .5

    with Dissolve(.5)

    $ renpy.pause(.5)





    "[gg]" "Жесть…"
    "[gg]" "Чуть не попались!"
    "[gg]" "Надо вернуться в комнату и успокоиться. "

    $ Event('ep3_milf_28_3',    'GG_Room')

    $ block_exit_home = True

    jump main_interface_label









label ep3_milf_28_3:
    $ events.pop('ep3_milf_28_3', 0)


    $ location_now  = 'GG_Room'
    $ time.time_now = 'evening'

    hide screen main_interface

    call show_all_images_label from _call_show_all_images_label_61
    with Dissolve(.5)


    show GG Think
    show GG Think:
        xalign .5
        ypos 1085


    with Dissolve(.5)

    "[gg]" "Думаю, после такого стресса, я заслужил немного отдыха. "

    $ block_time_forward = False
    $ Event('ep3_milf_28_4',    None, time = ['night', 'morning'])

    jump main_interface_label















label ep3_milf_28_4:

    $ events.pop('ep3_milf_28_4', 0)

    $ events.pop('ep3_milf_28_3', 0)

    $ block_time_forward = True

    $ location_now  = 'GG_Room'
    $ time.time_now = 'night'

    hide screen main_interface

    call show_all_images_label from _call_show_all_images_label_62
    with Dissolve(.5)


    show GG Normal
    show GG Normal:
        xalign .5
        ypos 1085


    with Dissolve(.5)



    show GG Normal

    "[gg]" "Пора проверить, как там Игорь."


    play sound 'audio/zvonok.mp3'

    show GG Surprise:
        xzoom -1

    "[gg]" "Что? Опять?!"

    show GG Angry

    "[gg]" "Чёрт, уже совсем поздно. Это наверняка Марина и Кристи вернулись из театра!"


    $ Event('ep3_milf_28_56',     'Corridor')




    jump main_interface_label


label ep3_milf_28_56:





    $ events.pop('ep3_milf_28_56', 0)
    $ location_now  = 'Corridor'

    $ time.time_now = 'night'

    hide screen main_interface

    call show_all_images_label from _call_show_all_images_label_63
    with Dissolve(.5)

    show GG Angry

    show GG Angry:
        xalign .1
        ypos 1085






    show GG Normal

    show GG Normal:
        xalign .1
        ypos 1085



    show Igor Spec_Normal_1
    show Igor Spec_Normal_1:
        ypos 1085

        xalign 1.8


    with Dissolve(.5)


    show Igor Spec_Normal_1:

        linear .7 xalign .95

    $ renpy.pause(.7, hard = True)

    hide Igor

    show Igor Spec_Normal_1

    show Igor Spec_Normal_1:
        ypos 1085

        xalign .95




















    $ block_time_forward = True

    "Игорь" "Я почти вскрыл сейф, чувак! Кто бы это ни был, задержи их любым способом. "
    "[gg]" "Постараюсь. Если не смогу, попробуй спрятаться. "
    "Игорь" "Никак! Систему просто так не отключить. Это тебе не вилку из розетки выдернуть."
    "Игорь" "Или ты отвлечёшь их, или я загремлю на нары! "
    "[gg]" "Ладно, понял. "
    "Игорь" "Я в тебя верю! "
    "[gg]" "Ага, спасибо…"



    show Igor Spec_Normal_1
    show Igor Spec_Normal_1:
        ypos 1085

        xalign .95


    with Dissolve(.1)


    show Igor Spec_Normal_1:
        xzoom -1
        linear .5 xalign 1.8

    $ renpy.pause(.5, hard = True)

    hide Igor

    show Igor Spec_Normal_1

    show Igor Spec_Normal_1:
        ypos 1085

        xalign 1.8








    show GG Think
    "[gg]" "Блин, ну и что мне сказать?.."


    play sound 'audio/zvonok.mp3'

    show GG Think
    "[gg]" "Я же не смогу держать их у двери вечно."


    play sound 'audio/zvonok.mp3'

    show GG Chagrin
    "[gg]" "Иду-иду. Сейчас открою..."
    show GG Think
    "[gg]" "Идея! Притворюсь, будто бы принимал душ. "
    show GG Think
    "[gg]" "Кину штаны в стирку, и…"
    $ block_exit_home = True
    $ descript = _("Кинуть штаны в стиральную машину.")

    $ locations['Restroom'].buttons[0].update({'washer': ((0, 650, 453, 429), [Jump('ep3_milf_29')])})



    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
