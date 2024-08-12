

image christie_root_26_anim_0 1:


    "christie_root_17_4_hand 1"
    .15
    "christie_root_17_4_hand 2"
    .15

    "christie_root_17_4_hand 3"
    .15

    "christie_root_17_4_hand 4"
    .15
    "christie_root_17_4_hand 5"
    .15
    "christie_root_17_4_hand 4"
    .15

    "christie_root_17_4_hand 3"
    .15

    "christie_root_17_4_hand 2"
    .15

    repeat


image christie_root_26_anim_0 2:


    "christie_root_17_4_hand 1"
    .1
    "christie_root_17_4_hand 2"
    .1

    "christie_root_17_4_hand 3"
    .1

    "christie_root_17_4_hand 4"
    .1
    "christie_root_17_4_hand 5"
    .1
    "christie_root_17_4_hand 4"
    .1

    "christie_root_17_4_hand 3"
    .1

    "christie_root_17_4_hand 2"
    .1

    repeat




image christie_root_26_anim_0 3:


    "christie_root_17_4_hand 1"
    .07
    "christie_root_17_4_hand 2"
    .07

    "christie_root_17_4_hand 3"
    .07

    "christie_root_17_4_hand 4"
    .07
    "christie_root_17_4_hand 5"
    .07

    "christie_root_17_4_hand 4"
    .07

    "christie_root_17_4_hand 3"
    .07

    "christie_root_17_4_hand 2"
    .07

    repeat

image christie_root_26_anim 1:


    "cg/christie_root/kristy_sit_8.png" with Dissolve(.1)
    .25

    "cg/christie_root/kristy_sit_9.png" with Dissolve(.1)
    .25

    "cg/christie_root/kristy_sit_10.png" with Dissolve(.1)
    .25

    "cg/christie_root/kristy_sit_11.png" with Dissolve(.1)
    .25

    "cg/christie_root/kristy_sit_12.png" with Dissolve(.1)
    .25

    "cg/christie_root/kristy_sit_11.png" with Dissolve(.1)
    .25

    "cg/christie_root/kristy_sit_10.png" with Dissolve(.1)
    .25

    "cg/christie_root/kristy_sit_9.png" with Dissolve(.1)
    .25

    repeat




image christie_root_26_anim 2:


    "cg/christie_root/kristy_sit_8.png" with Dissolve(.05)
    .12

    "cg/christie_root/kristy_sit_9.png" with Dissolve(.05)
    .12

    "cg/christie_root/kristy_sit_10.png" with Dissolve(.05)
    .12

    "cg/christie_root/kristy_sit_11.png" with Dissolve(.05)
    .12

    "cg/christie_root/kristy_sit_12.png" with Dissolve(.05)
    .12

    "cg/christie_root/kristy_sit_11.png" with Dissolve(.05)
    .12

    "cg/christie_root/kristy_sit_10.png" with Dissolve(.05)
    .12

    "cg/christie_root/kristy_sit_9.png" with Dissolve(.05)
    .12

    repeat



image christie_root_26_anim 3:


    "cg/christie_root/kristy_sit_8.png"
    .06

    "cg/christie_root/kristy_sit_9.png"
    .06

    "cg/christie_root/kristy_sit_10.png"
    .06

    "cg/christie_root/kristy_sit_11.png"
    .06

    "cg/christie_root/kristy_sit_12.png"
    .06

    "cg/christie_root/kristy_sit_11.png"
    .06

    "cg/christie_root/kristy_sit_10.png"
    .06

    "cg/christie_root/kristy_sit_9.png"
    .06

    repeat
