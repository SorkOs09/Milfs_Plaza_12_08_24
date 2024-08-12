
image ep5_milf_shower_anim_1_1 = Ani('cg/ep45/shower_3/anim_1/', 4,  float(20)/100, reverse = True, effect=Dissolve(.07), start=1,)

image ep5_milf_shower_anim_1_2 = Ani('cg/ep45/shower_3/anim_1/', 4,  float(15)/100, reverse = True, effect=Dissolve(.5), start=1,)

image ep5_milf_shower_anim_1_3 = Ani('cg/ep45/shower_3/anim_1/', 4,  float(10)/100, reverse = True, effect=None, start=1,)




image ep5_milf_shower_anim_2_1 = Ani('cg/ep45/shower_3/anim_2/', 5,  float(20)/100, reverse = True, effect=Dissolve(0.07), start=1,)

image ep5_milf_shower_anim_2_2 = Ani('cg/ep45/shower_3/anim_2/', 5,  float(12)/100, reverse = True, effect=Dissolve(0.5), start=1,)

image ep5_milf_shower_anim_2_3 = Ani('cg/ep45/shower_3/anim_2/', 5,  float(8)/100, reverse = True, effect=None, start=1,)


image ep5_milf_shower_anim_3_1 = Ani('cg/ep45/shower_3/anim_3/', 2,  1.5, reverse = True, effect=Dissolve(.1), start=1,)



image ep5_milf_shower_anim_4_1 = Ani('cg/ep45/shower_3/anim_4/', 2,  1.5, reverse = True, effect=Dissolve(.1), start=1,)



label ep5_milf_shower:

    if getattr(store, 'unlock_shower_together_2', 0):
        $ mp.unlock_shower_together_2 = True
        $ mp.save()

    if getattr(store, 'unlock_shower_together_3', 0):
        $ mp.unlock_shower_together_3 = True
        $ mp.save()

    if from_gallery_check():
        if mp.unlock_shower_together_2:
            $ unlock_shower_together_2 = True
        if mp.unlock_shower_together_3:
            $ unlock_shower_together_2 = True

    if from_gallery_check():
        $ help_ep5_milf = mp.help_ep5_milf

    menu:
        "Уровень 0" if from_gallery_check():
            jump ep3_milf_14_shower_0
        "Уровень 1" if True:
            $ add_to_gallery(-4)

            $ renpy.music.stop(fadeout=.5)

            $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)








            "[gg]" "Марина, ты в душе?"


            "Марина" "Как ты вообще сюда попал? Я вроде бы закрывала дверь."

            "[gg]" " Хе-хе-хе. Дверь была открыта."


            "Марина" "Как странно… "


            "Марина" "Говори скорее, что ты хотел? "

            "[gg]" "Хотел принять душ."


            "Марина" "Но я уже в кабинке."

            "[gg]" "Да, я знаю."


            "Марина" "…."


            "Марина" "Ну, если хочешь, можешь войти."




            if preferences.language in ('eng', None, 'rus'):
                menu:
                    "Войти" if True:
                        $ pass
                    "Уйти" if True:
                        scene expression '#000' with Dissolve(.5)

                        return



            call ep5_milf_shower_1 from _call_ep5_milf_shower_1


            return





        "Уровень 2" if getattr(store, 'unlock_shower_together_2', 0):




            $ renpy.music.stop(fadeout=.5)

            $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)








            "[gg]" "Марина, ты в душе?"


            "Марина" "Я что, снова забыла закрыть дверь?"

            "[gg]" " Хе-хе-хе. Видимо да."


            "Марина" "Как странно… "


            "Марина" "Ну, если хочешь, можешь войти."
            if preferences.language in ('eng', None, 'rus'):
                menu:
                    "Войти" if True:
                        $ pass
                    "Уйти" if True:
                        scene expression '#000' with Dissolve(.5)

                        return

            call ep5_milf_shower_2 from _call_ep5_milf_shower_2
            return
        "Уровень 3" if getattr(store, 'unlock_shower_together_3', 0):




            $ renpy.music.stop(fadeout=.5)

            $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)






            "[gg]" "Марина, ты в душе?"


            "Марина" "Я что, снова забыла закрыть дверь?"

            "[gg]" " Хе-хе-хе. Видимо да."


            "Марина" "Как странно… "


            "Марина" "Ну, если хочешь, можешь войти."




            if preferences.language in ('eng', None, 'rus'):
                menu:
                    "Войти" if True:
                        $ pass
                    "Уйти" if True:
                        scene expression '#000' with Dissolve(.5)

                        return

            scene expression '#000' with Dissolve(.5)











            call ep5_milf_shower_3 from _call_ep5_milf_shower_3

            return
        "!Уровень 2" if not getattr(store, 'unlock_shower_together_2', 0):
            $ pass
        "!Уровень 3" if not getattr(store, 'unlock_shower_together_3', 0):
           $ pass
        "Назад" if True:
            return
    scene expression '#000' with Dissolve(.5)
    return



