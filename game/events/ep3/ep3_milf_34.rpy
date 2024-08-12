




image Milf_Kitchen_2k_anim:
    'images/cg/ep3/Milf_Kitchen/2k_a.png' with Dissolve(.5)
    1
    'images/cg/ep3/Milf_Kitchen/2k_b.png' with Dissolve(.35)
    1

    repeat


image Milf_Kitchen_4k_anim:
    'images/cg/ep3/Milf_Kitchen/4k_a.png' with Dissolve(.25)
    1
    'images/cg/ep3/Milf_Kitchen/4k_b.png' with Dissolve(.25)
    1

    repeat

image Milf_Kitchen_3d_anim:

    'images/cg/ep3/Milf_Kitchen/2d.png' with Dissolve(.1)
    .3
    'images/cg/ep3/Milf_Kitchen/3d.png' with Dissolve(.1)
    .3

    repeat

image Milf_Kitchen_6k_anim:

    'images/cg/ep3/Milf_Kitchen/6k_a.png' with Dissolve(.3)
    .75
    'images/cg/ep3/Milf_Kitchen/6k_b.png' with Dissolve(.3)
    .75

    repeat


image Milf_Kitchen_6k_anim_2:

    'images/cg/ep3/Milf_Kitchen/6k_a.png' with Dissolve(.15)
    .4
    'images/cg/ep3/Milf_Kitchen/6k_b.png' with Dissolve(.15)
    .4

    repeat

screen ep3_milf_34_screen:
    imagebutton:
        idle 'cg/milf_and_sister_activities/milf_kitchen.png'
        hover im.MatrixColor('cg/milf_and_sister_activities/milf_kitchen.png', im.matrix.brightness(.1))
        focus_mask True
        action Return()
