label christie_root_34:




    call show_bg_image_label from _call_show_bg_image_label_142

    show Christie Normal
    show Christie Normal:
        xalign .85
    with my_dissolve


    show GG Normal
    show GG Normal at go_from_left


    $ remove_from_inventory('Костюм Харли Квин.')




    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/sunny-morning-by-musiclfiles-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Эй, у меня для тебя подарочек!"
    show Christie Normal

    "Кристи" "Ха, и у меня!"
    show GG Smile:
        xalign .15
    with my_dissolve
    "[gg]" "Вот, распакуй и переоденься. Уверен, ты будешь приятно удивлена. "
    show Christie Embarrassment
    "Кристи" "Обожаю сюрпризы."
    show Christie Angry
    "Кристи" "Но предупреждаю, если это что-то вульгарное, то одевать не стану."
    show GG Laughs
    "[gg]" "За кого ты меня держишь?!"
    show GG Normal
    show Christie Embarrassment
    with my_dissolve
    "[gg]" "Я скрупулёзно выбирал наряд с учётом твоих вкусов и предпочтений."
    show Christie Skepticism
    "Кристи" "Но ты ведь не знаешь ни того, ни другого."
    show GG Normal
    "[gg]" "Ну…"
    show GG Smile
    "[gg]" "Тем интересней!"
    show Christie Normal
    "Кристи" "Ладно, сейчас вернусь."

    show Christie:

        linear 1 xalign -1.2
    show GG Think
    "[gg]" "Блин, я чуть не забыл про Игоря."
    show GG Think
    "[gg]" "Сейчас идеальная возможность, чтобы сделать отличную фоточку Кристи для него."
    
    show GG:
        xzoom -1
        linear 1 xalign -1.1
    $ renpy.pause(.75)
    scene black with Dissolve(.5)

    $ renpy.pause(1, hard = True)







    scene expression 'cg/christie_root/ep8_photo/1.png'
    show expression 'cg/christie_root/ep8_photo/1_0.png':
        xpos 0
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    scene expression 'cg/christie_root/ep8_photo/1.png'
    call screen christie_root_30_screen(1, 'cg/christie_root/ep8_photo/1_0.png')









    show expression 'cg/christie_root/ep8_photo/1_0.png'
    with None
    show expression 'cg/christie_root/ep8_photo/1_1.png':
        xpos 0
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    hide expression 'cg/christie_root/ep8_photo/1_0.png'
    call screen christie_root_30_screen(2)
    show expression 'cg/christie_root/ep8_photo/1_1.png':
        xpos 0
        easein_cubic 1.5 xpos -490
    $ renpy.pause(1.8, hard = True)






    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    $ add_to_gallery("29_1")
    "[gg]" "Даааа, вот это грация… Утончённость."
    "[gg]" "Не удивительно, что Игорь так нервничает из-за её снимков в эротическом амплуа."
    "[gg]" "Глядя на неё, хочется совершать подвиги, лишь бы привлечь её внимание."
    "[gg]" "Если уж Трою разрушили ради красавицы Елены, то что говорить про Кристи, которая, словно ангел, воссоздана по всем правилам эстетического совершенства."
    "[gg]" "Теперь я понимаю Париса, что решился похитить чужую жену…"
    "[gg]" "Устоять перед этой красотой невозможно."
    scene expression 'cg/christie_root/ep8_photo/2.png'
    with Dissolve(.5)
    $ renpy.pause(.75, hard = True)

    call screen christie_root_30_screen(3)

    show white with Dissolve(.1)
    
    play sound 'audio/photo_click.mp3'
    $ renpy.pause(1, hard = True)

    hide white with Dissolve(1.25)

    $ renpy.pause(1.5, hard = True)

    "[gg]" "Всё, снимок готов. Пора сваливать. "

    scene black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    if from_gallery_check():
        jump main_interface_label
    call show_bg_image_label from _call_show_bg_image_label_143


    with my_dissolve


    show GG Normal
    show GG Normal at go_from_left



    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/sunny-morning-by-musiclfiles-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Фух…"
    "[gg]" "Вроде пронесло. "
    show GG:
        xalign .15

    show Christie Harly_Laughs
    show Christie Harly_Laughs:
        xzoom -1
        xalign -.5
        easein 1.0 xalign .75
        xzoom 1
    "Кристи" "Уиииииииии!!!"

    show Christie Harly_Smile
    with my_dissolve
    "Кристи" "Стилизованный под современный дизайн костюм кровавой Мэри! "
    show Christie Harly_Laughs:
        xalign .75
        xzoom 1
    show Christie Harly_Laughs
    "Кристи" "Спасибо, [gg]! "
    show Christie Harly_Normal
    "Кристи" "Это не совсем то, что я ожидала, но стоит отметить, ты выбрал крайне оригинальный и подходящий моему типажу наряд! "
    show GG Laughs
    "[gg]" "Ха-ха-ха!"
    show GG Laughs
    "[gg]" "Вообще-то это Харли Квин."
    show Christie Harly_Surprise
    "Кристи" "Кто?"
    show GG Normal
    "[gg]" "Ну как это «кто»? Известный персонаж комиксов, злодейка, подружка Джокера."
    show Christie Harly_Normal
    "Кристи" "Ааа… Вот оно что."
    show Christie Harly_Normal
    "Кристи" "Извини, ты же знаешь, я читаю только книги."
    show Christie Harly_Smile
    "Кристи" "Но Джокера я знаю!"
    show Christie Harly_Smile
    "Кристи" "Это антагонист из фильма «Тёмный рыцарь», верно?"
    show GG Smile
    "[gg]" "Ага."
    show Christie Harly_Smile
    "Кристи" "Ну что ж… Тогда я тоже не ошиблась с выбором."
    show Christie Harly_Normal
    "Кристи" "Конечно, я бы могла подобрать кого-то значимого, из классики… "
    show GG Surprise
    "[gg]" "М…?"
    show Christie Harly_Passion
    "Кристи" "Человек в железной маске, Призрак Оперы или… Дориан Грей."
    show Christie Harly_Normal
    "Кристи" "Но вряд ли эти костюмы можно купить в обычном магазине, так что я решила ограничиться ровно тем, как я понимаю, кто лично тебе понравится в качестве альтэр-эго! "
    show GG Surprise
    "[gg]" "И кто же этот негодник? "
    show Christie Harly_Smile
    "Кристи" "Джокер!"
    show GG Surprise
    "[gg]" "Джокер?!"
    show GG Surprise
    show Christie Harly_Laughs
    with my_dissolve
    "[gg]" "Фантастическое совпадение!!!"
    show Christie Harly_Smile
    "Кристи" "Ага, я тоже удивилась, когда ты сказал, что Харли его подружка. "
    show GG Normal
    "[gg]" "Гениальные умы мыслят одинаково! "
    show Christie Harly_Normal
    "Кристи" "Как здорово, что мы с тобой на одной волне."
    show GG Normal
    "[gg]" "Ещё бы!"
    show Christie Harly_Embarrassment
    "Кристи" "Так волнительно, что мы, наконец, друзья как и раньше."
    show GG Embarrassment
    "[gg]" "Ради этого я и прилагаю все усилия. "
    show Christie Harly_Embarrassment
    "Кристи" "И я, [gg]. Поверь, я тоже. "
    show GG Embarrassment
    "[gg]" "…"
    show GG Laughs
    "[gg]" "Ну так… Я пойду, переоденусь?"
    show Christie Harly_Normal
    "Кристи" "Ага."

    show GG:
        xzoom -1
        linear .5 xalign -1.1
    $ renpy.pause(.6, hard = True)

    show expression '#0000' with my_vpunch

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/aerosol-of-my-love-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "О БОЖЕЕЕЕЕЕЕЕЕ!!!"
    show Christie Harly_Surprise
    "Кристи" "Что случилось?!"
    show Christie:
        easein 1 xalign -1.1
    $ renpy.pause(1.25, hard = True)

    scene black with Dissolve(.5)

    $ renpy.pause(.9, hard = True)
    $ location_now = "GG_Room"

    call show_bg_image_label from _call_show_bg_image_label_144







    show GG Joker_Please
    show GG Joker_Please:
        xzoom -1
        xalign .9
    with my_dissolve
    show Christie Harly_Surprise
    show Christie Harly_Surprise at go_from_left(xxzoom=-1)

    "Кристи" "Что стрялось, [gg]?!"
    show Christie Harly_Surprise
    "Кристи" "Всё хорошо? Ты в порядке?"
    show Christie:
        xalign .15
    show GG Joker_Angry
    with my_vpunch
    "[gg]" "В порядке ли я?!.."
    show GG Joker_Please
    with my_vpunch
    "[gg]" "Посмотри на меня! Я же чёртов клоун!"
    show Christie Harly_Surprise
    "Кристи" "Хм… А что не так?.."
    show Christie Harly_Surprise
    show GG Joker_Please
    with my_dissolve
    "Кристи" "На сколько мне известно, Джокер это шут и носит маску шута. "
    show GG Joker_Angry
    "[gg]" "Да, но не такую же! "
    show GG Joker_Angry
    "[gg]" "Она должна быть мрачной, со стекающей краской по лицу и всё такое… "
    show GG Joker_WTF
    "[gg]" "Да кому я это объясняю?..."
    show GG Joker_Chagrin
    "[gg]" "Ты уже и не помнишь, наверное."

    show Milf Surprise
    show Milf Surprise:
        xzoom -1
        xalign -1.1
        easein .5 xalign .05
    show Christie:
        easein .5 xalign .5
        xzoom 1
    $ renpy.pause(.55, hard = True)
    show Milf Surprise:
        xzoom -1
        xalign .05
    show Christie:
        xalign .5
        xzoom 1
    show GG Joker_Embarrassment
    with my_dissolve
    "Марина" "Я слышала ваша крики, вы тут что, поубивать друг друга решили?!"
    show Milf Surprise
    show Christie Harly_Embarrassment
    with my_dissolve
    "Марина" "И почему, Кристи, ты выглядишь как дешёвая шлюха после разборок, а [gg]…"
    show GG Joker_Chagrin
    "[gg]" "Как обыкновенный детский клоун."
    show Milf Surprise
    show GG Joker_Please
    with my_dissolve
    "Марина" "Ну да. Именно. "
    show GG Joker_Chagrin
    "[gg]" "Всё в порядке, Марина, мы просто прикалываемся. "
    show Milf Normal
    "Марина" "Ох… Ладно."
    show Milf Normal
    "Марина" "Только не шумите так сильно, пожалуйста. "
    show GG Joker_Chagrin
    "[gg]" "Хорошо."

    show Milf Surprise:
        xzoom -1
        easein .5 xalign -1.1
    show Christie:
        easein .5 xalign .1
        xzoom -1
    $ renpy.pause(.55, hard = True)
    hide Milf
    show Christie Harly_Chagrin:
        xalign .1
        xzoom -1
    "Кристи" "Блиииин…."
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/daily-beetle-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Кристи" "Прости, я всё испортила."

    show GG Joker_Chagrin
    with my_dissolve
    "Кристи" "Я такая идиотка."
    show GG Joker_Embarrassment
    "[gg]" "Эй-эй, не надо так, Кристи."
    show GG Joker_Normal
    "[gg]" "Мы не на «Комик-Кон» идём, а на очень важную миссию."
    show GG Joker_Normal
    "[gg]" "Да, это совсем не то, что я планировал надеть… СОВСЕМ НЕ ТО!"
    show GG Joker_Smile
    "[gg]" "Но!..."
    show GG Joker_Normal
    "[gg]" "Главное, что меня в этом костюме никто не узнает. "
    show Christie Harly_Chagrin
    "Кристи" "Правда?.."
    show GG Joker_Normal
    "[gg]" "Правда."
    show Christie Harly_Embarrassment
    "Кристи" "И ты на меня не сердишься? "
    show GG Joker_Smile
    "[gg]" "Признаться, я не могу на тебя сердиться, когда ты выглядишь как… дешёвая шлюха после разборок, ха-ха-ха!"
    show Christie Harly_Laughs
    "Кристи" "Ахахахах! Ну ты и дурачок."
    show GG Joker_Normal
    "[gg]" "Раз уж мы подготовили свои костюмы, то в любое время сможем осуществить нашу слежку."
    show Christie Harly_Normal
    "Кристи" "Только не слишком рано, я люблю отоспаться. "
    show GG Joker_Normal
    "[gg]" "Эй, прекращай. Работа есть работа."
    show GG Joker_Normal
    "[gg]" "Жди моей команды, ясно?"
    show Christie Harly_Normal
    "Кристи" "Ладно. Постараюсь."
    scene black with Dissolve(.5)
    $ time.time_now = 'evening'



    $ descript_Christie= _("Отправить фотку Кристи Игорю.")
    $ events.pop('christie_root_34', 0)
    jump christie_root_35
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