label ep5_milf_shower_3:







    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/GGGN.png'

    show expression 'cg/ep45/shower_3/milf_0.png'

    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'


    with Dissolve(.5)



    "Марина" "{i}Я уже не могу сдерживать страсть, что испытываю к своего другу.{/i}"


    "Марина" "{i}Более того, я практически не стыжусь своих развратных мыслей.{/i}"

    "[gg]" "Надеюсь, я тебя не тесню?"


    "Марина" "Нет, вовсе нет."


    "Марина" "…."


    "Марина" "Если честно, крайне необычно тебя видеть здесь…"

    "[gg]" "Хе-хе… "

    "[gg]" "Я тоже чувствую себя неловко."


    "Марина" "Он жадно глазеет на моё мокрое, горячее тело…"


    "Марина" "Нельзя его винить за это. Я ведь сама его спровоцировала"


    "Марина" "Ну, раз уж ты здесь, может, я помогу тебе помыть спинку?.."


    if preferences.language in ('eng', None, 'rus'):
        menu:
            "Согласиться." if True:
                jump ep5_milf_shower_3_menu_tmp
            "Предложить помыть её саму." if True:

                $ pass

    else:
        menu:
            "Да" if True:
                jump ep5_milf_shower_3_menu_tmp
            "Нет" if True:

                $ pass


















    "[gg]" "А могу ли я сам предложить тебе эту же услугу?"


    "Марина" "О да…"


    "Марина" "Я ждала этих слов."


    "Марина" "Я не против."


    "Марина" "Если, конечно, это тебя не смутит. "

    "[gg]" "Я постараюсь держать себя в руках."


    "Марина" "Нет, этого делать ему точно не надо."




    scene expression 'cg/ep45/shower_3/bg.png'



    show expression 'cg/ep45/shower_3/or1.png'

    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    with Dissolve(.5)


    "Марина" "Тогда начинай."

    "[gg]" "Д-да… Сейчас…"


    "Марина" "{i}Ой, кажется я слишком поторопилась. {/i}"


    "Марина" "{i}Он жутко застеснялся от моей вызывающей позы.{/i}"


    "Марина" "{i}Такое ощущение, что он сейчас наброситься на меня.{/i}"


    "Марина" "{i}Надеюсь на это…{/i}"

    "[gg]" "{i}Мой член касается её попки!!!{/i}"




    "Марина" "{i}Вау. Какая у него высокая моральная устойчивость.{/i}"






    "[gg]" "{i}Роскошное тело Марины сводит меня с ума.{/i}"

    "[gg]" "{i}Я не могу противиться ей…{/i}"

    "[gg]" "{i}Ещё мгновение, и я сам её трахну. {/i}"



    scene expression 'cg/ep45/shower_3/bg.png'



    show expression 'cg/ep45/shower_3/or2.png'

    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    with Dissolve(.5)



    "Марина" "{i}Пожалуй, мне всё же стоит сделать первый шаг. {/i}"




    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/or2.png'
    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'
    show expression 'cg/ep45/shower_3/anim_1_bg_2.png'
    show expression 'cg/ep45/shower_3/anim_2/1.png'


    with Dissolve(.5)


    "[gg]" "Я…"

    "Марина" "Хочешь мою попочку, да?"

    "[gg]" "Больше всего на свете!"

    "Марина" "Тогда начинай двигаться, милый"



    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/or2.png'


    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'
    show expression 'cg/ep45/shower_3/anim_1_bg_2.png'
    show ep5_milf_shower_anim_2_1
    with Dissolve(.5)



    "[gg]" "Я люблю тебя, Маришка!"


    "Марина" "О да, я знаю."


    "Марина" "В такие моменты все мужчины любят своих женщин"

    "[gg]" "Но я действительно люблю тебя!"


    "Марина" "Это взаимно, милый."


    "Марина" "Продолжать любить меня в попку."


    "Марина" "Я так давно этого хотела…"

    "[gg]" "Да-да-да!"


    "Марина" "Моё тело пылает от удовольствия."


    "Марина" "Входи в меня как можно глубже. "


    "Марина" "Я обожаю, когда ты растягиваешь дырочку моего ануса своим гигантским членом!"


    "Марина" "Оххххх…"


    "Марина" "Аахххх….."


    "Марина" "Ещё-ещё-ещё!"





