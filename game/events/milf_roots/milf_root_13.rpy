


image milf_root_13_1_1:






    'cg/ep85/gg_milf_sex/1.png' with Dissolve(0)
    .12
    'cg/ep85/gg_milf_sex/2.png' with Dissolve(0)
    .12
    'cg/ep85/gg_milf_sex/3.png' with Dissolve(0)
    .12
    'cg/ep85/gg_milf_sex/4.png' with Dissolve(0)
    .12
    'cg/ep85/gg_milf_sex/5.png' with Dissolve(0)
    .07
    'cg/ep85/gg_milf_sex/6.png' with Dissolve(0)
    .07
    'cg/ep85/gg_milf_sex/5.png' with Dissolve(0)
    .07
    'cg/ep85/gg_milf_sex/4.png' with Dissolve(0)
    .12
    'cg/ep85/gg_milf_sex/3.png' with Dissolve(0)
    .12
    'cg/ep85/gg_milf_sex/2.png' with Dissolve(0)
    .12


    repeat



image milf_root_13_1_2:




    'cg/ep85/gg_milf_sex/1.png' with Dissolve(0)
    .08
    'cg/ep85/gg_milf_sex/2.png' with Dissolve(0)
    .08
    'cg/ep85/gg_milf_sex/3.png' with Dissolve(0)
    .08
    'cg/ep85/gg_milf_sex/4.png' with Dissolve(0)
    .08
    'cg/ep85/gg_milf_sex/5.png' with Dissolve(0)
    .04
    'cg/ep85/gg_milf_sex/6.png' with Dissolve(0)
    .04
    'cg/ep85/gg_milf_sex/5.png' with Dissolve(0)
    .04
    'cg/ep85/gg_milf_sex/4.png' with Dissolve(0)
    .08
    'cg/ep85/gg_milf_sex/3.png' with Dissolve(0)
    .08
    'cg/ep85/gg_milf_sex/2.png' with Dissolve(0)
    .08




    repeat


image milf_root_13_1_3:




    'cg/ep85/gg_milf_sex/1.png' with Dissolve(0)
    .06
    'cg/ep85/gg_milf_sex/2.png' with Dissolve(0)
    .06
    'cg/ep85/gg_milf_sex/3.png' with Dissolve(0)
    .06
    'cg/ep85/gg_milf_sex/4.png' with Dissolve(0)
    .06
    'cg/ep85/gg_milf_sex/5.png' with Dissolve(0)
    .03
    'cg/ep85/gg_milf_sex/6.png' with Dissolve(0)
    .03
    'cg/ep85/gg_milf_sex/5.png' with Dissolve(0)
    .03
    'cg/ep85/gg_milf_sex/4.png' with Dissolve(0)
    .06
    'cg/ep85/gg_milf_sex/3.png' with Dissolve(0)
    .06
    'cg/ep85/gg_milf_sex/2.png' with Dissolve(0)
    .06




    repeat



image milf_root_13_1_4:




    'cg/ep85/gg_milf_sex/1.png' with Dissolve(0)
    .05
    'cg/ep85/gg_milf_sex/2.png' with Dissolve(0)
    .05
    'cg/ep85/gg_milf_sex/3.png' with Dissolve(0)
    .05
    'cg/ep85/gg_milf_sex/4.png' with Dissolve(0)
    .05
    'cg/ep85/gg_milf_sex/5.png' with Dissolve(0)
    .03
    'cg/ep85/gg_milf_sex/6.png' with Dissolve(0)
    .03
    'cg/ep85/gg_milf_sex/5.png' with Dissolve(0)
    .03
    'cg/ep85/gg_milf_sex/4.png' with Dissolve(0)
    .05
    'cg/ep85/gg_milf_sex/3.png' with Dissolve(0)
    .05
    'cg/ep85/gg_milf_sex/2.png' with Dissolve(0)
    .06




    repeat



image milf_root_13_2_1:


    'cg/ep85/gg_milf_sex/1s.png' with Dissolve(0)
    .25
    'cg/ep85/gg_milf_sex/2s.png' with Dissolve(0)
    .25
    'cg/ep85/gg_milf_sex/3s.png' with Dissolve(0)
    .25
    'cg/ep85/gg_milf_sex/4s.png' with Dissolve(0)
    .25
    '#0000'
    1


    repeat


image milf_root_13_2_2:


    'cg/ep85/gg_milf_sex/1s.png' with Dissolve(0)
    .13
    'cg/ep85/gg_milf_sex/2s.png' with Dissolve(0)
    .13
    'cg/ep85/gg_milf_sex/3s.png' with Dissolve(0)
    .13
    'cg/ep85/gg_milf_sex/4s.png' with Dissolve(0)
    .13
    '#0000'
    1


    repeat

