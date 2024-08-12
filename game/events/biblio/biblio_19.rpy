init:
    image incel = "images/cg/biblio/characters/incel.png"
    image secretman = "images/cg/biblio/characters/secretman.png"
    image simp1 = "images/cg/biblio/characters/simp1.png"
    image simp2 = "images/cg/biblio/characters/simp2.png"


label biblio_19:
    # Description: Это всё или нет? Если я захочу вновь увидеть Нэнси, мне надо посетить её в библиотеке.
    # Task: Активировать библиотеку.
    
    call show_bg_image_label
    show GG Normal
    show GG Normal at go_from_left(xxalign = .1)
    # show BiblioGirl Angry
    # show BiblioGirl Angry:
    #     xalign .4
    #     xzoom -1
    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign .4
        xzoom -1

    show simp1
    show simp2
    show incel
    with my_dissolve
    
    
    # //GG_Normal выезжает слева
    # //BiblioGirl_Angry
    # //Incel_lider (лидер инцелов)
    # //simp (одинаковые спрайты симпов)
    
    "Нэнси" "Прекратите этот кавардак, мальчишки!"
    "Нэнси" "Здесь приличное заведение."
    "Нэнси" "Соблюдайте правила тишины или убирайтесь!"
    "Incel" "Вы не заткнёте нас, леди!"
    "Incel" "Мы тоже имеем право на свободу слова!"
    "Incel" "Меня зовут Олихандэр Подземельный и представляю сообщество инцелов и социалистическую партию нашего района!"
    # show BiblioGirl Surprise with my_dissolve
    "Нэнси" "Чего?!"
    "Incel" "Мы требуем секс! Самый лучший секс в мире! Срочно! Любой ценой, но бесплатно!"
    # show BiblioGirl Skepticism with my_dissolve
    "Нэнси" "Как вас выпустили из дурки?"
    # show BiblioGirl Angry with my_dissolve
    "Нэнси" "Вы хоть понимаете, что городите?! Это библиотека, а не публичный дом."
    "Нэнси" "Покиньте помещение, пока я... Я..."
    "Incel" "Вы не имеете права нас выгонять!"
    "Incel" "Это городская библиотека. Она существует на наши налоги и мы, как жители этого города, так же имеем права здесь находиться и выражать свои мысли!"
    "Incel" "А сюда мы пришли, потому что желаем секс от умных и образованных женщин!"
    "Incel" "Нам не нужным подачки от вульгарных хабалок, которые готовы предоставить плотские утехи исключительно из меркантильных соображений."
    "Incel" "Долой вагинокапитализм! Даёшь – секс-коммунизм!"
    # show BiblioGirl Chagrin with my_dissolve
    "Нэнси" "Ну и что же мне делать..."

    show BiblioGirl Normal:
        xalign .4
        xzoom 1
    pause .1
    show BiblioGirl Normal:
        ease .3 xalign .25

    # // BiblioGirl_Chagrin движется в сторону GG
    
    # show BiblioGirl Surprise with my_dissolve
    "Нэнси" "Ох, [gg], и ты здесь!"
    # show BiblioGirl Smile with my_dissolve
    "Нэнси" "Ты даже не представляешь, как я безумно рада тебя видеть."
    "[gg]" "Взаимно, Нэнси."
    "[gg]" "Я и сам рад, что оказался здесь в такой момент."
    show GG Skepticism with my_dissolve
    "[gg]" "Эти придурки тебя донимают, но не волнуйся, сейчас я сгоняю домой за битой и отмудохаю уродов."
    # show BiblioGirl Surprise with my_dissolve
    "Нэнси" "Нет!!!"
    "Нэнси" "Ты что?! Нельзя так поступать с людьми."
    show GG Angry with my_dissolve
    "[gg]" "Ну и что по твоему я должен сделать?"
    "[gg]" "Умолять их заткнуться или вытолкнуть телекинезом?"
    # show BiblioGirl Chagrin with my_dissolve
    "Нэнси" "Извини..."
    "Нэнси" "Если б я знала, я бы справилась сама."
    "Нэнси" "Активисты настроены слишком серьёзно и всё, что мы можем сделать, это просто вызвать полицию."
    show GG Skepticism with my_dissolve
    "[gg]" "В задницу полицию."
    show GG Normal with my_dissolve
    "[gg]" "Сам справлюсь."
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Но без насилия, [gg]!"
    "Нэнси" "В противном случае они сами обратятся в полицию и тебя арестуют за физическое самоуправство."
    "[gg]" "Да понял я, понял."
    "[gg]" "Дайте пройти. Разберусь."
    
    # // GG_Normal движется вправо к Incel_lider и Simp`ам

    show BiblioGirl Normal:
        ease .5 xalign .1
        xzoom -1

    show GG Normal:
        ease .5 xalign .4

    "[gg]" "В чём проблема, парни?"
    "Incel" "А ты не видишь?!"
    "Incel" "Мы все, включая тебя – рабы системы!"
    "Incel" "Если мы не подобьёмся, чтобы женщины давали нам секс по первому требованию мужчины, мы навсегда останемся безвольными животными."
    "Incel" "Только секс позволяет мужчинам совершать великие открытия, творить подвиги, создавать шедевры, спасать человечество... ЭВОЛЮЦИОНИРОВАТЬ! В конце-концов..."
    "Incel" "Секс это всё! Секс – это энергия! ЭТО ЭНЕРГИЯ БЛЯДЬ!"
    "[gg]" "Понятно...  Диалог бесполезен."
    "[gg]" "Но я вас услышал, парни."
    "Incel" "Так ты с нами, чувак?! Ты вступишь в ряды секс-коммунизма?"
    "[gg]" "Я сделаю кое-что лучше."
    
    # //GG_Normal отъезжает вновь к BiblioGirl_Normal:

    show GG Normal:
        xzoom -1
        ease .5 xalign .25
    pause 0.5
    
    "[gg]" "У меня есть план, Нэнси."
    # show BiblioGirl Surprise with my_dissolve
    "Нэнси" "Бескровный, я надеюсь?"
    "[gg]" "Рабочий."
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "...."
    "Нэнси" "И что ты придумал?"
    "[gg]" "Найти пару женщин, готовых совратить этих идиотов."
    # show BiblioGirl Smile with my_dissolve
    "Нэнси" "Да кто на это согласится?"
    "[gg]" "О, это лучшие люди города!"
    
    # //мысли
    
    show GG Think with my_dissolve
    "[gg]" "{i}Кажется, у меня есть работка для Зудилы и Бубнилы.{/i}"
    
    # //конец мысли
    # //Карта города #TODO а как это сделать? Это же просто экран а не локация
    
    $ events.pop("biblio_19", 0)
    $ Event("biblio_20", location = "JayBob")
    
    jump main_interface_label
