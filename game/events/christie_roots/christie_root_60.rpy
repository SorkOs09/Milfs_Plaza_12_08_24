transform christie_root_60_mini_game_text_transform:
    xpos 0 ypos 0
    easein_cubic 1.0 xpos -10
    easein_cubic 1.0 xpos 0
    repeat
screen christie_root_60_mini_game:
    viewport:
        xmaximum 190
        ymaximum 190
        image 'images/tests/Timer.png' xalign .5 yalign .5 zoom .9
        xalign .5 ypos 10 
        text str(timer_now.time) xalign .5 yalign .5

    default ttr = 0
    default _plakat = 1
    #default dspl_img = renpy.display.core.displayable_by_tag("master", "GG")
   # text str(timer_now.time) xpos 800 ypos 300

    image 'GG Plakat_'+str(_plakat):
        ypos 192 
        #at transform:

         #   xalign .5 ypos 195 xzoom 0.0
            #linear 1.0 xalign .9

    image "characters/BlackGuy/EMO/Normal.png":
        if timer_now.time < 23 and timer_now.time > 15:
            at transform:
                xalign 1.25 ypos 0 
                easein_cubic 1.5 ypos 20
                easein_cubic 1.5 ypos 0
                repeat
        
        else:
            at transform:
                xalign 1.25 
                easein_cubic 1.5 ypos 0
                



    image "characters/bandit/EMO/Normal.png":
        if timer_now.time > 26 or (timer_now.time < 10 and timer_now.time > 5):

            at transform:
                
                xalign .9 ypos 0 xzoom -1.0
                easein_cubic 1.5 ypos 20
                easein_cubic 1.5 ypos 0
                repeat
        else:
            if timer_now.time > 23 or (timer_now.time < 15 and timer_now.time > 10) or (timer_now.time < 5 and timer_now.time > 1):
                at transform:
                    xzoom 1.0
            
            else:
                at transform:
                    xzoom -1.0
                    #easein_cubic 4.0 xalign -1.5
            

    # image Composite((300, 150), 
    #     #(0, 0), Solid("#000"),
    #     (0, 0), Frame(Transform('interface/comic_v2/bg_frame_2.png', alpha = .8), Borders(64, 64, 64, 64)),
    #     (90, 10), christie_root_60_mini_game_text_transform(child = Text(
    #                     __(" Бла\n  бла\nбла"), 
    #                     kerning  = 5,
    #                     size     = 40,
    #                     outlines = [(2, "#000a", 0, 0),],
    #                     font = "fonts/mango_comics_er.ttf",
                        
    #                     )),
    #     (1020, 60), Transform("comic_frame_say_3")
    #     )
    
    viewport:
        if timer_now.time > 26 or (timer_now.time < 10 and timer_now.time > 5):
            at transform:
                
                xpos 1480 ypos 230 alpha .0
                parallel:
                    easein_cubic 1.0 alpha 1.0
                
                parallel:
                    easein_cubic 1.5 ypos 240
                    easein_cubic 1.5 ypos 230
                    repeat
        else:
            at transform:
                

                easein_cubic 1.0 alpha 0.0 ypos 230

        xmaximum 240 ymaximum 180
        
        image "#0000"
        viewport:
            xmaximum 200 ymaximum 150
            xpos 40
            image Frame('interface/comic_v2/bg_frame_2.png', Borders(64, 64, 64, 64))
            text __("Бла") font "fonts/mango_comics_er.ttf":
                at transform:
                    xpos 40 ypos 20
                    easein_cubic 1.0 xpos 100
                    easein_cubic 1.0 xpos 40
                    pause 1.0
                    repeat

            text __("Бла") font "fonts/mango_comics_er.ttf":
                at transform:
                    xpos 40 ypos 60
                    easein_cubic 1.2 xpos 100
                    easein_cubic 1.2 xpos 40
                    pause .6
                    repeat

            text __("Бла") font "fonts/mango_comics_er.ttf":
                at transform:
                    xpos 40 ypos 100
                    easein_cubic 1.5 xpos 100
                    easein_cubic 1.5 xpos 40
                    repeat
        
        image Transform("comic_frame_say_3", xzoom = -1.0) ypos 65
            
    viewport:
        if timer_now.time < 23 and timer_now.time > 15:
            at transform:
                xpos 1620 ypos 150 alpha .0
                parallel:
                    easein_cubic 1.0 alpha 1.0
                
                parallel:
                    easein_cubic 1.5 ypos 30
                    easein_cubic 1.5 ypos 20
                    repeat
        
        else:
            at transform:
                

                alpha 0.0 ypos 20 xpos 100
        
        xmaximum 500 ymaximum 180
        image "#0000"
        viewport:
            xmaximum 500 ymaximum 150
            image Frame('interface/comic_v2/bg_frame_2.png', Borders(64, 64, 64, 64)) zoom .5
            $ j = 0

            hbox:
                xpos 20 ypos 20
                for i in __("Бла-Бла?"):
                
                    text i font "fonts/mango_comics_er.ttf":
                        if j%2:
                            at transform:
                                ypos 0
                                
                                easein_cubic 1.0 ypos -5
                                easein_cubic 1.0 ypos 0
                                #pause 3.0
                                repeat

                        else:
                            at transform:
                                ypos -5
                                
                                easein_cubic 1.0 ypos 0
                                easein_cubic 1.0 ypos -5
                                #pause 3.0
                                repeat

                    $ j += 1
            image Transform("comic_frame_say_1") xpos 50 ypos 72


    image 'images/tests/nark_2.png':
        at transform:
            xalign 1.4 yalign 1.2 xzoom -1.0
            easein_cubic 2.5 xalign .6
            xzoom -1.0
            
            ease 1.0 yalign 1.4 xalign .45
            pause 5.5
            xzoom 1.0
            
            easein_cubic 3.5 xalign 1.4 yalign 1.2

            repeat
    image 'images/tests/nark.png':
        at transform:
            xalign 1.4 yalign 1.1 xzoom -1.0
            easein_cubic 4.5 xalign .5
            ease 1.0 yalign 1.3 xalign .55
            pause 5.5
            xzoom 1.0
            
            easein_cubic 5.5 xalign 1.4 yalign 1.1

            repeat
    image 'images/tests/nark.png':
        at transform:
            
            xalign .4 ypos 100 xzoom -1.0
            ease 1.0 xalign .35 ypos 200 rotate -10
            pause 5.5
            xzoom 1.0 


            easein_cubic 2.5 xalign 2.4 ypos 200 rotate 1 ypos 100
            xzoom -1.0
            easein_cubic 2.5 xalign .4

            repeat
        



    add timer_now xpos -850 ypos -1000
        
    if (timer_now.time > 23 and timer_now.time < 27) or (timer_now.time < 15 and timer_now.time > 10) or (timer_now.time < 5 and timer_now.time > 1):
        if _plakat == 1:
            imagebutton:
                xpos 100
                ypos 800
                idle 'circle_mini_game'
                hover 'circle_mini_game'
                xanchor .5
                yanchor .5
                focus_mask None
                at circle_mini_game_transform(2.0)
                action SetScreenVariable("_plakat", 2)

            timer 2.0 action Return(0)
        

        image 'shadow_full':
            if _plakat == 1:
                at transform:
                    alpha .0
                    easein_cubic 2.0 alpha 1.0
            
            else:
                at transform:
                    
                    easein_cubic .5 alpha 0.0
            
    else:
        timer .1 action SetScreenVariable("_plakat", 1)
        #use qte_mini_game(ttimer = 2, shake = True)
    #     image Transform("comic_frame_say_1") xpos 40 ypos 75

    #text str(dspl_img) ypos 300


