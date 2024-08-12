label biblio_2:
    # Description: Спросить у Игоря про странную записку.
    # Task: Активировать Игоря в Парке.
    
    call show_bg_image_label
    show GG Smile
    show GG Smile at go_from_left(xxalign = .15)
    show Igor Ok
    show Igor Ok:
        xalign .85
    with my_dissolve
    
    "Игорь" "Почему-то, когда вижу тебя, сразу испытываю напряжение."
    "[gg]" "Может, ты просто влюблён в меня?"
    show Igor Angry with my_dissolve
    "Игорь" "Ага. Только вместо бабочек в животе, у меня вилы в жопе."
    show Igor Smile with my_dissolve
    "Игорь" "Ладно уж. Выкладывай, чего припёрся?"
    show GG Normal with my_dissolve
    "[gg]" "Я тут нашёл какую-то тарабарщину. Хотел бы узнать, что именно она означает."
    show Igor Normal with my_dissolve
    "Игорь" "Ничего не понял, но показывай."
    show GG Skepticism with my_dissolve
    "[gg]" "Вот, держи."
    show Igor Skepticism with my_dissolve
    "Игорь" "Хех..."
    show Igor Normal with my_dissolve
    "Игорь" "Сперва скажи, где ты это нашёл?"
    show GG Normal with my_dissolve
    "[gg]" "Выпало из книги."
    show Igor Smile with my_dissolve
    "Игорь" "А книгу где взял?"
    "[gg]" "Дали почитать."
    show Igor Skepticism with my_dissolve
    "Игорь" "Кто?"
    show GG Angry with my_dissolve
    "[gg]" "Слушай, какая разница? Просто скажи наконец, что конкретно здесь написано."
    show Igor Normal with my_dissolve
    "Игорь" "Бро, это Синдарин."
    show GG Surprise
    "[gg]" "Чего?"
    "Игорь" "Эльфийский, дурная твоя башка."
    "Игорь" "Выдуманный язык Джона Толкина, автора книги «Властелина Колец»."
    "[gg]" "Ух ты. Ну и что здесь написано?"
    "Игорь" "Откуда мне знать? Я ж не эльф."
    show GG Smile with my_dissolve
    "[gg]" "Это заметно."
    "Игорь" "Пошёл нахер, эльфоёб."
    "Игорь" "Тот, кто подложил тебе эту записку определённо хочет, чтобы ты приложил усилия для расшифровки."
    show GG Skepticism with my_dissolve
    "[gg]" "Проверить мой интеллект?"
    "Игорь" "Скорее энтузиазм."
    "Игорь" "Любой дурак знает, что это Синдарин, но тебе в любом случае понадобится какое-то время, чтобы перевести его."
    show GG Normal with my_dissolve
    "[gg]" "Хм... Спасибо за разъяснение, дружище."
    "Игорь" "Пожалуйста."
    hide Igor with my_dissolve
    show GG Think with my_dissolve
    "[gg]" "Можно было бы воспользоваться интернетом и вбить запрос в поисковик..."
    "[gg]" "Но вбить символы я не смогу, поэтому придётся смотреть в словарь и разбираться что есть что, подбирая нужные значения."
    "[gg]" "Это долго и не факт, что я истолкую текст верно."
    "[gg]" "Нужен эксперт."
    "[gg]" "Тревожить Игоря по пустякам я не хочу, он и так постоянно выручает меня."
    "[gg]" "Возможно Кристи мне поможет."
    
    $ events.pop("biblio_2", 0)
    $ Event("biblio_3", location = "Christie", time=["morning", "afternoon", "evening"])
    
    jump main_interface_label