label ep3_milf_34:
    $ time.time_now = 'night'



    $ location_now = 'Kitchen'

    call show_all_images_label from _call_show_all_images_label_43


    $ renpy.music.stop(fadeout=.5)

    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)


    hide screen empty_screen
    show screen main_interface

    show screen ep3_milf_34_screen
    with Dissolve(.5)
    call screen empty_screen
    $ events.pop('ep3_milf_34', 0)

    hide screen ep3_milf_34_screen
    hide screen main_interface 
    hide screen empty_screen
    scene expression 'images/cg/ep3/Milf_Kitchen/Background.png'








    show expression 'images/cg/ep3/Milf_Kitchen/1k.png':
        xalign .5
        yalign 1.0
    with Dissolve(.5)
    "Марина" "Ах!… Осторожно. Здесь всё горячее. "
    "[gg]" "О да, я чувствую."
    "Марина" "Пожалуйста, перестань. "
    "[gg]" "Не перестану."
    "Марина" "Дома Кристи. Она может услышать."
    "[gg]" "Тогда не будем шуметь."
    scene expression 'images/cg/ep3/Milf_Kitchen/Background.png'

    show expression 'images/cg/ep3/Milf_Kitchen/2k.png':
        xalign .5
        yalign 1.0
    with Dissolve(.5)
    "Марина" "Прошу, не надо. Мы зашли слишком далеко. Если твой брат узнает, он убьёт нас обоих. "

    "[gg]" "Значит мы не скажем ему об этом. "
    "Марина" "Я не могу так… [gg]. Это предательство. Я просто поддалась сиюминутной страсти. "
    "[gg]" "Не верю."
    scene expression 'images/cg/ep3/Milf_Kitchen/Background.png'

    show Milf_Kitchen_2k_anim:
        xalign .5
        yalign 1.0
    with Dissolve(.5)

    "Марина" "Я…"
    "Марина" "Я говорю правду…"
    "Марина" "Пожалуйста, прекрати. "
    "Марина" "Мы поступаем неправильно."


    scene expression 'images/cg/ep3/Milf_Kitchen/Background.png'

    show expression 'images/cg/ep3/Milf_Kitchen/3k.png':
        xalign .5
        yalign 1.0
    with Dissolve(.75)

    $ renpy.pause(.1, hard = True)
    $ renpy.pause(99999999999)

    scene expression 'images/cg/ep3/Milf_Kitchen/Background.png'

    show expression 'images/cg/ep3/Milf_Kitchen/4k.png':
        xalign .5
        yalign 1.0
    with Dissolve(.5)
    $ renpy.pause(.1, hard = True)
    $ renpy.pause(99999999999)

    scene expression 'images/cg/ep3/Milf_Kitchen/Background.png'

    show Milf_Kitchen_4k_anim:
        xpos 0
        yalign 1.0
    with Dissolve(.5)




    "[gg]" "Попроси меня ещё раз. И я остановлюсь."
    "Марина" "*Вздох*"
    "Марина" "Это не честно."
    "[gg]" "Ну же, скажи это."
    "Марина" "Нет…"
    "[gg]" "Скажи!"
    scene expression 'images/cg/ep3/Milf_Kitchen/Background.png'

    show Milf_Kitchen_4k_anim:
        xalign .5
        yalign 1.0


    show expression 'images/cg/ep3/Milf_Kitchen/1d.png'
    show expression 'images/cg/ep3/Milf_Kitchen/1d.png':
        xpos 2250
    with Dissolve(.5)

    $ renpy.pause(.1, hard = True)
    $ renpy.pause(9999)
    show expression 'images/cg/ep3/Milf_Kitchen/1d.png':
        linear .5 xpos 1750

    hide Milf_Kitchen_4k_anim


    show expression 'images/cg/ep3/Milf_Kitchen/5k.png':
        xpos 0
        yalign 1.0
    with Dissolve(.5)





    "Марина" "Почему ты остановился?"
    "[gg]" "Хочу знать, как сильно ты меня хочешь."
    "Марина" "Пожалуйста… Не мучай меня."
    "Марина" "Я пока не готова к этому."
    "Марина" "Ладно… Если хочешь, можешь продолжать, но без проникновения."
    hide expression 'images/cg/ep3/Milf_Kitchen/1d.png'
    show Milf_Kitchen_3d_anim

    show Milf_Kitchen_3d_anim:
        xpos 1750
        yalign 1.0
    with my_dissolve

    "[gg]" "Ладно… Но ты должна обещать, что в следующий раз, мы точно сделаем это."
    "Марина" "Обещаю…"


    scene expression 'images/cg/ep3/Milf_Kitchen/Background.png'
    show Milf_Kitchen_3d_anim:
    show Milf_Kitchen_3d_anim:
        xpos 1550
        yalign 1.0

    show expression 'images/cg/ep3/Milf_Kitchen/6k.png':
        xpos 0
        yalign 1.0

    with Dissolve(.5)

    $ renpy.pause(.1, hard = True)
    $ renpy.pause(99999)
    "[gg]" "О дааа…."


    "Марина" "Аххх… Я чувствую мокроту твоего горячего члена."


    scene expression 'images/cg/ep3/Milf_Kitchen/Background.png'
    show Milf_Kitchen_3d_anim:
    show Milf_Kitchen_3d_anim:
        xpos 1550
        yalign 1.0
    show Milf_Kitchen_6k_anim:

    show Milf_Kitchen_6k_anim:
        xpos 0
        yalign 1.0

    with Dissolve(.5)
    "Марина" "Просто невероятно."

    "[gg]" "Я люблю тебя."
    "Марина" "Невероятно!.."
    "Марина" "Мои извращённые фантазии сбываются наяву."

    "Марина" "Твои юное пламя сладко обжигает мою попочку."
    "Марина" "Твой член просто великолепен, милый. Продолжай, мой хороший, продолжай."

    "Марина" "Тебе нравится, как я сжимаю твой член? Классно, да?"
    "Марина" "Ещё-ещё-ещё! Я хочу, чтобы ты насладился этим моментом сполна."

    "Марина" "Сделай это. Сделай это вместе со мной. Я почти на грани…."
    "Марина" "Почти…."










    scene expression 'images/cg/ep3/Milf_Kitchen/Background.png'
    show Milf_Kitchen_3d_anim:
    show Milf_Kitchen_3d_anim:
        xpos 1550
        yalign 1.0
    show Milf_Kitchen_6k_anim:

    show Milf_Kitchen_6k_anim:
        xalign .5
        yalign 1.0

    with Dissolve(.5)
    $ renpy.pause(.05, hard = True)
    $ renpy.pause(9999)

