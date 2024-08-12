

label ep45_milf_49_05:

    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()
    $ Hide('main_interface')()
    scene black
    with Dissolve(.5)

    $ block_exit_home    = False

    $ block_time_forward = False
    $ block_change_milf_position = False
    $ descript = _("Выяснить у Кэт (Ночной гостьи), где именно удерживают Игоря. Для этого следует дождаться её ночью. ")
    $ help_ep3_milf_14 = 2
    $ unlock_masturbation_restroom = 2
    $ unlock_shower_together_3 = 1
    #$ unlock_film_1            = True
    $ new_events               = True

    $ add_ach('ACH_8')

    $ Event('night_girl',     'GG_Room',     'ep45_milf_49_1', day_start = time.day_now + 1, time = ['morning'])

    return

label ep45_milf_49_0:





    call ep45_milf_49_05 from _call_ep45_milf_49_05_1


    jump main_interface_label











label ep45_milf_49_1:
    scene expression 'images/cg/ep1/night_collector/Night_collector_2.png'
    with vpunch

    stop music fadeout 1.5
    play music 'audio/n_girl.mp3' fadein 1.5


    "Кэт" "Ха! Я думала, ты мёртв."


    "[gg]" "Если продолжишь сдавливать моё горло лезвием, так оно и будет. "


    "Кэт" "Хе-хе-хе. "
    scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
    with Dissolve(.5)


    "Кэт" "Ты зря тут разлёгся, дурень. "


    "Кэт" "За тобой вот-вот явятся."


    "[gg]" "Тогда что ты здесь делаешь? "
    scene expression 'images/cg/ep1/night_collector/Night_collector_5.png'
    with Dissolve(.5)


    "Кэт" "Понадеялась и соскучилась."


    "[gg]" "Оу…. Я, если честно, приятно удивлён."
    scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
    with Dissolve(.5)


    "Кэт" "Не мели чушь, придурок. "


    "Кэт" "Я соскучилась по деньгам."
    scene expression 'images/cg/ep1/night_collector/Night_collector_5.png'
    with Dissolve(.5)


    "[gg]" "Чего?!!"
    scene expression 'images/cg/ep1/night_collector/Night_collector_7.png'
    with Dissolve(.5)


    "Кэт" "Гони мои бабки! Живо!"


    "[gg]" "У тебя ни стыда, ни совести. "
















    menu:
        "Вот, возьми (отдать {i}{b}20{/b}{/i} баксов)." if money >= 20:
            $ money -= 20
            $ show_text_animation('-20 money')
        "!Вот, возьми (отдать {i}{b}20{/b}{/i} баксов)." if money <  20:
            $ pass
        "Это всё, что я могу дать (отдать {i}{b}[money]{/b}{/i} баксов)." if money > 0 and money < 20:
            $ show_text_animation('- ' + str(money)+' money')
            $ add_ach('ACH_13')
            $ money = 0
        "Извини, но у меня вообще ничего нет…" if True:
            with Dissolve(.5)


            scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
            with Dissolve(.5)

            "Кэт" "Голый король, где твои сокровища?"


            "[gg]" "Извини…"
            jump ep45_milf_49_2


    scene expression 'images/cg/ep1/night_collector/Night_collector_8.png'
    with Dissolve(.5)


    "Кэт" "Обожаю шелест купюр. "











