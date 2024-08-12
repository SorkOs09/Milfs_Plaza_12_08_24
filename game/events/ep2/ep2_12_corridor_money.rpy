label ep2_12_corridor:
    
    if 'ep2_12_corridor' in allowed_events:
        $ allowed_events.remove('ep2_12_corridor')
    



    if 'ep2_12_milf' in allowed_events:
        $ allowed_events.remove('ep2_12_milf')
    


    

    $ events.pop('ep2_12_corridor', 0)

    call show_all_images_label from _call_show_all_images_label_68

    show Christie Normal
    show Christie Normal:
        xalign -.7
        xzoom -1

        ypos 1085
        zoom 1.0-0.035

    show Milf Chagrin
    show Milf Chagrin:
        xalign 1.5
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)

    $ renpy.pause(.1, hard = True)
    show Christie Normal
    show Christie Normal:
        linear 1 xalign .32
        xzoom -1

        ypos 1085
        zoom 1.0-0.035
    show Milf Chagrin
    show Milf Chagrin:
        linear 1 xalign .85
        ypos 1085
        zoom 1.0-0.035
    $ renpy.pause(1, hard = True)
    show Christie Normal
    show Christie Normal:
        xalign .32
        xzoom -1

        ypos 1085
        zoom 1.0-0.035
    show Milf Chagrin
    show Milf Chagrin:
        xalign .85
        ypos 1085
        zoom 1.0-0.035







    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)



    show Milf Chagrin
    "Марина" "Извини, что недавно накричала на тебя, Кристи."
    show Milf Chagrin
    "Марина" "Я была не права."
    show Christie Smile
    "Кристи" "Я знаю, мамочка. Ты не со зла. "
    show Christie Chagrin
    "Кристи" "И ты меня извини. Я эгоистка."
    show Christie Chagrin
    "Кристи" "Потратила деньги, что ты дала на продукты. "
    show Christie Chagrin
    "Кристи" "Это мерзкий поступок."
    show Milf Smile
    "Марина" "Я рада, что мы обсудили это."
    show Milf Smile
    "Марина" "У меня словно камень упал с плеч. "
    show Christie Smile
    "Кристи" "Да, я тоже чувствовала груз ответственности за свой поступок."
    show Christie Smile
    "Кристи" "Я люблю тебя, мамочка."
    show Milf Smile
    "Марина" "И я тебя, Кристи."
    $ milf_position['morning'] = ['Kitchen',   'milf_kitchen']
    $ milf_position['afternoon'] = ['Kitchen',   'milf_kitchen']

    
    show Christie Normal
    show Christie Normal:
        xzoom 1
        linear 1.5 xalign -.7

        ypos 1085
        zoom 1.0-0.035
    show Milf Chagrin
    show Milf Normal:
        xzoom -1
        linear 1.5 xalign 1.5
        ypos 1085
        zoom 1.0-0.035
    $ renpy.pause(2, hard = True)
    jump main_interface_label








transform my_tmp_transform:
    xzoom .01
    linear 5 xzoom 1
transform my_tmp_transform_2:
    xzoom .01
    linear 10 xzoom 1

image look_milf_pancu_anim:
    'images/cg/ep2/look_milf_pancu/look_milf_pancu_1.png' with Dissolve(.5)
    1
    'images/cg/ep2/look_milf_pancu/look_milf_pancu_2.png' with Dissolve(.5)
    1
    repeat

