label ep4_milf_47_mom_menu:
    show Milf Dress_Smile

    "Официант" "Вы так миленько смотритесь, словно мама и сын на свидании. Я просто не имею права вам отказать. "

    menu:
        "Спасибо, вы тоже очень любезны." if True:

            show Milf Dress_Embarrassment


            "Официант" "Очень рада вам угодить. "
        "Ну, вообще-то это и есть моя мама" if True:

            show Milf Dress_Embarrassment


            "Официант" "Оуу…"
        "Такое сравнение мне кажется оскорбительным." if True:



            show Milf Dress_Chagrin


            "Официант" "Прошу прощения за бестактность."

    "Официант" "Что ж. Я скоро вернусь."

    return
screen ep4_main_city_screen(mpn=True):
    imagebutton:
        idle '#0000'
        hover '#0000'
        action NullAction()
    zorder 900
    if mpn:
        add 'images/interface/city_interface/city_bg_'+time.time_now+'.png'
    add 'gradient_up'
    button:
        add time.time_now+'_button'
        xalign .5
        action NullAction()

    add 'play_icon' xalign .5
    if time.time_now == 'night':
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






screen ep4_milf_47_city_screen():


    use ep4_main_city_screen



    imagebutton:
        idle 'city_restaurant_button'
        hover 'city_restaurant_button'
        at ButtonEffect01
        focus_mask True

        action Return()



label ep4_milf_47:
    $ block_time_forward = True
    scene expression '#000' with Dissolve(.5)




























    call screen ep4_milf_47_city_screen
    $ renpy.music.stop(fadeout=1.5)
    scene expression '#000' with Dissolve(.5)
    $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    scene expression 'cg/ep4/ep4_restaurant_bg_blur.png'
    show RestAdmin Normal
    show RestAdmin Normal:
        xalign .85
        ypos 1085


    with Dissolve(.5)


    show GG Costume_Normal
    show GG Costume_Normal:
        xalign -.75
        ypos 1085




    show Milf Dress_Smile
    show Milf Dress_Smile:
        xzoom -1
        xalign -.75
        ypos 1085


    show GG Costume_Normal
    show GG Costume_Normal:
        linear .75 xalign .25
        ypos 1085




    show Milf Dress_Smile
    show Milf Dress_Smile:
        xzoom -1
        linear .75 xalign .05
        ypos 1085


    $ renpy.pause(.75, hard = True)


    show GG Costume_Normal
    show GG Costume_Normal:
        xalign .25
        ypos 1085




    show Milf Dress_Smile
    show Milf Dress_Smile:
        xzoom -1
        xalign .05
        ypos 1085









    "Официант" "Добро пожаловать. Очень рады вас здесь видеть."

    "[gg]" "Привет."

    "[gg]" "Мы можем пройти?"

    "Официант" "Конечно. Какой столик у вас заказан?"
    show GG Costume_Surprise
    "[gg]" "А у вас надо заказывать? "

    "Официант" "Не обязательно, но сегодня, к сожалению, все места заняты. Вечер Субботы, сами понимаете. "

    show GG Costume_Normal


    "Официант" "Мы могли бы предложить вам зайти чуть позже или прийти в другой раз. "
    show Milf Dress_Chagrin
    "Марина" "…."


    menu:

        "!Может, договоримся? (150$)" if money < 150:
            $ pass
        "!Не морочь мне голову. Быстро освободи нам столик.(500$)" if money < 500:
            $ pass
        "Может, договоримся? (150$)" if money >= 150:


            
            $ add_ach('ACH_23')

                #achievement.grant("ACH_23")
                #achievement.sync()



            $ ep4_milf_47_tmp = 1
            "Официант" "Вообще-то мы никогда так не поступаем. У нас кристально чистая репутация, знаете ли."

            "Официант" "Но…"




            call ep4_milf_47_mom_menu from _call_ep4_milf_47_mom_menu


            $ money = max(0, money-150)
            $ show_text_animation('-150 money')


        "Не морочь мне голову. Быстро освободи нам столик.(500$)" if money >= 500:
            $ ep4_milf_47_tmp = 3
            $ add_ach('ACH_23')
            #python:
            #    achievement.grant("ACH_23")
            #    achievement.sync()


            "Официант" "Да-да. Конечно. Извините, что задерживаем вас."
            call ep4_milf_47_mom_menu from _call_ep4_milf_47_mom_menu_1

            $ money = max(0, money-500)
            $ show_text_animation('-500 money')
        "Что ж… Мы зайдём в другой раз. (альтернативный путь)." if True:
            $ add_ach('ACH_22')

            #python:
                #achievement.grant("ACH_22")
                #achievement.sync()


            $ ep4_milf_47_tmp = 2

            show Milf Dress_Normal
            "Марина" "Полагаю, двухсот долларов лично вам, моя маленькая леди, будет более чем достаточно, чтоб мы могли провести вечер в вашем заведении? "

            "Официант" "Вообще-то мы никогда так не поступаем. У нас кристально чистая репутация, знаете ли."

            "Официант" "Но…"
            call ep4_milf_47_mom_menu from _call_ep4_milf_47_mom_menu_2









    show RestFamily Normal
    show RestFamily Normal:

        xpos 2400
        ypos 1085


    show RestAdmin Normal
    show RestAdmin Normal:
        xzoom -1
        linear 1 xalign 1.5
        ypos 1085


    $ renpy.pause(2, hard = True)

    show RestAdmin Normal
    show RestAdmin Normal:
        xzoom -1
        xpos 2700
        ypos 1085


    show RestFamily Normal:
        xzoom 1
        linear .85 xpos 1250
        ypos 1085


    show RestAdmin Normal:
        xzoom 1
        linear .85 xpos 2300
        ypos 1085


    $ renpy.pause(.85, hard = True)









    "Семья" "Это беспредел! Мы будем жаловаться!"

    "Официант" "Прошу вас, успокойтесь. Мы всё вам компенсируем. "
    show RestFamily Normal:
        xzoom -1
    "Семья" "Позор!"

    show RestFamily Normal:
        xzoom 1
    $ renpy.pause(.2, hard = True)
    show RestFamily Normal:
        xzoom 1
        linear 1 xpos -600
        ypos 1085


    show RestAdmin Normal:
        xzoom 1
        linear 1 xpos 2000
        ypos 1085


    $ renpy.pause(1.5, hard = True)


    "Официант" "Что ж… Как видите, я очень для вас постаралась."

    "[gg]" "Мы это ценим, спасибо."

    show RestAdmin Normal:
        xzoom -1
        linear 1 xpos 2600
        ypos 1085


    $ renpy.pause(.2, hard = True)

    show GG Costume_Normal:
        xzoom 1
        linear 1.5 xalign 1.5
        ypos 1085




    show Milf Dress_Normal:
        xzoom -1
        linear 1.5 xalign 1.5
        ypos 1085


    $ renpy.pause(2, hard = True)

    jump ep4_milf_48
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
