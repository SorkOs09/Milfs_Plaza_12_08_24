image christie_root_40_igor 1 = 'cg/ep89/park/igor_1.png'
image christie_root_40_igor 2 = 'cg/ep89/park/igor_2.png'

image christie_root_40_officer 1 = 'cg/ep89/park/officer_1.png'
image christie_root_40_officer 2 = 'cg/ep89/park/officer_2.png'


label christie_root_40_0:
    if getattr(store, 'block_igor_position', False):

        $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")

        $ Event('christie_root_40_0', day_start = time.day_now + 1)
        jump main_interface_label

    
    call christie_root_try_to_del_descript_christie_block_igor from _call_christie_root_try_to_del_descript_christie_block_igor_2
    
    $ events.pop('christie_root_40_0', 0)
    $ Event('christie_root_40', 'City_Psi', time = ['morning', 'afternoon'])
    
    $ unlock_city_psi = True
    jump main_interface_label

label christie_root_40:
    if getattr(store, 'block_igor_position', False):
        "[gg]" "Чтобы начать это задание нужно найти куда пропал Игорь..."
        $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")
        $ location_now = 'City_Home'
        $ Event('christie_root_40', 'City_Psi', time = ['morning', 'afternoon'], day_start = time.day_now + 1)
    
        jump main_interface_label

    $ events.pop('christie_root_40', 0)


    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    scene black with Dissolve(.5)
    $ renpy.pause(.6, hard = True)

    scene expression 'cg/christie_root/Psi_Build.png'
    show expression 'cg/christie_root/officer_on_psi_build.png'

    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show Christie Harly_Normal
    show Christie Harly_Normal at go_from_right(xxalign=.7)

    show GG Joker_Normal
    show GG Joker_Normal at go_from_right(xxalign=1.05, xxzoom = -1)

    #// Joker_Normal выезжают cправа

    #// Harly_Normal выезжают справа

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Кристи" "Мы вовремя!"
    
    "[gg]" "Ага."
    show GG Joker_Chagrin:
        xzoom -1
        xalign 1.05
    "[gg]" "Признаюсь, я совсем не ожидал тебя увидеть."
    show Christie Harly_Chagrin:
        xzoom -1
        xalign .7
    with my_dissolve
    "Кристи" "…."
    show Christie Harly_Chagrin
    "Кристи" "Я тоже не ожидала этого от себя."
    show GG Joker_Normal
    "[gg]" "Ты всё ещё боишься? "
    show Christie Harly_Embarrassment
    "Кристи" "Чуточку."
    show GG Joker_Please
    "[gg]" "Но делаешь это только потому, что сама согласилась мне помочь?"
    show Christie Harly_Laughs
    "Кристи" "И это тоже, хи-хи."
    show GG Joker_WTF
    show Christie Harly_Surprise
    with my_dissolve
    "[gg]" "Нет, так не годится, Кристи. "
    show GG Joker_Angry
    "[gg]" "Я не хочу тобой рисковать."
    show GG Joker_WTF
    show Christie Harly_Chagrin
    with my_dissolve
    "[gg]" "Если тебя продирает дрожь, я бы предпочёл, чтобы ты вернулась домой."
    show GG Joker_WTF
    "[gg]" "От этого полицейского можно ожидать всё что угодно, ты же знаешь."
    show Christie Harly_Smile
    "Кристи" "Всё в порядке, [gg]. С тобой я чувствую себя в безопасности."
    show GG Joker_Embarrassment
    "[gg]" "…."
    show GG Joker_Normal
    "[gg]" "А если испугаешься? Запаникуешь?"
    show Christie Harly_Chagrin
    show GG Joker_Chagrin
    with my_dissolve
    "Кристи" "Знаешь, меня обижает, что ты ищешь повод избавиться меня."
    show GG Joker_Normal
    "[gg]" "…."
    show GG Joker_Please
    "[gg]" "Просто не хочу, чтобы ты совершала над собой насилие. В этом нет никакой необходимости."
    show Christie Harly_Chagrin
    "Кристи" "…."
    show GG Joker_Normal
    show Christie Harly_Skepticism
    with my_dissolve
    "[gg]" "Я взялся за эту работу, потому что мне нравится такой род деятельности."
    show GG Joker_Normal
    " Joker" "Это моё."
    show Christie Harly_Normal
    "Кристи" "А я согласилась помочь, потому что хочу…"
    show Christie Harly_Embarrassment
    show GG Joker_Embarrassment
    with my_dissolve
    "Кристи" "Потому что мне хочется быть с тобой чаще! "
    show Christie Harly_Smile
    "Кристи" "Даже в минуты опасности!"
    show GG Joker_Surprise
    "[gg]" "Оу…"
    show Christie Harly_Embarrassment
    "Кристи" "Переживать с тобой яркие эмоции, понимаешь?!"
    show GG Joker_Surprise
    "[gg]" "Да, но…"
    show Christie Harly_Passion
    show GG Joker_Embarrassment
    with my_dissolve
    "Кристи" "Никаких «но», я хочу быть рядом."
    show Christie Harly_Passion
    show GG Joker_Surprise
    with my_dissolve
    "Кристи" "Чтобы, когда я испугаюсь, а я наверняка испугаюсь – ты прав, было бы глупо это отрицать, - у меня был бы повод пригласить тебя переночевать со мной. "
    show GG Joker_Embarrassment
    "[gg]" "Вот оно как…"
    show Christie Harly_Laughs
    "Кристи" " Да, именно."
    show Christie Harly_Embarrassment
    "Кристи" "Хочу чувствовать тебя рядом. В одной кровати. Как в тот раз."
    show Christie Harly_Embarrassment
    show GG Joker_Passion
    with my_dissolve
    "Кристи" "Чтобы ты успокаивал меня…"
    show Christie Harly_Passion
    "Кристи" "И всё такое…"
    show GG Joker_Embarrassment
    "[gg]" "…."
    #//мысли начало

    show shadow_full with my_dissolve

    show GG Joker_Surprise
    with my_dissolve
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/lo-fi-hip-hop-02-by-winniethemoog-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "{i}Офигеть!!!{/i}"

    "[gg]" "{i}Кажется, это новый этап в наших отношениях.{/i}"

    "[gg]" "{i}То самое проявление инициативы, о которых говорила мне Сьюзен в последней беседе.{/i}"


    "[gg]" "{i}Нельзя упускать этот шанс, и уж тем более подавлять её рвение.{/i}"

    "[gg]" "{i}Это знак! Практическое доказательство того, что она… любит меня?{/i}"

    "[gg]" "{i}Ладно, об этом пока рано говорить.{/i}"

    "[gg]" "{i}Но то, на какие самопожертвования она идёт ради меня… Ради того, чтобы просто быть со мной.{/i}"

    "[gg]" "{i}Я должен позволить ей остаться.{/i}"

    "[gg]" "{i}И сделать всё возможное, чтобы она пострадала на моей чёртовой работе.{/i}"
    #//мысли конец
    hide shadow_full with my_dissolve
    
    show GG Joker_Smile
    "[gg]" "Окей. Я тебя понял. Теперь мы одна команда, и бояться будем тоже вместе. "
    show Christie Harly_Smile
    "Кристи" "Хи-хи-хи!"
    show Christie Harly_Normal:
        xzoom 1
    with my_dissolve
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Кристи" "Эй, смотри. Кажется, муж Сьюзен, он уходит!"
    show GG Joker_Angry
    "[gg]" "Вижу, вперёд! "

    hide expression 'cg/christie_root/officer_on_psi_build.png'
    show Officer Normal
    show Officer Normal:
        xalign .1
    with Dissolve(.5)

    if time.time_now == "evening":
        $ time.time_now = "afternoon"
    
    $ renpy.pause(.9, hard = True)

    show Officer:
        xzoom -1
        easein 1.2 xalign -1.0
    show GG:
        ease .8 xalign .3

    show Christie:
        ease .8 xalign .8
    $ renpy.pause(1, hard = True)


    show GG Joker_Surprise:
        ease .8 xalign -1.6

    show Christie:
        ease .8 xalign -1.8
    $ renpy.pause(.85)



    scene black with Dissolve(.5)


    $ renpy.pause(.5)

    scene image 'interface/city_interface/city_bg_'+time.time_now+'.png'
    #show image 'interface/city_interface/city_icon_gg.png'
    #show image 'interface/city_interface/city_icon_christie.png'
    
    show city_icon_jokers normal:
        xpos 1360 ypos 530 alpha .0
    
    show city_icon_officer:
        xpos 1360 ypos 530
    with Dissolve(.5)

    $ renpy.pause(.5)
    show city_icon_jokers normal:
        3.0
        linear .5 ypos 580 alpha 1.0
        easein 1.5 xpos 1200 ypos 540
    
    show city_icon_officer:
        linear .5 ypos 580

        linear 1 xpos 1200 ypos 540
        linear 1.5 xpos 1050 ypos 635
    $ renpy.pause(4, hard = True)

    with vpunch

    $ renpy.pause(1, hard = True)



    show city_icon_officer:
        xzoom -1
    show city_icon_jokers scared:
        easein .5 xpos 1360 ypos 650 zoom .65 alpha .65

    with my_vpunch
    $ renpy.pause(1, hard = True)

    show city_icon_officer:
        xzoom 1
    $ renpy.pause(.75, hard = True)
    show city_icon_officer:
        linear 1.5 xpos 900 ypos 600
        linear .5 alpha .0
    show city_icon_jokers normal:
        linear 1 xpos 1200 ypos 540 zoom 1.0 alpha 1.0
        linear 1 xpos 995 ypos 660
        linear .5 xpos 900 ypos 600 alpha .0
    $ renpy.pause(3, hard = True)
    scene black with Dissolve(.3, hard = True)
    $ renpy.pause(.5, hard = True)
    $ location_now  = 'City_Park'

    call show_bg_image_label from _call_show_bg_image_label_200

    show GG Joker_Angry
    show GG Joker_Angry at go_from_left(xxalign=-.1)

    show Christie Harly_Angry
    show Christie Harly_Angry at go_from_left(xxalign=.1, xxzoom = -1)


    show christie_root_40_officer 1
    show christie_root_40_officer 1:
        xpos 900
        ypos 892

    show christie_root_40_igor 1
    show christie_root_40_igor 1:
        xpos 1240
        ypos 892

    # show Igor Normal
    # show Igor Normal:
    #     xzoom -1
    #     xalign .3
    #     ypos 1085

    # show Officer Normal
    # show Officer Normal:
        
    #     xalign .7
    #     ypos 1085
        
    with Dissolve(.5)


    # show Christie Harly_Normal
    # show Christie Harly_Normal at go_from_right(xxalign=1.0)


    # show GG Joker_Normal
    # show GG Joker_Normal at go_from_right(xxalign=1.2, xxzoom = -1)

