label biblio_17:
    # Description: Нужно придумать, что подарить Нэнси. Если уж я сам не смогу додуматься, то следует поспрашивать знакомых.
    # Task: Активировать спрайт Таинственный продавец в гетто.
    
    call show_bg_image_label
    show Jay Silence
    show Jay Silence:
        ypos 1085
        xalign .65
    show Bob Normal
    show Bob Normal:
        ypos 1085
        xalign .95
    show GG Normal
    show GG Normal at go_from_left(xxalign = .15)
    with my_dissolve
    
    "[gg]" "Привет, парни."
    "Зудило" "Ёу, [gg]!"
    "Зудило" "Тебе снова нужен синхрофразатрон? Детали от атомного реактора? Или волшебный цветок, что растёт на краю земли одну ночь в году?"
    show GG Smile with my_dissolve
    "[gg]" "Всего лишь подарок для очень необычный, загадочной девушки."
    "Зудило" "Ха, ты по адресу, чувачело! Я эксперт по пикапу."
    "Зудило" "Если ты только начали встречаться – подари ей какую-то безделушку или конфеты, а если какое-то время вместе – свежую модель телефона."
    "Зудило" "Это база, чувак!"
    show GG Normal with my_dissolve
    "[gg]" "Ну..."
    "[gg]" "Она не совсем моя девушка."
    "[gg]" "Да и в целом довольно самобытная личность."
    "Зудило" "Херня это всё, чувак."
    "Зудило" "Делай как я говорю и всё сработает, словно по часам."
    "Зудило" "Если, конечно, ты не во фрэндзоне. Тогда это бесполезная трата времени и денег."
    "[gg]" "Спасибо за совет, пацаны."
    "[gg]" "Попробую уж сам."
    $ events.pop("biblio_17", 0)
    $ unlock_city_getto = True
    
    $ Location(
        'City_Getto',
                    buttons = []
                    )
    $ locations['City_Getto'].image_buttons["secretman"] = Jump("biblio_18_secretman")

    $ location_now = "City_Shop"


    jump main_interface_label

label biblio_18_secretman:
    # //При активации Таинственного продавца
    
    "SecretMan" "Псссс, парень. Подойди сюда."
    show GG Surprise with my_dissolve
    "[gg]" "А?.."
    "SecretMan" "Я знаю... Я хорошо знаю этот взгляд полоумного дебила, который не знает, как совладать с женщиной."
    show GG Angry with my_dissolve
    "[gg]" "Пошёл ты нахер, мудило!"
    "[gg]" "Ты что, нарываешься на неприятности?"
    "SecretMan" "Вовсе нет. Я хочу предложить тебе что-то, что наверняка понравится тебе и твоей даме."
    show GG Surprise with my_dissolve
    "[gg]" "Что ты имеешь в виду?"
    "SecretMan" "Ты ведь ищешь подарок, верно?"
    "[gg]" "Откуда ты знаешь?!"
    "SecretMan" "Потому что я сам тебя искал, [gg]."
    show GG Angry with my_dissolve
    "[gg]" "И давно ты следишь за мной?"
    "SecretMan" "Достаточно, чтобы выяснить, как сильно ты нуждаешься в моей помощи."
    show GG Skepticism with my_dissolve
    "[gg]" "Ну хорошо..."
    "[gg]" "Сделаю вид, что заинтригован. Что ты можешь предложить?"
    "[gg]" "Лава-лампу или книгу-почемучку?"
    "SecretMan" "Ээээ нет, приятель. Мы же говорим о чём-то «особенном»."
    "SecretMan" "Этот подарок, который уготовлен исключительно для твоей возлюбленной."
    "[gg]" "Вообще-то, мы просто друзья."
    "SecretMan" "Не важно, [gg]."
    "SecretMan" "Возьми эту коробочку."
    "SecretMan" "Сама по себе она не представляет никакой ценности. Это всего лишь шкатулка, внутри которой и содержится настоящий приз."
    "SecretMan" "Уверяю, твоя дама не останется равнодушной."
    "[gg]" "Хм..."
    show GG Normal with my_dissolve
    "[gg]" "Что там внутри? И как её открыть?"
    "SecretMan" "Шкатулка закрыта на замок-пазл."
    "SecretMan" "Чтобы взломать её, тебе придётся изрядно потрудиться, но для человека, который любит разгадывать тайны, это сущий пустяк."
    "SecretMan" "Будь уверен, [gg], что тот, для кого предназначена эта вещь, без проблем доберётся до содержимого."
    show GG Skepticism with my_dissolve
    "[gg]" "И сколько с меня?"
    "SecretMan" "150 долларов."
    show GG Normal with my_dissolve
    "[gg]" "Чёрт! Дорого!"
    "[gg]" "И слишком подозрительно."
    show GG Skepticism with my_dissolve
    "[gg]" "А если внутри коробки окажется сибирская язва?"
    "SecretMan" "Там может оказаться и отрезанный палец."
    "SecretMan" "Но пока не купишь – не узнаешь."
    show GG Normal with my_dissolve
    "[gg]" "Ладно, я тебя понял."
    "SecretMan" "Ну так что, покупаешь?"

    jump biblio_17_buy_menu

label biblio_17_buy_menu:

    # //Варианты ответов
    # 1.	Да (если есть 150 долларов)
    # 2.	Нет сейчас (если нет 150 долларов)
    # //Итог 2 варианта
    
    
    
    # //Квест остаётся прежним
    # //При повторной активации SecretMan
    
    
    menu:
        "Да" if money >= 150:
            "SecretMan" "Хорошая сделка."
            "[gg]" "Я на это очень надеюсь."
            
            show screen give_item_screen(i_path+'items/ticket.png', _('Волшебный коробок'), _('Какая-то шкатулка с замком-пазлом.'))
            pause #TODO Себе напоминаю что нужно добавить предмет в инвентарь
            hide screen give_item_screen

            python:
                Event("biblio_18", location = "City_Library_BiblioGirl", time=["morning", "afternoon"], button_name="Подарить коробку")
                time.time_now = "evening"
                locations['City_Getto'].image_buttons["secretman"] = NullAction() #TODO Или его вообще с локации убрать?

        "Не сейчас":
            "SecretMan" "Возвращайся, когда будешь готов купить шкатулку."
            $ locations['City_Getto'].image_buttons["secretman"] = Jump("biblio_17_repeat")
    jump main_interface_label
    

label biblio_17_repeat:
    "SecretMan" "Ну так что, покупаешь шкатулку?"
    jump biblio_17_buy_menu

    
    
    
