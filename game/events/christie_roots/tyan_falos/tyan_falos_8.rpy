
image tyan_falos_8_anim 0 = 'cg/ep86/anim/1.png'
image tyan_falos_8_anim 1:
    'cg/ep86/anim/1.png'
    .17
    'cg/ep86/anim/2.png'
    .17
    'cg/ep86/anim/3.png'
    .17
    'cg/ep86/anim/4.png'
    .17
    'cg/ep86/anim/5.png'
    .17
    'cg/ep86/anim/6.png'
    .17
    'cg/ep86/anim/5.png'
    .17
    'cg/ep86/anim/4.png'
    .17
    'cg/ep86/anim/3.png'
    .17
    'cg/ep86/anim/2.png'
    .17
    repeat

image tyan_falos_8_anim_cum_1:
    'cg/ep86/anim/end_1_1.png'
    .12
    'cg/ep86/anim/end_1_2.png'
    .12
    'cg/ep86/anim/end_1_3.png'
    .12
    '#0000'
    2
    repeat

image tyan_falos_8_anim_cum_2:
    'cg/ep86/anim/end_2_1.png'
    .12
    'cg/ep86/anim/end_2_2.png'
    .12
    'cg/ep86/anim/end_2_3.png'
    .12
    '#0000'
    2.2
    repeat   

image tyan_falos_8_anim 2:
    'cg/ep86/anim/1.png'
    .12
    'cg/ep86/anim/2.png'
    .12
    'cg/ep86/anim/3.png'
    .12
    'cg/ep86/anim/4.png'
    .12
    'cg/ep86/anim/5.png'
    .12
    'cg/ep86/anim/6.png'
    .12
    'cg/ep86/anim/5.png'
    .12
    'cg/ep86/anim/4.png'
    .12
    'cg/ep86/anim/3.png'
    .12
    'cg/ep86/anim/2.png'
    .12
    repeat



image tyan_falos_8_anim 3:
    'cg/ep86/anim/1.png'
    .08
    'cg/ep86/anim/2.png'
    .08
    'cg/ep86/anim/3.png'
    .08
    'cg/ep86/anim/4.png'
    .08
    'cg/ep86/anim/5.png'
    .08
    'cg/ep86/anim/6.png'
    .08
    'cg/ep86/anim/5.png'
    .08
    'cg/ep86/anim/4.png'
    .08
    'cg/ep86/anim/3.png'
    .08
    'cg/ep86/anim/2.png'
    .08

    
    
    
    repeat


image tyan_falos_8_anim 4:
    'cg/ep86/anim/1.png'
    .06
    'cg/ep86/anim/2.png'
    .06
    'cg/ep86/anim/3.png'
    .06
    'cg/ep86/anim/4.png'
    .06
    'cg/ep86/anim/5.png'
    .06
    'cg/ep86/anim/6.png'
    .06
    'cg/ep86/anim/5.png'
    .06
    'cg/ep86/anim/4.png'
    .06
    'cg/ep86/anim/3.png'
    .06
    'cg/ep86/anim/2.png'
    .06
    repeat

image cg ep86 c 1 = 'cg/ep86/c1.png'
image cg ep86 c 2 = 'cg/ep86/c2.png'
image cg ep86 c 3 = 'cg/ep86/c3.png'
image cg ep86 c 3wp = 'cg/ep86/c3wp.png'
image cg ep86 c 4 = 'cg/ep86/c4.png'


image cg_ep86 a 1 = 'cg/ep86/1a.png'

image cg_ep86 a 2 = 'cg/ep86/2a.png'

image cg_ep86 a 3 = 'cg/ep86/3a.png'

image cg_ep86 a 4 = 'cg/ep86/4a.png'

image cg_ep86 a 5 = 'cg/ep86/5a.png'


label tyan_falos_8:

    if getattr(store, 'tyan_falos_day', -999) == time.day_now:
        "[gg]" "Пожалуй хватит на сегодня."
        jump main_interface_label
    #menu:
    #    "1 Уровень":
     #       if getattr(store, 'tyan_falos_day', -999) == time.day_now:
        #"!2 Уровень (WIP)":
     #       $ pass
        #"!3 Уровень (WIP)":
      #      $ pass
