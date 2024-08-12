



label ep2_7_need_wash_pants:

    $ Event('ep2_7_need_wash_pants_k', 'Kitchen', 'ep2_7_need_wash_pants')
    $ Event('ep2_7_need_wash_pants_h', 'Hall', 'ep2_7_need_wash_pants')
    $ Event('ep2_7_need_wash_pants_ch', 'City_Home' 'ep2_7_need_wash_pants')
    $ Event('ep2_7_need_wash_pants_s_r', 'Sister_Room', 'ep2_7_need_wash_pants')
    $ Event('ep2_7_need_wash_pants_g_r', 'GG_Room', 'ep2_7_need_wash_pants')

    '[gg]' "Сперва мне нужно положить штаны в стирку."

    $ location_now = 'Corridor'

    jump main_interface_label


label ep2_7_wash_pants:

    call show_all_images_label from _call_show_all_images_label_64
    window hide

    show expression 'cg/gg_activities/gg_clothes_restroom_nude.png'
    $ renpy.pause(9999)
    hide expression 'cg/gg_activities/gg_clothes_restroom_nude.png'
    show GG Nude_Normal
    show GG Nude_Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    '[gg]' "Раз уж я решил постирать штаны, заодно и трусы кину в стирку."



    show Milf Smile
    show Milf Smile at go_from_right

    'Марина' "[gg], я хотела спросить…"

    show GG Nude_OMG:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    show Milf dick_look_2:
        xalign .85
    with my_dissolve

    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/aerosol-of-my-love-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    '[gg]' "Какого чёрта, Марина?! Ты разве не знаешь, что надо стучать?!"
    $ renpy.pause(999999)
    show Milf Embarrassment
    with my_dissolve
    'Марина' "Какая же я растяпа, [gg]!.."
    'Марина' "Я просто хотела… хотела…"
    show Milf dick_look_1 with Dissolve(.5)
    'Марина' "Бог ты мой! Какой же у него огромный, жилистый член."
    $ renpy.pause(999999)
    'Марина' "И такой напряжённый… "
    'Марина' "Ему давно пора обзавестись девушкой."
    show GG Nude_Angry
    '[gg]' "Марина, ты уходить вообще собираешься?!"
    show Milf dick_look_2
    'Марина' "Ой, да, прости-прости. Конечно, я уже ухожу."
    show Milf dick_look_3
    'Марина' "Какой позор, я задумалась о члене брата своего мужа."
    show Milf Smile:
        xzoom -1
        linear .5 xalign 1.5
    $ renpy.pause(1, hard = True)
    show GG:
        linear .5 xalign .5
    $ renpy.pause(.5, hard = True)
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/day.mp3', fadein = 1.5)
    show GG Nude_OMG
    '[gg]' "Что всё это значит? "
    '[gg]' "У Марины чуть слюнки не потекли, пока она пялилась на меня. "
    '[gg]' "Сначала я решил, что это моё больное воображение, но теперь знаю наверняка – она определённо видит во мне мужчину."
    '[gg]' "Но что на счёт меня? Вижу ли я в ней женщину?"
    '[gg]' "Нет. Я не имею право такое говорить. Даже думать о таком! "
    '[gg]' "Ладно, думать я ещё могу. Как бы то ни было – мои мысли при мне, и навредить никому не могут. Мне стоит помнить, она – жена моего брата."
    '[gg]' "Смотри, но не трогай."
    scene expression '#000' with Dissolve(.5)
    $ Event('ep2_8_sms', 'GG_Room', time = ['morning'])
    $ Event('ep2_8_corridor', 'Corridor')
    $ location_now  = 'GG_Room'
    $ time.time_now = 'night'


    $ locations['Restroom'].buttons[0]['washer'] = ((0, 650, 453, 429), [Jump('restroom_washer_label')])
    if "ep2_7_need_wash_pants_k" in allowed_events:
        $ allowed_events.remove("ep2_7_need_wash_pants_k")
    
    if "ep2_7_need_wash_pants_h" in allowed_events:
        $ allowed_events.remove("ep2_7_need_wash_pants_h")
    
    if "ep2_7_need_wash_pants_ch" in allowed_events:
        $ allowed_events.remove("ep2_7_need_wash_pants_ch")
    
    if "ep2_7_need_wash_pants_s_r" in allowed_events:
        $ allowed_events.remove("ep2_7_need_wash_pants_s_r")
    
    if "ep2_7_need_wash_pants_g_r" in allowed_events:
        $ allowed_events.remove("ep2_7_need_wash_pants_g_r")
    $ allowed_events.append('ep2_8_corridor')
    $ allowed_events.append('ep2_8_sms')
    $ events.pop('ep2_7_need_wash_pants_k',  0)
    $ events.pop('ep2_7_need_wash_pants_h',   0)
    $ events.pop('ep2_7_need_wash_pants_ch',  0)
    $ events.pop('ep2_7_need_wash_pants_s_r', 0)
    $ events.pop('ep2_7_need_wash_pants_g_r', 0)
    $ block_exit_home   = False
    $ block_sister_home = False


    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/night.mp3', fadein = 1.5)
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
