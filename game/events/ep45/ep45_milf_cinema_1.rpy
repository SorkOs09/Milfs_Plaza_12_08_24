
init python:








    
    renpy.image("ep5_milf_cinema_1_fg_table", Image('cg/ep5/cinema_1/table.png'))

    renpy.image(
        "ep5_milf_cinema_1_fg", 

        LiveComposite(
        (1920, 1080),
        (0, 0), 'ep5_milf_cinema_1_fg_table',
        (0, 0), 'cg/ep5/cinema_1/corn.png',
        )
        )


    for i in range(1, 7):
        j = str(i)
        renpy.image(
            "ep5_milf_cinema_1 k"+j, Image('cg/ep5/cinema_1/k'+j+'.png'))
           


    for i in range(0, 3):

        renpy.image(
        "ep5_milf_cinema_1_anim_1 "+str(i+1), 
        Ani('cg/ep5/cinema_1/anim_1/', 6,  
            float(15-5*i)/100, reverse = True, effect=None, start=1,),
        )


        renpy.image(
        "ep5_milf_cinema_1_anim_2 "+str(i+1), 
        Ani('cg/ep5/cinema_1/anim_2/', 8,  
            float(15-5*i)/100, reverse = True, effect=None, start=1,),
        )

    for i in ("1", "2"):
        renpy.image("ep5_cinema_1_bg " + i, Image('cg/ep5/cinema_1/bg_'+i+'.png'))
        
        j = "ep5_milf_cinema_1_anim_"+i
        
        renpy.image(
        j+" end", 
        Image('cg/ep5/cinema_1/anim_'+i+'/end.png'),)

        renpy.image(
        j + " 0", 
        'cg/ep5/cinema_1/anim_'+i+'/1.png',
        )

    


    renpy.image(
        "ep5_milf_cinema_1_anim_1 end_2", 
        Image('cg/ep5/cinema_1/anim_1/end_2.png'),)