#    $ renpy.pause(.5, hard = True)


    #// Officer_Normal появляется и уезжает влево

    #// Joker_Normal исчезает влево

    #// Harly_Normal исчезает влево

    
    #Park

    #//Sprite_Officer_Igor (Офицер общается с Игорем)

    #// Joker_Normal выезжают слева

    #// Harly_Normal выезжают слева

    show shadow_full with my_dissolve


    "[gg]" "Не подходи слишком близко."
    
    show GG: 
        xalign -.1

    show Christie:
        xalign .1
        xzoom -1
    with my_dissolve
    "Кристи" "Тссс, я не дура!"
    
    hide shadow_full 
    with my_dissolve
    
    #//Наши комиксные диалоги между ментом и игорем

    
    call screen comic_frame(__("Ты классный парень, Игорь."), 900, 400)#офицеп
    call screen comic_frame(__("Да ну?"), 1120, 480)
    call screen comic_frame(__("Ага. Пока [gg] отсиживается дома и шляется по продажным девкам, ты с полной самоотверженностью трудишься на благо города."), 900, 400)#офицеп
    call screen comic_frame(__("Наверное."), 1120, 480)
    call screen comic_frame(__("Дай угадаю. Твой приятель пообещал тебе некую выгоду, получить которую ты сможешь не ранее, чем пройдёт предписание судьи. "), 900, 400)#офицеп
    call screen comic_frame(__("Это уже наше личное дело, офицер."), 1120, 480)
    call screen comic_frame(__("Ха! "), 900, 400)#офицеп
    call screen comic_frame(__("Но я близок, верно?"), 900, 400)#офицеп
    call screen comic_frame(__("…."), 1120, 480)
    call screen comic_frame(__("Ха-ха!"), 900, 400)#офицеп
    call screen comic_frame(__("По глазам вижу, что я прав. По глазищам! Вон как сверкают злобой, прожигая меня насквозь. "), 900, 400)#офицеп
    call screen comic_frame(__("Но ты не на того злишься, Игорь. Я тебе не враг, уверяю."), 900, 400)#офицеп
    call screen comic_frame(__("И не для того я здесь, чтобы насмехаться над тобой, парень."), 900, 400)#офицеп
    call screen comic_frame(__("Напротив."), 900, 400)#офицеп
    call screen comic_frame(__("Ты мне нравишься."), 900, 400)#офицеп
    call screen comic_frame(__("Не хочу, чтобы у тебя возникли какие-то проблемы с тем, что ты прикрываешь своего друга."), 900, 400)#офицеп
    call screen comic_frame(__("Разве я что-то делаю противозаконное, сэр?"), 1120, 480)
    call screen comic_frame(__("К сожалению… Да. Нарушаешь. Ещё как нарушаешь."), 900, 400)#офицеп
    call screen comic_frame(__("Эту работу должен выполнять [gg], но вместо этого её делаешь ты. "), 900, 400)#офицеп
    call screen comic_frame(__("Можно сказать, ты сообщник. А это уже статья."), 900, 400)#офицеп
    call screen comic_frame(__("И если кто-то… Разумеется не я, Игорь, просто предупреждаю…"), 900, 400)#офицеп
    call screen comic_frame(__("Так вот если кто-то засвидетельствует о факте подмены исполнителя, то исполняемому придётся туго. "), 900, 400)#офицеп
    call screen comic_frame(__("Ну… "), 1120, 480)
    call screen comic_frame(__("Максимум, что мне грозит, это общественные работы, которые я и так уже делаю. Безвозмездно, кстати."), 1120, 480)
    call screen comic_frame(__("Это если судья не увидит других правонарушений, и тогда, в противном случае, может быть заключение на тридцать или шестьдесят суток. "), 900, 400)#офицеп
    call screen comic_frame(__("Что вы от меня хотите, сэр?"), 1120, 480)
    call screen comic_frame(__("Информацию, ясное дело. "), 900, 400)#офицеп
    call screen comic_frame(__("Ты постоянно в парке, много видишь, много знаешь."), 900, 400)#офицеп
    call screen comic_frame(__("Вы предлагаете мне стать вашим стукачом? "), 1120, 480)
    call screen comic_frame(__("Эй, зачем ты так? "), 900, 400)#офицеп
    call screen comic_frame(__("Речь идёт о роле информатора, и не бесплатно. "), 900, 400)#офицеп
    call screen comic_frame(__("Нет, спа…"), 1120, 480)
    with my_vpunch
    call screen comic_frame(__("Заткнись, сосунок."), 900, 400)#офицеп
    call screen comic_frame(__("Ты не в сраном магазине, чтобы тебе что-то предлагали. "), 900, 400)#офицеп
    call screen comic_frame(__("Теперь я твой шеф и ты будешь докладывать обо всём, что здесь…"), 900, 400)#офицеп
    
    # show Christie Harly_Surprise
    # show Christie Harly_Surprise at go_from_right(xxalign=1.2)


    # show GG Joker_Angry
    # show GG Joker_Angry at go_from_right(xxalign=1.0, xxzoom = -1)

    $ renpy.pause(.2, hard = True)
    show shadow_full with my_dissolve
    
    "[gg]" "Этот подонок хочет подставить Игоря!"

    "Кристи" "Но что мы можем сделать, [gg]?"
    #show GG Joker_Angry
    "[gg]" "Отвлечь его."
    #show Christie Harly_Surprise
    "Кристи" "Как?"
    #show GG Joker_Angry
    "[gg]" "Дай мне свой кроссовок!"
    #show Christie Harly_Surprise
    "Кристи" "Что?!"
    #show GG Joker_Angry
    "[gg]" "Обувь дай! Быстрее!"
    #show Christie Harly_Surprise
    "Кристи" "Вот, возьми. Но за…?"

