



























label christie_root_21_pre_menu:
    call show_bg_image_label from _call_show_bg_image_label_133
    $ location_now = 'City_Library_BiblioGirl'
    $ check_ev = check_events()
    $ library_event_name = ""

    if check_ev:
        $ library_event_name = check_ev.button_name
    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign .85
    show GG Normal
    show GG Normal at go_from_left


label christie_root_21_menu:

    menu:
        "Реферат" if len(library_event_name):
            $ location_now = 'City_Library'
            $ renpy.jump(check_ev.label)
        "Говорить" if not len(library_event_name):
            $ location_now = 'City_Library'
            if time.time_now == 'evening':
                "Библиотекарша" "Извините, но мы уже закрываемся."
                show GG Normal:
                    xalign .15
                with my_dissolve
                "[gg]" "Да, я понял. "
                jump christie_root_21_menu

            "Библиотекарша" "Добро пожаловать в обитель знаний, меня зову Нэнси. "
            show GG Normal:
                xalign .15
            with my_dissolve
            "[gg]" "Привет, а меня [gg]."

            "Библиотекарша" "Вы к нам по делу или так?"
            show GG Normal
            "[gg]" "А что из «так» вы предлагаете?"

            "Библиотекарша" "Смотря что вы ожидаете, хи-хи."
            jump christie_root_21_menu
        "Уйти" if True:


            $ location_now    = 'City_Library'






            scene black with Dissolve(.5)
            jump main_interface_label

label christie_root_21:






    "Библиотекарша" "Добро пожаловать в обитель знаний."
    show GG Laughs:
        xalign .15
    with my_dissolve
    "[gg]" "Привет."

    "Библиотекарша" "Вы к нам по делу или так?"
    show GG Think
    "[gg]" "А что из «так» вы предлагаете?"

    "Библиотекарша" "Смотря что вы ожидаете, хи-хи."
    show GG Smile
    "[gg]" "Вы очень милая"

    "Библиотекарша" "Спасибо, хи-хи-хи."
    show GG Normal
    "[gg]" "Если честно, то я действительно по делу."

    "Библиотекарша" "Как жаль."

    "Библиотекарша" "У нас ведь столько разнообразных развлечений, кроме как чтения книг сидя, чтения книг стоя, и чтение книг во время ходьбы по залу. "

    "Библиотекарша" "Хи-хи-хи-хи!"
    show GG Passion
    "[gg]" "Меня интересуют книги по «Обществознанию». "
    show GG Normal
    "[gg]" "Я пишу реферат и мне нужен подходящий материл для этой темы."

    "Библиотекарша" "Вы оказались в нужном месте и обратились к нужному человеку. "

    "Библиотекарша" "Проходите в читальный зал, а я принесу вам всё необходимое. "

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
    scene expression "images/cg/christie_root/library/morning_gg_comics.png"
    with my_dissolve





    "[gg]" "{i}Хм…. Забавно.{/i}"
    "[gg]" "{i}Посетитель, что был здесь до меня, читал какие-то комиксы.{/i}"
    "[gg]" "{i}Взгляну-ка и я. {/i}"
    "[gg]" "{i}О, это же истории по мотивам любимого сериала Марины «Сладкий кексик» {/i}"












    scene expression "images/cg/christie_root/library/afternoon.png"
    show GG Normal
    show GG Normal:
        xalign .85
        xzoom -1
    with Dissolve(.5)
    show BiblioGirl Normal
    show BiblioGirl Normal at go_from_left(xxzoom = -1)




    "Библиотекарша" "Во необходимые вам книги. "
    show GG Smile

    "[gg]" "Спасибо, вы очень добры."
    show BiblioGirl:
        xalign .15
    with my_dissolve
    "Библиотекарша" "Это моя работа."
    show GG Smile
    "[gg]" "И вы отлично с ней справляетесь. "

    "Библиотекарша" "Хи-хи-хи."
    show GG Normal
    "[gg]" "Но как вы узнали, какие именно книги мне нужны?"

    "Библиотекарша" "Я же библиотекарь, сэр. "

    "Библиотекарша" "Не смотря на то, что львиная доля информации перетекла в интернет, это место всё ещё пользуется спросом."

    "Библиотекарша" "В особенности у тех, кто предпочитает учиться, а не имитировать обучение. "
    show GG Smile
    "[gg]" "А как вы относитесь к тем, кто не имитирует и не учится?"

    "Библиотекарша" "Хи-хи-хи."

    "Библиотекарша" "Знаете, я взяла на себя смелость и хочу вам предложить ещё одну книгу, лично от себя. "

    $ add_to_inventory(name = 'Камасутра')
    play sound 'audio/get_item.ogg'
    show screen give_item_screen(i_path+'/items/camasutra.png', _('Камасутра'), [_('Древнеиндийский трактат,'), _('посвящённый теме эмоциональной жизни,'), _('влечения и любви.')])
    with Dissolve(.75)

    $ renpy.pause(.5, hard = True)

    $ renpy.pause(9999)

    hide screen give_item_screen

    show GG Laughs
    with my_dissolve
    "[gg]" "Хех… Благодарю."

    "Библиотекарша" "Ознакомьтесь на досуге."
    show GG Laughs
    "[gg]" "Обязательно."

    "Библиотекарша" "Буду ждать ваших отзывов. Ну а пока, продуктивной работы вам, сэр."
    show GG Smile
    "[gg]" "Ага, спасибо."

    scene black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)

    scene expression "images/cg/christie_root/library/morning_gg.png"
    with my_dissolve





    "[gg]" "Так-с, чего тут у нас?... "
    "[gg]" "Социальные течения, политические пертурбации, веяния моды… "
    "[gg]" "… И та самая «Камасутра», что дала мне библиотекарша."
    "[gg]" "Вау…."
    "[gg]" "Кажется я определённо ей понравился."
    "[gg]" "Но сейчас мне не до этого."
    "[gg]" "Здесь работы до самой ночи, а может и до утра."
    "[gg]" "Но раз уж я взялся, назад дороги нет. "
    "[gg]" "Здесь выпишем, тут пару заметок…."
    "[gg]" "Ага, вот этот абзац определённо пригодится."
    "[gg]" "B здесь хорошее наблюдение."
    "[gg]" "Немного отсебятины… Или много…. "
    "[gg]" "Голова вот-вот взорвётся!"

    $ time.time_now = "evening"
    scene black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)


    scene expression "images/cg/christie_root/library/evening_gg.png"
    with my_dissolve






    "[gg]" "Нет, за один присест здесь точно не закончить."
    "[gg]" "Я полностью обессилен. "
    "[gg]" "Осталось только перечитать и можно смело идти. "











    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign -0.5
        xzoom -1
        easein_cubic 1 xalign .15



    "Библиотекарша" "Простите, но мы уже закрываемся."
    scene expression "images/cg/christie_root/library/evening.png"

    show GG Normal
    show GG Normal:
        xalign .85
        xzoom -1


    with my_dissolve
    "[gg]" "Да, я и сам собирался уходить."
    show BiblioGirl Normal
    show BiblioGirl Normal:
        xzoom -1
        xalign .15

    with my_dissolve
    "Библиотекарша" "Приходите ещё, хи-хи."
    show GG Smile
    "[gg]" "Я подумаю."

    show GG:

        ease 1.2 xalign -1.5
    show BiblioGirl:
        xzoom 1
        ease 1.2 xalign -1.5
    $ renpy.pause(1.5, hard = True)




    scene black with Dissolve(.5)

    call show_bg_image_label from _call_show_bg_image_label_134







    $ add_to_inventory(name = 'Реферат «Обществознание» 1/3')
    play sound 'audio/get_item.ogg'
    show screen give_item_screen(i_path+'/items/referat_2.png', _('Реферат «Обществознание» 1/3'), ['Мой собственный многочасовой', 'интеллектуальный труд.'])
    with Dissolve(.75)

    $ renpy.pause(1, hard = True)

    $ renpy.pause(9999)





    show GG Think
    show GG Think:
        xalign .5
    hide screen give_item_screen


    with my_dissolve
    "[gg]" "Я сделал примерно одну треть."

    "[gg]" "Мне придётся сюда вернуться ещё минимум два раза, если я хочу закончить начатое. "

    scene black with Dissolve(.5)
    $ time.time_now      = "night"
    $ location_now       = "City_Home"
    $ block_time_forward = True

    $ Event('christie_root_22', 'Corridor')

    $ events.pop('christie_root_21', 0)
    if not hasattr(store, 'allowed_events'):
        $ allowed_events = []
    $ allowed_events.append("christie_root_22")








    $ descript_Christie   = _("Завершить реферат по «Обществознанию».")
    $ unlock_city_library = False
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
