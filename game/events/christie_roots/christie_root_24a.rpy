



image christie_root_24a_anim 1:


    "cg/christie_root/restroom/1.png" with Dissolve(.1)
    .5
    "cg/christie_root/restroom/2.png" with Dissolve(.1)
    .5

    "cg/christie_root/restroom/3.png" with Dissolve(.1)
    .5

    "cg/christie_root/restroom/4.png" with Dissolve(.1)
    .5
    "cg/christie_root/restroom/5.png" with Dissolve(.1)
    .5
    "cg/christie_root/restroom/6.png" with Dissolve(.1)
    .5

transform tr_christie_root_24a_anim_right_1_0:
    xpos -30

transform tr_christie_root_24a_anim_right_1_1:
    xalign .45
    yalign .5
    zoom .94

image christie_root_24a_anim_right_1 1:

    'cg/christie_root/restroom/right_1.png' with Dissolve(.1)
    xpos 930
    zoom 1.0
    1.25
    'cg/christie_root/restroom/right_1.png' with Dissolve(.1)
    xpos 960
    yalign .5
    zoom .94
    .75
    repeat


image christie_root_24a_anim_right_1 2:

    'cg/christie_root/restroom/right_1.png' with Dissolve(.1)
    xpos 930
    zoom 1.0
    1
    'cg/christie_root/restroom/right_1.png' with Dissolve(.1)
    xpos 960
    yalign .5
    zoom .94
    .36
    repeat


image christie_root_24a_anim_right_1 3:

    'cg/christie_root/restroom/right_1.png'
    xpos 930
    zoom 1.0
    .3
    'cg/christie_root/restroom/right_1.png'
    xpos 960
    yalign .5
    zoom .94
    .18
    repeat

image christie_root_24a_anim 2:


    "cg/christie_root/restroom/fuck_1.png" with Dissolve(.1)
    .25
    "cg/christie_root/restroom/fuck_2.png" with Dissolve(.1)
    .25

    "cg/christie_root/restroom/fuck_3.png" with Dissolve(.1)
    .25

    "cg/christie_root/restroom/fuck_4.png" with Dissolve(.1)
    .25
    "cg/christie_root/restroom/fuck_5.png" with Dissolve(.1)
    .25
    "cg/christie_root/restroom/fuck_4.png" with Dissolve(.1)
    .25
    "cg/christie_root/restroom/fuck_3.png" with Dissolve(.1)
    .25
    "cg/christie_root/restroom/fuck_2.png" with Dissolve(.1)
    .25

    repeat



image christie_root_24a_anim 3:


    "cg/christie_root/restroom/fuck_1.png" with Dissolve(.1)
    .12
    "cg/christie_root/restroom/fuck_2.png" with Dissolve(.1)
    .12

    "cg/christie_root/restroom/fuck_3.png" with Dissolve(.1)
    .12

    "cg/christie_root/restroom/fuck_4.png" with Dissolve(.1)
    .12
    "cg/christie_root/restroom/fuck_5.png" with Dissolve(.1)
    .12
    "cg/christie_root/restroom/fuck_4.png" with Dissolve(.1)
    .12
    "cg/christie_root/restroom/fuck_3.png" with Dissolve(.1)
    .12
    "cg/christie_root/restroom/fuck_2.png" with Dissolve(.1)
    .12

    repeat


image christie_root_24a_anim 4:


    "cg/christie_root/restroom/fuck_1.png" with Dissolve(.05)
    .06
    "cg/christie_root/restroom/fuck_2.png" with Dissolve(.05)
    .06

    "cg/christie_root/restroom/fuck_3.png" with Dissolve(.05)
    .06

    "cg/christie_root/restroom/fuck_4.png" with Dissolve(.05)
    .06
    "cg/christie_root/restroom/fuck_5.png" with Dissolve(.05)
    .06
    "cg/christie_root/restroom/fuck_4.png" with Dissolve(.05)
    .06
    "cg/christie_root/restroom/fuck_3.png" with Dissolve(.05)
    .06
    "cg/christie_root/restroom/fuck_2.png" with Dissolve(.05)
    .06

    repeat


image christie_root_24a_anim 5:


    "cg/christie_root/restroom/fuck_1.png"
    .02
    "cg/christie_root/restroom/fuck_2.png"
    .02

    "cg/christie_root/restroom/fuck_3.png"
    .02

    "cg/christie_root/restroom/fuck_4.png"
    .02
    "cg/christie_root/restroom/fuck_5.png"
    .02
    "cg/christie_root/restroom/fuck_4.png"
    .02
    "cg/christie_root/restroom/fuck_3.png"
    .02
    "cg/christie_root/restroom/fuck_2.png"
    .02

    repeat
