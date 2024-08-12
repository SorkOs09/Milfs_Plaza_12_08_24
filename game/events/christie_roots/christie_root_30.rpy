
image christie_root_30_anim:
    'cg/christie_root/falos/1.png' with Dissolve(.02)
    .18
    'cg/christie_root/falos/2.png' with Dissolve(.02)
    .18
    'cg/christie_root/falos/3.png' with Dissolve(.02)
    .18
    'cg/christie_root/falos/4.png' with Dissolve(.02)
    .18
    'cg/christie_root/falos/5.png' with Dissolve(.02)
    .18
    'cg/christie_root/falos/4.png' with Dissolve(.02)
    .18
    'cg/christie_root/falos/3.png' with Dissolve(.02)
    .18
    'cg/christie_root/falos/2.png' with Dissolve(.02)
    .18
    repeat
image christie_root_30_anim_2:
    'cg/christie_root/falos/1.png'
    .13
    'cg/christie_root/falos/2.png'
    .13
    'cg/christie_root/falos/3.png'
    .13
    'cg/christie_root/falos/4.png'
    .13
    'cg/christie_root/falos/5.png'
    .13
    'cg/christie_root/falos/4.png'
    .13
    'cg/christie_root/falos/3.png'
    .13
    'cg/christie_root/falos/2.png'
    .13
    repeat
image christie_root_30_anim_3:
    'cg/christie_root/falos/1.png'
    .1
    'cg/christie_root/falos/2.png'
    .1
    'cg/christie_root/falos/3.png'
    .1
    'cg/christie_root/falos/4.png'
    .1
    'cg/christie_root/falos/5.png'
    .1
    'cg/christie_root/falos/4.png'
    .1
    'cg/christie_root/falos/3.png'
    .1
    'cg/christie_root/falos/2.png'
    .1
    repeat


image christie_root_30_anim_4:
    'cg/christie_root/falos/1.png'
    .08
    'cg/christie_root/falos/2.png'
    .08
    'cg/christie_root/falos/3.png'
    .08
    'cg/christie_root/falos/4.png'
    .08
    'cg/christie_root/falos/5.png'
    .08
    'cg/christie_root/falos/4.png'
    .08
    'cg/christie_root/falos/3.png'
    .08
    'cg/christie_root/falos/2.png'
    .08
    repeat
transform christie_root_30_move_door_close:
    xpos -470

    easein_cubic .5 xpos 0

transform christie_root_30_move_door_open:
    xpos 0

    easein_cubic .5 xpos -470


define christie_root_30_move_door_close_w = { "master" : christie_root_30_move_door_close}

define christie_root_30_move_door_open_w = { "master" : christie_root_30_move_door_open}


screen christie_root_30_screen(circle_position=1, img='cg/christie_root/falos/1_0.png'):


    if circle_position     == 1:
        add img:
            at transform:
                xpos 0
                .75
                easein_cubic .5 xpos -50
                .25
                easeout_cubic .5 xpos 0
                1.75
                repeat

        imagebutton:
            xpos 1100
            ypos 800
            idle 'circle_mini_game'
            hover 'circle_mini_game'
            xanchor .5
            yanchor .5








            action Return()

    if circle_position     == 2:
        imagebutton:
            xpos 300
            ypos 800
            idle 'circle_mini_game'
            hover 'circle_mini_game'
            xanchor .5
            yanchor .5








            action Return()
            at transform:
                .75
                easein_cubic .25 zoom .9
                easein_cubic .25 zoom 1.0
                easein_cubic .25 zoom .9
                easein_cubic .25 zoom 1.0
                2.75
                repeat
    if circle_position     == 3:
        imagebutton:
            xpos 1030
            ypos 450
            idle 'circle_mini_game'
            hover 'circle_mini_game'
            xanchor .5
            yanchor .5

            action Return()
            at transform:
                .5
                easein_cubic .25 zoom .7
                easein_cubic .25 zoom .8
                easein_cubic .25 zoom .7
                easein_cubic .25 zoom .8
                2.5
                repeat