label ep5_milf_shower_3_menu_1:
    window hide
    $ renpy.pause(9999)
    menu:
        "Продолжить." if True:
            jump ep5_milf_shower_3_menu_1
        "Ускориться." if True:
            pass







    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/or2.png'

    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    show expression 'cg/ep45/shower_3/anim_1_bg_2.png'
    show ep5_milf_shower_anim_2_2

    with Dissolve(.5)









    "[gg]" "Трахать тебя в задницу настоящее блаженство!"


    "Марина" "О дааа, ещё бы!"


    "Марина" "Теперь моя задница принадлежит тебе. "


    "Марина" "Можешь использоваться её всегда, когда пожелаешь. "

    "[gg]" "Маришка!!!"


    "Марина" "Оххххх…."


    "Марина" "Я чувствую, как твой член увеличивается во мне ещё больше."


    "Марина" "Аххх… Как же глубоко ты проникаешь."


    "Марина" "От этого ощущения я испытываю череду невероятных оргазмов!"

    "[gg]" "Сейчасс я тоже собираюсь кое-что испытать!.."

    $ ep5_milf_shower_3_menu_2 = 2
label ep5_milf_shower_3_menu_2:
    window hide
    $ renpy.pause(9999)
    menu:
        "Хочу продолжения" if True:
            jump ep5_milf_shower_3_menu_2
        "Уменьшить скорость" if ep5_milf_shower_3_menu_2 != 1:
            $ ep5_milf_shower_3_menu_2 -= 1

            scene expression 'cg/ep45/shower_3/bg.png'


            show expression 'cg/ep45/shower_3/or2.png'

            show expression 'cg/ep45/shower_3/fog.png'
            show expression 'cg/ep45/shower_3/shadow.png'

            show expression 'cg/ep45/shower_3/anim_1_bg_2.png'
            if ep5_milf_shower_3_menu_2 == 1:

                show ep5_milf_shower_anim_2_1

            if ep5_milf_shower_3_menu_2 == 2:

                show ep5_milf_shower_anim_2_2

            if ep5_milf_shower_3_menu_2 == 3:

                show ep5_milf_shower_anim_2_3

            with Dissolve(.5)
            jump ep5_milf_shower_3_menu_2

        "Увеличить скорость" if ep5_milf_shower_3_menu_2 != 3:
            $ ep5_milf_shower_3_menu_2 += 1


            scene expression 'cg/ep45/shower_3/bg.png'


            show expression 'cg/ep45/shower_3/or2.png'

            show expression 'cg/ep45/shower_3/fog.png'
            show expression 'cg/ep45/shower_3/shadow.png'

            show expression 'cg/ep45/shower_3/anim_1_bg_2.png'
            if ep5_milf_shower_3_menu_2 == 1:

                show ep5_milf_shower_anim_2_1

            if ep5_milf_shower_3_menu_2 == 2:

                show ep5_milf_shower_anim_2_2

            if ep5_milf_shower_3_menu_2 == 3:

                show ep5_milf_shower_anim_2_3

            with Dissolve(.5)
            jump ep5_milf_shower_3_menu_2
        "Кончить" if True:



            $ pass

    if hasattr(store, 'ep5_milf_shower_3_menu_2'):
        $ del ep5_milf_shower_3_menu_2

    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/or2.png'

    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    show expression 'cg/ep45/shower_3/anim_1_bg_2.png'
    show ep5_milf_shower_anim_2_3

    with Dissolve(.5)




















    "Марина" "Давай, кончи в меня всё, что у тебя накопилось."


    "Марина" "Хочу, чтобы из моей дырочки стекала твоя горячая белая сперма. "

    "[gg]" "Ещё чуть-чуть…"

    "[gg]" "Да-да-да!!!"





    "[gg]" "Кончаааююююю!!!!..."

    scene expression '#FFF' with Dissolve(.3)

    $ renpy.pause(.5, hard = True)

    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/or2.png'

    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    show expression 'cg/ep45/shower_3/anim_1_bg_2.png'

    show expression 'cg/ep45/shower_3/anim_2/end.png'

    with Dissolve(1)

    "[gg]" "О даааа…"


    "Марина" "Ты моё чудо, [gg]."











    "[gg]" "Как ты и просила. "

    "[gg]" "Стекающая сперма."


    "Марина" "Ах, милаш. Ты мой развратник. "

    return