image milf_root_13_2_3:


    'cg/ep85/gg_milf_sex/1s.png' with Dissolve(0)
    .07
    'cg/ep85/gg_milf_sex/2s.png' with Dissolve(0)
    .07
    'cg/ep85/gg_milf_sex/3s.png' with Dissolve(0)
    .07
    'cg/ep85/gg_milf_sex/4s.png' with Dissolve(0)
    .07
    '#0000'
    1


    repeat


label milf_root_13:



    if getattr(store, 'block_exit_home', False) or getattr(store, 'block_time_forward', False):
        $ Event('milf_root_13', location = "Corridor", day_start = time.day_now+1, time = ['evening'])
        jump main_interface_label
    $ events.pop('milf_root_13', 0)







    call show_bg_image_label from _call_show_bg_image_label_156
    with Dissolve(.5)
    show Milf Night_Normal
    show Milf Night_Normal at go_from_right
    show GG Surprise
    show GG Surprise at go_from_left
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/your-call-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Эй, ты чего в ночнушке?! "
    show GG:
        xalign .15
    show Milf Night_Smile:
        xalign .85
    with my_dissolve
    "Марина" "Доверься. Такой вид на него лучше сработает."
    show GG WTF
    "[gg]" "Охх… Не нравится мне этот план."
    show Milf Night_Normal
    "Марина" "Пока спрячься у себя в комнате. Я скажу полицейскому, что никого нет дома."
    show Milf Night_Normal
    "Марина" "Когда мы проследуем в спальню, можешь выдвигаться. "
    show GG Normal
    "[gg]" "Понял-принял."

    show GG:
        xzoom -1
        easein_cubic 4 xalign -1.5
    $ renpy.pause(1, hard = True)
    hide GG
    show Officer Smile
    show Officer Smile:
        alpha 0 xalign .55 xzoom -1
        easein_cubic 1 xalign .15 alpha 1.0
        xzoom 1
    $ renpy.pause(1.2, hard = True)
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/lo-fi-hip-hop-02-by-winniethemoog-from-filmmusic-io.mp3', fadein = 1.5)
    show Milf Night_Embarrassment_pose_3
    show Officer:
        xalign .15 alpha 1.0
        xzoom 1
    with my_dissolve
    "Офицер" "Добрый вечер, хозяюшка…"
    show Milf Night_Embarrassment_pose_3
    "Марина" "Добро пожаловать, офицер. "
    show Officer Chagrin
    "Офицер" "Сегодня вы одеты как-то… по-особенному. "
    show Milf Night_Passion_pose_3
    "Марина" "У меня и настроение, скажу я вам, особенное. "
    show Officer Laughs
    "Офицер" "Хех… Знаете, мне очень импонирует ваше гостеприимство. "
    show Milf Night_Smile_pose_3
    "Марина" "Ох! Приберегите ваши комплименты, офицер, они ещё пригодятся вам. "
    show Officer Smile
    "Офицер" "Кхм..Кхм.. Просто тяжело устоять перед вашей… доброжелательностью."
    show Milf Night_Smile_pose_3
    "Марина" "Ха-ха-ха!"
    show Milf Night_Passion_pose_3
    "Марина" "Вы такой джентльмен. "
    show Officer Smile
    "Офицер" "Стараюсь… Марина. Могу я обращаться к вам на «ты»? "
    show Milf Night_Smile_pose_3
    "Марина" "Попробуй… те. Хи-хи-хи."
    show Officer Laughs
    "Офицер" "Хех."
    show Officer Normal
    "Офицер" "Вы… То есть, ты сегодня одна дома? "
    show Milf Night_Passion_pose_3
    "Марина" "О да. "
    show Milf Night_Normal_pose_3
    "Марина" "Ну… По крайней мере где [gg] я не знаю. Так что да, пожалуй, что одна. "
    show Officer Normal
    "Офицер" "А ваша приёмная дочь?"
    show Milf Night_Smile_pose_3
    "Марина" "Понятия не имею. Возможно, заперлась в своей комнате и слушает музыку. "
    show Milf Night_Passion_pose_3
    "Марина" "Да не волнуйтесь вы так, офицер, нас никто не потревожит. "
    show Milf Night_Passion_pose_3
    "Марина" "Лучше пройдёмте в мою комнату. Да, там нам будет комфортнее. "
    show Officer Smile
    "Офицер" "Меня дважды просить не надо, хех…"

    show Milf:
        xzoom -1
        easein_cubic 3 xalign 1.75
    show Officer:
        easein_cubic 3 xalign 1.75
    $ renpy.pause(1.5, hard = True)
    show GG GivePhone
    show GG GivePhone at go_from_left


    "[gg]" "Мой выход!"
    show GG:
        easein_cubic 3 xalign 1.75
    show black:
        alpha 0.0
        easein_cubic 2 alpha 1.0
    $ renpy.pause(3, hard = True)
    scene expression 'tests/ep805/bg_blur.png'
    show expression 'cg/christie_root/falos/1_0.png'
    show expression 'cg/christie_root/falos/0.png'

    with Dissolve(.5)
    hide expression 'cg/christie_root/falos/1_0.png'

    call screen christie_root_30_screen(1)
    show expression 'cg/christie_root/falos/1_0.png'
    with None
    show expression 'cg/christie_root/falos/1_1.png':
        xpos 0
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    hide expression 'cg/christie_root/falos/1_0.png'
    call screen christie_root_30_screen(2)
    show expression 'cg/christie_root/falos/0.png':
        easein_cubic 1.7 alpha .0
    show expression 'cg/christie_root/falos/1_1.png':
        xpos 0
        easein_cubic 1.5 alpha .0 xpos -770
    $ renpy.pause(2, hard = True)
    scene expression 'cg/ep85/Marina_Shant_Officer_1.png'
    with my_dissolve





    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Марина" "[gg] мне рассказал о ваших прениях…"
    "Офицер" "О, позволь мне объясниться."
    "Марина" "Попробуйте."
    "Офицер" "Дело в любви, Марина. "
    "Марина" "Да ну?"
    "Офицер" "Слово офицера полиции! – такими речами, поверьте, я не разбрасываюсь. "
    "Офицер" "Я влюбился в тебя с первого взгляда!"
    "Офицер" "Меня будто бы молния пронзила, и я только и мог, что думать о тебе!"
    "Марина" "Хи-хи-хи."
    "Офицер" "А этот твой паренёк… Всего-навсего удачное стечение обстоятельств. "
    "Офицер" "Когда мне посчастливилось его задержать, я истолковал этот случай знаком свыше - возможностью познакомиться с тобой поближе, Марина."
    "Марина" "Звучит слишком романтично, не находите?"
    "Офицер" "Поверь, это чистая правда."
    "Офицер" "Я не желаю зла мальчишке."
    "Офицер" "Да, он очень упёрт, нахален, и считает меня личным врагом."
    "Офицер" "В его возрасте это нормальное явление."
    "Марина" "Он говорит, будто бы вы шантажировали его."
    "Офицер" "Хех..."
    "Офицер" "Это слишком громко звучит! Слишком… инфантильно. "
    "Марина" "Хотите сказать, у него не было причин для вражды?"
    "Офицер" "Признаю, мне пришлось его припугнуть немного. "
    "Офицер" "Но вовсе не для того, чтобы навредить. Я лишь хотел убрать соперника с дороги. "


    "Марина" "Убрать с дороги?!.."
    "Офицер" "В метафорическом смысле, конечно."
    "Марина" "А как же повестка к следователю? "
    "Офицер" "Она настоящая. "
    "Марина" "Значит, всё-таки опасность есть? "
    "Офицер" "Всегда есть опасность, она подстерегает нас на каждом углу…"
    "Офицер" "Но если вы скажете мне «ДА», уверяю тебя, Маришка, я сделаю всё… ВСЁ, что в моих силах, чтобы с вашего парня не упал ни один волос."
    "Офицер" "А уж я могу горы свернуть. "
    "Офицер" "В этом вы можете убедиться лично, хе-хе."


