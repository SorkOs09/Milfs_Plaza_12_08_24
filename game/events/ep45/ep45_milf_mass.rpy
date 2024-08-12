
image ep5_milf_help_anim_1 = Ani('cg/ep5/mass/anim_1/', 2,  float(70)/100, reverse = True, effect=Dissolve(.1), start=1,)

image ep5_milf_help_anim_2 = Ani('cg/ep5/mass/anim_2/', 2,  float(70)/100, reverse = True, effect=Dissolve(0.1), start=1,)

image ep5_milf_help_anim_3 = Ani('cg/ep5/mass/anim_3/', 5,  float(18)/100, reverse = True, effect=Dissolve(0.1), start=1,)

image ep5_milf_help_anim_4 = Ani('cg/ep5/mass/anim_4/', 5,  float(18)/100, reverse = True, effect=Dissolve(0.04), start=1,)




label ep5_milf_help:
    $ Hide('main_interface', transition = Dissolve(.5))()







    if not hasattr(store, 'help_ep5_milf'):
        $ help_ep5_milf = 0

    if mp.help_ep5_milf is None:
        $ mp.help_ep5_milf   = 0
        $ mp.save()
    if mp.help_ep5_milf < help_ep5_milf:
        $ mp.help_ep5_milf = help_ep5_milf
        $ mp.save()

    if from_gallery_check():
        $ help_ep5_milf = mp.help_ep5_milf


    menu:
        "Уборка в комнате 1 ур" if True:
            $ show_text_animation('+10 milf')

            $ pass


            $ renpy.music.stop(fadeout=.5)

            $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)
            $ add_to_gallery(-3)
            call ep5_milf_help_1 from _call_ep5_milf_help_1


        "Уборка в комнате 2 ур" if help_ep5_milf >= 1:


            $ show_text_animation('+10 milf')

            $ renpy.music.stop(fadeout=.5)

            $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)

            call ep5_milf_help_2 from _call_ep5_milf_help_2

        "Уборка в комнате 3 ур" if help_ep5_milf >= 2:
            $ show_text_animation('+10 milf')


            $ renpy.music.stop(fadeout=.5)

            $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)

            call ep5_milf_help_3 from _call_ep5_milf_help_3

        "!Уборка в комнате 2 ур" if help_ep5_milf < 1:
            $ pass
        "!Уборка в комнате 3 ур" if help_ep5_milf < 2:
            $ pass

        "Назад" if True:

            return
label ep5_milf_help_end:





    $ time.time_now = 'evening'

    scene expression '#000' with Dissolve(.5)

    return












label ep5_milf_help_1:


    call show_bg_image_label from _call_show_bg_image_label_71
    with Dissolve(.5)


    show GG Normal
    show GG Normal:

        xalign .1
        ypos 1085
        zoom 1.0-0.035
    show Milf Losi_Normal
    show Milf Losi_Normal:

        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with my_dissolve



    "[gg]" "Ты столь усердно трудишься в раскорячку, что твоя спина наверняка уже затекла. "

    "Марина" "Ты чертовски прав…"

    "[gg]" "Так почему же тебе не обратиться к профессиональному массажисту, а? А?!"


    "Марина" "Извини, у меня нет времени на походы в массажный салон."

    "[gg]" "Эй, я предлагаю себя!"


    "Марина" "Оу… Конечно, милый. "


    "Марина" "Моя спина в твоём распоряжении. "

    scene expression 'cg/ep5/mass/bg.png'
    show ep5_milf_help_anim_1
    with Dissolve(.5)




    "Марина" "Вот тут, да…."




    "Марина" "Охх… Прекрасно, просто прекрасно."


    "Марина" "Только сейчас я понимаю, как сильно я устала."


    "Марина" "Продолжай, не останавливайся."


    "Марина" "У тебя волшебные пальчики. "


    "Марина" "Это лучший перерыв в моей жизни. "


    "Марина" "Ты такой сильный, нежный и чувственный."


    "Марина" "Я просто таю в твоих руках…"


    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/4.png'
    with Dissolve(.5)

    "[gg]" "О…."

    "[gg]" "Кажется, ты вспотела."


    "Марина" "Просто жарко…"





    menu:
        "Стянуть лямку" if True:
            $ pass
        "Уйти" if True:
            jump ep5_milf_help_1_end
























    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/5.png'
    with Dissolve(.5)


    "Марина" "Ты что делаешь?"

    "[gg]" "Извини, я случайно."


    "Марина" "Всё в порядке, я не обижаюсь. "


    "Марина" "Будь аккуратнее в следующий раз."

    "[gg]" "Значит, до следующего раза?"


    "Марина" "Наверное…"




