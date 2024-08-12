image milf_titsjob:
    'images/cg/ep1/milf_sleep/milf_tits_3.png' with Dissolve(.2)
    .5
    'images/cg/ep1/milf_sleep/milf_tits_4.png' with Dissolve(.2)
    .5
    'images/cg/ep1/milf_sleep/milf_tits_3.png' with Dissolve(.2)
    .5
    'images/cg/ep1/milf_sleep/milf_tits_4.png' with Dissolve(.2)
    .5
    'images/cg/ep1/milf_sleep/milf_tits_3.png' with Dissolve(.2)
    .5
    'images/cg/ep1/milf_sleep/milf_tits_4.png' with Dissolve(.2)
    1
    repeat
image gg_milf_masturbation:
    'images/cg/ep1/milf_sleep/gg_milf_masturbation/1.png' with Dissolve(.5)
    .5
    'images/cg/ep1/milf_sleep/gg_milf_masturbation/2.png' with Dissolve(.5)
    1
    repeat

image gg_milf_fingers:
    'images/cg/ep1/milf_sleep/gg_milf_fingers/1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/2.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/2.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/2.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/2.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/2.png' with Dissolve(.2)
    2
    repeat

image gg_milf_fingers_2:
    'images/cg/ep1/milf_sleep/gg_milf_fingers/3.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/4.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/3.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/4.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/3.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/4.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/3.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/4.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/3.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_fingers/4.png' with Dissolve(.2)
    2
    repeat

image gg_milf_cunnilingus:
    'images/cg/ep1/milf_sleep/gg_milf_cunnilingus/1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_cunnilingus/2.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_cunnilingus/1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_cunnilingus/2.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_cunnilingus/1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_cunnilingus/2.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_cunnilingus/1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_cunnilingus/2.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_cunnilingus/1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/gg_milf_cunnilingus/2.png' with Dissolve(.2)
    2
    repeat

image gg_milf_ass_dick:
    'images/cg/ep1/milf_sleep/Sleep_ass_dick_1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/Sleep_ass_dick_2.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/Sleep_ass_dick_1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/Sleep_ass_dick_2.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/Sleep_ass_dick_1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/Sleep_ass_dick_2.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/Sleep_ass_dick_1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/Sleep_ass_dick_2.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/Sleep_ass_dick_1.png' with Dissolve(.2)
    1
    'images/cg/ep1/milf_sleep/Sleep_ass_dick_2.png' with Dissolve(.2)
    2
    repeat

label milf_sleep_label:
    $ Hide('main_interface')()
    $ Hide('icons_interface')()

    with Dissolve(.5)
    if not getattr(store, 'milf_drunk', False):

        '[gg]' "У неё слишком чуткий сон. Она проснётся."
        '[gg]' "Возможно, если она выпьет вина, то будет спать крепче."
        jump main_interface_label


    play music 'audio/Erotic.mp3' fadein 1.5
label milf_sleep_label_whmi:
    scene expression 'images/cg/ep1/milf_sleep/milf_sleep.png'
    with Dissolve(.5)
    $ renpy.pause(1, hard = True)
    $ add_to_gallery(6)
    menu:
        "1. Стянуть одеяло." if True:
            scene expression 'images/cg/ep1/milf_sleep/milf_sleep_adult.png' with Dissolve(.5)
            $ renpy.pause(1, hard = True)
            if not from_gallery_check():
                $ Event('stump_milf_sleep', 'Bedroom', 'stump_milf_sleep', time = ['night'])

            menu:
                "1. Играть с сиськами." if True:
                    jump milf_sleep_tits
                "2. Играть с задницей." if True:



                    jump milf_sleep_ass
                "3. Играть с киской." if True:
                    jump milf_sleep_pussy
                "4. Уйти." if True:
                    

                    $ location_now = 'Hall'
        "2. Уйти." if True:
            
            $ location_now = 'Hall'


    $ location_now = 'Hall'

    scene expression '#000' with Dissolve(.5)


    jump main_interface_label