label christie_root_40_kick:
    hide shadow_full with my_dissolve
    $ i = renpy.call_screen('circle_mini_game_screen', xp = 870, yp = 500, tm = 10)
    if not i:
        jump christie_root_40_kick
    hide Christie    
    hide GG
    show Christie
    show Christie Harly_Surprise:
        xalign .1 xzoom -1

    show GG Joker_Angry
    show GG Joker_Angry:
        xalign -.1
        easein_cubic .5 xalign -.2
        easein_cubic .3 xalign .2
    $ renpy.pause(.7, hard = True)
    show christie_root_40_officer 2:
        easein_cubic 2 zoom .95 ypos 840 
    with my_vpunch

    $ renpy.pause(2, hard = True)
    #//Тут надо сделать, как ты делал в других мини-играх с прицеливанием, 
    #нажать в момент уменьшения шарика, чтобы попасть в голову офицеру

    #//При попадании 

    #//встряска экрана

    #//спрайты исчезают, появляются герои

    #//расположение героев слева направо

    # show GG Joker_Normal
    # "[gg]" ""
    # show Christie Harly_Normal
    # "Кристи" ""
    # show Officer Normal
    # "Офицер" ""
    # show Igor Normal
    # "Igor" ""
    scene black
    with vpunch
    $ renpy.pause(.5, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_201

    show GG Joker_Angry
    show GG Joker_Angry:
        xalign .01

    show Christie Harly_Surprise
    show Christie Harly_Surprise:
        xalign .3
        xzoom -1


    show Officer Angry
    show Officer Angry:
        xalign .7
        xzoom -1
        

    show Igor Troll
    show Igor Troll:
        xalign .99

    with my_dissolve
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Офицер" "Какого хера мать вашу?!!"
    show GG Joker_Normal
    "[gg]" "О, сэр, прошу прощения! "
    show GG Joker_Normal
    "[gg]" "Моя девушка такая нерасторопная. "
    show GG Joker_Normal
    "[gg]" "Она подвернула ногу и упала, а когда падала с неё слетел кроссовок. "
    show GG Joker_Normal
    "[gg]" "Могу ли я попросить вас вернуть его, офицер? "
    show Officer Skepticism
    "Офицер" "Это же вы!"
    show GG Joker_Passion
    show Christie Harly_Normal
    with my_dissolve
    "[gg]" "Мы?"
    show Officer Skepticism
    show Christie Harly_Skepticism
    with my_dissolve
    show GG Joker_Angry
    with my_dissolve
    "Офицер" "Да, те самые потрахушники, что пытались уединиться в переулке."
    show GG Joker_Passion
    show Christie Harly_Angry
    with my_dissolve
    "[gg]" "Вполне возможно. А вы тот самый офицер, что…?"
    show Officer Angry
    with my_vpunch
    show Igor Angry
    with my_dissolve
    show GG Joker_Angry
    with my_dissolve
    "Офицер" "Закрой рот!"
    show Officer Angry
    "Офицер" "Лучше следи за своей тупой бабой, которая к своим годам не научилась завязывать шнурки."
    show Christie Harly_Angry
    "Кристи" "Эй! Вы грубиян!!!"
    show GG Joker_Angry
    "[gg]" "Она права, сэр. Вы не имеете права так обращаться к нам!"
    show Officer Angry
    "Офицер" "Ещё слово, и я арестую вас за покушение на офицера полиции."
    show GG Joker_Angry
    "[gg]" "Вы не в себе? За случайно упавший на голову кроссовок?!"
    show Officer Angry
    "Офицер" "Случайно ли?! Это ещё предстоит выяснить. "
    show Igor Normal
    "Igor" "Я уже могу идти? "
    show Officer Normal
    show Igor Angry
    with my_dissolve
    "Офицер" "На сегодня разговор окончен, так что да – вали. "
    #//Igor_Normal исчезает вправо
    show Igor:
        xzoom -1
        easein 1 xalign 1.5
    show Officer:
        easein 1 xalign .9
    $ renpy.pause(1, hard = True)
    hide Igor
    show GG Joker_Passion
    show Officer:
        xalign .9
    with my_dissolve
    "[gg]" "Пожалуй, мы тоже пойдём. "
    show GG:
        xzoom -1
        easein 3 xalign -1.5
    show Christie:
        xzoom 1
        easein 3 xalign -1.5
    show Officer Normal:
        easein 1 xalign .5
    $ renpy.pause(1, hard = True)

    "Офицер" "…."
    show Officer Angry
    "Офицер" "Чёртова молодёжь…"

    scene black
    with Dissolve(.5)
    $ location_now = 'City_Home'
    $ time.time_now = 'evening'
    $ renpy.pause(.5, hard = True)

    call show_bg_image_label from _call_show_bg_image_label_203
    
    show GG Joker_Normal
    show GG Joker_Normal at go_from_left(xxalign=.15)

    show Christie Harly_Normal
    show Christie Harly_Normal at go_from_left(xxalign=.85, xxzoom = -1)
    #"Time" "Evening"
    $ renpy.pause(1, hard = True)

    #//

    #//Joker_Normal выезжает слева

    #//Harly_Normal выезжает слева
    show Christie Harly_Normal:
        xalign .85
        xzoom 1
    show GG Joker_Normal:
        xalign .15
    with my_dissolve
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/full-moon-lofi-vibes-by-edikey20-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "В этот раз мы легко отделались. "
    show Christie Harly_Smile
    "Кристи" "Ага."
    show GG Joker_WTF
    "[gg]" "Боюсь, больше нам так везти не будет. "
    show Christie Harly_Laughs
    "Кристи" "Предлагаешь сменить наряды?"
    show GG Joker_Normal
    "[gg]" "Слишком заморочено. "
    show GG Joker_Normal
    show Christie Harly_Normal
    with my_dissolve
    "[gg]" "Пока он не знает, кто скрыт под нашими масками, нам волноваться не о чем. "
    show Christie Harly_Surprise
    "Кристи" "Но теперь-то он точно обратит на нас внимание, если мы окажемся рядом. "
    show GG Joker_Smile
    "[gg]" "Значит, будем более осторожными. "
    show Christie Harly_Passion
    "Кристи" "Или более беспечными, если продолжим за ним слежку зная, чем всё может обернуться."
    show GG Joker_Passion
    "[gg]" "Полицейский убеждён, что мы просто любовная парочка. "
    show GG Joker_Passion
    "[gg]" "Этого достаточно, чтобы усыпить его бдительность."
    show Christie Harly_Normal
    "Кристи" "Ну… окей."
    show GG Joker_Normal
    "[gg]" "Постой-ка. Мне кто-то пишет смс."
    #//появляется SMS Сьюзен
    show Psi Invis
    show Psi Invis:
        xalign .48
    show image 'cg/christie_root/restroom/shadow.png'
    show image 'cg/christie_root/restroom/shadow.png':
        align (0, 0)
        xzoom 1.3
        #xpos 300
        alpha .0
        easein 2.0 alpha .9
    "Сьюзен" "Бабушка уже приехала?"
    "[gg]" "Чего?"
    "Сьюзен" "Пирожки остыли, волк проголодался. "
    "[gg]" "Сьюзен, ваш телефон взломали?"
    "Сьюзен" "Дурачок, это конспирологическая обманка на случай, если муж захочет проверить мой телефон."
    "[gg]" "Просто удаляйте СМС."
    "Сьюзен" "Полицейские имеют доступ к удалённым сообщениям."
    "[gg]" "Тогда нам конец."
    "Сьюзен" "Ладно. Рассказывай, получилось что-то выяснить? "
    "[gg]" "Только то, что ваш муж продажный коп, извращенец и, ко всему прочему, шантажист."
    "Сьюзен" "Меня интересует только измена. "
    "[gg]" "Нет, пока что этого грешка за ним не наблюдается. "
    "Сьюзен" "Может, ты недостаточно пристально ведёшь слежку? "
    "[gg]" "Если хотите, можете обратиться к другому «детективу»."
    "Сьюзен" "Извини…"
    "Сьюзен" "Хорошо, жду от тебя информации. "
    "[gg]" "До связи."
    #//исчезает SMS
    hide image 'cg/christie_root/restroom/shadow.png'
    show Christie Harly_Angry
    with my_dissolve
    "Кристи" "Это Сьюзен?"
    hide Psi Invis
    show GG Joker_Normal
    with my_dissolve
    "[gg]" "Да, спрашивала о наших успехах. "
    show Christie Harly_Skepticism
    "Кристи" "Какая нетерпеливая. "
    show GG Joker_Normal
    "[gg]" "Её можно понять. Завра утром продолжим?"
    show Christie Harly_Smile
    "Кристи" "Обязательно!"
    
    
    
    #Tian_41
    scene black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)

    $ descript_Christie = _("Пока не ясно, как скоро мы поймаем офицера на измене жене, зато можно запечатлеть его «грязные» поступки, которые, вероятно, нам тоже пригодятся.")
    
    $ Event('christie_root_41', 'City_Psi', day_start = time.day_now + 1, time = ['morning', 'afternoon'])

    jump main_interface_label