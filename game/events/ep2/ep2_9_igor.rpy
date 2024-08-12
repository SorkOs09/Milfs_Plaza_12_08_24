
label ep2_9_igor:
    $ events.pop('ep2_9_igor', 0)
    call show_bg_image_label from _call_show_bg_image_label_30

    call show_additional_images_label from _call_show_additional_images_label_25

    show Igor Silence
    show Igor Silence:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_left

    '[gg]' "Привет, Игорь"
    show Igor Ok
    'Игорь' "Явился, не запылился. "
    show GG Angry:
        xalign .15
    '[gg]' "Что за наезды? Если ты не обратил внимания, мы оба в дерьме."
    show Igor Bad
    'Игорь' "Ну да, только пашу я сам. "
    '[gg]' "Ты сам выбрал эту участь. И где твои сломанные рёбра? "
    show Igor Troll
    'Игорь' "Нигде. Это была гипербола."
    show GG Angry
    '[gg]' "Хуербола, чувак. А мне, вот, нож к горлу приставляли без всяких преувеличений. "
    show Igor Angry
    'Игорь' "Меня тоже пнули, без шуток. И в следующий раз это может быть что-то посерьёзней. "
    show GG Normal
    '[gg]' "Именно поэтому я и хочу поговорить с тобой."
    show Igor Normal
    'Игорь' "И я, чувак. И я!"
    show GG Normal
    '[gg]' "Ты первый."
    show Igor Normal
    'Игорь' "Нет ты."
    show Igor Silence
    '[gg]' "…."
    show GG Passion
    '[gg]' "Если тебя убьют, я не стану по тебе скучать, чёртов зануда. "
    show Igor Troll
    'Игорь' "Аналогично."
    show GG Normal
    '[gg]' "Короче…."
    '[gg]' "После того случая ночью, я загорелся идеей свалить в другой город. На неделю или две."
    '[gg]' "Но…"
    show Igor Ok
    'Игорь' "Но понял, что тебе не на что будет жить это время; что вскоре тебя и так найдут; и что две недели – не тот срок, за который нам простили бы долг."
    show GG Smile
    '[gg]' "Хм… Почти. "
    show GG Chagrin
    '[gg]' "Я понял, что не могу бросить Марину. Я лишь недавно наладил с ней отношения и не хочу их разрушить вновь. К тому же, я давал слово брату, что позабочусь о ней."
    show Igor Ok
    show Officer Normal
    show Officer Normal:

        xalign 1.5
        ypos 1085
        zoom 1.0-0.035
    'Игорь' "А ещё, если бы ты свалил, то она была первой, кого трясли, чтобы выбить информацию о твоём местонахождении. "
    show GG Passion
    '[gg]' "Чёртов калькулятор, тебе мозг на череп не давит?"



    play music 'audio/game_start.mp3' fadein 1.5 

    show Officer Normal:
        xzoom -1
        easein_cubic 1 xalign .85
        ypos 1085
        zoom 1.0-0.035


    show GG Surprise:
        easein_cubic 1 xalign .1

    show Igor Angry:
        xzoom -1
        easein_cubic 1 xalign .32
    $ renpy.pause(1, hard = True)

    'Офицер' "Доброе утро, ребята."
    show Officer Normal:
        xzoom -1
        xalign .85
        ypos 1085
        zoom 1.0-0.035


    show GG Normal:
        xalign .1

    show Igor:
        xzoom -1
        xalign .32
    with my_dissolve
    '[gg]' "Здравствуйте, офицер."
    show Igor Normal
    'Игорь' "Здравие желаю! "
    show Officer Say

    'Офицер' "А я, вот, проходил мимо и решил, думаю, зайду проверю. Как там наш [gg] справляется с реабилитацией в глазах общества. "

    show GG Smile
    '[gg]' "Нормально, как видите."
    show Officer Angry

    'Офицер' "Тогда почему метлу держит твой приятель, а не ты?"

    show GG Laughs
    show Igor Angry
    '[gg]' "А я уже отработал. Вот, сдаю смену. "
    show Officer Hm

    'Офицер' "Понятненько. Ладно."

    show Officer Say

    'Офицер' "[gg], будь добр, зайди ко мне домой, как у тебя будет время. Я хотел поговорить с тобой. "

    show GG Normal
    '[gg]' "Как скажете…"
    show Officer Normal

    'Офицер' "Всего доброго, ребята."

    show Igor Troll
    'Игорь' "И вам не болеть."



    show Officer Angry:
        xzoom 1
        easein_cubic 1.1 xalign 1.5



    show GG Surprise:
        easein_cubic .9 xalign .32

    show Igor Angry:
        easein_cubic 1.1 xalign .85
        xzoom 1
    $ renpy.pause(1.1, hard = True)
    play music 'audio/day.mp3' fadein 1.5 
    'Игорь' "Вот мудак."
    hide Officer



    show GG Passion:
        xalign .32

    show Igor:
        xalign .85
        xzoom 1
    with my_dissolve

    '[gg]' "И не говори."
    show Igor Normal
    'Игорь' "Теперь слушай, что я тебе поведаю."
    'Игорь' "Деваться нам некуда, [gg]. Мы в жопе – это факт."
    show GG Normal
    '[gg]' "Факт."
    show Igor Normal
    'Игорь' "И денег за такой срок мы не достанем, даже если ограбим ювелирку – это тоже факт."
    show GG Normal
    '[gg]' "Факт!"
    show Igor Normal
    'Игорь' "И рано или поздно, а скорее всего очень скоро, к нам снова явятся люди Жлоба и будут выбивать из нас дерьмо. "
    show GG Normal
    '[gg]' "Факт!!"
    hide Igor




    show Igor Angry
    show Igor Angry:
        xalign .85
        ypos 1085
        zoom 1.0-0.035

    show GG Laughs
    'Игорь' "Заткнись, мать твою."
    show GG Silence
    '[gg]' "…."
    show Igor Normal
    'Игорь' "Нам ничего не остаётся, кроме как защитить себя. "
    show GG WTF
    '[gg]' "Ты меня пугаешь…"
    show Igor Normal
    show GG Surprise
    'Игорь' "Нам нужны стволы, чувак. Каждому по пушке. "
    'Игорь' "Так мы сможем защитить себя и родных."
    show GG WTF
    '[gg]' "А ты не боишься, что к нам тоже придут с пушками?"
    show Igor Angry
    'Игорь' "Я не для гангстерских разборок их хочу взять. Просто припугнуть. Чтобы избежать бесконечных наездов."
    show Igor Troll
    'Игорь' "Это не спасёт нас от долга и угроз Жлоба, но шпана к нам точно не полезет."
    show GG WTF
    '[gg]' "Не хотелось бы марать руки, но если другого выхода нет... Ты уже знаешь где купить оружие?"
    show Igor Normal
    'Игорь' "Да, у меня есть человек, который сможет нам достать пару хороших пушек. С тебя 150 баксов."
    show GG Surprise
    '[gg]' "Ого. Прямо сейчас?"
    show Igor Angry
    'Игорь' "Ебанутый что ли? Тут рядом фараон расхаживает. "
    show Igor Normal
    'Игорь' "Как будут деньги, перекинь мне на карту."
    show GG Normal
    '[gg]' "Окей. А как ты передашь мне ствол?"
    show Igor Normal
    'Игорь' "Напишу в смс."
    show GG Normal
    '[gg]' "Хорошо, удачи."
    show Igor Ok
    'Игорь' "Не болей."

    hide Igor

    show GG:
        linear 1 xalign .6
    $ renpy.pause(1, hard = True)
    show GG Think with Dissolve(.5)
    $ unlock_masturbation_together = True
    '[gg]' "У меня нет своей карты банка. Как только у меня будет 150 долларов, попрошу Марину перечислить деньги Игорю на карту."
    $ descript = _('Как только у меня будет 150 долларов, попросить Марину перечислить деньги Игорю.')

    $ help_ep3_milf_14 = 0

    $ Event('ep2_10_corridor',  'Corridor', time = ['morning',  'afternoon',  'evening'])









    $ location_now = 'City_Park'
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
