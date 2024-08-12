screen ep4_milf_37_block_igor_descript_screen_2:
    if getattr(store, 'block_igor_position', False):
        if __(descript_Christie) in (
        __("Теперь я могу отправиться к психологу, но сперва мне следует поговорить с Игорем и попросить его помочь с замком Кристи."),
        __('Продолжить следить за офицером. Как и в предыдущий раз, лучше всего это делать Утром, когда полицейский выходит из дома.'),
        __('Проведать Игоря в Парке и показать ему запись с продажным копом.'),
        __("Сходить к Игорю к Парк и попросить его взломать телефон продавщицы."),
        __("Сначала поговорить с Игорем, а после отправиться в библиотеку и продолжить написание реферата по теме «Обществознание»."),
        
        __("Отправить Игорю Видео с Кристи."),
        __("Поговорить с Игорем в парке завтра Утром, узнав у него, смог он взломать телефон Маши или нет."),
        __("Отправить Игорю ролик, где Кристи показывает стриптиз."),

        ):
            text __("Чтобы начать это задание нужно найти куда пропал Игорь...")  color '#000' line_spacing 0
label ep4_milf_37_block_igor:
    
    $ block_igor_position = True
   # if getattr(store, 'descript_Christie', '') == _("Теперь я могу отправиться к психологу, но сперва мне следует поговорить с Игорем и попросить его помочь с замком Кристи."):
    python:
        if 'christie_root_6' in events:
            for i in store.phone_sms_screen['Игорь']:
                if i.id == "3":
                    i.check = True
                    break

        #if 'christie_root_6' in events:
        for i in store.phone_sms_screen['Игорь']:
            if i.id == "2":
                i.check = True
            if i.id == "christie_root_35":
                i.check = True
            if i.id == "25":
                if not i.check:
                    i.check = True

                    if 'christie_root_54' not in store.completed_events:
                        descript_Christie = _("Поговорить с Игорем в парке завтра Утром, узнав у него, смог он взломать телефон Маши или нет.")
                        Event('christie_root_54', 'Igor', day_start = time.day_now + 1)
                        events.pop('christie_root_53', 0)
# id == "25"
    return
label ep4_milf_37:
    $ events.pop('ep4_milf_37', 0)

    call ep4_milf_37_block_igor from _call_ep4_milf_37_block_igor
    # $ igor_position = {
    #     'morning'   : ('None',       'None'),
    #     'afternoon' : ('None',       'None'),
    #     'evening'   : ('None',       'None'),
    #     'night'     : ('None',       'None'),
        
    #     }

    $ location_now = 'City_Park'
    $ Hide('main_interface')()


    call show_all_images_label from _call_show_all_images_label_34

    with Dissolve(.5)
    show Officer Normal
    show Officer Normal:

        xalign 1.5
        ypos 1085



    show GG Normal
    show GG Think:
        xalign .32
        ypos 1085

    with my_dissolve
    "[gg]" "Его нет."
    #show GG Think
    "[gg]" "Твою мать, этого я и боялся."
    #show GG Think
    "[gg]" "Нет-нет-не… Не могу поверить, чтобы Игорь кинул меня на бабки. "
    #show GG Think
    "[gg]" "Он бы так не поступил… Наверное. "
    #show GG Think
    "[gg]" "Сколько, он говорил, там было денег? ДОХРЕНИЩА? "
    #show GG Think
    "[gg]" "Знать бы ещё, какой у Игоря порог моральной устойчивости…"

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    show Officer Normal:
        xzoom -1
        linear 1 xalign .85
        ypos 1085

    $ renpy.pause(1, hard = True)

    show Officer Normal:
        xzoom -1
        xalign .85
        ypos 1085

    show GG Surprise
    with my_dissolve
    'Офицер' "Здравие желаю, [gg]. "
    show GG Skepticism
    "[gg]" "И вам того же."
    show GG Normal
    "[gg]" "Не обращайте внимание, что я в штатском, офицер. Я уже того… отработал ещё с утра."
    show Officer Normal
    'Офицер' "Ой, да брось ты. "
    show Officer Normal
    'Офицер' "Я прекрасно осведомлён, что твой дружок трудится вместо тебя. Видимо, у вас такой уговор. Пусть так. Я в чужие дела не лезу."
    show Officer Normal
    'Офицер' " Правда, как я погляжу, сегодня твой приятель отсутствует. Случилось чего?"
    show GG Surprise
    "[gg]" "Ничего!.."
    show GG Laughs
    "[gg]" "Что, по-вашему, с ним могло случиться? Выиграл в лотерею миллион и свалил из этого поганого городишка на все четыре стороны? "
    show Officer Normal
    'Офицер' "Тебе виднее, [gg]. Он же твой друг."
    show GG Normal
    "[gg]" "Вы чертовски правы, офицер. Мой братишка заболел… Отлёживается в тёплой кроватке и просто ждёт, когда улицы вычистят сами себя."
    show Officer Normal
    'Офицер' "А ты приколист."
    show GG Normal
    "[gg]" "Это всё, что вы хотели узнать?"
    show Officer Normal
    'Офицер' "Нет, постой. У меня для твоей подруги маленький сувенир. "

    show GG Skepticism
    "[gg]" "Суве… что?! "
    show Officer Pendant
    'Офицер' "Да, вот. Скромный, но на редкость элегантный кулон."
    show GG Angry
    "[gg]" "Вы же в курсе, что моя подруга замужем?"

    show Officer Normal
    'Офицер' "Значит не распространяйся об этом громко. "
    show GG Skepticism
    "[gg]" "Не уверен, что смогу обещать."
    show Officer Normal
    'Офицер' "Ты уж постарайся, дружище. Если не хочешь, чтобы кто-то упомянул, будто бы ты не исполняешь предписания судьи, или, чего ещё хуже, продолжаешь нарушать закон… к примеру, снова совершил кражу к ювелирном магазине."
    show GG Surprise
    "[gg]" "Хотите сказать, этот кулон краденный?! "
    show Officer Say
    'Офицер' "Да шучу я, шучу. Приятель, будь другом, передай Марине от меня подарочек. "
    show GG Angry
    "[gg]" "Окей. "
    show Officer Normal
    'Офицер' "Поверь, я умею помнить хорошие дела. "


    show Officer Normal:
        xzoom 1
        linear 1 xalign 1.5
        ypos 1085

    $ renpy.pause(1, hard = True)
    show GG Think
    "[gg]" "Вот мудак, решил, что сможет манипулировать мною. Ну-ну."
    $ descript = _('Вернуться домой и подарить Марине кулон от себя.')
    $ Event('ep4_milf_38',   'Milf', 'ep4_milf_38', button_name = _('Кулон'))
    $ block_change_milf_position = True


    $ milf_position = {
        'morning'   : ['Restroom',  'milf_restroom'],
        'afternoon' : ['Kitchen',   'milf_kitchen'],
        'evening'   : ['Hall',      'milf_evening_hall'],
        'night'     : ['Milf_Room', 'milf_room'],
    }
    $ block_milf_home   = False
    $ block_sister_home = False
    $ block_exit_home   = False
    $ time.time_now = 'evening'



    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
