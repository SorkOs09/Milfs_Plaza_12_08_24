label ep2_3_igor:


    call comic_frame_v2_predict_label(images=[
        "mini_games/cleaning_mini_game/cleaning_bg.png",
        "mini_games/cleaning_mini_game/l_1.png",
        "mini_games/cleaning_mini_game/l_2.png",
        "mini_games/cleaning_mini_game/l_3.png",
        "mini_games/cleaning_mini_game/l_4.png",
        "mini_games/cleaning_mini_game/l_5.png",
        "mini_games/cleaning_mini_game/l_6.png",
        
        ]) from _call_comic_frame_v2_predict_label_6
    $ events.pop('ep2_3_igor', 0)

    call show_bg_image_label from _call_show_bg_image_label_42
    call show_additional_images_label from _call_show_additional_images_label_36
    with Dissolve(.5)

    show Igor Normal
    show Igor Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)




    show GG Normal
    show GG Normal at go_from_left

    $ renpy.pause(1, hard = True)





    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/daily-beetle-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    show GG Normal
    "[gg]" "Тебе идёт эта форма, хе-хе."
    show Igor Ok
    show GG:
        xalign .15
    "Игорь" "А тебе идёт хуй во рту."
    show GG Laughs
    "[gg]" "Ха-ха-ха!"
    show Igor Angry
    "Игорь" "Я пашу здесь с раннего утра!"
    show Igor Angry
    "Игорь" "На руках мозоли размером с волдырь. Спину ломит. Отдышка появилась…. На кой чёрт я согласился заменять тебя?!"


    show GG Smile
    "[gg]" "Чёрт, говоришь? Хе-хе."
    show GG Smile
    "[gg]" "О нет, дружище. Твои внутренние демоны тут не при делах."
    show GG Skepticism
    "[gg]" "Это твоё крошечное, почти невидимое, но всё ещё теплящееся внутри, чувство вины. "
    show GG Skepticism
    "[gg]" "Ведь это ты, говнюк эдакий, не предупредил меня о подходе охранника во время кражи часов в ювелирном магазине."
    show GG Skepticism
    "[gg]" "А когда запахло жаренным, скрылся, оставив меня разгребать это дерьмо. "
    show GG Skepticism
    "[gg]" "Наше ОБЩЕЕ дерьмо, я замечу."
    show GG Normal
    "[gg]" "Ну как, я близок к истине?"
    show Igor Bad


    show Igor Bad
    "Игорь" "Извини, чувак. "
    show Igor Bad
    "Игорь" "Я обосрался по полной"
    show Igor Bad
    "Игорь" "Да, я не заметил охранника."
    show Igor Bad
    "Игорь" "И вместо того, чтобы отвлечь на себя внимание, испугался и убежал."
    show GG Normal
    "[gg]" "Знаю, бро. Знаю."
    show Igor Bad
    "Игорь" "Значит, ты не злишься на меня?.."
    show GG Normal
    "[gg]" "Проехали."
    show Igor Troll
    "Игорь" "Тогда, может, ты возьмёшь у меня метлу и немного подсобишь?"
    show GG Laughs
    "[gg]" "Ахахаха!"
    show Igor Normal
    "Игорь" "Нет, я серьёзно. Помоги мне, бро!"
    show GG Normal

    menu:
        "Помочь" if True:
            show GG Normal
            "[gg]" "Гони метлу, работяга! "
            show GG Normal
            "[gg]" "Профессиональный дворник в деле."
            call mini_game_park_clean_label from _call_mini_game_park_clean_label

            call show_bg_image_label from _call_show_bg_image_label_87
            call show_additional_images_label from _call_show_additional_images_label_73

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

            show Igor Ok
            "Игорь" "Чёт как-то не много ты мне помог…"
            show GG Surprise
            "[gg]" "Нихера ж себе благодарности подъехали. "
            show Igor Normal
            "Игорь" "Ладно-ладно. Спасибо и на этом."
            show Igor Normal
            "Игорь" "Вот, держи, а то обидишься ещё!"

            show GG Normal
            "[gg]" "Что это?"
            show Igor Normal
            "Игорь" "Коллекционный купон. Но сейчас эта самая ходовая валюта на чёрном рынке."
            show Igor Normal
            "Игорь" "Если ты найдёшь продавцов, которые её принимают, ты за бесценку сможешь купить уникальные и стоящие вещи. "
            show GG Normal
            "[gg]" "Круто."
            show Igor Normal
            "Игорь" "Надеюсь, теперь я по достоинству оценил твою работу."
            show GG Normal
            "[gg]" "Вполне. Но знай, это разовая акция."
            $ add_to_inventory('Купон «кекса»', ncopy = True)
            window hide
            show screen give_item_screen(i_path+'/items/keks.png', _('Купон «кекса»'),[_('Коллекционный купон, '), _('Но сейчас эта самая ходовая валюта'), _('на чёрном рынке.')])
            with Dissolve(.5)
            $ renpy.pause(9999)
            hide screen give_item_screen
            with Dissolve(.5)
        "Не помогать" if True:


            show GG Normal
            "[gg]" "Ну, если я ещё и твою работу выполнять буду, это уж слишком."
            show Igor Ok
            "Игорь" "…."










    show Igor Normal
    "Игорь" "Кстати о работе. "
    show Igor Normal
    "Игорь" "Я тут проходил мимо магазина и заметил, что твою « торговую точку» заняли двое каких-то балбесов. "
    show Igor Normal
    "Игорь" "Миллион баксов ты там не заработаешь, разумеется, но и совсем лишать себя заработка было бы безрассудно."
    show Igor Normal
    "Игорь" "Короче говоря, прогнать их надо."
    show Igor Normal
    "Игорь" "Пусть не сегодня, так завтра нам пригодятся деньги на мелкие расходы. "
    show GG Chagrin
    "[gg]" "Да, но знаешь…"
    show GG Chagrin
    "[gg]" "Я, признаться, не горю желанием возвращаться к продаже наркотиков."
    show GG Normal
    "[gg]" "Когда ты предложил эту «железобетонную» игру в покер, я рассчитывал вложить свою долю выигрыша в какой-нибудь бизнес и завязать с криминалом…"
    show GG Chagrin
    "[gg]" "А теперь погряз ещё сильнее. "
    show GG Chagrin
    "[gg]" "Не очень-то хочется усугублять своё, и без того трудное, положение."
    show Igor Normal
    "Игорь" "А я?"
    show Igor Angry
    "Игорь" "Разве я не усугубляю своё положение, торча здесь у всех на виду, из-за чего могу стать жертвой Жлоба в любой момент?"
    show Igor Angry
    "Игорь" "Тебе удобно говорить о сраной нравственности, протирая штаны дома под полным опекунством «мамочки»."

    show GG Angry
    show Igor Angry
    "Игорь" "А я здесь один, и моя жопа всегда под прицелом. "
    show Igor Normal
    "Игорь" "Каждую секунду я думаю над нашим следующим шагом."
    show Igor Angry
    "Игорь" "И когда придёт время действовать, [gg], я ооооочень надеюсь, что у нас будут хоть какие-то деньги в этот момент. Понял?!"
    show GG Normal
    "[gg]" "Понял-понял. "

    show Igor Normal

    show GG Normal
    "[gg]" "Только твои нотации бесполезны. Толку мне отбивать свою «точку», если у меня нет денег на закупку товара. "
    show Igor Troll
    "Игорь" "С этим проблем не возникнет."
    show Igor Troll
    "Игорь" "В этом парке полно закладок. "
    show Igor Troll
    "Игорь" "Достаточно перешерстить несколько кустиков, и ты наверняка найдёшь пакетик с товаром. "
    show GG Normal
    "[gg]" "Отлично. Ты предлагаешь мне следует красть чужой товар, а потом перепродать его на углу магазина?"
    show GG Normal
    "[gg]" "Какое ещё дно я должен пробить, чтобы сказать «хуже уже некуда»?"

    "Игорь" "Это бездна, чувак!"

    "Игорь" "Бееееееееезднааа!"
    show Igor Ok
    "Игорь" "Всяко лучше смерти."
    show GG Normal
    "[gg]" "Как сказать…"

    call comic_frame_v2_predict_label(action=renpy.stop_predict,
        images=[
        "mini_games/cleaning_mini_game/cleaning_bg.png",
        "mini_games/cleaning_mini_game/l_1.png",
        "mini_games/cleaning_mini_game/l_2.png",
        "mini_games/cleaning_mini_game/l_3.png",
        "mini_games/cleaning_mini_game/l_4.png",
        "mini_games/cleaning_mini_game/l_5.png",
        "mini_games/cleaning_mini_game/l_6.png",
        
        ]

        ) from _call_comic_frame_v2_predict_label_9

    $ Location(
            'City_Shop',
            buttons       = [],
            image_buttons = {
            }
            )


    $ locations['City_Park'].image_buttons_times = {
    'morning'   : {'search_game_icon': Jump('search_game_label'),},
    'afternoon' : {'search_game_icon': Jump('search_game_label'),},
    'evening'   : {},
    'night'     : {},
    }

    $ locations['City_Shop'].image_buttons_times = {
    'morning'   : {
    'jay_bob': Jump('talk_with_jay_bob_label'),
    'door' : [Function(JumpToLocation, 'StoreIn')],
    },
    'afternoon' : {
    'jay_bob': Jump('talk_with_jay_bob_label'),
    'door' : [Function(JumpToLocation, 'StoreIn')],
    },
    'evening'   : {
    'door' : [Function(JumpToLocation, 'StoreIn')],
    },
    'night'     : {

    },
    }

    $ Location(
                'StoreIn',
                buttons = []
                )


    $ Event('talk_with_store_woman_label', 'StoreIn')

    $ storein_shop_items = [_('Красное вино'), _('Попкорн')]


    $ descript = _('Отбить свою «торговую точку» на углу Магазина. Мне нужен или помощник, или подручное средство против гопников.')


    $ Event('ep2_4_jay_bob', 'JayBob')






    scene expression '#000' with Dissolve(1)




    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
