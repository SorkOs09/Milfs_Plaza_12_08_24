label christie_root_46:
    #Description: Сходить к Игорю к Парк и попросить его взломать телефон продавщицы. 
    # "A Task" ""
    # #Активировать Игоря в Парке
    if getattr(store, 'block_igor_position', False):

        $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")

        $ events['christie_root_46'].day_start = time.day_now + 1
        jump main_interface_label
    # "Scene" ""
    $ events.pop('christie_root_46', 0)
    #//Парк

    call show_bg_image_label from _call_show_bg_image_label_188

    show Igor Normal
    show Igor Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left
    
    "[gg]" "Привет, Игорь."
    show Igor Normal
    "Игорь" "Привет."
    
    show GG:
        xalign .15
    with my_dissolve
    "Игорь" "Я всё думаю, когда, наконец, так произойдёшь, что это я к тебе заскочу в гости, а ты в этот момент… ну не знаю, посуду моешь, пылесосишь ковёр или, хотя бы, стираешь пыль со стола?"
    show GG Normal
    "[gg]" "Ты ведь сам предложил пахать вместо меня. Давай метлу, форму. Ворвусь в клининг с двух ног!"
    show Igor Normal
    "Игорь" "Да пошёл ты, [gg]. Это нотки житейского бытия. Эхо рабочего класса, понял, да?"
    show GG Normal
    "[gg]" "Понял-понял, мой боец с капитализмом. Я с делом."
    show Igor Normal
    "Игорь" "Как будто бывает по другому. "
    show GG Normal
    "[gg]" "Недавно я приносил тебе видео-свидетельства о том, как продажный коп берёт взятку."
    show Igor Normal
    "Игорь" "Ага."
    show GG GivePhone
    "[gg]" "Теперь я добыл кое-что покруче. Телефон его любовницы."
    show Igor Normal
    "Игорь" "Охренееееееть!"
    show Igor Normal
    "Игорь" "И чо там?! Жарево?!"
    
    "[gg]" "А вот это тебе и предстоит выяснить. "
    show GG Normal
    "[gg]" "Взломай пароль и поведай о содержании. Очень и очень надо."
    show Igor Normal
    "Игорь" "Хм…"
    show Igor Normal
    "Игорь" "Я, конечно, никогда не прочь придушить змея на горячие сливы «хоум видео», но взломать пароль телефона?"
    show Igor Normal
    "Игорь" "Ёптвою мать, я ж хакер, который Пентагон по выходным ломает. "
    show Igor Normal
    "Игорь" "Обладай я такими навыками, на кой хер мне вообще пришлось бы ввязываться в азартные игры, а?!"
    show GG Normal
    "[gg]" "Ты ввязываешься в них не по причине глупости, а по причине азарта. Ты ебанутый как и я, вот и всё."
    show Igor Normal
    "Игорь" "Ладно, почитай гайды в интернетах. Может чего и получится. Обещать не могу."
    show GG Normal
    "[gg]" "Нет, чувак. Мне кровь из носа нужно содержание этого телефона."
    show Igor Normal
    "Игорь" "Зачем? У нас есть видеофакт с его преступлением. Мы хоть сегодня можем шантажировать его или отправить видос в полицию."
    show Igor Normal
    "Игорь" "А зарабатывать себе геморой на жопу ради потрахушек тупого мента? Не понимаю. Просто не понимаю."
    show GG Normal
    "[gg]" "Думай как хочешь. Нужно и всё."
    show Igor Normal
    "Игорь" "Хорошо. Ты хочешь затруднить меня, я затрудню тебя."
    show GG Normal
    "[gg]" "Новую фоточку Кристи? Окей."
    show Igor Normal
    "Игорь" "Ха! Разбежался!"
    show Igor Normal
    "Игорь" "Тут работы с устройством непочатый край. Одной фоточки будет маловато."
    show GG Normal
    "[gg]" "Хорошо, давай сделаю несколько."
    show Igor Normal
    "Игорь" "Соблазнительно, но нет. Мои аппетиты возросли. Последним снимком ты слишком раззадорил меня, чувак. "
    show Igor Normal
    "Игорь" "Я хочу видео."
    show GG Surprise
    "[gg]" "Видео?!!"
    show Igor Normal
    "Игорь" "Ага. И в нормальном качестве. "
    show Igor Normal
    "Игорь" "Сними её где-нибудь в душе, пока она моется, или в комнате, когда она раздевается перед сном. "
    show Igor Normal
    "Игорь" "Короче говоря, что-то, что можно было бы истолковать эротическим. "
    show Igor Normal
    "Игорь" "И не вздумай мне снимать её пока она спит, отдыхает, или просто нежится в ванной. Мне это не интересно. "
    show Igor Normal
    "Игорь" "Нужно действие, понимаешь?"
    show GG Normal
    "[gg]" "Крышей поехал?"
    show Igor Normal
    "Игорь" "Ты просишь меня взломать сраный телефон ради потрахушек мента с его любовницей, а крышей поехал я?! "
    show GG Normal
    "[gg]" "Ладно, сделаю."
    show Igor Normal
    "Игорь" "Что, серьёзно?"
    show GG Normal
    "[gg]" "Ты чо, брал меня на «слабо»?"
    show Igor Normal
    "Игорь" "Нет, я просто не думал, что ты сможешь. "
    show Igor Normal
    "Игорь" "Сколько я тебя знаю, а я знаю я тебя предостаточно, раз уж ты согласился на афёру, это значит только одно - ты уверен в том, что сможешь её выполнить."
    show Igor Normal
    "Игорь" "Вот я и поражаюсь. Как, чёрт возьми, ты сможешь добыть мне такое клёвое видео?"
    show GG Normal
    "[gg]" "Оставь эти заботы мне. "
    show Igor Normal
    "Игорь" "Понял-понял. Гудини своих секретов не раскрывает. "
    show Igor Normal
    "Игорь" "Тогда до встречи. Теперь мне есть ради чего жить!"
    show GG Normal
    "[gg]" "Чудила. "
    
    scene black with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    
    call christie_root_try_to_del_descript_christie_block_igor from _call_christie_root_try_to_del_descript_christie_block_igor_3
    
    #Tian_47
    $ descript_Christie = _("Заснять Кристи в Душе, когда она моется или Ночью в её комнате, во время переодевания.")
    
    $ sister_position['afternoon'] = ['Restroom', 'sister_restroom']

    
    $ remove_from_inventory_by_id(40)
    
    $ block_change_milf_position_christie_root_46 = copy.deepcopy(block_change_milf_position)    
    $ block_milf_home_christie_root_46 = copy.deepcopy(block_milf_home)

    $ block_change_milf_position = True
    $ block_milf_home = True
    

    $ Event('christie_root_47_sister_room', location = 'Sister_Room', time = ['night', ])

    $ Event('christie_root_47_restroom', location = 'Restroom', time = ['afternoon', ])

    $ time.time_forward()

    jump main_interface_label