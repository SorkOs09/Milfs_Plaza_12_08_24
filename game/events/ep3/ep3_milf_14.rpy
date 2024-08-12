




image tr_7_animation:

    'cg/ep5/help_2/tr7.png' with Dissolve(.5)
    1
    'cg/ep5/help_2/tr8.png' with Dissolve(.5)
    1

    repeat


image 3_yu_animation:

    'cg/ep5/help_3/3yu.png' with Dissolve(.5)
    1
    'cg/ep5/help_3/2yu.png' with Dissolve(.5)
    1

    repeat


image 3_yu_animation_fast:

    'cg/ep5/help_3/3yu.png' with Dissolve(.4)
    .75
    'cg/ep5/help_3/2yu.png' with Dissolve(.4)
    .75

    repeat



image 3_yu_animation_fastest:

    'cg/ep5/help_3/3yu.png' with Dissolve(.4)
    .5
    'cg/ep5/help_3/2yu.png' with Dissolve(.4)
    .5

    repeat


image Milf_Fap_Water_anim:
    'cg/ep3/Milf_Fap_Water/milf_2.png' with Dissolve(.5)
    1
    'cg/ep3/Milf_Fap_Water/milf_3.png' with Dissolve(.5)
    1
    repeat



image Milf_Fap_Water_anim_gg:
    'cg/ep3/Milf_Fap_Water/gg_1.png' with Dissolve(.25)
    .5
    'cg/ep3/Milf_Fap_Water/gg_2.png' with Dissolve(.25)
    .5
    repeat



image Play_Ass_Face_Anim:
    'cg/ep3/Play_Ass_Face/4.png' with Dissolve(.5)
    1
    'cg/ep3/Play_Ass_Face/5.png' with Dissolve(.5)
    1


    repeat



image Corridor_scene_anim_0:
    'cg/ep3/Corridor_scene/3.png' with Dissolve(.3)
    1
    'cg/ep3/Corridor_scene/4.png' with Dissolve(.3)
    1

    repeat
label ep3_milf_14:

    $ events.pop('ep3_milf_14', 0)

    $ renpy.pause(.5, hard = True)
    $ descript = _('Проверить телефон')


    $ ShowPhone = Show('phone_interface')

    $ sms_now = SmsBlock('Игорь', 'igor', "10",)
    $ sms_now.add_sms(_('TT: Чувак, как прогресс?'))
    $ sms_now.add_sms(_('TT: Чем дольше ты тянешь, тем хуже для нас обоих.\n'))
    $ sms_now.add_sms(_('GG: Всё под контролем. Я узнал дату рождения.'))
    $ sms_now.add_sms(_('GG: Как только Марина и Кристи свалят из дома,\n я перепробую все комбинации.\n'))
    $ sms_now.add_sms(_('TT: Держи меня в курсе, я весь на нервах.'))
    $ sms_now.add_sms(_('GG: Окей.'))

    $ phone_warning  = True
    $ ep3_new_events = True


    $ descript = _('Дождаться, когда никого не будет дома, и перебрать все комбинации. Уверен, через день-два такая возможность появится. ')
    $ milf_shower_ep3 = True
    $ new_events      = True
    $ Event('ep3_milf_15', 'Corridor', day_start = time.day_now + 2,)

    $ check_and_jump('pre_ep3_night_girl')
    $ check_and_jump('ep3_night_girl')
    $ check_and_jump('night_girl')

    jump main_interface_label



