label ep5_milf_help_1_end:
    scene expression '#000' with Dissolve(.5)
    call show_bg_image_label from _call_show_bg_image_label_72
    with Dissolve(.5)


    show GG Normal
    show GG Normal:

        xalign .1
        ypos 1085
        zoom 1.0-0.035
    show Milf Losi_Normal
    show Milf Losi_Normal:

        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with my_dissolve


    "Марина" "Спасибо за массаж, [gg]. Ты был прекрасен. "

    "[gg]" "Всё для тебя. "


    return



















label ep5_milf_help_2:


    call show_bg_image_label from _call_show_bg_image_label_73
    with Dissolve(.5)


    show GG Normal
    show GG Normal:

        xalign .1
        ypos 1085
        zoom 1.0-0.035
    show Milf Losi_Normal
    show Milf Losi_Normal:

        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with my_dissolve

    "[gg]" "Ты столь усердно трудишься в раскорячку, что твоя спина наверняка уже затекла. "

    "Марина" "Ты чертовски прав…"

    "[gg]" "Так почему же тебе не обратиться к профессиональному массажисту, а? А?!"


    "Марина" "Извини, у меня нет времени на походы в массажный салон."

    "[gg]" "Эй, я предлагаю себя!"


    "Марина" "Оу… Конечно, милый. "


    "Марина" "Моя спина в твоём распоряжении. "



    scene expression 'cg/ep5/mass/bg.png'
    show ep5_milf_help_anim_1
    with Dissolve(.5)



    "Марина" "Вот тут, да…."




    "Марина" "Охх… Прекрасно, просто прекрасно."


    "Марина" "Только сейчас я понимаю, как сильно я устала."


    "Марина" "Продолжай, не останавливайся."


    "Марина" "У тебя волшебные пальчики. "


    "Марина" "Это лучший перерыв в моей жизни. "


    "Марина" "Ты такой сильный, нежный и чувственный."


    "Марина" "Я просто таю в твоих руках…"


    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/4.png'
    with Dissolve(.5)

    "[gg]" "О…."

    "[gg]" "Кажется, ты вспотела."


    "Марина" "Просто жарко…"




    menu:
        "Стянуть лямку" if True:
            $ pass
        "Уйти" if True:
            jump ep5_milf_help_1_end






















    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/5.png'
    with Dissolve(.5)








    "Марина" "Ты… снова это сделал."

    "[gg]" "Да, но понимаешь, эта лямка сильно мешает массажировать твои плечевые суставы."


    "Марина" "Хм…"

    "[gg]" "Я всякий раз задеваю их руками."


    "Марина" "Наверное ты прав. "


    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/7.png'
    with Dissolve(.5)



    "Марина" "Тогда мне следует снять и вторую. "

    "[gg]" "Д-даа… Стоило бы."


    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/8ref.png'
    with Dissolve(.5)



    "Марина" "Теперь ты можешь продолжать?"

    "[gg]" "Ещё бы!!!..."


    "Марина" "…?"

    "[gg]" "Ну, то есть, да, разумеется могу."



    scene expression 'cg/ep5/mass/bg.png'
    show ep5_milf_help_anim_2
    with Dissolve(.5)

    "Марина" "Святые Небеса, так намного лучше. "


    "Марина" "Ты знаешь, что нужно делать, чтобы я чувствовала себя по настоящему отдохнувшей. "


    "Марина" "Каждое движение твоих рук отзывается приятным импульсом в спине."


    "Марина" "Фантастика…"


    "Марина" "Ммммм, как хорошо. Как усыпляюще. "


    "Марина" "Мой позвоночник ещё никогда не испытывал такого удовольствия от массажа. "























    menu:
        "Спуститься ниже" if True:
            $ pass
        "Уйти" if True:
            jump ep5_milf_help_1_end






    "Марина" "…?"

    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/8re2.png'
    with my_dissolve




    "Марина" "Это уже не спина."

    "[gg]" "Я знаю-знаю, но это же комплексный массаж. "




    "Марина" "Знаешь, я как-то не готова для «такого» комплекса. "


    "Марина" "Пожалуй, оставим это на другой раз. "

    "[gg]" "Значит, мы продолжим этот сеанс?"


    "Марина" "Наверное, но старайся придерживаться только области моей шейного позвонка и плечевых сустава. "

    "[gg]" "Хорошо…"

    jump ep5_milf_help_1_end