label milf_root_13_test:
    scene expression 'tests/ep805/bg_blur.png'
    show Milf Night_Embarrassment_pose_3
    show Milf Night_Embarrassment_pose_3:
        xalign .1 xzoom -1
    show Officer Smile
    show Officer Smile:
        xalign .9 xzoom -1






    with my_dissolve
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/aerosol-of-my-love-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Офицер" "Марина, позволь я…"
    "Марина" "Нет-нет-нет. Не позволю."
    "Офицер" "Поздно метаться, милая, курок уже возведён и меня не остановить."
    show Milf Night_Angry_pose_3
    with my_dissolve
    "Марина" "Оставьте меня в покое!"
    show Officer Laughs
    with my_dissolve
    "Офицер" "Люблю, когда женщины сопротивляется. "
    "Марина" "Прекратите распускать руки! Я вызову полицию!"
    show Milf:
        easein_cubic 4 xalign .01
    show Officer:
        easein_cubic 4 xalign .5
    "Офицер" "Ха! Ты просто провоцируешь меня!"

    hide Milf
    show expression 'tests/ep805/milf_1.png'
    show Officer Angry:
        easein_cubic .5 xalign .9
    with my_vpunch
    "Марина" "Я говорю «НЕТ!»"
    show Officer:
        xalign .9
    with my_vpunch
    "Офицер" "Эй, что это за херня? Перцовый баллончик? "
    if not renpy.has_label('milf_root_13_ntr'):
        jump milf_root_13_not_ntr
    
    menu:
        "Вмешаться! (Каноничный вариант)" if True:
           jump milf_root_13_not_ntr
        "Не вмешиваться. (NTR-вариант)" if True:
           $ pass










    "[gg]" "{i}Вот блин, я не уверен, что это достаточно убедительная сцена.{/i}"
    "[gg]" "{i}Мне казалось, он будет более напористым.{/i}"
    "[gg]" "{i}Начнёт заламывать ей руки, толкнёт на кровать…{/i}"
    "[gg]" "{i}Надо ещё подождать. Хотя бы чуточку.{/i}"




    "Марина" "{i}Проклятье, перцовый баллончик не сработал!{/i}"


    "Офицер" "Чёрт, женщина, я не собираюсь тебя насиловать!"
    "Офицер" "Ты сама пригласила меня в спальню, и наставляешь на меня перцовый баллончик? Уму не постижимо!"
    "Марина" "Да, вы правы…"
    "Офицер" "Наверное, ты очень переволновалась, милая. Адреналин в крови, чувство страсти…"
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    show Officer Smile
    with my_dissolve
    "Офицер" "Так бывает, когда рядом настоящий мужчина."

    hide expression 'tests/ep805/milf_1.png'
    show expression 'tests/ep805/milf_0.png'
    with my_dissolve
    "Марина" "В-возможно вы и п-правы."
    "Офицер" "Так что на счёт моего вопроса? "
    "Марина" "…."
    "Марина" "Извините, но я не знаю."
    "Марина" "Я хочу быть уверена, что [gg] не будет арестован."
    "Офицер" "Я же сказал – даю слово офицера полиции."
    "Марина" "А как мне знать, что вы не обманите меня? "
    "Офицер" "Я люблю тебя, детка. Обмануть тебя – значит обмануть себя."
    "Марина" "Аххх… Мужчины, вы такие самоуверенные. "
    "Офицер" "Моя работа обязывает меня в этом."
    "Марина" "Но что, если я вас не люблю?.."
    "Офицер" "Обидно слышать это. Обидно до глубины души."
    "Офицер" "С другой стороны, неприступная женщина – ещё более желанная женщина. "
    "Марина" "Хи-хи-хи."
    "Марина" "Буду с вами честна, офицер, я делаю это только ради спасения чужой жизни, не ради себя."
    "Офицер" "Понимаю. Это достойная и очень красивая жертва. "
    "Марина" "Ох…Какой же вы льстец."
    "Офицер" "Мне есть ради кого стараться."
    jump milf_root_13_ntr

