label final_act_16:    #Final_Act_16


    #"Description" "Мне удалось немного расшатать болты унитаза, но этого недостаточно. Теперь мне надо подкачаться ЕЩЁ СИЛЬНЕЕ! "
    call prison_talk_with_milf_sex_start from _call_prison_talk_with_milf_sex_start_1
    #Активировать Милфу Днём



    #"//При Попытке Пропустить Время (Пропуском Или Действия «Отжиматься») 
    #Игрок Выведется Надпись" ""
    #"[gg]" "Я не могу СЕЙЧАС игнорировать Марину. "


    
    show Milf Street_0_Smile
    with my_dissolve
    "Марина" "Миленький, дорогой, она согласилась!"
    show GG Prison_Surprise
    with my_dissolve
    "[gg]" "Мама Игоря?"
    #show Milf Street_0_Chagrin
  
    "Марина" "Ага."
    #show Milf Street_0_Chagrin

    show Milf Street_0_Normal
    with my_dissolve
    "Марина" "Когда я посетила Людмилу Сергеевну, она пребывала подавленном состоянии."
    #show Milf Street_0_Chagrin

    show Milf Street_0_Chagrin
    with my_dissolve
    "Марина" "Правда о сыне стала для неё настоящим шоком."
    #show Milf Street_0_Chagrin

    show Milf Street_0_Normal
    with my_dissolve
    "Марина" "И всё же она без колебаний ответила «да»."
    #show Milf Street_0_Chagrin
    "Марина" "У меня возникло ощущение, что для неё это дело чести. "
    show GG Prison_WTF
    with my_dissolve
    "[gg]" "Ну ясное дело, на кону жизнь её сына."
    #show Milf Street_0_Chagrin

    show Milf Street_0_Chagrin
    with my_dissolve
    "Марина" "Не знаю – не знаю."
    #show Milf Street_0_Chagrin

    show Milf Street_0_Normal
    with my_dissolve
    "Марина" "Когда я назвала твоя имя, Людмила Сергеевна моментально приободрилась и заверила меня, что сделает всё, что в её силах."
    show GG Prison_Surprise
    with my_dissolve
    "[gg]" "Даже так?.."
    #show Milf Street_0_Chagrin
    "Марина" "Вот-вот, я сам удивилась."
    #show Milf Street_0_Chagrin

    show Milf Street_0_Sad
    with my_dissolve
    "Марина" "Интересно, с чем связана её такая позитивная реакция?.."
    show GG Prison_WTF
    with my_dissolve
    "[gg]" "Ну… Мы немного знакомы."
    #show Milf Street_0_Chagrin

    show Milf Street_0_Angry
    with my_dissolve
    "Марина" "Мне стоит ревновать? "
    show GG Prison_Please
    with my_dissolve
    "[gg]" "Возможно."
    #show Milf Street_0_Chagrin
    show shadow_full:
        alpha .35
    show Milf Street_0_Passion
    with my_dissolve
    "Марина" "Играешь со мной?"
    show shadow_full:
        alpha .5
    show GG Prison_Passion
    with my_dissolve
    "[gg]" "Ага. Хочу, чтобы наши встречи стали более горячими."
    #show Milf Street_0_Chagrin

    "Марина" "Оооо, значит, тебе хочется развития наших свиданий…"
    #show Milf Street_0_Chagrin
    $ _sitost_img = 'interface/prison_survival_sitost.png'
    show shadow_full:
        alpha .75
    show Milf Street_0_Sex_Passion
    with my_dissolve
    "Марина" "Тогда я знаю, чем тебя обрадовать в этот раз. "
    show screen prison_survival_screen
    with my_dissolve
    menu:
        "!Мастурбировать (-20 {image=[_sitost_img]})" if final_act_sitost < 20:
            $ pass
        "!Мастурбировать 2 ур. (-30 {image=[_sitost_img]})"  if final_act_sitost < 30:
            $ pass
        "Мастурбировать (-20 {image=[_sitost_img]})" if final_act_sitost >= 20:
            $ time.time_now = "evening"
            hide screen prison_survival_screen
            call final_act_13_masturbation from _call_final_act_13_masturbation_1
        "Мастурбировать 2 ур. (-30 {image=[_sitost_img]})"  if final_act_sitost >= 30:
            $ time.time_now = "evening"
            hide screen prison_survival_screen
            call final_act_16_masturbation from _call_final_act_16_masturbation
        "Отказаться":
            #"//Если Игрок Выбирает Вариант «Отказаться « (Например, У Него Не Хватает Выносливости), То Далее Идёт Такой Диалог" ""
            hide screen prison_survival_screen
            call prison_talk_with_milf_masturbation_reject from _call_prison_talk_with_milf_masturbation_reject_1
    jump final_act_16_end
    #"//Варианты Ответов" ""
    #Мастурбировать (-20 Выносливости).

    #Мастурбировать 2 ур. (-30 Выносливости)

    #Отказаться.

    #//Milf_Turtma_Ass

    #//Dick_Turma_Anim

    #//x1