label tyan_falos_8_debug:
    if store.test_debug_mod_next:
        $ location_now = 'Corridor'
        scene black
        show image Text('DEBUG: Переход к ивенту tyan_falos_8'):
            align (.5, .5)
        with my_dissolve
        $ renpy.pause(.5, hard = True)
        call wait_click_label from _call_wait_click_label_44
label tyan_falos_8_0_1:
    $ add_to_gallery(33)
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    #show GG Think
    #show GG Think at go_from_left(xxzoom = -1, xxalign = .53)
    # Description: Активировать отверстие в стене при наступлении ночи. 
    # //Событие теперь многоразовое
    # A task: 
    # 1.  Активировать стену и выбрать пункт «1 Уровень».  //Всего будет 3
    # Scene:
    # Wall_First_1
    scene image 'cg/ep86/bg.png'
    show cg_ep86 a 1
    show image 'cg/ep86/falos.png':
        alpha 0.0
    show  image '#000':
        xpos 960
        easein 1.5 alpha .0
        1
        easein 1.5 alpha 1.0
    show cg ep86 c 1:
        xpos -960
    
    show image 'cg/ep86/shadow.png'
    show image 'cg/ep86/fg.png'
    with my_dissolve

    call screen comic_frame(__("Я слышу какой-то шум."), 1215, 250)
    call screen comic_frame(__("Кажется, она ищет свой резиновый фалос. "), 1215, 250)
    call screen comic_frame(__("Ага, точно."), 1215, 250)
    #show  image '#000':
    #    easein .5 alpha .0
    #    easein .5 alpha 1.0
    call screen comic_frame(__("Сейчас она прикрепит его, и нужно было подыскать удобной момент, чтобы заменить его."), 1215, 250)
    #Wall_First_2
    show cg ep86 c 1:
        easein 1 xpos 0
    call screen comic_frame(__("Сегодня я определённо нуждаюсь своём «дружке»."), 50, 300, -1.0)
    #Wall_First_3
    show cg ep86 c 2
    show image 'cg/ep86/falos.png':
        alpha 1.0
    with my_dissolve
    #show  image '#000':
    #    easein .5 alpha .0
    #    easein .5 alpha 1.0
    call screen comic_frame(__("Вот, вроде держится."), 50, 300, -1.0)
    show cg ep86 c 3
    with my_dissolve
    call screen comic_frame(__("Отлично."), 50, 300, -1.0)
    #Wall_First_4
    hide  image '#000'
    show cg ep86 c 4
    show cg_ep86 a 2
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show cg_ep86 a 3
    hide image 'cg/ep86/falos.png'
    with Dissolve(.5)
    $ renpy.pause(.9, hard = True)
    
    show cg_ep86 a 4
    with my_dissolve
    call screen comic_frame(__("Пора снять трусики и предаться блаженству." ), 360, 350)
    #Wall_First_5 //здесь меняется фалос
    #Wall_First_6 //здесь меняется фалос
    
    #with my_dissolve
    show cg ep86 c 3
    with my_dissolve
    call screen comic_frame(__("Что за?.."), 50, 290, -1.0)
    
    call screen comic_frame(__("[gg] действительно думает, что я поверю в такую подмену?"), 50, 290, -1.0)
    call screen comic_frame(__("Какой же дурак…"), 50, 290, -1.0)
    call screen comic_frame(__("И теперь дрожит в ожидании, полагая, видимо, что я вот-вот воспользуюсь его агрегатом."), 50, 290, -1.0)
