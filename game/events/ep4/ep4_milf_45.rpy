

screen ep4_milf_45_screen:
    imagebutton:
        idle "cg/ep4/CostumeOnBedEp4.png"
        hover im.MatrixColor("cg/ep4/CostumeOnBedEp4.png", im.matrix.brightness(.3))
        focus_mask True

        action Return()




image ep4_milf_45_m5:
    'cg/ep4/MilfDressing/m5.png' with Dissolve(.25)
    1
    'cg/ep4/MilfDressing/m6.png' with Dissolve(.25)
    1
    repeat




label ep4_milf_45:

    $ events.pop('ep4_milf_45', 0)

















    $ Hide('main_interface')()

    scene black with Dissolve(.75)

    $ renpy.pause(.75, hard = True)
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    scene expression 'cg/ep4/MilfDressing/m1.png'

    with Dissolve(.5)
    "[gg]" "Прятать такое тело под одеждой – преступление против человечества. "




    scene expression 'cg/ep4/MilfDressing/m2.png'
    with vpunch

    "Марина" "Подглядывать некрасиво. "

    scene expression 'cg/ep4/MilfDressing/m3.png'
    with Dissolve(.5)

    "[gg]" "Извини…"



    scene expression 'cg/ep4/MilfDressing/m4.png'
    with Dissolve(.5)

    "Марина" "Оу… Это мне?"


    "[gg]" "Нравится?"


    "Марина" "Очень."


    "[gg]" "Значит, я сделал всё правильно. "


    "Марина" "Ты умеешь удивлять, [gg]."
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)




    scene expression 'cg/ep4/MilfDressing/Background.png'
    show expression 'cg/ep4/MilfDressing/m5.png'
    with Dissolve(.5)
    "[gg]" "Значит, для тебя и этого стало неожиданностью, хе-хе?"
    "Марина" "Охххх!!..."
    "Марина" "Прекрати, пожалуйста. А иначе…"

    scene expression 'cg/ep4/MilfDressing/Background.png'

    show ep4_milf_45_m5

    with Dissolve(.5)
    "[gg]" "А иначе что?"
    "Марина" "Я сорву с тебя одежды, повалю на кровать и…"
    '[gg]' "И?..."
    "Марина" "И мы останемся дома. "
    "Марина" "Весь день и всю ночь…."
    "[gg]" "Теперь я точно не смогу отлипнуть."
    "Марина" "Ну всё. Хватит. "
    "Марина" "Мы обязательно продолжим, всему своё время."

    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    $ add_to_gallery(13)
    if from_gallery_check():
        call check_gallery_label from _call_check_gallery_label_1

    call show_bg_image_label from _call_show_bg_image_label_47

    call show_additional_images_label from _call_show_additional_images_label_41

    with Dissolve(.5)



    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085



    show Milf Dress
    show Milf Dress_Smile:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "[gg]" "Ты выглядишь просто ослепительно."
    show Milf Dress_Embarrassment
    "Марина" "Только благодаря тебе. "
    show GG Passion
    "[gg]" "Поверь, платье здесь не при чём."
    show Milf Dress_Smile
    "Марина" "И я не про платье. Именно ты делаешь меня красивой и желанной женщиной. "
    show GG Embarrassment
    "[gg]" "Ну… просто я люблю тебя."
    show Milf Dress_Passion
    "Марина" "Эй… побереги комплименты. Вечер только начался. А ты уже рискуешь не дойти до ресторана."
    show GG Laughs
    "[gg]" "Хе-хе-хе. Провокация."
    show Milf Dress_Normal
    "Марина" "Раз уж ты так сильно меня любишь, тогда будь добр одеть костюм. "
    show GG Surprise
    "[gg]" "Ой…"

    "Марина" "Не бойся. Я уже купила тебе его. Вот он, лежит на кровати."
    hide Milf
    call show_bg_image_label from _call_show_bg_image_label_48

    call show_additional_images_label from _call_show_additional_images_label_42

    show expression 'cg/ep4/CostumeOnBedEp4.png'

    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085


    show Milf Dress_Smile
    show Milf Dress_Smile:
        xalign .85
        ypos 1085


    with Dissolve(.5)

    show GG Normal
    show GG Normal:
        linear .5 xalign 0.0
        ypos 1085



    show Milf Dress
    show Milf Dress_Smile:
        linear .5 xalign 1.0
        ypos 1085


    $ renpy.pause(.5)


    $ descript = _('Взять костюм с кровати.')
    call show_bg_image_label from _call_show_bg_image_label_49
    call show_additional_images_label from _call_show_additional_images_label_43
    show expression 'cg/ep4/CostumeOnBedEp4.png'

    show GG Normal
    show GG Normal:
        xalign 0
        ypos 1085



    show Milf Dress
    show Milf Dress_Smile:
        xalign 1.0
        ypos 1085



    call screen ep4_milf_45_screen
    call show_bg_image_label from _call_show_bg_image_label_50
    call show_additional_images_label from _call_show_additional_images_label_44
    with Dissolve(.5)


    jump ep4_milf_46
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
