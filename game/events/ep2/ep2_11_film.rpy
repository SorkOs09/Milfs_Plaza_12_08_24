
label ep2_11_film:

    if not from_gallery_check():
        if get_item('Попкорн', True) is None:
            '[gg]' "Мне нужно еще купить попкорн"
            jump main_interface_label
    call show_bg_image_label from _call_show_bg_image_label_33
    call show_additional_images_label from _call_show_additional_images_label_28
    $ remove_from_inventory('Попкорн')
    $ unlock_film_alexandr = True


    if not getattr(store, '_from_talk_with_milf', False):
        $ events.pop('ep2_11_film', 0)
    show Milf Night_Normal
    show Milf Night_Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left

    $ renpy.pause(1)

    show GG Normal
    "[gg]" "У меня тут проблемка возникла…"
    show Milf Night_Smile:
        xalign .85
    show GG:
        xalign .15
    with my_dissolve
    "Марина" "Да?.."
    show GG Laughs
    "[gg]" "Я, знаешь ли, купил два огромных ведра с попкорном и не совсем уверен, что одолею их самостоятельно…"
    show Milf Night_Smile
    "Марина" "Карамельный? "
    show GG Normal
    "[gg]" "Ага."
    show Milf Night_Smile
    "Марина" "Чур я выбираю кино! "
    show GG Smile
    "[gg]" "Справедливо!"

    scene expression '#000' with Dissolve(.5)

    scene expression 'cg/ep2/alexandr/cinema_alexandr_0.png'
    with Dissolve(.5)


    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "Фильм" "Я кажусь тебе такой же старой?.."


    "Фильм" "«Пронзительный взгляд» "


    scene expression 'cg/ep2/alexandr/cinema_alexandr_bg.png'
    show expression 'cg/ep2/alexandr/cinema_alexandr_bg_1.png'
    show expression 'cg/ep2/alexandr/CA1.png'
    show expression 'cg/ep2/alexandr/cinema_alexandr_fg.png'
    show GG Invis:
        xalign .44
    show Milf Invis:
        xalign .7
    with Dissolve(.5)


    if not getattr(store, '_from_talk_with_milf', False):

        "[gg]" "Ты не смотришь кино."


        "Марина" "А? Что? "


        "Марина" "С чего ты решил?"


        "[gg]" "Ты не притронулась к попкорну и сидишь, как заворожённая. "


        "Марина" "…."


        "Марина" "Да, наверное ты прав, но я не хочу грузить тебя проблемами."


        "[gg]" "Зато я хочу. Что случилось?"


        "Марина" "Не выкинуть из головы нашу ссору с Кристи. "


        "Марина" "Я ужасная мать…"


        "[gg]" " Да ну, Кристи та ещё транжира. "


        "[gg]" "Иногда, наверное, её стоит приводить к чувства."


        "Марина" "Это не те деньги, ради которых стоит устраивать скандал. "


        "Марина" "Просто…"


        "Марина" "Джеймс не звонит уже несколько месяцев."


        "[gg]" "И ты волнуешься? Понимаю."
    else:
        call wait_click_label from _call_wait_click_label

    scene expression 'cg/ep2/alexandr/cinema_alexandr_bg.png'
    show expression 'cg/ep2/alexandr/cinema_alexandr_bg_1.png'
    show expression 'cg/ep2/alexandr/CA2.png'
    show expression 'cg/ep2/alexandr/cinema_alexandr_fg.png'

    show GG Invis:
        xalign .44
    show Milf Invis:
        xalign .7
    with Dissolve(.5)



    if not getattr(store, '_from_talk_with_milf', False):
        "Марина" "Нет, я зла на него!"


        "Марина" "Я прекрасно знаю, что с ним всё в порядке. "


        "Марина" "Он не звонит, потому что не хочет. "


        "Марина" "Его всецело устраивает такое положение вещей."


        "Марина" "Он уезжает заграницу, проводит там столько времени, сколько считает нужным, и наверняка изменяет мне, поскольку понимает, что я никогда об этом не узнаю."


        "Марина" "Ладно, хорошо! Это я ещё могу понять, хотя мне жутко обидно, и лично я, почему-то, храню ему верность."


        "[gg]" "Это твои предположения."


        "Марина" "Допустим. "


        "Марина" "Тогда как объяснить, что когда Джеймс возвращается, он совсем не притрагивается ко мне?"


        "Марина" "Он редко говорит со мной, и предпочитает проводить время в одиночестве."


        "[gg]" "…."


        "[gg]" "Наверное, я скажу полнейшую глупость, но может он… устаёт?"

    else:
        call wait_click_label from _call_wait_click_label_1
    scene expression 'cg/ep2/alexandr/cinema_alexandr_bg.png'
    show expression 'cg/ep2/alexandr/cinema_alexandr_bg_1.png'
    show expression 'cg/ep2/alexandr/CA3.png'
    show expression 'cg/ep2/alexandr/cinema_alexandr_fg.png'
    
    show GG Invis:
        xalign .44
    show Milf Invis:
        xalign .7
    with Dissolve(.5)



    if not getattr(store, '_from_talk_with_milf', False):
        "Марина" "Лучше бы он был геем!"


        "[gg]" "Ха-ха-ха!"
    else:
        call wait_click_label from _call_wait_click_label_2

    scene expression 'cg/ep2/alexandr/cinema_alexandr_bg.png'
    show expression 'cg/ep2/alexandr/cinema_alexandr_bg_1.png'
    show expression 'cg/ep2/alexandr/CA4.png'
    show expression 'cg/ep2/alexandr/cinema_alexandr_fg.png'

    show GG Invis:
        xalign .44
    show Milf Invis:
        xalign .7
    with Dissolve(.5)



    if not getattr(store, '_from_talk_with_milf', False):
        "Марина" "Но нет, это не так."


        "Марина" "Я ему наскучила, вот и всё. "


        "Марина" "Джеймс не воспринимает меня как женщину. Живую, из плоти и крови. Полную страсти и желаний."


        "Марина" "Я для него вещь, старая, ценная реликвия, которую надо беречь, потому что так требуют социальное положение в обществе."


        "Марина" "Формальное приложение к его идеальной жизни."


        "[gg]" "…."


        "Марина" "Я чувствую себя никчёмной…"


        "[gg]" "Тогда почему ты не разведёшься? "


        "Марина" "Боюсь…"


        "[gg]" "Чего?"


        "Марина" "Остаться одной."


        "Марина" "Кому нужна старая одинокая женщина?.."

    else:
        call wait_click_label from _call_wait_click_label_3
    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    if not getattr(store, '_from_talk_with_milf', False):
        scene expression 'cg/ep2/alexandr/cinema_alexandr_bg.png'
        show expression 'cg/ep2/alexandr/cinema_alexandr_bg_1.png'
        show expression 'cg/ep2/alexandr/CA5.png'
        show expression 'cg/ep2/alexandr/cinema_alexandr_fg.png'

        show GG Invis:
            xalign .44
        show Milf Invis:
            xalign .7
        with Dissolve(.5)


        $ renpy.music.stop(fadeout=1.5)



        "[gg]" "Не говори так!"


        "[gg]" "Ты потрясающая! "


        "Марина" "Ты просто успокаиваешь меня."


        "[gg]" "Нет, это правда."
    else:
        call wait_click_label from _call_wait_click_label_4


    scene expression 'cg/ep2/alexandr/cinema_alexandr_bg.png'
    show expression 'cg/ep2/alexandr/cinema_alexandr_bg_6.png'
    show expression 'cg/ep2/alexandr/CA6.png'
    show expression 'cg/ep2/alexandr/cinema_alexandr_fg.png'

    show GG Invis:
        xalign .44
    show Milf Invis:
        xalign .7
    with Dissolve(.5)



    if not getattr(store, '_from_talk_with_milf', False):
        "[gg]" "Я понимаю, что сказанное мною сейчас, может быть воспринято неадекватно, но будь я на месте Джеймс, то горел бы от нетерпения, чтобы увидеться с тобой как можно скорее."



        "Марина" "Но почему?.."


        "[gg]" "Потому что ты самая желанная, привлекательная женщина, которую я только знаю!"


        "[gg]" "Быть рядом с тобой, и не сгорать от стыда, наслаждаясь видом твоего горячего тела попросту невозможно."


        "Марина" "Моего горячего тела?.."


        "[gg]" "Да!"


        "[gg]" "Разве можно быть равнодушным к твоей красоте? "


        "[gg]" "Твоим…огромным, соблазнительным грудям, по которым стекают капли пота?!"






        "[gg]" "Разве можно не восхищаться твоими будоражащими формами, от вида которых у меня дрожат пальцы?! "


        "Марина" "Ты… Смущаешь меня."


        "[gg]" "Извини, я наверное, слишком увлёкся. "


        "Марина" "Но знаешь…"


        "Марина" "Это очень приятно слышать."


        "Марина" "Спасибо тебе огромное. "


        "Марина" "Я рада, что у меня такое замечательный друг."

    else:
        $ from_say_screen = False
        call wait_click_label from _call_wait_click_label_5
    scene expression 'cg/ep2/alexandr/CA7.png'

    show GG Invis:
        xalign .44
    show Milf Invis:
        xalign .7
    with my_dissolve





    "[gg]" "Боже, какие же у неё сочные сиськи…"


    "[gg]" "Как бы я хотел прильнуть к ним и пососать её молочко…"

    if not getattr(store, '_from_talk_with_milf', False):
        "[gg]" "Джеймс не достоин её."


        "[gg]" "Оставлять такую женщину одну, и проявлять к ней абсолютное равнодушие по возвращению?!"


        "[gg]" "Он точно голубой…"


    "Марина" "Кажется, он пялиться на меня."


    "Марина" "Точнее не на меня, а на мои груди."


    "Марина" "Пусть."

    if not getattr(store, '_from_talk_with_milf', False):
        "Марина" "Я в таком отчаянии, что чуточку внимания от друга мне не помешает. "





    scene expression 'cg/ep2/alexandr/CA8.png'

    show GG Invis:
        xalign .44
    show Milf Invis:
        xalign .7
    with Dissolve(.5)





    "Марина" "Ой…"


    "[gg]" "Не ловко получилось…"


    

    if getattr(store, '_from_talk_with_milf', False):
        scene black with Dissolve(.3)
        $ renpy.pause(.5)
        jump main_interface_label






    call show_bg_image_label from _call_show_bg_image_label_34
    call show_additional_images_label from _call_show_additional_images_label_29
    show GG Normal
    show GG Normal:
        xalign .25
        ypos 1085
        zoom 1.0-0.035
    show Milf Night_Normal
    show Milf Night_Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)

    "Марина" "Сладких снов, [gg]."


    "[gg]" "С-сладких, Маришка…"

    hide Milf
    show GG Think:
        xalign .5
    with Dissolve(.5)
    "[gg]" "Я начинаю испытывать безумное влечение к Марине."
    show GG Think
    "[gg]" "Прекрати, слышишь?! Прекрати о таком думать! "
    show GG Think
    "[gg]" "Она твоя подруга, и не более, чёртов извращенец."




    $ add_to_gallery(1)
    if not from_gallery_check():


        $ descript = _("Лечь спать. ")
















        $ Event('ep2_11_sms', 'GG_Room', time = ['morning'])
        $ time.time_now = 'night'

        scene expression '#000' with Dissolve(.5)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