label final_act_16_masturbation:
    $ Hide('info_panel')()
    scene black 
    with my_dissolve
    $ renpy.pause(.5, hard = True)

    $ final_act_sitost -= 30
    $ Show('info_panel', ttext = "-30", iimage = "info_panel_prison_sitost")()

    scene image 'cg/final_act/milf_cage/milf/anal.png'
    show final_act_milf_gg_jerk anim_1
    with my_dissolve
    "[gg]" "О дааа, чудесный вид на самую роскошную задницу в мире!"
    "[gg]" "Какая она большая, сочная, притягательная…"
    "[gg]" "Как бы мне хотелось потереть между этими булочками, ощутить их мягкие объятия."
    "[gg]" "Я уверен, твоя дырочка явно изголодалась по моему члену, Маришка…"
    "Марина" "Ага."
    "Марина" "Но всё что нам остаётся, это удовлетворять фантазии друг друга."

    #//x2
    show final_act_milf_gg_jerk anim_2
    with my_dissolve
    "[gg]" "Значит, ты постоянно грезишь обо мне?"
    "[gg]" "Жаждишь мой член, верно?"
    "Марина" "Аххх..!! Ещё как!"
    "Марина" "Каждую ночь я громко стонаю от одиночества…"
    "Марина" "Я не могу уснуть, пока не доведу себя до оргазма от мысли по тебе!"
    "[gg]" "Уфффф!... Проддолжай, Мирашка. Продолжай говорить!"
    "[gg]" "Эти мысли согревают меня в тяжёлые минуты заключения."
    "Марина" "Ничто так не спасает, как тепло настоящей любви, верно?"
    "[gg]" "И не только…"
    "Марина" "Аххх…Ты моей шикарной заднице, верно?"
    "[gg]" "Твоё прекрасное тело – пока что единственное, что поддерживает во мне жизнь здесь."
    "Марина" "Давай, милый, кончи на мою попку. Залей её спермой!"
    "Марина" "Оставь на моём теле хотя бы маленькую частичку себя…."
    #//кончить
    show final_act_milf_gg_jerk anim_3
    with my_dissolve
    #//х3

    "Марина" "О дааа, я слышу, как яростно ты дрочишь на меня."
    "Марина" "Я практически ощущаю член внутри себя… "
    "Марина" "Эти фантомные чувства радости от секса…"
    "Марина" "Анального секса…!"
    "Марина" "Моя попка уже готова для твоего бурного фонтана любви, [gg]!"
    "[gg]" "Кончааааааюююююуууу!!!...."
    call prison_talk_with_milf_cum from _call_prison_talk_with_milf_cum_1
    #//Milf_Turtma_Tits_End

    #//Dick_Turma

    #show Milf Street_0_Chagrin
    
    call prison_talk_with_milf_masturbation_end from _call_prison_talk_with_milf_masturbation_end_1
    return

label final_act_16_end:

    #"//Time" "+1"

    
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_9
    $ renpy.pause(.3, hard = True)
#    $ Event(
#        'final_act_17',  
#        time      = ['night',], 
#        )    

    $ locations['Prison'].image_buttons_times['night'].update(
        {'food':Jump('final_act_17')}
        )
    


    call final_act_blind_transition_to_black_label from _call_final_act_blind_transition_to_black_label_5
        

    $ time.time_now = "evening"
    
    jump main_interface_label
    #"Time" "+1"

    #//Нюанс

    #//Теперь Игроку надо будет пробовать расшатать туалет до 2 уровня!

    #//Всё время ДО этого Днём и Вечером будут появляться спрайты Милфы и Мента, но никакого значения для сюжета диалоги с ними нести не будут. Это так, типа, для интерактива.


    #//Повторяющаяся сцена с Милфой




    #show Milf Street_0_Chagrin
    "Марина" "Привет, любимый."
    
    "[gg]" "Привет, Маришка."
    
    "[gg]" "Есть свежие новости? "
    #show Milf Street_0_Chagrin
    "Марина" "О нет, пока нет."
    #show Milf Street_0_Chagrin
    "Марина" "Я здесь лишь для того, чтобы развеять твои мрачные будни."
    
    "[gg]" "Значит, я вновь могу пошалить?"
    #show Milf Street_0_Chagrin
    "Марина" "Со мной, милый, ты можешь делать всё, что тебе заблагорассудится. "
    
    "[gg]" "От такого трудно отказаться…"
    #show Milf Street_0_Chagrin
    "Марина" "Тогда позволь мне чуточку развлечь тебя."
    "//Варианты Ответов" ""
    #Мастурбировать (-20 Выносливости).

    #Мастурбировать 2 ур. (-30 Выносливости).

    #Отказаться.

    #//Далее сцена полностью повторяет то, что я писал выше

    "Time" "+1"

    #//Повторяющаяся сцена с Ментом





