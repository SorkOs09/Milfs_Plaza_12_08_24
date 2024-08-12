label christie_root_6:
    $ events.pop('christie_root_6', 0)

    scene black with Dissolve(.5)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/lo-fi-hip-hop-02-by-winniethemoog-from-filmmusic-io.mp3', fadein = 1.5)
    $ renpy.pause(.5)

    scene expression 'cg/christie_root/kristy_sit_1.png' with Dissolve(.5)

    "Кристи" "Эй, разве ты не видишь? Я занята. "
    "[gg]" "А я думал тебе интересно послушать про мой первый сеанс у мозгоправа."
    "Кристи" "Беру свои слова назад! Выкладывай всё как есть."
    "[gg]" "Ну… Это была умная беседа двух умных людей."
    "Кристи" "Сьюзан я знаю, а кто второй? "
    "[gg]" "Ха-ха-ха! Очень смешно."
    "Кристи" "Хи-хи-хи!"
    "Кристи" "Она тебе понравилась, да?"
    "[gg]" "Почему ты спрашиваешь именно об этом?"
    "Кристи" "Так понравилась или нет?"
    "[gg]" "Довольно привлекательная. "
    "Кристи" "Значит, ты пойдёшь к неё ещё раз, верно?"
    "[gg]" "Совсем не из-за её внешности."
    "Кристи" "Ну да, ну да, так я и поверила."
    "[gg]" "Хм…"
    "[gg]" "Зачем ты тогда советовал мне её, если не веришь, будто она может мне помочь? "
    "Кристи" "Просто я жутко удивлена, что ты вообще на такое решился."
    "[gg]" "Вот именно!"
    "[gg]" "Мы долго и основательно говорили, и в ходе беседы она помогла мне с идентификацией самого себя."
    "Кристи" "Вау. Звучит интригующе!"
    "Кристи" "Как тебе её сиськи? Ты их тоже идентифицировал?"
    "[gg]" "Ты издеваешься?"
    "Кристи" "Ахахаха! Прости, не могу удержаться. "
    "Кристи" "Это всё так интригующе, я вся на взводе!"
    "[gg]" "Ты хочешь услышать о том что было, или обсуждать внешность Сьюзен? "
    "Кристи" "Говори-говори. Я молчу."
    "[gg]" "После разговора с ней, я понял, что жил совсем не так, как мне того хотелось бы."
    "[gg]" "И теперь, надеюсь, я смогу начать всё с чистого листа."
    "Кристи" "Ого… Мне бы тоже этого хотелось."
    "[gg]" "Правда?"
    "Кристи" "Без шуток."
    "[gg]" "Знаешь, мне почему-то хочется компенсировать свой эгоизм и помогать близким людям. Быть им полезным."
    "Кристи" "Да? А я вхожу в их число?"
    "[gg]" "Конечно."
    "Кристи" "О, замечательно!"

    scene expression 'cg/christie_root/kristy_sit_2.png' with vpunch
    "Кристи" "Как на счёт массажа для ног? Ты достаточно угодлив для такого рода помощи? "
    "[gg]" "Ну… Если ты просишь. "
    "Кристи" "Очень-очень прошу. Это засчитается тебе в карму, честное слово!"
    "[gg]" "Что ж… Я только рад сделать тебе приятное. "


    scene expression 'cg/christie_root/kristy_sit_3.png' with Dissolve(.5)
    "Кристи" "О даааа, это действительно оооочень и оооочень приятно."
    "[gg]" "Тебе настолько нравится?"
    "Кристи" "Никогда бы не подумала, что у тебя такие ласковые руки. "
    "Кристи" "Пожалуйста, продолжай."
    "Кристи" "Массируй мои ножки столько, на сколько у тебя хватит сил."
    "Кристи" "Ведь ты же сильный, верно?"
    "[gg]" "Хочется в это верить, конечно, хотя прежде мне не приходилось массажировать чьи-либо ноги на износ. "
    "Кристи" "Оххх… Прошу. "
    "Кристи" "Вот тут, да. Пощипывай. Ага. "
    "Кристи" "А здесь поглаживай. Да-да, просто восхитительно. Кристи"


    scene expression 'cg/christie_root/kristy_sit_4.png' with Dissolve(.5)

    "[gg]" "А у тебя очень нежная, мягкая кожа."
    "[gg]" "Её приятно трогать, ласкать… "
    "[gg]" "Знаешь, я раньше никогда не смотрел на твои ножки, но теперь вижу, какие они красивые и аккуратные. "
    "Кристи" "Д-действительно?..."
    "[gg]" "Ага."
    "[gg]" "Я с огромным наслаждением массажирую их."
    "Кристи" "Так… т-так, постой. "
    scene black with vpunch
    $ renpy.pause(.5, hard = True)




    $ time.time_now = 'evening'
    $ location_now  = 'Hall'
    call show_bg_image_label from _call_show_bg_image_label_100

    call show_additional_images_label from _call_show_additional_images_label_85

    show Christie Embarrassment
    show Christie Embarrassment:
        xalign .85
        ypos 1085


    show GG Normal
    show GG Normal:
        xalign .2



    with my_dissolve
    "Кристи" "Этого более чем достаточно, [gg]."
    show Christie Embarrassment
    "Кристи" "Спасибо за массаж и компанию, но я, пожалуй, вернусь в свою комнату. "
    show Christie Embarrassment
    "Кристи" "У меня там кое-какие дела ещё…"
    show GG Embarrassment
    "[gg]" "Рад бы услужить, Кристи. "
    show Christie Embarrassment:
        linear .75 xalign -1.5

    $ renpy.pause(1, hard = True)
    hide Christie

    show GG Think
    with my_dissolve
    "[gg]" "Обалдеть, кажется я возбудил её…"

    "[gg]" "Да кого я обманываю? Я и сам не на шутку завёлся."
    "[gg]" "Мне не стоило так увлекаться массажем, это уже чересчур. "


    $ descript_Christie = _("Поговорить с Кристи на следующий день, возможно я снова пригожусь ей для какого-нибудь «дела». Думаю лучше обратиться к ней прямо самого утра.")
    $ Event('christie_root_7', 'Christie', time = ['morning'])
    $ sister_position['morning'] = ['Kitchen', 'sister_kitchen_2']
    #$ block_milf_home = True
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
