label christie_root_59:
    
    $ events.pop('christie_root_59', 0)

    call show_bg_image_label from _call_show_bg_image_label_222
    show Jay Normal
    show Jay Normal:
        xalign .35
        ypos 1085
        zoom 1.0-0.035
        xalign .65
    show Bob Normal
    show Bob Normal:
        xalign .65
        ypos 1085
        zoom 1.0-0.035
        xalign .95
    with Dissolve(.5)

    show GG Think
    show GG Think at go_from_left
    #Купить красивую корзину, куда можно будет положить бутерброды и салат. Но что-то мне подсказывает, в магазине я вряд ли её смогу найти.
    #"ext" "Активировать JayBob"
    
    "[gg]" "Эй, ребята, я понимаю, вопрос может показаться странным и даже абсурдным, но… возможно, вы знаете, где приобрести корзину для пикника?"
    "Зудило" "Мать твою, чувак! Мы кто по-твоему? Корзинщики и мастера-лозоплетельщики?!"
    show GG:
        xalign .15
    with my_dissolve
    "[gg]" "Тогда откуда вы знакомы с такими определениями? "
    "Бубнило" "……"
    "Зудило" "Перед тем как влиться в струю фарцовщиков (струя мне за щеку!), Бубнило ходил в кружок плетения, где, собственно, плёл и корзины в том числе. "
    "Зудило" "Но в основном шляпы. Чудные пляжные шляпы. Как у мексиканцев или монахов Шаолиня."
    "Бубнило" "……"
    show GG Normal
    with my_dissolve
    "Зудило" "Так что, в принципе…. Если тебе очень надо, а Бубнило сильно постарается, то, возможно, что-то и может получиться. "
    "[gg]" "Снова услуга?"
    "Зудило" "Зришь в корень! "
    "Зудило" "В наше время экономических кризисов, нестабильного рынка и бесконечной инфляции, только бартер является самой надёжной бизнес моделью. "
    "[gg]" "Ну говори уж, бизнесмен хренов."
    "Зудило" "Реклама."
    "[gg]" "Реклама?"
    "Зудило" "Да, чёрт тебя дери, сраная реклама."
    "Зудило" "В последнее время у нас много конкурентов."
    "Зудило" "Основная тусовка обосновалась в гетто. Копы их не трогают, место рыбное. Они демпингуют цены и все обрыганы и укурыши идут к ним. "
    "Зудило" "К тому же, они парят откровенное дерьмо. Практически песок из кошачьего туалета и газон из-под подошвы. "
    "Зудило" "А у нас – высший сорт. "
    "Зудило" "Нам нужно, чтобы ты устроил небольшую рекламную акцию в том районе, ну а мы, понятное дело, отблагодарим в лучшем виде."
    "Зудило" "Бубнило изготовит тебе такую корзину, едрить её в корень, что ты туда армейский склад поместить сможешь, ещё и для парочки боевых вьетконговцев место останется. Сечёшь? "
    "Бубнило" "….."
    "[gg]" "Заманчиво. Так что конкретно от меня требуется? "
    "Зудило" "В интернете я вычитал, что лучший пиар это чёрный пиар, а лучший чёрный пиар – антипиар!"
    "[gg]" "Ты что, собираешься мне лекцию по маркетингу зачитать? "
    "Зудило" "Я довожу до тебя суть, чувачело!"
    "Зудило" "Всё, что тебе надо – это постоять кое-какое время в гетто с плакатом."
    "[gg]" "А что будет на плакате?"
    "Зудило" "Информация."
    "[gg]" "Какая информация?"
    "Зудило" "Ну… Там будет изображён плохой продавец с соответствующей пометкой."
    "[gg]" "И как быстро мне вырвут кадык?"
    "Зудило" "Вот и узнаем, хе-хе."
    "Зудило" "Тебе нужна корзина, а нам – пиар! "
    "[gg]" "Думаете, если местные говноеды взглянут этот плакат, они сразу побегут к вам? "
    "Зудило" "Не сразу, но как минимум усомнятся в честности местного барыги. И начнут искать новых поставщиков."
    "Зудило" "А это мы! Мы – ближайшие конкуренты. Так или иначе, они найдут нас, что и приведёт наш бизнес к успеху."
    "Зудило" "И да, ВАЖНОЕ ЗАМЕЧАНИЕ – ни в коем случае не попадайся на глаза местным «смотрящим»."
    "Зудило" "Это суровые на вид бугаи, что охраняют барыг от ограбления или, в крайнем случае – от фараонов."
    "[gg]" "Дай-ка я всё осмыслю."
    "[gg]" "Я должен отправиться в гетто и постоять там с вашей «афишей», после чего вернуться к вам и забрать свою корзину. Верно?"
    "Зудило" "Шаришь, братишка! "
    "[gg]" "Ладно, гоните плакат, чудилы."
    "Зудило" "Вот, смотри не сломай. Бубнило может огорчиться, он лично рисовал."
    "[gg]" "Ха! Да я гляжу, у Бубнило творческая натура."
    "Зудило" "Абсолютно. "
    "Зудило" "В детстве он прибился к бродячим художникам.… или это были цыгане? Не помню, короче."
    "Зудило" "Вот и отразилось на моём кореше."
    "[gg]" "Мгу…"

    call show_additional_images_label from _call_show_additional_images_label_110
    hide Jay
    hide Bob
    show shadow_full
    show GG Think
    with my_dissolve
    "[gg]" "{i}Задание предельно простое, хотя и крайне рискованное.{/i}"
    
    "[gg]" "{i}Но корзина мне нужна и.. вроде как, не так уж и много от меня требуется.{/i}"
    
    
    
    
    $ descript_Christie = __("Отправиться в Гетто Утром или Днём с плакатом, полученным от Зудилы и Бубнилы.")
    $ unlock_city_getto = True

    $ Location(
        'City_Getto',
                    buttons = []
                    )

    $ Event("christie_root_60", "City_Getto", time = ["morning", "afternoon"])


    jump main_interface_label