label ep2_12_milf:
    if 'ep2_12_milf' in allowed_events:
        $ allowed_events.remove('ep2_12_milf')

    $ events.pop('ep2_12_milf', 0)

    call show_bg_image_label from _call_show_bg_image_label_55
    call show_additional_images_label from _call_show_additional_images_label_49

    show Milf Normal
    show Milf Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left
    $ from_say_screen = False
    $ renpy.pause(1)
    'Марина' "Привет, мой хороший. Снова бездельничаешь? "

    show GG Laughs
    '[gg]' "И это тоже."

    show GG Normal:
        xalign .15
    with my_dissolve
    '[gg]' "Марина, не могла бы ты помочь мне с переводом денег? Я дам тебе 150 долларов, а ты перекинешь эту сумму на карту Игоря. "

    show Milf Smile
    'Марина' "Без проблем. Давай 150 долларов."

    show GG Smile
    '[gg]' "Я думала ты доверяешь мне."

    show Milf Smile
    'Марина' "Деньги на стол, хитрец."

    menu:
        "!1. «Вот, держи.» (150 долларов)" if money < 150:
            $ pass
        "1. «Вот, держи.» (150 долларов)" if money >= 150:
            $ pass
        "2. «Позже принесу.»" if True:
            $ Event('ep2_12_milf', 'Kitchen_Milf')
            show Milf Normal
            'Марина' "Вот как принесёшь, тогда и возвращайся. "

            jump main_interface_label
    $ money -= 150
    $ show_text_animation('-150 money')
    show Milf Normal
    'Марина' "Я сейчас немного занята на кухне, но если ты принесёшь мой телефон из спальни, я помогу тебе."

    show GG Think
    '[gg]' "Разве твоя спальня не закрыта?"

    show Milf Embarrassment
    'Марина' "Нет, я… Я забыла её закрыть."


    show GG Normal
    '[gg]' "Хорошо, я мигом!"



    $ locations['Milf_Room'].image_buttons = {
        'phone_underpants_table' : Jump('ep2_12_milf_underpants'),

        }

    $ block_exit_home_tmp_tmp            = copy.deepcopy(block_exit_home)
    $ block_time_forward_tmp_tmp         = copy.deepcopy(block_time_forward)
    
    $ block_exit_home            = True
    $ block_time_forward         = True

    if not hasattr(store, 'allowed_events'):

        $ allowed_events = []
    $ descript = _('Сходить в спальню Марины за её телефоном.')
    $ allowed_events.append('ep2_12_end')

    




    jump main_interface_label

label ep2_12_milf_underpants:
    if not from_gallery_check():
        $ locations['Milf_Room'].image_buttons.pop('phone_underpants_table', 0)

        $ milf_position[time.time_now][0] = 'Kitchen'
    show GG Invis
    show GG Invis:
        xalign .5
    show expression 'cg/ep2/tumba_phone_cg.png':
        xalign .5

    with my_dissolve

    '[gg]' "Ага, вот её телефон…"
    '[gg]' "И трусики."
    #call show_all_images_label from _call_show_all_images_label_69
    #show GG Normal
    hide expression 'cg/ep2/tumba_phone_cg.png'
    show GG Pancu_1
    with my_dissolve


    play music 'audio/trusi.mp3' fadein 1.5
    '[gg]' "Интересно, это те же трусики, что я тогда видел на кухне?"
    '[gg]' "Она что, забыла их надеть?"
    '[gg]' "Вряд ли, конечно… Но от мысли, что она сейчас на кухне без нижнего белья, я начинаю заводиться."
    '[gg]' "Ничего же не станется, если я немного понюхаю их? "


    
    show GG Pancu_3
    with my_dissolve
    '[gg]' "Мммммммммммм!"
    '[gg]' "О дааааааааааааа!"







    show expression 'cg/ep2/milf_pancu_1_cg.png':
        xalign .1
    with my_dissolve

    '[gg]' "Она явно намокала в этих трусиках…"
    '[gg]' "Я чувствую её сладкие соки. "
    '[gg]' "Чувствую, как моё обоняние поглощает остатки её сексуальной неудовлетворённости. "
    '[gg]' "Её мокрая, возбуждённая прелесть манит меня."







    show expression 'cg/ep2/milf_pancu_2_cg.png':
        xalign .9
    with my_dissolve
    '[gg]' "Этот ароматный запах киски такой пронизывающий, словно она играла сама с собой буквально минуту назад."
    '[gg]' "Как же приятно она пахнет…"
    '[gg]' "А всё потому, что у неё давно уже не было секса. "
    '[gg]' "Да, её пальчики уже не справляются. Ей нужен кто-то, кто попробует на вкус её дрожащий от нетерпения клитор. "
    show expression AlphaMask(Transform(Crop((0, 0, 960, 1080),'cg/ep2/milf_pancu_3_cg.png'), xzoom = -1), At('tests/anim_par/image_par_mask_2.png', my_tmp_transform_2)):
        xpos 0
        xzoom -1
    show expression AlphaMask(Crop((960, 0, 960+960, 1080),'cg/ep2/milf_pancu_3_cg.png'), At('tests/anim_par/image_par_mask_2.png', my_tmp_transform_2)):
        xpos 0+960





    '[gg]' " Потрясающая киска жены моего брата заполонила моё сознание. "
    '[gg]' "Теперь я готов на всё, лишь бы попробовать её взаправду. "
    '[gg]' "Хотя бы разочек… "

    scene look_milf_pancu_anim
    show Milf Invis:
        xalign .7 
    with Dissolve(.3)
    'Марина' "Чёрт, он всё-таки заинтересовался ими…"
    'Марина' "Когда я оставляла их на видное место, я до последнего надеялась, что он проигнорирует их. Но нет."
    'Марина' "Значит, [gg] всё-таки испытывает ко мне сексуальное влечение."
    'Марина' "И я понятия не имею, что мне теперь делать…"
    if not renpy.music.get_playing() or 'day' not in renpy.music.get_playing():
        $ renpy.music.stop(fadeout=1.5)
        $ renpy.music.play('audio/day.mp3', fadein = 1.5)




    call show_all_images_label from _call_show_all_images_label_71
    show GG Normal
    show GG Pancu_4:
        xalign .5
    with Dissolve(.5)
    $ add_to_gallery(2)
    '[gg]' "Даааа, это настоящее блаженство."
    '[gg]' "Надо быстро положить их на место и бежать на кухню. Марина уже заждалась меня."
    if from_gallery_check():
        call check_gallery_label from _call_check_gallery_label_7
    play sound 'audio/get_item.ogg'

    show screen give_item_screen(i_path+'/items/phone.png', _('Телефон'),  _('Обыкновенный смартфон.'))


    with Dissolve(.5)
    $ renpy.pause(999999)
    $ add_to_inventory(name = 'Телефон')
    $ Event('ep2_12_end', 'Milf')
    hide GG
    hide screen give_item_screen
    with Dissolve(.5)
    $ descript = _('Принести Марине её телефон.')



    jump main_interface_label
