label christie_root_24a:
    if not from_gallery_check():
        $ events.pop('christie_root_24a', 0)
    elif True:
        $ time          = Time()
        $ time.time_now = 'morning'










    $ location_now = 'Corridor'
    scene black with Dissolve(.5)
    $ renpy.pause(.5)
    call show_bg_image_label from _call_show_bg_image_label_125
    show Christie Invis
    show Christie Invis:
        xalign .85
    
    with my_vpunch

    "Кристи" "Эй, кто-нибудь!"

    show GG Surprise
    show GG Surprise:
        xalign -1.5
        easein_cubic 1.5 xalign .15
    "Кристи" "Помогите!!!"
    "Кристи" "Марина! [gg]!!"
    "Кристи" "Вы меня слышите?!"
    show GG Surprise:
        xalign .15
    with my_dissolve

    "[gg]" "Я тебя слышу, Кристи. "

    "[gg]" "Что стряслось?"
    "Кристи" "Зайди в ванную, пожалуйста! Дверь открыта."
    "Кристи" "У меня тут непредвиденная авария!"

    show GG Surprise:
        easein 1 xalign 1.4


    $ renpy.pause(1, hard = True)

    scene black with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    scene expression 'images/locations/bg/Restroom/morning.png'
    show GG Surprise
    show GG Surprise:
        xzoom -1
        xalign .85
    show expression 'cg/christie_root/restroom_christie_root_24a_0.png'
    with Dissolve(1)

    $ renpy.pause(1, hard = True)





    "[gg]" "Ого."
    with my_vpunch
    "Кристи" "Хватить пялиться на мою задницу, лучше помоги мне!"
    show GG Surprise
    "[gg]" "Что здесь стряслось?"
    "Кристи" "Ты ослеп?! "
    "Кристи" "Я застряла!!!"
    show GG Laughs
    with my_dissolve
    "[gg]" "Харош придуриваться, в стиральной машинке невозможно застрять!"
    "Кристи" "Ну вот представь себе, а я умудрилась…"
    "Кристи" "Тут большое свободное пространство, но очень маленький люк. "
    "Кристи" "Я как-то зацепилась локтём, зажала себя плечами, и теперь с трудом могу двинуться. "
    show GG Skepticism
    with my_dissolve
    "[gg]" "Это просто нелепо! Вылезай уже!"
    "Кристи" "Ты издеваешься?!"
    show GG Skepticism
    with my_dissolve
    "[gg]" "Ты наверняка разыгрываешь меня, Кристи. "
    show GG Skepticism
    with my_dissolve
    "[gg]" "Я не поведусь на твои уловки."
    "Кристи" "Это чистая правда, [gg]!!!"
    "Кристи" "Просто вытащи меня…"
    "Кристи" "Пожаааалуйста!"
    show GG Think
    with my_dissolve
    "[gg]" "{i}Блин, кажется она реально застряла. {/i}"

    scene black with Dissolve(.5)
    $ renpy.pause(.5, hard = True)

    scene expression 'cg/christie_root/restroom/bg.png'
    show expression 'cg/christie_root/restroom/body.png'
    show expression 'cg/christie_root/restroom/shadow.png'
    with Dissolve(1)
    $ renpy.pause(1, hard = True)
    with my_dissolve
    "[gg]" "Вот, я возьму тебя здесь, ты не против?"
    show expression 'cg/christie_root/restroom/right_1.png'
    with my_dissolve
    "Кристи" "Хватай меня где пожелаешь, только вызволи меня отсюда, умоляю!"
    "[gg]" "Звучит как приглашение, ха-ха-ха."
    "Кристи" "Мне не до шуток, [gg]."
    "Кристи" "Как бы не пришлось теперь вызывать слесаря. "
    "[gg]" "Посмотрим."
    scene expression 'cg/christie_root/restroom/bg.png'

    show expression "cg/christie_root/restroom/1.png"
    show expression 'cg/christie_root/restroom/shadow.png'
    show expression 'cg/christie_root/restroom/right_1.png'
    with my_dissolve

    "[gg]" "Постарайся расслабиться, а я понемногу стану потягивать тебя к себе."
    "Кристи" "Хорошо."
    "Кристи" "Только очень осторожно. Мне страшно."
    "[gg]" "{i}О боже, как же плотно её задница прилегает ко мне.{/i}"
    "[gg]" "{i}Я начинаю стремительно возбуждаться и ничего не могу с этим поделать.{/i}"


    scene expression 'cg/christie_root/restroom/bg.png'

    show christie_root_24a_anim 1
    show expression 'cg/christie_root/restroom/shadow.png'
    show expression 'cg/christie_root/restroom/right_1.png'
    with my_dissolve

    "[gg]" "{i}Кристи наверняка почувствовала, как резко вырос мой член.{/i}"
    "[gg]" "{i}Даааа, комично получается.{/i}"
    "[gg]" "{i}Но я не могу её вот так бросить, дожидаясь, пока мой «приятель» образумится.{/i}"
    "[gg]" "{i}Она рассчитывает на меня, и я её не брошу!{/i}"
    "[gg]" "{i}Хотя… Кого я обманываю? Мои руки буквально прилипли к ней.{/i}"
    "Кристи" "Ну так как, ты тащишь меня?"
    "[gg]" "Да, вот, готова? На счёт три…"
    "[gg]" "Раз…"
    "[gg]" "Два…"
    scene expression 'cg/christie_root/restroom/bg.png'

    show expression "cg/christie_root/restroom/7.png"
    show expression 'cg/christie_root/restroom/shadow.png'
    show expression 'cg/christie_root/restroom/right_2.png'
    with my_vpunch
    "[gg]" "Три!"





    "Кристи" "Я что-то чувствую…."
    "[gg]" "Где? Внутри?"
    "Кристи" "Нет, что-то упирается мне в попку."

    scene expression 'cg/christie_root/restroom/bg.png'

    show christie_root_24a_anim 2
    show expression 'cg/christie_root/restroom/shadow.png'
    show expression 'cg/christie_root/restroom/right_1.png'

    with my_dissolve

    "[gg]" "Наверное это мой ремень от штанов… Извини, но я не могу его сейчас снять."
    "Кристи" "Хорошо."
    "Кристи" "Он мне не мешает."
    "Кристи" "Просто, кажется, он несколько странной формы. "
    "[gg]" "{i} Ещё немного, и она раскусит меня!{/i}"
    "[gg]" "Давай не будем отвлекаться на мелочи, и сосредоточимся на деле."
    "Кристи" "Да, ты прав. Тяни меня сильнее, кажется, начинает получаться."
























