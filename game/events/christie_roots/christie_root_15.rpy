image christie_root_15_gg = Composite((1920, 1080),
(1732, 338),  Crop((0,0,188,742), "cg/christie_root/kitchen/kitche_kristy_atlas.png"))


image christie_root_15_kristy 1 = Composite((1920, 1080),
(1103, 275),  Crop((256,0,270,765), "cg/christie_root/kitchen/kitche_kristy_atlas.png"))


image christie_root_15_kristy 2 = Composite((1920, 1080),
(1103, 275),  Crop((0,742,261,765), "cg/christie_root/kitchen/kitche_kristy_atlas.png"))


image christie_root_15_kristy 3 = Composite((1920, 1080),
(1103, 283),  Crop((522,0,261,757), "cg/christie_root/kitchen/kitche_kristy_atlas.png"))



label christie_root_15:
    python:


        if not from_gallery_check():
            
            events.pop("christie_root_15", 0)
            for i in ('afternoon', 'evening', 'night'):
                
                locations['Kitchen'].image_buttons_times[i].pop("coffe_100_percent", 0)
        else:
            location_now  = 'Kitchen'
            time          = Time()
            time.time_now = 'morning'

    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/past-sadness-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    if not from_gallery_check():
        $ block_milf_home = copy.deepcopy(block_milf_home_8546412)
    call show_bg_image_label from _call_show_bg_image_label_122
    call show_additional_images_label from _call_show_additional_images_label_97




    show christie_root_15_kristy 1
    show christie_root_15_kristy 1:
        xpos 950


    show christie_root_15_gg
    show christie_root_15_gg:
        xpos 1100
        easein_cubic 1 xpos 960
    $ renpy.pause(1.25, hard = True)














    "[gg]" "{i}О, как замечательно. Кажется, она нашла мой подарочек.{/i}"



    "Кристи" "Ммммм, как вкусно."
    show christie_root_15_gg:
        xpos 960
    "Кристи" "Обожаю горячее кофе по утру. "


    show christie_root_15_kristy 2
    with my_dissolve
    "Кристи" "…."

    "[gg]" "{i}Вау! {/i}"

    "[gg]" "{i}Как неожиданно и приятно.{/i}"

    "[gg]" "{i}Эта сиська явно желает познакомиться со мной поближе, хе-хе-хе.{/i}"

    "[gg]" "{i}Стоило бы окликнуть Кристи, наверное, но тогда она спрячет эту красоту обратно.{/i}"

    "[gg]" "{i}Наверное, мне лучше тихо уйти и вернуться позже.{/i}"

    show christie_root_15_kristy 3
    with vpunch
    $ stnd_music_play()

    "Кристи" "А?!!"
    "Кристи" "Ты меня напугал!"
    "Кристи" "Давно ты здесь стоишь?"






    "[gg]" "Извини, просто засмотрелся. Хе-хе-хе."

    call show_bg_image_label from _call_show_bg_image_label_119


    show GG Laughs
    show GG Laughs:
        xalign .85
        xzoom -1
    show Christie Embarrassment
    show Christie Embarrassment:
        xalign .15
        xzoom -1

    with vpunch


    $ add_to_gallery(21)
    "Кристи" "Бесстыдник! "
    show GG Smile
    "[gg]" "Эй, это кухня, а не ванная комната. "
    show GG Smile
    "[gg]" "Я здесь не для того, чтобы подглядывать за тобой исподтишка. "
    show Christie Embarrassment
    "Кристи" "Но делал именно это."
    show GG Smile
    "[gg]" "Условия располагали."
    call check_gallery_label from _call_check_gallery_label_10
    show Christie Smile
    "Кристи" "Ладно, чудила. Я всё равно у тебя в долгу. Пусть это будет моей наградой тебе за то, что ты так выручил меня."
    show GG Normal
    "[gg]" "О, значит ты оценил мой ход. "
    show Christie Passion
    "Кристи" "Скажешь тоже! "
    show Christie Passion
    "Кристи" "Кофе просто супер."
    show Christie Passion
    "Кристи" "Но как ты смог его достать за такой короткий срок?"
    show Christie Passion
    "Кристи" "Я заказываю его через интернет, в обычных магазинах его нет в продаже."
    show GG Normal
    "[gg]" "Пустяки."
    show GG Normal
    "[gg]" "У меня свои поставщики. "
    show Christie Skepticism
    "Кристи" "Действительно?"
    show GG Normal
    "[gg]" "Разумеется. Но называть их, по понятным причинам, я не стану."
    show Christie Surprise
    "Кристи" "Ты что, нарушал закон?"
    show GG Skepticism
    "[gg]" "По твоему, только так я способен сделать добро близкому человеку?"
    show Christie Chagrin
    "Кристи" "Что ты! Нет, ни в коем случае! Извини…."
    show Christie Chagrin
    "Кристи" "Я настоящая тварь."
    show GG Smile
    "[gg]" "Всё в порядке."
    show GG Normal
    "[gg]" "Я понимаю твою озабоченность. "
    show GG Normal
    "[gg]" "У тебя есть основания, это правда."
    show GG Normal
    "[gg]" "Но в этот раз я действительно всё сделал по уму."
    show GG Embarrassment
    "[gg]" "Почти…"
    show Christie Smile
    "Кристи" "Какой же ты хороший, [gg] спасибо!"
    show GG Normal
    "[gg]" "Очевидно, походы к психологу идут мне на пользу."
    show Christie Smile
    "Кристи" "Значит ты продолжишь сеансы?"
    show GG Normal
    "[gg]" "Почему бы и нет."
    show GG Normal
    "[gg]" " Хотя это ощутимо бьёт по моему кошельку. "
    show Christie Smile
    "Кристи" "Ага, удары кувалдой, не иначе. Хи-хи-хи."
    show Christie Smile
    "Кристи" "Увидимся, [gg]!"
    show GG Normal
    "[gg]" "Обязательно."

    show Christie:
        xzoom -1
        ease 1 xalign 1.4

    $ renpy.pause(1.2, hard = True)
    hide Christie
    with my_dissolve
    show GG Think:
        ease .5 xalign .5


    "[gg]" "Если так подумать, я на верном пути исправления."
    show GG Think:
        xalign .5
    with my_dissolve
    "[gg]" "Пожалуй, мне стоит снова сходить к психологу и закрепить успех самосовершенствования. "





    $ Event('christie_root_16', 'City_Psi', time = ['morning', 'afternoon'])

    $ unlock_city_psi   = True

    $ descript_Christie = _("Провести очередной сеанс с психологом, живущей в соседнем доме. Она принимает только Утром или Днём.")
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
