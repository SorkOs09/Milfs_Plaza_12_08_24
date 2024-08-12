image tyan_falos_9_anim 0_1 = 'cg/ep86/blowjob_1.png'
image tyan_falos_9_anim 0_2 = 'cg/ep86/blowjob_2.png'

image tyan_falos_9_anim_panel end = 'cg/ep86/steam/end.png'

image tyan_falos_9_anim_panel_sperm_1:
    'cg/ep86/steam/sperm/1.png'
    .18
    'cg/ep86/steam/sperm/2.png'
    .18
    'cg/ep86/steam/sperm/3.png'
    .18
    'cg/ep86/steam/sperm/4.png'
    .18
    'cg/ep86/steam/sperm/5.png'
    .18
    'cg/ep86/steam/sperm/6.png'


image tyan_falos_9_anim_panel_sperm_2:# = LiveComposite((1920, 1080), (0, 0), Solid('#F00a'))
    'cg/ep86/steam/sperm/1.png'
    .18
    'cg/ep86/steam/sperm/2.png'
    .18
    'cg/ep86/steam/sperm/3.png'
    .18
    'cg/ep86/steam/sperm/4.png'
    .18
    'cg/ep86/steam/sperm/5.png'
    .18
    'cg/ep86/steam/sperm/6.png'


image tyan_falos_9_anim_panel_sperm_3:
    'cg/ep86/steam/sperm/1.png'
    .18
    'cg/ep86/steam/sperm/2.png'
    .18
    'cg/ep86/steam/sperm/3.png'
    .18
    'cg/ep86/steam/sperm/4.png'
    .18
    'cg/ep86/steam/sperm/5.png'
    .18
    'cg/ep86/steam/sperm/6.png'


image tyan_falos_9_anim_panel 1:
    'cg/ep86/steam/1.png'
    .18
    'cg/ep86/steam/2.png'
    .18
    'cg/ep86/steam/3.png'
    .18
    'cg/ep86/steam/4.png'
    .18
    'cg/ep86/steam/5.png'
    .18
    'cg/ep86/steam/6.png'
    .18
    'cg/ep86/steam/5.png'
    .18
    'cg/ep86/steam/4.png'
    .18
    'cg/ep86/steam/3.png'
    .18
    'cg/ep86/steam/2.png'
    .18
    repeat

image tyan_falos_9_anim_panel 2:
    'cg/ep86/steam/1.png'
    .12
    'cg/ep86/steam/2.png'
    .12
    'cg/ep86/steam/3.png'
    .12
    'cg/ep86/steam/4.png'
    .12
    'cg/ep86/steam/5.png'
    .12
    'cg/ep86/steam/6.png'
    .12
    'cg/ep86/steam/5.png'
    .12
    'cg/ep86/steam/4.png'
    .12
    'cg/ep86/steam/3.png'
    .12
    'cg/ep86/steam/2.png'
    .12
    repeat

image tyan_falos_9_anim_panel 3:
    'cg/ep86/steam/1.png'
    .09
    'cg/ep86/steam/2.png'
    .09
    'cg/ep86/steam/3.png'
    .09
    'cg/ep86/steam/4.png'
    .09
    'cg/ep86/steam/5.png'
    .09
    'cg/ep86/steam/6.png'
    .09
    'cg/ep86/steam/5.png'
    .09
    'cg/ep86/steam/4.png'
    .09
    'cg/ep86/steam/3.png'
    .09
    'cg/ep86/steam/2.png'
    .09
    repeat


image tyan_falos_9_anim 1:
    'cg/ep86/blowjob_1.png' with Dissolve(.3)
    1.5
    'cg/ep86/blowjob_2.png' with Dissolve(.3)
    1.5
    repeat

image tyan_falos_9_anim 2:
    'cg/ep86/blowjob_1.png' with Dissolve(.3)
    1.2
    'cg/ep86/blowjob_2.png' with Dissolve(.3)
    1.2
    repeat