label christie_root_24a_meu:
    window hide
    $ renpy.pause(9999)
    menu:
        "Продолжить" if True:
            jump christie_root_24a_meu
        "Ускориться" if True:
            $ pass
    scene expression 'cg/christie_root/restroom/bg.png'

    show christie_root_24a_anim 3
    show expression 'cg/christie_root/restroom/shadow.png'
    show expression 'cg/christie_root/restroom/right_1.png'
    with my_dissolve
    "[gg]" "{i}Ещё как получается, я сейчас кончу…{/i}"
    "Кристи" "Мои руки постепенно высвобождаются."
    "Кристи" "Я чувствую, что вот-вот вылезу отсюда."
    "Кристи" "Давай, налегай сильнее."
    "Кристи" "Сильнее! Ещё сильнее!"
    "[gg]" "Твою мать, Кристи…"
    "[gg]" "Я делаю всё от меня зависящее, не пытайся меня подгонять."
    "[gg]" "{i}Как же мне хотелось бы продлить это блаженство как можно дольше.{/i}"
    "Кристи" "Извини, просто я сильно волнуюсь."
    "Кристи" "Мне кажется, или ты стал каким-то чрезмерной горячим?"
    "[gg]" "Даааа, наверное давление поднялось. "
    "Кристи" "Оуу…"
    "Кристи" "Ты так сильнее волнуешься за меня?"
    "[gg]" "Я заинтересован в твоём высвобождении не меньше твоего, Кристи."
    "[gg]" "Но переживаю, как бы не навредить тебе в процессе освобождения."
    "[gg]" "Давай двигаться в такт. "
    "Кристи" "У меня получается?"
    "[gg]" "Ага, вот так, хорошо."
    "Кристи" "Ты буквально обжигаешь меня своим теплом, поскорее вынь меня отсюда, пожалуйста!"
    "[gg]" "Ох.. Ты права."
    "[gg]" "Ещё мгновение, и моё волнение перерастёт в бурный фонтан."

    $ christie_root_24a_meu_2_var = 3
