label christie_root_2:
    $ events.pop('christie_root_2', 0)
    call show_bg_image_label from _call_show_bg_image_label_97
    call show_additional_images_label from _call_show_additional_images_label_82

    show Christie Normal
    show Christie Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left




    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/sunny-morning-by-musiclfiles-from-filmmusic-io.mp3', fadein = 1.5)

    "[gg]" "Доброе утро."
    show Christie Normal


    "Кристи" "Добренькое."
    show GG Smile:
        xalign .15
    with my_dissolve
    "[gg]" "Вкусное кофе? "
    show Christie Normal
    "Кристи" "[gg]… "
    #show Christie Normal
    "Кристи" "Чем больше ты будешь заговаривать мне зубы, тем сильнее я буду подозрительной в отношении тебя."
    show GG Normal
    "[gg]" "Да, извини. Это я так, для разрядки ситуации."
    #show Christie Normal
    "Кристи" "Кажется ты перепутал провода."
    show GG Embarrassment
    "[gg]" "Хорошо-хорошо, я начну заново…"
    show Christie Angry
    show shadow_full
    with my_dissolve
    "Кристи" "<смотрит на своё остывающее кофе>"
    #show GG Embarrassment
    show Christie Normal
    hide shadow_full
    with my_dissolve
    "[gg]" "Знаешь, я поразмыслил над твоими словами."
    #show GG Embarrassment
    "[gg]" "И… Мне стыдно это признавать, но в тот раз я действительно обманывал тебя."
    #show GG Embarrassment
    "[gg]" "Мне просто нужны были деньги, вот и всё."
    #show Christie Normal
    "Кристи" "Чёрт…"
    #show GG Embarrassment
    "[gg]" "Однако твои суждения… Они словно обухом по башке."
    #show GG Embarrassment
    "[gg]" "Можешь не верить, но ты достучалась моего разума, или совести, это уже как тебе угодно."
    #show GG Embarrassment
    "[gg]" "И я понял, что меняться надо не для кого-то, а для себя. "
    show GG Normal
    "[gg]" "Ведь это моя жизнь, правда? И в первую очередь я отчитываюсь перед собой. "
    #show GG Normal
    "[gg]" "И если меня устраивает быть преступником, если мне комфортно в роли негодяя, значит, вымаливая прощения, я просто обманываю."
    show Christie Surprise
    "Кристи" "Тааааак?"
    show GG Embarrassment
    "[gg]" "Короче говоря, я думал о своём отношении к жизни, и о том, какие люди меня окружают."
    show Christie Smile
    "Кристи" "Ты думал про Игоря? Хи-хи"
    show GG Laughs
    "[gg]" "И про него тоже. "


    show GG Normal
    "[gg]" "Он мой друг, и он совсем не похож на бандита, хотя, конечно, мы промышляем одним и тем же, но при этом мы сами ненавидим и наше занятие, и тех, с кем приходиться иметь дело."
    #show GG Normal
    "[gg]" "Так зачем, спрашивается, я тогда этим занимаюсь?"
    show Christie Normal
    "Кристи" "Ну и зачем?"


    show GG Normal
    "[gg]" "В этом-то и загвоздка. Я не знаю! Реально не знаю."
    #show GG Normal
    "[gg]" "Я в растерянности и понятия не имею, что мне делать и как измениться. Какова должна быть моя исходная точка?"
    show Christie Normal
    "Кристи" "Знаешь, [gg], это правильные слова."
   # show Christie Normal
    "Кристи" "Я думаю, нет, я уверен, что тебе нужна «нравственная реабилитация»!"
    show GG Skepticism
    "[gg]" "Это ещё что за херня?"
    show Christie Smile
    "Кристи" "Помощь специалиста."
    show GG Skepticism
    "[gg]" "Психиатра?! "
    show Christie Normal
    "Кристи" "Психолога. "
    show GG Surprise
    "[gg]" "А какая разница?"
    show Christie Normal
    "Кристи" "Колоссальная. "


    show Christie Normal
    "Кристи" "У меня, к слову, есть знакомая-психолог, она крутой профессионал и могла бы помочь тебе."
    show GG Embarrassment
    "[gg]" "Когда я просил о помощи, я имел в виду совсем не это…"
    show Christie Angry
    "Кристи" "Так ты хочешь измениться, или ты просто дерьмо мне на уши вешал?"
    show GG Embarrassment
    "[gg]" "Хочу, но…"
    show Christie Angry
    "Кристи" "Никаких но! Я завтра же позвоню ей и запишу тебя на приём. "
    show GG Embarrassment
    "[gg]" "Если она профи, то её сеансы платные, а у меня сейчас, скажем так, некоторые трудности с деньгами…"
    show Christie Smile
    "Кристи" "Пусть эта задача выступает для тебя мотиватором, а не препятствием. "
    show Christie Angry
    "Кристи" "Но заначки мои не трогай! Надоело их прятать от тебя!"
    show GG Laughs
    "[gg]" "Ничего не обещаю. «Плохого парня» не вытравить за один день, ты же знаешь."
    show Christie Normal
    "Кристи" "До завтра, [gg]. "
    show GG Normal
    "[gg]" "Увидимся."
    $ location_now = 'Kitchen'
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/morning.mp3', fadein = 1.5)
    $ descript_Christie = _("Кристи обещала записать меня к психологу. Если я готов на «трепанацию мозга», мне следует поговорить с ней об этом завтра Днём.")
    $ Event('christie_root_2_2', 'Corridor')
    $ Event('christie_root_3', 'Christie', time = ['afternoon'], day_start = time.day_now + 1,)
    jump main_interface_label


label christie_root_2_2:
    $ events.pop('christie_root_2_2', 0)

    $ location_now = 'Corridor'
    call show_bg_image_label from _call_show_bg_image_label_98
    call show_additional_images_label from _call_show_additional_images_label_83

    $ from_say_screen = False
    show Milf Normal
    show Milf Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)

    show GG Normal
    show GG Surprise at go_from_left

    "[gg]" "Марина?!"
    show Milf Embarrassment
    "Марина" "Ой…"
    show Milf Embarrassment# at hehe_transform()
    show GG:
        xalign .15
    with my_dissolve
    "Марина" "Не ловко вышло, хи-хи."
    show Milf Embarrassment
    "Марина" "Я совершенно случайно услышала ваш разговор с Кристи, ну и…"
    show GG Embarrassment
    "[gg]" "Подслушивать некрасиво!"
    show Milf Embarrassment
    "Марина" "Ох, прости. Я лишь застала последние несколько фраз о походе к психологу, это правда?"
    show GG Normal
    "[gg]" "Пока ещё не знаю. Теперь, когда об этом уже знает весь дом, трудно сказать наверняка."
    show Milf Embarrassment
    "Марина" "О нет-нет-нет. Пожалуйста, не меняй своего решения. "
    show Milf Normal
    "Марина" "Я лишь хотела поддержать тебя. "
    show Milf Passion
    "Марина" "Ты очень смелый, если решился на такое."
    show GG Laughs
    "[gg]" "Хах!!... Ну, если ты так говоришь."
    show Milf Passion
    "Марина" "Я горжусь тобой, [gg]. "
    show GG Embarrassment
    "[gg]" "….С-спасибо."
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
