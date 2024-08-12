image secret_final 1 = 'cg/final_act/morgue/end/1.png' 
image secret_final 2 = 'cg/final_act/morgue/end/2.png' 
init python:
    def _end_credits_screen_def():
        pass
        if store.end_credits_screen_clicks < 3:
            store.end_credits_screen_clicks += 1
            renpy.music.stop(channel = "ero", fadeout=.5)
            if store.end_credits_screen_clicks == 1:
                renpy.music.play('audio/heart_beat_1_3.mp3', fadein = 1.5)
            elif store.end_credits_screen_clicks == 2:
                renpy.music.play('audio/heart_beat_1_5.mp3', fadein = 1.5)
            elif store.end_credits_screen_clicks == 3:
                renpy.music.play('audio/heart_beat_1_75.mp3', fadein = 1.5)
            renpy.restart_interaction()
        else:
            add_ach('ACH_19')

            #achievement.grant("ACH_19")
            #achievement.sync()

            Jump('final_act_25_secret_final')()


transform end_credits_transform:
    #on show:
    xalign .5 ypos 300 alpha 0.0
    
    parallel:
        easeout 1.5 alpha 1.0
    parallel:
        pause  2.0
        linear 30 ypos -2000
image _pre_end_1_blur = 'cg/final_act/morgue/pre_end/1_blur.png'
screen end_credits_screen_bg:
    zorder 30
    viewport:
        maximum (1920, 1080)

        if hasattr(store, 'end_credits_screen_clicks'):
            
            
            imagebutton:
                idle  'alpha_solid'
                hover 'alpha_solid'
                action Function(_end_credits_screen_def)
            # image _pre_end_1_blur:
            #     zoom 2.1 pos (0, -550)
            #     alp
        #else:
        #    at transform:
        #        alpha 0.0
        #        easeout 1.5 alpha 1.0
            image 'cg/final_act/morgue/pre_end/1_blur.png':
                zoom 2.1 pos (0, -550)
                if hasattr(store, 'end_credits_screen_clicks'):
                    alpha 1.0-(end_credits_screen_clicks*.25)

        #if hasattr(store, 'end_credits_screen_clicks'):
            #text "!!!" + str(end_credits_screen_clicks)
            image 'shadow_full': 
                alpha end_credits_screen_clicks*.12
screen end_credits_screen:
    zorder 40
    use credits_screen(
            # pr_xalign=.5, pr_yalign=.5,
            pr_transform = end_credits_transform, 
            pr_outlines=[(3, '#000c', 0, 0)], 
            pr_size = 70,
            pr_spacing = 30,
            )
       
        
            
label final_act_25_0:
    $ Location(
        'Prison',
        buttons = [
        {

        }
        ]
        )
    $ location_now = 'Prison'

    $ locations['Prison'].buttons[0].update({
        'toilet':(
            (1000, 470, 220, 350), [Jump('prison_toilet_label')])
            }
            )
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/night.mp3', fadein = 1.5)
    
label final_act_25:
    # scene black
    # show image Text("DEBUG: финальный ивент для тестирования в этой версии."):
    #     align(.5, .5)
    # with my_dissolve 
    call wait_click_label from _call_wait_click_label_34 
    #$ renpy.quit()
    



    $ events.pop('final_act_25', 0)
    #$ time.time_now = "night"
    scene black
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_236
    show GG Prison_WTF
    show GG Prison_WTF: 
        xzoom -1.0
        xalign .86 ypos 1081
    with my_dissolve
    "[gg]" "Я не могу уснуть на голодный желудок."

    "[gg]" "Я вообще ничего не могу сделать в таком состоянии. "

    "[gg]" "Я проглочу эту грёбаную таблетку."
    show GG Prison_Angry
    with my_dissolve
    "[gg]" "Да, прямо сейчас."

    menu:
        "Проглотить таблетку?"

        "Да":
            $ pass
        "Нет":
            scene black with my_dissolve
            $ renpy.pause(.5, hard = True)
            scene black with my_vpunch
            play audio 'audio/falldown.mp3'
            
            jump final_act_25_die

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    
    show GG Prison_WTF
    with my_dissolve
    "[gg]" "Хм…"
    
    "[gg]" "Вроде бы ничего не происходит."
    
    "[gg]" "Может, это просто чьей-то розыгрыш?"

    with my_dissolve
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_36 
    $ renpy.pause(.7, hard = True)
    show GG Prison_Surprise
    with my_vpunch
    
    $ renpy.pause(1.5, hard = True)
    play audio 'audio/falldown.mp3'
    scene black with my_vpunch


    $ renpy.pause(2.5, hard = True)
    #//Встряска экрана

    #//Герой падает

    #//Экран гаснет
    $ from_say_screen = False
    scene image 'cg/final_act/morgue/pre_end/bg.png'
    show Officer Normal
    show Officer Hm:
        xalign .75
        ypos 1080
        xzoom -1
    
    show image 'cg/final_act/morgue/pre_end/gg.png'
    with my_dissolve_very_long
    $ renpy.pause(1.1, hard = True)
    #//Dead_GG art (в морге, всё тело гг кроме головы накрыто простынёй)

    #//Officer_Normal

   # show Officer Normal
    "Офицер" "Хм…"
    show Officer Say:
        easein_cubic 3.5 xalign .45
        
    "Офицер" "Не понимаю."
    
    "Офицер" "Если от чего и должен был подохнуть этот щенок, то точно не от сердечного приступа."
    show Officer Hm:
        xalign .45
        xzoom -1
    show shadow_full: 
        #alpha 0.0
        alpha 1.0

    with my_dissolve
    "Офицер" "По крайней мере именно таков предварительный диагноз коронера."
    
    "Офицер" "Ну ничего. Вскрытие всё покажет…"
    
    "Офицер" "Возможно, это просто отравление. Или даже яд."
    show Officer Chagrin:
        xalign .5 ypos 1080 xzoom 1
        easein .1 ypos 1085
        easein .1 ypos 1080
        easein .1 ypos 1085
        easein .1 ypos 1080
        easein .1 ypos 1085
        easein .1 ypos 1080
    show shadow_full: 
        alpha 1.0
        easein .75 alpha 0.0

    #with my_vo
    "Офицер" "Яд?..."
    "Офицер" "Занимательная мысль ко мне пришла."
    show Officer Hm:
        easein_cubic 8.5 xalign .9
    hide shadow_full
    #with my_dissolve
    "Офицер" "И кому нужно его травить?"
    
    "Офицер" "Вопрос."
    show Officer Hm:
        xzoom -1
    show shadow_full: 
        #alpha 0.0
        alpha 1.0
    with my_dissolve
    "Офицер" "Да уж… Кто-то ненавидит этого сучёныша ещё сильнее, чем я."
    
    "Офицер" "Крайне любопытное дело. Крайне."

    #//Тут должны пойти НЕПРОПУСКАЕМЫЕ титры. Наебём игроков. Хочу реализовать такую же фичу, как в финале Хитмана БладМани

    #//Титры должны будут идти зациклено (так как у нас их банально очень мало, да и игроку проще будет осознать в чём подвох).

    #//Так же было бы здорово программно картинку заблюрить (не титры). Типа конец концов

    #//При клике в любой место со временем усиливался бы звук сердцебиения, а по краям экрана появлялся бы градиент затемнени

    #//По факту мы встраиваем мини-игру, где надо накликать «условную полоску», которая падает с каждой секундой. Только никаких полосок визуально игрок видеть не будет, а должен понимать всё интуитивно.

    #//Таким образом, мы встроем «невидимую» полоску, и поделим её на этапе.

    #// 1 уровень полоски снижает увеличивает прозрачность титров на 20%, и увеличивает частоту звука сердцебиения на 30%

    #// 2 уровень полоски снижает увеличивает прозрачность титров на 40%, и увеличивает частоту звука сердцебиения на 50%

    #// 3 уровень полоски снижает увеличивает прозрачность титров на 75%, и увеличивает частоту звука сердцебиения на 75%

    #// 4 уровень убирает все эфекты, блюр и прочее. Игроку представляется картинка с полуожившим гг
    show Officer Say
    
    show shadow_full: 
        #alpha 0.0
        easein 1.0 alpha 0.0

    "Офицер" "Здесь больше не на что смотреть."
    hide final_act_pre_end 1
    hide image 'cg/final_act/morgue/pre_end/1_blur.png'
    "Офицер" "Мне пора идти."
    show Officer Normal:
        xzoom 1 
        easein 4.5 xalign 1.5
    show black:
        alpha 0.0
        easeout 3.0 alpha 1.0
    show final_act_pre_end 1:
        alpha 0.0

    show image 'cg/final_act/morgue/pre_end/1_blur.png':
        alpha 0.0

    $ renpy.pause(3.5, hard = True)
    python:
        try:
            del end_credits_screen_clicks
        except:
            pass

    $ renpy.music.stop(fadeout=21.0)
    $ renpy.music.play('audio/heart_beat_1_0.mp3', fadein = 3.0)


    show final_act_pre_end 1:
        alpha 0.0 zoom 2.1 pos (0, -550)
        easeout 1.5 alpha 1.0

    $ renpy.pause(1.75, hard = True)
    
    show image 'cg/final_act/morgue/pre_end/1_blur.png':
        alpha 0.0 zoom 2.1 pos (0, -550)
        easeout 1.5 alpha 1.0
    show screen end_credits_screen
        
    #show screen end_credits_screen_bg
    #show screen end_credits_screen
    
    $ renpy.pause(1.75, hard = True)
    #hide final_act_pre_end 1
    #hide screen end_credits_screen_bg
    $ store.end_credits_screen_clicks = 0
    hide image 'cg/final_act/morgue/pre_end/1_blur.png'
    show screen end_credits_screen_bg
    

    #with my_dissolve
    $ renpy.pause(20.5, hard = True)
    scene black
    hide screen end_credits_screen_bg
    hide screen credits_screen
    
    with my_dissolve
    $ renpy.pause(1.0, hard = True)    
    $ renpy.full_restart()




