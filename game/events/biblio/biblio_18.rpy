init:
    image pants_in_book = "images/cg/biblio/pants_book.png"

    image bg biblio_cuni = "images/cg/biblio/cuni/background.png"
    image biblio_cuni boobs_1 = "images/cg/biblio/cuni/boobs_1.png"
    image biblio_cuni boobs_2 = "images/cg/biblio/cuni/boobs_2.png"
    image biblio_cuni clothed_1 = "images/cg/biblio/cuni/clothed_1.png"
    image biblio_cuni clothed_2 = "images/cg/biblio/cuni/clothed_2.png"
    image biblio_cuni nude_1 = "images/cg/biblio/cuni/nude_1.png"
    image biblio_cuni nude_2 = "images/cg/biblio/cuni/nude_2.png"
    image biblio_cuni pants = "images/cg/biblio/cuni/pants.png"

    image biblio_cuni_gg 1 = "images/cg/biblio/cuni/gg/1.png"
    image biblio_cuni_gg 2 = "images/cg/biblio/cuni/gg/2.png"
    image biblio_cuni_gg 3 = "images/cg/biblio/cuni/gg/3.png"
    image biblio_cuni_gg 4 = "images/cg/biblio/cuni/gg/4.png"

    image biblio_cuni scenes anim 1 = "images/cg/biblio/cuni/scenes/1.png"
    image biblio_cuni scenes anim 2 = "images/cg/biblio/cuni/scenes/1.png"
    image biblio_cuni scenes anim 3 = "images/cg/biblio/cuni/scenes/1.png"
    image biblio_cuni scenes anim 4 = "images/cg/biblio/cuni/scenes/2.png"
    image biblio_cuni scenes anim 5 = "images/cg/biblio/cuni/scenes/2.png"
    image biblio_cuni scenes anim 6 = "images/cg/biblio/cuni/scenes/2.png"


