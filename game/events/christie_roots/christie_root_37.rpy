image christie_root_37_0a:
    'cg/christie_root/ep8_night/1.png' with Dissolve(.25)
    1
    'cg/christie_root/ep8_night/2.png' with Dissolve(.25)
    1
    'cg/christie_root/ep8_night/3.png' with Dissolve(.25)
    1
    'cg/christie_root/ep8_night/4.png' with Dissolve(.25)
    1


image christie_root_37_1a:
    'cg/christie_root/ep8_night/5.png'
    .15
    'cg/christie_root/ep8_night/6.png'
    .15
    'cg/christie_root/ep8_night/7.png'
    .15
    'cg/christie_root/ep8_night/8.png'
    .15
    'cg/christie_root/ep8_night/9.png'
    .15
    'cg/christie_root/ep8_night/10.png'
    .15
    'cg/christie_root/ep8_night/9.png'
    .15
    'cg/christie_root/ep8_night/8.png'
    .15
    'cg/christie_root/ep8_night/7.png'
    .15
    'cg/christie_root/ep8_night/6.png'
    .15

    repeat



image christie_root_37_1a_2:
    'cg/christie_root/ep8_night/5.png'
    .1
    'cg/christie_root/ep8_night/6.png'
    .1
    'cg/christie_root/ep8_night/7.png'
    .1
    'cg/christie_root/ep8_night/8.png'
    .1
    'cg/christie_root/ep8_night/9.png'
    .1
    'cg/christie_root/ep8_night/10.png'
    .1
    'cg/christie_root/ep8_night/9.png'
    .1
    'cg/christie_root/ep8_night/8.png'
    .1
    'cg/christie_root/ep8_night/7.png'
    .1
    'cg/christie_root/ep8_night/6.png'
    .1

    repeat




image christie_root_37_1a_3:
    'cg/christie_root/ep8_night/5.png'
    .075
    'cg/christie_root/ep8_night/6.png'
    .075
    'cg/christie_root/ep8_night/7.png'
    .075
    'cg/christie_root/ep8_night/8.png'
    .075
    'cg/christie_root/ep8_night/9.png'
    .075
    'cg/christie_root/ep8_night/10.png'
    .075
    'cg/christie_root/ep8_night/9.png'
    .075
    'cg/christie_root/ep8_night/8.png'
    .075
    'cg/christie_root/ep8_night/7.png'
    .075
    'cg/christie_root/ep8_night/6.png'
    .075

    repeat



image christie_root_37_1a_4:
    'cg/christie_root/ep8_night/5.png'
    .05
    'cg/christie_root/ep8_night/6.png'
    .05
    'cg/christie_root/ep8_night/7.png'
    .05
    'cg/christie_root/ep8_night/8.png'
    .05
    'cg/christie_root/ep8_night/9.png'
    .05
    'cg/christie_root/ep8_night/10.png'
    .05
    'cg/christie_root/ep8_night/9.png'
    .05
    'cg/christie_root/ep8_night/8.png'
    .05
    'cg/christie_root/ep8_night/7.png'
    .05
    'cg/christie_root/ep8_night/6.png'
    .05

    repeat

label christie_root_37:






    "[gg]" "Хррррр…."
    "[gg]" "Чавк-чавк-чавк…."
    "[gg]" "Хррррр…. Хррррр…."
    "[gg]" "Мням-мням-мням…."
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Голос" "Эййй…. Проснись."
    "Голос" "Просыпайся, соня…"

    "Голос" "Ну же, проснись!"



    $ location_now = 'GG_Room'
    $ time.time_now = "night"
    call show_bg_image_label from _call_show_bg_image_label_147
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .5
    show Christie Night_Embarrassment:
        xzoom -1
        xalign .1
    show GG Night_Surprise
    show GG Night_Surprise:
        xzoom -1
        xalign .9
    with my_dissolve
    "[gg]" "К..Кристи? Это ты? "
    "[gg]" "Ты почему не спишь? Который час?"

    "Кристи" "Я не могу уснуть, мне страшно. "

    "Кристи" "Та ситуация с полицейским никак не выйдет у меня из головы."

    "Кристи" "Прислушиваюсь теперь к каждому шороху и вздрагиваю от завывания ветра за окном."

    show GG Night_Please
    with my_dissolve
    "[gg]" "Ну… Если хочешь, я могу поспать у тебя в комнате на коврике."

    "Кристи" "Примерно это я и хотела тебя попросить сделать, но пока будила, поняла, что хочу другого…"

    show GG Night_Passion
    with my_dissolve
    "[gg]" "Да?"

    "Кристи" "А можно попросить тебя лечь со мной в кровати?"

    "[gg]" "Можно…"

    "[gg]" "Вот только у тебя очень маленькая кровать и нам… ну, ты понимаешь, может быть тесно. "

    "Кристи" "Плевать. "

    "Кристи" "Я хочу, чтобы ты был рядом. "

    "[gg]" "Хорошо, пойдём."
    show Christie:
        xzoom 1
        ease 1.5 xalign -1.0
    show GG:
        ease 1.5 xalign -1.0
    $ renpy.pause(1, hard = True)