label milf_root_13_not_ntr:
    $ ep5_tmp = renpy.call_screen('circle_mini_game_screen', xp = 1500, yp = 300, tm = 10)
    if not ep5_tmp:
        jump milf_root_13_not_ntr






    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Получай, засранец!"

    scene expression 'tests/ep805/bg_blur.png'
    show expression 'tests/ep805/milf_0.png'
    show expression 'tests/ep805/milf_0.png':
        xpos 900
    show expression 'tests/ep805/ment_1.png'
    show expression 'tests/ep805/ment_1.png'
    show expression 'tests/ep805/ment_1.png':
        xpos 1100
    show expression 'tests/ep805/gg_1.png'
    show expression 'tests/ep805/gg_1.png':
        xpos 1250
    show expression 'tests/ep805/gg_0.png'
    show expression 'tests/ep805/gg_0.png':
        xpos 1100


    show expression '#fff'
    with None
    $ renpy.pause(.05, hard = True)
    show expression 'tests/ep805/milf_0.png':
        easein_cubic 4 xpos 650
    show expression 'tests/ep805/ment_1.png':
        easein_cubic 2.5 xpos 900
    show expression 'tests/ep805/gg_1.png':
        alpha 1.0
        easein_cubic 3 alpha .0 xpos 850
    show expression 'tests/ep805/gg_0.png':
        easein_cubic 2.5 xpos 900
    show expression '#fff':
        alpha 1.0
        linear .5 alpha .0




    $ renpy.pause(4, hard = True)


    hide expression 'tests/ep805/ment_1.png'
    hide expression 'tests/ep805/milf_0.png'
    hide expression 'tests/ep805/gg_0.png'
    hide expression 'tests/ep805/gg_1.png'
    show expression 'cg/ep5/jlob/7.png'
    show expression 'tests/ep805/ment_2.png'
    show expression 'tests/ep805/milf_0.png'
    show expression 'tests/ep805/milf_0.png':
        xpos 650
    with vpunch
    $ renpy.pause(.5, hard = True)
    hide expression 'tests/ep805/milf_0.png'
    scene expression 'tests/ep805/bg_blur.png'
    show expression 'cg/ep5/jlob/7.png'
    show expression 'tests/ep805/ment_2.png'
    show Milf Night_Surprise
    show Milf Night_Surprise:
        xalign -.25 xzoom -1
        easein_cubic .5 xalign .1
    
    with my_dissolve
    "Марина" "Какой ужас..."
    hide expression 'tests/ep805/milf_0.png'
    show Milf Night_Surprise
    show Milf Night_Surprise:
        xalign .1 xzoom -1

    "Марина" "Ты что, убил его?"
    hide expression 'cg/ep5/jlob/7.png'
    show GG Skepticism
    show GG Skepticism:
        xalign .9
        xzoom -1
    with my_dissolve
    "[gg]" "К сожалению нет."


    show GG Skepticism
    "[gg]" "Вроде дышит гад. Живучий."
    show Milf Night_Normal
    "Марина" "Выглядит неважно."
    show GG Smile
    "[gg]" "Ха! Слабо сказано. Я ему влепил от всей души."
    show GG Angry
    "[gg]" "Это ждёт всякого, кто решит притронуться к тебе."
    show Milf Night_Normal
    "Марина" "У тебя получилось заснять его домогательства на телефон? "
    show GG Normal
    "[gg]" "Да."
    show Milf Night_Embarrassment_pose_3
    "Марина" "Я боюсь, [gg]. А если он умрёт?"
    show Milf Night_Chagrin
    "Марина" "Боже! Если это произойдёт, наша жизнь покатится в ад."
    show GG Angry
    "[gg]" "А что, по-твоему, я должен был предпринять? Постучать в дверь и вежливо попросить свалить нахер и оставить насс в покое?!"
    show Milf Night_Embarrassment
    "Марина" "Извини, ты прав."

    "Марина" "Я совсем растерялась. Перцовый баллончик не сработал. Офицер стал налегать..."



    show Milf Night_Passion_pose_3
    with my_dissolve
    "Марина" "Ты спас меня, [gg]."
    show GG Normal
    "[gg]" "Я спас нас обоих, Маришка."

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/Erotic.mp3', fadein = 1.5)
    "Марина" "Я люблю тебя, милый. Люблю больше всех на свете."

    show GG Embarrassment
    with my_dissolve
    "Марина" "И, пойду за тобой до конца. "
    show GG Embarrassment
    "[gg]" "Я тоже тебя люблю, Марина."
    show Milf Night_Passion
    "Марина" "Аххх... Как приятно это слышать из твоих уст."
    show GG Angry
    "[gg]" "Пока этот мент заигрывал с тобой, я едва сдерживался, чтобы не скрутить ему голову."

    "Марина" "Догадываюсь. А ещё? Что ещё тебя обуревало?"
    show GG Angry
    "[gg]" "Ещё я злился на тебя!"

    "Марина" "Был в ярости."
    show GG Angry
    "[gg]" "Да. Слушая, как ты кокетничаешь с этим подонком, моё сердце словно пронзали тысяча игл."

    "Марина" "Оу... Столько неприкрытой властности."
    show GG Angry
    "[gg]" " Мне стыдиться нечего. Ты моя женщина."

    "Марина" "Столько бурной ревности…"
    show GG Angry
    "[gg]" "Имею права."
    "Марина" "Тогда чего же ты ждёшь, милый? Хи-хи-хи!"
    show expression '#000' with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show GG Night_Passion:
        xalign .9
    hide expression '#000' with Dissolve(.5)



    show Milf Night_Surprise_pose_3
    with my_dissolve
    "Марина" "Ты что, собираешься это сделать прям здесь?!"
    "[gg]" "Почему нет? Вряд ли этот кусок мяса нам помешает."

    show Milf Night_Passion_pose_3
    with my_dissolve
    "Марина" "Не стану спорить. Я полностью в твоей власти. "
    scene expression 'cg/ep85/tits_1.png'
    with Dissolve(.5)

    $ renpy.pause(99999)
    scene expression 'cg/ep85/tits_2.png'
    with Dissolve(.5)
    $ renpy.pause(99999)