label biblio_18:
    # Description: Подарить Нэнси шкатулку. Как всегда, её можно найти в библиотеке.
    # Task: Активировать Нэнси в библиотеке утром или днём.
    
    call show_bg_image_label
    show GG Normal
    show GG Normal:
        xalign .15
    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign .85
    with my_dissolve
    
    "[gg]" "Привет, Нэнси!"
    "Нэнси" "Приветик."
    "[gg]" "Как дела?"
    # show BiblioGirl Smile with my_dissolve
    "Нэнси" "Отлично."
    "Нэнси" "Не без твоей помощи, конечно."
    "[gg]" "Какие планы на сегодня? Разношу книги или слежу за порядком?"
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Ничего."
    "Нэнси" "Сегодня я решила не обременять тебя никакими делами."
    # show BiblioGirl Smile with my_dissolve
    "Нэнси" "Напротив, я хочу, чтобы ты насладился умиротворением и просто отдохнул."
    "Нэнси" "А потому вот. Маленький подарок от меня."
    # show BiblioGirl Embarrassment with my_dissolve
    "Нэнси" "Хочу подарить тебе книгу, которой заинтерисовался однажды, когда ждал моего появления в читальном зале."
    show GG Surprise with my_dissolve
    "[gg]" "О! Это же то фэнтези «Под знаком мантикоры»."
    show GG Smile with my_dissolve
    "[gg]" "Спасибо, Нэнси."
    show GG Passion with my_dissolve
    "[gg]" "Но я тоже не с пустыми руками."
    "[gg]" "Вот, эта необычная шкатулка с сюрпризом внутри для тебя."
    "Нэнси" "Ух ты! Как мило с твоей стороны, [gg]."
    "[gg]" "Я, признаюсь, и сам не знаю, что там содержится, но продавец заверил, что ты будешь в восторге."
    # show BiblioGirl Surprise with my_dissolve
    "Нэнси" "Даже так?.."
    "Нэнси" "Ты умеешь нагнать саспенс..."
    "Нэнси" "Мне уже не терпится всё узнать!"
    show GG Normal with my_dissolve
    "[gg]" "Сразу открыть не получится."
    "[gg]" "Шкатулка закрыта на замок-пазл."
    "[gg]" "Надеюсь, тебя обрадует этот элемент, учитывая, как сильно ты любишь всякие загадки."
    # show BiblioGirl Smile with my_dissolve
    "Нэнси" "Ещё бы! Конечно!"
    "Нэнси" "Я и мечтать о таком не могла..."
    "Нэнси" "Ещё раз спасибо тебе, [gg]!"
    # show BiblioGirl Embarrassment with my_dissolve
    "Нэнси" "Меня всю распирает от любопытства!"
    "Нэнси" "Я так тебе благодарна, [gg]! Ты такой классный, такой внимательный парень! Меня переполняют чувства благодарности."
    show GG Smile with my_dissolve
    "[gg]" "Радостно видеть тебя в таком хорошем расположении духа."
    "Нэнси" "Не забудь и про мой подарок, хорошо?"
    "[gg]" "Конечно. Как раз собрался пойти в читальный зал и почитать."
    
    # //GG_Normal движется вправо
    # //GG_Read_B_1
    show GG Normal:
        ease 1 xalign 1.5
    show BiblioGirl Normal:
        ease 1 xalign 1.5
    with None
    scene cg readroom
    show cg_readroom table
    show cg_readroom_lamp
    show cg_readroom_peoples
    show cg_readroom_gg 1
    with my_dissolve #my_fade #TODO а куда my_fade делся?
    
    "[gg]" "Ну вот, наконец-то я смогу ознакомиться с этим фэнтези романом."
    "[gg]" "Хотя..."
    "[gg]" "Очень странные ощущение."
    "[gg]" "Такое чувство, будто бы книга стала ощутимо легче."
    "[gg]" "Она и без того не особо плотная..."
    "[gg]" "Ну и ладно. Какое мне до этого дело? Я собрался читать книгу, а не употреблять её в пищу."
    
    # //Book_Pancu (спрайт с книгой, внутри которой вырезано отверстие и вложены трусики
    show pants_in_book
    
    "[gg]" "Ох... Нэнси-Нэнси!"
    "[gg]" "Какая же ты чертовка, хе-хе-хе."
    
    # //Читальный зал
    # //Спрайты читателей
    scene bg readroom
    
    show GG Normal
    show GG Normal:
        xalign .5
    with my_dissolve
    "[gg]" "Надо её найти, раз уж она так явно подбрасывает намёки."
    
    # //GG_Normal движется вправо
    # //Книжный полки
    # //GG_Normal выезжает слева
    # //Спрайт Biblio_W_Window
    # //Необходимо активировать спрайт Biblio_W_Window #TODO разобрать на две сцены
    # //Window_Biblio_1

    show GG Normal:
        ease 1 xalign 1.5
    with None
    pause 1
    scene bg bookshelves
    with my_dissolve

    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign .85
    show GG Normal
    show GG Normal:
        xalign -.5
        ease 1 xalign .15
    pause 1

    show biblio_cuni pants
    show biblio_cuni pants:
        yalign 2.0
        ease 1 yalign 0
    pause 1
    
    "[gg]" "Я нашёл эти трусики у себя в книге."
    "Нэнси" "Да ну?"
    "Нэнси" "Кому бы они могли пренадлежать?"
    "[gg]" "Чьи бы они не были, подарок-то я не собираюсь возвращать."
    "Нэнси" "Хи-хи-хи."
    "Нэнси" "Но выяснить-то всё равно надо."
    "[gg]" "Этим я и планирую сейчас заняться."
    "Нэнси" "Главное помни правила игры – тихо, нежно, страстно."
    "[gg]" "Постараюсь не забыть..."
    "[gg]" "Я, наверное, единственный посетитель данного заведения, кому ты не позволяешь читать книги."
    "Нэнси" "Интеллект тебя испортит, [gg]."
    "Нэнси" "Хи-хи-хи."
    "Нэнси" "Литература, особенно хорошая, сделаем твой ум скучным и надменным."
    "[gg]" "Эй, не хочешь ли ты сказать, что я глупый?"
    "Нэнси" "Вовсе нет."
    "Нэнси" "Ты привлекательный и весёлый дурачок, хи-хи-хи."
    "[gg]" "Дерзкая девчонка!"
    
    scene bg biblio_cuni
    show biblio_cuni clothed_1
    with my_dissolve
    # //Выбор:
    # //Выбрав первый, после игроку всё равно предоставится второй и наоборот
    python:
        tmp_biblio_18 = 0
    menu:
        "Снять свитер.":
            call biblio_18_sweetear
        "Снять юбку.":
            call biblio_18_skirt
    menu:
        "Снять свитер." if tmp_biblio_18 == 1:
            call biblio_18_sweetear
        "Снять юбку." if tmp_biblio_18 == 2:
            call biblio_18_skirt  
    python:
        del tmp_biblio_18
    

    # //Когда Window_Biblio_2 (цифра абстрактна, но суть такова, что она без юбки и с голыми сиськами)
    
    "[gg]" "Все ответы я знаю и так, Нэнси."
    "[gg]" "Но по регламенту, чтобы у тебя не возникли сомнения в моём профессионализме, я проведу экспертизу полученных улик."
    "Нэнси" "Что ж..."
    "Нэнси" "Приступай к делу, мой хорошенький."
    "Нэнси" "Хочу лицезреть профессионала за работой, хи-хи-хи."
    
    # // Window_Biblio_3 (там в 2 слайда разрывает колготки)
    # // Window_Biblio_3 (пялится на киску)
    show biblio_cuni_gg 3
    with my_dissolve
    show biblio_cuni nude_1
    show biblio_cuni_gg 4
    with my_dissolve
    show biblio_cuni_gg 1
    with my_dissolve
    show biblio_cuni_gg 2
    with my_dissolve

    "[gg]" "Воу!.."
    "[gg]" "Ты очень приятно пахнешь."
    "Нэнси" "С-спасибо."
    "Нэнси" "Меня начинает смущать вся эта пошлость."
    "[gg]" "Занесу твои слова в «протолок», хе-хе."
    "Нэнси" "Пожалуйста, просто сделай то, что собирался..."
    "Нэнси" "Я чувствую себя неловко и, кажется, у меня начинается паника."
    "Нэнси" "Мы слишком заигрались, и боюсь, что сюда кто-то может войти."
    
    # //Kuni_1_anim (анимация куни)
    # //x1
    scene biblio_cuni scenes anim 1 with my_dissolve
    
    "[gg]" "Ох, Нэннси, ты такая сладкая на вкус."
    "[gg]" "Касаться тебя язычком сплошное наслаждение."
    "[gg]" "А этот красивый пучок из волос у твоей киски..."
    "[gg]" "Он делаает тебя ещё более сексуальной."
    
    # //Kuni_2_anim (анимация сиськи вид снизу)
    # //x1

    scene biblio_cuni scenes anim 4 with my_dissolve

    
    "Нэнси" "Боже, [gg], твои комплименты будоражат меня изнутри."
    "Нэнси" "Я так польщена твоими стараниями, что завожусь ещё сильнее."
    "Нэнси" "Продолжай, дурашка, продолжай ласкать мою киску."
    
    # //Kuni_1_anim (анимация куни)
    # //x2
    scene biblio_cuni scenes anim 2 with my_dissolve

    
    "[gg]" "Ты стала такой мокрой, Нэнси."
    "[gg]" "Волнительной, горячей..."
    "[gg]" "Твоё тело покрывается каплями пота, а из твоей киски струятся пахучие соки."
    "[gg]" "Всякий раз, когда твои половые губы касаются моего лица, они нежно щекочут меня волосками."
    "[gg]" "Восхитительно!.."
    
    # //Kuni_2_anim (анимация куни)
    # //x2
    scene biblio_cuni scenes anim 5 with my_dissolve

    
    "Нэнси" "О дааа, [gg]!"
    "Нэнси" "Мне так хорошо с тобой..."
    "Нэнси" "Ты знаешь, как довести женщину до экстаза."
    "Нэнси" "Твой язычок просто чудесный..."
    "Нэнси" "Он так ловко массажирует мою киску, что я едва сдерживаюсь!.."
    "Нэнси" "Только бы не закричать от удовольствия."
    "Нэнси" "И чем больше мне это нравится, тем равнодушнее я становлюсь к последствиям.."
    
    # //Kuni_1_anim (анимация куни)
    # //x3
    scene biblio_cuni scenes anim 3 with my_dissolve

    
    "[gg]" "Значит мне стоит налегать ещё сильнее, иначе ты я буду считать, что выполнил свою задачу не полностью."
    "[gg]" "Я должен довести тебя до экстаза!"
    "[gg]" "Твой клитор уже дрожит, буквально искрясь от радости."
    "[gg]" "Мне лишь остаётся ускориться..."
    "[gg]" "Усилить проникновение вглубь..."
    "Нэнси" "Аххх, [gg]! Я... Я... Кончаю уже в пятыйраз!"
    "[gg]" "О дааа, я чувствую - ты уже на грани. Твоя киска начинает сжимать мой язык, соки заливают мне рот, а твои ляжки стали скользкими от пота."
    
    # //Kuni_2_anim (анимация куни)
    # //x3
    scene biblio_cuni scenes anim 6 with my_dissolve
    
    "Нэнси" "Охххххх!!..."
    "Нэнси" "Только бы не закричать! Только бы не закричать!"
    "Нэнси" "Давай, [gg], скорее, ещё скорее. Уткнись в меня всем лицом!"
    "Нэнси" "Кажется, что я вот-вот..."
    "Нэнси" "Я хочу сделать сквирт!.. Да! Это случится. Прям  сейчас!.."
    
    # //Кончить
    # //Kuni_1_END_anim (кончает) #TODO честно хз тут наверное еще всякие детали должны быть
    
    "Нэнси" "Аффффффффф!!!...."
    "Нэнси" "Даааааааааа!!!"
    "Нэнси" "Какое блаженство, [gg]!.."
    "Нэнси" "Я тебя обожаю..."
    "[gg]" "Мне тоже понравилось."

    with hpunch
    
    # //Книжные полки
    # // GG_ Surprise
    # // BiblioGirl_Surprise
    # //Симп выезжает слева

    scene bg bookshelves
    show GG Normal
    show GG Normal:
        xalign .70
    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign .90
    with my_dissolve
    with vpunch
    #TODO А какой спрайт у симпа?
    
    "Симп" "Эй, что здесь за шум?!"
    "Симп" "Кого-то убивают?"
    show BiblioGirl Surprise with my_dissolve
    "Нэнси" "Мы... Я..."
    "[gg]" "Всё в порядке, приятель. Мы просто перебирали книгу, и одна из них оказалась достаточно... редкой."
    show BiblioGirl Embarrassment with my_dissolve
    "Симп" "Я вам не верю. Здесь пахнет сексом!"
    show GG Angry with my_dissolve
    "[gg]" "Чувак, но ты же не думаешь, что мы должна оправдываться перед тобой?"
    show GG Smile with my_dissolve
    "[gg]" "Пойдём, Нэнси. У нас хватает своих забот."
    show BiblioGirl Smile with my_dissolve
    "Нэнси" "Ага. Пошли."
    
    # //Оба спрайта едут влево
    # //Библиотека Хол
    # //Оба спрайта выезжают справа

    show GG Normal:
        ease 1 xalign -.5
    show BiblioGirl Normal:
        ease 1 xalign -.5
    with None
    call show_bg_image_label
    with my_dissolve #my_fade #TODO а куда my_fade делся?
    show GG Normal
    show GG Normal:
        xalign 1.5
        ease 1 xalign .85
    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign 1.5
        ease 1 xalign .15
    pause 1
    
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Чуть не попались!"
    show GG Normal with my_dissolve
    "[gg]" "Этого следовало ожидать. Мы переступаем черту, хе-хе."
    "Нэнси" "Согласна. И нам, наверное, пора остановиться."
    show GG Chagrin with my_dissolve
    "[gg]" "Но ведь мы можем встречаться в другом месте, в другое время..."
    # show BiblioGirl Chagrin with my_dissolve
    "Нэнси" "Тогда в наших встречах не будет ничего интересного."
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Обычный, ничем не примечательный роман и скорое затухание чувство от однообразия."
    "[gg]" "Значит, это и была последняя наша встреча?.."
    "Нэнси" "Не знаю..."
    "[gg]" "Твоя неопределённость меня убивает."
    # show BiblioGirl Smile with my_dissolve
    "Нэнси" "Ага. Я просто плыву по течению. И тебе советую."
    "[gg]" "...."
    
    $ events.pop("biblio_18", 0)
    $ Event("biblio_19", day_start=time.day_now+1, location = "City_library")
    
    jump main_interface_label