label ep45_milf_49_2:
    scene expression 'images/cg/ep1/night_collector/Night_collector_11.png'
    with Dissolve(.5)


    "Кэт" "Ну ладно-ладно. За тобой я тоже чуточку соскучилась. "


    "[gg]" "И я…"


    "[gg]" "Знаешь, нам стоило бы узнать друг друга лучше."


    "[gg]" "Могли бы встретиться в более располагающей обстановке, выпить там, поболтать по душам…"


    "Кэт" "Ну, всё-всё. Не надо распускать нюни."


    "Кэт" "Ненавижу телячьи нежности. "


    "Кэт" "Спасибо, что живой. Я пошла."


    "[gg]" "….."


    "[gg]" "Постой, не уходи. Я хочу купить у тебя информацию."
    scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
    with Dissolve(.5)


    "Кэт" "Ха-ха-ха!"


    "Кэт" "Если ты планируешь выведать у меня какие-либо тайны о Жлобе, то даже не думай."
    scene expression 'images/cg/ep1/night_collector/Night_collector_7.png'
    with Dissolve(.5)


    "Кэт" "Я кто, по-твоему, камикадзе? "


    "[gg]" "Мне не нужен твой босс."


    "Кэт" "…А?"


    "[gg]" "Мне нужно узнать, где удерживают Игоря."
    scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
    with Dissolve(.5)


    "Кэт" "Чёрт, парень, это почти тоже самое! "


    "[gg]" "Сжалься, Кэт! Его могут убить!"


    "Кэт" "…."


    "Кэт" "Нет, это безумие."


    "[gg]" "Ну пожалуйста."


    "Кэт" "Отвали."


    "[gg]" "Умоляю!"


    "Кэт" "Не-а."


    "[gg]" "Ну Кэт! Ну очень прошу! Это вопрос жизни и смерти. "


    "Кэт" "Мне проще самой тебя убить, чем слушать это нескончаемое нытьё."


    "[gg]" "Я… Я сделаю для тебя всё что пожелаешь!"
    scene expression 'images/cg/ep1/night_collector/Night_collector_11.png'
    with Dissolve(.5)


    "Кэт" "О!.."


    "Кэт" "Всё что пожелаю?.."


    "[gg]" "Именно! "
    "Кэт" "Дай-ка уточнить. "
    "Кэт" "Абсолютно всё, что я попрошу, и каким бы безумным или вопиющим эта просьба тебе не казалась, ты исполнишь это?"
    '[gg]' "Ну…."
    '[gg]' "Я бы исключил из этого…."
    "Кэт" "Ну? Исключил?"
    "Кэт" "Если ты сомневаешься в собственной благонадёжности, то как ты предлагаешь мне рисковать своей жопой?"
    '[gg]' "Да, ты совершенно права. "
    '[gg]' "Я сделаю всё. Любую херню, что тебе взбредёт в голову."
    "Кэт" "Это именно то, что я хотела услышать."


    "Кэт" "Почему ты сразу с этого не начал?"


    "[gg]" "Понадеялся на твою доброту."


    "Кэт" "Ну ты и кретин."


    "[gg]" "…."


    "Кэт" "Не могу обещать, что у меня получится, но я попробую."


    "[gg]" "Я буду благодарен любой попытке!"


    "[gg]" "Просто знай, от твоей информации зависит жизнь человека."


    "Кэт" "Да знаю я, не грузи. "


    $ Event('night_girl',     'GG_Room',     'ep3_night_girl', day_start = time.day_now + 7, time = ['morning'])

    scene expression '#000' with Dissolve(.5)











    $ location_now  = 'GG_Room'
    $ time.time_now = 'morning'

    call show_all_images_label from _call_show_all_images_label_6
    with Dissolve(.5)
    show GG Think
    show GG Think:
        xalign .5
        ypos 1085
    with Dissolve(.5)
    "[gg]" "Пора действовать. "
    show GG Think
    "[gg]" "Я не могу позволить себе отлёживаться дома, дожидаясь возвращения Кэт. "
    show GG Think
    "[gg]" "Пока Игорь в плену, а на мне висит административное наказание в виде общественных работ, я должен лично отрабатывать предписание судьи. "
    show GG Think
    "[gg]" "Ещё этот полицейский…."
    show GG Think
    "[gg]" "После того, как я подарил его кулон Марине лично от себя, даже не сомневаюсь, он сделает всё возможное, чтобы насолить мне."

    show GG Think
    "[gg]" "Следует исключить такую возможность и регулярно появляться в парке, демонстрируя высший пилотаж по уборки листвы и мусора. "

    $ descript = _("Если я не хочу проблем с офицером полиции, мне следует убирать в Парке каждый день. ")

    $ Event('ep45_milf_50', 'Corridor')

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