label ep5_milf_shower_2:






    scene expression '#000' with Dissolve(.5)





    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/GGGN.png'

    show expression 'cg/ep45/shower_3/milf_0.png'



    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    with Dissolve(.5)
    "Марина" "{i}Дура, зачем ты пригласила своего друга к себе в душ?!{/i}"


    "Марина" "{i}Я что, совсем ополоумела от одиночества?{/i}"

    "[gg]" "Надеюсь, я тебя не тесню?"


    "Марина" "Нет, вовсе нет."


    "Марина" "…."


    "Марина" "Если честно, крайне необычно тебя видеть здесь…"

    "[gg]" "Хе-хе… "

    "[gg]" "Я тоже чувствую себя неловко."


    "Марина" "Он жадно глазеет на моё мокрое, горячее тело…"


    "Марина" "Нельзя его винить за это. Я ведь я сама его спровоцировала"


    "Марина" "Ну, раз уж ты здесь, может, я помогу тебе помыть спинку?.."

    "[gg]" "Эм… "

    "[gg]" "Да, наверное. Это будет мило с твоей стороны."


label ep5_milf_shower_3_menu_tmp:



    scene expression 'cg/ep45/shower_3/bg.png'



    show expression 'cg/ep45/shower_3/anim_3/1.png'
    show expression 'cg/ep45/shower_3/GGGN_2.png'


    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    with Dissolve(.5)

    "[gg]" "Забавно."


    "Марина" "Что?"

    "[gg]" "Говорю, что это забавно."

    "[gg]" "Помню, как ты мыла меня, когда я был совсем маленьким."



    "[gg]" "Кто бы мог подумать, что спустя столько лет, это снова случится."


    scene expression 'cg/ep45/shower_3/bg.png'


    show ep5_milf_shower_anim_3_1
    show expression 'cg/ep45/shower_3/GGGN_2.png'



    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    with Dissolve(.5)

    "Марина" "Да…."


    "Марина" "Но ведь в этом же нет ничего предосудительного, верно? "

    "[gg]" "Конечно. Мы просто моемся вместе."


    "Марина" "Вместе…"

    "[gg]" "А?..."


    "Марина" "Да это я так. Не обращай внимание."


    "Марина" "{i}Я вся дрожу от мысли, что массирую спину голого парня.{/i}"


    "Марина" "{i}Его член уже так возбуждён…{/i}"


    "Марина" "{i}Представляю, как он сейчас напряжён, чтобы не обкончать здесь всё.{/i}"




    "Марина" "{i}Посмотрим, как он отреагирует, если я опущусь чуть ниже…{/i}"














    "[gg]" "…."


    "Марина" "{i}Он ничего не сказал.{/i}"


    "Марина" "{i}То ли он впал в ступор от стыда, то ли замер, чтобы не спугнуть меня.{/i}"



















    "Марина" "[gg]…"

    "[gg]" "Да?"


    "Марина" "Тебе нравится? Или мне стоит продолжить мыть тебе спинку?.."

    "[gg]" "М-мне очень нравится."

    "[gg]" "Мой меня так, как считаешь нужным. "


    "Марина" "Это я его совращаю или он меня?"


    "Марина" "Лучше бы он сказал «нет»."


    "Марина" "Теперь меня не остановить…"






    "Марина" "Повернись, пожалуйста."

    "[gg]" "Повернуться?.."


    "Марина" "Да, мне же нужно помыть тебя и спереди. "



    "[gg]" "Л-логично…"


    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/anim_4/1.png':
        xpos -100

    show expression 'cg/ep45/shower_3/shock.png':
        xpos -100

    show expression 'cg/ep45/shower_3/GGGN.png'


    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    with Dissolve(.5)

    "Марина" "Большой, дрожащий от возбуждения…"


    "Марина" "Мочалка, наверное, будет грубовата в этом случае."

    "[gg]" "И что же делать? "


    "Марина" "Есть у меня один план, но тебе нужно закрыть глаза и облокотиться об стенку. "

    "[gg]" "Хм…"

    "[gg]" "Ладно."



    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/anim_1_bg.png'




    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    with Dissolve(.5)




    "Марина" "Не подглядывай."

    "[gg]" "И не думал."



    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/anim_1_bg.png'





    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'
    show expression 'cg/ep45/shower_3/anim_1_bg_2.png':
        xpos 1134
        ypos -39
    show ep5_milf_shower_anim_1_1

    with my_dissolve




    "Марина" "У меня получается?"

    "[gg]" "П-потрясающее чувство."

    "[gg]" "Это что, твои…?"


    "Марина" "Груди. Да."

    "[gg]" "Ты ещё никогда так не мыла меня таким образом."


    "Марина" "Знаю…"


    "Марина" "Ты же не против?"

    "[gg]" "Теперь я хочу мыться исключительно так."


    "Марина" "Ахххх…."

    "[gg]" "Раз уж я догадался, что это такое, я могу открыть глаза?"


    "Марина" "Нет, не можешь."



    "[gg]" "Тогда, пожалуйста, будь несколько… быстрой."


    "Марина" "Хорошо."





    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/anim_1_bg.png'


    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    show expression 'cg/ep45/shower_3/anim_1_bg_2.png':
        xpos 1134
        ypos -39

    show ep5_milf_shower_anim_1_2
    with my_dissolve



    "Марина" "Вот так, да?"

    "[gg]" "Да, именно так…"


    "Марина" "Я знала, что тебе понравиться такой способ."

    "[gg]" "Ты всегда знаешь о моих предпочтениях лучше меня самого."


    "Марина" "Я всё знаю о своём лучшем друге. "

    "[gg]" "Оххх…."

    "[gg]" "Это прекрасно."

    "[gg]" "Меня охватывает неописуемая радость. "


    "Марина" "Хи-хи-хи."

    "[gg]" "О даааа…."


    "Марина" "Полагаю, катарсис уже рядом."

    "[gg]" "Почти…."








    $ ep5_milf_shower_3_menu_3 = 2