label ep3_milf_14_korridor:
    $ Hide('main_interface', transition = Dissolve(.5))()







    if not hasattr(store, 'help_ep3_milf_14'):
        $ help_ep3_milf_14 = 0
    if mp.help_ep3_milf_14 is None:
        $ mp.help_ep3_milf_14   = 0
        $ mp.save()
    if mp.help_ep3_milf_14 < getattr(store, 'help_ep3_milf_14', 0):
        $ mp.help_ep3_milf_14 = help_ep3_milf_14
        $ mp.save()
    if from_gallery_check():
        $ help_ep3_milf_14 = mp.help_ep3_milf_14

    call show_bg_image_label from _call_show_bg_image_label_20
    with Dissolve(.5)
    menu:
        "Помощь 1 ур" if hasattr(store, 'help_ep3_milf_14'):
            $ pass

            $ show_text_animation(_('+10 milf'))
            $ add_to_gallery(-2)





        "!Помощь 2 ур" if help_ep3_milf_14 < 1:
            $ pass

        "Помощь 2 ур" if help_ep3_milf_14 >= 1:

            $ renpy.music.stop(fadeout=1.5)

            $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)




            $ show_text_animation(_('+10 milf'))




            $ renpy.music.stop(fadeout=1.5)

            $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)



            show GG Normal
            show GG Normal:
                xalign .32
                ypos 1085
                zoom 1.0-0.035
            show Milf Normal
            show Milf Normal:
                xalign .85
                ypos 1085
                zoom 1.0-0.035

            show GG Laughs
            with Dissolve(.5)

            "[gg]" "Работы на высоте сопряжены с большим риском для здоровья, знаешь ли."

            "Марина" "Болтун. Хочешь помочь? "

            "[gg]" "С радостью. "

            "Марина" "Тогда держи меня. Очень и очень крепко."
            scene expression 'cg/ep5/KoridorDay_Blur.png'
            show expression 'cg/ep5/help_2/tr1.png'
            with Dissolve(.5)





            "Марина" "Если долго не поливать растение, оно начнёт стремительно увядать."


            "Марина" "И реанимировать его практически нереально."

            "[gg]" "А ты?"


            "Марина" "Я?"

            "[gg]" "Да, что с тобой случится, если ты перестанешь чувствовать мою… заботу?"


            "Марина" "Огорчусь, наверное."

            "[gg]" "И это всё?"

            "[gg]" "А как на счёт твоего цветка?"


            "Марина" "Не понимаю, о чём ты."
            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_2/tr2.png'

            with Dissolve(.5)





            "[gg]" "Мне кажется, ему тоже не хватает внимания."

            "[gg]" "Моего внимания."


            "Марина" "Прекратить надо мной подшучивать, [gg]."


            "Марина" "С твоей стороны это очень некрасиво."
            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_2/tr3.png'

            with Dissolve(.5)






            "[gg]" "А я и не шучу. "

            "[gg]" "Я хочу позаботиться о твоём «цветочке». "


            "Марина" "Пошляк. Ты же понимаешь, что не стоит так играть со мной?"
            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_2/tr4.png'

            with Dissolve(.5)






            "[gg]" "Именно поэтому я хочу, чтобы всё было по серьёзному. "


            "Марина" "Пожалуйста, не надо. Нас могут заметить."
            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_2/tr5.png'

            with Dissolve(.5)




            "[gg]" "Эта дырочка выглядит такой одинокой."

            "[gg]" "Словно цветок, который давно не поливали. "


            "Марина" "…."

            "[gg]" "Я не могу ей позволить скучать всё это время. "

            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_2/tr6.png'

            with Dissolve(.5)





            "Марина" "Ах…."


            "Марина" "Боже…."

            "[gg]" "Какой приятный вкус зрелой женщины."


            "Марина" "[gg], если ты не прекратишь, я могу упасть."

            "[gg]" "Оказаться на полу под твоей задницей было бы для меня настоящим праздником."


            "Марина" "Охх…."


            "Марина" "Ты пошляк."




            "[gg]" "Дурманящий запах её попки сводит меня с ума."

            "[gg]" "Мой язык готов вылизывать её до тех пор, пока она не завизжит от удовольствия. "


            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_2/tr7.png'

            with Dissolve(.5)


            "Марина" "[gg], миленький, ты…"


            "Марина" "Заставляешь чувствовать себя живой и цветущей. "
            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_2/tr6.png'

            with Dissolve(.5)




            "[gg]" "Обожаю, когда ты делишься со мной своими ощущениями."

            "[gg]" "Когда я такое слышу, то я завожусь ещё больше. "
            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_2/tr5.png'

            with Dissolve(.5)




            "[gg]" "Нравится, как я работаю язычком?"


            "Марина" "Твои вопросы смущают меня…"

            "[gg]" "Ты хочешь, чтобы я проник ещё глубже?"


            "Марина" "Да, пожалуйста."


            "Марина" "Обожаю когда ты лижешь мой анус. "


            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_2/tr6.png'

            with Dissolve(.5)




            "[gg]" "Я знал, что ты нуждаешься в моей заботе."

            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_2/tr7.png'

            with Dissolve(.5)




            "[gg]" "И прекрасно чувствую, когда ты испытываешь надобность в моей помощи. "

            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_2/tr6.png'

            with Dissolve(.5)




            "[gg]" "Она уже вся течёт от удовольствия."

            "[gg]" "И дрожит так, словно я трахаю её членом."



            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_2/tr7.png'

            with Dissolve(.5)

            "Марина" "Я..."

            "[gg]" "Да, чувствую."

            scene expression 'cg/ep5/KoridorDay_Blur.png'


            show tr_7_animation

            with Dissolve(.5)



            "Марина" "Я уже на пределе, миленький…"


            "Марина" "Горю от наслаждения…"


            "Марина" "Ахххх…."


            "Марина" "О даааааа….."


            "Марина" "Кончаааюююю!!!.."


            scene expression '#fff' with Dissolve(1)
            $ renpy.pause(.75, hard = True)
            scene expression 'cg/ep5/KoridorDay_Blur.png'



            show expression 'cg/ep5/help_2/tr9.png'
            with Dissolve(.5)


            "[gg]" "Твой цветок выглядит совершенно сытым."


            "Марина" "Ага. Не забудь меня «кормить» регулярно. "

            scene expression '#000' with Dissolve(.5)
            $ location_now = 'Corridor'
            $ time.time_now = 'evening'

            call show_bg_image_label from _call_show_bg_image_label_21
            call show_additional_images_label from _call_show_additional_images_label_16
            with Dissolve(.5)

            show GG Passion
            show GG Passion:
                xalign .32
                ypos 1085
                zoom 1.0-0.035
            show Milf Passion
            show Milf Passion:
                xalign .85
                ypos 1085
                zoom 1.0-0.035


            with Dissolve(.5)









            "Марина" "Спасибо за помощь, [gg]."

            "[gg]" " Можешь положиться на меня."


            show Milf Laughs

            "Марина" "Миленький."






            jump main_interface_label




        "Помощь 3 ур" if help_ep3_milf_14 >= 2:


            $ renpy.music.stop(fadeout=1.5)

            $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)





            $ show_text_animation(_('+10 milf'))

            $ renpy.music.stop(fadeout=1.5)

            $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)



            show GG Normal
            show GG Normal:
                xalign .32
                ypos 1085
                zoom 1.0-0.035
            show Milf Normal
            show Milf Normal:
                xalign .85
                ypos 1085
                zoom 1.0-0.035

            show GG Laughs
            with Dissolve(.5)
            "[gg]" "Работы на высоте сопряжены с большим риском для здоровья, знаешь ли."

            "Марина" "Если такой умный, возьми лейку сам. "

            "[gg]" "С радостью. "

            "Марина" "Оу…"





            scene expression '#000' with Dissolve(.5)
            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_3/gf1.png'


            with Dissolve(.5)

            "[gg]" "Таааак-с. Стул кажется не очень устойчивым. "



            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_3/gf2.png'

            with Dissolve(.5)

            "Марина" "Не волнуйся, я подстрахую тебя."

            "[gg]" "А?.."


            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_3/gf3.png'

            with Dissolve(.5)


            "Марина" "Или ты думаешь, будто бы только я нуждаюсь в помощи? "

            "[gg]" "Я просто люблю проявлять к тебе внимание. "


            "Марина" "О…."


            "Марина" "Сейчас мы узнаем, насколько велико это «внимание»."


            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_3/gf4.png'

            with Dissolve(.5)


            "[gg]" "Я думал, тебе нужно полить цветок. "


            "Марина" "Разве я просила тебя об этом?"

            "[gg]" "Ну, ты же дала мне лейку и…"



            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_3/gf5.png'

            with Dissolve(.5)


            "Марина" "И ты сделал ровно то, что и требовалось."

            "[gg]" "Так мне поливать или нет?"



            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_3/gf6.png'

            with Dissolve(.5)

            "Марина" "Как же быстро ты возбудился…"

            "[gg]" "Поливать?.."




            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_3/gf7.png'

            with Dissolve(.5)

            "Марина" "Святые угодники, да он у тебя просто гигантский. "

            "[gg]" "…."



            scene expression 'cg/ep5/KoridorDay_Blur.png'

            show expression 'cg/ep5/help_3/gf8.png'

            with Dissolve(.5)

            "Марина" "Вау!!!.."


            "Марина" "Ты быстро пришёл в боевую готовность."


            "Марина" "Хи-хи-хи."


            "Марина" "Подходящий размерчик для моего «цветка»."

            scene expression '#000' with Dissolve(.5)
            scene expression 'cg/ep5/help_3/background.png'

            show expression 'cg/ep5/help_3/1yu.png'

            with Dissolve(.5)




            "Марина" "А вот теперь, милый, можешь и «полить»."

            "[gg]" "Мариночка…."



            scene expression 'cg/ep5/help_3/background.png'

            show expression 'cg/ep5/help_3/2yu.png'

            with Dissolve(.5)


            "Марина" "Мгл…"


            "Марина" "Какой сладкий на вкус."


            "Марина" "И такой сочный, приятный на ощущения."


            "Марина" "Ммм…."


            "Марина" "Восхитительно."


            "Марина" "Обожаю сладкий привкус этого члена. "


            scene expression 'cg/ep5/help_3/background.png'

            show 3_yu_animation

            with Dissolve(.5)



            "[gg]" "Марина, ты так яростно сосёшь…"

            "[gg]" "Быть может, ты немножко замедлишься?.."




            "Марина" "Нет! Твой член слишком вкусный. "


            "Марина" "Я не могу позволить тебе расслабиться."







            "Марина" "Хочу, чтобы ты накончал мне в рот как можно больше спермы."

            "[gg]" "Можешь быть уверена, я выплесну в тебя всё, что во мне накопилось."






            "Марина" "О дааа…."


            "Марина" "Я уже чувствую, как подступает горячее молочко моего мальчика."

            scene expression 'cg/ep5/help_3/background.png'

            show 3_yu_animation_fast

            with Dissolve(.5)


            "Марина" "Давай же, милый, трахай мой рот, что есть мочи."


            "Марина" "Давай! Ещё-ещё1"





            "Марина" "Высуши своего дружка до капли!"


            scene expression 'cg/ep5/help_3/background.png'

            show 3_yu_animation_fastest

            with Dissolve(.5)

            "[gg]" "Я практически готов…"








            "Марина" "Я тоже…"




            "[gg]" "Оооооо…. Даааа….."







            "Марина" "Мгл! Мгл! Мгл!!!"







            "[gg]" "Кончаю-кончаю-кончаю!!!"




            scene expression '#fff' with Dissolve(1)
            $ renpy.pause(.5, hard = True)
            scene expression 'cg/ep5/help_3/background.png'


            show expression 'cg/ep5/help_3/4yu.png'

            with Dissolve(.5)




            "[gg]" "Аххххх…."

            "[gg]" "Просто охренеть…."

            "[gg]" "Марина, я обожаю тебя."

            scene expression 'cg/ep5/help_3/background.png'

            show expression 'cg/ep5/help_3/5yu.png'

            with Dissolve(.5)





            "Марина" "А я тебя."


            "Марина" "Если хочешь повторить, приходи ещё."

            "[gg]" "Ещё бы."




            scene expression '#000' with Dissolve(1)
            $ location_now = 'Corridor'
            $ time.time_now = 'evening'

            call show_all_images_label from _call_show_all_images_label_21
            with Dissolve(1)

            show GG Passion
            show GG Passion:
                xalign .32
                ypos 1085
                zoom 1.0-0.035
            show Milf Passion
            show Milf Passion:
                xalign .85
                ypos 1085
                zoom 1.0-0.035

            with Dissolve(.5)







            "Марина" "Спасибо за помощь, [gg]."

            "[gg]" " Можешь положиться на меня."


            show Milf Laughs

            "Марина" "Миленький."







            jump main_interface_label

        "!Помощь 3 ур" if help_ep3_milf_14 < 2:
            $ pass

        "Назад." if True:

            jump main_interface_label




    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)



    show GG Normal
    show GG Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    show Milf Normal
    show Milf Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035

    show GG Laughs
    with Dissolve(.5)
    "[gg]" "Работы на высоте сопряжены с большим риском для здоровья, знаешь ли."
    show Milf Smile
    "Марина" "Болтун. Хочешь помочь? "
    show GG Normal
    "[gg]" "С радостью. "
    show Milf Passion
    "Марина" "Тогда держи меня. Очень и очень крепко."

    scene expression '#000' with Dissolve(1)

    $ renpy.pause(.5, hard = True)
    scene expression 'cg/ep3/Corridor_after_scene/1.png' 
    show GG Invis
    show GG Invis:
        xalign .33
    show Milf Invis
    show Milf Invis:
        xalign .6
    with Dissolve(.5)
    "Марина" "Таааак, аккуратно. Спокойно. "
    "Марина" "Забавно."
    "[gg]" "Да?"
    "Марина" "Ещё не так давно мы ходил в поход и лазили по горам практически без страховки."
    "Марина" "Теперь же я не только нуждаюсь в сторонней помощи, чтобы просто полить цветок, но и жутко боюсь высоты. "
    "[gg]" "Намекаешь на свой возраст?"

    "Марина" "Опасаюсь чрезмерной опеки с твоей стороны."
    "[gg]" "Если хочешь поиграть в «сильную и независимую», я могу уйти."
    "Марина" "Нет, останься. Я сглупила."
    "[gg]" "Как на счёт моих глупостей? Небольшое землетрясение..."

    scene expression 'cg/ep3/Corridor_after_scene/2.png' 
    show GG Invis
    show GG Invis:
        xalign .33
    show Milf Invis
    show Milf Invis:
        xalign .6
    with my_dissolve
    "Марина" "А?…"

    scene expression 'cg/ep3/Corridor_after_scene/3.png' 
    show GG Invis
    show GG Invis:
        xalign .33
    show Milf Invis
    show Milf Invis:
        xalign .6
    with my_dissolve
    "Марина" "Ой, кажется я падаю!"

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)



    scene expression 'cg/ep3/Corridor_scene/1.png' 

    show Milf Invis
    show Milf Invis:
        xalign .65
    with vpunch
    "Марина" "Ты в порядке?"

    show expression 'cg/ep3/Corridor_scene/2.png' 

    show Milf Invis
    show Milf Invis:
        xalign .65
    with Dissolve(.5)
    $ renpy.pause(999)
    "Марина" "Я постараюсь встать…"


    show expression 'cg/ep3/Corridor_scene/3.png' 

    show Milf Invis
    show Milf Invis:
        xalign .65
    with Dissolve(.5)

    "Марина" "Ахх…. "

    show expression 'cg/ep3/Corridor_scene/4.png' 

    show Milf Invis
    show Milf Invis:
        xalign .65
    with Dissolve(.5)

    "Марина" "Не получается…"
    show Corridor_scene_anim_0 

    show GG Invis
    show GG Invis:
        xalign .65
    with Dissolve(.5)
    "[gg]" "…."