#   Wall_First_6 //Здесь нужно показать ГГ
    show cg_ep86 a 5
    with my_dissolve
   # hide  image '#000'
    call screen comic_frame(__("Почему она так долго? "), 1215, 250)
    call screen comic_frame(__("Она ищет смазку?.."), 1215, 250)
 
    if preferences.language in (None, 'eng', 'rus'):
        call screen comic_frame(__("Чёрт…"), 50, 260, -1.0)
    
    scene image 'cg/ep86/bg.png'
    show image 'cg/ep86/6a.png'
    show image 'cg/ep86/fg.png'
    with my_dissolve

    call screen comic_frame(__("А его член и вправду выглядит привлекательным."), 50, 260, -1.0)
    call screen comic_frame(__("Особенно сейчас, когда я намеревалась удовлетворить себя."), 50, 260, -1.0)
    call screen comic_frame(__("Он стал немного мокреньким… хи-хи-хи."), 50, 260, -1.0)
    call screen comic_frame(__("Перевозбудился от мысли, что сможет почувствовать мою киску сейчас."), 50, 260, -1.0)
    call screen comic_frame(__("Что ж… "), 50, 260, -1.0)
    call screen comic_frame(__("Подыграю ему немножко. "), 50, 260, -1.0)
    #Wall_First_7

    scene image 'cg/ep86/bg.png'

    show image 'cg/ep86/7a.png'
    show image 'cg/ep86/fg.png'
    with my_dissolve
    call screen comic_frame(__("Наконец-то!"), 1215, 250)
    call screen comic_frame(__("Она трогает меня своей киской…"), 1215, 250)
    call screen comic_frame(__("Боже, как же это волнительно!"), 1215, 250)
    call screen comic_frame(__("Уххх… Его член так напрягся сразу."), 60, 270, -1.0)
    call screen comic_frame(__("Пожалуй, немного пошалить я с ним могу."), 60, 270, -1.0)
    call screen comic_frame(__("Пока что без проникновения, конечно."), 60, 270, -1.0)
    call screen comic_frame(__("Но, думается мне, он и так будет всецело доволен."), 60, 270, -1.0)
    #Wall_First_7_anim
    #//Анимация

    scene image 'cg/ep86/bg.png'
    show image 'cg/ep86/anim/bg.png'
    show tyan_falos_8_anim 1
    show image 'cg/ep86/anim/fg.png'
    show image 'cg/ep86/8.png'
    show image 'cg/ep86/fg.png'
    with my_dissolve
    call screen comic_frame(__("Обалдееееееть!..."), 1215, 250)
    call screen comic_frame(__("Она трётся об меня половыми губками, и даже не подозревает, что на самом деле это мой член."), 1215, 250)
    call screen comic_frame(__("Наивная, но страстная Кристи."), 1215, 250)#/*сестрёнка
    call screen comic_frame(__("Ощущать её мокрую киску просто блаженство."), 1215, 250)
    call screen comic_frame(__("Аххх… Как же тепло и мокро от её прикосновения. Наверняка она сейчас мечтает о том, чтобы быть со мной рядом. "), 1215, 250)
    call screen comic_frame(__("[gg] держится молодцом хи-хи."), 60, 210, -1.0)
    call screen comic_frame(__("Практически не шевелится, притворяясь моим бездушным фалоимитатором. "), 60, 210, -1.0)
    call screen comic_frame(__("Стоит признать, чувствовать настоящий член куда приятней, чем дурацкую резину. "), 60, 210, -1.0)
    call screen comic_frame(__("О даааа…. Очень хорошо. "), 60, 210, -1.0)
    call screen comic_frame(__("Я могу использоваться его орган, как пожелаю, а [gg] даже не шелохнётся, надеясь, что я не распознаю «подделки»."), 60, 210, -1.0) #/*братик
    #//Скорость х2
label tyan_falos_8_1:
    menu:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            call wait_click_label from _call_wait_click_label_49
            jump tyan_falos_8_1
    show tyan_falos_8_anim 2
    call screen comic_frame(__("Она стала шустрее!"), 1215, 250)
    call screen comic_frame(__("Но, почему-то, всё ещё не впустила мой член внутрь себя."), 1215, 250)
    call screen comic_frame(__("Я немного разыгралась… "), 60, 210, -1.0)
    call screen comic_frame(__("[gg] стоит за стенкой и сходит с ума, наверняка думая о том, как бы не кончить раньше времени. "), 60, 210, -1.0)
    call screen comic_frame(__("Чтож… Ему придётся изрядно постараться, раз уж он так сильно этого хочет."), 60, 210, -1.0)
    call screen comic_frame(__("Я не планирую заканчивать слишком быстро."), 60, 210, -1.0)
    call screen comic_frame(__("Всякий раз, когда головка члена касается моего клитора, по всему телу пробегает приятный электрический заряд."), 60, 210, -1.0)
    call screen comic_frame(__("И чем быстрее я двигаюсь, тем сильнее меня обуревает ощущение полного экстаза. "), 60, 210, -1.0)
    call screen comic_frame(__("Интересно, что в этот момент чувствует [gg]?"), 60, 210, -1.0)#/*братик
