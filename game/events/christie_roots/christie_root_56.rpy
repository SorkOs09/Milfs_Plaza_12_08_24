label christie_root_56:
    #Вернуться к Кристи.
    #"ext" "Активировать Кристи Утром или Днём."
    #"ext" "GG_Normal"
    #"ext" "Kristy_Normal"
    $ sister_position['evening']  = ['None',  'sister_room']

    $ events.pop('christie_root_56', 0)
    call show_bg_image_label from _call_show_bg_image_label_210
    call show_additional_images_label from _call_show_additional_images_label_106
    show Christie Normal
    show Christie Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Smile
    show GG Smile at go_from_left

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/full-moon-lofi-vibes-by-edikey20-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Вот и всё, Кристи, мы разрушили брак Сьюзен и теперь полностью свободны!"
    show Christie Chagrin
    "Кристи" "Хотя мы и руководствовались благими намерениями, гордиться результатом трудно."
    show GG Normal:
        xalign .15
    with my_dissolve
    "[gg]" "Тогда оставим это в прошлом и будем жить настоящим."
    show Christie Normal
    "Кристи" "Рада, что ты на позитиве. "
    show GG Skepticism
    "[gg]" "Эй! Мы сделали всё, что от нас требовалось. "
    show GG Skepticism
    "[gg]" "Что же нам теперь, панихиду устраивать?"
    show Christie Normal
    "Кристи" "Да, ты прав. "
    show Christie Chagrin
    "Кристи" "Просто сейчас, наверное, Сьюзен совершенно разбита. "
    show Christie Chagrin
    "Кристи" "Может мне сходить к ней гости и поддержать?"
    show GG Embarrassment
    "[gg]" "Ну…"
    show GG Laughs
    "[gg]" "Как мне показалось, она стойко приняла этот «удар»."
    show Christie Skepticism
    "Кристи" "Хм…."
    show Christie Skepticism
    "Кристи" "Думаешь, она и сама ожидала данной развязки? "
    show GG Normal
    "[gg]" "Когда мы в последний раз поднимали эту тему, ты и сама подозревала её в чём-то корыстном. "
    show Christie Embarrassment
    "Кристи" "Из ревности…"
    show GG Normal
    "[gg]" "Но я своего мнения не поменял."
    show GG Smile
    "[gg]" "Предлагаю забыть о Сьюзен и хорошо провести время вместе."
    show Christie Smile
    "Кристи" "Чудное предложение. Я только за!"
    show GG Smile
    "[gg]" "Как на счёт вечерней прогулке в Парке?"
    show Christie Smile
    "Кристи" "Согласна! "
    show GG Smile
    "[gg]" "Тогда готовься, в любой момент я могу пригласить тебя."
    show Christie Chagrin
    "Кристи" "Почему не сегодня? Или даже сейчас?"
    show GG Smile
    "[gg]" "Извини, сегодня у меня ещё есть кое-какие дела…"
    show Christie Chagrin
    "Кристи" "Хорошо…"
    show GG:
        xzoom -1
        easein 2 xalign -1.5
    $ renpy.pause(1, hard = True)
    scene black
    with Dissolve(.5)
    $ christie_root_56_loc = copy.deepcopy(location_now)
    $ location_now = "Corridor"
    $ renpy.pause(.5, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_211
    call show_additional_images_label from _call_show_additional_images_label_107
    
    
    show GG Think
    with my_dissolve
    if christie_root_56_loc in ("Sister_Room", "Kitchen"):

        show GG Think at go_from_left(xxalign = .5)
    else:
        show GG Think at go_from_right(xxalign = .5)

    #"ext" "// Kristy_Chagrin исчезает в сторону"
    
    "[gg]" "Было бы здорово устроить пикник."
    "[gg]" "Но…"
    "[gg]" "Я совсем не умею готовить."
    "[gg]" "Конечно, всегда можно купить готовую еду или фастфуд."
    "[gg]" "Только я хочу порадовать Кристи личными достижениями."
    "[gg]" "Хочется привнести в наши отношения что-то настоящее, без решения всех вопросов деньгами."
    "[gg]" "Хотя, на кое-что мне в любом случается придётся потратиться…"
    "[gg]" "Плед я точно сам не сошью, да и корзину из соломы сплести вряд ли получится… Хе-хе-хе."
    
    "[gg]" "А вот кушать – это пожалуйста. Хоть что-то я точно сделать осилю! "
    
    
    
    #"ext" " "
    
    
    
    python:
        try:
            del christie_root_56_loc
        except:
            pass

        descript_Christie = __("Купить продукты для пикника.")

        mishwanda_store_events_items.update({"christie_root_57":[57, ]})

        Event("christie_root_57", location = "After_StoreIn", need_items = [57, ])
        
        
    jump main_interface_label