label milf_sleep_titjob_label:
    scene milf_titsjob with Dissolve(.5)

    show shadow_full
    with my_dissolve
    "Марина" "{i}О боже... Что он делает{/i}?!"
    "Марина" "{i}Какой отчаянный  поступок с его стороны{/i}..."
    "Марина" "{i}Нет, это неправильно. Следует остановиться{/i}."
    "Марина" "{i}Но я продолжаю неподвижно лежать и делать вид, что сплю{/i}."
    "Марина" "{i}Запах его горячего члена сводит меня с ума{/i}."
    "Марина" "{i}Я обескуражена, но... почему-то не силах сказать «нет»{/i}."
    "Марина" "{i}Мне очень хочется, чтобы он продолжал{/i}."
    "Марина" "{i}И, возможно, зашёл чуточку дальше{/i}..."
    hide shadow_full
    with my_dissolve
    '[gg]' "Я всю жизнь мечтал это сделать с тобой, подруга."
    '[gg]' "Твои груди такие большие и сочные."
    '[gg]' "И твоё тяжёлое дыхание… Оно участилось. Тебе нравится, правда?"
    '[gg]' "Уверен, что нравится."
    '[gg]' "Твой сладкий сон, твоя беспомощность возбуждают меня ещё сильнее."
    '[gg]' "Главное, чтобы ты не проснулась раньше времени…"
    #call milf_sleep_end
    menu:
        "1. Продолжать." if True:
            jump milf_sleep_titjob_label
        "2. Кончить." if True:
            $ pass



    scene expression 'cg/ep1/milf_sleep/milf_tits_5.png' with Dissolve(.7)
    $ renpy.pause(.5, hard = True)
    scene expression 'cg/ep1/milf_sleep/milf_tits_6.png' with Dissolve(.3)
    $ renpy.pause(.7, hard = True)
    '[gg]' "О дааааа!!!..."
    '[gg]' "Ты лучшая, подруга! "
    '[gg]' "Мне определённо стоит явиться снова."
    $ location_now = 'Hall'
    $ milf_drunk   = False

    scene black with Dissolve(.5)


    jump main_interface_label


label milf_sleep_tits:
    scene expression 'images/cg/ep1/milf_sleep/milf_tits_1.png' with Dissolve(.5)
    menu:
        "1. Стянуть одежду." if True:
            scene expression 'images/cg/ep1/milf_sleep/milf_tits_2.png' with Dissolve(.5)
            menu:
                "1. Член между сисек." if True:
                    jump milf_sleep_titjob_label
                "2. Предыдущее действие." if True:


                    jump milf_sleep_tits
                "3. Уйти." if True:
                    
                    jump milf_sleep_label_whmi
        "2. Уйти." if True:



            jump milf_sleep_label_whmi

label milf_sleep_ass:
    scene expression 'images/cg/ep1/milf_sleep/milf_ass_1.png' with Dissolve(.5)
    menu:
        "1. Стянуть одежду." if True:

            scene expression 'images/cg/ep1/milf_sleep/milf_ass_2.png' with Dissolve(.5)

            menu:
                "1. Стянуть трусики наполовину." if True:
                    scene expression 'images/cg/ep1/milf_sleep/milf_ass_3.png' with Dissolve(.5)
                    menu:
                        "1. Дрочить." if True:
                            jump milf_sleep_masturbation
                        "2. Уйти." if True:
                            jump milf_sleep_ass
                "2. Стянуть трусики полностью." if True:

                    scene expression 'images/cg/ep1/milf_sleep/milf_ass_4.png' with Dissolve(.5)
                    menu:
                        "1. Дрочить." if True:
                            jump milf_sleep_masturbation
                        "2. Член между ягодиц" if True:
                            jump milf_sleep_ass_dick
                        "3. Уйти." if True:
                            jump milf_sleep_ass
                "3. Дрочить." if True:
                    jump milf_sleep_masturbation
                "4. Уйти." if True:
                    jump milf_sleep_label_whmi
        "2. Уйти." if True:
            jump milf_sleep_label_whmi