label christie_root_24a_meu_2:
    $ renpy.show('christie_root_24a_anim ' + str(christie_root_24a_meu_2_var))
    with my_dissolve
    window hide
    $ renpy.pause(9999)
    menu:
        "Продолжить" if True:
            jump christie_root_24a_meu_2
        "Замедлиться" if christie_root_24a_meu_2_var != 2:
            $ christie_root_24a_meu_2_var -= 1

            jump christie_root_24a_meu_2
        "Ускориться" if christie_root_24a_meu_2_var != 3:
            $ christie_root_24a_meu_2_var += 1

            jump christie_root_24a_meu_2
        "Кончить" if True:

            $ pass

    python:
        try:
            del christie_root_24a_meu_2_var
        except:
            pass
    scene expression 'cg/christie_root/restroom/bg.png'

    show christie_root_24a_anim 4
    show expression 'cg/christie_root/restroom/shadow.png'
    show expression 'cg/christie_root/restroom/right_1.png'
    with my_dissolve

    "Кристи" "Давай, почти!"
    "Кристи" "Я уже практически вылезла!"
    "Кристи" "Последние усилия!"
    "Кристи" "Тащи-тащи-тащи!!!"
    "[gg]" "Тащууууууууу!!!!"

    scene expression '#fff' with Dissolve(.2)
    $ renpy.pause(.1, hard = True)




    scene expression 'cg/christie_root/restroom/bg.png'

    show expression 'cg/christie_root/restroom/fuck_end.png'
    show expression 'cg/christie_root/restroom/shadow.png'
    show expression 'cg/christie_root/restroom/right_3.png'

    with Dissolve(1.5)

    $ renpy.pause(2, hard = True)


    "[gg]" "О дааа…"
    "[gg]" "Готово."
    "Кристи" "Мои руки полностью свободы, спасибо."
    "Кристи" "Теперь я могу вылезти сама."

    scene black with Dissolve(1)
    $ renpy.pause(1.2, hard = True)
    $ add_to_gallery(25)
    $ location_now = 'Restroom'

    call show_bg_image_label from _call_show_bg_image_label_126
    show Christie Embarrassment
    show Christie Embarrassment:
        xzoom -1
        xalign .15
    show GG Nude_Chagrin
    show GG Nude_Chagrin:
        xzoom -1
        xalign .85
    with my_dissolve
    "Кристи" "Получилось."

    "[gg]" "Ага."
    show Christie Embarrassment
    "Кристи" "Ты в курсе, что у тебя член торчит из штанов?"
    show GG Nude_OMG
    "[gg]" "…."
    show Christie Embarrassment
    "Кристи" "Полагаю, это и был тот самый «ремень»?"

    "[gg]" "Ну, в общем, да. Извини."
    show Christie Embarrassment
    "Кристи" "Я что, так сильно тебе нравлюсь?.."

    "[gg]" "Наверное…"

    "[gg]" "Мне очень стыдно, честно."

    "[gg]" "Это случилось совсем случайно, без злого умысла…"
    show Christie Embarrassment
    "Кристи" "Прекрати оправдываться."
    show Christie Embarrassment
    "Кристи" "Я всё прекрасно понимаю сама."
    show Christie Embarrassment
    "Кристи" "И шокирована не тем, что вижу, а тем, что знаю."
    show Christie Embarrassment
    "Кристи" "Я сразу догадался чем это ты трёшься об меня, но не стала тебя стыдить. "

    "[gg]" "Почему?"
    show Christie Embarrassment
    "Кристи" "….."
    show Christie Embarrassment
    "Кристи" "Потому что не хочу, чтобы ты чувствовал себя виноватым и прекратил работать над собой."

    "[gg]" "С-серьёзно?!"
    show Christie Embarrassment
    "Кристи" "Да. Но я не хочу это обсуждать."
    show Christie Embarrassment
    "Кристи" "Это пошло."
    show Christie Embarrassment
    "Кристи" "Пожалуйста, можешь выйти? Я хочу привести себя в порядок."

    "[gg]" "Да, разумеется."

    scene black with Dissolve(.5)

    call check_gallery_label from _call_check_gallery_label_8

    $ renpy.pause(.5)
    $ location_now = 'Corridor'
    $ time.time_now = get_next_time()
    call show_bg_image_label from _call_show_bg_image_label_127
    with Dissolve(.5)
    show GG Think
    show GG Think:
        xalign .5
    with my_dissolve
    "[gg]" "Кажется, я окончательно поехал крышей."
    #show GG Think
    "[gg]" "Зачем я домогаюсь её?!"
    #show GG Think
    "[gg]" "Я так конфужен произошедшим, что у меня не хватит смелости подойти сегодня к Кристи. "
    #show GG Think
    "[gg]" "Пожалуй, я дождусь завтра и отдам ей реферат с утра."

    $ Event('christie_root_24a_ref', 'City_Library_BiblioGirl', button_name = _("Реферат"), priority = -1)
    $ events.pop('christie_root_21', 0)
    $ events.pop('christie_root_24', 0)


    $ unlock_city_library = True
    jump main_interface_label