label milf_root_13_gg_milf_sex_1:
    $ add_to_gallery(32)
    scene expression '#000' with Dissolve(.85)

    $ renpy.pause(1.2, hard = True)
    scene expression 'cg/ep85/gg_milf_sex/bg.png'
    show milf_root_13_1_1
    show expression 'cg/ep85/gg_milf_sex/fg.png'
    show GG Invis
    show GG Invis:
        xalign .8
    show Milf Invis
    show Milf Invis:
        xalign .2
    
    with Dissolve(.5)

    $ renpy.pause(.75, hard = True)







    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Значит, тебе нравится быть в роли подчинённой? "
    "Марина" "Мне нравится быть твоей, миленький."
    "[gg]" "Даже если это грозит нам тюремным сроком?"
    "Марина" "Аххх….Разве любовь может быть наказуемой?.."
    "[gg]" "Если рядом лежит полицейский, которого я минуту назад оглушил по башке, то да, хе-хе."
    "Марина" "Плевать на этого бандита в форме, главное, что чувствуем мы по отношению друг к другу."
    "[gg]" "Сладкая ложь…"
    "[gg]" "Я чувствовал горечь, пока ты пыталась осуществлять свой план… "
    "Марина" "Злость придала тебе силы."
    "[gg]" "Если твоя задумка была в этом, то мне лишь остаётся поразиться твоему коварству, Маришка!"
    "Марина" "Охххх…. Я ожидала, что ты можешь приревновать меня, но не думала, что настолько. "
    "Марина" "Я…. Аххх… Я очень довольна результатом."
    "[gg]" "Бесстыжая сучка!"
    "Марина" "Даааа…. О дааа, милый. Я вынудила тебя страдать. "
    "[gg]" "С виду ты типичная домохозяйка, но в тебе таится настоящий демон!"
    "Марина" "Звучит… Аххх…. Охххх… Претенциозно!"