#screen christie_root_60_mini_game_buttons:
    #add 'images/tests/Timer.png' xalign .5 ypos 10 zoom .9
    #add timer_now xpos -850 ypos -870



           # if dspl_img is not None:



label christie_root_60:
    $ events.pop('christie_root_60', 0)
    call show_bg_image_label from _call_show_bg_image_label_212
    with Dissolve(.5)
    #Отправиться в Гетто Утром или Днём с плакатом, полученным от Зудилы и Бубнилы.
    #"ext" "Активировать Гетто Утром или Днём."
    show GG Plakat_1
    show GG Plakat_1 at go_from_left(xxalign = .5)
    #"" "{color=#F00}GG PlakatNormal{/color}"
    "[gg]" "Уф… От одного только вида окрестностей мне уже как-то не по себе. "
    
    "[gg]" "Стоит вновь проговорить нюансы… "
    show GG:
        xalign .5
    with my_dissolve

    "[gg]" "Первое. Плакат предназначен для местных торчков. "
    
    "[gg]" "Именно им я и должен его демонстрировать. "
    
    "[gg]" "Второе. Если объявятся «смотрящие» - местные бугаи, что охраняют барыг от ограбления или копов, плакат нужно прятать!"
    
    "[gg]" "Как и от самих копов, я полагаю… У них могут возникнуть ко мне вопросы. "
    
    "[gg]" "Но делать им здесь нечего, так что строго следую плану."
    
    "[gg]" "Ну и третье – не увлекаться. "
    
    "[gg]" "Достаточно показать плакат как можно большему числу торчков и валить отсюда."
    show GG Plakat_1:
        xzoom -1.0
        ease .75 xalign 0.0 ypos 1087
        xzoom 1.0
    "[gg]" "Всё, погнали!"
    show GG Plakat_1:
        xalign 0.0 ypos 1087
        xzoom 1.0
    with my_dissolve
    #"ext" "//
