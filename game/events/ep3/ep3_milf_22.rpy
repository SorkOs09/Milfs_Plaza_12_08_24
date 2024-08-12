image Shop_Flower_Anim:
    'images/cg/ep3/Shop_Flower/1.png'
    .25
    'images/cg/ep3/Shop_Flower/2.png' with vpunch
    .5

    repeat















label ep3_milf_22:
    $ events.pop('ep3_milf_22', 0)

    scene expression '#000' with Dissolve(.5)

    $ renpy.play('audio/Door.mp3')

    call show_all_images_label from _call_show_all_images_label_22
    with Dissolve(.5)

    $ Event('talk_with_store_woman_label', 'StoreIn')





    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085



    show Misha Normal
    show Misha Normal:
        xalign .65
        ypos 1085

        xalign .95

    with Dissolve(.5)








    $ remove_from_inventory(name = 'Букет роз')
    "[gg]" "Добрый день."
    "Продавщица" "Ну типа. "
    show GG Flower
    "[gg]" "Это вам."
    show Misha Surprise
    "Продавщица" "Мне?!!"

    "[gg]" "Да. Подарок от вашего… ваших поклонников."


    show GG Normal

    show Misha Flower

    with Dissolve(.5)


    "Продавщица" "Оу. Здесь даже записка есть."

    show GG Embarrassment

    "[gg]" "Ну, я пошёл."



    "Продавщица" "Нет-нет, постойте. Я бы хотела вас отблагодарить. "

    show GG Laughs

    "[gg]" "Ох, не стоит себя так утруждать. Мне уже пора."



    "Продавщица" "О нет. Вы заслужили сполна, сударь. "




    scene expression '#000' with Dissolve(.5)

    $ renpy.pause(1, hard = True)

    $ renpy.music.stop(fadeout=.5)

    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)

    call show_all_images_label from _call_show_all_images_label_23
    show expression '#000a'
    show Shop_Flower_Anim:
        xpos -50

    with vpunch
    "Продавщица" "Ублюдок, мать твою. Говно собачье. Ананист чёртов! Вали отсюда, идиот, пока ещё жив! "
    "[gg]" "Что здесь творится?!!"
    "[gg]" "Эй-эй, прекрати! "
    "Продавщица" "По твоему это смешно, мудило, вручить мне цветы с запиской: “Слыш, детка, не хочешь мне отсосать?» "
    hide expression '#000a'


    show Jay Mobile
    show Jay Mobile:
        xpos -300
        ypos 1085
        xzoom -1


    show Bob Mobile
    show Bob Mobile:
        xpos -300
        ypos 1085
        xzoom -1




    show Jay Mobile:
        xzoom -1
        linear .5 xpos 500



    show Bob Mobile
    show Bob Mobile:
        ypos 1085
        xzoom -1

        linear .5 xpos 200


    $ renpy.pause(.55, hard = True)



    "Зудило" "Гы-гы-гы! А я говорил, Бубнило, будет натуральный трэш!"
    "Бубнило" "…."


    hide Shop_Flower_Anim



    show expression 'images/cg/ep3/Shop_Flower/1.png':
        xpos -50




    with Dissolve(.1)



    "Продавщица" "Зудило? Бубнило? Так это ваших рук дело?!"
    "Зудило" "Остынь, детка, это социальный эксперимент. Называется пранк! "
    "Продавщица" "Вот уроды! Сейчас и вы у меня огребёте! "





    call show_all_images_label from _call_show_all_images_label_24

    show Misha Chagrin
    show Misha Chagrin:
        xalign .65
        ypos 1085

        xalign .95



    show GG Surprise
    show GG Surprise:
        xpos 1000
        xzoom -1
        ypos 1085


    show Jay Mobile

    show Jay Mobile

    show Jay Mobile:
        ypos 1085
        xzoom 1
        xpos 500




    show Bob Mobile
    show Bob Mobile:
        ypos 1085
        xzoom 1

        xpos 200
    with vpunch

    $ renpy.pause(.5, hard = True)
    show Jay Mobile:
        xzoom 1
        linear .5 xpos -300
    show Bob Mobile:
        xzoom 1
        linear .5 xpos -300




    show Bob Mobile:

        xzoom 1

        linear .5 xpos -300








    show GG Surprise:
        xpos 1000
        ypos 1085
        linear .5 xpos -300



    $ renpy.pause(.5, hard = True)



    $ Event('ep3_milf_22_2', 'JayBob')

    $ descript =  _("Поговорить с Зудилой и Бубнилой.")
    scene expression '#000' with Dissolve(.5)

    $ location_now = 'City_Shop'




    jump main_interface_label




label ep3_milf_22_2:
    $ events.pop('ep3_milf_22_2', 0)

    show GG Angry
    show GG Angry:
        xalign .1
        ypos 1085

    show Jay Normal
    show Jay Normal:
        xalign .35
        ypos 1085

        xalign .65
    show Bob Normal
    show Bob Normal:
        xalign .65
        ypos 1085

        xalign .95

    with Dissolve(.5)







    "[gg]" "Какого хрена, чуваки?! "
    "Зудило" "Всё путём, чувачок. Ты отлично сыграл свою роль. "
    "[gg]" "Вижу, мне снова придётся воспользоваться своей битой. И на этот раз пострадает не только ваше самолюбие."
    "Зудило" "Алло! Это просто шутка. Мы пранкеры. Розыгрышь, понимаешь? Мы ведём свой канал на ютубе и пытаемся его раскрутить. А ты немного помог нам."
    "[gg]" "Насрать мне на ваш канал. Платить за билеты я не стану. Чтобы завтра, мать вашу, билеты были у меня."
    "Зудило" "Окей-окей. Сделаем, как и договаривались, не ссы."
    $ location_now = 'City_Shop'
    $ Event('ep3_milf_23', 'JayBob')
    $ descript =  _("Забрать билеты в театр у Зудилы и Бубнилы. ")

    $ time.time_now = 'evening'

    jump main_interface_label




    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
