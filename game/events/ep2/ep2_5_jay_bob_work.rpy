

label ep2_5_jay_bob_work_1:
    $ location_now = 'City_Shop'
    menu:
        "!1. Работа (у вас есть [inventory_drugs] пакетиков товара)" if inventory_drugs <= 0:

            $ pass


        "1. Работа (у вас есть [inventory_drugs] пакетиков товара)" if getattr(store, 'inventory_drugs', 0) > 0 and money >= 3000:

            $ enough_money_game_var = 'jay_bob_work'

            jump enough_money_game


        "1. Работа (у вас есть [inventory_drugs] пакетиков товара)" if getattr(store, 'inventory_drugs', 0) > 0 and money < 3000:


            $ events.pop('ep2_5_jay_bob_work_1', 0)
            $ Event('ep2_6_blins',   'Corridor', time = ['morning', 'afternoon', 'evening'])

            $ descript = _('Дождусь новостей от Игоря и тогда уж решу окончательно, валить из города, или принять свою участь и сдохнуть, как собака. ')
            call show_all_images_label from _call_show_all_images_label_55
            play music 'audio/work.mp3' fadein 1.5
            $ timer_now = TimerClassSellGame(30, 'ep2_5_jay_bob_work_2')
            $ sell_mini_game = SellMiniGame()
            $ nastroi   = max(0,  nastroi-5)

            call screen SellMiniGameScreen

            jump sell_game_end
        "2. Уйти" if True:


            jump main_interface_label

    jump main_interface_label

label ep2_5_jay_bob_work_2:
    scene expression '#000' with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    $ time.time_now = 'evening'
    call show_all_images_label from _call_show_all_images_label_56
    with Dissolve(.5)
    show GG Think
    show GG Think:
        xalign .5
        ypos 1085
        zoom 1.0-0.035

    hide screen SellMiniGameScreen

    hide screen text_animation_sell

    with Dissolve(.5)


    "[gg]" "Думаю, какое-то время я ещё могу так поработать. "

    "[gg]" "Дождусь новостей от Игоря и тогда уж решу окончательно, валить из города, или принять свою участь и сдохнуть, как собака. "


    $ time.time_now = 'night'
    $ money        += sell_mini_game.money
    $ show_text_animation('+'+str(sell_mini_game.money)+' money')
    $ location_now  = 'City_Shop'
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