label ep3_milf_34_menu:
    menu:
        "Продолжить" if True:
            $ renpy.pause(9999)
            jump ep3_milf_34_menu
        "Закончить" if True:
            $ pass

    show Milf_Kitchen_6k_anim_2:
        xalign .5
        yalign 1.0

    with Dissolve(.5)


    "Марина" "Кончаааааааааааааюююююююю!!!"
    "[gg]" "И яяяяяяяяяяя!!!…."
    scene expression 'images/cg/ep3/Milf_Kitchen/Background.png'

    show expression '#fff'
    with Dissolve(.2)

    $ renpy.pause(.1, hard = True)
    hide expression '#fff'
    show expression 'images/cg/ep3/Milf_Kitchen/7k.png'
    show expression 'images/cg/ep3/Milf_Kitchen/7k.png':
        xalign .1
        yalign 1.0
    show expression 'images/cg/ep3/Milf_Kitchen/4d.png'
    show expression 'images/cg/ep3/Milf_Kitchen/4d.png':
        xpos 1750
        yalign 1.0
    with Dissolve(1)
    $ renpy.pause(.1, hard = True)
    $ renpy.pause(99999)

    hide expression 'images/cg/ep3/Milf_Kitchen/4d.png'
    show expression 'images/cg/ep3/Milf_Kitchen/1d.png'
    show expression 'images/cg/ep3/Milf_Kitchen/1d.png':
        xpos 1750
        yalign 1.0
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show expression 'images/cg/ep3/Milf_Kitchen/1d.png':
        xzoom -1
        linear 1 xpos 2200
    $ renpy.pause(1, hard = True)












    scene expression '#000' with Dissolve(1)

    $ renpy.pause(.5, hard = True)
    scene expression 'images/cg/ep3/Milf_Kitchen/Background.png'
    with Dissolve(1)
    show GG Embarrassment
    show GG Embarrassment:
        xalign .15
        ypos 1085
        zoom 1.0

    show Milf Embarrassment
    show Milf Embarrassment:
        ypos 1085

        xalign .85
    with Dissolve(.5)


    "[gg]" "Ты слышала? Сюда кто-то идёт!"
    show Milf Embarrassment
    "Марина" "Тссс…"

    hide Milf
    show Milf Embarrassment
    show Milf Embarrassment:
        ypos 1085

        xalign .85

    show Milf Embarrassment:
        linear .5 xalign .35
        xzoom -1


    hide GG
    show GG Embarrassment
    show GG Embarrassment:
        ypos 1085

        xalign .15

    show GG Embarrassment:
        linear .5 xalign .05
    with None


    show Christie Normal

    show Christie Normal:

        ypos 1085

        xalign .85

    with Dissolve(.5)

    $ renpy.pause(.4, hard = True)

    "Кристи" "Эй, вы почему ещё не спите?"
    show Milf Embarrassment
    "Марина" "Ну… Мы…"
    show GG Normal
    "[gg]" "А ты почему не спишь, Кристи?"
    "Кристи" "Меня разбудил какой-то шум. То ли крики, то ли звук замка входной двери… тяжело разобрать спросонья. "
    "Кристи" "Решила осмотреть дом, а тут вы."
    show Milf Normal
    "Марина" "Тут такое дело… [gg] не ужинал, и я решила приготовить ему поесть. "
    show GG Smile
    "[gg]" "Ага."
    show Christie Skepticism
    "Кристи" "Чёт я не вижу никакой еды."
    show GG Laughs
    "[gg]" "Я всё съел. "

    "Кристи" "Ага, понятно. "

    "Кристи" "Значит, вы идёте спать?"
    show Milf Normal
    "Марина" "Да, конечно. Всем сладких снов."
    show GG Normal
    "[gg]" "Сладких…"
    show GG Normal
    "[gg]" "(Чёрт, я надеюсь, Игорь справился со своей задачей и давно свалил.)"

    show Milf:
        linear 1 xalign 1.5

    $ renpy.pause(1, hard = True)

    show GG Normal
    "[gg]" "Ну, и я спать."
    "Кристи" "Великолепно."
    $ check_saves        = True
    $ block_exit_home    = False
    $ block_time_forward = False
    if from_test:
        jump test_anim

    show GG Normal:
        linear 1 xalign 1.5
    $ renpy.pause(.5, hard = True)
    scene expression '#000' with Dissolve(.5)
    $ add_to_gallery(10)
    if not from_gallery_check():
        $ block_time_forward = False

        $ block_exit_home    = False

        $ block_sister_home  = False

        if hasattr(store, 'ep3_milf_16'):
            $ del ep3_milf_16

        $ location_now = 'Corridor'

        $ events.pop('ep3_milf_28', 0)


        $ events.pop('stump_bed', 0)

        $ descript = _('Лечь спать.')

        $ events.pop('bed_night_milf_34', 0)

        $ events.pop('bed_night_milf_35', 0)



        $ Event('ep3_milf_35', None, day_start = time.day_now + 1)
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