label ep5_milf_cinema_1:
    if from_gallery_check():
        $ location_now  = 'Hall'
        $ time.time_now = 'evening'
    $ add_to_gallery("20_1")

    $ renpy.music.stop(fadeout=.5)

    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)
    
    $ from_say_screen = False
    
    call show_bg_image_label from _call_show_bg_image_label_69
    


    show Milf Night_Normal
    show Milf Night_Normal:

        xalign .85
        ypos 1080
    with my_dissolve

    show GG Laughs

    show GG Laughs at go_from_left

    $ renpy.pause(.3, hard = True)

    "[gg]" "Сегодня мой выбор пал на фильм «Кикбоксёр»."
    show Milf Night_Smile
    with my_dissolve
    "Марина" "Тот, что с Жан Клодом Ван Дамом?"
    show GG Normal
    with my_dissolve
    "[gg]" "Ага. Видела его?"
    show Milf Night_Surprise
    with my_dissolve
    "Марина" "Ещё бы. Это кино моего детства."
    show GG Embarrassment
    with my_dissolve
    "[gg]" "Чувствую себя глупым юнцом."
    show Milf Night_Smile
    with my_dissolve
    "Марина" "Так и есть, мой милый."

    "Марина" "Но я рада твоему выбору. Давай смотреть."
    show Milf Night_Passion
    with my_dissolve
    "Марина" "Это значит, что сегодня у тебя «боевое» настроение. "

    "Марина" "Давай смотреть."
    show GG Normal
    with my_dissolve
    "[gg]" "Давай."



    scene black
    with Dissolve(.5)
    scene expression 'cg/ep5/cinema_1/cinema_1_kick_1.png'
    with my_dissolve




    "Кино" "Вууааааааааа!!..."


    "Кино" "* Звук хлёсткого удара по лицу*"


    "Кино" "* Звук тяжёлого дыхания бойцов *"


    "Кино" "* Рёв зала и кровожадные выкрики*"



    scene expression 'cg/ep5/cinema_1/cinema_1_kick_2.png'
    with my_dissolve



    "Кино" "Оооооооооо!!!!"


    "Кино" "*Звук удара, напоминающего взрыв хлопушки*"


    "Кино" "*Звук хруста нескольких рёбер*"


    "Кино" "*Вопль бойца, раздающееся эхом при замедленной съёмки*"

    scene ep5_milf_cinema_1 k1
    show ep5_milf_cinema_1_fg_table
    show GG Invis:
        xalign .45
    show Milf Invis:
        xalign .68
    with my_dissolve



    "Марина" "Эти каратисты такие жестокие."


    "Марина" "И брутальные…"


    "Марина" "Не то, чтобы я была фанаткой таких фильмов, но я приятно впечатлена."


    "[gg]" "Ещё бы! Такие картины больше не снимают. "


    "[gg]" "Они устарели."


    "Марина" "Время никого не щадит…"


    show ep5_milf_cinema_1 k2
    with my_dissolve


    "[gg]" "Эй! Прекрати."


    "[gg]" "Некоторым вещам следует настояться много лет, прежде чем их можно будет оценить по достоинству."

    show ep5_milf_cinema_1 k3
    with my_dissolve

    "Марина" "Чувствую себя египетской мумией. "


    "[gg]" "Клеопатрой! "


    "Марина" "Хи-хи. Мне нравится ход твоих мыслей."


    show ep5_milf_cinema_1 k4
    with my_dissolve



    "Марина" "Ну, и сколько лет мне ещё прождать, прежде чем ты оценишь «это»?"


    "[gg]" "П-пресвятые угодники!"


    "[gg]" "Для меня ты само совершенство, Марина."


    scene ep5_milf_cinema_1 k5
    show ep5_milf_cinema_1_fg
    show GG Invis:
        xalign .15
    show Milf Invis:
        xalign .55
    with my_dissolve





    "Марина" "Хочу убедиться в этом наверняка."


    "[gg]" "Этот вечер перестаёт быть томным…"


    show ep5_milf_cinema_1 k6
    with my_dissolve

    "Марина" "Я люблю запоминающиеся вечера."


    "Марина" "Особенно, если это время я провожу со своим любимым. "


    "[gg]" "Хех… Люблю, когда ты доминируешь."


    "Марина" "Опыт обязывает."




    "Марина" "Моя вкусняшка. "

    scene ep5_cinema_1_bg 1
    show ep5_milf_cinema_1_anim_1 1
    show ep5_milf_cinema_1_fg
    show GG Invis:
        xalign .15
    show Milf Invis:
        xalign .55
    with my_dissolve


    "[gg]" "Как аппетитно ты смакуешь мой член…"


    "[gg]" "Сразу понятно, какое блюдо у тебя любимое. "


    "Марина" "Мгл… Мгл…"


    "[gg]" "Разумеется, меня это устраивает."


    "[gg]" "Я обожаю тепло твоего рта…"


    "[gg]" "Но больше всего, меня заводит, когда я слышу вульгарные причмокивание, что ты издаёшь во время минета. "


    "Марина" "Чмок… Чмок… Чмок…"


    "[gg]" "Да-да, я знаю. Продолжай."


    "[gg]" "Ты восхитительная женщина. "










    call before_menu_label from _call_before_menu_label
label ep5_milf_cinema_1_menu_1:
    call at_menu_label from _call_at_menu_label
    menu:
        "Продолжить." if True:
            call wait_click_label from _call_wait_click_label_6
            jump ep5_milf_cinema_1_menu_1
        "Увеличить скорость" if True:
            $ pass


    
    show ep5_milf_cinema_1_anim_1 2
    
    with my_dissolve










    "[gg]" "Аххх… "


    "[gg]" "Ты ускоряешься…"


    "Марина" "Чмок…. Чмок…"


    "Марина" "Мгл… Мгл… Мгл…"


    "[gg]" "У тебя сейчас такое вульгарное выражение лица."


    "[gg]" "Хочется схватить тебя за волосы и насильно запихнуть в тебя член как можно глубже."


    "[gg]" " Да так, чтобы достать до самой глотки."


    "[gg]" "И кончить туда как можно больше."


    "Марина" "Мгл!!.. Мгл!!.."


    "Марина" "Чмок! Чмок! Чмок!.."

    $ ep5_milf_cinema_1_menu_2 = 0
    call before_menu_label from _call_before_menu_label_1
