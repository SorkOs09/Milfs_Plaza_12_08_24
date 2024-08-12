
image ep5_getto_gachi_2:
    'cg/ep5/getto/gachi/2_0.png' with Dissolve(.1)
    .08
    'cg/ep5/getto/gachi/2_1.png' with Dissolve(.1)
    .08
    'cg/ep5/getto/gachi/2_2.png' with Dissolve(.1)
    .08
    'cg/ep5/getto/gachi/2_1.png' with Dissolve(.1)
    .08
    'cg/ep5/getto/gachi/2_0.png' with Dissolve(.1)
    .08
    repeat

image ep5_getto_gachi_3:
    'cg/ep5/getto/gachi/3_0.png' with Dissolve(.1)
    .08
    'cg/ep5/getto/gachi/3_1.png' with Dissolve(.1)
    .08

    'cg/ep5/getto/gachi/3_0.png' with Dissolve(.1)
    .08
    repeat

screen bandit_screen_milf_70:
    use ep4_main_city_screen(mpn=False)
    imagebutton:
        focus_mask True
        idle 'cg/ep5/bandit_screen_milf_70.png'
        hover im.MatrixColor('cg/ep5/bandit_screen_milf_70.png', im.matrix.brightness(.3))
        action Return()


screen ep4_milf_70_city_screen(btn='city_getto_button'):


    use ep4_main_city_screen



    imagebutton:
        idle btn
        hover btn
        at ButtonEffect01
        focus_mask True

        action Return()


