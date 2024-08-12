screen empty_screen

label watch_porn_ep2:


    scene expression '#000' with Dissolve(.5)
    $ Show('fake_pc_interface_ep2', transition = Dissolve(.5))()
    call screen empty_screen
label watch_porn_ep2_2:
    $ Hide('porn_site', transition = Dissolve(.5))()
    $ Hide('pc_interface', transition = Dissolve(.5))()
    $ Hide('fake_pc_interface_ep2', transition = Dissolve(.5))()
    $ Hide('empty_screen', transition = Dissolve(.5))()
    $ Hide('main_interface', transition = Dissolve(.5))()
    play music 'audio/porn.mp3'
    scene expression 'cg/ep2/porn_site.png'
    '[gg]' "О да, шикарно!"

    scene fap_time_anim with Dissolve(.5)
    '[gg]' "Давай, детка. Покажи мне самые лучшие виды."
    '[gg]' "Нет, всё не то. Не так."
    scene expression 'images/cg/ep2/fap_time_ep2/fap_time_1.png' with Dissolve(.5)



    '[gg]' "Вот, эта порнушка поинтереснее…"

    scene fap_time_anim with Dissolve(.5)
    show Milf Night_Passion
    show Milf Night_Passion:
        xpos -500
        ypos 1085
        xzoom -1
        easein .5 xpos 500

    $ renpy.pause(.5, hard = True)

    '[gg]' "Да, делай это красиво."
    '[gg]' "Ну вот, опять одно и тоже…"


    hide Milf Night_Passion
    show fap_time_milf_anim
    with Dissolve(.5)
    '[gg]' "Это, кажись, получше будет."
    '[gg]' "Главное, представить на её месте Марину."
    '[gg]' "Аххх… Да, теперь хорошо."
    '[gg]' "Давай, Мариночка, позволь мне трахнуть тебя как следует. "
    'Марина' "Я знала, что он не сможет сегодня уснуть."
    'Марина' "Всякий раз, когда он смотрит на меня, он словно пожирает моё тело."
    'Марина' "И мне стыдно признаться, но мне начинает нравиться это."

    scene expression 'images/cg/ep2/fap_time_ep2/fap_time_3.png'
    show expression 'images/cg/ep2/fap_time_ep2/fap_time_milf_3.png'
    with Dissolve(.5)


    '[gg]' "Уххххххххххх…."
    '[gg]' "Даааааааааааааа!"
    if not renpy.music.get_playing() or 'night' not in renpy.music.get_playing():
        $ renpy.music.stop(fadeout=1.5)
        $ renpy.music.play('audio/night.mp3', fadein = 1.5)
    scene expression '#000' with Dissolve(1.5)
    $ location_now  = 'GG_Room'
    $ time.time_now = 'night'
    call show_all_images_label from _call_show_all_images_label_2
    show GG Think
    show GG Think:
        xalign .5
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(1.5)
    '[gg]' "Проклятье, я даже подрочить на порно не могу, не думая о Марине. "
    '[gg]' "Я начинаю сходить с ума…"
    '[gg]' "Мне уже мало просто смотреть. "
    '[gg]' "Я хочу её. "
    '[gg]' "Хочу её всеми фибрами кожи."

    $ add_to_gallery(4)
    if not from_gallery_check():
        $ Event('ep2_16_sms', 'GG_Room', day_start = time.day_now + 2)

        $ watch_porn_ep2 = False
        $ descript = _('Дождаться сообщения от Игоря.')

    jump main_interface_label
label go_out_from_fake_pc_interface_ep2:
    
    $ location_now = 'GG_Room'
    $ Hide('pc_interface')() 
    $ Hide('fake_pc_interface_ep2')()
    scene expression '#000' with Dissolve(.5)
    jump main_interface_label

screen fake_pc_interface_ep2():
    imagebutton:
        idle '#0000'
        hover '#0000'
        action NullAction()
    add 'pc_bg'
    imagebutton xalign .93 ypos 130:
        idle 'pc_exit'
        hover 'pc_exit'
        xanchor .5
        yanchor .5
        at PulseButtonXzoom09
        action Jump('go_out_from_fake_pc_interface_ep2')

    imagebutton xpos 150 ypos 150:
        idle 'pc_cards_icon'
        hover 'pc_cards_icon'
        xanchor .5
        yanchor .5
        at PulseButtonXzoom
        if money >= 300:
            action Jump('enough_money_game')
        elif time.time_now == 'night':
            action Jump('bored_now_game')
        else:
            action Show('pc_game_interface', transition = Dissolve(.5))

    text _('Казино') outlines [(2, "#2b4b77", 0, 0)] size 25 xpos 100 ypos 200
    text _('Магазин') outlines [(2, "#2b4b77", 0, 0)] size 25 xpos 100 ypos 350
    #text _('Вебка') outlines [(2, "#213c0f", 0, 0)] size 25 xpos 120 ypos 500
    text _('Порно') outlines [(2, "#213c0f", 0, 0)] size 25 xpos 120 ypos 500
    imagebutton xpos 150 ypos 300:
        idle 'pc_bag_icon'
        hover 'pc_bag_icon'
        xanchor .5
        yanchor .5
        at PulseButtonXzoom
        action Jump('online_shop_label')

    # imagebutton xpos 150 ypos 450:
    #     idle 'pc_cam_icon'
    #     hover 'pc_cam_icon'
    #     xanchor .5
    #     yanchor .5
    #     at PulseButtonXzoom
    #     action Jump('wip_game')

    imagebutton xpos 152 ypos 450: #xpos 152 ypos 600:
        idle 'pc_porn_icon'
        hover 'pc_porn_icon'
        xanchor .5
        yanchor .5
        at PulseButtonXzoom
        action Jump('pc_porn')

screen porn_site:
    imagebutton:
        idle '#0000'
        hover '#0000'

        action NullAction()
    add 'cg/ep2/porn_site.png'
    imagebutton:
        idle '#0000'
        hover '#fffa'
        xmaximum 1275
        ymaximum 680
        ypos 200
        xpos 170
        action Jump('watch_porn_ep2_2')

label pc_porn:
    $ watch_porn_ep2 = False

    $ Show('porn_site', transition = Dissolve(.5))()
    call screen empty_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