label milf_root_13_gg_milf_sex_2:
    menu:
        "Ускориться" if True:
            $ pass
        "Продолжить в том же темпе" if True:
            $ renpy.pause(9999)
            jump milf_root_13_gg_milf_sex_2
    scene expression 'cg/ep85/gg_milf_sex/bg.png'
    show milf_root_13_1_2
    show expression 'cg/ep85/gg_milf_sex/fg.png'
    show GG Invis
    show GG Invis:
        xalign .8
    show Milf Invis
    show Milf Invis:
        xalign .2
    with Dissolve(.5)

    $ renpy.pause(.75, hard = True)

    "[gg]" "Я слишком люблю тебя, чтобы обижаться на твои шалости. "
    "[gg]" "Один только вид твоего роскошного тела срывает мне крышу. "
    "[gg]" "В такие моменты я готов простить тебе почти всё, кроме измены!"
    "Марина" "Я бы никогда не променяла тебя ни на кого другого… Пусть даже, ты бы сам меня принудил к этому…."
    "Марина" "Лучше смерть…"
    "[gg]" "Да ну?"
    "Марина" "Да-да-да… охххх…. Дааааа!"
    "[gg]" "Меня страшит твоя изощрённость в сексуальных предпочтениях..."
    "[gg]" "Хочется наказать тебя за твою инициативу, хочется трахать тебя грубо, быстро, неуважительно! "
    "[gg]" "Входить в тебя так глубоко и так сильно, чтобы ты и слова сказать не могла, а только блеяла и мычала, стоная в недоумении…"
    "[gg]" "Хитрая, бестыжкая сучка!..."
    "Марина" "Ты… Уффффф, Оххххх…. Повторяешься!.."
    "[gg]" "Ты смеешь мне перечить?"
    "[gg]" "Пора тебя перевоспитать как следует, Маришка!"

label milf_root_13_gg_milf_sex_3:
    menu:
        "Ускориться" if True:
            $ pass
        "Продолжить в том же темпе" if True:
            $ renpy.pause(9999)
            jump milf_root_13_gg_milf_sex_3
    scene expression 'cg/ep85/gg_milf_sex/bg.png'
    show milf_root_13_1_3
    show expression 'cg/ep85/gg_milf_sex/fg.png'
    show GG Invis
    show GG Invis:
        xalign .8
    show Milf Invis
    show Milf Invis:
        xalign .2
    with Dissolve(.5)

    $ renpy.pause(.75, hard = True)

    "Марина" "Ооооо даааа!!! Божее… дааа! Столько вырвавшейся злобы наружу!"
    "Марина" "Теперь я понимаю, как сильно задела твои чувства."
    "Марина" "Всё моё тело лихорадит в оргазмическом угаре, а твой член буквально разрывает меня изнутри! "
    "[gg]" "Хорошо, что до тебя самой это доходит."
    "Марина" "Ты…. Ахххх…. Ммм…. Умеешь доказывать свою точку зрения. "
    "Марина" "Умеешь поставить меня на место… Оххххх! Да-да-да!"
    "[gg]" "Это всё, что ты можешь сказать в своё оправдание?!"
    "[gg]" "Извиняйся!"
    "Марина" "П-п—п-п…. "
    "Марина" "П-п-пожалуйста, извини… М—м-м-м-меня-я-я-я!!! Уфффф…"
    "[gg]" "Звучит так, будто бы мне следует трахнуть тебя ещё жёстче. "
    "Марина" "Дааа.. О даааа…. Я знала, что недостаточно искренняя в своих слова. "
    "Марина" "Я буду молить тебя о прощении всякий раз, когда… Аххх… Аххх… Когда ты пронзаешь меня внутри. "
    "[gg]" "Тогда умоляй!!!"
    "Марина" "П-прости!"
    with my_vpunch
    "Марина" "….. Прости!!!"
    with my_vpunch
    "Марина" "………..Прости-прости-прости!!!"

