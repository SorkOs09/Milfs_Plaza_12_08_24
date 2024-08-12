label biblio_3:
    # Description: Поговорить с Кристи по поводу эльфийского языка.
    # Task: Активировать Кристи утром/днём/вечером.
    
    call show_bg_image_label
    show GG Normal
    show GG Normal at go_from_left(xxalign = .15)
    show Christie Smile
    show Christie Smile:
        xalign .85
    with my_dissolve
    
    "[gg]" "У меня для тебя прекрасная новость, Кристи!"
    "Кристи" "Да ну?!"
    "[gg]" "Я нашёл способ применить твою эрудицию на практике и дать волю тем огромным знаниям, что ты копила все эти годы."
    show Christie Angry with my_dissolve
    "Кристи" "Это шутка?"
    show GG Smile with my_dissolve
    "[gg]" "Только если ты ничего на самом деле на копила, а вместо книг читала идиотские цитатки гламурных дур в интернете."
    "Кристи" "Ты же понимаешь, что с каждым своим словом только сильнее злишь меня?"
    show GG Normal with my_dissolve
    "[gg]" "Я на полном серьёзе."
    "[gg]" "Мне нужна твоя помощь с переводом эльфийского текста."
    show Christie Surprise with my_dissolve
    "Кристи" "Вау!"
    "Кристи" "Зачем тебе понадобилось переводить Синдарин?"
    show GG Embarrassment with my_dissolve
    "[gg]" "Игорь попросил."
    show Christie Angry
    "Кристи" "Не упоминай имени этого извращенца в моём присутствии."
    show GG Angry with my_dissolve
    "[gg]" "Эй!"
    show GG Normal with my_dissolve
    "[gg]" "Не будь такой сучкой. Он мой лучший друг."
    "Кристи" "Да-да, я знаю, и готова помочь ТЕБЕ, раз уж ты вызвался помочь своему другу."
    "Кристи" "Ты же знаешь... Я терпеть его не могу."
    "[gg]" "У всех свои недостатки."
    "Кристи" "Ага. Только если он не пытается сталкерить тебя."
    "[gg]" "Хватит это вспоминать. Это было много лет назад, во втором классе."
    "[gg]" "Игорь просто перепутал туалетные комнаты."
    show Christie Skepticism with my_dissolve
    "Кристи" "Два раза подряд?"
    show GG Embarrassment with my_dissolve
    "[gg]" "Ну..."
    show GG Smile with my_dissolve
    "[gg]" "Он действовал в рамках науки."
    show GG Laughs
    "[gg]" "Стал свидетелем неизвестного явления, а после – перепроверил эффект, чтобы укрепиться в полученных знаниях."
    show Christie Normal with my_dissolve
    "Кристи" "....."
    "Кристи" "Разве такой «гений» не в состоянии самостоятельно перевести Синдарин?"
    show GG Speak
    "[gg]" "Так ты поможешь мне или нет?"
    "Кристи" "Помогу."
    "Кристи" "Давай сюда свой текст и я попробую что-то сделать."
    show GG Smile with my_dissolve
    
    $ remove_from_inventory('Любовная записка')
    
    $ events.pop("biblio_3", 0)
    $ Event("biblio_4", location = "Corridor", day_start=time.day_now+3, time=["morning", "afternoon", "evening"])
    
    jump main_interface_label