label christie_root_24a_ref:

    $ events.pop('christie_root_24a_ref', 0)













    "Библиотекарша" "Знания манят вас, словно сила притяжения. "

    "Библиотекарша" "Не говорите, не надо. Я сама угадаю."

    "Библиотекарша" "Вам нужно всё те же книги, что и прежде."
    show GG Normal
    "[gg]" "Я становлюсь предсказуемым."

    "Библиотекарша" "Но умным."
    show GG Smile
    "[gg]" "Ха-ха. Спасибо. "
    show GG Smile
    "[gg]" "Вы знаете, как завлечь посетителя остаться в у вас подольше. "

    "Библиотекарша" "Хи-хи-хи!"

    "Библиотекарша" "Без лишней скромности скажу, что в этом деле я специалист."
    show GG Smile
    "[gg]" "Теперь даже не знаю, остаться с вами, чтобы убедиться в этих качествах самолично, или заняться своими делами."

    "Библиотекарша" "Большой соблазн, неправда ли? Хи-хи-хи."

    "Библиотекарша" "Проходите, не стесняйтесь. Ваши учебники уже на столе."
    show GG Normal
    "[gg]" "Спасибо."


    show BiblioGirl:
        ease 1 alpha 1.0
    show GG:
        ease 1 xalign 1.5
    $ renpy.pause(1.5, hard = True)
    scene black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    scene expression "images/cg/christie_root/library/afternoon.png"
    with Dissolve(.5)

    $ renpy.pause(.5)
    scene expression "images/cg/christie_root/library/morning_gg.png"
    with my_dissolve





    "[gg]" "Подправить, подчеркнуть, подсчитать… Ага. Отлично."
    "[gg]" "Перепроверить информацию, дописать кое-что по делу, стереть лишнее. "
    "[gg]" "Указать список авторов…"

    scene expression "images/cg/christie_root/library/evening.png"
    with Dissolve(.5)

    $ renpy.pause(.5)
    scene expression "images/cg/christie_root/library/evening_gg.png"
    with my_dissolve


    "[gg]" "Чёрт, а заниматься учёбой не так уж и скучно, как может показаться."
    "[gg]" "Пока я выписывал материалы и уточнял факты, я узнал много всего познавательного."
    "[gg]" "В целом и в общем, реферат готов. "
    "[gg]" "И я, как не странно, крайне доволен результат проделанной работы. "






    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign -0.5
        xzoom -1
        easein_cubic 1 xalign .15






    "Библиотекарша" "Вы не против, если я провожу вас к выходу?"

    "Библиотекарша" "Мне кажется, это стало доброй традицией для нас."
    scene expression "images/cg/christie_root/library/evening.png"

    show GG Smile
    show GG Smile:
        xalign .85
        xzoom -1

    show BiblioGirl Normal
    show BiblioGirl Normal:
        xzoom -1
        xalign .15

    with my_dissolve

    "[gg]" "Конечно."

    "[gg]" "Мне приятна ваша компания. "





    show GG:

        ease 1.2 xalign -1.5
    show BiblioGirl:
        xzoom 1
        ease 1.2 xalign -1.5
    $ renpy.pause(1.5, hard = True)
    $ time.time_now = 'evening'

    scene black with Dissolve(.5)


    call show_bg_image_label from _call_show_bg_image_label_128







    $ remove_from_inventory(name = 'Реферат «Обществознание» 1/3')
    $ remove_from_inventory(name = 'Реферат «Обществознание» 2/3')
    $ add_to_inventory(name = 'Реферат «Обществознание» 3/3')
    play sound 'audio/get_item.ogg'
    show screen give_item_screen(i_path+'/items/referat_2.png', _('Реферат «Обществознание» 3/3'), ['Мой собственный многочасовой', 'интеллектуальный труд.'])
    with Dissolve(.75)
    $ descript_Christie_tmp_0 = __("1. Отправиться в библиотеку и продолжить написание реферата по теме «Обществознание» (3/3).")


    $ descript_Christie     = str(descript_Christie_tmp_0) + "\n" + str(descript_Christie_tmp_1)

    $ renpy.pause(1, hard = True)

    $ renpy.pause(9999)








    hide screen give_item_screen


    with my_dissolve



























    $ events.pop('christie_root_24a', 0)
    $ events.pop('christie_root_24a_ref',  0)
    $ descript_Christie_tmp_0 = ''
    if not len(getattr(store, 'descript_Christie_tmp_1', '')):
        $ descript_Christie = _("Дождаться завтра и отдать Кристи реферат по «Обществознанию».")


        $ Event('christie_root_25', 'GG_Room', time = ['morning',], button_name = _("Реферат"), priority = -1)




    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
