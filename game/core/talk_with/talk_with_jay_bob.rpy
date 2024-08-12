

transform dance_down:
    linear .2 zoom 1.0-0.035

transform dance_up:
    linear .2 zoom 1.0

image Jay Normal xz = Transform('Jay Normal', xzoom = -1)
image Jay dancing:
    'Jay Normal'
    dance_down
    .05
    'Jay Normal'
    dance_up
    .05
    'Jay Normal'
    dance_down
    .05
    'Jay Normal'
    dance_up
    .05
    'Jay Normal xz' with Dissolve(0.2, alpha=True)
    dance_down
    .05
    'Jay Normal xz'
    dance_up
    .05
    'Jay Normal xz'
    dance_down
    .05
    'Jay Normal xz'
    dance_up
    .05


image Bob Normal xz = Transform('Bob Normal', xzoom = -1)
image Bob dancing:
    'Bob Normal'
    dance_down
    .05
    'Bob Normal'
    dance_up
    .05
    'Bob Normal'
    dance_down
    .05
    'Bob Normal'
    dance_up
    .05
    'Bob Normal xz' with Dissolve(0.2, alpha=True)
    dance_down
    .05
    'Bob Normal xz'
    dance_up
    .05
    'Bob Normal xz'
    dance_down
    .05
    'Bob Normal xz'
    dance_up
    .05


label talk_with_jay_bob_label:
    call check_surv_label from _call_check_surv_label_1
    play music 'audio/bubnila.mp3' fadein 1.5
    $ location_now = 'JayBob'
    $ check_ev = check_events()
    if check_ev:
        $ Jump(check_ev.label)()
    $ inventory_drugs = getattr(get_item('Товар', True), 'quant', 0)
    
    $ location_now = 'JayBobTalk'
    $ check_ev = check_events()
    
    $ location_now = 'City_Shop'
    menu:
        "Говорить" if check_ev:
            $ Jump(check_ev.label)()

        "Работа (у вас есть [inventory_drugs] пакетиков товара)" if getattr(store, 'inventory_drugs', 0) <= 0:
            $ pass
        "Работа (у вас есть [inventory_drugs] пакетиков товара)" if getattr(store, 'inventory_drugs', 0) > 0 and money >= 3000:
            $ enough_money_game_var = 'jay_bob_work'
            jump enough_money_game
        "Работа (у вас есть [inventory_drugs] пакетиков товара)" if getattr(store, 'inventory_drugs', 0) > 0 and money < 3000:
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

            show GG Normal
            show GG Normal at go_from_left

            '[gg]' "Чуваки, сегодня моя очередь фарцевать. "
            'Зудила' "Нет проблем, дружище. Мы сваливаем."
            $ time.time_forward(jump_to_main_interface = False)
            call show_all_images_label from _call_show_all_images_label_13

            play music 'audio/work.mp3' fadein 1.5
            $ timer_now = TimerClassSellGame(30)
            $ sell_mini_game = SellMiniGame()
            $ nastroi   = max(0,  nastroi-5)

            call screen SellMiniGameScreen

            jump sell_game_end
        "Назад" if True:
            $ pass
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
