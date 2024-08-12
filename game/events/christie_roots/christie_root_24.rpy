
























































































label christie_root_24:

    $ events.pop('christie_root_20', 0)
    "Библиотекарша" "Вы снова у нас!"

    "Библиотекарша" "Я знала, что вы вернётесь."
    show GG Normal
    "[gg]" "Да? И почему же?"

    "Библиотекарша" "К нам все возвращаются, хи-хи-хи."
    show GG Smile
    "[gg]" "Ха-ха. Вы очень приветливы."

    "Библиотекарша" "Наверное потому, что я очень люблю комплименты."
    show GG Smile
    "[gg]" "У меня их с избытком, всегда готов поделиться. "

    "Библиотекарша" "Хи-хи-хи."
    show GG Normal
    "[gg]" "Могу я пройти в читальный зал и получить от вас те же книги по «Обществознанию»?"

    "Библиотекарша" "Разумеется."


    show BiblioGirl:
        ease 1 alpha 1.0
    show GG:
        ease 1 xalign 1.5
    $ renpy.pause(1.5, hard = True)
    scene black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    scene expression "images/cg/christie_root/library/afternoon.png"
    with Dissolve(.5)

    $ renpy.pause(.5)
    scene expression "images/cg/christie_root/library/morning_gg.png"
    with my_dissolve






    "[gg]" "Пару слов об этом, пару слов о том…"
    "[gg]" "Аналитические выкладки, статистика, реакция на это общественного мнения."
    "[gg]" "Абзац, ещё один абзац, заметка о важном… Что ж, кажется этого достаточно на сегодня."

    scene expression "images/cg/christie_root/library/evening.png"
    with Dissolve(.5)

    $ renpy.pause(.5)
    scene expression "images/cg/christie_root/library/evening_gg.png"
    with my_dissolve


    "[gg]" "Работа близится к завершению…"
    "[gg]" "Главное не забыть упомянуть об основах культурологии и кое-каких издержках субъективного изложения, но об этом уже в следующий раз."
    "[gg]" "На сегодня я полностью истощён и совсем не хочу ломать голову."


    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign -0.5
        xzoom -1
        easein_cubic 1 xalign .15





    "Библиотекарша" "Вы всегда работаете на износ? "
    scene expression "images/cg/christie_root/library/evening.png"

    show GG Normal
    show GG Normal:
        xalign .85
        xzoom -1


    with my_dissolve



    "[gg]" "Хех… Сейчас моя жизнь полна перемен, и такая работа, вероятно, издержки данного явления."

    show BiblioGirl Normal
    show BiblioGirl Normal:
        xzoom -1
        xalign .15

    with my_dissolve
    "Библиотекарша" "Берегите себя. "

    "Библиотекарша" "Библиотека – дом знаний, а не кладбище трудоголиков. "
    show GG Normal
    "[gg]" "Спасибо за совет, постараюсь выжить. "





    show GG:

        ease 1.2 xalign -1.5
    show BiblioGirl:
        xzoom 1
        ease 1.2 xalign -1.5
    $ renpy.pause(1.5, hard = True)




    scene black with Dissolve(.5)

    call show_bg_image_label from _call_show_bg_image_label_135







    $ remove_from_inventory(name = 'Реферат «Обществознание» 1/3')
    $ add_to_inventory(name = 'Реферат «Обществознание» 2/3')
    play sound 'audio/get_item.ogg'
    show screen give_item_screen(i_path+'/items/referat_2.png', _('Реферат «Обществознание» 2/3'), ['Мой собственный многочасовой', 'интеллектуальный труд.'])
    with Dissolve(.75)

    $ renpy.pause(1, hard = True)

    $ renpy.pause(9999)








    hide screen give_item_screen


    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)










    scene black with Dissolve(.5)
    $ time.time_now      = "night"
    $ location_now       = "City_Home"








    $ descript_Christie_tmp_0 = __("1. Отправиться в библиотеку и продолжить написание реферата по теме «Обществознание» (2/3).")

    $ descript_Christie     = str(descript_Christie_tmp_0) + "\n" + str(descript_Christie_tmp_1)

    $ Event('christie_root_24a', 'Corridor', time = 'morning', priority = -1)

    $ events.pop('christie_root_24', 0)





    $ unlock_city_library = False

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