label christie_root_26:


    if not from_gallery_check():
        $ events.pop('christie_root_26', 0)

        $ remove_from_inventory(name = 'Реферат «Обществознание» 3/3')
    elif True:
        scene expression 'locations/bg/Hall/morning.png'
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    python:
        if not from_gallery_check():
            
            block_milf_home = copy.deepcopy(christie_root_25_block_milf_home)
            
            try:
                del christie_root_25_block_milf_home
            except:
                pass



    show Christie Normal
    show Christie Normal:
        xalign .85
    with my_dissolve


    show GG Normal
    show GG Normal at go_from_left






    "[gg]" "А вот и я!"
    show GG Normal:
        xalign .15
    with my_dissolve
    "[gg]" "С целой кипой бумаг и авторским текстом."
    show Christie Surprise
    "Кристи" "Ты что, всё это время провёл за написанием реферата?!"
    show GG Embarrassment
    "[gg]" "Ага."
    show Christie Surprise
    "Кристи" "Ты волшебник!!!"
    show GG Laughs
    "[gg]" "Первый курс Хогвартса, как никак."
    show Christie Smile
    "Кристи" "Какой же ты классный, [gg]!"
    show Christie Laughs
    "Кристи" "Ты снова спас меня!!"
    show Christie Chagrin
    "Кристи" "Даже и не знаю, как тебя отблагодарить. "
    show GG Smile
    "[gg]" "О, оставь. Я сделал это от чистого сердца."
    show Christie Embarrassment
    "Кристи" "Ах…"
    show Christie Laughs
    "Кристи" "Ну же, не стой столбом, садись, рассказывай, как тебе удалось так быстро справиться?!"

    scene expression 'cg/christie_root/kristy_sit_1.png' with my_dissolve


    "[gg]" "Профессионал никогда не раскрывает своих тайн."
    "Кристи" "Ну ты и зануда. "
    "[gg]" "Учусь у лучших, хе-хе-хе."


    "Кристи" "Если честно, сейчас мне очень стыдно, что я обрушила на тебя столько работы сразу."
    "[gg]" "Звучит так, словно речь идёт лишь об объёме. "


    "Кристи" "Ха-ха-ха!"
    "Кристи" "Ну да, я не прочь свесить ноги на чью-то шею, особенно, если это очень крепкая и обаятельная шея. "
    "[gg]" "Ты первая, кто делает комплимент моей шее."
    "Кристи" "Ха-ха-ха!"
    "Кристи" "Цени это."


    "[gg]" "А как же мои руки?"
    "[gg]" "Разве они не достойны восторженных отзывов после стольких сеансов массажа? "
    "Кристи" "Оуууу!"
    "Кристи" "Да, у тебя животворящие пальчики. Я их просто обожаю."
    "[gg]" "Приятно слышать."
    "[gg]" "Если хочешь, я сделаю тебе массаж."


    scene expression 'cg/christie_root/kristy_sit_5.png' with my_dissolve

    "Кристи" "…."
    "Кристи" "Я так часто прошу тебя об этом, не говоря уж о том, что ты и так очень много делаешь для меня, от чего испытываю жуткое чувство стыда."
    "[gg]" "В данном случае, это моя собственная инициатива. "
    "Кристи" "Д-даа…"
    "Кристи" "Понимаю."


    scene expression 'cg/christie_root/kristy_sit_6.png' with my_dissolve
    "Кристи" "И не собираюсь отказываться, ха-ха-ха."


    "Кристи" "Мои ножки в твоём полном распоряжении. "



    scene expression 'cg/christie_root/kristy_sit_3.png'
    with my_dissolve
    "[gg]" "У тебя очень приятная кожа. "
    "Кристи" "С-спасибо…"
    "[gg]" "Такая тёплая, гладкая. Мне очень нравится тебя касаться."
    "Кристи" "Ты загоняешь меня в краску."
    "[gg]" "Просто говорю правду. "
    "[gg]" "Ты очень красивая и мне повезло, что именно удостоилось право трогать твои ножки."
    "Кристи" "[gg]… Ты слишком мил со мной."

    scene christie_root_17_4_anim_bg
    show christie_root_17_2_face 1
    show christie_root_17_4_anim 1
    show christie_root_17_4_anim_fg

    with my_dissolve
    "[gg]" "А ты слишком привлекательная. "
    "Кристи" "Хи-хи-хи."
    "Кристи" "Ты говоришь это из лести, потому что мы друзья."
    "[gg]" "Или потому, что испытываю влечение к тебе…"
    "Кристи" "Мне кажется, это не совсем нормально."
    "[gg]" "Массаж?"
    "Кристи" "Ты знаешь о чём я."
    "[gg]" "…."

    scene christie_root_17_4_anim_bg
    show christie_root_17_2_face 1

    show christie_root_26_anim_0 1
    show christie_root_17_4_anim_fg

    with my_dissolve
    "[gg]" "Ты об этом, верно?"
    "Кристи" "Мммммм….."
    "Кристи" "И об этом тоже, [gg]."
    "Кристи" "Ты ведь понимаешь, что нам нельзя этого делать?"

    menu:
        "Ускориться" if True:
            $ pass

    show christie_root_26_anim_0 2
    with my_dissolve
    "[gg]" "Тебя пугают последствия?"
    "Кристи" "А тебя нет?"
    "[gg]" "Не знаю."
    "[gg]" "Сейчас я думаю только о тебе."
    "Кристи" "Ааххххх…."
    "Кристи" "Я вижу… И чувствую…."
    "[gg]" "Всякий раз, когда ты рядом, я с трудом контролирую своё поведение."

    menu:
        "Ускориться" if True:
            $ pass

    show christie_root_26_anim_0 3
    with my_dissolve
    "[gg]" "Я понимаю цену ответственности своих действий."
    "[gg]" "И в данный момент я искренне пытаюсь разобраться в своих чувствах к тебе."
    "Кристи" "И что будет, когда ты разберёшься?"
    "[gg]" "Я решусь на следующий шаг."
    "Кристи" "Следующий шаг?"

    "[gg]" "Да."
    scene black with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    scene expression "cg/christie_root/kristy_sit_8.png"
    with my_dissolve
    "Кристи" "О боже…."
    "Кристи" "[gg], пожалуйста, Марина дома!"
    "[gg]" "Знаю."
    "Кристи" "Марина убьёт нас, если увидит всё это!"
    "[gg]" "Знаю."


    scene christie_root_26_anim 1
    with my_dissolve
    "Кристи" "Тогда зачем же ты продолжаешь, безумец?!"
    "[gg]" "Затем же, зачем ты позволяешь мне это делать."
    "Кристи" "Ммммм…."
    "Кристи" "Ооооох…."
    "Кристи" "Как же приятно…."
    "Кристи" "Но…."
    "[gg]" "Разве могут быть сейчас какие-то «но»?"
    "Кристи" "Нет, мы не можем продолжать."
    "Кристи" "Я ещё не готова к этому. "
    "Кристи" "У нас будут проблемы."
    "[gg]" "Значит, мы решим её вместе."
    "Кристи" "Ты не понимаешь, что говоришь."
    "Кристи" "Твой рассудок замутнён неумолимой похотью. "
    "[gg]" "Как и твой, я полагаю."



    menu:
        "Ускориться" if True:
            $ pass
    scene christie_root_26_anim 2
    with my_dissolve
    "Кристи" "Уффффф…."
    "Кристи" "Да, но я стараюсь противиться этому."
    "[gg]" "Зачем? Наши действия естественная реакция друг на друга. "
    "Кристи" "Нет, ты пытался меня совратить, это слишком вульгарно."
    "Кристи" "Слишком пошло…"
    "Кристи" "Слишком извращённо для моего представления о любви."
    "[gg]" "Но ты ведь хочешь, меня, правда?"
    "Кристи" "Аххх…. Ахххххх…."
    "Кристи" "Я не стану тебе отвечать сейчас."
    "Кристи" "Мой ответ должен быть взвешенным, а не под напором сексуального давления. "
    "[gg]" "Разве этот напор не следствие наших чувств?"
    "Кристи" "Ооооохххх!..."
    "Кристи" "Не дави на меня. "
    "Кристи" "Точнее, дави, но не на меня…."

    menu:
        "Ускориться" if True:
            $ pass
    scene christie_root_26_anim 3
    with my_dissolve
    "Кристи" "О даааа, ещё…. "
    "Кристи" "Продолжай, пожалуйста…"
    "Кристи" "Я уже почти…."
    "Кристи" "Давай-давай, вот тут, да..."
    "Кристи" "Уххх, как приятно. Как это восхитительно. "
    "[gg]" "Ты дрожишь от удовольствия. "
    "Кристи" "Да, я наслаждаюсь."
    "[gg]" "У тебя там так влажно и горячо."
    "Кристи" "Пожалуйста, не будь таким вульгарным. Я стесняюсь."
    "[gg]" "Ты стыдишься своих действий."
    "Кристи" "Это съедает меня изнутри."
    "[gg]" "Я хочу, чтобы ты кончила."
    "Кристи" "Ахххх…. "
    "Кристи" "Да… Я уже на грани."
    "Кристи" "Я…"
    "[gg]" "Я чувствую, как ты кончаешь."
    "Кристи" "Да-да-да!!!"
    "Кристи" "Я кончааааааююююю!!!!"

    menu:
        "Кончить" if True:
            pass

    $ renpy.pause(.5, hard = True)
    scene white with Dissolve(1.5)

    $ renpy.pause(2, hard = True)

    scene expression 'cg/christie_root/kristy_sit_end.png'
    with Dissolve(.5)

    $ renpy.pause(1, hard = True)
    "Кристи" "Боже…"
    "Кристи" "Это было так пошло."
    "[gg]" "И прекрасно."
    "Кристи" "Боюсь соглашаться."
    "[gg]" "Тогда просто наслаждайся моментом."


    scene black with Dissolve(1)

    $ renpy.pause(1.5, hard = True)

    $ location_now = 'Hall'
    $ add_to_gallery(26)
    call show_bg_image_label from _call_show_bg_image_label_132


    show Christie Embarrassment
    show Christie Embarrassment:
        xalign .85
        ypos 1085


    show GG Embarrassment
    show GG Embarrassment:
        xalign .15
        ypos 1085
    with Dissolve(.5)

    "Кристи" "Мы зашли слишком далеко."
    show GG Smile
    "[gg]" "Знаю."
    show GG Smile
    "[gg]" "Но тебе ведь понравилось, правда?"
    show Christie Embarrassment
    "Кристи" "…."
    show Christie Embarrassment
    "Кристи" "Извини, я должна идти."
    show Christie Embarrassment
    "Кристи" "Мне нужно всё хорошо обдумать."
    show GG Embarrassment
    "[gg]" "Конечно."

    scene black with Dissolve(.5)
    call check_gallery_label from _call_check_gallery_label_15
    $ renpy.pause(.5, hard = True)
    $ time.time_now = 'evening'


    $ remove_from_inventory(name = 'Реферат')





    $ christie_root_26_end = True
    $ descript_Christie= _("Конец рута Кристи для эпизода [version_now]")

    call christie_root_27_activate from _call_christie_root_27_activate

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
