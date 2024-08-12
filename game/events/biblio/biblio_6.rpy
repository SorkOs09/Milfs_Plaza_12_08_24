init:
    image bg bookshelves = "images/cg/biblio/bookshelves.png"

    image stairs ass = "images/cg/biblio/stairs/ass.png"
    image stairs stay = "images/cg/biblio/stairs/stay.png"


label biblio_6:
    # Description: Вернуть “Кама-сутру» Нэнси в библиотеке в пятницу.
    # Task: Активировать Нэнси в Библиотеке в ПЯТНИЦУ

    if time.tdtd != "Пятница":
        #show screen icons_interface(click=False)
        #with my_dissolve
        '[gg]' '{i}Вернуть “Кама-сутру» Нэнси в библиотеке в {b}пятницу{/b}.{/i}'
        jump main_interface_label
    
    call show_bg_image_label
    show GG Smile
    show GG Smile:
        xalign .15
    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign .85
    with my_dissolve
    
    "[gg]" "Нэнси, верно?"
    # show BiblioGirl Embarrassment #TODO нет вообще никаких эмоций, оставлю пока так
    "Нэнси" "Вы запомнили."
    "[gg]" "Ага. Я пришёл вернуть вашу книгу."
    # show BiblioGirl Smile with my_dissolve
    "Нэнси" "Хи-хи-хи."
    # show BiblioGirl Normal with my_dissolve
    "Нэнси" "Вам понравилось?"
    show GG Embarrassment with my_dissolve
    "[gg]" "Признаюсь... я совсем не читал её."
    # show BiblioGirl Chagrin with my_dissolve
    show GG Normal with my_dissolve
    "[gg]" "Но!"
    "[gg]" "Предугадывая ваш следующий вопрос, я оценил вашу любовь к эпопеи Толкина."
    # show BiblioGirl Embarrassment with my_dissolve
    "Нэнси" "Значит, вы пришли сюда не просто так..."
    show GG Smile with my_dissolve
    "[gg]" "Только если сегодня пятница."
    # show BiblioGirl Smile with my_dissolve
    "Нэнси" "Хи-хи-хи."
    # show BiblioGirl Embarrassment with my_dissolve
    "Нэнси" "Так волнительно и приятно."
    "Нэнси" "Как бы то ни было, сейчас мы находимся в библиотеке, и всё, что мы можем себе позволить, это познавать друг друга через книги."
    show GG Normal with my_dissolve
    "[gg]" "Не очень понял вас..."
    "Нэнси" "Прошу следовать за мной."
    
    show GG Normal:
        ease 1 xalign 1.5
    show BiblioGirl Normal:
        ease 1 xalign 1.5
    scene bg bookshelves with my_dissolve #my_fade #TODO а куда my_fade делся?
    show GG Normal:
        xalign -.5
        ease 1 xalign .15
    show BiblioGirl Normal:
        xalign -.5
        ease 1 xalign .85
    pause 1
    # // GG_Normal движется вправо
    # // BiblioGirl_Embarrassment движется вправо
    # //Читальный зал
    # // GG_Normal движется вправо
    # // BiblioGirl_Embarrassment движется вправо
    # //Полки книг
    
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Подождите меня здесь, пожалуйста."
    "Нэнси" "Сейчас я должна положить эту книгу на место."
    "Нэнси" "Можете пока осмотреться, возможно, вам приглянется какой-то роман."
    "[gg]" "Вряд ли здесь найдётся что-то интересное для меня."
    #show BiblioGirl Passionl with my_dissolve
    "Нэнси" "Пока не попробуете, не узнаете."
    
    scene bg bookshelves
    # //Biblio_Komnata_1
    show stairs stay 
    show BiblioGirl Invis
    show BiblioGirl Invis:
        xalign .25
    show GG Invis
    show GG Invis:
        xalign .53
    with my_dissolve
    
    "[gg]" "И часто вам приходится так рисковать?.."
    "Нэнси" "О, не беспокойтесь!"
    "Нэнси" "Эта лестница очень надёжная."
    "Нэнси" "Но если вы переживаете, то можете подстраховать меня."
    "[gg]" "Да, разумеется."
    "Нэнси" "Это так самоотверженно с вашей стороны, [gg]."
    "Нэнси" "Хи-хи-хи."
    
    # //Для продолжения нужно кликнуть по Нэнси на лестницу 
    call screen rtrn_screen("images/cg/biblio/stairs/stay.png", show_icons_interface = False)
    scene bg bookshelves:
        blur 15
    #show stairs stay:
    #    blur 15
    show stairs ass
    show stairs ass:
        xpos 450
    show BiblioGirl Invis
    show BiblioGirl Invis:
        xalign .25
    show GG Invis
    show GG Invis:
        xalign .75
    with my_dissolve
    # //Biblio_Komnata_2 (Ass)
    
    "[gg]" "Уфф..."
    "[gg]" "Лишь с такого ракурса становится понятно, насколько ценна и безупречна её работа."
    "[gg]" "У этой девушки на редкость шикарные формы."
    "[gg]" "Я с радостью послужу для неё подушкой безопасности."
    
    # //Biblio_Komnata_1
    
    "Нэнси" "Вот и всё, я справилась."

    hide stairs ass with my_dissolve
    scene bg bookshelves:
        blur 15
        ease 1 blur 0
    pause 1

    show GG Normal:
        xalign .15
    show BiblioGirl Normal:
        xalign .85
    with my_dissolve

    # //Полки книг
    
    "Нэнси" "Что ж, рада была вас повидать."
    "Нэнси" "Заходите ещё, если, конечно, на то будут причины."
    show shadow_full
    with my_dissolve
    "[gg]" "{i}Стоило бы предложить ей встретиться вновь.{/i}"
    "[gg]" "{i}В более располагающей обстановке.{/i}"
    "[gg]" "{i}Но раз она хочет, чтобы я посещал именно библиотеку, мне тоже нужна причина сюда являться.{/i}"
    hide shadow_full
    show GG Smile 
    with my_dissolve
    "[gg]" "А знаете, Нэнси..."
    "Нэнси" "Да?"
    "[gg]" "Я, наверное, всё таки возьму книгу для домашнего чтения."
    # show BiblioGirl Smile with my_dissolve
    "Нэнси" "Передумали?"
    show GG Embarrassment with my_dissolve
    "[gg]" "Ага. Решил пристраститься. Посоветуете что-нибудь? В том же духе, как и предыдущая книга."
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Вот и замечательно."
    "Нэнси" "У меня как раз есть подходящий экземпляр."
    # show BiblioGirl Passion with my_dissolve
    "Нэнси" "В этой книге вы обязательно найдёте повод, чтобы посетить меня вновь."
    "Нэнси" "Вот, держите."
    show GG Smile with my_dissolve
    "[gg]" "Спасибо."
    
    show screen give_item_screen(i_path+'items/ticket.png', _('Анжелика и Король'), _('Классический любовный роман'))
    pause
    hide screen give_item_screen
    
    # //Библиотека Холл
    call show_bg_image_label
    with my_dissolve #my_fade #TODO а куда my_fade делся?

    pause 1

    # //Библиотекарши нет #TODO как её убрать на локации??

    $ add_to_inventory(name = 'Книга «Анжелика и Король»')
    
    $ events.pop("biblio_6", 0)
    
    jump main_interface_label