label christie_root_60_game:


    $ timer_now = TimerClassSellGame(30, "christie_root_60_win", True)
    call show_bg_image_label from _call_show_bg_image_label_208
    hide GG Plakat_1
    with my_dissolve
    call screen christie_root_60_mini_game
    scene black with my_vpunch
    "" "Миссия проваленна"

    menu:
        "Попровать снова":
            $ pass
        "Вернуться в главное меню":
            $ renpy.full_restart()
    jump christie_root_60_game
label christie_root_60_win:
    #"ext" "//При успешном показе, будет заполняться соответствующая шкала"
    #"ext" "//Если показывать НЕ ТУ сторону плаката для торчков, то шкала немного падает."
    #"ext" "//Если показать НЕ ТУ сторону плакала бандосов, то это авто-проигрышь"
    #"ext" "//Для торчков это одна сторона плаката, для бандосов – другая"
    #"ext" "//Спрайт с ГГ я нарисую, торчки у нас есть, бандосы тоже"
    
    #"ext" "//При успешном завершении мини игры"
    
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    scene black with Dissolve(.1)
    $ renpy.pause(.2, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_209
    show GG Plakat_Smile
    show GG Plakat_Smile:
        xalign .5 ypos 1080
        
    with my_dissolve
    "[gg]" "Вау, кажется пронесло."
    
    "[gg]" "Пора сваливать."
    #"ext" "//GG_Plakat_Normal отезжает в правый край"
    #"ext" "//Officer_Normal появляется слева"
    show GG Plakat_Surprise:
        #xzoom -1
        .3
        easein 1 xalign .9
    show Officer Normal
    show Officer Normal at go_from_left(xxalign = .2)
    show shadow_full
    with my_dissolve
    "Officer" "Стоять! Не двигаться! "
    

    show GG Plakat_Surprise:
        xalign .9
    with my_dissolve
    "[gg]" "Стою. Не двигаюсь."
    show Officer Normal:
        xalign .2
    with my_dissolve
    "Officer" "Теперь медленно, со скоростью замедленной съёмки, повернись в мою сторону."
    #"ext" "//GG_Plakat_Surprise разворачивается в сторону офицера"
    
    show GG:
        xzoom -1
    hide shadow_full
    with Dissolve(.5)
    $ renpy.pause(.5)
    with my_vpunch
    "[gg]" "Офицер?.."
    show Officer Surprise
    with my_vpunch
    "Officer" "[gg]!"
    show Officer Angry
    "Officer" "Так и знал, мелкий ублюдок, что ты найдёшь способ попасть в тюрьму пораньше. "
    
    "[gg]" "Но я ничего не…"
    #show Officer Normal
    "Officer" "Заткнись. Всё что ты скажешь, может и будет использовано против тебя в суде."
    #show Officer Normal
    "Officer" "Открывать рот будешь только по команде! А команды здесь даю я! Усёк?!"
    show GG Plakat_Angry
    #"" "{color=#F00}GG PlakatAngry{/color}"
    
    "[gg]" "Мгу…"
    show Officer Normal
    "Officer" "Подойди ближе и рассказывай, что это за дебильный плакат на тебе?"
    
    show GG Plakat_WTF
    #"" "{color=#F00}GG PlakatWtf{/color}"
    
    "[gg]" "Рекламный баннер. Небольшая подработка…"
    show Officer Angry
    "Officer" "Больше похоже на какую-то провокацию."
    
    "[gg]" "Я кто, по вашему, самоубийца?"
    show Officer Normal
    "Officer" "Тоже верно… "
    #show Officer Normal
    "Officer" "Ну и что ты рекламируешь?"
    
    "[gg]" "Эм… Средство от запора."
    #show Officer Normal
    "Officer" "Понятно."
    #show Officer Normal
    "Officer" "Самое время им воспользоваться, [gg], так как я не верю ни единому твоему слову."
    #"ext" "GG_Plakat_Angry"
    show GG Plakat_Angry
    show Officer Angry
    "Officer" "Снимай с себя этот картон."
    show black
    with Dissolve(.2)
    $ renpy.pause(.5, hard = True)
    hide black
    show GG Angry
    with my_dissolve
    "[gg]" "Готово."
    show Officer Normal
    "Officer" "Сейчас мы отправимся в участок, и я составлю на тебя протокол."
    #show Officer Normal
    "Officer" "А ты, уж давай, пока будем идти, придумай историю поубедительнее…"
    show Bandit Normal
    show BandtiWithPistol WTF
    show GG Surprise:
        easein 1 xalign 1.1

    show Officer:
        easein 1 xalign .7
        xzoom -1
    
    show Bandit at go_from_left(xxzoom = -1, xxalign_start = -1.5, xxalign = -.2)
    show BandtiWithPistol at go_from_left(xxzoom = -1, xxalign_start = -1.5, xxalign = .2)
    
    #"ext" "//Bandit_1 выезжает слева"
    #"ext" "//Bandit_2 выезжает слева"
    #"ext" "// Officer_Normal движется вправо, и поворачивается к бандитам"
    "Качок" "Ух ты..! "
    "Качок" "Кого я вижу! "
    "Качок" "Фараон в гетто посреди ночи – вот так улов! "
    show BandtiWithPistol:
        xalign .2
    show Bandit:
        xalign -.2
    show GG:
        xalign 1.1

    show Officer Angry:
        xalign .7 xzoom -1
    with my_dissolve
    "Officer" "Да вы…"
    show BandtiWithPistol Normal:
        easein 1 xalign .3
    show Officer Surprise:
        easein 1 xalign .75
    "Бандит" "Не вздумай рыпаться, придурок. "
    "Качок" "Мой приятель немного дёрганый. "
    "Качок" "Лучше не бесить его, если не хочешь, чтобы он оставил в тебе пару узорчатых отверстий."
    "Качок" "Слыш, парниша в футболке, вали отсюда.  "
    "Качок" "Сегодня нам есть с кем порезвиться, хы-хы-хы."
    #"ext" "//Officer_Normal поворачивается к ГГ"
    show Officer Hm:
        xzoom 1
    "Officer" "[gg], не бросай меня. Слышишь… Я же коп. "
    
    "Officer" "Если ты уйдёшь, это будет считаться как соучастие в преступлении. "
    show GG Skepticism:
        easein 1.0 xalign 1.5
    
    "[gg]" "Пошёл ты в жопу!"
    #"ext" "// GG_Skepticism исчезает вправо"
    #"ext" "//Бандит приближается к менту"
    show Bandit:
        easein 3 xalign .25
    show BandtiWithPistol Passion:
        easein 2 xalign .8
    show Officer Surprise:
        xzoom -1
        easein 2 xalign 1.15
    show shadow_full:
        alpha .0
        easein 1 alpha 1.0
    "Качок" "Сколько я зарезал… Сколько перерезал…"
    #"ext" "//Бандит приближается к менту ещё ближе"
    "Бандит" "Сколько душ я загубил… Хе-хе-хе!"

label christie_root_60_kick:
    hide shadow_full with my_dissolve
    
    $ i = renpy.call_screen('circle_mini_game_screen', xp = 500, yp = 300, tm = 10)
    if not i:
        jump christie_root_60_kick


    
    $ christie_root_60_kick_1 = Transform('tests/ep805/gg_1.png', xzoom = -1)
    $ christie_root_60_kick_0 = Transform('tests/ep805/gg_0.png', xzoom = -1)



    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    play audio 'audio/kick.mp3'


    #"[gg]" "Получай, засранец!"

    #scene expression 'tests/ep805/bg_blur.png'
    hide Bandit
    show Bandit
    show Bandit WTF:
        xzoom -1 rotate_pad False xpos 700 ypos 1080


    show image christie_root_60_kick_1
    show image christie_root_60_kick_1:
        xpos -1050
    show image christie_root_60_kick_0
    show image christie_root_60_kick_0:
        xpos -900

    show BandtiWithPistol WTF:
        xzoom 1
    show white
    with None
    $ renpy.pause(.05, hard = True)
    show BandtiWithPistol:
        ypos 1080
        easein_cubic 1 xalign .9
    show Officer Chagrin:
        easein_cubic 1 xalign 1.2
    show Bandit:
        easein_cubic 4.5 rotate 30 xpos 1000 ypos 1500
    show image christie_root_60_kick_1:
        alpha 1.0
        easein_cubic 2.5 alpha .0 xpos -50
    show image christie_root_60_kick_0:
        easein_cubic 2 xpos 0
    
    show white:
        alpha 1.0
        linear .5 alpha .0




    $ renpy.pause(1.0, hard = True)

    #hide image christie_root_60_kick_0
    #hide image christie_root_60_kick_1
    show Bandit:
        easein_cubic 2 alpha 0.0
    show Officer Chagrin:
        easein_cubic .5 xalign 1.35
    $ renpy.pause(.5, hard = True)
    play audio 'audio/kick.mp3'
    show Officer Kick:
        easein_cubic 1.0 xalign .85
    show BandtiWithPistol:
        ypos 1080
        parallel:
            easein_cubic 1 xalign .4 alpha 0.0
        parallel:
            .1
            easein_cubic 1.5 ypos 1250 
    $ renpy.pause(.1)
    with my_vpunch

    # hide expression 'tests/ep805/ment_1.png'
    # hide expression 'tests/ep805/milf_0.png'
    # hide expression 'tests/ep805/gg_0.png'
    # hide expression 'tests/ep805/gg_1.png'
    # show expression 'cg/ep5/jlob/7.png'
    # show expression 'tests/ep805/ment_2.png'
    # show expression 'tests/ep805/milf_0.png'
    # show expression 'tests/ep805/milf_0.png':
    #     xpos 650

    #show expression Transform('cg/ep5/jlob/7.png', xzoom = -1)
    $ renpy.pause(1.0, hard = True)
    scene black
    with vpunch
    $ renpy.pause(.5, hard = True)
    #"ext" "//GG вылетает слева и бьёт одного бандоса"
    #"ext" "//Бандит с пушкой разворачивается на ГГ"
    #"ext" "//Мент бьёт бандоса с пушкой"
    call show_bg_image_label from _call_show_bg_image_label_213
    show GG Normal
    show GG Normal:
        xalign .2
    show Officer Chagrin
    show Officer Chagrin:
        xalign .8 xzoom -1
    with my_dissolve_long
    "Officer" "Ты…"
    show GG Smile
    "[gg]" "Ага, спас твою дырявую задницу."
    show GG Smile
    "[gg]" "Теперь ты мой должник."
    show Officer Normal
    "Officer" "…."
    show GG Smile
    "[gg]" "Я думаю, нам лучше поскорее разойтись. "
    show GG Smile
    "[gg]" "Мало ли, какие ещё приключения нас могут поджидать здесь. "
    show GG Laughs
    "[gg]" "Мой лимит на удачу не бесконечен."
    show Officer Say
    "Officer" "Согласен."
    #"ext" "//Officer_Normal исчезает влево"
    #"ext" "//GG_Smile исчезает вправо"
    
    show GG:
        easein_cubic 4 xalign 1.5
    show Officer:
        easein_cubic 6 xalign -1.5
    $ renpy.pause(.5, hard = True)
    scene black
    with Dissolve(.5)

    $ renpy.pause(.75, hard = True)

    $ location_now = "City_Home"
    $ time.time_now = "night"
    call show_bg_image_label from _call_show_bg_image_label_214
    with my_dissolve
    show GG Normal
    show GG Normal at go_from_left(xxalign = .5, ttimer = 2)
    #"ext" "Stree_Night"
    
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Фьюх… Чуть не влетело."
    "[gg]" "Ещё и этот офицер откуда ни возьмись…"
    #"ext" 

    $ sms_now = SmsBlock('Сьюзан', 'Susan', "60", Jump('christie_root_60_1'))

    
    $ sms_now.add_sms(_("TT: [gg], умоляю, это вопрос жизни и смерти!!!"))
    $ sms_now.add_sms(_('GG: Я уже всё вам сказал, Сьюзен,\nпрекратите меня донимать.\n'))
    $ sms_now.add_sms(_("TT: Если бы ты знал, как это важно,\nты бы понял меня.\n"))
    $ sms_now.add_sms(_("TT: Но я не могу сказать\nэто в переписке.\n"))
    $ sms_now.add_sms(_("TT: Клянусь, это последняя просьба!\n"))
    
    $ sms_now.add_sms(_("GG: Вы вынуждаете меня\nзаблокировать ваш номер.\n"))
    if preferences.language in (None, 'eng', 'rus'):
        $ sms_now.add_sms(_("GG: Прощайте."))
    
    
    #$ location_now = 'StoreIn'
    #call show_all_images_label
    #with my_dissolve
    #$ check_ev = True
    $ unlock_city_getto = False

    $ events.pop('christie_root_60', 0)
    $ descript_Christie = __("Прочесть смс.")
    jump main_interface_label
    

   # "" "{color=#F00}SMS_Mobile закрывается{/color}"
label christie_root_60_1:
    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    show GG Think
    show GG Think:
        xalign .5
    with my_dissolve
    "[gg]" "Боже, какая же она прилипчивая."
    
    "[gg]" "Всё, добавил её в игнор."
    "[gg]" "Пусть сама разбирается."
    
    
    $ Event("christie_root_61", "JayBobTalk")
    
    
    $ descript_Christie = __("Забрать у Зудилы и Бубнилы причитающуюся награду. ")

    jump main_interface_label