label ep5_milf_cinema_1_menu_2:
    call at_menu_label from _call_at_menu_label_1
    menu:
        "Продолжить." if True:
            call wait_click_label from _call_wait_click_label_7
            jump ep5_milf_cinema_1_menu_2
        "Уменьшить скорость" if not ep5_milf_cinema_1_menu_2:
            $ pass
            $ ep5_milf_cinema_1_menu_2 = 1

            
            show ep5_milf_cinema_1_anim_1 1
            
            with my_dissolve
            call wait_click_label from _call_wait_click_label_8
            jump ep5_milf_cinema_1_menu_2
        "Увеличить скорость" if ep5_milf_cinema_1_menu_2:

            $ ep5_milf_cinema_1_menu_2 = 0

            show ep5_milf_cinema_1_anim_1 2

            with my_dissolve
            call wait_click_label from _call_wait_click_label_9
            jump ep5_milf_cinema_1_menu_2
        "Кончить" if True:
            $ pass

    python:
        try:
            del ep5_milf_cinema_1_menu_2
        except:
            pass

    show ep5_milf_cinema_1_anim_1 3

    with my_dissolve




















    "[gg]" "Мариночка…."


    "[gg]" "Я уже близко..."


    "[gg]" "Хочу, чтобы ты сосала так, словно хочешь высушить меня досуха!"


    "[gg]" "Давай, соси! Соси из последних сил."


    "[gg]" "Я собираюсь обкончать тебе весь рот!!!"





    show white with Dissolve(.2)

    $ renpy.pause(.5, hard = True)

    show ep5_milf_cinema_1_anim_1 end
    hide white
    with my_dissolve

    $ renpy.pause(.3,)



    "[gg]" "Не устаю восхищаться твоему мастерству, Марина."


    "Марина" "Всё, ради моего любимого мальчика. "


    show ep5_milf_cinema_1_anim_1 end_2
    with my_dissolve

    "[gg]" "Я горжусь, что именно ты моя женщина. "


    "Марина" "Тогда не позволяй своей женщине остаться без твоего мощного члена в моей киске. "


    "Марина" "Она, знаешь ли, тоже изголодалась. "


    "[gg]" "Я готов трахать тебя всю ночь."


    "Марина" "Оу, как грубо…."


    "Марина" "Мне нравится, хи-хи."



    scene black with my_dissolve
    $ renpy.pause(.5)
    $ store.nameboxes['Milf'].state = "need_up"
    $ from_say_screen = False


    scene ep5_cinema_1_bg 2
    show ep5_milf_cinema_1_anim_2 0
    show ep5_milf_cinema_1_fg
    show GG Invis:
        xalign .3
    show Milf Invis:
        xalign .05
    with my_dissolve



    "Марина" "Теперь перейдём к десерту, милый."


    "Марина" "Хочу, чтобы ты трахнул меня в этой похабной позе."


    "[gg]" " Как скажешь..."


    show ep5_milf_cinema_1_anim_2 1
    with my_dissolve




    "Марина" "Оххх…."


    "Марина" "Я только вошла, а мой клитер уже изнемогает от страсти."


    "Марина" "Мир ходит кругом, а в глазах сверкает."


    "Марина" "Давай, тискай меня за сиськи!"


    "Марина" "Трахай меня изо всех сил, миленький."


    "Марина" "Как же приятно, что у тебя такой огромный, пульсирующий член."


    "[gg]" "Мариночка..."


    "Марина" "Да, я твоя Мариночка!"


    call before_menu_label from _call_before_menu_label_2
