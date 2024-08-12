

label ep5_milf_60:
    $ events.pop('ep5_milf_60', 0)

    # if time.time_now in ['evening', 'night']:

    #     "[gg]" "Нет, сейчас Марина не заметит моих стараний."
    #     "[gg]" "Следует сделать это или утром, или днём."
    #     jump main_interface_label

    $ remove_from_inventory('Растение в горшке')
    #$ locations['Corridor'].buttons[0].pop('ep5_milf_60', 0)

    $ locations['Corridor'].bg = 'Corridor'



    $ Hide('main_interface')()
    $ Hide('tree_screen_ep5')()

    if hasattr(store, 'korridor_without_tree_ep5'):
        $ del korridor_without_tree_ep5
    call show_bg_image_label from _call_show_bg_image_label_31
    call show_additional_images_label from _call_show_additional_images_label_26
    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    show GG Think
    show GG Think:
        xzoom -1
        xalign .89
        ypos 1085


    show Milf Normal
    show Milf Normal:
        xalign -.5
        xzoom -1
        ypos 1085

    with Dissolve(.5)

    "[gg]" "Вот, собственно, и всё."
    show GG Think
    "[gg]" "Марина должна быть довольна."
    show GG Think

    "[gg]" "Я надеюсь…"


    show Milf Normal
    show Milf Normal:
        linear 1 xalign .1
        xzoom -1
        ypos 1085

    show GG Surprise
    $ renpy.pause(1, hard = True)




    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    show Milf Normal
    "Марина" "Прив…"
    show Milf Surprise
    with vpunch
    "Марина" "О Господи, ты воскресил Джими?!!"
    show GG Laughs
    "[gg]" "Хе-хе-хе. К сожалению, нет."
    show Milf Surprise
    "Марина" "Тогда как?! Почему?!.."
    show GG Smile
    "[gg]" "Знакомься, Марина, это мистер [ep5_tree_name]. [ep5_tree_name], это Марина. "

    show Milf Smile
    "Марина" "Он прекрасен!"
    show Milf Smile
    "Марина" "Где ты это откопал?"
    show GG Laughs
    "[gg]" "Э… Лучше об этом не распространяться. "
    show Milf Smile
    "Марина" "Cпасибо, [gg]! Огромное тебе спасибо!"
    show Milf Smile
    "Марина" "Ты потрясающий!"
    show Milf Chagrin
    "Марина" "Мне так стыдно, что я обиделась на тебя…"
    show GG Normal
    "[gg]" "Ты имела на это полное право."
    show Milf Passion
    "Марина" "Теперь я имею право отблагодарить тебя. "
    show GG Smile
    "[gg]" "Если желаешь."
    show Milf Passion
    "Марина" "Ещё как желаю. Жду тебя сегодня ночью у себя."
    $ descript = _("Посетить спальню Марины сегодня ночью.")
    $ Event('ep45_milf_61',     'Hall', time = ['night'])

    $ block_change_milf_position = False
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
