label milf_root_12:






    $ events.pop('milf_root_12', 0)






    call show_bg_image_label from _call_show_bg_image_label_152
    play sound 'audio/zvonok.mp3'
    $ renpy.pause(.3, hard = True)
    show GG Think
    if getattr(store, 'old_location', None) in ['Hall', "Restroom"]:

        show GG Think at go_from_right(xxalign = .15)
    elif True:
        show GG Think at go_from_left
    show Milf Normal
    show Milf Normal at go_from_right
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Марина" "Я открою."
    show Milf Surprise:
        xalign .85
    show GG:
        xalign .15
    with my_dissolve
    "Марина" "Возможно это полицейский, включай диктофон. "
    show GG Normal
    "[gg]" "Окей."
    show Officer Normal
    show Officer Normal:
        alpha 0 xalign .55 xzoom -1
        easein_cubic .5 xalign .5 alpha 1.0
    show Milf Angry
    with my_dissolve
    "Офицер" "Вечер добрый…"

    show GG Angry:
        easein_cubic .5 xalign .1
    "[gg]" "Бывало и добрее. "
    show Milf Normal

    "Марина" "Здравствуйте, офицер. Вас оставить наедине? "
    show GG:
        xalign .1
    show Officer:
        xzoom 1
        xalign .5 alpha 1.0
    with my_dissolve

    "Офицер" "Да, если можно. "

    show Milf Smile:
        easein_cubic 1 ypos 1095
        easein_cubic 1 ypos 1085
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha 0
        easein_cubic 1 alpha .5
        easein_cubic 1 alpha 0
    with my_dissolve
    "" "{i}Марина подмигивает вам{/i}"







    show GG:
        easein_cubic 2 xalign 1.5
    show Officer:
        xzoom 1
        easein_cubic 2 xalign 1.5
    show black:
        alpha 0.0
        easein_cubic 1 alpha 1.0
    $ renpy.pause(1.2, hard = True)

    $ location_now = 'Hall'

    call show_bg_image_label from _call_show_bg_image_label_153
    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    show GG Angry

    show GG Angry at go_from_left(xxzoom = .95, yyzoom = .95)

    show Officer Normal
    show Officer Normal at go_from_left(xxalign = .9)


    $ renpy.pause(1, hard = True)

    show expression 'cg/ep85/milf_stealth.png'

    show expression 'cg/ep85/milf_stealth.png':
        xpos -300 ypos 1080
        easein_cubic 1 xpos 50

    "[gg]" "Ну, чего опять припёрься?"

    show GG:
        xalign .15
    show Officer Normal:
        xzoom -1 xalign .9
    with my_dissolve
    "Офицер" "Ты почему грубишь представителю закона?"

    show expression 'cg/ep85/milf_stealth.png':
        ypos 1080
        xpos 50
    show Officer Angry
    "Офицер" "Я, можно сказать, с рабочим визитом. "
    show Officer Angry
    "Офицер" "Убеждаюсь в том, что предписание судьи выполняется. Не более."
    show GG Skepticism
    "[gg]" "Мы оба прекрасно знаем, зачем ты здесь!"
    show Officer Normal
    "Офицер" "Для диалога, [gg], только для диалога."

    show expression 'cg/ep85/milf_stealth.png':
        xpos 50
        ypos 1080
        easein_cubic 1 xpos 70
    show GG Angry

    "[gg]" "И что вы хотите услышать? Чтобы я «продал» Марину?!"
    show Officer Normal
    "Офицер" "Для начала я хочу, чтобы ты успокоился. "
    show GG Angry
    "[gg]" "Я спокоен."
    show Officer Smile
    "Офицер" "Хе-хе-хе. Ну, как скажешь."
    show Officer Normal
    "Офицер" "Мне не нужно твоё уважение, парень. Поступки больше говорят за человека."
    show Officer Laughs
    "Офицер" "Напомню, что по окончанию срока общественных работ, которые ты обязан выполнять ежедневно, именно мне предстоит написать твою характеристику судье."
    show Officer Normal
    "Офицер" "Не говоря уже о следователе…"
    show GG Angry
    "[gg]" "Ну-ну. "
    show GG Angry
    "[gg]" "Это похоже на шантаж."
    show Officer Angry
    "Офицер" "Пффф. Просто смешно."
    show Officer Normal
    "Офицер" "Я не повторяю дважды, парень, но я готов ждать. И надеяться."
    show GG Angry
    with my_vpunch
    "[gg]" "На что надеяться?! На то, что я позволю тебе приставать к Марине?!"
    show Officer Skepticism
    "Офицер" "Ты что, пил? "
    show Officer Skepticism
    "Офицер" "Хочу верить, что в следующий раз ты прекратишь устраивать истерики. Времени у тебя немного."
    show expression 'cg/ep85/milf_stealth.png':
        xpos 50
        ypos 1080
        easein_cubic 1 xpos -150
    show GG Angry:
        easein_cubic .5 xzoom 1 yzoom 1 xalign .5
    "[gg]" "Это угроза, да?! Вы угрожаете мне?"
    show GG:
        xalign .5
        xzoom -1
    with my_dissolve
    show Officer Normal:
        easein_cubic 4 xalign -1.5
    "Офицер" "До встречи, [gg]."
    show GG:
        xzoom -1
        easein_cubic 3 xalign -1.5
    $ renpy.pause(1, hard = True)

    scene black with Dissolve(.5)



    $ location_now = 'Corridor'

    call show_bg_image_label from _call_show_bg_image_label_154
    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    show GG Angry

    show GG Angry at go_from_right(xxalign = .99, xxzoom = -1)

    show Officer Hm
    show Officer Hm at go_from_right(xxalign = .7, xxzoom = -1)


    $ renpy.pause(1.3, hard = True)




    show GG:
        xalign .85
    show Officer Hm:
        xalign .7



    show Milf Normal
    show Milf Normal at go_from_left(xxzoom = -1)

    "Офицер" "До новых встреч, хозяева. "
    show Milf Normal:
        xalign .15
    with my_dissolve
    "Марина" "До встречи…"

    show Officer:
        alpha 1.0
        easein_cubic 1 alpha .0 xalign .5

    show GG Angry:
        easein_cubic .7 xalign .8
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "…"

    hide Officer
   


    show Milf Normal
    "Марина" "Ничего не получилось, да?"
    show GG Please:
        xalign .8
    with my_dissolve
    "[gg]" "Ты сама всё видела."
    show Milf Embarrassment
    "Марина" "Такое чувство, словно он раскусил нас."
    show GG WTF
    "[gg]" "Не думаю. Просто подстраховывается."
    show GG Angry
    "[gg]" "Я недооценил этого мудака. "
    show GG WTF
    show Milf Chagrin
    with my_dissolve
    "[gg]" "Он, как матёрый бандит, предусмотрел возможность просушки, и два раза одно и тоже повторять не станет. "
    show GG WTF
    "[gg]" "По крайней мере вслух."
    show Milf Normal
    "Марина" "И что же нам делать? Снова ждать?"
    show GG Think
    "[gg]" "Надо думать…"
    show Milf Normal
    "Марина" "Хм… [gg]?"
    show GG Normal
    "[gg]" "Да?"
    show Milf Embarrassment
    "Марина" "А могу я тоже предложить свой план?"
    show GG Surprise
    "[gg]" "О боже…"
    show GG Skepticism
    "[gg]" "Только не говори, что всё это время только и делала, что думала о том, как поступить в сложившейся ситуации!"
    show Milf Smile
    "Марина" "У домохозяйки не слишком много забот, знаешь ли, ха-ха-ха."
    show GG Skepticism
    "[gg]" "Ну ладно, выкладывай."
    show Milf Normal
    "Марина" "Короче, тут вот какое дело… "
    show Milf Normal
    "Марина" "Если первостепенная задача полицейского добиться моего расположения, то почему бы нам не опередить его?"
    show GG Surprise
    "[gg]" "….."
    show GG Surprise
    "[gg]" "Что ты имеешь в виду?!"
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .0
        easein_cubic 1 alpha .45

    show Milf Passion
    "Марина" "Я имею в виду, что мы можем запечатлеть, как он непосредственно домогается меня."
    show expression 'cg/ep45/shower_3/shadow.png':
        easein_cubic 1 alpha .65

    show Milf Passion
    "Марина" "Уж такое развитие событий он явно не предусмотрит, а?"
    show GG Chagrin
    "[gg]" "Мне не нравится как это звучит, Маришка. "
    hide expression 'cg/ep45/shower_3/shadow.png'
    show Milf Angry
    with my_dissolve
    "Марина" "Эй, я не собираюсь отдаваться этому грязному копу, милый!!"
    show Milf Normal
    "Марина" "Я лишь подыграю полицейскому."
    show Milf Smile
    show GG WTF
    with my_dissolve
    "Марина" "Когда он начнёт лезть до меня, дам отворот-поворот! Перцовый баллончик всегда при мне. "
    show Milf Normal
    "Марина" "Ты снимешь это на камеру и вуаля, доказательства его бесчинства!"
    show GG Chagrin
    "[gg]" "Чёрт… Не знаю-не знаю, всё это чересчур рискованно. "
    show Milf Embarrassment:
        easein_cubic .5 xalign .25
    "Марина" "Милый… "
    show Milf Embarrassment:
        easein_cubic .5 xalign .35
    "Марина" "Любименький… "
    show Milf Embarrassment:
        easein_cubic .5 xalign .15
    "Марина" "Доверься мне, я всё сделаю как надо. "
    show Milf Embarrassment
    "Марина" "Этого негодяя следует проучить!"
    show GG Please
    "[gg]" "А если я не успею помочь?"
    show Milf Embarrassment:
        xalign .15

    with my_dissolve
    "Марина" "Ты всегда будешь рядом. "
    show Milf Embarrassment
    "Марина" "Заранее спрячешься, я встречу офицера как ни в чём не бывало, приглашу его в спальню, он себе нафантазирует страсти-мордасти, ну а дальше ты понял."
    show GG Angry
    "[gg]" "А дальше он начнёт распускать руки…"
    show Milf Smile
    "Марина" "Достаточно одного его движения, и я достаю перцовый баллончик!"
    show GG Normal
    "[gg]" "Но он увернётся или обхватит тебя насильно, и ты не сможешь ничего сделать?!"
    show Milf Passion
    "Марина" "Вот тогда появишься ты, и спасёшь меня!"
    show GG Laughs
    "[gg]" "Хе-хе…"
    show Milf Embarrassment
    "Марина" "Ну пожаааааалуйста, [gg], позволь мне проявить себя. Я так хочу помочь!"
    show GG Normal
    "[gg]" "……."
    show GG WTF
    "[gg]" "Ладно, но я лично проконтролирую, чтобы всё шло строго по плану. "
    show GG Angry
    "[gg]" "Понятно?!"
    show Milf Smile
    "Марина" "Конечно, миленький!!!"
    show GG Skepticism
    "[gg]" "Ладно, давай попробуем."
    show Milf Laughs
    "Марина" "Ураааа!"



    $ milf_root_9_text= _("Дождаться появления офицера полиции через 2-3 дня вечером в коридоре.")
    $ Event('milf_root_13', location = "Corridor", day_start = time.day_now+2, time = ['evening'])
    $ new_events = True
    $ events.pop('milf_root_12', 0)
    $ events.pop('milf_root_11', 0)
    
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
