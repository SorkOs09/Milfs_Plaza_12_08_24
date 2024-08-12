label christie_root_try_to_del_descript_christie_block_igor:
    python:
        try:
            del descript_Christie_block_igor
        except:
            pass
    return
label christie_root_1:
    $ events.pop('christie_root_1', 0)
    call show_bg_image_label from _call_show_bg_image_label_108
    call show_additional_images_label from _call_show_additional_images_label_90

    show Christie Normal
    show Christie Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left





    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/sunny-morning-by-musiclfiles-from-filmmusic-io.mp3', fadein = 1.5)

    "[gg]" "Кристи…"
    show Christie Chagrin
    show GG:
        xalign .15
    with my_dissolve
    "Кристи" "Нет."
    show GG Surprise
    "[gg]" "Я ведь ещё ничего не сказал."
    show Christie Chagrin
    "Кристи" "Мы оба знаем, к чему ты ведёшь, [gg]."
    show GG Smile
    "[gg]" "С каких пор ты стала телепатом?"
    show Christie Angry
    with my_vpunch
    "Кристи" "С тех самых пор, как ты стал барыжить наркотиками, увлекаться азартными играми и обчищать мои заначки по всей квартире."
    show Christie Angry
    "Кристи" "Нет, я не дам тебе денег."
    show GG Chagrin
    "[gg]" "Я здесь не за этим."
    show Christie Skepticism
    "Кристи" "Да ну?"
    show GG Smile
    "[gg]" "Ладно... Ты меня прочла. Но не только за этим!"
    show Christie Angry
    "Кристи" "У тебя десять секунд, прежде чем я пну тебя по яйцам."
    show GG Normal
    "[gg]" "Ты не поверишь, но я твёрдо решил завязать с криминалом. "
    show Christie Normal
    "Кристи" "Ты угадал, я не верю."
    show GG Normal
    "[gg]" "Эх…"
    show GG Angry
    "[gg]" "Но если я не получу от тебя хотя бы каплю сочувствия, как по твоему, я должен взять себя в руки?!"
    show Christie Smile
    "Кристи" "Ха-ха-ха!"
    show Christie Smile
    "Кристи" "И что послужило поводом? Тюрьма на горизонте? "
    show GG Normal
    "[gg]" "Ты опережаешь мои слова."
    show Christie Smile
    "Кристи" "Я опережаю тебя в развитии, парень. О чём ты думал, когда брался за всё это дерьмо?"
    show GG Chagrin
    "[gg]" "Поздно копаться в причинах, когда задница уже наступила. "
    show GG Chagrin
    "[gg]" "Сейчас я хочу вернуться к нормальной жизни и знать, что люди, которым я не безразличен, смогут понять и простить."
    show Christie Skepticism
    "Кристи" "С чего ты решил, что ты мне не безразличен?!"
    show GG Surprise
    "[gg]" "Ауч…"
    show Christie Smile
    "Кристи" "Да шучу я, шучу. "
    show Christie Normal
    "Кристи" "Но я не могу вестись на твои щенячьи глаза, только потому, что ты, оказавшись в трудной ситуации, внезапно решил одуматься."
    show Christie Normal
    "Кристи" "Знаешь, всякий преступник, которого ловят на горячем, тоже жалеет о содеянном."
    show Christie Normal
    "Кристи" "Особенно тогда, когда осознаёт всю строгость предстоящего наказания."
    show Christie Normal
    "Кристи" "Но как только он выходит на свободу, начинает понимать, что ничего другого, кроме как убивать или красть, он не умеет, а потому, он принимает свою сущность и снова берётся за старое."
    show GG Angry
    "[gg]" "Я не такой!!."
    show Christie Skepticism
    "Кристи" "Да-да, так они и говорят. Обманывая себя и окружающих. "
    show GG Chagrin
    "[gg]" "…."
    show Christie Skepticism
    "Кристи" "И происходит от того, что никто из них не хочет над собой работать. Нельзя нажать в головке кнопку и переключиться с «Хайотичного-зла» на «Нейтрально-законного». "
    show GG Normal
    "[gg]" "И что ты предлагаешь? Сходить к психологу? Провести курс лечебной терапии? Переформатировать мозги? "
    show Christie Normal
    "Кристи" "Я ничего не предлагаю, [gg]. Это ты принял решение «измениться». Тебе и решать, как именно ты будешь это реализовывать."
    show Christie Normal
    "Кристи" "Я лишь хочу сказать тебе, что не верю в твою искренность. "
    show Christie Normal
    "Кристи" "Мне нужны доказательства, [gg] и очень серьёзные. "
    show GG Normal
    "[gg]" "Доказательства…"
    show Christie Normal
    "Кристи" "Да. Но ты всегда можешь послать меня, ведь я не требую от тебя перемен, и не лезу в твои дела. Ты сам ко мне явился. "
    show GG Normal
    "[gg]" "И ты права, Кристи. "
    show GG Normal
    "[gg]" "Мне действительно стоит обдумать это."
    show Christie Normal
    "Кристи" "Что ж, вот и замечательно. А пока ты думаешь, я, пожалуй, продолжу читать книгу. "
    show GG Normal
    "[gg]" "Да, конечно."
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/happy-days-in-summer-by-musiclfiles-from-filmmusic-io.mp3', fadein = 1.5)


    hide Christie
    with Dissolve(.5)
    show GG Think:
        ease .5 xalign .5
    "[gg]" "Кристи права, я должен переосмыслить своё отношение к жизни. "
    #show GG Think
    "[gg]" "И, конечно, нужно быть честным с самим собой."
    show GG:
        xalign .5
    with my_dissolve
    "[gg]" "Едва ли я смогу порвать с прошлым так быстро, как мне того хочется."
    #show GG Think
    "[gg]" "Если, вдруг, мне понадобятся деньги, куда я пойду? На завод? Нет, конечно. Я сыграю в карты, продам пару пакетиков отравы или стащу заначку Кристи."
    #show GG Think
    "[gg]" "Это «родовые» пятна моего прошлого? Или неотъемлемая часть меня?"
    #show GG Think
    "[gg]" "Если я действительно хочу перемен, я должен отмыться от этого дерьма."
    #show GG Think
    "[gg]" "И раз уж Кристи согласилась меня выслушать, то, наверное, она может дать подходящего совета…"
   # show GG Think
    "[gg]" "Но в следующий раз, не хочу её тревожить вновь."
    scene black with Dissolve(.5)
    $ location_now = 'Corridor'

    $ sister_position['morning'] = ['Kitchen', 'sister_kitchen']
    $ descript_Christie = _("Подобрать подходящее время для беседы. Поговорить с Кристи Утром на Кухне.")
    $ Event('christie_root_2', 'Christie', time = ['morning'])
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
