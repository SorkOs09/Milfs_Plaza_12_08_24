label christie_root_4:
    $ events.pop('christie_root_4', 0)

    $ events.pop('Обсудить психолога (Задание Кристи)', 0)


    $ events.pop(_('Обсудить психолога (Задание Кристи)'), 0)


    call show_bg_image_label from _call_show_bg_image_label_124

    call show_additional_images_label from _call_show_additional_images_label_98

    show Igor Normal
    show Igor Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_left

    "[gg]" "Здарова, бро."
    show Igor Normal
    "Игорь" "Здарова, коль не шутишь. "
    show GG Normal:
        xalign .15
    with my_dissolve
    "[gg]" "Понимаю, ты и без того изрядно нагружен, но у меня к тебе маленькая просьба не по делу…"
    show Igor Normal
    "Игорь" "Мог ли я ожидать чего-то другого? "
    show Igor Normal
    "Игорь" "Валяй уж, что там у тебя стряслось. "
    show GG Normal
    "[gg]" "Замок в двери, что в комнате Кристи, заедает. "
    show GG Think
    "[gg]" "Закрывается, но не открывается. Как думаешь, что с ним не так?"
    show GG Normal
    "[gg]" "Может, маслом смазать или ещё чего? "
    show Igor Troll
    "Игорь" "Кристи, говоришь?"
    show GG Normal
    "[gg]" "Я говорил про дверной замок."
    show Igor Troll
    "Игорь" "Нееет, меня не проведёшь. Ты определённо упомянул Кристи."
    show GG Normal
    "[gg]" "Ну да, речь о двери, ведущей в её комнату."
    show Igor Troll
    "Игорь" "Значит Кристи нужна моя помощь, верно? "
    show GG Angry
    "[gg]" "Нет, чувак, помощь нужна мне, ты помогаешь мне, а я тем самым помогу Кристи! Понятно?"
    show Igor Ok
    "Игорь" "Окееееей."
    show Igor Ok
    "Игорь" "Прежде чем понять, что не так с замком, я должен лично в этом убедиться. Сечёшь? "
    show GG Chagrin
    "[gg]" "Только без глупостей, Игорь. Кристи боится тебя. "
    show Igor Agr
    "Игорь" "Враньё. Оно меня обожает."
    show GG Please
    "[gg]" "Нет, чувак, она от тебя в ужасе. "
    #show GG Normal
    "[gg]" "После того как ты преследовал её в школьные годы, она до сих пор вздрагивает при упоминании твоего имени."
    show Igor Bad
    "Игорь" "Ты просто ревнуешь, вот и всё."
    show GG Normal
    "[gg]" "Оставайся в рамках приличия, и не вздумай вытворять какую-нибудь херню. "
    show GG Normal
    "[gg]" "Или я обращусь за помощью к кому-нибудь другому."
    show Igor Bad
    "Игорь" "Я уже распланировал нашу свадьбу, а ты хочешь этому помешать…"
    show GG Normal
    "[gg]" "Хватит бредить и просто сделай, что тебя просят. "
    show Igor Bad
    "Игорь" "Я сделаю это только ради Кристи."
    show GG Laughs
    "[gg]" "Замётано. Но без приколов! "
    show Igor Bad
    "Игорь" "Хорошо…"


    hide Igor
    show GG Think
    with my_dissolve
    "[gg]" "С Игорем я договорился. Теперь у меня есть время на поход к психологу."
    show GG Think
    "[gg]" "Судя по адресу, она живёт буквально в соседнем доме… удачно!"


    
    call christie_root_try_to_del_descript_christie_block_igor from _call_christie_root_try_to_del_descript_christie_block_igor_4
    


    $ descript_Christie = _("Утром или Днём сходить к психологу на приём.")
    $ time.time_now     = 'evening'
    $ unlock_city_psi   = True
    $ Event('christie_root_5', 'City_Psi', 'christie_root_5', time = ['morning', 'afternoon'])
    scene black with Dissolve(.5)


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
