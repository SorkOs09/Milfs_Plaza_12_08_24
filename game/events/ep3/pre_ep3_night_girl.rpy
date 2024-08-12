label ep3_night_girl_menu_1:
    menu:
        "1. Пусть лижет дальше." if True:


            $ renpy.pause(99999999)
            "[gg]" "Охх…"
            "[gg]" "Не останавливайся. "
            "[gg]" "У тебя отлично получается."
            call ep3_night_girl_menu_1 from _call_ep3_night_girl_menu_1
        "2. Хочу продолжения." if True:
            $ pass

    return

label ep3_night_girl_menu_2:
    menu:
        "1. Пусть продолжает в текущем темпе." if True:


            $ renpy.pause(99999999)
            call ep3_night_girl_menu_2 from _call_ep3_night_girl_menu_2
        "2. Хочу продолжения." if True:
            $ pass
    return

label ep3_night_girl_menu_3:
    menu:
        "1. Пусть продолжает в текущем темпе." if True:


            $ renpy.pause(99999999)
            call ep3_night_girl_menu_3 from _call_ep3_night_girl_menu_3
        "2. Кончить." if True:
            $ pass
    return


image Night_collector_16anim:
    'images/cg/ep1/night_collector/Night_collector_16.png' with Dissolve(.5)
    1
    'images/cg/ep1/night_collector/Night_collector_17.png' with Dissolve(.5)
    1

    repeat

image Night_collector_18anim:
    'images/cg/ep1/night_collector/Night_collector_18.png' with Dissolve(.5)
    1
    'images/cg/ep1/night_collector/Night_collector_19.png' with Dissolve(.5)
    1

    repeat

label pre_ep3_night_girl:
    if events.get('pre_ep3_night_girl'):
        $ events.pop('pre_ep3_night_girl', 0)