label ep5_milf_shower_3_menu_3:
    window hide
    $ renpy.pause(9999)
    menu:
        "Хочу продолжения" if True:
            jump ep5_milf_shower_3_menu_3
        "Уменьшить скорость" if ep5_milf_shower_3_menu_3 != 1:
            $ ep5_milf_shower_3_menu_3 -= 1






            scene expression 'cg/ep45/shower_3/bg.png'


            show expression 'cg/ep45/shower_3/anim_1_bg.png'


            show expression 'cg/ep45/shower_3/fog.png'
            show expression 'cg/ep45/shower_3/shadow.png'

            show expression 'cg/ep45/shower_3/anim_1_bg_2.png':
                xpos 1134
                ypos -39

            if ep5_milf_shower_3_menu_3 == 1:

                show ep5_milf_shower_anim_1_1
            elif ep5_milf_shower_3_menu_3 == 2:

                show ep5_milf_shower_anim_1_2
            elif ep5_milf_shower_3_menu_3 == 3:

                show ep5_milf_shower_anim_1_3
            with Dissolve(.5)

            jump ep5_milf_shower_3_menu_3

        "Увеличить скорость" if ep5_milf_shower_3_menu_3 != 3:
            $ ep5_milf_shower_3_menu_3 += 1





            scene expression 'cg/ep45/shower_3/bg.png'


            show expression 'cg/ep45/shower_3/anim_1_bg.png'

            show expression 'cg/ep45/shower_3/fog.png'
            show expression 'cg/ep45/shower_3/shadow.png'

            show expression 'cg/ep45/shower_3/anim_1_bg_2.png':
                xpos 1134
                ypos -39

            if ep5_milf_shower_3_menu_3 == 1:

                show ep5_milf_shower_anim_1_1
            elif ep5_milf_shower_3_menu_3 == 2:

                show ep5_milf_shower_anim_1_2
            elif ep5_milf_shower_3_menu_3 == 3:

                show ep5_milf_shower_anim_1_3

            with Dissolve(.5)

            jump ep5_milf_shower_3_menu_3
        "Кончить" if True:



            $ pass





    if hasattr(store, 'ep5_milf_shower_3_menu_3'):
        $ del ep5_milf_shower_3_menu_3








    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/anim_1_bg.png'


    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    show expression 'cg/ep45/shower_3/anim_1_bg_2.png':
        xpos 1134
        ypos -39

    show ep5_milf_shower_anim_1_3
    with Dissolve(.5)








    "[gg]" "Я уже на грани, Мариночка…"


    "Марина" "Давай, мой хороший, выплесни своё молочко на меня. "

    "[gg]" "Аааааааххх!!!"

    scene expression '#fff' with Dissolve(.3)

    $ renpy.pause(.2, hard = True)

    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/anim_1_bg.png'


    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    show expression 'cg/ep45/shower_3/anim_1_bg_2.png':
        xpos 1134
        ypos -39
    show expression 'cg/ep45/shower_3/anim_1/end.png'
    with Dissolve(1.5)


    $ renpy.pause(999)


    "Марина" "Ого, как много."


    "Марина" "И такая вкусная…"

    "[gg]" "Я обожаю купаться с тобой. "


    "Марина" "Оу…"







    "[gg]" "C-спасибо. "


    "Марина" "Я не буду против, если ты снова захочешь принять душ вместе."

    "[gg]" "Я приду, обязательно приду. "


    "Марина" "Он придёт…. Конечно же он придёт."


    return























