label christie_root_42:
    if getattr(store, 'block_igor_position', False):

        $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")

        $ events['christie_root_42'].day_start = time.day_now + 1
        jump main_interface_label
        
    $ events.pop('christie_root_42', 0)
    #Description: Проведать Игоря в Парке и показать ему запись с продажным копом.
    # "A Task" ""
    # #Активировать Igor_Sprite в Park 
    call show_bg_image_label from _call_show_bg_image_label_199
    call show_additional_images_label from _call_show_additional_images_label_39 

    show Igor Normal
    show Igor Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_left
    # "Scene" ""
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/daily-beetle-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Игорь" "Эй!"
    show Igor Ok
    show GG:
        xalign .15
    with my_dissolve
    "Игорь" "Это же тот парень, который называет меня своим другом!"
    show Igor Ok
    "Игорь" "Как ваши беззаботные дела, мистер «Друг»?"
    show GG Think
    "[gg]" "Ты умный, но тупой."
    show GG Think
    "[gg]" "Ты видишь, но слепой."
    show GG Think
    "[gg]" "Ты слышишь, но глухой."
    show Igor Angry
    "Игорь" "Слыш, Сократ, а не пойти ли тебе нахуй?"
    show GG Smile
    "[gg]" "Пойду. Обязательно пойду. Сразу после тебя."
    show GG Passion
    "[gg]" "Вчера тебе помог клоун, который смачно долбанул кроссовком прям по башке полицейского, но судя по тому, что ты сейчас несёшь – большой красный нос тебе и самому не помешает."
    show Igor Smile
    "Игорь" "Нихерасе «сетап» и «панчлайн»."
    show GG Laughs
    "[gg]" "Раунд, сука!"
    show Igor Surprise
    "Игорь" "Так это был ты?!"
    show GG Normal
    "[gg]" "Ага."

    "Игорь" "А та отвязана Харли Квин кто?"
    show GG Normal
    "[gg]" "Кристи. "
    
    "Игорь" "Охренеть!"
    show GG Passion
    "[gg]" "И это ещё не все сюрпризы, чувак!"
    show Igor Troll
    "Игорь" "У меня аж жопа зачесалась. "
    show GG WTF
    "[gg]" "Я заснял, как сраный коп берёт взятку у двух продавцов травы на углу продуктового магазина. "
    show Igor Surprise
    show GG Laughs
    with my_dissolve
    "Игорь" "Да ладно?!"
    show GG Normal
    show Igor Troll
    with my_dissolve
    "[gg]" "Ага. Сейчас скину тебе на телефон. Может, используем это как-то в нашу пользу?"
    show Igor Normal
    "Игорь" "Почему нет? Нам всё пригодится."
    show GG Normal
    "[gg]" "Рад, что у тебя поднялось настроение."
    show Igor Say
    "Игорь" "Хорошие новости – как бальзам на душу. "
    show Igor Silence
    "Игорь" "Да и само твоё появление, знаешь ли, тоже приободрило меня немного. "
    show Igor Ok
    "Игорь" "История, в которую мы влепили… Все эти переделки… Этот мент постоянно в шею дышит…"
    show Igor Bad
    "Игорь" "А тут ещё, получается, надо горбатиться каждое утро, без денег и слов благодарности… "
    show Igor Angry
    "Игорь" "Дерьмо это короче, а не работа."

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/sunny-morning-by-musiclfiles-from-filmmusic-io.mp3', fadein = 1.5)
    show GG WTF
    "[gg]" "Слыш, чувак."
    show Igor Smile
    "Игорь" "А?"
    #//Встряска экрана
    scene image "cg/ep89/igor/f_1_bg.png"
    show image "cg/ep89/igor/f_1.png"
    with my_vpunch
    show image "cg/ep89/igor/f_1.png":
        #yalign .5
        ypos 1000
        easein .5 ypos 900
        easein .5 ypos 1050
        # easein .5 ypos 900
        # easein .5 ypos 1050
        
    #$ renpy.pause(9999)
        


    #//GG_Normal 
    #show Igor Silence
    #with my_dissolve
    
    "" "{i}[gg] пожимает руку Игорю{/i}"

    scene black with Dissolve(.4)
    $ renpy.pause(.5, hard = True)
    scene image 'cg/ep89/igor/f_3_bg.png':
        xalign 1.0
        easein 120 xalign .0
    show image 'cg/ep89/igor/f_2.png'
    show image 'cg/ep89/igor/f_2.png':
        xpos 450
        easein 70 xpos 1400 
    
    with my_dissolve

    "[gg]" "Спасибо, друг."

    scene image 'cg/ep89/igor/f_2_bg.png':
        xalign .0
        easein 120 xalign 1.0
    show image 'cg/ep89/igor/f_3.png'
    show image 'cg/ep89/igor/f_3.png':
        xpos 1400
        easein 70 xpos 300 
    
    with my_dissolve
    "Игорь" "….."
    
    "Игорь" "П-пожалуйста…"
    
    "Игорь" "Друг."
    scene image 'cg/ep89/igor/f_3_bg.png':
        xalign 1.0
        easein 120 xalign .0
    show image 'cg/ep89/igor/f_2.png'
    show image 'cg/ep89/igor/f_2.png':
        xpos 450
        easein 70 xpos 1400 
    
    with my_dissolve

    "[gg]" "…."
    scene image 'cg/ep89/igor/f_2_bg.png':
        xalign .0
        easein 120 xalign 1.0
    show image 'cg/ep89/igor/f_3.png'
    show image 'cg/ep89/igor/f_3.png':
        xpos 1400
        easein 70 xpos 300 
    
    with my_dissolve
    "Игорь" "….."
    #//Прежние спрайты
    scene black with Dissolve(.4)
    $ renpy.pause(.5, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_202

    show Igor Normal
    show Igor Normal:
        xalign .85
        ypos 1085


    
    show GG Normal
    show GG Normal: 
        xalign .15

    with my_dissolve
    "[gg]" "Ну, я пошёл."
    show Igor Normal
    "Игорь" "Давай."
    show Igor Normal
    "Игорь" "Вали."
    show GG Laughs
    "[gg]" "Ха-ха-ха! "
    show Igor Normal
    "Игорь" "Ха-ха-ха!!"
    
    #Tian_43
    
    call christie_root_try_to_del_descript_christie_block_igor from _call_christie_root_try_to_del_descript_christie_block_igor_1
    
    $ descript_Christie = _("Отправиться в магазин одежды. Желательно днём. Следует отвлечь продавщицу и проникнуть в туалетную комнату.")

    $ Event('christie_root_43', 'Store_Masha', day_start = time.day_now + 1)
    
    
    if not block_time_forward:
        $ time.time_now = 'evening'
    
    jump main_interface_label