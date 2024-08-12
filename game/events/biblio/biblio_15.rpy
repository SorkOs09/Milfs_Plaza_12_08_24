init:
    image cg_readroom_gg 1 = "images/cg/biblio/wank/gg/1.png"
    image cg_readroom_gg 2 = "images/cg/biblio/wank/gg/2.png"
    image cg_readroom_gg 3 = "images/cg/biblio/wank/gg/3.png"
    image cg_readroom_gg 4 = "images/cg/biblio/wank/gg/4.png"
    image cg_readroom_gg 5 = "images/cg/biblio/wank/gg/5.png"

    image cg_readroom_nency 1 = "images/cg/biblio/wank/nency/1.png"
    image cg_readroom_nency 2 = "images/cg/biblio/wank/nency/2.png"
    image cg_readroom_nency enter = "images/cg/biblio/wank/nency/enter.png"
    image cg_readroom_nency_shadow = "images/cg/biblio/wank/nency/shadow.png"
    image cg_readroom_lamp = "images/cg/biblio/wank/lamp.png"

    image cg_readroom_nency gg = "images/cg/biblio/wank/nency/up.png"

    image cg_readroom_fap 1 = "images/cg/biblio/wank/fap/1.png"
    image cg_readroom_fap 2 = "images/cg/biblio/wank/fap/2.png"
    image cg_readroom_fap 3 = "images/cg/biblio/wank/fap/3.png"
    image cg_readroom_fap 4 = "images/cg/biblio/wank/fap/4.png"
    image cg_readroom_fap 5 = "images/cg/biblio/wank/fap/5.png"
    image cg_readroom_fap 6 = "images/cg/biblio/wank/fap/6.png"


    image cg_readroom_fap anim1:
        "cg_readroom_fap 1"
        0.25
        "cg_readroom_fap 2"
        0.25
        "cg_readroom_fap 3"
        0.25
        "cg_readroom_fap 4"
        0.25
        "cg_readroom_fap 5"
        0.25
        "cg_readroom_fap 6"
        0.25
        "cg_readroom_fap 5"
        0.25
        "cg_readroom_fap 4"
        0.25
        "cg_readroom_fap 3"
        0.25
        "cg_readroom_fap 2"
        0.25
        repeat
    
    
    image cg_readroom_fap anim2:
        "cg_readroom_fap 1"
        0.18
        "cg_readroom_fap 2"
        0.18
        "cg_readroom_fap 3"
        0.18
        "cg_readroom_fap 4"
        0.18
        "cg_readroom_fap 5"
        0.18
        "cg_readroom_fap 6"
        0.18
        "cg_readroom_fap 5"
        0.18
        "cg_readroom_fap 4"
        0.18
        "cg_readroom_fap 3"
        0.18
        "cg_readroom_fap 2"
        0.18
        repeat
    
    
    image cg_readroom_fap anim3:
        "cg_readroom_fap 1"
        0.1
        "cg_readroom_fap 2"
        0.1
        "cg_readroom_fap 3"
        0.1
        "cg_readroom_fap 4"
        0.1
        "cg_readroom_fap 5"
        0.1
        "cg_readroom_fap 6"
        0.1
        "cg_readroom_fap 5"
        0.1
        "cg_readroom_fap 4"
        0.1
        "cg_readroom_fap 3"
        0.1
        "cg_readroom_fap 2"
        0.1
        repeat

    image cg_readroom_fap_cum 1 = "images/cg/biblio/wank/cum/1.png"
    image cg_readroom_fap_cum 2 = "images/cg/biblio/wank/cum/2.png"
    image cg_readroom_fap_cum 3 = "images/cg/biblio/wank/cum/3.png"
    image cg_readroom_fap_cum 4 = "images/cg/biblio/wank/cum/4.png"
    image cg_readroom_fap_cum 5 = "images/cg/biblio/wank/cum/5.png"
    image cg_readroom_fap_cum 6 = "images/cg/biblio/wank/cum/6.png"

    image cg_readroom_fap_cum anim:
        "cg_readroom_fap_cum 1"
        0.1
        "cg_readroom_fap_cum 2"
        0.1
        "cg_readroom_fap_cum 3"
        0.1
        "cg_readroom_fap_cum 4"
        0.1
        "cg_readroom_fap_cum 5"
        0.1
        "cg_readroom_fap_cum 6"

    

