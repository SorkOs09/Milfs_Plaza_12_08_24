label ep3_milf_27:
    $ events.pop('ep3_milf_27', 0)


    play sound 'audio/zvonok.mp3'


    hide screen main_interface


    $ block_time_forward = True
    $ block_exit_home    = False
    $ Event('ep3_milf_27_2',     'City_Home',   'ep3_milf_27_2')
    jump main_interface_label





label ep3_milf_27_2:
    $ location_now  = 'Corridor'
    $ time.time_now = 'evening'

    hide screen main_interface
    $ milf_15_audio = True


    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    $ events.pop('ep3_milf_27_2', 0)



    $ block_time_forward = True
    $ block_exit_home    = True

    call show_all_images_label from _call_show_all_images_label_32

    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085



    show Igor Spec_Normal_2
    show Igor Spec_Normal_2:
        ypos 1085

        xalign .95


    with Dissolve(.5)






















    show GG Surprise
    "[gg]" "Что это? "
    "Игорь" "Маскировочный костюм. "


    "Игорь" "На случай, если что-то пойдёт не по плану."
    show GG Smile
    "[gg]" "Ты бы ещё пистолет взял, чтобы отстреливаться. "
    "Игорь" "А я взял."
    show GG Normal
    "[gg]" "Поехавший!"
    "Игорь" "Сам такой."
    "[gg]" "Комната Марины в твоём полном распоряжении. У тебя, как ты и просил, минимум полтора часа. От меня что-то требуется?"

    "Игорь" "Не мешать. "
    "[gg]" "Понял-принял! "
    "[gg]" "Постарайся как можно скорее. "
    "Игорь" "Если такой умный. Иди сам взламывай сейф."








    show Igor Spec_Normal_1:
        xzoom -1
        linear .7 xalign 1.8

    $ renpy.pause(.7, hard = True)
    hide Igor
    show GG Laughs
    with my_dissolve
    "[gg]" "Исчезаю! "
    $ descript = _("Вернуться в свою комнату, дождавшись, пока Игорь взломает сейф.")

    $ block_time_forward = True

    $ Event('ep3_milf_28',     'Milf_Room')

    $ Event('ep3_milf_28_2',    'GG_Room')



    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