label ep5_milf_70_1:
    $ block_exit_home = True
    scene expression 'images/interface/city_interface/city_bg_' + time.time_now + '.png'
    with Dissolve(.5)
    call screen ep4_milf_70_city_screen
    $ Location(
                'City_Getto',
                buttons = [{
                  
                }, ]
                )
    $ location_now = 'City_Getto'

    call show_all_images_label from _call_show_all_images_label_52
    with Dissolve(.5)






























    show expression 'cg/ep5/bandit_screen_milf_70.png'
    show Kat Bat_Normal
    show Kat Bat_Normal:
        xzoom -1
        xalign -.5

    show GG Bat_Normal
    show GG Bat_Normal:
        xalign -.5
    with Dissolve(.5)

    show Kat Bat_Normal:
        linear 1 xalign .4


    show GG Bat_Normal:
        linear .75 xalign -0.1

    $ renpy.pause(1, hard = True)


    show Kat Bat_Normal:
        xzoom 1
        xalign .4


    show GG Bat_Normal:
        xalign -0.1


    with my_dissolve

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/loopster-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    "[gg]" "Мы на месте. "

    "Кэт" "Я вижу. "

    "Кэт" "А ещё я вижу мудака на шухере. "


    show Kat Bat_Surprise
    "Кэт" "Думаешь, нас пустят внутрь только потому, что мы одеты как два клоуна? "

    "[gg]" "Спокойно, Кэт."

    "[gg]" "В этих нарядах, если надо, мы сможем добраться и до самого президента. "
    show Kat Bat_Smile
    "Кэт" "Разве что до Кеннеди. "

    "[gg]" "Примани его в переулок, а я подкрадусь сзади и выведу бандита из строя."

    show Kat Bat_WTF
    "Кэт" "Аааааа!"

    "Кэт" "Мерзавец!"
    "Кэт" "Теперь я поняла, почему ты выбрал для меня именно такой наряд!"

    "[gg]" "Можем поменяться. Хе-хе-хе."

    "Кэт" "Говнюк."

    show Kat Bat_Normal
    "[gg]" "Ближе к делу!"
    show GG Bat_Smile
    "[gg]" "Точнее, даже, ближе к телу – хе-хе-хе!"

    show Kat Bat_Surprise
    "Кэт" "…."

    "[gg]" "Слушай, Кэт, я ведь не принуждаю тебя совокупляться с этим животным. "

    "[gg]" "Всего лишь отвлечь, а всю грязную работу я сделаю сам."
    show Kat Bat_WTF
    "Кэт" "Больше похоже на то, что испачкаюсь здесь только я…"

    "[gg]" "Это займёт у тебя буквально минуту. "

    "Кэт" "… И позор на всю жизнь. "

    "Кэт" "А где твой пистолет? Ты его не забыл?"
    show GG Bat_Smile
    "[gg]" "Всё под контролем. Я приклеил его около паха."

    show Kat Bat_WTF

    "Кэт" "Зачем?"

    show GG Bat_Sad

    "[gg]" "На случай, если нас станут обыскивать. Ты когда-нибудь видела, чтобы кто-то трогал член в поисках оружия?"

    "Кэт" "…."

    "[gg]" "Ну? Ты идёшь?"
    show Kat Bat_Surprise
    "Кэт" "Ладно уж, ниже падать мне некуда. "
    show Kat Bat_Smile
    "Кэт" "Спрячься пока, а я постараюсь соблазнить этого быдлана. "

    "[gg]" "Понял-принял."
    show GG Bat_Normal:
        xzoom -1
        linear 1 xalign -1.5
    show Kat Bat_Normal:
        xzoom -1
        linear 1 xalign 1.5

    $ renpy.pause(1)
    show GG:
        xzoom -1
        xalign -1.5
    show Kat:
        xzoom -1
        xalign 1.5
    call show_all_images_label from _call_show_all_images_label_54
    show expression 'cg/ep5/bandit_screen_milf_70.png'
    with Dissolve(.5)
    call screen bandit_screen_milf_70
    $ stnd_music_play()














    show GG Bat_Normal
    show GG Bat_Normal:
        xzoom -1 xalign -1.5
    show Kat Bat_Normal
    show Kat Bat_Normal:
        xzoom -1 xalign .2
    show Bandit Normal
    show Bandit Normal:
        xalign .82
    with Dissolve(.5)
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "Кэт" "Привееееет, красавчик."
    show Bandit Normal
    "Качок" "Чо надо?"

    "Кэт" "Проходила мимо и увидела твою скучающую мордашку. "

    "Кэт" "Вот, думаю, может… мы, ну, ты знаешь, развлечёмся где-нибудь здесь, за углом."
    show Bandit Normal
    "Качок" "Хе-хе-хе."
    show Bandit Normal
    "Качок" "А ты смешная. "
    show Bandit Normal
    "Качок" "Напоминаешь мне одну дурёху, что работает на моего босса."
    show Kat Bat_Smile
    "Кэт" "И как, она миленька?"
    show Bandit Normal
    "Качок" "Ха-ха-ха!"
    show Bandit Normal
    "Качок" "Есть у вас что-то общее, определённо. "
    show Bandit Normal
    "Качок" "Но я бы не назвал её миленькой. Да и ты, знаешь ли, скорее бесишь меня, чем привлекаешь."
    show Kat Bat_WTF
    "Кэт" "А?!"
    show Bandit Normal
    "Качок" "Это девка… Кэт её кажется зовут. Да, точно Кэт. Она чокнутая, сечёшь? Беды с башкой и всё в таком духе."

    "Кэт" "Это ещё почему?!"
    show Bandit Normal
    "Качок" "Ну…"
    show Bandit Normal
    "Качок" "Как-то мой босс отправил её… ну, скажем, так, на ответственное задание к одному типу, что задолжал нам крупную сумму денег. "
    show Kat Bat_Surprise
    "Кэт" "И?"
    show Bandit Normal
    "Качок" "А она заявила боссу, дескать, так и так, не будет этого делать, поскольку она не хочет в тюрячку, и вообще, не для того её нанимали. Хе-хе-хе."

    "Кэт" "Но ведь до этого же она наверняка выполняла массу других… эммм… поручений, и успешно?"
    show Bandit Normal
    "Качок" "Чёрт! Ха-ха-ха!"
    show Bandit Normal
    "Качок" "Ты угадала!"
    show Bandit Normal
    "Качок" "Да! Именно так и было. "
    show Bandit Normal
    "Качок" "Я подозреваю, она просто влюбилась в этого пацана, а все её отмазки тупая попытка оправдаться."
    show Bandit Normal
    "Качок" "Дура она в общем. Завалят их обоих."

    "Кэт" "…."
    show Kat Bat_WTF
    "Кэт" "Вечер становится томным. "
    show Bandit Normal
    "Качок" "Ага."

    "Кэт" "Дык может, того, давай… Ну, ты и я. Завершим этот миг приятным для нас эпиологом?"
    show Bandit Normal
    "Качок" "Хе-хе-хе!"
    show Bandit Normal
    "Качок" "А ты настырная, как я погляжу."
    show Bandit Normal
    "Качок" "Нет, дурёха, меня девчонки не интересуют. "
    show Bandit Normal
    "Качок" "Ищи другого кавалера. "
    show Kat Bat_Surprise
    "Кэт" "Ч..чиво?!"
    show Bandit Normal
    "Качок" "Чо слышала, то и сказал. Гуляй, говорю."

    "Кэт" "Л-ладно…"





    show Kat Bat_Normal:
        xzoom 1
        linear 1 xalign -1.2
    $ renpy.pause(1)


    scene black
    with Dissolve(.5)

    $ renpy.pause(.5)

    call show_all_images_label from _call_show_all_images_label_53
    with Dissolve(.5)
    show GG Bat_Normal
    show GG Bat_Normal:
        xalign .2
    show Kat Bat_Normal
    show Kat Bat_Normal:

        xalign 1.5
    with Dissolve(.5)

    show Kat Bat_Normal:
        linear 1 xalign .82
    $ renpy.pause(1)

    show Kat Bat_Normal:
        xalign .82




    with my_dissolve








    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/loopster-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    "[gg]" "Эй, ты почему его не завела в переулок?!"

    "Кэт" "Дело труба."

    show GG Bat_Sad
    "[gg]" "Почему?"

    "Кэт" "Он голубой."

    show GG Bat_Normal
    "[gg]" "Неожиданно. "
    show Kat Bat_Smile
    "Кэт" "Так бывает, если долго ходить в качалку."

    show GG Bat_Smile
    "[gg]" "Хех…."
    show Kat Bat_Normal
    "Кэт" "Но я знаю что в этом случае делать."

    show GG Bat_Sad
    "[gg]" "Смена пола?"
    show Kat Bat_Surprise
    "Кэт" "Лучше! Я отправлю тебя соблазнять нашего сторожило у подъезда!"

    show GG Bat_Normal
    "[gg]" "Чтоооо?!"
    show Kat Bat_WTF
    "Кэт" "Что слышал. "

    "Кэт" "Там твой друг, если ты вдруг забыл."
    show Kat Bat_Normal
    "Кэт" "И раз уж я согласился на твой план, то ты тем более должен быть рад, что тебе подвернулась возможность собственноручно реализовать задуманное! "

    "[gg]" "…."

    "[gg]" " Мдэ…"

    "[gg]" " Ты абсолютно права. "
    show Kat Bat_WTF
    "Кэт" "Да?!"

    "[gg]" " Ага."

    "[gg]" " Вот, возьми мой пистолет. "

    "[gg]" " Смотри и учись как работают профессионалы."
    show Kat Bat_Surprise
    "Кэт" "Офигеть… Пойду спрячусь."
    show GG Bat_Normal:
        linear 1 xalign 1.5

    $ renpy.pause(1)
    show GG:
        xalign 1.5
    call show_all_images_label from _call_show_all_images_label_89
    with Dissolve(.5)
    call screen bandit_screen_milf_70


    show GG Bat_Normal
    show GG Bat_Normal:
        xalign -1.5
    show Bandit Normal
    show Bandit Normal:
        xalign .82



    with Dissolve(.5)
    show GG Bat_Normal:
        linear 1 xalign .2

    $ renpy.pause(1)
    show GG Bat_Normal:
        xalign .2




















    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/past-sadness-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    show Bandit Normal
    "Качок" "Это что, костюм Зорро? "

    "[gg]" "{i}Подумать только, этот дуболом знает Зорро.{/i}"
    show Bandit Normal
    "Качок" "Антонио Бандерас?"

    "[gg]" "Ален Дэлон."
    show Bandit Normal
    "Качок" "А ты хорош!"

    "[gg]" "Спасибо. Ты вроде тоже… ничего так."
    show Bandit Normal
    "Качок" "Уууу…."
    show Bandit Normal
    "Качок" "Тебе нравятся мои мышцы? "

    show GG Bat_Chagrin
    "[gg]" "Выглядят… упругими. "
    show Bandit Normal
    "Качок" "Как и мои маслянистые ягодицы, пацан. "

    show GG Bat_Sad
    "[gg]" "Н-наверное. Пожалуй, что так."
    show Bandit Normal
    "Качок" "Хотел бы их пощупать?"

    show GG Bat_Chagrin
    "[gg]" "Кого? Задницу?"
    show Bandit Normal
    "Качок" "Ха-ха-ха!!!"
    show Bandit Normal
    "Качок" "Мышцы, пацан, мои мышцы. Но знаешь, твой ход мысли мне нравится больше, хе-хе-хе."

    show GG Bat_Sad
    "[gg]" "Даа…. Я такой."

    "[gg]" "{i}На какую херню я только что подписался?!{/i}"
    show Bandit Normal
    "Качок" "Тогда, может, зайдёшь ко мне на минуточку?"
    show Bandit Normal
    "Качок" "Уверен, ты не пожалеешь. "

    show GG Bat_Chagrin
    "[gg]" "{i}Сразу внутрь дома? Всё даже идёшь лучше, чем я предполагал.{/i}"

    "[gg]" "Да, это прекрасная идея. Пойдём."

    show GG Bat_Normal:
        linear 1 xalign 1.5
    show Bandit Normal:
        xzoom -1
        linear 1 xalign 2.2
    $ renpy.pause(1)
    show Kat Bat_Normal
    show Kat Bat_Normal at go_from_left(xxzoom = -1)
    $ renpy.pause(.5)




    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/loopster-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)



    show GG Bat_Normal:
        xalign 1.5
    show Bandit Normal:
        xzoom -1
        xalign 2.2

    show Kat Bat_Surprise:
        xalign .15
    with my_vpunch
    "Кэт" "Куда это они?!"
    show Kat Bat_WTF
    "Кэт" "Но ведь это не по плану…"

    "Кэт" "И как, чёрт возьми, я проникну в дом? Они же закрылись."



    scene black with Dissolve(.5)

    $ renpy.pause(.5)

    scene expression 'cg/ep5/getto/room_1.png'
    show GG Bat_Normal
    show GG Bat_Normal:
        xalign 1.5
    show GG Bat_Normal
    show Bandit Normal:
        xalign 1.5
    with Dissolve(.5)
    show GG Bat_Normal:
        xzoom -1
        linear 1 xalign .1
    show Bandit Normal:
        linear 1 xalign .82
    $ renpy.pause(1, hard = True)
    show GG Bat_Normal:
        xzoom 1
        xalign .1
    show Bandit Normal:
        xalign .82
    with my_dissolve
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "Качок" "Уверяю тебя, пацан, ты не пожалеешь о своём выборе."

    show GG Bat_Chagrin
    "[gg]" "Я… Я в предвкушении…"

    show GG Bat_Sad
    "[gg]" "{i}Ну и что мне теперь делать?!{/i}"

    "[gg]" "{i}Я даже не успею снять с пистолета предохранитель. Этот плейбой быстро меня заломит и устроит небо в алмазах.{/i}"

    show GG Bat_Chagrin
    "[gg]" "{i}Ладно, импровизируем…{/i}"

    show Bandit Normal:
        linear 1 xalign .3
    $ renpy.pause(1, hard = True)

    scene expression 'cg/ep5/getto/room_1.png'
    show expression 'cg/ep5/getto/gachi/1.png'
    with vpunch



    "Бандит" "Если честно, я редко бываю таким напористым."


    "[gg]" "Тяжело в это поверить…"


    "Бандит" "Это ты так на меня действуешь."


    "[gg]" "Извини…"


    "Бандит" "Всё в порядке. Я вижу, что у тебя это впервые. "


    "[gg]" "Т-ты меня р-раскусил… "

    scene expression 'cg/ep5/getto/room_1.png'
    show ep5_getto_gachi_2
    show Kat Bat_Normal
    show Kat Bat_Normal:
        xalign 1.5
    with Dissolve(.5)

    $ renpy.pause(9999)
    "Бандит" "Ооо, я вижу тебе уже невтерпёж. Люблю, когда партнёр берёт инициативу в свои руки."


    "[gg]" "Это точно."


    "[gg]" "{i}Доставайся же ты, чёртов пистолет. {/i}"


    "[gg]" "{i}Не получается! Слишком сильно приклеил скотчем… {/i}"

    show Kat Bat_Normal:
        linear 1 xalign .82
    $ renpy.pause(1, hard = True)
    show Kat Bat_Surprise:
        xalign .82
    hide ep5_getto_gachi_2
    show ep5_getto_gachi_3
    with vpunch
    $ renpy.pause(99999)
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    "Кэт" "[gg]??!!!"
    show Kat Bat_WTF
    "Кэт" "Какого хера?!!.."


    "Бандит" "А ты ещё откуда взялась?!"


    "[gg]" "Ты не так всё поняла, Кэт!"


    "Бандит" "Кэт?! Так это ты?!"

    "Кэт" "Чёрт, ну спасибо!"

    hide ep5_getto_gachi_3

    show expression 'cg/ep5/getto/gachi/3_2.png'
    with vpunch
    $ renpy.pause(999)

