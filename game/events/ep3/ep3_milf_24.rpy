label ep3_milf_24:

    if time.time_now in ['night', 'evening']:
        $ tmp_milf_costume = 'Night_'
    elif True:
        $ tmp_milf_costume = ''

    $ events['ep3_milf_24'].complete = True

    hide screen main_interface

    call show_bg_image_label from _call_show_bg_image_label_44
    call show_additional_images_label from _call_show_additional_images_label_38
    with Dissolve(.5)




    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085



    if time.time_now in ['night', 'evening']:

        show Milf Night_Normal
    elif True:


        show Milf Normal


    if time.time_now in ['night', 'evening']:

        show Milf Night_Normal:

            ypos 1085

            xalign .95
    elif True:



        show Milf Normal:

            ypos 1085

            xalign .95

    with Dissolve(.5)



















    "[gg]" "Марина, ты весь день занимаешься домашними делами, и не позволяешь себе отдохнуть."



    if time.time_now in ['night', 'evening']:

        show Milf Night_Embarrassment
    elif True:


        show Milf Embarrassment


    "Марина" "Как мило с твоей стороны, [gg]. Хочешь сократить мои обязанности? "

    show GG Laughs
    "[gg]" "Я ещё не готов идти на такие жертвы. "


    if time.time_now in ['night', 'evening']:

        show Milf Night_Angry
    elif True:


        show Milf Angry




    "Марина" "Так я и думала."
    show GG Smile
    "[gg]" "Но зато у меня есть два билета на представление «Кошки». Не хочешь сходить?"


    if time.time_now in ['night', 'evening']:

        show Milf Night_Surprise
    elif True:


        show Milf Surprise


    "Марина" "Обалдеть!!! Они наверняка стоили кучу денег! "
    if time.time_now in ['night', 'evening']:

        show Milf Night_Angry
    elif True:


        show Milf Angry

    "Марина" "О нет, только не говори, что ты украл их!"
    show GG Normal
    "[gg]" "Какого хорошего ты обо мне мнения. "


    if time.time_now in ['night', 'evening']:

        show Milf Night_Chagrin
    elif True:


        show Milf Chagrin


    "Марина" "Извини, пожалуйста. Просто… ну, ты сам знаешь. Твои проблемы с законом и всё такое."
    show GG Normal
    "[gg]" "Проехали."

    if time.time_now in ['night', 'evening']:

        show Milf Night_Embarrassment
    elif True:


        show Milf Embarrassment

    "Марина" "Ну так что, ты приглашаешь?"

    if time.time_now in ['night', 'evening']:

        show Milf Night_Chagrin
    elif True:


        show Milf Chagrin

    "[gg]" "Не совсем…"



    if time.time_now in ['night', 'evening']:

        show Milf Night_Chagrin
    elif True:


        show Milf Chagrin



    "Марина" "…."
    "[gg]" "Я бы с радостью. Честно. Но сейчас у меня полно дел. "
    "[gg]" "Мне получилось добыть два билета, для тебя и Кристи. Уверен, вы отлично проведёте время. "
    "Марина" "Да, очень жаль… "


    if time.time_now in ['night', 'evening']:

        show Milf Night_Angry
    elif True:


        show Milf Angry


    "[gg]" "Это же «Кошки», Марина! Пожалуйста, соглашайся. Я приложил много усилий, чтобы достать вам эти билеты. "
    $ block_change_milf_position = False
    $ remove_from_inventory("Билеты")

    if time.time_now in ['night', 'evening']:

        show Milf Night_Normal
    elif True:


        show Milf Normal


    "Марина" "Ты прав. Спасибо. Я ценю твои старания."

    show GG Normal

    "[gg]" "Вот и замечательно!"



    hide screen main_interface

    if hasattr(store, 'tmp_milf_costume'):
        $ del tmp_milf_costume

    if events.get('ep3_milf_24_2') and events['ep3_milf_24_2'].complete:
        jump ep3_milf_24_final

    jump main_interface_label






label ep3_milf_24_2:


    $ events['ep3_milf_24_2'].complete = True

    hide screen main_interface
    
    #$ location_now = 'Hall'
    #call show_bg_image_label from _call_show_bg_image_label_45
    #call show_additional_images_label from _call_show_additional_images_label_39
    #with Dissolve(.5)

    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085



    show Christie Normal
    show Christie Normal:
        xalign .65
        ypos 1085

        xalign .95

    with Dissolve(.5)

    "[gg]" "Привет, Кристи. У меня для тебя сюрприз."
    show Christie Smile
    "Кристи" "Я заинтригована. "
    "[gg]" "Я достал пару билетов на представление «Кошки» в местный театр. Для тебя и Марины. "

    show Christie Skepticism
    "Кристи" "Хм… С чего такая щедрость?"
    show GG Smile
    "[gg]" "Во-первых, я очень вас люблю. А во-вторых…"
    show Christie Normal
    "Кристи" "А во-вторых, ты снова хочешь проникнуть в комнату Марины. Интересно, зачем?"

    show GG Surprise
    "[gg]" "Чёрт…"
    "[gg]" "Ты застала меня врасплох. "
    show Christie Normal
    "Кристи" "Одними билетами тут не отделаешься. Признавайся, что у тебя на уме?"
    show GG Chagrin
    "[gg]" "Эм…"
    show GG Normal
    "[gg]" "Ладно, детектив, готов написать чистосердечное признание."
    "[gg]" "Как ты помнишь, я выпытывал у тебя День Рождения Марины? Ну вот, теперь я собираюсь подобрать ей подходящий подарок. "

    "[gg]" "Понимаю, звучит как оправдания полоумного извращенца, но…. Хочу немного порыться в её вещах, убедившись, что именно ей может не хватать"
    show Christie Smile
    "Кристи" "Хех. А не проще спросить?"
    "[gg]" "Тогда это не будет сюрпризом."
    show Christie Skepticism
    "Кристи" "Ладно. Сделаю вид, что верю. "
    "[gg]" "Так ты пойдёшь на представление?"
    show Christie Smile
    "Кристи" "Само собой. Это же «Кошки»!"
    "[gg]" "Желаю приятно провести время. Представление пройдёт в ближайшие дни."
    show Christie Normal
    "Кристи" "Спасибо."





    $ location_now = 'Corridor'
    hide screen main_interface
    if events.get('ep3_milf_24') and events['ep3_milf_24'].complete:
        jump ep3_milf_24_final

    jump main_interface_label

label ep3_milf_24_final:
    call show_bg_image_label from _call_show_bg_image_label_46
    call show_additional_images_label from _call_show_additional_images_label_40
    with Dissolve(.5)

    $ events.get('ep3_milf_24', 0)

    $ events.pop('ep3_milf_24_2', 0)

    show GG Think

    show GG Think:
        xalign .5
        ypos 1085


    with Dissolve(.5)

    $ block_milf_home   = True
    $ block_sister_home = True

    "[gg]" "Теперь стоит выпроводить их из дому, убедившись, что я остаюсь сам."
    $ descript = _("Попрощаться с Мариной и Кристи, дождавшись их у входной двери в коридоре Вечером. ")


    $ Event('ep3_milf_25', 'Corridor', time = ['evening'])

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