label milf_root_13_gg_milf_sex_4:
    menu:
        "Кончить" if True:
            $ pass
        "Продолжить в том же темпе" if True:
            $ renpy.pause(9999)
            jump milf_root_13_gg_milf_sex_4
    scene expression 'cg/ep85/gg_milf_sex/bg.png'
    show milf_root_13_1_4
    show expression 'cg/ep85/gg_milf_sex/fg.png'
    show GG Invis
    show GG Invis:
        xalign .8
    show Milf Invis
    show Milf Invis:
        xalign .2
    with Dissolve(.5)

    $ renpy.pause(.75, hard = True)

    "[gg]" "Я…."
    "[gg]" "Получил…."
    "[gg]" "Свою…."
    "[gg]" " Сатисфакцию!!!!"

    scene expression '#fff' with Dissolve(.3)

    $ renpy.pause(1, hard = True)

    scene expression 'cg/ep85/gg_milf_sex/bg.png'
    show expression 'cg/ep85/gg_milf_sex/7.png'
    show milf_root_13_2_2:
        xpos 80
        ypos -80
    show expression 'cg/ep85/gg_milf_sex/fg.png'
    show GG Invis
    show GG Invis:
        xalign .8
    show Milf Invis
    show Milf Invis:
        xalign .2
    with Dissolve(1)
    $ renpy.pause(1.2, hard = True)
    "Марина" "Дааааааааааааааааааааааааааааааааа!!!"
    "Марина" "Потрясающий финал…"
    "[gg]" "Взаимно, Маришка."
    "[gg]" "Фуьюх…. "
    "[gg]" "Я залил в тебя столько спермы… Обалдеть."
    "Марина" "Теперь эта сперма моя, хи-хи-хи."

    "Марина" "Нам нужно одеться, миленький. "

    "[gg]" "Конечно."

    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    scene expression 'tests/ep805/bg_blur.png'
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show GG Normal
    show GG Normal at go_from_left

    show Milf Night_Normal
    show Milf Night_Normal at go_from_right

    "" "*звуки невнятного скулежа*"

    "Марина" "Смотри, кажется полицейский просыпается."
    show GG Angry
    "[gg]" "Ага. Вижу."
    show GG Angry
    "[gg]" "Прогони эту скотину из дома, а я пока вернусь в свою комнату и перекину запись видео Игорю."
    show Milf Night_Normal
    "Марина" "Хорошо."

    show GG:
        easein_cubic 3 xalign 1.85
    $ renpy.pause(2.5, hard = True)
    show Officer Normal
    show Officer Normal at go_from_left

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Офицер" "Что, мать твою, здесь стряслось?! Башка тупо раскалывается на части."
    show Milf Night_Normal
    "Марина" "Ну..."
    show Milf Night_Normal
    "Марина" "Я задаюсь тем же вопросом."
    show Milf Night_Normal
    "Марина" "В какой-то момент вы начали терять сознание и плюхнулись на кровать."
    show Milf Night_Normal
    "Офицер" "В голове звенит так, будто на меня потолок свалился..."

    "Офицер" "Уфф... Кажется, у меня сотрясение."
    show Milf Night_Smile_pose_3
    "Марина" "Это давление, наверное."

    show Officer Agr
    with my_dissolve
    "Офицер" "Давление?! Да что ты такое несёшь?!"
    show Milf Night_Embarrassment_pose_3
    "Марина" "В вашем возрасте это норма."
    show Milf Night_Chagrin_pose_3
    "Марина" "Особенно при дурном питании, тяжёлой, стрессовой работе, хи-хи-хи."

    "Офицер" "Сука..."
    show Milf Night_Angry_pose_3
    "Марина" "Ах вот как!"
    show Milf Night_Angry_pose_3
    "Марина" "Покиньте мой дом, офицер."
    show Milf Night_Angry_pose_3
    "Марина" "Немедленно."

    "Офицер" "Тебе это просто так с рук не сойдёт."

    show Officer:
        easein_cubic 2 xalign 1.85
    $ renpy.pause(2, hard = True)
    scene expression '#000' with Dissolve(.5)
    if not from_gallery_check():

        $ location_now = "Hall"
        $ time.time_now = "night"

        $ Event('milf_root_13_end', location = "City_Home", day_start = time.day_now+1)
        $ new_events = True
        $ milf_root_9_text = __("Конец ивента для эпизода 0.8.5")
    jump main_interface_label