label ep3_milf_14_korridor_2:
    menu:
        "1. Продолжать лежать." if True:
            $ renpy.pause(999)
            jump ep3_milf_14_korridor_2
        "2. Закончить." if True:
            $ pass


    $ time.time_now = 'evening'

    jump main_interface_label












label ep3_milf_14_shower_0:

    call show_bg_image_label from _call_show_bg_image_label_68
    show expression 'images/cg/ep1/mother_restroom_back.png'
    with Dissolve(.5)
    if not renpy.music.get_playing() or 'shower_milf' not in renpy.music.get_playing():
        play music 'audio/shower_milf.mp3'
    '[gg]' "Интересно, а это нормально, что я подглядываю за тем, как моется моя подруга?"
    '[gg]' "У неё потрясающее тело. И эта массивная, аппетитная задница - просто кайф."
    show expression 'images/cg/ep1/mother_restroom_front.png'
    with Dissolve(.5)
    '[gg]' "Она так увлечена процессом, что совсем не обращает на меня внимание. Я могу смотреть на это бесконечно"
    menu:
        "1. Продолжить смотреть." if True:
            $ location_now = 'Restroom'
            jump ep3_milf_14_shower_0
        "2. Прекратить смотреть." if True:
            $ location_now = 'Restroom'



    jump main_interface_label






