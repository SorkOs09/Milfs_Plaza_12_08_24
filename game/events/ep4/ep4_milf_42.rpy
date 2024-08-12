

init python:
    def ep4_milf_42_tmp_def(i):
        global ep4_milf_42_tmp, ep4_milf_42_tmp_dir
        ep4_milf_42_tmp_dir.update({i:len(ep4_milf_42_tmp)})
        ep4_milf_42_tmp.append(i)

screen ep4_milf_42_screen:
    for i in xrange(5):
        imagebutton:
            idle "cg/ep4/ClothesShop/Doors/"+str(i)+".png"
            hover im.MatrixColor("cg/ep4/ClothesShop/Doors/"+str(i)+".png", im.matrix.brightness(.3))
            focus_mask True
            at ButtonEffect01
            if len(ep4_milf_42_tmp) < 5:
                if i not in ep4_milf_42_tmp:

                    action Function(ep4_milf_42_tmp_def, i), Jump('ep4_milf_42_ClothesShopDoor_'+str(len(ep4_milf_42_tmp)))
                else:
                    action Jump('ep4_milf_42_ClothesShopDoor_'+str(ep4_milf_42_tmp_dir[i]))

            else:
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






screen ep4_milf_42_locker_screen:
    imagebutton:
        idle "cg/ep4/ClothesShop/ClothesStoreLocker.png"
        hover im.MatrixColor("cg/ep4/ClothesShop/ClothesStoreLocker.png", im.matrix.brightness(.3))
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
label ep4_milf_42:



    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    scene expression 'locations/bg/ClothesStore/night.png'
    show expression 'cg/ep4/ClothesShop/gg_divan_1.png'

    with Dissolve(.5)
    "[gg]" "Надеюсь, мне не придётся ждать целую вечность. "


    "[gg]" "Учитывая, что мой лучший друг кинул меня на деньги, жить мне осталось не долго."


    "[gg]" "И что дальше? Бежать? Трястись за свою шкуру до конца своих дней, оглядываясь, прячась? "


    "[gg]" "В задницу это. "


    "[gg]" "Хватит с меня бестолковых волнений и боязни смерти."

    show Milf Dress_Pose_1
    show Milf Dress_Pose_1:
        xalign 1.6

    "[gg]" "Теперь мне есть ради кого жить, пусть эта жизнь и не обещать быть долгой, зато счастливой."

    show Milf Dress_Pose_1:
        xzoom 1
        linear .75 xalign .85
        ypos 1085

    $ renpy.pause(.75, hard = True)

    scene expression 'locations/bg/ClothesStore/night.png'

    show expression 'cg/ep4/ClothesShop/gg_divan_2.png'
    show Milf Dress_Pose_1
    show Milf Dress_Pose_1:
        xzoom 1
        xalign .85
        ypos 1085

    with Dissolve(.5)


    "[gg]" "Воу!!!"


    "Марина" "Нравится? "






    menu:
        "1. Я в восторге! " if True:


            $ pass
        "2. Круто, но чего-то не хватает." if True:


            $ pass
        "3. Давай и другие посмотрим." if True:


            $ pass













    "Марина" "Всё ради тебя, милый. Сейчас вернусь."

    show Milf Dress_Pose_1:
        xzoom -1
        linear .75 xalign 1.6
        ypos 1085


    $ renpy.pause(.75, hard = True)
    scene expression 'locations/bg/ClothesStore/night.png'

    show expression 'cg/ep4/ClothesShop/gg_divan_1.png'
    show Milf Dress_Pose_1
    show Milf Dress_Pose_1:
        xzoom -1
        xalign 1.6
        ypos 1085

    with Dissolve(.5)

    "[gg]" "Как же она прекрасна. "

    "[gg]" "Странно, что это великолепие я стал замечать только сейчас, когда моя жизнь на волоске от смерти."

    "[gg]" "Наверное, во время опасности, человеческие чувства настолько обостряются, что мы лучше понимаем, с кем нам комфортно находиться в трудную минуту."

    "[gg]" "Как говорится, и в радости, и в печали…"


    show Milf Dress_Pose_2:
        xzoom 1
        linear .75 xalign .85
        ypos 1085

    $ renpy.pause(.75, hard = True)
    scene expression 'locations/bg/ClothesStore/night.png'

    show expression 'cg/ep4/ClothesShop/gg_divan_2.png'
    show Milf Dress_Pose_2
    show Milf Dress_Pose_2:
        xzoom 1
        xalign .85
        ypos 1085

    with Dissolve(.5)

    "[gg]" "У меня нет слов! "

    "Марина" "Но ты уж постарайся. Женщины любят ушами. "






    menu:
        "1. Ты выглядишь крайне обольстительно." if True:
            $ pass
        "2. Тебе идёт, хе-хе-хе!" if True:

            $ pass
        "3. Давай ещё!" if True:

            $ pass















    "Марина" "Хи-хи-хи! Какой ты хорошенький."

    "Марина" "Скоро вернусь."

    show Milf Dress_Pose_2:
        xzoom -1
        linear .75 xalign 1.6
        ypos 1085


    $ renpy.pause(.75, hard = True)
    scene expression 'locations/bg/ClothesStore/night.png'

    show expression 'cg/ep4/ClothesShop/gg_divan_1.png'


    show Milf Dress_Pose_2
    show Milf Dress_Pose_2:
        xzoom -1
        xalign 1.6
        ypos 1085

    with Dissolve(.5)

    "[gg]" "Кофейку бы…"



    show Milf Dress_Pose_3:
        xzoom 1
        linear .75 xalign .85
        ypos 1085


    $ renpy.pause(.75, hard = True)

    scene expression 'locations/bg/ClothesStore/night.png'

    show expression 'cg/ep4/ClothesShop/gg_divan_2.png'
    show Milf Dress_Pose_3
    show Milf Dress_Pose_3:
        xzoom 1
        xalign .85
        ypos 1085

    with Dissolve(.5)
    "[gg]" "…."

    "Марина" "Ну, и чего ты замолчал?"













    menu:
        "1. Я хочу тебя." if True:
            $ pass
        "2. Поражён твоей красотой." if True:

            $ pass
        "3. Горло пересохло." if True:

            $ pass

    "Марина" "Тогда найди мою коморочку, [gg] и тогда, возможно, тебе станет чуточку легче. "
    if preferences.language in (None, 'eng', 'spn', 'rus'):
        $ descript = "Найти раздевалку Марины"
    show Milf Dress_Pose_3:
        xzoom -1
        linear .75 xalign 1.6
        ypos 1085


    $ renpy.pause(.75, hard = True)

    scene expression 'locations/bg/ClothesStore/night.png'


    with Dissolve(.5)
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    call screen ep4_milf_42_locker_screen

    $ ep4_milf_42_tmp = []

    $ ep4_milf_42_tmp_dir = {}


