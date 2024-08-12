
screen ep4_milf_41_screen:
    imagebutton:
        idle "locations/imagebuttons/ClothesStore/Sit.png"
        hover im.MatrixColor("locations/imagebuttons/ClothesStore/Sit.png", im.matrix.brightness(.3))
        focus_mask True
        at ButtonEffect01
        action Return()


    add 'gradient_up'





    button ypos 20 xpos 130+130:
        add 'quest_button'
        action Function(show_descript_screen)
    if old_descript != descript:
        add 'warning_icon' xpos 340 ypos 100

    button ypos 20 xpos 130:
        add 'bag_button'
        action Show('bag_interface', transition = Dissolve(.5))


    button:
        add 'mobile_button'
        action NullAction()



    button:
        add time.time_now+'_button'
        xalign .5


        action NullAction()


    viewport:
        xmaximum 170
        ymaximum 195
        xalign .5
        imagebutton:
            idle '#0000'
            hover '#0000'
            action NullAction()

    add 'pause_icon' xalign .5










    add 'interface/Panel_Money.png' xalign 1.0
    text '$' + str(money) xalign .9 color '#000' ypos 40
    add 'interface/Panel_Day.png' xpos 587 ypos 30
    add 'interface/Panel_Day.png' xpos 1020 ypos 30 xzoom -1
    viewport:
        xmaximum 310
        ymaximum 90
        add '#0000'


        $ times = time.tdtd.title()
        text _(str(times)) color '#000' xalign .5 yalign .5 size 25
        xpos 587 ypos 30
    viewport:
        xmaximum 310
        ymaximum 90
        add '#0000'

        $ times = rus_time[time.time_now].title()
        text _(str(times)) xalign .5 yalign .5 color '#000' size 25
        xpos 1020 ypos 30


label ep4_milf_41:
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    $ Hide('main_interface')()


    scene expression 'locations/bg/ClothesStore/night.png'
    show Milf Street_Normal
    show Milf Street_Normal:
        xzoom -1
        xalign -0.5
        ypos 1085


    show GG Normal
    show GG Normal:

        xalign -0.5
        ypos 1085

    show Masha Normal
    show Masha Normal:
        xzoom 1
        xalign 1.5
        ypos 1085

    with Dissolve(.5)


    show Milf Street_Normal
    show Milf Street_Normal:
        xzoom -1
        linear .75 xalign .05
        ypos 1085


    show GG Normal
    show GG Normal:

        linear .75 xalign .3
        ypos 1085

    show Masha Normal
    show Masha Normal:
        xzoom 1
        linear .75 xalign .85
        ypos 1085


    $ renpy.pause(.75, hard = True)

    show Milf Street_Normal:
        xzoom -1
        xalign .05
        ypos 1085


    show GG Normal:

        xalign .3
        ypos 1085

    show Masha Normal:
        xzoom 1
        xalign .85
        ypos 1085



    with my_dissolve











    "Администратор" "Чем могу быть полезна? У нас самый большой выбор платьев, лучшие новинки сезона и цены на любой вкус. "
    show Milf Street_Normal
    "Марина" "Мы разберёмся."

    "Администратор" "Как вам угодно. Если что, я рядом. Зовите. Подскажу и покажу."
    show Milf Street_Normal
    "Марина" "Леди, вы свободны. "

    "Администратор" "Ой. Извините."

    show Masha Normal:
        xzoom -1
        linear 1 xalign 1.5
        ypos 1085

    show Milf:
        xzoom -1
        linear 1 xalign .85
        ypos 1085


    $ renpy.pause(1, hard  = True)



    hide Masha
    show Milf Street_Normal:
        xzoom 1
        xalign .85
        ypos 1085
    with my_dissolve

    "Марина" "Присаживайся, малыш. Я буду примерять платье."


    show Milf Street_Normal:
        xzoom -1
        linear 1 xalign 1.5

    $ renpy.pause(1, hard = True)
    $ descript = _("Сесть на диван.")
    scene expression 'locations/bg/ClothesStore/night.png'
    show GG Think
    with Dissolve(.5)

    "[gg]" "Ну и где мне усесться?"

    scene expression 'locations/bg/ClothesStore/night.png'
    with Dissolve(.5)

    call screen ep4_milf_41_screen
    jump ep4_milf_42
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