label christie_root_30:
    scene black with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    scene expression 'cg/christie_root/falos/Start.png'
    show expression 'cg/christie_root/falos/1_0.png':
        xpos 0
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    scene expression 'cg/christie_root/falos/Start.png'
    call screen christie_root_30_screen(1)
    show expression 'cg/christie_root/falos/1_0.png'
    with None
    show expression 'cg/christie_root/falos/1_1.png':
        xpos 0
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    hide expression 'cg/christie_root/falos/1_0.png'
    call screen christie_root_30_screen(2)
    show expression 'cg/christie_root/falos/1_1.png':
        xpos 0
        easein_cubic 1.5 xpos -470
    $ renpy.pause(1.6, hard = True)
    scene expression 'cg/christie_root/falos/Start.png'
    with Dissolve(.5)



    $ renpy.pause(.5, hard = True)
    $ renpy.pause(999)
    scene christie_root_30_anim with Dissolve(.5)
    
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/aerosol-of-my-love-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Кристи" "Уххх!!..."
    "Кристи" "Афффф!.."
    "Кристи" "Уффф!.."
    "Кристи" "Да-да-да!"
    "[gg]" "Вау…"
    "[gg]" "Этого я совсем не ожидал."
    "[gg]" "Она приклеила резиновый фалос к стене и теперь трахается с ним. "
    "[gg]" "Если она продолжит это делать с таким же упорством, как сейчас, однажды моя стена рухнет мне прям на голову. "

    menu:
        "Ускориться" if True:
            $ pass
    scene christie_root_30_anim_2 with Dissolve(.5)
    "Кристи" "Мммм!!..."
    "Кристи" "Ох-ох-ох-ох!!"
    "Кристи" "Уф-уф-уф!"
    "[gg]" "Кажется, её этот факт совсем не волнует."
    "[gg]" "Да чего уж там…"
    "[gg]" "Глядя на это торжество жизни, я, пожалуй, готов пойти на эту жертву. "
    "[gg]" "И даже поспособствовать этому. "
    "[gg]" "Пусть ломает всё, что ей вздумается."
    "[gg]" "Главное, чтобы ей было хорошо, и это послужило бы поводом разделить этот миг со мной…"

    menu:
        "Ускориться" if True:
            $ pass
    scene christie_root_30_anim_3 with Dissolve(.5)
    "[gg]" "С каким же страстным рвением она удовлетворяет свою похоть! "
    "[gg]" "Такая искренняя в гармонии со своим телом."
    "[gg]" "Большая редкость для мужчин, видеть как девушка по-настоящему получает удовольствие…"
    "[gg]" "Охх…"
    "[gg]" "Мне лишь остаётся смотреть и облизываться."
    "[gg]" "Давай, детка, кончай."
    "[gg]" "Кончай столько, сколько тебе нужно!"
    menu:
        "Ускориться" if True:
            $ pass

    scene christie_root_30_anim_4 with Dissolve(.5)
    "Кристи" "Уххх!!..."
    "Кристи" "Афффф!.."
    "Кристи" "Уффф!.."

    scene white with Dissolve(.5)

    $ renpy.pause(.75, hard = True)
    scene expression 'cg/christie_root/falos/6.png'
    with my_vpunch

    "Кристи" "Нет!"
    show expression 'cg/christie_root/falos/1_1.png' at christie_root_30_move_door_close

    "[gg]" "Что?! Она заметила меня?"
    "Кристи" "Нет, это просто невозможно!"
    "Кристи" "Мне нужен настоящий."
    show expression 'cg/christie_root/falos/1_1.png' at christie_root_30_move_door_open

    "Кристи" "Никакой искусственный фаллос мне не поможет."
    "Кристи" "Мне нужен секс. С мужчиной…"
    "Кристи" "С мужчиной, которого я люблю."
    "[gg]" "Вау, а у неё реально проблем-ка."
    "Кристи" "Может всё-таки…"
    "Кристи" "Нет, я не могу ему сознаться!"
    "Кристи" "Нужно просто найти парня и точка."


    show expression 'cg/christie_root/falos/1_1.png' at christie_root_30_move_door_close
    $ renpy.pause(.6, hard = True)
    scene black with Dissolve(.5)
    $ location_now  = 'Corridor'
    $ time.time_now = 'night'
    $ renpy.pause(.5, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_151
    with Dissolve(.5)
    $ renpy.pause(.5)
    show GG Think
    show GG Think:
        xalign .5
    with my_dissolve
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/almost-bliss-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Чёрт…"
    show GG Think
    "[gg]" "Я могу потерять её."
    show GG Think
    "[gg]" "Только не сейчас…"



    scene black with Dissolve(.5)
    if not from_gallery_check():
        $ location_now = "GG_Room"

        $ time.time_now   = 'night'

        if 'christie_root_30' in allowed_events:
            $ allowed_events.remove("christie_root_30")



        $ block_exit_home     = copy.deepcopy(block_exit_home_tmp)
        $ block_milf_home     = copy.deepcopy(block_milf_home_tmp)

        $ block_time_forward = copy.deepcopy(block_time_forward_tmp)


        $ Event('christie_root_31', 'GG_Room',  time = ['morning'])
        $ Event('christie_root_31b', 'City_Psi', time = ['morning', 'afternoon'])
        $ events.pop('christie_root_29', 0)
        $ events.pop('christie_root_30', 0)
        $ add_to_gallery(28)



        $ descript_Christie= _("Поговорить со Сьюзен по поводу работы.")
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