image tyan_falos_9_anim 3:
    'cg/ep86/blowjob_1.png' with Dissolve(.1)
    1.0
    'cg/ep86/blowjob_2.png' with Dissolve(.1)
    1.0
    repeat


label tyan_falos_9:
    #Wall_First_1
    $ add_to_gallery(48)
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    $ events.pop('tyan_falos_9', 0)
    scene image 'cg/ep86/bg.png'
    show GG Invis
    show GG Invis:
        xalign .65
    show Christie Invis
    show Christie Invis:
        xalign .2
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

    $ sex_name_box = True
    "[gg]" "Ага, ей снова не спится."
    "[gg]" "Хочет поиграть со своим силиконовым дружком."
    "[gg]" "Что ж, я тоже не прочь немного развлечься…"

    #Wall_First_2
    show cg ep86 c 1:
        easein 1 xpos 0
    "Кристи" "Интересно, [gg] снова решит меня разыграть и просунет свой член, вместо моего фалоимитатора?  "

    $ sex_name_box = False
    show cg ep86 c 2
    show image 'cg/ep86/falos.png':
        alpha 1.0
    with my_dissolve

    $ sex_name_box = True
    "Кристи" "Кажись прикрепила."
#Wall_First_4

    $ sex_name_box = False
    hide  image '#000'
    show cg ep86 c 4
    show cg_ep86 a 2
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show cg_ep86 a 3
    hide image 'cg/ep86/falos.png'
    with Dissolve(.5)
    $ renpy.pause(.9, hard = True)
    
    show cg_ep86 a 5

    show cg ep86 c 3
    with my_dissolve


    $ sex_name_box = True
    #Wall_First_5 //здесь меняется фалос

    #Wall_First_6 //здесь меняется фалос

    #Wall_First_1 //я не помню какой спрайт, нужен тот, где она смотрит на член гг


    "Кристи" " Ах ты ж мелкий говнюк!"
    "Кристи" "Не спит. Караулит меня. "
    "Кристи" "Интересно, как долго он простоял у стены?.. "
    "[gg]" "Ну чего она тянет-то?.."
    "[gg]" "Уснула, что ли?"
    "Кристи" "Терпеливый сукин сын, хи-хи-хи."
    "Кристи" "Наверное, в полном недоумении, почему я ещё не «зарядила его револьвер»."
    "Кристи" "Ну ничего-ничего."
    "Кристи" "Постой. "
    "Кристи" "Помучайся. Тебе полезно, хи-хи-хи."
    "Кристи" "Но кого я мучаю-то?.."
    "Кристи" "Скорее себя, чем его."
    hide cg ep86 c 3
    show cg_ep86 a 5
    
    show tyan_falos_9_anim 0_1
    with my_dissolve
    
    "Кристи" "Его член выглядит таким привлекательным и… возбуждённым. "
    "Кристи" "Я и сама немного завелась."
    hide cg_ep86 a 5
    
    show tyan_falos_9_anim 0_2
    with my_dissolve
    "Кристи" "Пожалуй, ничего не станется, если я немного пошалю с ним."
    show image "cg/ep86/steam/panel_bg.png"
    show tyan_falos_9_anim_panel 1
    show image "cg/ep86/steam/panel_fg.png"
    with my_dissolve
    #Wll_Minet_Anim


    "[gg]" "Вау!.."
    "[gg]" "Она что, взяла его в рот?!"
    "[gg]" "Разве женщины берут фалоимитаторы в рот?.."
    "[gg]" "Мне казалось, их используют для других, более насущных целей."
    "[gg]" "Может… Она просто тренируется?"

  #  show tyan_falos_9_anim 0_1
  #  with my_dissolve
    "Кристи" "Мммм…"
    "Кристи" "Какой он ароматный и необычный на вкус."
    "Кристи" "Сложно поверить, что мужской детородный орган может вызывать столько вульгарных позывов."
    "Кристи" "А ведь я даже не планировала ничем таким заниматься."
    "Кристи" "Просто хотела проверить, как сильно [gg] желает меня."

    #show tyan_falos_9_anim 0_2
    #with my_dissolve
    "Кристи" "Но завидев его член, и сама его захотела."
    "Кристи" "Тут ещё стоит поспорить, у кого из нас большая зависимость друг от друга."
    show tyan_falos_9_anim_panel 2
    with my_dissolve
    #//x2


    "[gg]" "Воу-воу! Её энтузиазм возрос. "
    "[gg]" "Я слышу её громкие причмокивания"
    "[gg]" "Кристи определённо наслаждается процессом. Её прям распирает от удовольствия."
    "[gg]" "А ведь она ей и в голову не придёт, что тренируясь с фалосом, она реализует своё мастерство на практике."
    
   # show tyan_falos_9_anim 0_1
   # with my_dissolve
    "Кристи" "Какой же он всё-таки болван."
    "Кристи" "Наверняка убеждён в том, что я не догадываюсь о его подмене. "
    "Кристи" "Так и хочется прикусить его немного… Ну так, забавы ради."
    "Кристи" "[gg] или стерпит, чтобы не попасться, или завоет, и тогда мы оба окажемся в неловкой ситуации."
    "Кристи" "Ему придётся оправдываться, а мне придётся делать вид, что я обижаюсь."
    "Кристи" "И ни он, ни я не получим никакого удовольствия. "
    "Кристи" "Пусть это останется нашей тайной, которую мы негласном скрываем друг от друга."
    #//x3
    show tyan_falos_9_anim_panel 3
    with my_dissolve

    "[gg]" "У Кристи проснулся аппетит."
    "[gg]" "Она буквально запихивает мой член себе в глотку…"
    "[gg]" "Это просто офигено! "
    "[gg]" "Я и сам чувствую, что немного подталкиваю её…"
    "[gg]" "Надеюсь, она не замечает моих телодвижений, но устоять перед её минетом становится невыносимо."
    "[gg]" "И я вот-вот готов кончить ей в рот…"
    "[gg]" "Чёрт, но если я сделаю это, она точно всё поймёт!!!"
    "Кристи" "Ух ты! Его член разбух до чудовищных размеров."
    "Кристи" "Судя по всему, он уже готов выплеснуть семя."
    "Кристи" "Но если это произойдёт, то его маскировка будет раскрыта."
    "[gg]" "Блядь, я уже не могу терпеть…"
    "Кристи" "Если я не выпью его сперму, все мои усилия пропадут даром."
    "Кристи" "Да, есть идея!"
    "Кристи" "Когда я пойму, что он вот-вот кончит, просто выну его член изо рта, словно я закончила, а на самом деле останусь и всё проглочу! "
    #// кончить

    "[gg]" "Всё… Не могу…"
    
    
    "[gg]" "Кончаюююююууууууу бляаааааадь!"
    $ sex_name_box = False
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_47
    show tyan_falos_9_anim 0_2
    show tyan_falos_9_anim_panel end
    show tyan_falos_9_anim_panel_sperm_1
    with my_dissolve

    $ renpy.pause(.6, hard = True)
    show tyan_falos_9_anim_panel_sperm_2
    show tyan_falos_9_anim_panel_sperm_2:
        pos (960, 1080) alpha 1.0
        easein .3 pos (960-50, 1080)
        easein .3 pos (960-50, 1090) alpha .5
        


    $ renpy.pause(.6, hard = True)
    show tyan_falos_9_anim_panel_sperm_3
    show tyan_falos_9_anim_panel_sperm_3:
        pos (960, 1080)
        easein .3 pos (960-90, 1080-90)
    
    $ renpy.pause(1.0, hard = True)

    $ sex_name_box = True
        
    "[gg]" "Оххх…"
    "[gg]" "Мне фантастически повезло. Кажется она ушла."
    "[gg]" "Ещё чуть-чуть и я попался бы."
    "Кристи" "Какое вкусное лакомство."
    "Кристи" "Мммммм…"
    "Кристи" "Спасибо, [gg]!"
    "Кристи" "Это был чудесный десерт перед сном."
    scene black with my_dissolve
    $ location_now = 'Corridor'
    jump main_interface_label