label christie_root_37_scene:
    $ from_say_screen = False
    scene black with Dissolve(.5)
    scene expression 'cg/christie_root/ep8_night/Start.png'
    with Dissolve(.5)






    $ renpy.pause(.3, hard = True)
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    call screen comic_frame(_("Прижмись ко мне крепче и обними меня, [gg]."), 1220, 270)

    call screen comic_frame(_("Как скажешь…"), 110, 250, -1.0)
    call screen comic_frame(_("Сладких снов."), 1220, 270)
    call screen comic_frame(_("Сладких…"), 110, 250, -1.0)

    scene black with Dissolve(.5)
    if preferences.language in (None, 'eng', 'rus'):
        show expression Text(__('Какое-то время спустя…')):
            xalign .5 yalign .5

        with Dissolve(.5)

        $ renpy.pause(.3, hard = True)

        $ renpy.pause(9999)
    else:
        $ renpy.pause(1.0, hard = True)



    scene expression 'cg/christie_root/ep8_night/Start_END2.png'
    with my_dissolve
    call screen comic_frame(_("Кристи?.."), 110, 250, -1.0)
    call screen comic_frame(_("Пссс, Кристи."), 110, 250, -1.0)
    call screen comic_frame(_("Ты спишь?"), 110, 250, -1.0)
    call screen comic_frame(_("…"), 110, 250, -1.0)
    call screen comic_frame(_("Ну спи-спи."), 110, 250, -1.0)


    scene expression 'cg/christie_root/ep8_night/1.png' with my_dissolve
    call screen comic_frame(_("Так приятно лежать с ней рядом..."), 110, 250, -1.0)
    call screen comic_frame(_("Наблюдать за её умиротворённым сном..."), 110, 250, -1.0)
    call screen comic_frame(_("...и знать, что именно со мной она испытывает безопасность."), 110, 250, -1.0)
    call screen comic_frame(_("Тепло её нежного тела пьянит меня."), 110, 250, -1.0)
    call screen comic_frame(_("Запах её волос кажется сладким и дурманящим."), 110, 250, -1.0)
    scene expression 'cg/christie_root/ep8_night/2.png' with my_dissolve
    call screen comic_frame(_("Лежать с ней рядом, чувствовать её сладкий запах, прижиматься…"), 110, 250, -1.0)
    call screen comic_frame(_("Ох, это настоящее наслаждение…."), 110, 250, -1.0)
    call screen comic_frame(_("Моё сердце вот-вот вырвется от радости и…"), 110, 250, -1.0)
    scene expression 'cg/christie_root/ep8_night/3.png' with my_dissolve
    call screen comic_frame(_("…Возбуждения."), 110, 250, -1.0)
    call screen comic_frame(_("Ну же, идиот, приди наконец в себя и просто ляг спать!"), 110, 250, -1.0)
    call screen comic_frame(_("Хватит упиваться её запахом!"), 110, 250, -1.0)
    call screen comic_frame(_("Хватит впадать в экстаз от трепета её дыхания!"), 110, 250, -1.0)
    call screen comic_frame(_("Хватит!"), 110, 250, -1.0)
    call screen comic_frame(_("…."), 110, 250, -1.0)
    call screen comic_frame(_("Нет, так я никогда не смогу уснуть."), 110, 250, -1.0)
    call screen comic_frame(_("Мне остаётся лишь оставить её одну или успокоить себя силой воли."), 110, 250, -1.0)
    call screen comic_frame(_("Ну да… Какой к чёрту воли?"), 110, 250, -1.0)
    call screen comic_frame(_("Ммм…."), 110, 250, -1.0)
    call screen comic_frame(_("Ладно."), 110, 250, -1.0)
    scene expression 'cg/christie_root/ep8_night/4.png' with my_dissolve
    call screen comic_frame(_("Я думаю, мои действия не будут истолкованы ею превратно, если я немного пошалю с ней."), 110, 250, -1.0)
    call screen comic_frame(_("В конце концов, я не собираюсь переходить границы."), 110, 250, -1.0)
    call screen comic_frame(_("Верно я говорю?"), 110, 250, -1.0)
    call screen comic_frame(_("Конечно, верно!"), 110, 250, -1.0)
    call screen comic_frame(_("Я же обращаюсь ни к кому-то..."), 110, 250, -1.0)
    call screen comic_frame(_("А к себе!"), 110, 250, -1.0)


    scene christie_root_37_1a


    call screen comic_frame(_("Аххх…"), 1240, 170, i_p = True)
    call screen comic_frame(_("Ну наконец-то."), 1240, 170, i_p = True)
    call screen comic_frame(_("Как же долго он решался."), 1240, 170, i_p = True)
    call screen comic_frame(_("Я знала, что нечто такое случится и всё равно пригласила его к себе."), 1240, 170, i_p = True)
    call screen comic_frame(_("Мне бы очень хотелось, чтобы он сам сделал первый и главный шаг."), 1240, 170, i_p = True)
    call screen comic_frame(_("Или, даже, надавил бы на меня, развеяв мои сомнения."), 1240, 170, i_p = True)
    call screen comic_frame(_("Но он, как и положено, ждёт взаимности."), 1240, 170, i_p = True)
    call screen comic_frame(_("А я слишком боюсь, чтобы принять это решение самостоятельно."), 1240, 170, i_p = True)
    call screen comic_frame(_("Ну да и пусть…"), 1240, 170, i_p = True)
    call screen comic_frame(_("Сейчас мне слишком хорошо, чтобы забивать голову будущими проблемами."), 1240, 170, i_p = True)
    call screen comic_frame(_("Надеюсь, он не планирует остановиться слишком быстро…"), 1240, 170, i_p = True)

    menu:
        "Ускориться" if True:
            $ pass

    scene christie_root_37_1a_2





    call screen comic_frame(_("Постараюсь быть нежным, насколько это возможно."), 110, 250, -1.0)
    call screen comic_frame(_("Не хотелось бы тревожить её сладкий сон."), 110, 250, -1.0)
    call screen comic_frame(_("Хотя, конечно, мне жутко сложно сдержаться и не ускориться в десятки раз сильнее, ведь я буквально горю от жажды возбуждения."), 110, 260, -1.0)
    call screen comic_frame(_("У меня такой сильное сердцебиение, что, кажется, оно слышно даже в коридоре."), 110, 250, -1.0)
    call screen comic_frame(_("Оххх… Кристи, какая же у тебя мягкая, круглая, упругая попочка…."), 110, 250, -1.0)
    call screen comic_frame(_("Нельзя быть настолько совершенной, находясь рядом с тем, кто поклоняется такой красоте."), 110, 250, -1.0)

    menu:
        "Ускориться" if True:
            $ pass

    scene christie_root_37_1a_3


    call screen comic_frame(_("О да…. Кажется, его чувство бдительности притупилось."), 1240, 170, i_p = True)

    call screen comic_frame(_("[gg] так яростно трётся об меня, что я уже вся теку."), 1240, 170, i_p = True)

    call screen comic_frame(_("Его толчки становятся всё сильнее и яростнее, будто бы он намеревается пройти в меня сквозь мои влажные от возбуждения трусики."), 1240, 170, i_p = True)

    call screen comic_frame(_("И мне это нравится!"), 1240, 170, i_p = True)

    call screen comic_frame(_("Лучше бы он снял их с меня, и просто сделал то, что должен."), 1240, 170, i_p = True)

    call screen comic_frame(_("Или я сделаю это сама…"), 1240, 170, i_p = True)

    call screen comic_frame(_("Нет, не могу."), 1240, 170, i_p = True)

    call screen comic_frame(_("Это будет выглядеть глупо. Он сразу поймёт, что я не спала всё это время."), 1240, 170, i_p = True)

    call screen comic_frame(_("Ну же, [gg], будь напористее!"), 1240, 170, i_p = True)

    call screen comic_frame(_("Сильнее, ещё сильнее!"), 1240, 170, i_p = True)

    call screen comic_frame(_("Я совсем обнаглел…."), 110, 250, -1.0)

    call screen comic_frame(_("Даже удивительно, как крепко она спит, ведь я буквально выталкиваю её с кровати."), 110, 250, -1.0)

    call screen comic_frame(_("Скоро я оставлю тебя в покое, Кристи, скоро ты сможешь спать как и прежде…"), 110, 250, -1.0)

    call screen comic_frame(_("Я уже подхожу к кульминации…."), 110, 250, -1.0)

    call screen comic_frame(_("Даааа…. Ещё совсем чуть-чуть. Не могу больше сдерживать себя."), 110, 250, -1.0)


    menu:
        "Кончить" if True:
            $ pass
    scene christie_root_37_1a_4


    call screen comic_frame(_("Вот так, ещё совсем немного!"), 120, 250, -1.0)
    call screen comic_frame(_("Я чувствую каждый изгиб её сладкой, мокрой киски!"), 130, 250, -1.0)
    call screen comic_frame(_("Её тёплые соки буквально обжигают мой изголодавшийся член."), 110, 250, -1.0)
    call screen comic_frame(_("Даааааааа!!!"), 110, 250, -1.0)
    scene white with Dissolve(.5)

    $ renpy.pause(1, hard = True)

    scene expression 'cg/christie_root/ep8_night/11.png'
    with Dissolve(.75)

    $ renpy.pause(.9, hard = True)


    call screen comic_frame(_("Всё…."), 120, 250, -1.0)
    call screen comic_frame(_("Я кончил."), 120, 250, -1.0)
    call screen comic_frame(_("Даже слишком…."), 120, 250, -1.0)
    call screen comic_frame(_("Приятных сновидений."), 120, 250, -1.0)
    call screen comic_frame(_("Миленькая моя..."), 120, 250, -1.0)
    call screen comic_frame(_("Успокоился, вроде бы…"), 1240, 170, i_p = True)

    call screen comic_frame(_("Судя по всему, он удовлетворён."), 1240, 170, i_p = True)

    call screen comic_frame(_("Хи-хи-хи."), 1240, 170, i_p = True)

    scene expression 'cg/christie_root/ep8_night/12.png' with my_dissolve
    call screen comic_frame(_("Теперь буду спать как убитый."), 120, 250, -1.0)
    call screen comic_frame(_("И я тоже."), 1240, 170, i_p = True)

    scene black with Dissolve(.5)

    if getattr(store, "from_tyan_sleep_event", False):
        $ from_tyan_sleep_event = False
        return

    $ renpy.pause(.75, hard = True)
    $ location_now  = 'Sister_Room'
    $ time.time_now = 'afternoon'


    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    call show_bg_image_label from _call_show_bg_image_label_148

    show Christie Night_Normal
    show Christie Night_Normal:
        xalign .9

    show GG Normal
    show GG Normal:
        xalign .1
    with my_dissolve

    "Кристи" "Доброе утро, [gg]!"
    "[gg]" "Доброе, Кристи."

    "Кристи" "Спасибо, что согласился провести эту ночь со мной. "

    "[gg]" "Готов это делать хоть каждый день."

    show Christie Night_Smile
    with my_dissolve
    "Кристи" "А я и не против."

    "Кристи" "Приходи ко мне ночью, когда пожелаешь. "

    "[gg]" "Воу!… Хорошо."

    "Кристи" "Теперь, если ты не против, я бы хотела переодеться. "

    "[gg]" "Ага. Удачного дня! "
    show GG:
        xzoom -1
        linear 1 xalign -1.2
    $ renpy.pause(.6, hard = True)
    scene black
    with Dissolve(.5)
    $ location_now = 'Corridor'







    call show_bg_image_label from _call_show_bg_image_label_149

    show Milf Embarrassment
    show Milf Embarrassment:
        xalign .9
    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_left

    "Марина" "[gg], мне привиделось или ты только что вышел из комнаты Кристи?"
    show GG Please:
        xalign .15
    with my_dissolve
    "[gg]" "Эм… Да."
    show GG Normal
    "[gg]" "Ей снились кошмары и она попросила меня поспать у неё на коврике."
    show Milf Embarrassment
    "Марина" "Ах вот оно что…"
    show Milf Passion
    "Марина" "Оууу!"
    show Milf Passion
    "Марина" "Теперь я знаю к кому обращаться с такими просьбами, хи-хи-хи."
    show Milf Passion
    "Марина" "Порой, мне такие страсти по ночам сняться…уххх!"
    show GG Laughs
    "[gg]" "В любое время дня и ночи, Марина! Только скажи."
    show Milf Laughs
    "Марина" "Ха-ха-ха!"
    show Milf Normal
    "Марина" "Ладно уж, иди, рыцарь. "
    show Milf Laughs
    "Марина" "И да, постарайся не вляпываться в неприятности."
    show GG Normal
    "[gg]" "Постараюсь."

    $ debug_exit()

    if not from_gallery_check() and not _just_scene:
        $ events.pop('christie_root_37', 0)
        $ events.pop('christie_root_34', 0)
        $ events.pop('christie_root_28', 0)
        $ Event('christie_root_38', 'City_Psi', time = ['morning', 'afternoon'])


        $ unlock_city_psi   = True
        $ add_to_gallery(29)


        $ descript_Christie= _("Сходить на приём к Сьюзен и рассказать ей известную информацию о муже.")
    else:
        $ _just_scene = False
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