label ep5_milf_cinema_1_menu_3:
    call at_menu_label from _call_at_menu_label_2
    menu:
        "Продолжить." if True:
            call wait_click_label from _call_wait_click_label_10
            jump ep5_milf_cinema_1_menu_3
        "Увеличить скорость" if True:
            $ pass


    
    
    show ep5_milf_cinema_1_anim_2 2
    
    with my_dissolve











    "Марина" "Твои безумные движения членом доводят меня до многочисленных оргазмов!"


    "Марина" "Ахххх…."


    "Марина" "Да-да-да-да! "


    "Марина" "Я взрываюсь от наслаждения!"


    "[gg]" "Я испытываю не меньшее удовольствие. "


    "[gg]" "Внутри тебя бушует настоящий фонтан из твоих женских соков."


    "Марина" "Это всё благодаря твоему животворящему члену."


    "Марина" "Я не позволю тебе выйти из меня, пока я сама не кончу тысячу раз!"


    "[gg]" "Делай, что считаешь нужным!"


    "[gg]" "Для меня только в удовольствие приносить тебе столько радости. "


    $ ep5_milf_cinema_1_menu_4 = 1
    call before_menu_label from _call_before_menu_label_3
label ep5_milf_cinema_1_menu_4:
    call at_menu_label from _call_at_menu_label_3
    menu:
        "Продолжить." if True:
            call wait_click_label from _call_wait_click_label_11
            jump ep5_milf_cinema_1_menu_4
        "Уменьшить скорость" if ep5_milf_cinema_1_menu_4:
            $ pass
            $ ep5_milf_cinema_1_menu_4 = 0

            
            
            show ep5_milf_cinema_1_anim_2 1
            
            with my_dissolve
            call wait_click_label from _call_wait_click_label_12
            jump ep5_milf_cinema_1_menu_4
        "Увеличить скорость" if True:

            $ ep5_milf_cinema_1_menu_4 = 0

            show ep5_milf_cinema_1_anim_2 2
            
            with my_dissolve

    python:
        try:
            del ep5_milf_cinema_1_menu_4
        except:
            pass





















    "Марина" "Оооо даааа!!!"


    "Марина" "Это настоящее блаженство!"


    "Марина" "Ты знаешь, как подарить мне истинное наслаждение от секса!"


    "Марина" "Да-да-да…."


    "Марина" "Я уже сбилась со счёту, сколько раз испытала оргазм, но чувствую, что впереди ещё один прекрасный момент для моей киски! "


    "[gg]" "Тогда позволь мне кончить одновременной с тобой."


    "Марина" "Конечно, любимой."


    "Марина" "Сделай это вместе со мной!"

    
    show ep5_milf_cinema_1_anim_2 2

    with my_dissolve

    $ ep5_milf_cinema_1_menu_5 = 2
    call before_menu_label from _call_before_menu_label_4
label ep5_milf_cinema_1_menu_5:
    call at_menu_label from _call_at_menu_label_4
    menu:
        "Продолжить." if True:
            call wait_click_label from _call_wait_click_label_13
            jump ep5_milf_cinema_1_menu_5
        "Уменьшить скорость" if ep5_milf_cinema_1_menu_5 != 1:
            $ ep5_milf_cinema_1_menu_5 -= 1

            jump ep5_milf_cinema_1_anim_2_label
        "Увеличить скорость" if ep5_milf_cinema_1_menu_5 != 3:

            $ ep5_milf_cinema_1_menu_5 += 1

            jump ep5_milf_cinema_1_anim_2_label
        "Кончить" if True:


            pass
    python:
    
        try:
            del ep5_milf_cinema_1_menu_5
        except:
            pass



    show ep5_milf_cinema_1_anim_2 3
    with my_dissolve



















    "[gg]" "Я приближаюсь…"


    "Марина" "И я…"


    "[gg]" "Я уже на пределе… "


    "[gg]" "Ещё мгновение!"


    "Марина" "Давай, миленький, кончай!"


    "Марина" "Я кончаааааааююююю!"


    "[gg]" "Ухххх!!!!...."


    "[gg]" "И яяяяяяя!!!...."


    "[gg]" "Дааааааааааааа!"


    show white with Dissolve(.2)

    $ renpy.pause(.5, hard = True)
    show ep5_milf_cinema_1_anim_2 end
    
    hide white
    
    with my_dissolve


    $ renpy.pause(.3,)



    "Марина" "Я ещё никогда не испытывала столько безумного восторга, как сейчас."


    "[gg]" "Мне даже нечего добавить."


    "[gg]" "Это было неповторимо. "


    "Марина" "Но мы же повторим, верно?.."


    "[gg]" "Ещё бы."





    scene black with Dissolve(.5)


    call show_bg_image_label from _call_show_bg_image_label_70
    with Dissolve(.5)


    show GG Normal
    show GG Normal:

        xalign .1
        ypos 1085
        zoom 1.0-0.035
    show Milf Night_Passion
    show Milf Night_Passion:

        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with my_dissolve










    "Марина" "Было приятно провести с тобой время."
    show GG Normal
    "[gg]" "И мне."
    show GG Normal
    "[gg]" "Жутко обидно, что этот день подходит к концу."
    show Milf Night_Passion
    "Марина" "Мы всегда можем продолжить."
    show GG Smile
    "[gg]" "Только ради этого и стоит просыпаться утром."

    $ time.time_forward(jump_to_main_interface = False)
    return
























