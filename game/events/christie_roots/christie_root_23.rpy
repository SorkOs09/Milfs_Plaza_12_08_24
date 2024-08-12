label christie_root_23:



    $ events.pop('christie_root_23', 0)
    call show_bg_image_label from _call_show_bg_image_label_99

    call show_additional_images_label from _call_show_additional_images_label_84

    show Igor Normal
    show Igor Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Angry
    show GG Angry at go_from_left

    "[gg]" "Ты это специально?!"
    show Igor Normal
    "Igor" "Не понимаю, о чём ты."
    show GG Angry:
        xalign .15
    with my_dissolve
    "[gg]" "Замок в комнате Кристи, который ты ЯКОБЫ починил, на самом деле поставил новый, который я не могу взломать. "
    show Igor Ok
    "Igor" "Разве тебя не учили, что личная жизнь человека конфиденциальна и нарушение её карается законом?"
    show GG Skepticism
    "[gg]" "Лучше скажи, как побороть твой механизм, «товарищ Майор»! "
    show Igor Troll
    "Igor" "Ну вот, я же говорил, что рано или поздно ты обратишься ко мне за помощью, хе-хе."
    show GG Angry
    "[gg]" "Это не просьба, а требование! "
    show Igor Angry
    "Igor" "Ээээ!"
    show Igor Angry
    "Igor" "Сейчас ты ведёшь себя как полный мудак, [gg]."
    show GG Chagrin
    "[gg]" "…."
    show Igor Angry
    "Igor" "Если помнишь, я помог не тебе, а Кристи. Это во-первых."
    show Igor Angry
    "Igor" "А если тебе нужна помощь с тем, чтобы проникнуть в её комнату, значит, и просить должен с подобающим уважением к другу. Это, во-вторых. "
    show GG Skepticism
    "[gg]" "А в третьих? "
    show Igor Angry
    "Igor" "…."
    show GG Skepticism
    "[gg]" "….."
    show Igor Silence
    "Igor" "Как тебе фотка её задницы?"
    show GG Smile
    "[gg]" "Шикарная."
    show Igor Silence
    "Igor" "Хе-хе-хе. Дааа, она клёвая. "
    show Igor Silence
    "Igor" "И ты ещё удивляешься тому, что я не смог устоять перед тем, чтобы не сфотографировать её. "
    show Igor Troll
    "Igor" "Никто бы не устоял!"
    show GG Skepticism
    "[gg]" "Верю, дружище, верю, но как на счёт замка?"
    show Igor Normal
    "Igor" "О, там элементарная комбинация. "
    show Igor Normal
    "Igor" "Способ я скину тебе на телефон, но сперва хочу знать, что благодарность не заставит себя ждать."
    show GG Skepticism
    "[gg]" "И что ты хочешь?"
    show Igor Normal
    "Igor" "Как говорил мой покойной отец «Бери ношу по себе, чтоб не падать при ходьбе»."
    show GG Skepticism
    "[gg]" "Ну и?"
    show Igor Normal
    "Igor" "Новой фоточки Кристи в нижнем белье или без мне было бы достаточно."
    show GG Normal
    "[gg]" "А если она узнает?"
    show Igor Troll
    "Igor" "Оооооооо!"
    show Igor Troll
    "Igor" "А если она узнает, что ты проник в её комнату? "
    show GG Embarrassment
    "[gg]" "….."
    show Igor Troll
    "Igor" "Не строй из себя праведника, [gg], мы потому и дружим, что стоим друг друга."
    show GG Normal
    "[gg]" "Хорошо, я согласен."
    show Igor Normal
    "Igor" "И ещё одно."
    show GG Normal
    "[gg]" "Да?"
    show Igor Bad
    "Igor" "Ты столько раз посещал меня, но ни разу, сука, ни разу не принёс мне пожрать!"
    show Igor Bad
    "Igor" "А я тут, знаешь ли, не на пляже прохлаждаюсь."
    show GG Chagrin
    "[gg]" "Извините, дружище. Моё упущение. В следующий раз так и сделаю."
    show Igor Normal
    "Igor" "Ага. Мы оба знаем, что этого никогда не случится"
    show GG Normal
    "[gg]" "Зачем же тогда просишь? "
    show Igor Normal
    "Igor" "Пытаюсь достучаться до твоего сердца, ебучий ты железный дровосек!"
    show GG Normal
    "[gg]" "До встречи, Буратино. "

    hide Igor
    with Dissolve(.5)
    show GG Think:
        ease 1 xalign .5

    "[gg]" "{i}Игорь скинул принцип взлома замка мне на телефоне.{/i}"

    "[gg]" "{i}Дело за малым, дождаться ночи и попробовать отпереть дверь.{/i}"



    call christie_root_try_to_del_descript_christie_block_igor from _call_christie_root_try_to_del_descript_christie_block_igor_9
    


    $ Event('christie_root_24b', 'Sister_Room', time = 'night', priority = -1)
    $ unlock_city_library = True
    $ events.pop('christie_root_21', 0)
    $ events.pop('christie_root_23_block', 0)
    $ Event('christie_root_24', 'City_Library_BiblioGirl', button_name = _("Реферат"), time = ['morning', 'afternoon'], priority = -1)

    $ descript_Christie_tmp_0 = __("1. Отправиться в библиотеку и продолжить написание реферата по теме «Обществознание» (1/3).")
    $ descript_Christie_tmp_1 = __("2. Ночью, пока все спят, взломать дверь Кристи.")
    $ descript_Christie       = str(descript_Christie_tmp_0) + "\n" + str(descript_Christie_tmp_1)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
