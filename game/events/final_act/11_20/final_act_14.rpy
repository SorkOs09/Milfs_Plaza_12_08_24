label final_act_14:    #Final_Act_14
    $ events.pop('final_act_14', 0)
    
    #$ time.time_now = "evening"

    call prison_talk_with_girl_officer_start from _call_prison_talk_with_girl_officer_start

    "Офицерша" "Знаешь, мне знакомы эти чувства, [gg]."
    show GG Prison_WTF
    with my_dissolve
    "[gg]" "Что ты имеешь в виду?"
    show GirlOfficer Normal
    "Офицерша" "Та женщина, что посещает тебя. Не трудно заметить, как сильно вы любите друг друга."
    show GG Prison_Smile
    with my_dissolve
    "[gg]" "Ах.. Ты про Маришку. Да, мы самые близкие люди на свете."
    show GG Prison_Chagrin
    with my_dissolve
    "[gg]" "Хотя, признаться, она – одна из причин, почему я здесь оказался."
    show GirlOfficer Smile
    with my_dissolve
    "Офицерша" "Ха, как мило!"
    #show GirlOfficer Normal
    "Офицерша" "Выходит, это не заключение, а жертва, на которую ты пошёл ради любимого человека."
    show GG Prison_Smile
    with my_dissolve
    "[gg]" "Хм… Любопытный взгляд со стороны. "
    show GirlOfficer Normal
    with my_dissolve
    "Офицерша" "А ведь я тоже иду на жертвы."
    show GG Prison_Please
    with my_dissolve
    "[gg]" "Да?.."

    "Офицерша" "Да. У меня тоже есть любимый человек."
    #//мысли

    show GG Prison_WTF
    show shadow_full:
        alpha .75
    with my_dissolve
    "[gg]" "{i}Мать твою, надеюсь она говорит не про меня.{/i}"
    
    "[gg]" "{i}Не хватало ещё разочаровывать её…{/i}"
    
    "[gg]" "{i}Я совсем не знаю эту девушку, но от её помощи зависит моя жизнь…{/i}"
    show GirlOfficer Normal
    hide shadow_full
    with my_dissolve
    "Офицерша" "Что с тобой, [gg]? Ты удивлён, что у меня есть парень?"
    show GG Prison_Smile
    with my_dissolve
    "[gg]" "Нет-нет. Я просто задумался о том, сколько у нас… общего."
    
    "Офицерша" "Да. Не смотря на все наши поступки, мы оба счастливые люди. "
    show GG Prison_Chagrin
    with my_dissolve
    "[gg]" "Наверное…"

    "[gg]" "….."
    
    "Офицерша" "И ради людей, которых мы любим, мы готовы пойти на любые прегрешения. "
    
    "Офицерша" "Как сейчас, например."
    show GG Prison_WTF
    with my_dissolve
    "[gg]" "Значит, помогая мне, ты идёшь на прегрешения?"
    
    "Офицерша" "Мгу."
    
    "Офицерша" "Но и мой любимый грешит ради меня."
    
    "Офицерша" "Стыдно сознаться, но у него есть жена."
    
    "Офицерша" "Я думаю, ты уже догадался, о ком я говорю, но, в силу сложившихся обстоятельств, я бы предпочла не называть его имени."
    show GG Prison_Chagrin
    with my_dissolve
    "[gg]" "Хорошо."
    show GG Prison_Please
    with my_dissolve
    "[gg]" "Но что будет в итоге?.. "

    "[gg]" "Помогая мне, ты разве не испортишь с ним отношения?"

    "Офицерша" "Пока что я не могу ответить тебе на этот вопрос, [gg]. "

    "Офицерша" "К тому же, мне пора идти. Вот, покушай, пока еда окончательно не остыла."
    show GG Prison_Chagrin
    with my_dissolve
    "[gg]" "Спасибо…"
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_6
    $ renpy.pause(.3, hard = True)
    $ locations['Prison'].image_buttons_times['afternoon'].update(
                {'milf':Jump('final_act_16')}
                )
    #+ восполнение едды

    
    $ Hide('info_panel')()
    $ final_act_sitost = min(final_act_sitost+50, 100)
    $ Show('info_panel', ttext = "+50", iimage = "info_panel_prison_sitost")()
    

    call final_act_blind_transition_to_black_label from _call_final_act_blind_transition_to_black_label_4
        


    $ time.time_now = 'morning'

    jump main_interface_label