label final_act_25_secret_final:
    #//Officer_Normal разворачивается и движется ко входу (но не исчезает

    #//Спрайт ГГ берёт какакие-то хирургические ножницы или скальпель со стола рядом

    #//Officer_Normal оборачивается на мгновение

    #//Сцена где ГГ повали офицера и приставил ему лезвие хирургического прибора





    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/sad-reflection-and-grief-piano-by-musiclfiles-from-filmmusic-io.mp3', fadein = 1.5)


    hide screen end_credits_screen_bg
    hide screen end_credits_screen
    with my_dissolve
    #scene image '#0000'
    #show image 'cg/final_act/morgue/pre_end/2.png'
    show final_act_pre_end 2#:
        #align (0, 0)
        #zoom 1.9 pos (50, -550)
        #zoom 1.9 pos (-695, -550)

    with my_vpunch
    $ renpy.pause(1.5, hard = True)

    scene image 'cg/final_act/morgue/pre_end/2.png':
        
        zoom 2.1 pos (0, -550)
        parallel:
            easein_cubic 2.5 pos (0, -700)
        parallel:
            #pause 1.0
            easein_cubic 2.5 zoom 2.5

    # $ renpy.pause(5.5, hard = True)
    show black:
        alpha 0.0
        easeout 1.5 alpha 1.0
    $ from_say_screen = False
    $ renpy.pause(2.0, hard = True)
    scene image 'cg/final_act/morgue/end/bg.png'
    show secret_final 1      
    show image 'cg/final_act/morgue/end/vfx.png':
        alpha 0.0
        pause .5
        easein .75 alpha 1.0
        pause .1
        easeout .75 alpha 0.0   
    show Officer Invis
    show Officer Invis:
        xalign .75
    show GG Invis
    show GG Invis:
        xalign .15
    with my_vpunch  
    "[gg]" "Привет, ублюдок!!!"
    "Офицер" "Ты?!!... ТЫ?!!!...."
    with my_vpunch
    "Офицер" "Но как?!!!"
    "[gg]" "Наверное, в аду решили, что здесь я буду нужнее."
    "Офицер" "Парень…"
    "Офицер" "Ты же понимаешь, какие последствия тебя ожидают если ты…"
    "[gg]" "Твой труп это волноваться не должно, мистер…"
    "[gg]" "Мать твою, а ведь я даже не знаю, как тебя зовут."
    "Офицер" "Разве это имеет какое-то значение?.."
    "[gg]" "Сейчас для тебя всё имеет значение."
    "Офицер" "Я скажу всё, что ты пожелаешь. Только прошу… не убивай."
    if mp.player_pool_name is None:
        $ mp.player_pool_name = __('Офицер')
        $ mp.save()
    $ officer_name = mp.player_pool_name
    "[gg]" "Имя. Говори своё чёртово-блядское имя!"
    $ nameboxes['Officer'].name = officer_name
    $ nameboxes['Officer'].create_text_obj()
    
    "[officer_name]" "[officer_name]"
    "[gg]" "Как-как ты сказал?.."
    "[officer_name]" "[officer_name]!!!"

    $ renpy.music.stop(channel = "ero", fadeout=5.5)
    show secret_final 2
    with my_dissolve

    "[gg]" "Вот оно как…"
    "[officer_name]" "Теперь ты отпустишь меня?.. "
    "[gg]" "Нет."
    show secret_final 1
    with my_vpunch
    "[gg]" "Всего лишь хочу знать имя того, чьи кишки будут украшать этот грёбаный склеп"
    "[officer_name]" "Нет! Пожалуйста!!"
    "[officer_name]" "Я читал твоё дело, парень… Я знаю тебя. Ты не убийца."
    show secret_final 2
    with my_dissolve
    "[gg]" "Да ну?!"
    "[officer_name]" "Умоляю, позволь мне сказать…"
    "[gg]" "У тебя тридцать секунд, но я не ручаюсь, что моя рука не дрогнет раньше."
    "[officer_name]" "Я…"
    "[officer_name]" "Я был не прав в отношении тебя."
    "[officer_name]" "Я знаю, в этого тяжело поверить, но мы очень похожи."
    show secret_final 1
    with my_vpunch
    "[gg]" "Чушь!"
    if type(mp.player_pool) == int or mp.player_pool is None:
        $ mp.player_pool = {
            'Любимый Типаж Девушек': 'Стройные',
            'Любимый Размер Груди' : '1',
            'Любимое Занятие Вне Работы':['Кино',],
            'Любимая Игра': "Milf's Plaza",
            'Кем Бы Я Хотел Стать В Другой Жизни':'Гидролиском',
            'Любимое время суток':'Утро',
            'Любимый напиток':'Чай',


            }
    # #//далее ответ будет отражать анкету, которую игрок заполняет перед началом игры

    # "// Любимый Типаж Девушек" ""
    # #//Стройные, Атлетичные, Мясистые, Худенькие.

    # "//Любимый Размер Груди" ""
    # #//1-5 и гигантский

    # "//Любимое Занятие Вне Работы" ""
    # #//Кино, Сериалы, Компьютерные игры, Аниме, Настольные игры, Спорт, Сон.

    # "// Любимая Игра" ""
    # #// Тут игрок должен вписать данные, по-другому никак

    # "// Кем Бы Я Хотел Стать В Другой Жизни" ""
    # #// Тут игрок должен вписать

    # "//Любимое Время Суток" ""
    # #//Утро, День, Вечер, Ночь

    # #//Любимый напиток

    # #//Тут игрок должен вписать


    # #//Тут придётся заморочиться и часть фраз составить таким образом, чтобы склонение адекватно ложилось на фразу.




    "[officer_name]" "Я такой же грешник, как и ты, парень. "
    "[officer_name]" "Всё, что ломает тебя, [gg], с не меньшей силой воздействует и на мою моральную устойчивость."
    $ girls_type = __(mp.player_pool['Любимый Типаж Девушек'])
    $ girls_boobs_size = __(mp.player_pool['Любимый Размер Груди'])

    "[officer_name]" "Я люблю [girls_type] с [girls_boobs_size] размером груди."
    "[officer_name]" "И мне не стыдно в этом сознаться, да!"
    $ love_deal = ''
    python:
        for i in mp.player_pool['Любимое Занятие Вне Работы']:
           love_deal += __(i) + ', ' 
        love_deal = love_deal[:-2]
    "[officer_name]" "После работы, я люблю [love_deal]. Всё это свойственно и тебе, я знаю."
    "[officer_name]" "Но есть вещи и глубже. "
    "[officer_name]" "Душевнее."
    "[officer_name]" "Человечнее… ведь я тоже человек. Как ты, из плоти и кожи."
    $ love_time   = __(mp.player_pool['Любимое время суток'])

    $ love_drink  = mp.player_pool['Любимый напиток']
    show secret_final 2
    with my_dissolve
    "[officer_name]" "[love_time] когда меня ничто и никто не беспокоит, глядя в окно и попивая [love_drink], в моей голове рождается потрясающая мысль… "
    "[officer_name]" "Мысль стать другим."
    $ love_future = mp.player_pool['Кем Бы Я Хотел Стать В Другой Жизни']
    "[officer_name]" "Мне представляется что я мог бы стать [love_future] и как бы сложилась моя жизнь в этом случае."
    "[officer_name]" "Оказался бы я здесь?"
    "[officer_name]" "Нет. Не думаю…"
    "[gg]" "Ебать мой хуй, ну и тирада!"
    "[gg]" "Ты бы не оказался здесь, [officer_name], если бы не хотел убить меня."
    "[officer_name]" "Что?.."
    "[officer_name]" "Я не собирался тебя убивать, [gg]. "
    "[officer_name]" "Я хотел придать тебя суду, да. Чтобы ты получил заслуженный срок… "
    "[officer_name]" "Но убить? Зачем?!"
    with my_vpunch
    "[gg]" "Ты – конченная мразота, не строй из себя идиота. "
    "[gg]" "Я прекрасно знаю про камеру смертников, и то, как ты морил меня голодом!"
    "[officer_name]" "Какого хуя ты говоришь?!"
    "[officer_name]" "Какая ещё камера смертников? Какой голод блядь?!"
    "[officer_name]" "Я просто посещал тебя, чтобы поизмываться словесно, но не более!"
    "[gg]" "Поверить не могу, что ты продолжаешь врать!"
    "[gg]" "Твоя любовница мне всё рассказала!!!"
    with my_vpunch
    "[officer_name]" "Кто?!"
    "[gg]" "Не придуривайся. Я про девушка-полицейскую, которая дежурит ночью."
    "[officer_name]" "Да ты ёбнулся, парень!"
    "[officer_name]" "В нашем отделе нет ни одной женщины-полицейской! "
    "[officer_name]" "И если уж мы начали откровенничать, то моя любовница – Даша, консультант из магазина одежды!"
    "[officer_name]" "Я понятия не имею, о ком ты говоришь!"
    "[gg]" "Тогда кто эта полицейская?!!"
    "[officer_name]" "Ты меня спрашиваешь?!"
    "[officer_name]" "Может это мне надо спросить?.."
    "[officer_name]" "И как вообще ты умер и ожил?.."
    "[gg]" "Что вообще здесь блядь происходит?!"
    "[gg]" "Ебать…"
    #//эффект воспоминаний
    show image 'cg/final_act/morgue/end/memory_1.png'
    show GirlOfficer Invis:
        xalign .05
    show GG Invis:
        xalign .85
    with my_dissolve
    "Офицерша" "Да. У меня тоже есть любимый человек."
    #//эффект воспоминаний закончился
    #hide image 'cg/final_act/morgue/end/memory_1.png'
    #with my_dissolve
    "[gg]" "Кажется я начинаю понимать…."
    #//эффект воспоминаний
    # show image 'cg/final_act/morgue/end/memory_1.png'
    # show GG Invis:
    #     xalign .85
    # with my_dissolve
    #show GG Prison_WTF
    "[gg]" "Значит, помогая мне, ты идёшь на прегрешения?"
    #show Policegirl Eda
    "Офицерша" "Мгу."
    #show Policegirl Eda
    "Офицерша" "Но и мой любимый грешит ради меня."
    #show Policegirl Eda
    "Офицерша" "Стыдно сознаться, но у него есть жена."
    #show Policegirl Eda
    "Офицерша" "Я думаю, ты уже догадался, о ком я говорю, но, в силу сложившихся обстоятельств, я бы предпочла не называть его имени."
    #//эффект воспоминаний закончился
    hide image 'cg/final_act/morgue/end/memory_1.png'
    show GG Invis:
        xalign .15
    with my_dissolve
    "[gg]" "Так вот о ком она говорила…"
    #//эффект воспоминаний
    show image 'cg/final_act/morgue/end/memory_2.png'
    show GG Invis:
        xalign .85
    show Milf Invis:
        xalign .15
    with my_dissolve
    #show GG Prison_WTF
    "[gg]" "Ты думаешь, это проделки брата?"
    #show Milf City
    "Марина" "Уверена."
    #show Milf City
    "Марина" "У него полно связей в полиции."
    #//эффект воспоминаний закончился
    # hide image 'cg/final_act/morgue/end/memory_2.png'
    # show GG Invis:
    #     xalign .15
    # with my_dissolve
    # "[gg]" "Всё было очевидно с самого начала. "
    #//эффект воспоминаний
    #show image 'cg/final_act/morgue/end/memory_2.png'
    #show GG Invis:
    #    xalign .85
    #with my_dissolve
    #show Milf Normal
    "Марина" "Если он поймёт, что не сможет меня вернуть, то отправится на поиски новой дуры, которую так же использует в своих целях."
    #//эффект воспоминаний закончился
    #show bla
    
    scene image 'cg/final_act/morgue/pre_end/bg.png'
    show GG Prison_WTF
    show GG Prison_WTF:
        xalign .86
        xzoom -1.0
        ypos 1080
    show Officer Normal
    show Officer Normal:
        xalign .15
        ypos 1080
        #xzoom -1

    with my_dissolve
    "[gg]" "Всё было очевидно с самого начала. "
    "[officer_name]" "Что?.. Что очевидно?"
    "[gg]" "Меня подставили!"
    "[gg]" "Я как тот бык, перед которым махают красной тряпкой."
    show Officer Hm
    with my_dissolve
    "[officer_name]" "И тряпка это я?"
    show GG Prison_Angry
    with my_vpunch
    "[gg]" "Сейчас не время обсуждать мои метафоры."
    
    with my_vpunch
    "[gg]" "Это проделки моего брата, [officer_name]!"
    show GG Prison_Please
    with my_dissolve
    "[gg]" "И девушка, которая мне якобы помогала…"
    #//Спрайт позади ГГ
    show GirlOfficer Pistol_1
    show GirlOfficer Pistol_1:
        xzoom -1.0
        xalign -1.5
        ypos 1080
        easein .75 xalign .0
    show GG Prison_Surprise:
        easein .75 xalign .9
        #xzoom -1.0
    show Officer Surprise:
        easein .75 xalign .6
        xzoom -1.0
        
    #with my_dissolve
    "Офицерша" "Идеально сыграла свою роль, не так ли?"
    #//морг

    #//Officer_Surpise справа, но перед ГГ

    #//GG_Morg_Surpise справа, но позади мента

    #//Of_woman_Normal слева

    #show Of Woman

    "Офицерша" "Я уж боялась, ты не додумаешься найти таблетку под унитазом, ха-ха-ха."
    #show GG Morg
    show Officer Angry:
        xalign .6
        xzoom -1.0
    show GG Prison_Angry:
        xalign .9
    show GirlOfficer Pistol_1:
        xzoom -1.0
        ypos 1080
        xalign .0
    with my_vpunch
    "[gg]" "Зачем ты решила подставить меня?!"
    #show GG Morg
    "[gg]" "На кой хрен тебе это нужно?"
    #show Of Woman
    "Офицерша" "Я думаю ты и сам знаешь ответ на этот вопрос."
    #show GG Morg
    "[gg]" "Дура! Джеймс не любит тебя!"
    #show GG Morg
    "[gg]" "Он просто использует твоё влечение к нему!"
    #show Of Woman
    show GirlOfficer Pistol_1 at hehe_transform()
    "Офицерша" "Ха-ха-ха!"
    #show Of Woman
    "Офицерша" "Ты такой же самоуверенный, как твой брат, [gg]."
    #show Of Woman
    "Офицерша" "Не могу не признаться - мне нравится эта черта в мужчинах."
    #show Of Woman
    "Офицерша" "Но с чего ты решил, что именно Джеймс меня использует, а не я его?"
    #show Of Woman
    "Офицерша" "Мне нужен Джеймс, а я – ему, но мы не можем быть вместе, пока он не разведётся с Мариной."
    #show Of Woman
    "Офицерша" "В случае развода он теряет 50%% всего имущества, а он куда богаче, чем вы, голубки, предполагаете."
    #show Of Woman
    "Офицерша" "Другое дело, если его жена умрёт, тогда всё перейдёт ему, то есть – нам."
    #show Of Woman
    "Офицерша" "Мы стоим друг друга."
    #show GG Morg
    show GG Prison_WTF
    with my_dissolve
    "[gg]" "Не понимаю…"
    #Of_woman_Norma

    #show GG Morg
    "[gg]" "Пока я был в заключении, вы давно могли добраться до Марины и расправиться с ней."
    #show GG Morg
    "[gg]" "Что вам мешало?.."
    #show Of Woman
    "Офицерша" "Если бы мы убили сейчас Марину, то все подозрения упали бы на Джеймса."
    #show Of Woman
    "Офицерша" "Нам нужен был козёл отпущения."
    #show Of Woman
    "Офицерша" "Я сделала всё возможное, чтобы ты возненавидел этого полицейского, выбрался из своей камеры и убил его."
    #show Of Woman
    "Офицерша" "После я должна была проследить за тобой и прикончить. Естественно, надёжно спрятав тело."
    #show Of Woman
    "Офицерша" "И как только это произойдёт, Джеймс ликвидирует Марину и Кристи."
    #show Of Woman
    "Офицерша" "Полицая решит, что это ты их убил, ведь у тебя УЖЕ на руках кровь полицейского. "
    #show Of Woman
    "Офицерша" "Ко всему прочему – ты беглец из заключения."
    #show Of Woman
    "Офицерша" " А Марина и Кристи, как самые близкие к тебе люди, вероятно, «слишком много о тебе знали», и могли выдать твоё местоположения."
    #show Of Woman
    "Офицерша" "Ну как тебе план? Хитро?"
    #show GG Morg
    "[gg]" "Судя по тому, что никого я убивать не собираюсь, операция провалена."
    #show Of Woman
    "Офицерша" "О нет. Вовсе нет. "
    #show Of Woman
    "Офицерша" "Просто небольшие коррективы."
    #// Of_woman_Normal стреляет в полицейского

    #GG_Morg_Surprise

    #//Officer_Dead_1
    # show image "/cg/final_act/morgue/end/officer_dead.png":
    #     align (0, 0)
    #     xpos -200
    #     easein 5.0 xpos 0
    show Officer Bited_2:
        xalign .7
        easein 5.0 xalign .85
    show final_act_vfx_bullet_1:
        align (0, 0)
        #zoom .75
        #xzoom -1.0
        pos (1100, 420)
        easein 6.0 pos (1300, 420)

    show christie_root_65_hat_3:

        pos (1100+200, 200) alpha 1.0 rotate 30
        easein 2.7 pos (1400+200, 400) alpha .1 rotate 70
    show christie_root_65_hat_2:

        pos (1100+200, 200) alpha 1.0 rotate 30
        easein 2.3 pos (1400+200, 400) alpha .1 rotate 70
    show christie_root_65_hat_1:
        pos (1100+200, 200) rotate 30
        easein 1.9 pos (1400+200, 400) rotate 70
    show GG Prison_Surprise:
        easein .1 xalign 1.2
    show GirlOfficer Pistol_2 at hehe_transform
    show white:
        alpha 1.0
        easein .1 alpha .0


    show image "cg/final_act/prison/pistol_vfx/0.png":
        align (0, 0)
        zoom .75
        xzoom -1.0
        pos (765, 360)
        easein .8 pos (780, 360)
    show image "cg/final_act/prison/pistol_vfx/1.png":
        align (0, 0)
        zoom .75
        pos (765, 360)
        xzoom -1.0
        easein .8 pos (780, 410)
    show image "cg/final_act/prison/pistol_vfx/2.png":
        align (0, 0)
        zoom .75
        pos (765, 360)
        xzoom -1.0
        easein .8 pos (780, 300)
    with my_vpunch
    $ renpy.pause(.3, hard = True)

    show image "cg/final_act/prison/pistol_vfx/0.png":
        easein .1 alpha 0.0
    show image "cg/final_act/prison/pistol_vfx/1.png":
        
        easein .1 alpha 0.0
    show image "cg/final_act/prison/pistol_vfx/2.png":
        easein .1 alpha 0.0
    show GirlOfficer Pistol_1
    $ renpy.pause(.3, hard = True)
    show final_act_vfx_bullet_2:
        align (0, 0)
        #zoom .75
        #xzoom -1.0
        pos (1000, 530)
        easein 6.0 pos (1200, 530)
    
    show image "cg/final_act/prison/pistol_vfx/0.png":
        alpha 1.0
        pos (765, 360)
        easein .8 pos (780, 360)
    show image "cg/final_act/prison/pistol_vfx/1.png":
        alpha 1.0
        pos (765, 360)
        easein .8 pos (780, 410)
    show image "cg/final_act/prison/pistol_vfx/2.png":
        alpha 1.0
        pos (765, 360)
        easein .8 pos (780, 300)
    show GirlOfficer Pistol_2 at hehe_transform

    show white:
        alpha 1.0
        easein .1 alpha .0
    with my_vpunch
    $ renpy.pause(.3, hard = True)
    show image "cg/final_act/prison/pistol_vfx/0.png":
        easein .1 alpha 0.0
    show image "cg/final_act/prison/pistol_vfx/1.png":
        
        easein .1 alpha 0.0
    show image "cg/final_act/prison/pistol_vfx/2.png":
        easein .1 alpha 0.0
    show GirlOfficer Pistol_1
    $ renpy.pause(.3, hard = True)
    show final_act_vfx_bullet_3:
        align (0, 0)
        #zoom .75
        #xzoom -1.0
        pos (1120, 750)
        easein 6.0 pos (1320, 750)
    show image "cg/final_act/prison/pistol_vfx/0.png":
        alpha 1.0
        pos (765, 360)
        easein .8 pos (780, 360)
    show image "cg/final_act/prison/pistol_vfx/1.png":
        alpha 1.0
        pos (765, 360)
        easein .8 pos (780, 410)
    show image "cg/final_act/prison/pistol_vfx/2.png":
        alpha 1.0
        pos (765, 360)
        easein .8 pos (780, 300)
    show GirlOfficer Pistol_2 at hehe_transform
    show white:
        alpha 1.0
        easein .1 alpha .0
    with my_vpunch
    $ renpy.pause(.3, hard = True)
    show GirlOfficer Pistol_1
    show image "cg/final_act/prison/pistol_vfx/0.png":
        easein .1 alpha 0.0
    show image "cg/final_act/prison/pistol_vfx/1.png":
        
        easein .1 alpha 0.0
    show image "cg/final_act/prison/pistol_vfx/2.png":
        easein .1 alpha 0.0

    with my_dissolve

    $ from_say_screen = False
    $ renpy.pause(.75, hard = True)
    show christie_root_65_hat_1:
        easein .3 alpha 0.0
    show christie_root_65_hat_2:
        easein .3 alpha 0.0
    show christie_root_65_hat_3:
        easein .3 alpha 0.0
    show Officer:
        easein .3 alpha 0.0
    show final_act_vfx_bullet_1:
        easein .3 alpha 0.0
    show final_act_vfx_bullet_2:
        easein .3 alpha 0.0
    show final_act_vfx_bullet_3:
        easein .3 alpha 0.0
    #with my_vpunch
    #$ renpy.pause(.3, hard = True)
    #"[officer_name]" "Ууффф!!!..."
    #show Officer Dead
    #"[officer_name]" "Оххххх…"
    #show Officer Dead
    #"[officer_name]" "Эх..!!.."
    #show Of Woman

    "Офицерша" "Беги, пока не поздно!"
    #show GG Morg
    show GG Prison_Angry:
        easein .75 xalign .7
    "[gg]" "Ты ненормальная!"
    #show Of Woman
    show GG Prison_Surprise:
        easein 1.0 xalign 1.1
    show GirlOfficer:
        easein 1.0 xalign .5
    "Офицерша" "Беги, иначе мне точно придётся поменять наш план."
    #show Of Woman
    "Офицерша" "А уж я умею импровизировать, ха-ха-ха!"
    #GG_Morg_Suprise
    $ renpy.call_screen('circle_attention_screen', xp = 700, yp = 255, zm = .5)
    show GirlOfficer:
        ypos 1220
        parallel:
            easein 1.15 rotate 15 xalign .8 alpha 0.0 
        parallel:
            easein .26 ypos 1280
    show Christie Harly_Bat
    show Christie Harly_Bat:
        pos (250, 1080)
        easein 3.5 pos (350, 1080)     
    show christie_root_65_bat_sfx_1_1:
        pos (1100-600, 270) alpha 1.0
        parallel:
            easein 9.5 pos (1400-600, 270) 
        parallel:
            easein 3.5 alpha .1
    show christie_root_65_bat_sfx_1_2:
        pos (1100-600, 270)
        parallel:
            easein 6.0 pos (1400-600, 270) 
        parallel:
            easein 3.5 alpha .1
    show christie_root_65_bat_sfx_1_3:
        pos (1100-600, 270)
        parallel:
            easein 3.5 pos (1400-600, 270)
        parallel:
            easein 3.5 alpha .1
    
    show christie_root_65_bat_sfx_2:
        pos (1100-300, 170)
        easein 4.0 pos (1400-300, 70)

    show christie_root_65_bat_sfx_3:
        pos (1100-200, 170)
        easein 3.5 pos (1400-200, 70)


    show christie_root_65_bat_sfx_4:
        pos (1100-100, 170)
        easein 3.0 pos (1400-100, 70)
    with my_vpunch
    $ renpy.pause(3.0, hard = True)
    hide GirlOfficer    
    hide christie_root_65_bat_sfx_1_1
    hide christie_root_65_bat_sfx_1_2
    hide christie_root_65_bat_sfx_1_3
    hide christie_root_65_bat_sfx_1
    hide christie_root_65_bat_sfx_2
    hide christie_root_65_bat_sfx_3
    hide christie_root_65_bat_sfx_4
    with my_vpunch

    $ renpy.pause(.5, hard = True)
    

    #//Кристи в костюме Харли Квин бьёт дубинкой по Of_woman_Normal

    #// Of_woman_Normal падает

    #// Кристи чуть продвигается ближе к ГГ, позади неё выезжают Кэт и Марина
    hide Christie
    with None
    show Kat Normal
    show Kat Normal:
        xzoom -1.0
        xalign -1.0
        ypos 1080
        easein 1.0 xalign -.1
    show Milf Street_Chagrin
    show Milf Street_Chagrin:
        xzoom -1.0
        xalign -1.0
        ypos 1080
        easein 1.0 xalign .1
    show Christie Harly_Bat_Angry
    show Christie Harly_Bat_Angry:
        xzoom -1.0
        xalign .5
        ypos 1080
    with my_vpunch
    "Кристи" "Вот же болтливая сучка!"
    #show GG Morg
    show GG Prison_Please:
        easein 1.0 xalign .95
    "[gg]" "Скорее, помогите мне. "
    #show GG Morg
    with my_vpunch
    "[gg]" "[officer_name] подстрелен. Нужно срочно отвезти его в скорую."
    show Milf Street_Surprise
    with my_dissolve
    "Марина" "Кто?.."
    
    "[gg]" "Чёрт, вы же совсем не в курсе!"
    
    "[gg]" "Это тот самый полицейский, что посадил меня в клетку."
    
    "Кэт" "Серьёзно? Ты хочешь спасти его?"
    
    "Кэт" "После всего того, что он сделал тебе?!"
    ##show Milf Street
    "Марина" "Да, девчонки в курсе, как этот негодяй измывался над тобой!"
    #show GG Morg
    "[gg]" "Нет, я ошибся! Всё дело в том что…"
    #show GG Morg
    hide Officer
    show GG:
        easein .5 xalign 1.2
    "[gg]" "Проклятье! У нас нет времени! Просто помогите мне!"
    #//мент появляется со встряской
    hide GG
    with None
    show Officer Normal
    show Officer Normal:
        xzoom -1.0
        xalign .85
        ypos 1080

    show GG Prison_Surprise
    show GG Prison_Surprise:
        xzoom -1.0
        xalign 1.2
        ypos 1080
    with my_vpunch
    ##show Officer Pula
    "[officer_name]" "Можете не утруждаться. Со мной всё в порядке."
    ##show Cat  Angry
    "Кэт" "Грёбаное зомби!!!"
    ##show Cat  Angry
    "Кэт" "Кристи, лупи эту тварь!"
    ##show Milf Street
    "Марина" "Я видела все фильмы про живых мертвецов, и знаю, что пока его мозги не расплющены, оно не оставит нас в покое!"
    ##show Milf Street
    "Марина" "Оторви ему голову, милая!"
    #//Кристи движется к менту.

    #// Можно даже сделать какой-то эффект скорости и/или приближение камеры
    show Christie:
        easein .3 xalign .2
    show Milf:
        easein .3 xalign -.1
    show Kat:
        easein .3 xalign -.3
    "Кристи" "ЛЕРООООООЙ!!!"
    #call hide_say_screen_with_dissolve_label 

    #$ renpy.pause(.4, hard = True)
    show Officer Surprise
        #pause .75
        #easein 3.0 xalign 1.0
    show Christie Harly_Bat:
        xzoom 1.0
        #pause .1
        xalign .1
        easeout .75 xalign -.1
        easein .5 xalign .2
    #// GG_Morg_Surprise перемещает перед ментов (типа защищает его от удара)

    #////Officer_Pula_Surprise перемещается чуть поотдаль, прячась за ГГ
    $ renpy.pause(1.0, hard = True)
    show Officer Surprise:
        easein .25 xalign 1.1
    show GG Prison_Angry:
        easein .25 xalign .8
    with None
    with my_vpunch
    #show GG Morg
    "[gg]" "СТОП!"
    show Christie Harly_Bat_2_Angry:
        xzoom -1.0
        easein .75 xalign .5
    show Milf:
        easein .75 xalign .1
    show Kat:
        easein .75 xalign -.1
    #with my_vpunch
    #show GG Morg
    "[gg]" "Он не зомби! "
    #show GG Morg
    with my_vpunch
    "[gg]" "Вы что, не понимаете, это же полный бред!"
    #show Cat Skepticism
    show Officer:
        xalign 1.1
    show GG:
        xalign .8
    show Christie:
        xalign .5
    show Milf:
        xalign .1
    show Kat:
        xalign -.1
    with my_dissolve
    
    "Кэт" "Ну и как, по твоему, он выжил после выстрелов из пистолета?"
    #show GG Morg
    "[gg]" "Скорее всего он просто бессмертный! Как Дункан Маклауд из клана Мауклаудов."
    #show GG Morg
    "[gg]" "Или как Нео из Матрицы – поверивший в собственную неуязвимость."
   # show Christie Harly
    "Кристи" "Значит, если я снова проломлю ему череп, он так же подымится и скажем там «Здрасте?»."
    #show Officer Pula
    show Officer Angry_Pistol
    with my_dissolve
    "[officer_name]" "Эй, хватит! Прекращайте этот балаган! Вы что, реально хотите убить меня?!"
    #show Christie Harly
    "Кристи" "Почему бы и нет."
    #show Cat Smile
    "Кэт" "Ты редкостный придурок, дядя."
    #show Milf Street
    "Марина" "И негодяй."
    #// ГГ поворачивается к менту

    #show GG Morg
    show GG Prison_WTF:
        xzoom 1.0
        xalign .7
    with my_dissolve
    "[gg]" "Мы тебя разыгрываем, [officer_name]."
    #show GG Morg
    "[gg]" "Судя по всему, на тебе был надет бронежилет, потому ты и не погиб. "
    ##show Officer Pula
    show Officer Hm
    with my_dissolve
    "[officer_name]" "Ты угадал."
    #show GG Morg
    "[gg]" "Но зачем ты его напялил, если отправлялся в морг?"
    #show Officer Pula
    "[officer_name]" "Эм…"
    #show Officer Pula
    "[officer_name]" "Ну, как ты показал на своём примере, [gg], людям свойственно возвращаться из мёртвых."
    #show GG Morg
    "[gg]" "Ха-ха-ха!"
    #show GG Morg
    "[gg]" "Выходит, ты просто боишься мертвецов?"
    #show Officer Pula
    "[officer_name]" "А кто их не боится?.."
    #show Milf Street
    "Марина" "Ха-ха-ха!"
    #show Cat Laugh
    "Кэт" "Умора!"
   # show Christie Harly
    "Кристи" "Вызывайте «Охотников на привидений»!"
    #show Officer Pula
    "[officer_name]" "Ладно, шутники. Посмеялись и хватит."
    #show Cat Normal
    "Кэт" "Вечно ты прерываешь кайф."
   # show Christie Harly
    "Кристи" "Занудный."
    #show Milf Street
    "Марина" "И мерзкий."
    #show Officer Pula
    "[officer_name]" "Это уже переходит все границы!!!"
    #show Milf Street
    "Марина" "Ха-ха-ха!"
    #show Cat Laugh
    "Кэт" "Хы-хы-хы!"
   # show Christie Harly
    "Кристи" "Хи-хи-хи!"
    #show GG Morg
    "[gg]" "Что ты будешь делать с любовницей моего брата, [officer_name]?"
    #Milf_Street_Normal

    #Cat_Laugh_Normal

    #Kristy_Harly_Normal

   # #show Officer Pula
 #   show Officer Normal
    "[officer_name]" "Посажу в ту же камеру, в которой держали тебя, а когда она оклемается, отправлю к детективам на допрос."
    #show GG Morg
    "[gg]" "Примерно это я и ожидал услышать."
    #show GG Morg
    "[gg]" "Она работает на моего брата Джеймса. "
    #show GG Morg
    "[gg]" "Узнаешь у неё, где скрывается мой брат и как он смог провернуть эту афёру с моей подкормкой в тюрьме – раскроешь дело. "
    #show Officer Pula
    "[officer_name]" "Я догадался."
    #show GG Morg
    "[gg]" "Но как на счёт меня? Что со мной будет?"
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_25 
    show black:
        alpha 0.0
        easein 1.0 alpha 1.0
    $ renpy.pause(1.0, hard = True)
    show image Text(_("Спустя несколько дней")):
        align (.5, .5)
    with my_dissolve
    $ renpy.pause(.3, hard = True)
    $ from_say_screen = False
    call wait_click_label from _call_wait_click_label_19
    scene image "cg/final_act/morgue/end/judgment/bg.png"
    show image "cg/final_act/morgue/end/judgment/hammer.png":
        align (0, 0)
        pos (50, 0)
    show GG Invis
    show GG Invis:
        xalign .5
    #//Чёрный экран

    #//Judje_1
    with my_dissolve
    "Судья" "Учитывая обстоятельства, при которых вы оказались за пределами своей камеры, и свидетельских показаний офицера полиции – я отпускаю вас домой с подпиской о невыезде."
    "Судья" "Вам следует дождаться повестки в суд и…"
    "Судья" "Постараться не нарушать закон!"
    "[gg]" "Спасибо!"
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_26 
    show image "cg/final_act/morgue/end/judgment/hammer.png":
        
        easein .5 pos (50, -100)
        easein .1 pos (50, 300)
        easein .5 pos (50, 0)
    $ renpy.pause(1.5, hard = True)
    #//Чёрный экран

    #//Полицейский участок внутри

    #//девчонки стоят слева

    #//гг выходит справа

    #Milf_Street_Normal

    #Cat_Laugh_Normal

    #Kristy_Harly_Normal

    #GG_Street_Normal
    scene black
    with my_dissolve
    $ renpy.pause(1.0, hard = True)
    scene image '/cg/final_act/prison/police_station/evening.png'

    #show Officer:
    #    xalign 1.1
    #show GG:
    #    xalign .8
    show Kat Normal
    show Kat Normal:
        xalign -.1
        xzoom -1.0

    show Milf Normal
    show Milf Normal:
        xalign .15
        xzoom -1.0
    show Christie Normal
    show Christie Normal:
        xalign .45
        xzoom -1.0
    show GG Normal
    show GG Normal:
        xzoom -1.0
        xalign .8

    with my_dissolve
    "[gg]" "Как приятно вас видеть вновь."
    #show Milf Street
    "Марина" "Ура, долгожданная свобода!"
    #show Cat Laugh
    "Кэт" "Что? Теперь мне не придётся караулить по ночам у двери?"
   # show Christie Street
    "Кристи" "Если бы судья отказала, я бы снова пришла с битой! "
    #//Выезжает слева

    show Officer Normal
    show Officer Normal:
        xalign 1.5
        xzoom -1.0
        easein 1.0 xalign 1.1
    show GG:
        easein 1.0 xalign .65
    show Christie:
        easein 1.0 xalign .35
    show Milf:
        easein 1.0 xalign .05
    show Kat:
        easein 1.0 xalign -.2
    "[officer_name]" "Вижу, ты уже собираешься домой."
    #show GG Street
    show Officer Normal:
        xzoom -1.0
        xalign 1.1
    
    show Christie:
        xalign .35
    show Milf:
        xalign .05
    show Kat:
        xalign -.2
    show GG Angry:
        xalign .65
        xzoom 1.0
    with my_dissolve
    "[gg]" "Пришёл попрощаться или подбросить дёгтя в банку с мёдом?"
    show Officer Smile
    "[officer_name]" "Хотел напомнить, что я сыграл немаловажную в роль в том, чтобы ты оказался на свободе."
    #show GG Street
    "[gg]" "Ага. Как и тогда, когда брал меня под стражу."
    #show GG Street
    "[gg]" "Как так вообще получилось, что ты оказался как раз в тот момент, когда мне чуть не впарили наркоту?"
    #show GG Street
    "[gg]" "Это ведь ты меня подставил…"
    
    "[officer_name]" "Мимо цели, [gg]. "
    
    "[officer_name]" "Помнишь жирдяя, которого ты вырубил у себя дома? "
    #show GG Street
    "[gg]" "Ты про Жлоба?"
    
    "[officer_name]" "Ага."
    
    "[officer_name]" "Когда мы повязали его, то нарыли массу улик, что свидетельствовали о его причастности к множеству преступлений."
    
    "[officer_name]" "Ряд обвинений он парировал в твой адрес. "
    
    "[officer_name]" "А поскольку вы взаимодействовали, а за тобой, к тому же, числится попытка воровства и подозрение в продаже наркотиков, то для прокурора ты оказался более чем соблазнительной целью. "
    
    "[officer_name]" "Я подозреваю, что все его оказания зиждутся на том, что не он, а именно ты – босс преступного мира. "
    
    "[officer_name]" "И это ещё не самое худшее."
   # show GG Street
    show expression 'cg/ep5/jlob/9.png':
        #xzoom -1
        xpos 1200
    

    "[gg]" "Что, чёрт возьми, может быть ещё хуже? Ты объявишь мне о наличии раковой опухоли?!"
    
    "[officer_name]" "…."
    #//Boss_Normal выезжает слева

    #// все персонажи, кроме мента смещаются вправо


    show Christie:
        easein 1.0 xalign .25
    show Milf:
        easein 1.0 xalign -.05
    show Kat:
        easein 1.0 xalign -.3
    show GG Angry:
        easein 1.0 xalign .4
    show Officer:
        linear 1 xalign 1.5
    show expression 'cg/ep5/jlob/9.png':
        linear 1 xpos 260

    $ renpy.pause(1)
    show Christie:
        xalign .25
    show Milf:
        xalign -.05
    show Kat:
        xalign -.3
    show GG Angry:
        xalign .4
    show Officer:
        xalign 1.5
    show expression 'cg/ep5/jlob/9.png':
        xzoom 1.0
        xpos 260
    show Goon Invis
    show Goon Invis:
        xalign 1.0
    with my_dissolve
    #show Boss Normal
    "Жлоб" "Ну здарова, дружище. "
    #show GG Street
    "[gg]" "Какого хера он на свободе, офицер?!"
    #show Boss Normal
    "Жлоб" "Меня выпустили по программе «защиты свидетеля». "
    #show Boss Normal
    "Жлоб" "И нахожусь под опекой государства, чтобы такие бандиты как ты, [gg], не вздумали заткнуть мне рот, хе-хе-хе."
    #show Boss Normal
    "Жлоб" "Ещё увидимся, надеюсь."
    #show Boss Normal
    hide expression 'cg/ep5/jlob/9.png'
    show expression 'cg/ep5/jlob/10.png':
        xzoom 1.0 xpos 260
        easein 2.0 xpos -1760
    show Officer Normal:
        xzoom -1.0
        easein 1.0 xalign 1.1
    show GG:
        easein 1.0 xalign .65
    show Christie:
        easein 1.0 xalign .4
    show Milf:
        easein 1.0 xalign .1
    show Kat:
        easein 1.0 xalign -.1
    
    show Goon Invis:
        easein 3.0 xalign -1.0

    "Жлоб" "Га-га-га."
    #show GG Street
    "[gg]" "Этого ещё не хватало…"
    hide expression 'cg/ep5/jlob/9.png'
    hide expression 'cg/ep5/jlob/10.png'
    show Officer Normal:
        xzoom -1.0
        xalign 1.1
    show GG:
        xalign .65
    show Christie:
        xalign .4
    show Milf:
        xalign .1
    show Kat:
        xalign -.1
    
    hide Goon
    with my_dissolve
    "[officer_name]" "Как видишь, [gg], я здесь не при чём."
    
    "[officer_name]" "Кто-то явно повлиял на судью."
   # show GG Street
    "[gg]" "Не трудно догадаться кто это был."
    
    "[officer_name]" "Твой брат?"
   # show GG Street
    "[gg]" "Ага."
    
    "[officer_name]" "Что ж… "
    
    "[officer_name]" "Я постараюсь с ним не связываться."
  #  show GG Street
    "[gg]" "Ты уже с ним связался."
    
    "[officer_name]" "И то верно."
    
    "[officer_name]" "Береги себя."
    #show GG Street
    "[gg]" "Взаимно."
    show Officer:
        xzoom 1.0
        easein 1.0 xalign 1.75
    show GG Normal:
        easein 1.0 xalign .9
        xzoom 1.0
   # show Christie Street
    show Christie:
        xzoom 1.0
        easein .25 xalign .45
    
    "Кристи" "Пойдёмте поскорее отсюда. Мне здесь не нравится."
    #show Milf Street
    "Марина" "Полностью согласна. Тем более, [gg], ты давно не кушал нормальной домашней еды."
    #show Cat Normal
    "Кэт" "Во-во! Я тоже хочу жрать!"
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_27
    show GG:
        easein 1.5 xalign 1.5
    show Christie:
        xzoom -1.0
        easein 1.75 xalign 1.5
    show Milf:
        easein 2.0 xalign 1.5
    show Kat:
        easein 2.5 xalign 1.5
    $ renpy.pause(1.5, hard = True)
    scene black
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    $ location_now  = 'City_Home'
    $ time.time_now = 'evening'
    call show_bg_image_label from _call_show_bg_image_label_241
    with my_dissolve
    show Kat Normal
    show Kat Normal:
        xzoom -1.0
        xalign -1.5
        easein 1.75 xalign -.1
    show Christie Normal
    show Christie Normal:
        xzoom -1.0
        xalign -1.5
        easein 1.75 xalign .25
    show Milf Normal
    show Milf Normal:
        xzoom -1.0
        xalign -1.5
        easein 1.75 xalign .5
    show GG Normal
    show GG Normal:
        xalign -1.5
        easein 1.75 xalign 1.0
        xzoom -1.0

        #xzoom 1.0

        #xzoom 1.0
        #easein 2.0 xalign 1.5

    $ from_say_screen = False
    $ renpy.pause(1.5, hard = True)
    #//Улица у дома

    #show GG Street
    "[gg]" "Вот интересно…"
    #show GG Street
    show Kat Normal
    show Kat Normal:
        xzoom -1.0
        xalign -.1
    show Christie Normal:
        xzoom -1.0
        xalign .25
    show Milf Normal:
        xzoom -1.0
        xalign .5
    show GG Normal
    show GG Normal:
        xzoom -1.0
        xalign 1.0
    with my_dissolve
    "[gg]" "Злодеи норовят выведать свой план чтобы потешить своё самолюбие или это фора, дабы у жертвы оставался шанс на спасение?"
    #show Milf Street
    "Марина" "Милый, если негодяи дают нам время, чтобы прийти и спасти тебя, пусть они никогда не затыкаются."
    #show Christie Street
    "Кристи" "Ха-ха-ха!"
    #show Cat Smile
    "Кэт" "Но смотри, [gg], мы не всегда можем быть рядом."
    #show Christie Street
    "Кристи" "Ага. Выручать тебя так изнурительно."
    #GG_Street_Embarrassment 

    #show Milf Street
    "Марина" "В особенности тогда, когда это предполагает томительное ожидание в одиночестве… "
   # show Christie Street
    "Кристи" "Особенно по ночам."
    #show Cat Surprise
    "Кэт" "Эй, что вы несёте?!"
    #show Cat Surprise
    "Кэт" "Разве не я была ночным сторожем для вас, принцессы?"
   # show Christie Street
    "Кристи" "Конечно, милая, Кэти. Конечно!"
    #show Milf Street
    "Марина" "Ты чудесно справлялась со своей задачей, дорогая."
    #show Cat Skepticism
    #"Кэт" ""
    #show Milf Street
    "Марина" "Давайте отложим трёп на потом и позволим нашему мальчику таки добраться домой и как следует отдохнуть. "
   # show GG Street
    "[gg]" "Хех! "
  #  show GG Street
    "[gg]" "Дамы, можете быть уверены, с вами я везде чувствую себя как дома. "
   # show Christie Street
    "Кристи" "Вау, как неожиданно и приятно! "
    #show Cat Embarrassment
    "Кэт" "Мать твою, [gg], а ты умеешь поднять самооценку!"
    #show Milf Street
    "Марина" "Полегче, милый, с таким сладкими словами мне у меня может приключиться сахарный диабет! Хи-хи-хи."
   # show GG Street
    "[gg]" "Ну вы и бестии!"
   # show GG Street
    "[gg]" "Пока отсиживался в темнице, вы так крепко сладили, что мне теперь трудно понять, подкалываете вы меня или и вправду смущены? "
    #show Milf Street
    "Марина" "Ха-ха-ха!"
    #show Milf Street
    "Марина" "Извини, милый, нам и вправду пришлось стать команды, дожидаясь, пока единственный мужчина вернётся в нашу… ложу. "
  #  show Christie Street
    "Кристи" "Хи-хи-хи."
    #show Cat Smile
    "Кэт" "Да пойдёмте уже! "
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_28
    show GG:
        xzoom 1.0
        easein .5 xalign 1.5
    show Milf:
        easein 1.0 xalign 1.5
    show Christie:
        xzoom -1.0
        easein 1.5 xalign 1.5
    show Kat:
        easein 2.0 xalign 1.5
    $ renpy.pause(1.5, hard = True)
    show black:
        alpha 0.0
        easein 1.5 alpha 1.0
    #with my_dissolve
    $ renpy.pause(1.75, hard = True)

    
    python:
        Event('final_act_26_christie', location = "Christie")
        Event('final_act_26_milf', location = "Milf")

        block_milf_events   = 'final_act_26_milf'
        block_sister_events = 'final_act_26_christie'
        

        block_change_milf_position_final_act_25 = copy.deepcopy(block_change_milf_position)
        block_change_milf_position   = True
        

        block_sister_home_final_act_25 = copy.deepcopy(block_sister_home)
        block_sister_home = False
        block_milf_home_final_act_25 = copy.deepcopy(block_milf_home)
        block_milf_home   = False

        block_time_forward_final_act_25 = copy.deepcopy(block_time_forward)
        block_time_forward = True

        block_exit_home_final_act_25 = copy.deepcopy(block_exit_home)
        block_exit_home = True
        
        allowed_events_final_act_25 = copy.deepcopy(allowed_events)
        allowed_events = ['final_act_26_christie', 'final_act_26_milf', 'final_act_27']

        milf_position['morning']     = ['Kitchen',   'milf_kitchen']
        milf_position['afternoon']   = ['Corridor',   'milf_corridor']
        milf_position['evening']     = ['Hall',   'milf_evening_hall']
        sister_position['morning']   = ['Hall', 'sister_hall']
        sister_position['afternoon'] = ['Hall', 'sister_hall']
        sister_position['evening'] = ['Sister_Room', 'sister_room']
        unlock_sister_room = True
        #sister_position['night']     = ['Sister_Room', 'sister_room_night']
        location_now   = 'GG_Room'
        time.time_now  = 'morning'
        milf_costume   = 'n_body'
        
        descript       = _("Я дома. И я безумно хочу секса!")
        not_survival   = copy.deepcopy(not_survival_final_act_4)
        gigiena        = 100
        sitost         = 100
        nastroi        = 100
        final_act_26_fix = True
        try:
            del final_act_prison_start
        except:
            pass

        try:
            del not_survival_final_act_4
        except:
            pass



    jump main_interface_label


label final_act_25_die:
    "" "{i}Вы погибли. Желудок остановился, и вы не смогли пережить эту ночь.{/i}"
    $ FilePage("auto")()
    $ renpy.pause(.5, hard = True)
    $ ShowMenu('load')()
    $ renpy.pause(9999)
    jump final_act_25_die
