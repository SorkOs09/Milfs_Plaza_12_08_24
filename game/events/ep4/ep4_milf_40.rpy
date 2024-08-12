screen ep4_milf_40_city_screen:

    use ep4_main_city_screen


    imagebutton:

        idle 'city_clothes_shop_button'
        hover 'city_clothes_shop_button'

        at ButtonEffect01

        focus_mask True

        action Return()


label ep4_milf_40:










    menu:
        "Отправиться в магазин (200$)" if money >= 200:
            $ pass
        "!Отправиться в магазин (200$)" if money < 200:
            $ pass
        "Назад" if True:

            $ Event('ep4_milf_40',   'Kitchen_Milf', 'ep4_milf_40', button_name = _('Платье'))
            $ Event('ep4_milf_40_2', 'Hall_Milf',    'ep4_milf_40', button_name = _('Платье'))

            jump main_interface_label


    $ block_change_milf_position = False
    $ events.pop('ep4_milf_40',   0)
    $ events.pop('ep4_milf_40_2', 0)
    call show_bg_image_label from _call_show_bg_image_label_204 
    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085




    show Milf Normal
    if time.time_now in ['evening', 'night']:
        $ tmp_milf = 'Night_'
        show Milf Night_Normal:
            xalign .85
            ypos 1085

    elif True:



        $ tmp_milf = ''

        show Milf Normal:
            xalign .85
            ypos 1085


    with Dissolve(.5)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "[gg]" "Марина, настало время превратить тебя в золушку."

    $ renpy.show('Milf ' + tmp_milf + 'Embarrassment')
    "Марина" "Но я думала, ты больше специализируешься по мачехам. "
    show GG Laughs
    "[gg]" "Подловила."
    show GG Smile
    "[gg]" "Ладно, собираемся и едем в магазин одежды."

    $ renpy.show('Milf ' + tmp_milf + 'Normal')

    "Марина" "Дай мне минутку. "

    if tmp_milf == '':
        show Milf Normal:
            xzoom -1
            linear 1 xalign 1.5
            ypos 1085

    elif True:

        show Milf Night_Normal:
            xzoom -1
            linear 1 xalign 1.5
            ypos 1085


    $ renpy.pause(1, hard = True)
    show Milf Street_Normal:
        xzoom 1
        linear 1 xalign .85
        ypos 1085

    $ renpy.pause(1, hard = True)

    show Milf Street_Normal:
        xzoom 1
        xalign .85
        ypos 1085
    with my_dissolve

    "Марина" "Я готова."
    show GG Normal
    "[gg]" "Тогда в путь!"

    $ descript = _('Отправиться в магазин одежды и купить Марине подходящее платье.')





    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.5, hard = True)

    call screen ep4_milf_40_city_screen

    jump ep4_milf_41
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
