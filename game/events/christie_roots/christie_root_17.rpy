image christie_root_17_5_face = Composite((1920, 1080),
(548, 167),  Crop((0,0,149,127), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_0 = Composite((1920, 1080), 

(0, 0), "cg/christie_root/sit_2/0.png"
)

image christie_root_17_1 = Composite((1920, 1080),
(411, 0),  Crop((1068,1080,1068,1080), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_900 = Composite((1920, 1080),
(1223, 0),  Crop((0,127,697,1080), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_999 = Composite((1920, 1080),
(0, 879),  Crop((1779,0,593,201), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_4_hand 4 = Composite((1920, 1080),
(423, 409),  Crop((733,0,733,346), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_4_hand 1 = Composite((1920, 1080),
(416, 400),  Crop((2924,0,731,354), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_3_hand 5 = Composite((1920, 1080),
(413, 402),  Crop((727,353,727,353), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_3_hand 2 = Composite((1920, 1080),
(407, 396),  Crop((1458,359,729,359), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_3_hand 4 = Composite((1920, 1080),
(412, 401),  Crop((2908,354,727,354), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_4_hand 3 = Composite((1920, 1080),
(421, 404),  Crop((0,1207,735,351), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_3_hand 1 = Composite((1920, 1080),
(406, 395),  Crop((728,718,728,359), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_3_hand 3 = Composite((1920, 1080),
(408, 398),  Crop((2187,714,729,357), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_4_hand 5 = Composite((1920, 1080),
(420, 409),  Crop((2952,1038,738,346), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_4_hand 2 = Composite((1920, 1080),
(420, 409),  Crop((0,1558,727,345), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_2_face 2 = Composite((1920, 1080),
(556, 54),  Crop((0,1903,808,768), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_2_face 1 = Composite((1920, 1080),
(556, 54),  Crop((2484,1536,828,768), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))

image christie_root_17_3_hand 6 = Composite((1920, 1080),
(415, 405),  Crop((0,2671,727,350), "cg/christie_root/sit_2/christie_root_sit_2_atlas.png"))








image christie_root_17_4_anim 1:


    "christie_root_17_3_hand 1"
    .15
    "christie_root_17_3_hand 2"
    .15

    "christie_root_17_3_hand 3"
    .15

    "christie_root_17_3_hand 4"
    .15
    "christie_root_17_3_hand 5"
    .15
    "christie_root_17_3_hand 6"
    .15
    "christie_root_17_3_hand 5"
    .15
    "christie_root_17_3_hand 4"
    .15

    "christie_root_17_3_hand 3"
    .15

    "christie_root_17_3_hand 2"
    .15

    repeat




image christie_root_17_4_anim 2:


    "christie_root_17_3_hand 1"
    .15
    "christie_root_17_3_hand 2"
    .15

    "christie_root_17_3_hand 3"
    .15

    "christie_root_17_3_hand 4"
    .15
    "christie_root_17_3_hand 5"
    .15
    "christie_root_17_3_hand 6"
    .15
    "christie_root_17_3_hand 5"
    .15
    "christie_root_17_3_hand 4"
    .15

    "christie_root_17_3_hand 3"
    .15

    "christie_root_17_3_hand 2"
    .15

    repeat


image christie_root_17_4_anim_bg = Composite((1920, 1080), 

(0, 0), "cg/christie_root/sit_2/0.png",



)
image christie_root_17_4_anim_fg = Composite((1920, 1080), 


(0, 0), "christie_root_17_5_face",
(0, 0),  "christie_root_17_999",

)




label christie_root_17:
    if not from_gallery_check():
        $ events.pop('christie_root_17', 0)

    scene black with Dissolve(.5)

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)




    $ renpy.pause(.5, hard = True)
    scene expression 'cg/christie_root/kristy_sit_1.png' with vpunch

    "Кристи" "Эй, я же читала книгу…"
    "[gg]" "Второй сеанс прошёл ещё лучше, чем первый!"
    "Кристи" "Да ладно?"
    "[gg]" "Да, кажется, я вошёл в кураж."
    "[gg]" "Сьюзен отлично меня понимает, и умеет наладить контакт должным образом."
    "Кристи" "Ты выглядишь так, словно этот контакт нёс характер плотских утех."
    "[gg]" "{i}Мать моя женщина, она чертовски близка к истине!{/i}"
    "[gg]" "Эээ… Нет! "
    "[gg]" "Я имел в виду её профессиональные навыки, как психолога, который знает подход к своим клиентам."


    scene expression 'cg/christie_root/kristy_sit_5.png' with my_dissolve

    "Кристи" "Вот оно как…"
    "[gg]" "Ага. "
    "[gg]" "Она мастерски выводит меня на нужную тему, учитывает мой темперамент и лояльная к моему прошлому. "
    "[gg]" "C ней я чувствую себя уверенно и, кажется, готов ей выведать все тайны мира."
    "Кристи" "А со мной?.."
    "[gg]" "Что с тобой?"
    "Кристи" "Ты разве не чувствуешь эту же уверенность, когда рядом с тобой я?"
    "[gg]" "Ну…."
    "Кристи" "Вот именно! Это странно! "
    "Кристи" "Ты едва её знаешь, [gg], а уже отзываешься о ней, словно вы сто лет дружите!"
    "Кристи" "Ты всего лишь её клиент, а она просто психолог, который должна вставить тебе мозги на место, понял?!"
    "[gg]" "Кристи…"



    "Кристи" "Что «Кристи»?!"
    "[gg]" "Мне кажется, или в твоих словах чувствуются нотки ревности? "
    "Кристи" "Глупости!"
    "Кристи" "Это ведь я тебя к ней отправила."
    "[gg]" "Вот именно."
    "Кристи" "И ты не мой парень!"
    "[gg]" "Тоже правда."
    "Кристи" "И вообще, если кажется, креститься нужно!"
    "[gg]" "…."
    "[gg]" "Извини, я не хотел тебя злить."
    "Кристи" "Ты вовсе не разозлил меня!"
    "Кристи" "У меня, как мы уже определили, нет ни малейших причин злиться и уж тем более ревновать!"
    "[gg]" "Я пойду?"




    "Кристи" "Нет, останься. "


    scene expression 'cg/christie_root/kristy_sit_6.png' with vpunch

    "Кристи" "Ты останешься здесь до тех пор, пока не испытываешь рядом со мной те же чувства, что испытываешь к Сьюзен. "
    "[gg]" "Хех…"
    "[gg]" "Предлагаешь провести мне на диване остаток жизни?"
    "Кристи" "Эй!!"
    "[gg]" "Шучу-шучу! Хе-хе-хе."
    "Кристи" "Ну а пока ты думаешь о том, как приблизить этот момент поскорее, советую быть полезным и не сидеть без дела. "
    "[gg]" "Значит ли это, что я должен делать массаж твоим ножкам? "
    "Кристи" "Именно это я и сказала!"


    scene expression 'cg/christie_root/kristy_sit_3.png'
    with my_dissolve
    "Кристи" "Я, признаться, несколько разочарована тобой, [gg]…"
    "[gg]" "Это ещё почему?"
    "Кристи" "Я отправляла тебя к Сьюзен, чтобы ты понимал, как наладить со мной отношения и изменил свою жизнь к лучшему. "
    "[gg]" "Именно этим я и занимаюсь."
    "Кристи" "…."
    "Кристи" "Да, стоит признать, ты стал угодливым и… нежным. "
    "Кристи" "Мне импонирует твоё внимание, а твоя забота – развращает. "



    "[gg]" "Только ради тебя и я пошёл к психологу."
    "[gg]" "А все последующие изменения – издержки моей работы над собой. "
    "Кристи" "Понимаю… "
    "Кристи" "И прекрасно вижу твои старания. "


    scene expression 'cg/christie_root/kristy_sit_4.png'
    with my_dissolve
    "Кристи" "….."
    "Кристи" "Я…"
    "Кристи" "Знаешь, наверное, ты прав."


    "Кристи" "Я действительно ревную тебя. "
    "Кристи" "Мне хочется вернуть наши прежние отношения…."
    "Кристи" "До того, как ты отдалился и стал преступником."
    "[gg]" "Поверь мне, и я сам ЭТОГО хочу."
    scene christie_root_17_4_anim_bg
    show christie_root_17_2_face 1
    show christie_root_17_3_hand 1
    show christie_root_17_4_anim_fg


    with vpunch
    "[gg]" "И к ЭТОМУ всё идёт…"
    "Кристи" "Охххх…."
    scene christie_root_17_4_anim_bg
    show christie_root_17_2_face 1
    show christie_root_17_4_anim 1
    show christie_root_17_4_anim_fg

    with my_dissolve
    "Кристи" "Мне кажется, всё идёт куда-то не туда…"
    "[gg]" "Главное, чтоб нам это нравилось, верно?.."

    show christie_root_17_2_face 2
    with my_dissolve
    "Кристи" "Н-наверное… "
    "Кристи" "Аххх!!… "
    "Кристи" "Пожалуйста, не надо."
    "Кристи" "Сейчас я не могу быть уверена в правильности наших поступков. "

    menu:
        "Ускориться" if True:
            $ pass
    show christie_root_17_4_anim 2
    with my_dissolve

    "[gg]" "Разве тебе не нравится?"
    "Кристи" "Ты меня смущаешь."
    "Кристи" "Прекрати, не надо. "
    "[gg]" "Но ты же сама говорила, чтобы я оставался здесь до тех пор, пока…"
    "Кристи" "Аххххх….!!"
    "Кристи" "Нет, ты не можешь так продолжать."
    "Кристи" "Всё-всё, ты свободен."
    show christie_root_17_2_face 1
    with my_dissolve
    "Кристи" "Ты можешь идти."
    "Кристи" "Прошу тебя, прекрати это."
    "[gg]" "Ты уверена?.."
    "Кристи" "Ммм…."
    show christie_root_17_2_face 2
    with my_dissolve
    "Кристи" "Да, пожалуйста, остановись."


    scene expression '#000' with Dissolve(1)
    call check_gallery_label from _call_check_gallery_label_9
    $ add_to_gallery(24)
    $ renpy.pause(1.5, hard = True)
    $ stnd_music_play()

    $ location_now = 'Hall'
    call show_bg_image_label from _call_show_bg_image_label_118


    show Christie Embarrassment
    show Christie Embarrassment:
        xalign .85
        ypos 1085


    show GG Embarrassment
    show GG Embarrassment:
        xalign .15
        ypos 1085
    with Dissolve(.5)



    "Кристи" "Я чувствую себя неловко, [gg]."
    show Christie Embarrassment
    "Кристи" "Ты… "
    show Christie Embarrassment
    "Кристи" "Точнее Мы делаем неправильные вещи. "
    show GG Embarrassment
    "[gg]" "Я всего лишь хочу быть нужным тебе."
    show Christie Embarrassment
    "Кристи" "Да, понимаю."
    show Christie Embarrassment
    "Кристи" "Но твои старания чрезмерны, [gg]."
    show Christie Embarrassment
    "Кристи" "Не обижайся на меня, но я бы предпочла ограничиться дружбой."
    show GG Chagrin
    "[gg]" "Я не обижаюсь…"
    show Christie Smile
    "Кристи" "Если хочешь быть «нужным», можешь помочь мне с написанием реферата."
    show GG Surprise
    "[gg]" "У тебя есть трудности с уроками?"
    show Christie Chagrin
    "Кристи" "Совсем чуточку."
    show Christie Normal
    "Кристи" "В какой-то момент я так старательно училась, что опередила программу. "
    show Christie Normal
    "Кристи" "А теперь, когда программа догнала меня, я банально ленюсь делать формальную «работу» для аттестата. "
    show Christie Normal
    "Кристи" "Для меня это плёвое дело. "
    show Christie Normal
    "Кристи" "Просто мне приятно, что ты проявляешь такую заботу."
    show Christie Normal
    "Кристи" "У нас появляются общие дела и мы можем больше времени проводить вместе. "
    show GG Smile
    "[gg]" "Согласен. Давай сюда свои темы, я попробую что-то придумать."
    show Christie Smile
    "Кристи" "О, спасибо. Ты просто супер!"
    show Christie Smile
    "Кристи" "Вот, я скинула тебе задания на телефон."
    show GG Normal
    "[gg]" "Есть контакт. Я ознакомлюсь и вернусь с результатами."
    show Christie Smile
    "Кристи" "Тогда до встречи."
    show GG Normal
    "[gg]" "Ага!"

    show Christie:
        easeout_cubic 1.5 xalign -1.2
    $ renpy.pause(1.5, hard = True)
    hide Christie
    show GG Think:
        ease 1 xalign .5
    "[gg]" "Какой же я придурок!"
    show GG Think:
        xalign .5
    with my_vpunch
    "[gg]" "Что, чёрт возьми, я себе возомнил?!"

    "[gg]" "Ясное дело, что Кристи будет смущена после таких действий…"
    show GG Think
    "[gg]" "И мне крупно повезло, что она не избила меня на полусмерти и не опозорила на весь дом, обозвав извращенцем. "
    show GG Think
    "[gg]" "Но сам-то я о чём думаю?..."
    show GG Think
    "[gg]" "С каких пор я не могу контролировать себя в её присутствии? "
    show GG Think
    "[gg]" "Мои руки отказывались мне подчиняться. "
    show GG Think
    "[gg]" "Подчиняться здравому смыслу!"
    show GG Think
    "[gg]" "Откуда у меня этот животный инстинкт?!"
    show GG Think
    with my_vpunch
    "[gg]" "Какой же я идиот! Кретин. Придурок!"
    show GG Think
    "[gg]" "Я всё понял!"
    show GG Think
    "[gg]" "Наверное, всё дело в сиськах Сьюзен. "
    show GG Think
    "[gg]" "Я слишком перевозбудился и, окажись на месте Кристи любая другая девушка, я бы вытворял ровно тоже самое."
    show GG Think
    "[gg]" "………"
    show GG Think
    "[gg]" "Или нет?.."
    show GG Think
    "[gg]" "Не знаю. Ничего не знаю."
    show GG Think
    "[gg]" "Правильно, что она отшила меня."
    show GG Think
    "[gg]" "…….."
    show GG Think
    "[gg]" "Так, что у нас там с рефератами?.."
    show GG Think
    "[gg]" "Проще всего будет скачать их из интернета, купив темы на соответствующих сайтах."

    $ time.time_now = "afternoon"





    $ descript_Christie= _("Купить реферат по «Обществознанию» в интернете.")


    $ add_items_for_web_shop_fixed.append(('Реферат', 150))

    $ Event('christie_root_18', 'Corridor', time = get_next_time())

    $ Event('christie_root_19', 'gg_room_pc_exit')




    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