label milf_sleep_masturbation:
    show gg_milf_masturbation with Dissolve(.5)
    "Марина" "{i}[player_name] такой извращенец.{/i}"
    "Марина" "{i}Ему достаточно и того, что я сплю, только бы лицезреть на моё полуобнажённое тело.{/i}"
    "Марина" "{i}Стыдно признаться, но я лишь упиваюсь чувством его похоти.{/i}"
    "Марина" "{i}Главное не шевелиться, иначе он может испугаться и больше не прийти.{/i}"

    '[gg]' "У тебя роскошная задница, Марина."
    '[gg]' "Такая мягкая и горячая. Словно создана для ублажения моего пульсирующего члена."
    '[gg]' "И вот я здесь, чтобы взять причитающееся и насладиться наградой."
    '[gg]' "Стоило бы шлёпнуть тебя по заднице. Услышав, как ты вскрикнешь от неожиданности и застанешь от удовольствия. "
    '[gg]' "Аххх!!! Нельзя…"
    '[gg]' "Тогда ты проснёшься. Запаникуешь и наверняка захочешь выгнать меня. "
    '[gg]' "Но когда-нибудь это случится. Я не выдержу и сделаю это."
    '[gg]' "Вид твоей мясистой попки вызывает во мне самые извращённые мысли."
    #call milf_sleep_end
    menu:
        "1. Продолжать." if True:
            jump milf_sleep_masturbation
        "2. Кончить." if True:
            $ pass
    hide gg_milf_masturbation
    show expression 'cg/ep1/milf_sleep/gg_milf_masturbation/2.png'
    show expression 'cg/ep1/milf_sleep/gg_milf_masturbation_sperm/1.png'
    with Dissolve(.3)
    $ renpy.pause(.3, hard = True)
    hide expression 'cg/ep1/milf_sleep/gg_milf_masturbation_sperm/1.png'
    show expression 'cg/ep1/milf_sleep/gg_milf_masturbation_sperm/2.png'
    with Dissolve(.3)
    $ renpy.pause(.3, hard = True)
    hide expression 'cg/ep1/milf_sleep/gg_milf_masturbation_sperm/2.png'
    show expression 'cg/ep1/milf_sleep/gg_milf_masturbation_sperm/3.png'
    with Dissolve(.3)
    $ renpy.pause(.3, hard = True)
    hide expression 'cg/ep1/milf_sleep/gg_milf_masturbation_sperm/3.png'
    show expression 'cg/ep1/milf_sleep/gg_milf_masturbation_sperm/4.png'
    with Dissolve(.3)
    $ renpy.pause(1, hard = True)

    '[gg]' "О дааааа!!!..."
    '[gg]' "Ты лучшая, подруга! Уверен, я приду ещё."
    $ location_now = 'Hall'
    $ milf_drunk   = False
    scene black with Dissolve(.5)


    jump main_interface_label


label milf_sleep_pussy:
    $ pussy = 0
    scene expression 'cg/ep1/milf_sleep/milf_vagina_1.png' with Dissolve(.5)


    menu:
        "1. Стянуть одежду." if True:
            $ pass
        "2. Уйти." if True:
            jump milf_sleep_label_whmi

    scene expression 'cg/ep1/milf_sleep/milf_vagina_2.png' with Dissolve(.5)
    menu:
        "1. Стянуть трусики" if True:
            $ pass
        "2. Уйти." if True:
            jump milf_sleep_pussy