label tyan_falos_8_2:
    menu:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            call wait_click_label from _call_wait_click_label_50
            jump tyan_falos_8_2
    show tyan_falos_8_anim 3
    call screen comic_frame(__("Ещё немного и я взорвусь от удовольствия…"), 1215, 250)
    call screen comic_frame(__("Я совсем не рассчитывал на такую бурную реакцию на мой член. "), 1215, 250)
    call screen comic_frame(__("Мне… Надо… Паузу…"), 1215, 250)
    call screen comic_frame(__("Одаааа, офигеть! Вот так, ещё-ещё-ещё!"), 50, 210, -1.0)
    call screen comic_frame(__("Знаю, [gg], ты уже на грани, но позволь мне ещё чуточку помучать тебя."), 50, 210, -1.0)
    call screen comic_frame(__("В тебе столько заряженной энергии…."), 50, 210, -1.0)
    call screen comic_frame(__("Столько сил, который ты копил всё это время… Для этой ночи."), 50, 210, -1.0)
    call screen comic_frame(__("Конечно, ты ожидал совсем другого..."), 50, 210, -1.0)
    call screen comic_frame(__("Но мне почему-то кажется - разочарованным ты не останешься."), 50, 210, -1.0)
    call screen comic_frame(__("Я почти… Я уже практически кончил…"), 1215, 250)
    call screen comic_frame(__("Ха, интересно, а как он предполагал притворить свой план действия, если в конце, когда он кончит, я всё равно пойму, что это член, а не просто резиновая игрушка? "), 30, 240, -1.0)
    if preferences.language in (None, 'eng', 'rus'):
        call screen comic_frame(__("Хи-хи-хи!"), 50, 210, -1.0)
    call screen comic_frame(__("Судя по его состоянию полнейшего релакса и тяжёлого дыхания, которое я слышу даже через стену, ему уже на всё плевать."), 50, 210, -1.0)
    call screen comic_frame(__("Да и разве можно думать про секс, как о чём-то рациональном?.."), 50, 210, -1.0)
    call screen comic_frame(__("По крайней мере я сейчас думаю только о его члене!.."), 50, 210, -1.0)
    call screen comic_frame(__("Я… Я…"), 50, 210, -1.0)
label tyan_falos_8_3:
    menu:
        "Кончить":
            $ pass
        "Продолжить в том же темпе":
            call wait_click_label from _call_wait_click_label_51
            jump tyan_falos_8_3
    show tyan_falos_8_anim 4
    #Wall_First_8
    call screen comic_frame(__("Кончааааюююууууууу!!!"), 1215, 250)
    call screen comic_frame(__("Ахххххххх!!"), 50, 210, -1.0)
    call screen comic_frame(__("Уффффф!!"), 50, 210, -1.0)
    call screen comic_frame(__("Дааааа…."), 50, 210, -1.0)
    #Wall_First_9
    show white with Dissolve(.75)
    #$ add_ach('ACH_15')

    # python:
    #     achievement.grant("ACH_15")
    #     achievement.sync()

    $ renpy.pause(.5, hard = True)
    scene image 'cg/ep86/bg.png'
    show image 'cg/ep86/anim/bg.png'
    show tyan_falos_8_anim 0
    show image 'cg/ep86/anim/final.png'
    show tyan_falos_8_anim_cum_1
    show tyan_falos_8_anim_cum_2
    show image 'cg/ep86/anim/fg.png'
    show image 'cg/ep86/8.png'
    show image 'cg/ep86/sperm.png'
    show image 'cg/ep86/fg.png'
    with my_dissolve
    call screen comic_frame(__("Вау, как же много он накончал."), 50, 210, -1.0)
    call screen comic_frame(__("И всё это он планировал выплеснуть в меня?.. Ну дела…."), 50, 210, -1.0)
#   Wall_First_10
    call screen comic_frame(__("Ну всё, дружок. Сладких снов и до новых встреч! Целую, люблю."), 50, 210, -1.0)

    $ tyan_falos_text = _("Теперь я могу забавляться с этой дырой в стене хоть каждую ночь...")
    $ tyan_falos_day = time.day_now
    $ debug_exit()
    jump main_interface_label