label ep4_milf_42_2:

    scene expression '#000' with Dissolve(.5)

    $ renpy.pause(.5, hard = True)


    scene expression 'locations/bg/ClothesStoreLocker/night.png'

    with Dissolve(.5)


    call screen ep4_milf_42_screen

    jump ep4_milf_42_2



label ep4_milf_42_ClothesShopDoor_0:
    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    scene expression 'cg/ep4/ClothesShop/0.png'
    show expression 'cg/ep4/ClothesShop/FrontGround.png'
    with Dissolve(.5)

    $ renpy.pause(.1, hard = True)


    "[gg]" "Господи Иисусе, будь осторожен с этой прекрасной женщиной. "



    jump ep4_milf_42_2

label ep4_milf_42_ClothesShopDoor_1:
    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.5, hard = True)

    scene expression 'cg/ep4/ClothesShop/1.png'
    show expression 'cg/ep4/ClothesShop/FrontGround.png'
    with Dissolve(.5)

    $ renpy.pause(.1, hard = True)


    "[gg]" "Современные нравы, блядь…"



    jump ep4_milf_42_2

label ep4_milf_42_ClothesShopDoor_2:
    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.5, hard = True)

    scene expression 'cg/ep4/ClothesShop/2.png'
    show expression 'cg/ep4/ClothesShop/FrontGround.png'
    with Dissolve(.5)

    $ renpy.pause(.1, hard = True)


    "[gg]" "Интересно, инста-самки размножаются почкованием? "



    jump ep4_milf_42_2

label ep4_milf_42_ClothesShopDoor_3:
    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.5, hard = True)

    scene expression 'cg/ep4/ClothesShop/3.png'
    show expression 'cg/ep4/ClothesShop/FrontGround.png'
    with Dissolve(.5)

    $ renpy.pause(.1, hard = True)


    "[gg]" "Пусто..."


    jump ep4_milf_42_2

label ep4_milf_42_ClothesShopDoor_4:
    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.5, hard = True)

    scene expression 'cg/ep4/ClothesShop/4.png'
    show expression 'cg/ep4/ClothesShop/FrontGround.png'
    with Dissolve(.5)

    $ renpy.pause(.1, hard = True)



    jump ep4_milf_43
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