label ep3_night_girl:
    stop music fadeout 1.5
    play music 'audio/n_girl.mp3' fadein 1.5

    scene expression 'images/cg/ep1/night_collector/Night_collector_1.png'
    with vpunch
    "[gg]" "Какого хера?!"
    scene expression 'images/cg/ep1/night_collector/Night_collector_5.png'
    with my_dissolve
    "Ночная гостья" "Соскучился?"
    scene expression 'images/cg/ep1/night_collector/Night_collector_13.png'
    with vpunch
    "[gg]" "А ты?"
    "Ночная гостья" "Ого, и что ты собираешься делать с этой штуковиной? "
    "[gg]" "Догадайся!"
    scene expression 'images/cg/ep1/night_collector/Night_collector_14.png'
    with my_dissolve
    "Ночная гостья" "Тогда, возможно, тебе пригодится «это»."
    "[gg]" "Чёрт…"
    scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
    with my_dissolve
    "Ночная гостья" "Предлагаю вернуться к нашим баранам. "
    "[gg]" "Может, не надо?"
    "Ночная гостья" "Где мои деньги, придурок?!"

    menu:
        "Вот, возьми (отдать {i}{b}20{/b}{/i} баксов)." if money >= 20:
            $ money -= 20
            $ show_text_animation('-20 money')
            scene expression 'images/cg/ep1/night_collector/Night_collector_8.png'
            with my_dissolve
            'Ночная гостья' "Люблю, когда всё по-моему. "
            '[gg]' " Надеюсь, ты удовлетворена и мы больше не увидимся."
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            with vpunch
            'Ночная гостья' "Ещё чего. Я буду навещать тебя каждую неделю, пока ты, наконец, не выплатишь долг. "
            '[gg]' " …"
            scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
            with my_dissolve
            'Ночная гостья' "Оривидэрчи, придурок. "
        "!Вот, возьми (отдать {i}{b}20{/b}{/i} баксов)." if money <  20:
            $ pass
        "Это всё, что я могу дать (отдать {i}{b}[money]{/b}{/i} баксов)." if money > 0 and money < 20:
            $ add_ach('ACH_13')

            #python:
            #    achievement.grant("ACH_13")
            #    achievement.sync()

            $ show_text_animation('-' + str(money) + ' money')
            $ money = 0
            scene expression 'images/cg/ep1/night_collector/Night_collector_8.png'
            with my_dissolve
            'Ночная гостья' "Не густо, конечно, но это лучше, чем совсем ничего. "
            '[gg]' " Надеюсь, ты удовлетворена и мы больше не увидимся."
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            with vpunch
            'Ночная гостья' "Ещё чего. Я буду навещать тебя каждую неделю, пока ты, наконец, не выплатишь долг. "
            '[gg]' " …"
            scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
            with my_dissolve
            'Ночная гостья' "Оривидэрчи, придурок. "
        "Извини, но у меня вообще ничего нет…" if True:
            scene expression 'images/cg/ep1/night_collector/Night_collector_3.png'
            with my_dissolve
            'Ночная гостья' "Мать твою, ты что, хочешь, чтобы я выпотрошила тебя? "
            '[gg]' " Клянусь собственными яйцами, у меня нет ни копейки."
            'Ночная гостья' "Хочется в это верить, иначе в следующий раз, ты обязательно останешься без них."
            '[gg]' " В следующий раз?!"
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            with my_dissolve
            'Ночная гостья' "А ты что думал? Я буду навещать тебя каждую неделю, пока ты, наконец, не выплатишь долг. "
            '[gg]' " …"
            scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
            with my_dissolve
            'Ночная гостья' "Оривидэрчи, придурок. "
        "Я дам тебе вдвое больше, если ты покажешь мне сиськи (отдать {i}{b}40{/b}{/i} баксов)." if money >= 40:
            $ money -= 40
            scene expression 'images/cg/ep1/night_collector/Night_collector_11.png'
            'Ночная гостья' "Чёртов извращенец."
            '[gg]' "Каков уж есть."
            'Ночная гостья' "Ладно-ладно. Тебе нравятся мои сиськи, мне – твои деньги."
            'Ночная гостья' "Но на большее не рассчитывай, сопляк."
            '[gg]' "Показывай уже!"
            scene expression 'images/cg/ep1/night_collector/Night_collector_12.png'
            'Ночная гостья' "Смотри и запоминай. Ты видишь их в первый и последний раз в жизни."
            '[gg]' "Чёрт, а ты горячая."
            'Ночная гостья' "…"
            '[gg]' "А можно потрогать?"
            'Ночная гостья' "Нет."
            '[gg]' "И за большую сумму?"
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            'Ночная гостья' "Всё, заткнись. Представление окончено. Давай бабки."
            $ show_text_animation('-40 money')
            scene expression 'images/cg/ep1/night_collector/Night_collector_8.png'
            '[gg]' "Вот."
            'Ночная гостья' "Оривидэрчи, придурок. Увидимся на следующей неделе."
            '[gg]' "Чего?!"
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            'Ночная гостья' "А ты что думал? Я буду навещать тебя каждую неделю, пока ты, наконец, не выплатишь долг."
            '[gg]' "…"
        "!Я дам тебе вдвое больше, если ты покажешь мне сиськи (отдать {i}{b}40{/b}{/i} баксов)." if money <  40:
            $ pass

        "!Как на счёт минета за 100 долларов?" if money < 100:
            $ pass

        "Как на счёт минета за 100 долларов?" if money >= 100:

            
            scene expression 'images/cg/ep1/night_collector/Night_collector_10.png'
            with Dissolve(.5)
            "Ночная гостья" "Охренеть! Ты проверяешь меня на моральную устойчивость?!"
            "[gg]" "У тебя слишком обаятельная мордашка."
            "Ночная гостья" "Хм… Честно?"
            "[gg]" "Да, ты очень миленькая."
            scene expression 'images/cg/ep1/night_collector/Night_collector_11.png'
            with Dissolve(.5)
            "Ночная гостья" "Ещё скажи, что влюбился в меня. "
            "[gg]" "Тяжело не испытывать влечения к симпатичной девушке, что сидит на моём члене. Хе-хе."
            "Ночная гостья" "А я всё думаю, что это упирается в меня…"
            "Ночная гостья" "Ладно. Деньги вперёд. "
            $ show_text_animation('-100 money')
            $ money -= 100
            scene expression 'images/cg/ep1/night_collector/Night_collector_8.png'
            with Dissolve(.5)
            "Ночная гостья" "Не могу обещать, что тебе понравится. "
            "[gg]" "Но ты уж постарайся."
            scene expression 'images/cg/ep1/night_collector/Night_collector_15.png'
            with Dissolve(.5)
            "Ночная гостья" "Ого, большой…"
            "[gg]" "Ты меня смущаешь. "
            "Ночная гостья" "Выглядит аппетитно. "
            scene Night_collector_16anim
            with Dissolve(.5)
            "Ночная гостья" "Какой сладкий."
            "Ночная гостья" "Крепчает от каждого моего касания. "
            "Ночная гостья" "Как забавно он вздрагивает, чувствуя приближения моего язычка."
            scene Night_collector_16anim

            call ep3_night_girl_menu_1 from _call_ep3_night_girl_menu_1_1






            scene Night_collector_18anim
            with Dissolve(.5)
            "[gg]" "Охренеть! Я достаю до самой глотки."
            "[gg]" "Внутри твоего ротика настоящий кайф. "
            "[gg]" "Ещё немного и я…"
            scene Night_collector_18anim
            call ep3_night_girl_menu_3 from _call_ep3_night_girl_menu_3_1



            scene expression '#fff' with Dissolve(.2)
            scene expression 'images/cg/ep1/night_collector/Night_collector_20.png'
            with Dissolve(1)

            $ renpy.pause(1)
            "[gg]" "Дааааа!!!"

            scene expression 'images/cg/ep1/night_collector/Night_collector_21.png'
            with Dissolve(.5)
            "Ночная гостья" "Ну как?"
            "[gg]" "Потрясающе. "
            "Ночная гостья" "Значит, я могу рассчитывать на чаевые? "

            menu:
                "1. Само собой. (-5 долларов)." if money >= 5:
                    scene expression '#000' with Dissolve(.5)

                    $ renpy.pause(.5, hard = True)
                    $ show_text_animation('-5 money')
                    $ money -= 5

                    scene expression 'images/cg/ep1/night_collector/Night_collector_8.png'
                    with Dissolve(.5)

                    "Ночная гостья" "Люблю деньги."
                    "[gg]" "Ещё бы."

                "!1. Само собой. (-5 долларов)." if money <  5:
                    $ pass
                "2. Мы так не договаривались." if True:
                    scene expression '#000' with Dissolve(.5)

                    $ renpy.pause(.5, hard = True)
                    scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
                    with Dissolve(.5)
                    "Ночная гостья" "Жадина. "
                    "[gg]" "Договор есть договор. "


            "Ночная гостья" "Оривидэрчи, придурок. Увидимся на следующей неделе. "
            "[gg]" "Чего?!"
            "Ночная гостья" "А ты что думал? Я буду навещать тебя каждую неделю, пока ты, наконец, не выплатишь долг. "
    if money == 0:
        $ add_ach('ACH_13')
    
    $ Event('night_girl',     'GG_Room',     'ep3_night_girl', day_start = time.day_now + 7, time = ['morning'])
    scene expression '#000' with Dissolve(.5)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
