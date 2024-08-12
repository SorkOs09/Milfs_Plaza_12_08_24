init 10:
    image cg readroom = "images/cg/biblio/readroom/background.png" #TODO а точно этот тот фон?
    image cg_readroom table = "images/cg/biblio/readroom/1.png"
    image cg_readroom table xray =  FlashLight("images/cg/biblio/readroom/1.png")
    image cg_readroom_peoples:
        choice:
            "images/cg/biblio/readroom/peoples/1.png"
        choice:
            "images/cg/biblio/readroom/peoples/2.png"
        time 5
        repeat

    image bg boobfuck = "images/cg/biblio/boobfuck/background.png"
    image boobfuck_boobs = "images/cg/biblio/boobfuck/boobs.png"
    image boobfuck_book = "images/cg/biblio/boobfuck/book.png"

    image bg readroom = "images/cg/christie_root/library/afternoon.png"
    image bookshelves_chair = "images/cg/biblio/book_chair.png"


label biblio_14:
    # Description: Нэнси ждёт меня в библиотеке.
    # Task: Активировать Нэнси в библиотеке утром или днём.
    
    call show_bg_image_label
    show GG Normal
    show GG Normal:
        xalign .15
    # show BiblioGirl Smile
    # show BiblioGirl Smile:
    #     xalign .85
    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign .85
    with my_dissolve
    
    "[gg]" "Лучший курьер на районе прибыл!"
    "Нэнси" "Хи-хи-хи!"
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Надеюсь, я не слишком утомляю тебя своими заботами."
    show GG Passion with my_dissolve
    "[gg]" "Ты трудишься на много больше."
    # show BiblioGirl Embarrassment with my_dissolve
    "Нэнси" "Оу!"
    "Нэнси" "Какая лестная оценка, [gg]."
    # show BiblioGirl Smile with my_dissolve
    "Нэнси" "Пойдём. Время не ждёт."
    show GG Normal:
        ease 1 xalign 1.5
    show BiblioGirl Normal:
        ease 1 xalign 1.5
    with None
    scene bg readroom
    with my_dissolve #my_fade #TODO а куда my_fade делся?
    show GG Normal:
        xalign -.5
        ease 1 xalign .15
    show BiblioGirl Normal:
        xalign -.5
        ease 1 xalign .85
    pause 1
    # //Оба спрайта движутся вправо
    # //Читальный зал
    # //Оба спрайта выезжает слева
    # //Читатели
    
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Правила ты помнишь, я надеюсь."
    "Нэнси" "Посетители просят книгу, и ты им её приносишь."
    show GG Skepticism:
        yalign 1.0
    "[gg]" "Я уже на взлёте, как чёртов шатл."
    # show BiblioGirl Smile with my_dissolve
    "Нэнси" "Ну вперёд, красавчик."

    show BiblioGirl Normal:
        ease 1 xalign 1.5
    pause 1
    hide BiblioGirl

    # Повторение мини-игры #TODO мини-игра, не трогаю
    # //При успехе мини-игры появляется табличка «Вы победили» (которая у нас есть)
    
    show GG Think with my_dissolve
    "[gg]" "Где Нэнси?"
    "[gg]" "Я думал он появиться, чтобы поблагодарить меня..."
    "[gg]" "Ну хорошо, поищу её сам."
    show GG Smile with my_dissolve
    "[gg]" "Возможно она снова приготовила мне сюрприз."
    
    # //GG_Normal едет вправо
    # //Книжные полки
    # //Спрайт  I_dont_Book
    # //После активации спрайт

    show GG Normal:
        ease 1 xalign 1.5
    with None
    pause 1
    scene bg bookshelves
    show bookshelves_chair
    with my_dissolve #my_fade #TODO а куда my_fade делся?
    show GG Normal:
        xalign -.5
        ease 1 xalign .25
    pause 1

    show GG Surprise with my_dissolve
    "[gg]" "Книга?"
    "[gg]" "Это и есть мой сюрприз?.."
    show GG Chagrin with my_dissolve
    "[gg]" "В тот раз был поинтереснее."
    show GG Think:
        yalign 1.0
    "[gg]" "Хм..."
    "[gg]" "Может в этой книге тоже сокрыто какое-то послание на эльфийском языке."
    "[gg]" "Стоит поискать."
    
    scene bg boobfuck
    show boobfuck_book
    with my_dissolve
    # //Boobs_Read_1
    
    "[gg]" "Нет..."
    "[gg]" "Здесь определённо ничего нет."
    "[gg]" "Как странно."
    "[gg]" "Попробую пролистать все страницы на случай, если где-то стоит пометка, а я просто не заметил."
    "[gg]" "Пробегая словами книгу, могу заметить, что это какой примитивный любовный роман..."
    "[gg]" "Может это и есть одно сплошное послание и мне просто следует вчитаться в содержание?.."

    scene bg boobfuck:
        ease 1 blur 15
    show boobfuck_book
    with my_dissolve

    "[gg]" "Если б ещё текст не вызывал у меня приступы острого стыда.."
    "[gg]" "На какой странице я бы не очутился, везде описываются «страстные» сцены нимфоманки и парня, который только начал постигать азы любви."
    "[gg]" "Ну вот..."
    "[gg]" "Очередная глава, где значится, что так и так..."
    "[gg]" "Неутолимая женщина застаёт возлюбленного врасплох, снимает с него штаны и, скрепив его возбуждённый член между своими двумя огромными дыньками, нежно массирует детородный орган парня."
    "[gg]" "Чёрт..."
    "[gg]" "Не смотря на весь примитивизм, признаться, я и сам немного возбудился."
    "[gg]" "От рассказа веет такой аурой сексуальности, что я буквально ощущаю, как сам испытываю сисько-трах..."
    "[gg]" "Стоит отдать автору должное, он сумел меня впечатлить."
    "[gg]" "Или же..."
    
    # //Книга опускается
    # //Boobs_Read_anim #TODO анимации все еще нет, делать тут нечего((((
    # //x1
    scene bg boobfuck:
        blur 8
    show boobfuck_boobs:
        blur 8
    show boobfuck_book
    with my_dissolve
    pause 0.5
    show boobfuck_book:
        ease 1 yoffset 1000
    pause 1.0
    scene bg boobfuck:
        blur 8
        ease 1 blur 0
    show boobfuck_boobs:
        blur 8
        ease 1 blur 0
    pause 1
    with hpunch

    "[gg]" "Нэнси?!!.."
    "Нэнси" "Тихо, дурашка!"
    "Нэнси" "Ты же не хочешь, чтобы сюда прибежала вся библиотека?"
    "[gg]" "Не хочу."
    "Нэнси" "Ну и? Чего замер? Хи-хи-хи."
    "[gg]" "Я... Э..."
    "Нэнси" "Разве не нравится книга?"
    "[gg]" "Неожиданно впечатляющая."
    "[gg]" "Я бы даже сказал - шокирующая."
    "Нэнси" "Рада, что смогла угодить и твоим читательским интересам."
    "Нэнси" "Продолжай читать, [gg]."
    "Нэнси" "Нам обоим предстоит дойти до развязки."
    "[gg]" "Хе-хе..."
    "[gg]" "Верно подмечено, Нэнси. Я, пожалуйста, углу... углублюсь в чтение."
    "Нэнси" "Ага."
    "[gg]" "В общем... В книге значится, что женщина ускорила свои массажные ласки."
    
    # //x2
    
    "Нэнси" "Хи-хи-хи."
    "Нэнси" "Ну же, не вздыхай так тяжело. Что было дальше?"
    "[gg]" "Дальше описывается её игривый, подобострастный взгляд и лёгкая улыбка, с которой она мастерски ублажала своего партнёра."
    "[gg]" "Женщина, пылая от предвкушения, стала покрываться горячим потом..."
    "[gg]" "А член её партнёра, словно в благодарность за старательность нимфоманки, пульсировал в такт с её движениями грудей, что крепко, но ласково, массировался вдоль всего размера."
    "[gg]" "Парень тяжело и громко дышал, не решаясь сказать ни слова."
    "[gg]" "То ли от того, что боялся спугнуть свою даму, то ли потому, что находился в полном ступоре от происходящего."
    "[gg]" "Во всяком случае, оба партнёра получали желаемое удовольствие."
    "Нэнси" "Ну же? Давай дальше!"
    "Нэнси" "Хочу знать, чем закончилась эта сцена."
    
    # //x3
    
    "[gg]" "Читаю-читаю..."
    "[gg]" "Леди, которая всё это время ублажала парня, разыгралась не на шутку."
    "[gg]" "Теперь, когда она поняла, что её партнёр испытал достаточно радости от массажа, даме захотелось приблизить кульминацию."
    "[gg]" "Всячески ускоряя ритм, продолжая строить вызывающую гримасу, она с наслаждением следила за реакцией своего мужчины."
    "[gg]" "Парень, чей член давно дрожал в нетерпении, сдерживался из последних сил."
    "[gg]" "Половой орган мужчины с избытком покрылся прозрачными выделениями, давно измазав сочные груди прекрасной нимфоманки."
    "[gg]" "И парень, и женщина, оба дышали в такт, вот-вот ожидая белоснежного фонтана, что должен был залить богатое декольты дамы."
    "Нэнси" "И как, [gg]? У него получилось, а?.."
    "Нэнси" "Порадовал он свою возлюбленную?"
    
    # //Выбор скорости/кончить
    # //Кончить
    # //Boobs_Read_END_anim
    
    "[gg]" "Кончаааааюююююю!!!"
    "[gg]" "О дааааааа...."
    "[gg]" "К чёрту эту книгу, Нэнси. Я обожаю твои сиськи!"
    
    # //Boobs_Read_END
    
    "Нэнси" "Хи-хи-хи!"
    "Нэнси" "Там много..."
    "Нэнси" "Так сладко пахнет и такая горячая. Ммммм..."
    "Нэнси" "Уверенна, наша концовка более реалистичная."
    "[gg]" "Ага."
    
    # //Книжные полки
    scene bg bookshelves
    
    # //Читальный зал
    show GG Embarrassment
    show GG Embarrassment:
        xalign .15
    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign .85
    with my_dissolve
    
    # show BiblioGirl Embarrassment with my_dissolve
    "Нэнси" "Чтоб ты понимал, [gg], ты первый, кого я так отблагодарила за помощь."
    "[gg]" "Я ценю это, Нэнси."
    "[gg]" "Ты мне нравишься, и я всегда рад тебе помочь."
    "Нэнси" "И чтоб ты понимал, ты единственный, кто разгадал мои загадки."
    show GG Passion with my_dissolve
    "[gg]" "Ты проверяла меня? Проверяла, можно ли быть со мной достаточно... близкой?"
    # show BiblioGirl Passion with my_dissolve
    "Нэнси" "Ну конечно."
    "Нэнси" "Мы должны были лучше узнать друг друга."
    "Нэнси" "И если парни, как правило, ценят в девушках их красоту, то я ценю ум и смекалку хи-хи-хи."
    "[gg]" "Ты права. Права во всём, хе-хе."
    "Нэнси" "До встречи, красавчик."
    "[gg]" "Увидимся."
    
    # 2 половина ебатории
    
    $ events.pop("biblio_14", 0)
    $ Event("biblio_15", location = "City_Library_BiblioGirl", day_start=time.day_now+1, time=["morning", "afternoon"], button_name="ХЗ КАК НАЗВАТЬ") #TODO !!!!!!!!!!!!!
    
    jump main_interface_label