label ep3_milf_14_shower:
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    $ Hide('main_interface', transition = Dissolve(.5))()

    scene expression 'images/cg/ep3/Milf_Fap_Water/bg.png'
    show expression 'images/cg/ep3/Milf_Fap_Water/milf_1.png'
    show expression 'images/cg/ep3/Milf_Fap_Water/FrontGround.png'

    with Dissolve(.5)
    "[gg]" "Я знал, что увижу нечто подобное."
    hide expression 'images/cg/ep3/Milf_Fap_Water/FrontGround.png'

    hide expression 'images/cg/ep3/Milf_Fap_Water/milf_1.png'
    show Milf_Fap_Water_anim_gg
    show Milf_Fap_Water_anim
    show expression 'images/cg/ep3/Milf_Fap_Water/FrontGround.png'

    with Dissolve(.5)
    "[gg]" "Да, Мариночка, ласкай себя. "

    "[gg]" "Твои пальчики такие нежные, ласковые… "
    "[gg]" "Ты проникаешь всё глубже и глубже. Ты определённо нуждается в моём члене."
    "[gg]" "Ох… Я сейчас кончу…"

label ep3_milf_14_shower_menu:
    window hide
    menu:
        "Продолжать." if True:
            $ renpy.pause(9999)
            jump ep3_milf_14_shower_menu
        "Закончить." if True:
            $ pass









    scene expression '#fff' with Dissolve(.2)
    $ renpy.pause(.2, hard = True)
    #$ add_to_gallery(-5)
    scene expression 'images/cg/ep3/Milf_Fap_Water/bg.png'
    show expression 'images/cg/ep3/Milf_Fap_Water/gg_3.png'



    show expression 'images/cg/ep3/Milf_Fap_Water/milf_4.png'
    show expression 'images/cg/ep3/Milf_Fap_Water/FrontGround.png'

    with Dissolve(1)

    $ renpy.pause(9999)
    "[gg]" "Обожаю её."
    if from_test:
        jump test_anim
    scene expression '#000' with Dissolve(.5)
    jump main_interface_label
















label ep3_milf_14_kitchen:
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/almost-bliss-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    $ Hide('main_interface', transition = Dissolve(.5))()
    scene expression 'images/cg/ep3/Play_Ass_Face/2.png'
    with Dissolve(.5)

    $ renpy.pause(9999)


    "Марина" "[gg]?.."
    "Марина" "Ты…"


    scene Play_Ass_Face_Anim
    with Dissolve(.5)


    "Марина" "… делаешь всё правильно."
    "Марина" "Продолжай, мой котёночек. "
    "Марина" "Мне очень хорошо."







    window hide

label ep3_milf_14_kitchen_2:

    menu:
        "1. Продолжить." if True:
            $ renpy.pause(999)
            jump ep3_milf_14_kitchen_2
        "2. Закончить." if True:
            $ pass
    scene expression '#fff' with Dissolve(.2)
    $ renpy.pause(.2, hard = True)
    scene expression 'cg/ep3/Play_Ass_Face/6.png'
    with Dissolve(1.5)
    "Марина" "О дааааа…."
    "Марина" "Как приятно."
    if from_test:
        jump test_anim






    "Марина" "Ты знаешь как поднять мне настроение, [gg]. "
    "[gg]" "Рад угодить, Марина."

    $ add_to_gallery(11)


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