label ep5_milf_70_1_circle:

    "[gg]" "Наконец-то!"
    $ ep5_tmp = renpy.call_screen('circle_mini_game_screen', xp = 540, yp = 400, tm = 3)

    if not ep5_tmp:
        "Бандит" "Это чё за хрень?"
        show black
        with vpunch
        "" "Миссия провалена"
        "" "Попробовать снова?"
        menu:
            "Да" if True:
                hide black
                with my_dissolve
                jump ep5_milf_70_1_circle
            "Нет (Выход в главное меню)" if True:
                $ renpy.full_restart()
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/loopster-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    hide expression 'cg/ep5/getto/gachi/3_2.png'

    show expression 'cg/ep5/getto/gachi/4_0.png'
    show expression 'cg/ep5/getto/gachi/4_1.png':
        xpos 0
        easein_cubic 1 xpos 200
    with vpunch
    $ renpy.pause(1, hard = True)







    "Бандит" "Ауч…."

    hide expression 'cg/ep5/getto/gachi/4_1.png'
    with vpunch
    hide expression 'cg/ep5/getto/gachi/4_0.png'

    show GG Bat_Normal
    show GG Bat_Normal:
        xalign 0.02
    with my_dissolve



    "[gg]" "Кажется, я его вырубил…"
    show Kat Bat_Surprise
    "Кэт" "А я уж решила, что ты окончательно слился со своим образом."

    "[gg]" "Да пошла ты! Зорро не был голубым!"
    show Kat Bat_Smile
    "Кэт" "Первая фаза – отрицание. Ха-ха-ха!"

    "[gg]" "…."

    show GG Bat_Normal
    show GG Bat_Normal:

        linear 1 xalign 1.5
    show Kat Bat_Normal
    show Kat Bat_Normal:
        xzoom -1
        linear 1 xalign 1.5
    $ renpy.pause(1, hard = True)

    scene black with Dissolve(.5)

    $ renpy.pause(.5)

    scene expression 'cg/ep5/getto/room_2.png'
    show Kat Bat_Normal
    show Kat Bat_Normal:
        xalign -1.5
    show GG Bat_Normal
    show GG Bat_Normal:
        xalign -1.5
    with Dissolve(.5)


    show Kat Bat_Normal:
        xzoom -1
        linear 1 xalign -.1
    show GG Bat_Normal:

        linear 1 xalign .2

    $ renpy.pause(1, hard = True)

    show expression 'cg/ep5/getto/bandit/pistolet_3.png':
        xpos 1200


    show Kat Bat_Normal:
        xzoom -1 xalign -.1
    show GG Bat_Normal:
        xalign .2


    with my_dissolve




    "Кэт" "Ты уже выяснил, в какой из квартир держат твоего друга?"

    "[gg]" "Нет, но сейчас узнаем. "



    $ descript = _('Найти Игоря')
    jump ep5_milf_70_2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