label ep5_milf_cinema_2:

    
    $ add_to_gallery("20_0")
    if from_gallery_check():
        $ location_now  = 'Hall'
        $ time.time_now = 'evening'
    call show_bg_image_label from _call_show_bg_image_label_111
    call show_additional_images_label from _call_show_additional_images_label_91


    show Milf Night_Normal
    show Milf Night_Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    show GG Vine
    show GG Vine at go_from_left
    $ renpy.pause(1)







    '[gg]' "Как на счёт того, чтобы посмотреть «Лолиту» и выпить немножко вина? "

    show Milf Night_Passion


    'Марина' "Вау, [gg]. Ты меня поражаешь. "

    '[gg]' "Ну так что?"

    show Milf Night_Smile

    'Марина' "Включай кино, а я пока открою бутылку."








    scene black with Dissolve(.5)


    stop music fadeout 1.5
    play music 'audio/movie_event.mp3' fadein 1.5
    scene expression 'cg/ep1/movie/cinema_screen_3.png' with Dissolve(.5)
    'Лолита' "Давай уедем. Далеко-далеко. Только ты и я."
    'Мужчина' "Это опрометчиво."
    'Лолита' "Но здесь нам не позволят быть вместе. Никогда…"
    scene expression 'cg/ep1/movie/cinema_wine_normal_0.png' with Dissolve(.5)
    '[gg]' "Как тебе вино?"
    'Марина' "Прекрасное. И кажется, я немного перебрала."
    scene expression 'cg/ep1/movie/cinema_wine_normal_1.png' with Dissolve(.5)
    '[gg]' "Слушай, подруга, пока мы ещё окончательно не напились, я хотел бы…"
    'Марина' "Нет, позволь мне первой."
    '[gg]' "Да?"
    'Марина' "Я хочу обсудить твой проступок, [gg]. "
    '[gg]' "О нет, только не вздумай портить наш вечер!"
    scene expression 'cg/ep1/movie/cinema_wine_normal_1a.png' with Dissolve(.5)
    'Марина' "Если ты и далее намерен жить в этом доме, следует придерживаться определённых правил. Главное из которых – никакой уголовщины."
    scene expression 'cg/ep1/movie/cinema_wine_normal_2.png' with Dissolve(.5)
    '[gg]' "Ну… Ты преувеличиваешь. Всего-лишь небольшая шалость. "
    scene expression 'cg/ep1/movie/cinema_wine_normal_3.png' with Dissolve(.5)
    'Марина' "Из-за которой тебя могли посадить на пару лет."
    '[gg]' "Кто ж знал, что всё так обернётся? Мы не собирались ничего воровать, просто шутили. "
    '[gg]' "Это самая нелепая отмазка, которую я только смог из себя выдавить. "
    scene expression 'cg/ep1/movie/cinema_wine_normal_4.png' with Dissolve(.5)
    'Марина' "Как я уже сказала, ворам здесь не место. "
    '[gg]' "Дааааа?"
    'Марина' "Да. Вор должен сидеть в тюрьме. "
    '[gg]' "Даже если это я?"
    'Марина' "Даже если и ты."
    '[gg]' "…"
    '[gg]' "Что ж! ЧТО ЖЕ!"
    scene expression 'cg/ep1/movie/cinema_wine_normal_5.png' with Dissolve(.5)
    '[gg]' "Тогда, если ты, вдруг, заболеешь раком и нам срочно понадобится огромная сумма денег на лечебные процедуры, не проси меня ограбить банк! Я, знаешь ли, не преступник."
    scene expression 'cg/ep1/movie/cinema_wine_normal_6.png' with Dissolve(.5)
    'Марина' "Ха-ха-ха-ха! "
    'Марина' "Какой ты дурашка."
    scene expression 'cg/ep1/movie/cinema_wine_normal_7.png' with Dissolve(.5)
    'Марина' "Я бы ни за что не стала о таком просить. Лучше мучительная смерть, чем видеть, как твой друг разлагается, теряя всякую человечность."
    scene expression 'cg/ep1/movie/cinema_wine_normal_2.png' with Dissolve(.5)
    '[gg]' "Я всё равно ограблю банк. Не смогу смотреть, как ты корчишься от боли!"
    scene expression 'cg/ep1/movie/cinema_wine_normal_1a.png' with Dissolve(.5)
    'Марина' "Эй, прекрати меня хоронить! Я ничем не болею. И уж тем более не планирую умирать."
    scene expression 'cg/ep1/movie/cinema_wine_normal_8.png' with Dissolve(.5)
    'Марина' "У меня имеются кое-какие сбережения для экстренных случаев. Так что, можешь оставить свои амбиции в сфере криминала."
    '[gg]' "Ах вот как… И много там, в заначке твоей? "
    'Марина' "Не твоего ума дела, хи-хи."
    scene expression 'cg/ep1/movie/cinema_wine_normal_0.png' with Dissolve(.5)
    '[gg]' "Ты права, я слишком перегибаю палку."
    'Марина' "Верно замечено, [gg]."
    '[gg]' "Учитывая, как я влип в этот самый криминал, лучше и не пытаться просить занять у неё денег."
    scene expression 'cg/ep1/movie/cinema_wine_normal_9.png' with Dissolve(.5)
    '[gg]' "Знаешь… Хочу ещё раз извиниться, что подвёл тебя. "
    '[gg]' "Прости меня, за эту дурость с кражей из магазина. Пожалуйста, поверь, я сделаю всё возможное, чтобы загладить свою вину перед тобой."
    'Марина' "Не надо ничего заглаживать, [gg]. Просто не совершай ничего такого, что может создать нам проблемы. "
    scene expression 'cg/ep1/movie/cinema_wine_normal_10.png' with Dissolve(.5)
    '[gg]' "По рукам."
    'Марина' "Вот и чудненько. Тогда, быть может, наконец-то посмотрим сериал?"
    '[gg]' "Конечно! "
    scene expression 'cg/ep1/movie/cinema_wine_normal_11.png' with Dissolve(.5)
    'Марина' "Если ты не против, я прилягу к тебе. Вино ударило мне в голову. "
    '[gg]' "Я полностью в твоём распоряжении. "
    scene black with Dissolve(1)
    $ renpy.pause(.5, hard = True)
    scene expression 'cg/ep1/movie/cinema_wine_sex_1.png' with Dissolve(1)
    'Марина' "Ах, как хорошо. "
    'Марина' "Мы так давно не были по-настоящему вместе. "
    'Марина' "С объятиями и дружеской беседой. "
    'Марина' "Как старые добрые друзья."
    '[gg]' "В-верно…"
    scene expression 'cg/ep1/movie/cinema_wine_sex_2.png' with Dissolve(.5)
    '[gg]' "О, Господи, её тело такое горячее!"
    '[gg]' "И её спокойное, протяжное дыхание… "
    '[gg]' "Только не смотри на неё! Только не смотри!"
    scene expression 'cg/ep1/movie/cinema_wine_sex_3.png' with Dissolve(.5)
    '[gg]' "Проклятье! "
    '[gg]' "Разве можно устоять перед этими огромными, сладкими дыньками?!"
    '[gg]' "Я бы отдал всё на свете, только бы попить из них молочко."
    scene expression 'cg/ep1/movie/cinema_wine_sex_4.png' with Dissolve(.5)
    '[gg]' "Марина?.."
    '[gg]' "Ты спишь?"
    scene expression 'cg/ep1/movie/cinema_wine_sex_5.png' with Dissolve(.5)
    '[gg]' "И очень вовремя. От разглядывания её сексуальных форм, у меня случился деревянный стояк. "
    '[gg]' "Что же мне делать? Разбудить её, пока ещё не слишком поздно? "
    '[gg]' "Или… Быть может…."
    scene expression 'cg/ep1/movie/cinema_wine_sex_6.png' with Dissolve(.5)
    '[gg]' "Аккуратно… Нежно… "
    '[gg]' "Я точно сошёл с ума!"
    '[gg]' "Если моя подруга проснётся, я вряд ли смогу оправдаться. "
    '[gg]' "Она наверняка решит, что её друг извращенец!"
    '[gg]' "Плевать."
    '[gg]' "Я слишком близко, чтобы отступать. "
    scene expression 'cg/ep1/movie/cinema_wine_sex_7.png' with Dissolve(.5)
    stop music fadeout 1.5
    play music 'audio/Erotic.mp3' fadein 1.5
    '[gg]' "O, даааааа!!! "
    '[gg]' "Как же они хороши!!!"
    scene expression 'cg/ep1/movie/cinema_wine_sex_8_1.png' with Dissolve(.5)
    '[gg]' "Я так взбудоражен, что, наверное, вот-вот взорвусь."
    scene cinema_wine_sex_Ani with Dissolve(.5)
    '[gg]' "Её мягкие, сочные груди просто таят в моих руках."
    '[gg]' " Марина так усиленно дышит, что это заводит меня ещё сильнее."
    '[gg]' "Ещё чуточку… Пожалуйста. Ещё чуточку."
    scene expression 'cg/ep1/movie/cinema_wine_sex_8_3.png' with Dissolve(.5)
    '[gg]' "Каааааайф!!!..."
    scene expression 'cg/ep1/movie/cinema_wine_sex_9.png' with Dissolve(.5)
    '[gg]' "Чёрт… Я так увлёкся, что чуть не разбудил её."
    scene expression 'cg/ep1/movie/cinema_wine_sex_6.png' with Dissolve(.5)
    '[gg]' "Нужно прекращать это безобразие и возвращаться в свою комнату. "
    scene expression 'cg/ep1/movie/cinema_wine_sex_2.png' with Dissolve(.5)
    play music 'audio/movie_event.mp3' fadein 1.5
    'Марина' "Ой, [gg], кажется я уснула на тебе."
    '[gg]' "Н-ничего страшного. Ты вовсе не стеснила меня. "
    scene expression 'cg/ep1/movie/cinema_wine_sex_1.png' with Dissolve(.5)
    'Марина' "Ну и хорошо. Мне сладко спалось."
    '[gg]' "Рад был провести с тобой время, подружка."
    'Марина' "И я…"
    scene expression 'cg/ep1/movie/cinema_wine_sex_10.png' with Dissolve(.5)
    'Марина' "Надеюсь, он не заметил, что я давно уже не сплю."
    'Марина' "И то, как сильно я возбудилась от его прикосновений…"
    'Марина' "Мне не стоило позволять ему делать это. "
    'Марина' "Это неправильно. "
    'Марина' "Больше я не совершу эту ошибку."
    $ location_now = 'Hall'
    scene black
    with Dissolve(.5)

    $ renpy.pause(.5)
    if from_gallery_check():
        jump main_interface_label
    $ time.time_forward(jump_to_main_interface = False)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc


label ep5_milf_cinema_1_anim_2_label:
    
    $ renpy.show("ep5_milf_cinema_1_anim_2 "+str(ep5_milf_cinema_1_menu_5))
    with my_dissolve
    call wait_click_label from _call_wait_click_label_14
    jump ep5_milf_cinema_1_menu_5