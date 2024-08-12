label final_act_2_debug:
    scene black
    show image Text("DEBUG: переход к final_act_2"):
        align(.5, .5)
    with my_dissolve 
    call wait_click_label from _call_wait_click_label_28
label final_act_2:    #Final_Act_2 
        


    #Активировать Кэт или Дверь (время пропускать нельзя)

    $ events.pop('final_act_2', 0)
    $ location_now = "GG_Room"

    #GG_Normal

    #Cat_Normal
    call show_bg_image_label from _call_show_bg_image_label_235


    show GG Normal
    with my_dissolve
    show GG Normal:
        xalign .5
        ypos 1080
        xzoom -1
        easein_cubic 1.0 xalign .1
        #ypos 1080
        #zoom .95
    $ renpy.pause(1.0, hard = True)
    show GG Surprise
    show Kat Normal
    
    show Kat Normal:
        xalign .85
        ypos 1080

    with my_vpunch

    "Кэт" "А у тебя крепкий сон."
    show GG Skepticism:
        xzoom 1
    with my_dissolve
    "[gg]" "Чёрт… "
    show GG Surprise
    with my_dissolve
    "[gg]" "Только не говори мне, что трахнула меня, пока я спал!"
    show Kat Smile at hehe_transform()
    "Кэт" "Ха-ха-ха!!!"
    show Kat Smile:
        easein .1 ypos 1080
    "Кэт" "Если это вся реакция, которую ты можешь выдать на такой перфоманс, в следующий раз так и сделаю!"
    show Kat Smile:
        ypos 1080
    show GG Passion
    with my_dissolve

    "[gg]" "Как будто я был бы против."
    show GG Normal
    with my_dissolve
    
    "[gg]" "И всё же, что случилось?"
    show Kat Normal
    "Кэт" "Пока ты дрых, [gg], какой-то чувак хотел размозжить тебе мозги."
    #GG_Surprise

    show Kat Normal
    "Кэт" "Ага. Судя по тому, что он тут мямлил, это муж Марины. "
    
    "Кэт" "Я и не знала, что ты увёл чужую жену."
    show GG Chagrin
    "[gg]" "Это… Долгая история."
    
    "Кэт" "Убери со своего лица эту кислую рожу. "
    
    "Кэт" "Мне, вообще-то, насрать на чужих жён и тех, с кем ты трахаешься."
    
    "Кэт" "Но этот парень был настроен серьёзно. А ты…"
    
    show Kat Skepticism
    with my_dissolve
    "Кэт" "Ты мне дорог, как друг. К тому же, я проживаю в твоей комнате, а значит, ты под моей защитой. "
    show GG Skepticism
    with my_dissolve
    "[gg]" "Да ну?"
    show Kat Smile
    "Кэт" "Ага."
    show Kat Normal
    "Кэт" "Короче говоря, этот тип пригрозил вернуться."
    show GG Normal
    "[gg]" "Это всё? Больше он ничего не сказал?"
    
    "Кэт" "Назвал меня шлюшкой. "
    
    "[gg]" "Я припомню эти слова."
    show Kat Normal
    "Кэт" "Я не обижаюсь."
    show Kat Surprise
    "Кэт" "Главное – будь предельно осторожен."
    
    "[gg]" "Хорошо. Спасибо."
    show Kat Normal:
        easein 1.2 xalign -.05
    show GG:
        pause  .4
        easein .4 xalign .3
        xzoom -1.0
    "Кэт" "Увидимся."
    show GG Laughs
    with my_dissolve
    "[gg]" "Хех… А где же твоё «Оривидерчи»?"
    show Kat WTF:
        xzoom -1.0
    with my_dissolve
    "Кэт" "…..Ну."
    show Kat WTF:
        easein 4.3 xalign .3
    
    show GG Surprise:
        easein 4.3 xalign .72
    
    "Кэт" "Я хочу, чтобы ты вернулся, [gg]."
    show Kat Embarrassment
    "Кэт" "И возвращался всегда. Живым и невредимым."
    show shadow_full:
        alpha 0.0
        easein .75 alpha .75
    show GG Embarrassment:
        easein .7 ypos 1092
    "[gg]" "С…Спасибо."
    show shadow_full:
        easein .7 alpha 0.0
    show GG Embarrassment:
        easein .7 ypos 1080 xalign .5
    show Kat:
        xzoom 1.0
        easein 1.8 xalign -1.2
    $ renpy.pause(1.0, hard = True)
    #//Cat_Embarrassment исчезает

    show GG Think:
        xalign .5 ypos 1080
    with my_dissolve
    "[gg]" "Вот я и доигрался…"
    
    "[gg]" "После того, как Джеймс узнал о наших отношениях с Мариной, мне следовало объясниться с ним."
    
    "[gg]" "Сделать всё возможное, чтобы брат простил меня."
    
    "[gg]" "Но нет, я думал только о себе, и о том, как сильно мне повезло с Мариной."
    
    "[gg]" "В то время как мой брал изнывал от боли предательства, которое я совершил…"
    
    "[gg]" "Теперь Джеймс успокоился, проанализировал ситуацию и намеревается отомстить."
    
    "[gg]" "И что самое страшное, он всегда достигает цели."
    
    "[gg]" "Если он что-то уготовил, значит так тому и быть."
    
    "[gg]" "Я полный кретин…"
    
    "[gg]" "Чёрт…"

    
    python:
        debug_next('final_act_3_debug',)
        block_time_forward = copy.deepcopy(block_time_forward_final_act_1) 
        try:
            del block_time_forward_final_act_1
        except:
            pass
        
        
        descript = _("Брат намеревается отомстить. Если он что-то уготовил, значит так тому и быть.")
        
        Event(
        'final_act_3',  
        'City_Home', 
        
        time      = ['morning','afternoon'], 
        )    
    jump main_interface_label