label milf_sleep_pussy_2:
    scene expression 'cg/ep1/milf_sleep/milf_vagina_3.png' with Dissolve(.5)
    menu:
        "1. Воспользоваться пальцем." if True:
            scene gg_milf_fingers with Dissolve(.5)
            $ pussy = 1
        "2. Воспользоваться языком." if True:
            scene gg_milf_cunnilingus with Dissolve(.5)
            $ pussy = 2
        "3. Вернуться." if True:
            jump milf_sleep_pussy
    show shadow_full with my_dissolve
    "Марина" "{i}Охх... Я давно этого ждала."
    "Марина" "{i}Наконец-то он решился на самый смелый шаг в своих ночных вылазках.{/i}"
    "Марина" "{i}Давай, малыш, дерзай, я не проч твои щекотливых стараний...{/i}"
    "Марина" "{i}Боже.. мне так хорошо, что я чуть было незапищала от восторга, но нет, нельзя. Он не должен ничего заподозрить.{/i}"
    hide shadow_full with my_dissolve
    '[gg]' "Какой у тебя красивый клитор, подруга."
    '[gg]' "И мокрое, горячее влагалище."
    '[gg]' "Раньше я мог только мечтать, чтобы увидеть тебя голой. "
    '[gg]' "Но теперь, когда ты ни о чём не подозреваешь, я наслаждаюсь богатством твоего сексуального тела. "
    '[gg]' "Не знаю, насколько правильно так поступать с тобой. "
    '[gg]' "Но это всецело твоя вина. Ты будоражишь моё сознание, Марина. Твоя мягкая, тугая киска сводит меня с ума."
    '[gg]' "Я могу ублажать тебя вечно…"
    #call milf_sleep_end
    menu:
        "1. Продолжать." if True:
            jump milf_sleep_pussy_2
        "2. Кончить." if True:
            $ pass



    if pussy == 1:
        scene gg_milf_fingers_2 with Dissolve(.5)
    elif True:
        scene expression 'images/cg/ep1/milf_sleep/gg_milf_cunnilingus/3.png' with Dissolve(.5)
    '[gg]' "Обалденно!!!"
    '[gg]' "Я обожаю твои женские соки… "
    $ location_now = 'Hall'
    $ milf_drunk   = False

    scene black with Dissolve(.5)


    jump main_interface_label



label milf_sleep_ass_dick:
    scene gg_milf_ass_dick with Dissolve(.5)
    show shadow_full
    with my_dissolve
    "Марина" "{i}Как же он обожает мои булочки...{/i}"
    "Марина" "{i}Мой сладкий сон лишь поддевает его приходить ко мне чаще и совершать всё более дерзкие поступки.{/i}"
    "Марина" "{i}Какой коварный, милый мальчик.{/i}"
    hide shadow_full
    with my_dissolve

    '[gg]' "У тебя роскошная задница, Марина."
    '[gg]' "Такая мягкая и горячая. Словно создана для ублажения моего пульсирующего члена."
    '[gg]' "И вот я здесь, чтобы взять причитающееся и насладиться наградой."
    '[gg]' "Стоило бы шлёпнуть тебя по заднице. Услышав, как ты вскрикнешь от неожиданности и застанешь от удовольствия. "
    '[gg]' "Аххх!!! Нельзя…"
    '[gg]' "Тогда ты проснёшься. Запаникуешь и наверняка захочешь выгнать меня. "
    '[gg]' "Но когда-нибудь это случится. Я не выдержу и сделаю это."
    '[gg]' "Вид твоей мясистой попки вызывает во мне самые извращённые мысли."
    #call milf_sleep_end
    menu:
        "1. Продолжать." if True:
            jump milf_sleep_ass_dick
        "2. Кончить." if True:
            $ pass

    scene expression 'cg/ep1/milf_sleep/Sleep_ass_dick_sperm_1.png'
    with Dissolve(.2)
    $ renpy.pause(.5, hard = True)
    scene expression 'cg/ep1/milf_sleep/Sleep_ass_dick_sperm_2.png'
    with Dissolve(.2)
    $ renpy.pause(.5, hard = True)
    '[gg]' "О дааааа!!!..."
    '[gg]' "Ты лучшая, Марина! Уверен, я приду ещё."
    $ location_now = 'Hall'
    $ milf_drunk   = False

    scene black with Dissolve(.5)


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc


label milf_sleep_end:
    show shadow_full
    with my_dissolve
    "Марина" "{i}О боже... Что он делает{/i}?!"
    "Марина" "{i}Какой отчаянный  поступок с его стороны{/i}..."
    "Марина" "{i}Нет, это неправильно. Следует остановиться{/i}."
    "Марина" "{i}Но я продолжаю неподвижно лежать и делать вид, что сплю{/i}."
    "Марина" "{i}Запах его горячего члена сводит меня с ума{/i}."
    "Марина" "{i}Я обескуражена, но... почему-то не силах сказать «нет»{/i}."
    "Марина" "{i}Мне очень хочется, чтобы он продолжал{/i}."
    "Марина" "{i}И, возможно, зашёл чуточку дальше{/i}..."
    hide shadow_full
    with my_dissolve
    
    return