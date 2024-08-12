label christie_root_50:
    #Description: Установить мобильный телефон возле телевизора в Зале Ночью, пока никто не видит.
    
    #Активировать тумбу под телевизором в зале.
    $ location_now = 'Hall'
    call show_bg_image_label from _call_show_bg_image_label_192
    show image 'cg/gg_activities/active_camera_cg.png'
    with my_dissolve
    "[gg]" "Надо установить мобильный телефон возле телевизора, пока никто не видит." 

    "[gg]" "Хм… Вроде незаметно. "
    call show_bg_image_label from _call_show_bg_image_label_193
    
    show GG Think
    show GG Think:
        xalign .5

    with my_dissolve
    "[gg]" "Теперь остаётся только ждать."
    #//GG_Think исчезает влево

    #MyRooNight

    #//GG_Think появляется слева


    "[gg]" "Пора спать."

    "[gg]" "Утром и узнаю, получилось у меня или нет."
    #//Экран затухает
    $ Event('christie_root_50_1', day_start = time.day_now + 1)


    $ descript_Christie = _("Пора спать. Утром и узнаю, получилось у меня или нет.")
    jump main_interface_label

label christie_root_50_1:
    scene black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    $ events.pop('christie_root_50_1', 0)
    $ location_now  = 'GG_Room'
    $ time.time_now = 'morning'

    call show_bg_image_label from _call_show_bg_image_label_194

    show GG Think
    show GG Think:
        xalign .5
    with my_dissolve
    "[gg]" "Я почти не спал, только и думал о том, оголилась Кристи или нет…"
    show GG Skepticism
    "[gg]" "Блин."
    show GG Skepticism
    "[gg]" "Меня гложет совесть."
    show GG Embarrassment
    "[gg]" "Последнее время она сильно доверяет мне, а я, зачем-то, пытаются тайным образом заснять её голой. "
    show GG Embarrassment
    "[gg]" " И ладно бы я это делал для себя, не из корысти, а из чувства похоти."
    show GG Embarrassment
    "[gg]" "Тоже, конечно, аргумент сомнительный… Но снимать видео Кристи для друга?"
    show GG Angry
    "[gg]" "Даже для лучшего друга – это подло, чёрт меня дери. Сравнимо с предательством!"
    show GG Angry
    "[gg]" "Я поступаю как полный гандон. "
    show GG Chagrin
    "[gg]" "И если где-то всплывёт ролик, и Кристи узнает о нём, она никогда меня за это не простит ."
    show GG Angry
    "[gg]" "Нет, так делать нельзя. Надо во всём сознаться и объяснить сложившуюся ситуацию! "


    $ block_sister_home_christie_root_50 = copy.deepcopy(block_sister_home) 
    $ block_sister_home = True
    

    $ block_milf_home_christie_root_50 = copy.deepcopy(block_milf_home) 
    $ block_milf_home = True
    
    $ block_exit_home_christie_root_50 = copy.deepcopy(block_exit_home)

    $ block_exit_home = True

    $ block_time_forward_christie_root_50 = copy.deepcopy(block_time_forward)
    $ block_time_forward = True

    if not hasattr(store, 'allowed_events'):
        $ allowed_events = []
    
    $ allowed_events.append('christie_root_50_2')

    $ descript_Christie = _("Надо во всём сознаться и объяснить сложившуюся ситуацию!")
    
    $ Event('christie_root_50_2', 'Hall', time = ['morning', ])

    jump main_interface_label
    #//GG_Normal исчезает влево
label christie_root_50_2:
    $ events.pop('christie_root_50_2', 0)
    $ allowed_events.remove('christie_root_50_2')
    call show_bg_image_label from _call_show_bg_image_label_195
    with my_dissolve

    $ events.pop('christie_root_50_2', 0)
    show GG Normal
    show GG Normal at go_from_left(xxalign = .2)
    #//Зал

    #//GG_Normal появляется слева

    "[gg]" "Кристи ушла? Как странно. Я думал, успею застать её в оголённом или, хотя бы, полуголом виде, хе-хе."
    show GG Normal
    "[gg]" "Надо проверить телефон."
    #//GG_Normal движется вправо, ближе к тумбе

    show GG:
        easein 1 xalign .7
    $ renpy.pause(1, hard = True)
    show GG Think:
        xalign .7
    with my_dissolve
    "[gg]" "Вот так вот, смартфон упал экраном вниз и, вероятно ничего не заснял."
    
    "[gg]" "Да, так и есть, на видео запись чёрного экрана."
    
    "[gg]" "Но где же сама Кристи?"
    
    $ Event('christie_root_50_3', 'Kitchen')
    $ allowed_events.append('christie_root_50_3')

    jump main_interface_label
    #//GG_Normal исчезает влево