label ep5_milf_shower_1:






    scene expression '#000' with Dissolve(.5)





    scene expression 'cg/ep45/shower_3/bg.png'


    show expression 'cg/ep45/shower_3/GGGN.png'

    show expression 'cg/ep45/shower_3/milf_0.png'


    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    with Dissolve(.5)








    "Марина" "{i}Дура, зачем ты пригласила своего друга к себе в душ?!{/i}"


    "Марина" "{i}Я что, совсем ополоумела от одиночества? {/i}"

    "[gg]" "Надеюсь, я тебя не тесню?"


    "Марина" "Нет, вовсе нет."


    "Марина" "…."


    "Марина" "Если честно, крайне необычно тебя видеть здесь…"

    "[gg]" "Хе-хе… "

    "[gg]" "Я тоже чувствую себя неловко."


    "Марина" "Он жадно глазеет на моё мокрое, горячее тело…"


    "Марина" "Нельзя его винить за это. Я ведь я сама его спровоцировала"


    "Марина" "Ну, раз уж ты здесь, может, я помогу тебе помыть спинку?.."

    "[gg]" "Эм… "

    "[gg]" "Да, наверное. Это будет мило с твоей стороны."




    scene expression 'cg/ep45/shower_3/bg.png'



    show expression 'cg/ep45/shower_3/anim_3/1.png'

    show expression 'cg/ep45/shower_3/GGGN_2.png'

    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    with Dissolve(.5)

    "[gg]" "Забавно."


    "Марина" "Что?"

    "[gg]" "Говорю, что это забавно."

    "[gg]" "Помню, как ты мыла меня, когда я был совсем маленьким."



    "[gg]" "Кто бы мог подумать, что спустя столько лет, это снова случится."


    scene expression 'cg/ep45/shower_3/bg.png'



    show ep5_milf_shower_anim_3_1

    show expression 'cg/ep45/shower_3/GGGN_2.png'

    show expression 'cg/ep45/shower_3/fog.png'
    show expression 'cg/ep45/shower_3/shadow.png'

    with Dissolve(.5)


    "Марина" "Да…."


    "Марина" "Но ведь в этом же нет ничего предосудительного, верно? "

    "[gg]" "Конечно. Мы просто моемся вместе."


    "Марина" "Вместе…"

    "[gg]" "А?..."


    "Марина" "Да это я так. Не обращай внимание."


    "Марина" "{i}Я вся дрожу от мысли, что массирую спину голого парня.{/i}"


    "Марина" "{i}Его член уже так возбуждён…{/i}"


    "Марина" "{i}Представляю, как он сейчас напряжён, чтобы не обкончать здесь всё.{/i}"



    "Марина" "{i}Ну всё, стоп. Прекрати думать о его члене. {/i}"


    "Марина" "{i}Пожалуй, я достаточно потрудилась.{/i} "











    "[gg]" "C-спасибо. "


    "Марина" "Бедняжка. Его член так возбуждён, что вот-вот взорвётся от удержания. "


    "Марина" "Я не буду против, если ты снова захочешь принять душ вместе."

    "[gg]" "Я приду, обязательно приду. "


    "Марина" "Он придёт…. Конечно же он придёт."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
