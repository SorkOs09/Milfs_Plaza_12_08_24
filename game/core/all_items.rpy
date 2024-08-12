
init -50 python:
    all_items = [


    Item(_('Продукты для пикника'), ['Отлично подходят чтобы устроить пикник!'], i_path+'/items/picnic_foods.png', NullAction(), item_id = 57),

    Item(_('Корзинка'), ['Крошечная плетёная корзинка'], i_path+'/items/korzinka.png', NullAction(), item_id = 61),


    Item(_('Отмычка'),      ['С помощью этого инструмента я смогу', 'проникать в некоторые закрытые двери.'], i_path+'/items/unlocker.png', NullAction()),

    Item(_('Слабительное'),  ['Слабительное'], i_path+'/items/laxative.png', NullAction()),

    Item(_('Кикбоксёр'),  ['Отличный фильм для', 'просмотра с любимым человеком.'], i_path+'/items/boxer.png', NullAction()),


    Item(_('Анальная пробка'), ['Сексуальная игрушка, предназначенная','Для введения в анальное отверстие.', 'Подарить её можно только Марине', 'После завершения сюжета.'],      i_path+'/items/plug.png', NullAction()),

    Item(_('Перцовый баллончик'), ['Помогает от неприятностей.'], i_path+'/items/perec.png', NullAction(), item_id = 10),

    Item(_('Закуска для пикника'), ['Я готовил это весь день!'], i_path+'/items/sandwitch.png', NullAction(), item_id = 58),

    
    
    Item(_('«Неизвестный» костюм для ролевых игр'), ['Выглядит просто отлично'], i_path+'/items/costume_0_9.png', NullAction(), item_id = 51),

    

    Item(_('Резак'), ['Прекрасное решение', 'для различных отверстий'], i_path+'/items/rezak.png', NullAction(), item_id = 11),

    Item(_('Дон Кихот'), [_('Подарочное издание'), 
        _('«Дон Кихот» Мигеля Де Сервантеса.')], i_path+'/items/don_kihot.png', NullAction(), item_id = 22),


    Item(_('Отвертка'), [_('Отличный инструмент'),], i_path+'/items/screwdriver.png', NullAction(), item_id = 33),


    Item(_('Реферат'), ['Реферат по «Обществознанию»'],      i_path+'/items/referat.png', NullAction()),


    Item(_('Костюм 1'), ['Костюм'],      i_path+'/items/costume_1.png', NullAction()),

    Item(_('Костюм 2'), ['Костюм'],      i_path+'/items/costume_2.png', NullAction()),

    Item(_('Красное вино'), ['Красное вино'],      i_path+'/items/wine.png', NullAction()),

    Item(_('Чёрные очки'), ['Чёрные очки'],      i_path+'/items/black_glasses.png', NullAction()),
    
    Item(_('Костюм Харли Квин.'), ['Костюм Харли Квин.'],      i_path+'/items/costume_harly.png', NullAction()),
    
    
    
    Item(_('Духи Марины'), ["Флакон с приторно-сладким ароматом фиалок"],      i_path+'/items/duhi.png', NullAction()),
    
    Item(_('Магические часы'), ['Магические-часы, 1 ур.'],   i_path+'/items/magic_clock_1.png', NullAction()),
    Item(_('Бинокль'),        ['Бинокль'],           i_path+'/items/binoculars.png', NullAction()),

    Item(_('Мощный Бинокль'), ['Как обычный, но мощнее!'], i_path+'/items/binoculars.png', NullAction()),

    Item(_('Фильм "Лолита"'), ['Отличный фильм для', 'просмотра с любимым человеком.'],           i_path+'/items/lolita.png', NullAction()), 
    
    Item(_('Лейка'), ['Сосуд для', 'поливки растений.'],           i_path+'/items/watering_can.png', NullAction()),

    Item(_('Кофе «Релакс»'), ['Колумбийски зёрна', 'наивысшего качества.'],           i_path+'/items/coffe.png', NullAction()),


    Item(_('Реферат «Обществознание» 1/3'), ['Мой собственный многочасовой', 'интеллектуальный труд.'],      i_path+'/items/referat_2.png', NullAction()),


    Item(_('Реферат «Обществознание» 2/3'), ['Мой собственный многочасовой', 'интеллектуальный труд.'],      i_path+'/items/referat_2.png', NullAction()),


    Item(_('Реферат «Обществознание» 3/3'), ['Мой собственный многочасовой', 'интеллектуальный труд.'],      i_path+'/items/referat_2.png', NullAction()),


    Item(_('Камасутра'), ['Древнеиндийский трактат,', 'посвящённый теме эмоциональной жизни,', 'влечения и любви.'],      i_path+'/items/camasutra.png', NullAction()),



    Item(_('Растение'), ["Неизвестный сорт."],           i_path+'/items/ep5_tree.png',     NullAction()),

    Item(_('Растение в горшке'), ["Обычное растение в горшке."],           i_path+'/items/ep5_tree_2.png',     NullAction()),

    Item(_('Товар'), ["Товар для продажи."],           i_path+'/items/drug.png',     NullAction(), max_quant = 35),

    Item(_('Купон «кекса»'), [_('Коллекционный купон.'), _('Но сейчас эта самая ходовая валюта на чёрном рынке.')],           i_path+'/items/keks.png', NullAction(), max_quant = 10),

    Item(_('Трусики Кристи'), ['Женское нижнее бельё.'],           i_path+'/items/kristy_pants.png', NullAction()),
    
    Item(_('Солнечное масло'), ['Это можно использовать в качестве смазки для петель двери'],           i_path+'/items/solar_oil.png', NullAction()),
    
    Item(_('Шпилька'),        ['Из трех таких можно сделать отмычку'],           i_path+'/items/hairpin.png', NullAction()),
    

    Item(_('Попкорн'),        ['Попкорн'],           i_path+'/items/corn.png', NullAction()),

    Item(_('Яблоко'),        ['Восстанавливает 10 сытости.'],           i_path+'/items/apple.png', eat_apple),

    Item(_('Телефон'),        ['Обыкновенный смартфон.'],           i_path+'/items/phone.png', NullAction()),

    Item(_('Телефон Продавщицы'), ['Обыкновенный смартфон.'],           i_path+'/items/phone.png', NullAction(), item_id = 40),



    Item(_("Букет роз"),        ["Собранные вместе цветы для подарка."],           i_path+'/items/buket.png', NullAction()),

    Item(_("Роза"),        ["Красивый, пахучий цветок бордового цвета."],           i_path+'/items/flower.png', NullAction()),

    Item(_("Билеты"),        ["Театральные билеты на постановку «Кошки»."],           i_path+'/items/ticket.png', NullAction()),

    Item(_('Резиновые перчатки'), [_('Оберегают руки при работе в хозяйственной сфере и не только.')], i_path+'/items/gloves.png', NullAction()),

    Item(_('Бейсбольная бита'), [_('Бейсбольная бита'), _('для пробивания человеческих черепов.')], i_path+'/items/bita.png', NullAction()),


    Item(_('Сильверболлер'), [_('Говорят, это оружие'), _('пользуется спросом у наёмных убийц.')], i_path+'/items/gun.png', NullAction()),



    Item(_('Букет из милых цветков'), [_('Прекрасный букет из бежевых цветов,'), _('который можно кому-нибудь подарить.')], i_path+'/items/search_flower_buket.png', NullAction()),

    Item(_('Милый цветок'), [_('Из 7 таких цветков можно будет сложить'), _('букет и кому-нибудь подарить.')], i_path+'/items/search_flower.png', NullAction()),

    Item(_('Шоколад'), [_('Вкусный шоколад, который может'), _('порадовать какую-нибудь женщину.'), 
        _('Так же его можно скушать самому'), _('и восполнить 30 ед. Сытости.')], i_path+'/items/chocko.png', eat_chocko),
 
    Item(_('Йогурт'), [_('Восстанавливает 30 ед. Сытости.')], i_path+'/items/yogurt.png', eat_yogurt),


    Item(_('Чипсы'), [_('Восстанавливает 20 ед. Сытости.')], i_path+'/items/chips.png', eat_chips),
    
    Item(_('Сок'), [_('Восстанавливает 10 ед. Сытости.')], i_path+'/items/juice.png', eat_juice),
 



    ] 
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