label ep2_12_end:
    $ events.pop('ep2_12_end', 0)



    call show_bg_image_label from _call_show_bg_image_label_56
    call show_additional_images_label from _call_show_additional_images_label_50
    $ remove_from_inventory('Телефон')

    show Milf Normal
    show Milf Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    show GG GivePhone
    show GG GivePhone at go_from_left
    $ renpy.pause(1)
    '[gg]' "Вот твой телефон, Марина."

    show GG Normal

    show Milf Mobile_1
    with my_dissolve

    'Марина' "Спасибо, [gg]. Сейчас переводу деньги твоему другу."
    'Марина' "Номер его карты прежний?"

    show GG Normal
    '[gg]' "Ага."

    show Milf Mobile_1
    'Марина' "Ну вот и всё, готово. "

    show GG Normal
    'Марина' "Большое спасибо, ты очень выручила меня."

    show Milf Smile with Dissolve(.5)
    'Марина' "Всегда пожалуйста."

    play sound 'audio/sms.ogg'
    '[gg]' "Я должен проверить СМС от друга."

    $ sms_now = SmsBlock('Игорь', 'igor', "6", Jump('ep2_13_after_sms'))
    $ sms_now.add_sms(_('TT: Ку.'))

    $ sms_now.add_sms(_('GG: Ку.'))

    $ sms_now.add_sms(_('TT: Деньги получил. Через пару дней отпишусь.'))

    $ sms_now.add_sms(_('GG: Окей.'))

    $ sms_now.add_sms(_('TT: бб'))
    
    $ phone_warning = True
    $ descript      = _('Прочесть СМС от Игоря.')

    $ block_change_milf_position = False

    $ block_exit_home    = copy.deepcopy(block_exit_home_tmp_tmp)
    $ block_time_forward = copy.deepcopy(block_time_forward_tmp_tmp)
    
    $ del block_exit_home_tmp_tmp
    $ del block_time_forward_tmp_tmp

    if 'ep2_12_end' in allowed_events: 

        $ allowed_events.remove('ep2_12_end')


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