label milf_root_13_end:
    $ events.pop('milf_root_13_end')
    scene expression '#000'
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_157
    show expression 'cg/ep5/Officer_Kick.png'
    with vpunch


    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Офицер" "Это ведь ты меня в тот вечер ударил, пиздюк мелкий?!"
    "Офицер" "Знаю, что ты! По роже твоей нахальной вижу."
    "[gg]" "Руки убери..."
    with my_vpunch
    "Офицер" "Ты чо, псина, забыл кто я такой?"
    with my_vpunch
    "Офицер" "Забыл, что я могу засадить тебя в тюрячку до скончания твоих дней?!"
    "[gg]" "Тогда мне тоже стоит напомнить, что я тот, у кого храняться видео ваших бравых похождений."
    "Офицер" "Что ты мелишь, сосунок? Какие ещё видео?"
    "[gg]" "Кино о мудацком легавом."
    "[gg]" "Там вы, мистер коп, домогаетесь до Марины и в красках хвастаетесь о том, как угрожали мне надумаными делами."




    call show_bg_image_label from _call_show_bg_image_label_161

    show GG Normal
    show GG Normal:
        xalign .5 xzoom -1
        easein_cubic 1 xalign .9
    show Officer Normal
    show Officer Normal:
        xalign .5
        easein_cubic 1 xalign .1
    show GG Think
    with Dissolve(.15)
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Правильное решение. "
    show GG Passion
    "[gg]" "И не советую меня больше трогать, иначе проблемы с законом появятся не только у меня, но и у вас."
    show GG Normal
    "[gg]" "Так же я советую вам побеседовать со следователем, и убедить его лучше разобраться в моём деле."
    show GG WTF
    "[gg]" "Я не требую себя обелить, офицер, но чужие грехи мне приписывать не надо."
    show Officer Normal
    "Офицер" "...."
    show Officer Skepticism
    "Офицер" "Чтож... Поздравляю, [gg]. На табло значится \"ничья\"."
    show Officer Angry
    "Офицер" "Пока что."



    show Officer Angry
    "Офицер" "Но знай, парень. Если это видео когда-нибудь всплывёт… ХОТЬ КОГДА-НИБУДЬ! Я сразу пойму, ЧЬИХ рук это дело."
    show Officer Angry
    "Офицер" " И тогда я являюсь за тобой, сука."


    show Officer Angry
    "Офицер" "В любое место на земле, где бы ты не прятался. В любой норе или под охраной. Мне плевать."
    show Officer Angry
    "Офицер" " Я найду тебя, и придушу собственными руками. "
    show Officer Normal
    "Офицер" "И когда это случится, уверяю тебя, закон – это последнее, о чём я буду думать, когда мои пальцы сдавят твоё моложавое горлице. "
    show Officer Agr
    "Офицер" "Ты меня понял?!"
    show GG Passion
    "[gg]" "Значит, не давайте мне повод."
    show Officer Skepticism
    "Офицер" "Гадёныш…"

    show Officer:
        xzoom -1
        easein_cubic 3 xalign -1.5
    $ renpy.pause(1, hard = True)




    show GG:
        easein_cubic .75 xalign .5

    $ renpy.pause(.8, hard = True)

    show GG Think
    with my_dissolve
    "[gg]" "Проклятье… А он реально псих!"
    show GG Think
    "[gg]" "Стоило бы показать это видео его жене, но последствия меня не прельщают. "
    show GG Think
    "[gg]" "Это видео – залог моей безопасности."
    $ milf_root_9_text = __("Конец ивента для эпизода [version_now]")
    $ unlock_milf_costumes = True
    if hasattr(store, 'christie_root_65_end'):
        call final_act_setup from _call_final_act_setup_3
    
    $ events.pop('milf_root_11', 0)
    $ events.pop('milf_root_13_end', 0)
    $ events.pop('milf_root_13', 0)
    $ events.pop('milf_root_12', 0)
    $ events.pop('milf_root_9', 0)
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc



