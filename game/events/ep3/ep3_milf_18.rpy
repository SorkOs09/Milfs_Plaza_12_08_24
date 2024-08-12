label ep3_milf_18:
    $ descript = _("Встретиться с Игорем. ")

    $ events.pop('ep3_milf_18', 0)

    if hasattr(store, 'ep3_milf_16'):
        $ del ep3_milf_16

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/loopster-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    $ block_time_forward = False
    $ block_milf_home  = False
    $ block_sister_home  = False
    $ block_exit_home    = False


    $ Hide('phone_interface')()
    $ Hide('main_interface')()
    if location_now == 'Milf_Room':
        $ location_now = 'Hall'

    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()

    call show_bg_image_label from _call_show_bg_image_label_17
    call show_additional_images_label from _call_show_additional_images_label_14
    with Dissolve(.5)
    show GG Normal
    show GG Normal:
        xalign .85
        xzoom -1

        ypos 1085
        zoom 1.0-0.035
    show Christie Skepticism
    show Christie Skepticism:
        xalign .15
        xzoom -1
        ypos 1085
        zoom 1.0-0.035

    with Dissolve(.5)







    "Кристи" "Мне показалось, или ты только что выходил из Марининой комнаты?"

    show GG Surprise
    "[gg]" "Эмм… "
    show GG Laughs
    "[gg]" "Нет, вовсе нет. Я просто проверял, нет ли её дома."


    show Christie Normal
    "Кристи" "Какое нелепое оправдание. Я всё расскажу Марине."

    show GG Surprise
    "[gg]" "Нет, погоди! Ты не так поняла! Я объяснюсь!"


    show Christie Laughs
    "Кристи" "Какая ирония, [gg]! "
    show Christie Normal
    "Кристи" "Не так давно ты шантажировал меня, чтобы выведать дату рождения Марины, но я и подумать не могла, что время расплаты наступит так быстро."

    show Christie Angry
    "Кристи" "Ха!"


    show GG Angry
    "[gg]" "Я не сделал тебе ничего дурного."
    show Christie Normal
    "Кристи" "Я тоже не собираюсь тебе вредить."
    show GG Chagrin

    show Christie Normal
    "Кристи" "Если, конечно, не «одолжишь» своей подружке сотню баксов."



    menu:

        "Вымогательница! (-100 долларов)" if money >= 100:
            $ pass
            $ show_text_animation('-100 money')
            $ money -= 100
            show Christie Smile
            "Кристи" "Видишь. У нас полное взаимопонимание. "

        "У меня только [money]." if money < 100:
            $ pass
            $ show_text_animation('-' + str(money) + ' money')
            $ money  = 0
            show Christie Skepticism
            "Кристи" "Как говорится: лучше синица в руках, чем журавль в небе. "













    show GG Angry
    "[gg]" "Я могу идти? "
    show Christie Normal
    "Кристи" "Ага."
    $ events.pop('ep2_9_igor', 0)
    $ Event('ep3_milf_18_2',     'Igor')

    jump main_interface_label





label ep3_milf_18_2:





    $ events.pop('ep3_milf_18_2', 0)
    call show_bg_image_label from _call_show_bg_image_label_18

    call show_additional_images_label from _call_show_additional_images_label_15

    show Igor Silence
    show Igor Silence:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_left






    "[gg]" "Привет, дружище… "
    "Игорь" "Ну здарова."
    show GG Chagrin
    "[gg]" "Всё, чувак, кажется это конец. Едва ли мы сможем узнать код от сейфа. Разве что перерыть комнату Марины вверх дном и просмотреть все записи в её телефоне. "

    show GG Chagrin
    "[gg]" "И то, не факт, что там окажется пароль."

    "[gg]" "Вряд ли ей нужно записывать 4 цифры от сейфа, которые легко можно запомнить. "
    show Igor Ok
    "Игорь" "А ты соображаешь. Правда, уже задним числом."
    show GG Angry
    "[gg]" "Эй! Твои упрёки неуместны. Мы на волоске от смерти. "
    show Igor Normal
    "Игорь" "Своё занудство я компенсирую своей гениальностью."
    show Igor Normal
    "Игорь" "Пока ты отсиживался дома, при чём делал это исключительно потому, что болен склерозом, я потратил своё драгоценное время на поиски аппарата для взлома домашних сейфов."
    show GG Surprise
    "[gg]" "Ого! "
    show Igor Normal
    "Игорь" "Ага, и таки нашёл его. "
    show GG Normal
    "[gg]" "Дай угадаю. Он стоит баснословных денег, и теперь я должен пойти заработать на него. "
    show Igor Troll
    "Игорь" "Ха, я положительно на тебя влияю. "
    show GG Skepticism
    "[gg]" "Ну, какова цена вопроса? "
    show Igor Silence
    "Игорь" "Человек, который его продаёт, хочет 400 баксов. "
    show GG Surprise
    "[gg]" "Нехило! "
    show Igor Normal
    "Игорь" "В нашем случае это очень дешево. Половину стоимости я уже оплатил, оставив 200 зелёных авансом. С тебя столько же. "
    show GG Normal
    "[gg]" "Откуда у тебя такие деньги? "
    show Igor Ok
    "Игорь" "Тебе трудно будет принять этот факт, но ты не единственный мой друг."
    show GG Smile
    "[gg]" "Хе-хе. А если честно? "
    show Igor Ok
    "Игорь" "Украл у родителей."
    show GG Chagrin
    "[gg]" "…."
    show GG Chagrin
    "[gg]" "Мы опускаемся на самое дно."

    "Игорь" "Поздно морализаторствовать. Лучше принеси поскорее деньги…"




label ep3_milf_18_3:
    $ location_now = 'City_Park'
    menu:

        "У меня уже есть необходимая сумма (-200$)," if money >= 200:
            $ descript = _("Спросить про билеты в театр у Зудилы и Бубнилы. ")
            $ Event('ep3_milf_20',     'JayBob')
            $ money -= 200
            $ show_text_animation('-200 money')
            $ events.pop('ep3_milf_18_4', 0)
            jump ep3_milf_19
        "Я вернусь когда наберу 200$" if money < 200:
            $ Event('ep3_milf_18_4',     'Igor')

            $ descript = _("Дать Игорю 200 долларов для покупки взломщика сейфов. ")
        "Я вернусь позже" if money >= 200:
            $ Event('ep3_milf_18_4',     'Igor')

            $ descript = _("Дать Игорю 200 долларов для покупки взломщика сейфов. ")
    jump main_interface_label



label ep3_milf_18_4:
    $ location_now = 'City_Park'
    call show_all_images_label from _call_show_all_images_label_18
    show GG Normal
    show GG Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    show Igor Normal
    show Igor Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    jump ep3_milf_18_3
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