label christie_root_50_3:
    python:
        try:
            block_sister_home = copy.deepcopy(block_sister_home_christie_root_50) 
            del block_sister_home_christie_root_50
        
        except:
            block_sister_home = False   
    
        try: 
            block_milf_home   = copy.deepcopy(block_milf_home_christie_root_50) 
            del block_exit_home_christie_root_50
        except:
            block_milf_home = False

        try:
            block_exit_home   = copy.deepcopy(block_exit_home_christie_root_50)
            del block_milf_home_christie_root_50
        except:
            block_exit_home = False


 

    $ allowed_events.remove('christie_root_50_3')

    #//Кухня

    #//GG_Normal выезжает справа

    #//Спрайт Kristy_Nude_Water пьёт воду, где по ней стекают струйки воды

    call show_bg_image_label from _call_show_bg_image_label_196
    show image 'cg/ep89/Christie_drink_water.png'
    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)


    show christie_root_15_gg
    show christie_root_15_gg:
        xpos 1100
        easein_cubic 1 xpos 960

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Довёл бедную девочку до изнеможения…"
    #show GG Embarrassment
    show christie_root_15_gg:
        xpos 960
    "[gg]" "До сексуального изнеможения."
    #show GG Embarrassment
    "[gg]" "Как же приятно наблюдать за тем, как капли холодной воды растекаются по её телу."
    #show GG Embarrassment
    "[gg]" "В такие моменты я осознаю красоту женского тела как выдающееся творение природы. "
    #//Спрайт Kristy_Nude_Water  исчезает

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/daily-beetle-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    call show_bg_image_label from _call_show_bg_image_label_197
    show Christie Angry
    show Christie Angry:
        xalign .2 xzoom -1
    with my_vpunch
    "Кристи" "Эй, ты снова подсматриваешь за мной?"
    show GG Passion
    show GG Passion at go_from_right(xxalign = .8, xxzoom = -1)
    
    "[gg]" "Не подсматриваю, а наслаждаюсь. "
    show Christie Smile
    "Кристи" "Тогда ладно, [gg]."#/*братик
    show GG Passion:
        xalign .8 xzoom -1
    "[gg]" "Хотел тебе кое в чём сознаться. С поличным, так сказать…"
    show Christie Skepticism
    "Кристи" "Я обижусь или нет?"
    show GG Normal
    "[gg]" "Главное, что ты узнаешь правду. "
    show Christie Normal
    "Кристи" "Хорошо, я слушаю."
    show GG Chagrin
    "[gg]" "Чтобы взломать телефон, мне нужна была помощь Игоря."
    show Christie Skepticism
    "Кристи" "Извращенца."
    show GG Chagrin
    "[gg]" "Моего друга."
    show Christie Skepticism
    "Кристи" "Я так и сказала."
    show GG Normal
    "[gg]" "Так вот он, в качестве платы, запросил видео с тобой в главной роли, где ты должна быть без одежды"
    show Christie Skepticism
    "Кристи" "Он ещё более сумасшедший, чем я думала… А ты? Что ты сделал?"
    show GG Embarrassment
    "[gg]" "Я согласился."
    show Christie Surprise
    "Кристи" "Чего?!! Как ты мог?!"
    show GG Embarrassment
    "[gg]" "Знаю-знаю, я не имел права… Но я так привык действовать вне моральных принципов, что согласился по инерции. "
    show GG Embarrassment
    "[gg]" "И почти осуществил план…"
    show Christie Angry
    "Кристи" "Какого чёрта, [gg]?! "
    show GG Chagrin
    "[gg]" "Извини, я конченый придурок. "
    show GG Chagrin
    "[gg]" "И прекрасно пойму, если больше ты не захочешь со мной общаться. "
    show Christie Angry
    "Кристи" "Твою мать… [gg], как же ты всё любишь усложнять на ровном месте!"
    show Christie Chagrin
    "Кристи" "Я думала, ты меня любишь, а ты использовал меня как вещь для достижения собственных целей!"
    show GG Chagrin
    "[gg]" "…Наших целей."
    show Christie Angry
    "Кристи" "Ну да, это же всё меняет!"
    show Christie Angry
    "Кристи" "Почему ты сразу не сказал, что Игорь потребовал у тебя такую плату?"
    show GG Chagrin
    "[gg]" "Я уже объяснил, извини. "
    show Christie Angry
    "Кристи" "Чёрт! Чёрт!! Чёрт!!!"
    show Christie Angry
    "Кристи" "Как же сложно тебя любить!"
    show GG Chagrin
    "[gg]" "…."
    show GG Chagrin:
        xzoom 1
    "[gg]" "Ладно, я пойду…"
    show Christie Angry
    with my_vpunch
    "Кристи" "Иди!"
    show GG Chagrin:
        easein 2 xalign 1.5
    "[gg]" "Извини ещё раз."

    scene black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)

    $ location_now = 'GG_Room'

    call show_bg_image_label from _call_show_bg_image_label_198
    with my_dissolve

    show GG Chagrin
    show GG Chagrin at go_from_left(xxalign = .5)
    
    #//GG_Chagrin исчезает вправо

    #//MyRoomDay

    #// GG_Chagrin появляется слева

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/lo-fi-hip-hop-02-by-winniethemoog-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Этого следовало ожидать. "
    #// GG_Chagrin исчезает

    #//GG_Sit_Cry_1

    show GG Chagrin:
        xalign .5
    with my_dissolve
    "[gg]" "Какой же я баран…"
    "[gg]" "Кристи права, я должен был сразу сознаться. "
    "[gg]" "Почему, сука, почему я это скрыл?!"
    "[gg]" "Не потому ли, что на самом деле я никак не изменился?"
    "[gg]" "Я по прежнему готов идти по головам близких, только бы достичь желаемой цели."
    "[gg]" "Ощущение добропорядочности во мне, как враждебный организм, нивелируется под давлением общей мерзотности. "
    "[gg]" "Я противен сам себе…"
    "[gg]" "Сеансы у Сьюзен ни к чему не привели. Лишь дали мнимую надежду, будто бы у меня есть шансы на исправление. "
    "[gg]" "Но нет, это всё туфта!.."
    "[gg]" "Разводка для лохов, которые платят бабки ради утешения. "
    "[gg]" "Нужно знать своё место в обществе и…"
    #//GG_Sit_Cry_2

    show Christie Chagrin
    show Christie Chagrin:
        xalign -1.5 xzoom -1
        easein_cubic 1 xalign .2
    show GG:
        easein_cubic 1 xalign .8
        xzoom -1
    "Кристи" "Ну и какое видео желает этот извращенец? "
    "[gg]" "Я не…"
    show Christie Angry:
        xzoom -1 xalign .2
    show GG:
        xalign .8 xzoom -1
    with my_dissolve
    "Кристи" "Говори, иначе уйду."
    "[gg]" "Прости, но я не могу."
    "Кристи" "Не будь идиотом, тебе нужно закончить сделку. "
    "[gg]" "Это бессмысленно, Кристи. "#/*сестрёнка
    "[gg]" "Я заключил бартер со Сьюзен, чтобы она помогла мне наладить с тобой отношения, сделать меня другим человеком, но средство достижения цели стало для меня важнее самой цели."
    "[gg]" "Я предал тебя, сделал больно. Я просто тупой мудак."
    show Christie Skepticism
    with my_dissolve
    "Кристи" "Ты тупой, да, но не мудак."
    show Christie Normal
    with my_dissolve
    "Кристи" "Во-первых, ты сознался. Это важно."
    "Кристи" "Во-вторых, невозможно измениться по щелчку пальцев, и психотерапия со Сьюзен очень помогла тебе."
    show GG Embarrassment
    with my_dissolve
    "Кристи" "Теперь ты отдаёшь отчёт в том, к каким последствиям приводят твои действия."
    "Кристи" "И самое главное – тебе это неприятно. Ты испытываешь угрызение совести"
    "Кристи" "Тебя так сильно это тревожит, что ты, не выдерживаешь и СОЗНАЁШЬСЯ в этом!"
    show Christie Smile
    with my_dissolve
    "Кристи" "А значит, ты изменился. Стал более честным, искреним… хорошим, понимаешь? "
    "[gg]" "Значит, ты меня простила?.."
    show Christie Laughs
    with my_dissolve
    "Кристи" "Конечно простила, [gg]. "#/*братик
    "Кристи" "А теперь хватит распускать нюни, и просто скажи, какое видео затребовал Игорь?"
    "[gg]" "Ну… В идеале, наверное, он ожидает некий стриптиз. Где ты снимаешь или одеваешь на себя одежду… Что-то такое, в общем. Эротичное. "
    show Christie Embarrassment
    with my_dissolve
    "Кристи" "Хм… Понятно."
    show Christie Passion
    with my_dissolve
    "Кристи" "Ну, тогда не будем разочаровывать твоего друга, раз уж успех нашей операции зависит от того, взломает он телефон или нет. "
    show GG Surprise
    with my_dissolve
    "[gg]" "Э….?"
    "Кристи" "Теперь я командую порадом!"
    "Кристи" "Купи мне костюм, [gg]. На твой вкус, разумеется, но достаточно подходящий, чтобы было интересно его снимать."
    "Кристи" "Уяснил?"
    "[gg]" "Ага."
    with my_vpunch
    "Кристи" "Тогда чего сидишь? Вперёд!"
    #"Time" "Evening"
    
    
    
    #//Обязательно сделать сцену с анальным сексом. Описание ниже

    
    # 

    #//Так же в доп.квесте с Кристи, 
    #где ГГ заменяет фалос на свой член Кристи понимает, 
    #что это Член ГГ и не позволяет ему проникать в себя, а просто трётся половыми губами об его детородный орган

    
    $ christie_root_50_end = True

    # #//Текст для сцены с аналом в комнате Кристи.

    # #//На определённом моменте туда зайдёт Милфа (или нет)

    # "Кристи" "Однако я очень хочу почувствовать тебя внутри. По-настоящему. Понимаешь?"
    # "[gg]" "Догадываюсь, хех…"
    # "Кристи" "Стыдно говорить об этом вслух, если честно."
    # "[gg]" "Можешь написать."
    # "Кристи" "Нет, это ещё глупее… Я должна сказать сама. "
    # "[gg]" "Хорошо, я не тороплю."
    # "Кристи" "Тебе ведь нравится моя попка, правда?"
    # "[gg]" "Я от неё без ума."
    # "Кристи" "Ну… Тогда…"
    # "[gg]" "Я уже догадался. "
    # "Кристи" "Знаю, но я хочу произнести это вслух."
    # "[gg]" "…."
    # "Кристи" "Я очень хочу, чтобы ты трахнул меня в попку, [gg]."
    # "Кристи" "Я жажду этого с того момента, как ты впервые прикоснулся к моей коже, намереваясь сделать массаж ног."
    # #//Kristy_GG_Anal_1

    # "[gg]" "О боже.."
    # "[gg]" "Чтобы сравнится с этим подарком, мне нужно было бы скупить весь книжный магазин."
    # "Кристи" "Только будь очень нежным, пожалуйста…."
    scene image '#000' with Dissolve(.5)


    $ time.time_now = 'evening'
    
    $ descript_Christie = _("Конец рута Кристи для эпизода 0.8.9")

    python:
        try:
            block_time_forward = copy.deepcopy(block_time_forward_christie_root_50)

            del block_time_forward_christie_root_50
        except:

            block_time_forward = False
    call christie_root_50_end_label from _call_christie_root_50_end_label_1
    call christie_root_51_0 from _call_christie_root_51_0_1
    jump main_interface_label



label christie_root_50_end_label:

    $ events.pop('christie_root_50', 0)
    $ events.pop('christie_root_50_1', 0)
    $ events.pop('christie_root_50_2', 0)
    $ events.pop('christie_root_50_3', 0)

    $ events.pop('christie_root_48', 0)
    $ events.pop('christie_root_49', 0)

    $ christie_root_50_end_2 = True

    return