label ep5_milf_help_3:


    call show_bg_image_label from _call_show_bg_image_label_74
    with Dissolve(.5)


    show GG Normal
    show GG Normal:

        xalign .1
        ypos 1085
        zoom 1.0-0.035
    show Milf Losi_Normal
    show Milf Losi_Normal:

        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with my_dissolve


    "[gg]" "Ты столь усердно трудишься в раскорячку, что твоя спина наверняка уже затекла. "

    "Марина" "Ты чертовски прав…"

    "[gg]" "Так почему же тебе не обратиться к профессиональному массажисту, а? А?!"


    "Марина" "Извини, у меня нет времени на походы в массажный салон."

    "[gg]" "Эй, я предлагаю себя!"


    "Марина" "Оу… Конечно, милый. "


    "Марина" "Моя спина в твоём распоряжении. "




    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/1.png'
    with Dissolve(.5)




    "Марина" "Вот тут, да…."




    "Марина" "Охх… Прекрасно, просто прекрасно."


    "Марина" "Только сейчас я понимаю, как сильно я устала."


    "Марина" "Продолжай, не останавливайся."


    "Марина" "У тебя волшебные пальчики. "


    "Марина" "Это лучший перерыв в моей жизни. "


    "Марина" "Ты такой сильный, нежный и чувственный."


    "Марина" "Я просто таю в твоих руках…"



    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/4.png'
    with Dissolve(.5)

    "[gg]" "О…."

    "[gg]" "Кажется, ты вспотела."


    "Марина" "Просто жарко…"




    menu:
        "Стянуть лямку" if True:
            $ pass
        "Уйти" if True:
            jump ep5_milf_help_1_end






















    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/5.png'
    with Dissolve(.5)





















    "Марина" "Ты… снова это сделал."

    "[gg]" "Да, но понимаешь, эта лямка сильно мешает массажировать твои плечевые суставы."


    "Марина" "Хм…"

    "[gg]" "Я всякий раз задеваю их руками."


    "Марина" "Наверное ты прав. "



    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/7.png'
    with Dissolve(.5)



    "Марина" "Тогда мне следует снять и вторую. "

    "[gg]" "Д-даа… Стоило бы."




    "Марина" "Теперь ты можешь продолжать?"

    "[gg]" "Ещё бы!!!..."


    "Марина" "…?"

    "[gg]" "Ну, то есть, да, разумеется могу."



    scene expression 'cg/ep5/mass/bg.png'
    show ep5_milf_help_anim_2
    with Dissolve(.5)



    "Марина" "Святые Небеса, так намного лучше. "


    "Марина" "Ты знаешь, что нужно делать, чтобы я чувствовала себя по настоящему отдохнувшей. "


    "Марина" "Каждое движение твоих рук отзывается приятным импульсом в спине."


    "Марина" "Фантастика…"


    "Марина" "Ммммм, как хорошо. Как усыпляюще. "


    "Марина" "Мой позвоночник ещё никогда не испытывал такого удовольствия от массажа. "









    menu:
        "Спуститься ниже" if True:
            $ pass
        "Уйти" if True:
            jump ep5_milf_help_1_end












    "Марина" "…?"

    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/8re2.png'
    with my_dissolve



    "Марина" "Разве мы не обсуждали это в предыдущий раз? "



    "[gg]" "Да, но если ты будешь избирательной в том, какие области тела я буду массировать, а какие нет, то от массажа не случится должного эффекта. "


    "Марина" "Хочешь сказать, что только так я смогу ощутить весь спектр удовольствия от процесса?"

    "[gg]" "Вот видишь, ты сама это прекрасно понимаешь."



    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/anim_3/1.png'
    with Dissolve(.5)




    "Марина" "Надеюсь, я об этом не пожалею…"

    scene expression 'cg/ep5/mass/bg.png'
    show ep5_milf_help_anim_3
    with Dissolve(.5)









    "Марина" "Мммммм…."


    "Марина" "Восхитительно…"


    "Марина" "И всё таки ты прав."



    "Марина" "Сейчас этот массаж кажется мне куда более содержательным, чем может показаться на первый взгляд. "


    "Марина" "Моё тело словно под гипнозом."

    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/16.png'
    with Dissolve(.5)

    $ renpy.pause(9999)


    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/17.png'
    with Dissolve(.5)

    $ renpy.pause(9999)

    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/18.png'
    with Dissolve(.5)




    "Марина" "Почему ты остановился?.."

    "[gg]" "Ой. Извини."

    "[gg]" "Просто задумался."


    "Марина" "Продолжай, пожалуйста. "








    menu:
        "Массировать груди" if True:
            $ pass
        "Уйти" if True:
            jump ep5_milf_help_1_end




    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/20_Start.png'
    with Dissolve(.5)







    "Марина" "Это что, тоже часть твоего всеобъемлющего массажа?"

    "[gg]" "Если ты продолжишь спорить и упираться, я никогда не доведу процедуру, какой она задумывалась изначально."

    scene expression 'cg/ep5/mass/bg.png'
    show ep5_milf_help_anim_4
    with my_dissolve

    "Марина" "Охх…."


    "Марина" "Сейчас я не в том состоянии, чтобы сопротивляться."


    "Марина" "Но знай, мне кажется это крайне подозрительным."


    "Марина" "В конце-концов, это моя грудь, а не спина. "



    "[gg]" "Моя задача привести в порядок всё твоё тело, а не только область позвоночника. "


    "Марина" "Оу…"


    "Марина" "Едва ли кто-то со стороны поверил бы в этом, видя как ты жадно массируешь мою грудь. "

    "[gg]" "Но ты же веришь мне?"


    "Марина" "Ну…"


    "Марина" "Скорее, мне просто не хочется в тебе разочаровываться."


    "Марина" "{i}Или признаваться себе в том, что я испытываю сексуальное влечение к своему другу.{/i}"




    "Марина" "Ахх…."


    "Марина" "Кажется…."


    "Марина" "Мне кажется, этот массаж я давно заслужила."

    scene expression 'cg/ep5/mass/bg.png'
    show expression 'cg/ep5/mass/21_End.png'
    with my_dissolve



    "[gg]" "Я рад, что тебе нравится."


    "Марина" "Я ценю твои старания. "
    $ add_ach('ACH_6')

    #python:
    #    achievement.grant("ACH_6")
    #    achievement.sync()


    jump ep5_milf_help_1_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
