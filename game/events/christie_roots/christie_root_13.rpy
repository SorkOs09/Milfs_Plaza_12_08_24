label christie_root_13:
    call show_bg_image_label from _call_show_bg_image_label_141
    $ events.pop("christie_root_13", 0)
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

    show GG Smile
    show GG Smile at go_from_left

    "[gg]" "Ну как ваши успехи, бизнесмены? "
    show GG Smile:
        xalign .15
    with my_dissolve
    "[gg]" "Получилось собрать деньги с подписчиков?"
    "Джей" "Знаешь…"
    "Джей" "Мне кажется, мир ещё не готов к гетеросексуальной мужикам, что не стесняются своего тела."
    "Джей" "Но сделка есть сделка. "
    "Джей" "Вот твоё кофе, чувак. Последняя баночка, знаешь ли."
    show GG Laughs
    "[gg]" "Я бы рад сказать, что ценю наше сотрудничество, но, боюсь, что это не так."
    "Джей" "Это удар в самое сердце, мудило!"
    show GG Normal
    "[gg]" "Но вы сдержали слово, и каждый получил то, что хотел. "
    show GG Normal
    "[gg]" "Спасибо. "
    "Джей" "Ага-ага. Пошли мы нахер."



    $ add_to_inventory(name = 'Кофе «Релакс»')

    show screen give_item_screen(i_path+'/items/coffe.png', _('Кофе «Релакс»'), ['Колумбийски зёрна', 'наивысшего качества.'])
    with Dissolve(.75)

    $ renpy.pause(1, hard = True)

    $ renpy.pause(9999)





    hide screen give_item_screen
    hide Jay
    hide Bob
    show GG Think
    with Dissolve(.5)

    $ renpy.pause(.5)

    show GG:
        ease .5 xalign .5

    "[gg]" "Теперь мне следует оставить банку с кофем на кухне до того, как туда явится Кристи."
    show GG Think:
        xalign .5
    with my_dissolve
    "[gg]" "Лучше сделать это Днём, Вечером или даже Ночью."
    show GG Think
    "[gg]" "Хочу, чтобы это было сюрпризом."
    show GG Think
    "[gg]" "Утром Кристи придёт завтракать и будет приятно удивлена, что её любимое кофе вновь на месте."



    python:
        location_now = "City_Shop"
        descript_Christie= _("Положить банку кофе на кухню, пока там нет Кристи: Днём, Вечером или Ночью.")
        locations['Kitchen'].image_buttons_times = copy.deepcopy(locations['Kitchen'].image_buttons_times)
        for i in ('afternoon', 'evening', 'night'):
            if i not in locations['Kitchen'].image_buttons_times:
                locations['Kitchen'].image_buttons_times.update({i:{}})
            locations['Kitchen'].image_buttons_times[i].update({"coffe_50_percent":Jump('christie_root_14')})




    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