label biblio_18_sweetear:
    if tmp_biblio_18:
        show biblio_cuni boobs_2
        with my_dissolve
    else:
        show biblio_cuni boobs_1
        with my_dissolve   

    python:
        tmp_biblio_18 = 2
    "[gg]" "О да..."
    "[gg]" "У тебя потрясающие формы, Нэнси."
    "[gg]" "Огромные, сладкие персики и впалые соски выглядят роскошно..."
    "Нэнси" "И вульгарно, хи-хи-хи."
    "Нэнси" "Они скучают по тебе, [gg]."
    "Нэнси" "Любят, когда на них смотрят такими голодными глазами."
    "Нэнси" "Но ещё больше, я люблю голодные допросы, хи-хи-хи."
    return
label biblio_18_skirt:
    if tmp_biblio_18:
        show biblio_cuni boobs_2
        with my_dissolve
    else:
        show biblio_cuni clothed_2
        with my_dissolve   
    python:
        tmp_biblio_18 = 1
    "[gg]" "Ха, а вот и место, откуда пропали трусики."
    "[gg]" "Эти колготки не скрывают, а лишь подчёркивают красотку твоей губастой киски."
    "[gg]" "Я с трудом могу оторвать взгляд... Слишком... Привлекательно."
    "Нэнси" "Из тебя получился бы отличный детектив, [gg], хи-хи-хи."
    "Нэнси" "Не желаешь ли провести дознание свидетеля? С пристрастием..."
    return