label biblio_15:
    # Description: Мне стоит вновь увидеться с Нэнси. Мне кажется, или у нас закручивается очень странный роман?..
    # Task: Активировать Нэнси в библиотеке утром или днём.
    
    call show_bg_image_label

    show GG Normal
    show GG Normal:
        xalign .15
    # show BiblioGirl Surprise
    # show BiblioGirl Surprise:
    #     xalign .85
    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign .85
    with my_dissolve
    
    "[gg]" "Сегодня отличный день для чтения, не правда ли?"
    "Нэнси" "Охх!! Ты мой спаситель, [gg]!"
    "Нэнси" "Я погибаю..."
    show GG Surprise with my_dissolve
    "[gg]" "Что произошло, Нэнси?!"
    show GG Angry with my_dissolve
    "[gg]" "Тебя кто-то обидел?"
    # show BiblioGirl Embarrassment with my_dissolve
    "Нэнси" "О! Нет-нет! Что ты!"
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Новые завсегдатаи библиотеки... Ну, те самые, за которых мы с тобой «бились», чтобы им у нас понравилось."
    show GG Skepticism with my_dissolve
    "[gg]" "Они разочарованы? Опять?!"
    "Нэнси" "Наоборот."
    "Нэнси" "Ребята с упоением читают книги, но совсем не умеют вести себя прилично."
    # show BiblioGirl Angry with my_dissolve
    "Нэнси" "Вскрикивают! Громко воздыхают. Переговариваются друг с другом или юубнят под нос..."
    "Нэнси" "Библиотека любит тишину, а не вот это вот всё!"
    "[gg]" "Предлагаешь их погнать всех шею?"
    # show BiblioGirl Surprise with my_dissolve
    "Нэнси" "Не сходи с ума, [gg]!"
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Следи за поведением посетителей – этого будет достаточно."
    
    # //Оба спрайте движутся вправо
    # //Читальный зал
    # //Оба спрайта выдвигаются слева
    
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

    show GG Normal with my_dissolve
    "[gg]" "Выдашь соответствующее вооружение?"
    # show BiblioGirl Smile with my_dissolve
    "Нэнси" "Ты не охранник, а вахтёр."
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Если кто-то начнёшь шуметь, просто подойти и тихонько сделай замечание."
    "Нэнси" "Вежливо, разумеется."
    "Нэнси" "Не вздумай кому-то угрожать или хамить."
    "[gg]" "А если не успею?.."
    "Нэнси" "Тогда будет слишком шумно, остальные посетители больше не захотят сюда приходить."
    "[gg]" "А если нарушители тишины не послушают меня?"
    "Нэнси" "Послушают. Ты же не в баре вышибалой работаешь."
    "Нэнси" "Подбери подходящие слова и всё будет хорошо."
    "[gg]" "Думаешь?"
    "Нэнси" "Знаю."
    "Нэнси" "Всё. Я бегу дальше выполнять свой регламент работ, а ты, пожалуйста, внимательно следи за посетителями. Тишина, понял?"
    "[gg]" "Да понял я, понял."

    show BiblioGirl Normal:
        ease 1 xalign 1.5
    pause 1
    hide BiblioGirl

    # //Мини-игра «Тишина» #TODO тут мини-игра - не трогаю
    # //Над головами посетителей переодически появляются иконки/диограмы звука, которые, пока висят, заполняют главную шкалу «звука», как только шкала заполнится, игрок проиграл
    # //Кликнув на иконку посетителя с диограмой звука, игроку отображается маленькая шкала с бегающим шариком и черточкой в случайном месте. Игроку надо поймать момент, когда шарик находится в чёрточке на шкале, и кликнуть мышкой (не важно куда). Успех – шкала «звука» ощутимо снижается (например, 2/3 от самой длины пустой шкалы)
    # Провал – шкала «звука» остаётся на прежнем уровне, но данный «посетитель» прекращает шуметь.
    # //Цель игры – продержаться минуту
    # //Про проигрыше
    # //То же помещение с теми же спрайтами читателей
    # //GG_Normal
    # //Выезжает справа BiblioGirl_Angry
    
    # show BiblioGirl Angry with my_dissolve
    "Нэнси" "Что произошло?!"
    "Нэнси" "Почему тут такой галдёж?!!"
    show GG Chagrin with my_dissolve
    "[gg]" "Извини, я не справился..."
    "[gg]" "Они меня совсем не слушают, да и я не особо успеваю подобрать нужные слова."
    show GG Embarrassment with my_dissolve
    "[gg]" "Бедняжка."
    "[gg]" "Я слишком много на тебя возлагаю."
    "[gg]" "Попробуешь ещё или в другой раз?"
    
    # //Если «в другой раз»
    # //Time: Evening
    # //Хол библиотеки
    # //библиотекарши нет
    # //В любой другой день при повторном разговоре
    
    show GG Normal with my_dissolve
    "[gg]" "Посетители все ещё шумят?"
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Ещё как."
    "[gg]" "Давай утихомирю."
    # show BiblioGirl Smile with my_dissolve
    "Нэнси" "Хи-хи-хи!"
    "Нэнси" "Мне нравится твой настрой."
    
    # //Оба спрайта движутся вправо
    # //Читальный зал
    # //Оба спрайта выдвигаются слева
    
    "Нэнси" "Готов?"
    "[gg]" "Абсолютно."
    
    # //Мини-игра
    # //При победе в мини-игре

    #TODO возвращаюсь в код тут
    
    show GG Think 
    with my_dissolve
    "[gg]" "Ха, я отлично справился с задачей."
    "[gg]" "Уже продолжительное время тишина. Ни писка."
    "[gg]" "Схожу поищу Нэнси."
    "[gg]" "Расскажу ей о своих успехах."
    
    # //GG_Normal движется вправо
    # //Книжный полки
    
    show GG Normal:
        ease 1 xalign 1.5
    with None
    pause 1
    scene bg bookshelves
    with my_dissolve #my_fade #TODO а куда my_fade делся?
    show GG Normal:
        xalign -.5
        ease 1 xalign .25
    pause 1

    show GG Chagrin with my_dissolve
    "[gg]" "Ну вот... В который раз это повторяется."
    "[gg]" "Снова она куда-то запропастилась."
    "[gg]" "И никаких намёков на то, куда она подевалась и что мне дальше делать."
    show GG Smile with my_dissolve
    "[gg]" "Ладно..."
    "[gg]" "Пока жду её, можно взять почитать какую-то книгу в читальном зале."
    "[gg]" "Раз уж я навёл там такой «порядок», я – как никто другой заслуживаю там читать в тишине и спокойствии."
    
    # //Art_Read_Book_1  (изображён ГГ за чтением)
    scene cg readroom
    show cg_readroom table
    show cg_readroom_lamp
    show cg_readroom_peoples
    show cg_readroom_gg 1
    with my_dissolve #my_fade #TODO а куда my_fade делся?

    
    "[gg]" "Интересно, все выбирают книги по красоте обложки или только я?"
    "[gg]" "«Под знаком Мантикоры»."
    "[gg]" "Судя по содержанию, это не просто фэнтези, но и настоящий детектив."
    "[gg]" "Главный герой, как и положено, бескомпромиссно прав, честолюбив и подкован идеологически."
    "[gg]" "К моему удивлению, жена главного героя тоже выступает действующим лицом романа."
    "[gg]" "Наверное, эта отважная, но красивая женщина, была списана с любимой дамы автора книги."
    
    # //Art_Read_Book_2 (Нэнси стоит у стола)
    # //Art_Read_Book_3  (Нэнси сидит за столом)
    show cg_readroom_nency enter behind cg_readroom_gg
    with my_dissolve
    pause 1
    show cg_readroom_nency 1 behind cg_readroom_gg
    show cg_readroom_nency_shadow behind cg_readroom_nency
    with my_dissolve    
    
    "Нэнси" "Увлекательно?"
    "Нэнси" "Хи-хи-хи!"
    show cg_readroom_gg 2 with my_dissolve
    "[gg]" "Извини, я не смог тебя найти и решил хоть как-то убить время."
    "Нэнси" "О, ты правильно поступил."
    "Нэнси" "Не хочу, чтобы ты зависит от моей благодарности."
    show cg_readroom_nency 2
    "Нэнси" "Но и не хочу, чтобы ты забывал, как я признательна тебе."
    show cg_readroom_gg 3 with my_dissolve
    "[gg]" "И что же ты предлагаешь?"
    
    # //Art_Read_Book_4 (Держит за член)
    show cg_readroom_nency gg
    hide cg_readroom_gg
    show cg_readroom table xray
    hide cg_readroom_nency_shadow
    show cg_readroom_fap 1 behind cg_readroom
    with my_dissolve
    
    "Нэнси" "Хочу просто посидеть рядом."
    "Нэнси" "Если ты не против, конечно."
    "[gg]" "Я... Нет..."
    "[gg]" "То есть, не против конечно. Сиди хоть до утра, хе-хе..."
    "Нэнси" "Тссс!"
    "Нэнси" "Не суетись так сильно."
    "Нэнси" "Продолжай читать и наслаждаться содержанием, хи-хи-хи."
    
    # //Art_Read_Book_4_anim
    # //x1
    show cg_readroom_fap anim1 with my_dissolve
    
    "[gg]" "Знаешь, я не могу сосредоточится, пока ты делаешь «это»..."
    "Нэнси" "Ага."
    "Нэнси" "В этом и заключается суть шалости."
    "Нэнси" "Надеюсь ты понимаешь всю неловкость ситуации и не будешь громко говорить, чтобы не привлечь внимания."
    "[gg]" "Я вообще предпочту молчать."
    "Нэнси" "У тебя не только большой... кхм... ну ты понял, но и большой ум, хи-хи-хи."
    "[gg]" "......"
    
    # //х2
    show cg_readroom_fap anim2 with my_dissolve
    
    "[gg]" "{i}Охххх... Она налегает ещё сильнее.{/i}"
    "[gg]" "{i}Текст расплывается перед глазами.{/i}"
    "[gg]" "{i}Я не в состоянии прочесть ни слова, чтобы хоть как-то придать своему выражению лица осмысленный вид.{/i}"
    
    "Нэнси" "Какой ты напряжённый, [gg]."
    "[gg]" "Это всё из-за тебя, Нэнси. Я ещё не встречал таких женщин прежде."
    "Нэнси" "Я всего лишь стараюсь быть милой и благодарной."
    "Нэнси" "Парни, вроде тебя, не особо увлечены такими «серыми мышками» как я."
    "Нэнси" "Быть одной... Окружённой только книгами и унылыми посетителями, что и глаз на тебя не поднимают..."
    "Нэнси" "Это угнетает, понимаешь?"
    "[gg]" "П-понимаю."
    
    "[gg]" "{i}Чёрт, мысли разбегаются, мозг отказывается работать...{/i}"
    "[gg]" "{i}Мне хотелось бы повысить её самооценку подходящими словами, но...{/i}"
    "[gg]" "{i}Я чувствую себя безвольной марионеткой, пока её шаловливая рука ласкает мой член.{/i}"
    
    # //x3
    show cg_readroom_fap anim3 with my_dissolve

    
    "[gg]" "Нэнси..."
    "Нэнси" "Да, милый [gg]?"
    "[gg]" "Ты..."
    "[gg]" "Одна из самых роскошных девушек, которых я только знал."
    "Нэнси" "Правда? Ты честно так думаешь?.."
    "[gg]" "Сейчас мне... Оххх... Тяжеловато думать."
    "Нэнси" "Хи-хи-хи!"
    "[gg]" "Но я совершенно искренен в своих слова, Нэнси."
    "[gg]" "Иначе бы я не стал...."
    
    "[gg]" "{i}О нет... Я сейчас кончу.{/i}"
    "[gg]" "{i}Больше не могу сдерживаться.{/i}"
    "[gg]" "{i}Вот бы всё это вывалить на её сиськи, чёрт!{/i}"
    
    "[gg]" "Иначе бы я не стал возвращаться к тебе, Нэнси."
    "Нэнси" "Звучит красиво, но мало ли причин посетить библиотеку, хи-хи-хи."
    "Нэнси" "Ой... Кажется твой дружок чересчур сильно пульсирует и собирается..."
    "Нэнси" "Оуууу, я чувствую, как всё случится прямо здесь и сейчас."
    
    # //кончить
    # //Art_Read_Book_4_End
    hide cg_readroom_fap
    show cg_readroom table
    show cg_readroom_nency 2
    show cg_readroom_gg 5
    with dissolve

    
    "[gg]" "Кооо..."
    "Нэнси" "Тссссссс!!!"
    
    # //Art_Read_Book_4_End_anim (анимация кончи)
    show cg_readroom_fap_cum anim
    pause 1
    show cg_readroom_fap_cum anim as cg_readroom_fap_cum2:
        xoffset -70
    show cg_readroom_fap_cum anim as cg_readroom_fap_cum3:
        xoffset 70
    
    "[gg]" "Охххххх...."
    
    # //Art_Read_Book_4_End
    show cg_readroom_gg 3
    
    "[gg]" "Это было супер."
    "[gg]" "Точнее, это ты супер, Нэнси."
    "Нэнси" "Спасибо, хи-хи-хи."
    "Нэнси" "Мне нравятся твои комплименты, [gg]."
    "Нэнси" "Ты всегда так добр ко мне."
    "[gg]" "Можно мы и дальше будем видеться?.."
    "Нэнси" "Я жду наших встреч больше всего не свете."
    
    # //Читальный зал
    # //Читатели
    scene bg readroom
    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign .85
    show BiblioGirl Embarrassment
    show BiblioGirl Embarrassment:
        xalign .15
    with my_dissolve #my_fade #TODO а куда my_fade делся?

    "[gg]" "Ну, пока. Увидимся."
    "Нэнси" "Ага. До свидания."

    $ time.time_now = "evening"
    
    $ events.pop("biblio_15", 0)
    $ Event("biblio_16", location = "City_Library_BiblioGirl", time=["morning", "afternoon"], button_name="ХЗ КАК НАЗВАТЬ") #TODO !!!!!!!!!!!!!
    
    jump main_interface_label
