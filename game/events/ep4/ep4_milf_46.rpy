label ep4_milf_46:




    $ events.pop('ep4_milf_45', 0)









    call show_bg_image_label from _call_show_bg_image_label_27
    call show_additional_images_label from _call_show_additional_images_label_22
    show GG Normal
    show GG Normal:
        xalign 0
        ypos 1085



    show Milf Dress_Smile
    show Milf Dress_Smile:
        xalign 1.0
        ypos 1085


    show GG Costume_Normal
    show GG Costume_Normal:
        linear .5 xalign .1
        ypos 1085



    show Milf Dress_Smile
    show Milf Dress_Smile:
        linear .5 xalign .85
        ypos 1085

    $ renpy.pause(.75, hard = True)

    show Milf:
        xalign .85

    show GG Costume_Smile:
        xalign .1
    with my_dissolve
    "[gg]" "Ну как я?"
    show Milf Dress_Passion
    "Марина" "Арррр… Я завелась раньше времени."
    show GG Costume_Normal
    "[gg]" "Так что, мне уже раздеваться? "
    show Milf Dress_Normal
    "Марина" "Только после ужина."
    show GG Costume_Normal
    "[gg]" "Чего же мы ждём? "

    "Марина" "Веди меня, кавалер."
    $ descript = _('Отправиться в ресторан с Мариной.')
    $ Event('ep4_milf_46b',     'Corridor')
    $ block_time_forward = True





    jump main_interface_label



label ep4_milf_46b:
    $ Hide('main_interface')()

    $ events.pop('ep4_milf_46b', 0)

    $ location_now = 'Corridor'


    call show_bg_image_label from _call_show_bg_image_label_28
    call show_additional_images_label from _call_show_additional_images_label_23
    with Dissolve(.5)
    play sound 'audio/zvonok.mp3'
    $ renpy.pause(.5, hard = True)





    show GG Costume_Normal
    show Milf Dress_Normal

    show GG Costume_Normal:
        xalign .15
        ypos 1085

    show Milf Dress_Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    "Марина" "Кто бы это мог быть?"
    "[gg]" "Я открою."

    show GG Costume_Normal:
        xalign 0
        ypos 1085

    show Officer Normal
    show Officer Normal:
        xzoom -1
        xalign .85
        ypos 1085


    show Milf Dress_Normal:
        xzoom -1
        xalign .35
        ypos 1085

    with Dissolve(.5)


    "Марина" "Офицер?"
    show Officer Say
    "Офицер" "Да. Он самый. Прощу прощения, что явился без приглашения."
    show Milf Dress_Normal
    "Марина" "Ну что вы, всё в порядке. Просто мы собирались уходить и не ожидали такой встречи."
    show Officer Say
    "Офицер" "Забавно. А я как раз хотел предложить вам прогуляться. Ну, чтобы мы ещё раз обсудили все тонкости выписки вашего «подопечного» с полицейского учёта."
    show Milf Dress_Surprise
    "Марина" "Разве есть какие-то трудности? Мне казалось, мы закрыли этот вопрос. [gg] прекрасный парень! Он на деле доказывает своё исправление. "
    show Officer Say
    "Офицер" "Вам не о чем волноваться. Обыкновенная бюрократические волокита."
    show Officer Say
    "Офицер" "Я всего лишь хочу помочь вам составить его характеристику, чтобы у прокурора не возникло никаких подозрений."
    show GG Costume_WTF
    show Milf Dress_Normal
    "Марина" "Вы очень добры к нам, спасибо."

    show Officer Say
    "Офицер" "Что ж, тогда до встречи, верно?.."
    show Milf Dress_Normal
    "Марина" "Ну, наверное..."
    show GG Costume_Normal
    "[gg]" "До свидания, офицер!"
    show Officer Say
    "Офицер" "А хотя знаете…"
    show GG Costume_Chagrin
    "[gg]" "Чёрт… Что опять ему нужно?!"
    show Milf Dress_Normal
    "Марина" "Слушаю вас."
    show Officer Say
    "Офицер" " С моей стороны было бы преступлением вот так уйти и не выразить вам моё искреннее восхищение. Вы выглядите просто великолепно. "
    show Milf Dress_Embarrassment
    "Марина" "Вы заставляете меня краснеть, офицер. "
    show Officer Say
    "Офицер" "Поверьте, это чистая правда. Вы неотразимы. "
    show Milf Dress_Embarrassment
    "Марина" "Оу, вы такой джентльмен."
    show Officer Say
    "Офицер" "Особенно вам идёт этот кулон. Хе-хе. Если понимаете, что я имею в виду."
    show Milf Dress_Smile
    "Марина" "Хи-хи-хи. Это всё [gg]. Он подарил мне его."

    show Officer Hm
    "Офицер" "Что?!.. Что вы сказали?"
    show Milf Dress_Smile
    "Марина" "Последнее время его просто не узнать. [gg] стал настоящим пай-мальчиком. Заботливый, вежливый, и никаких нареканий."
    show Officer Hm
    "Офицер" "Да ну?"
    show Milf Dress_Smile
    "Марина" "О да. В немалой степени это ваша заслуга. Вы дали ему шанс, и он им воспользовался в полной мере. "
    show Officer Hm
    "Офицер" "Согласен. "
    show Milf Dress_Smile
    "Марина" "А сегодня он подарил мне этот замечательный кулон. Очень рада, что вы обратили на него внимание. Пусть это послужит доказательством его исправления. "
    show Officer Agr
    "Офицер" "Поверьте, я поражён не меньше вашего. "
    show GG Costume_Surprise
    show Officer Agr
    "Офицер" "У меня, признаться, нет слов. [gg], ты!.. "
    show Officer Agr
    "Офицер" "Ты…"
    show Officer Agr
    "Офицер" "Настоящий…"
    show Milf Dress_Normal
    "Марина" "…."
    show GG Costume_Surprise
    "[gg]" "…"
    show Officer Hm
    "Офицер" "…Молодец."
    show GG Costume_Smile
    "[gg]" "С-спасибо."
    show GG Costume_Surprise
    show Officer Say
    "Офицер" "Кажется я услышал, что хотел. И мне здесь делать нечего."
    show Officer Say
    "Офицер" "Ещё увидимся. "
    show Milf Dress_Normal

    "Марина" "Хорошего вам вечера, офицер."

    hide Officer
    show Milf Dress_Normal:
        xzoom 1
        xalign .85
        ypos 1085

    with Dissolve(.5)
    "Марина" "Мне показалось, будто бы полицейский был чем-то встревожен. "
    show GG Costume_Smile
    "[gg]" "Ты же знаешь, у них нервная работа. Наверное, просто стресс."
    show Milf Dress_Normal
    "Марина" "А ещё я совсем не хочу идти с ним навстречу, но боюсь, что если не сделаю это, он может обозлится и навредит тебе. "
    show GG Costume_Normal
    "[gg]" "Пустяки. Я разберусь."
    show Milf Dress_Surprise
    "Марина" "Ты сам с ним поговоришь?"
    show GG Costume_Normal
    "[gg]" "Да, кажется, мы найдём общий язык."
    show Milf Dress_Surprise
    "Марина" "Я тебе не верю."
    show GG Costume_WTF
    "[gg]" "Эй, ты же только что распиналась, какой я весь замечательный! "
    show Milf Dress_Embarrassment
    "Марина" "Я врала."
    show GG Costume_Smile
    "[gg]" "Ну ты и сучка."
    show Milf Dress_Angry
    "Марина" "Молодой человек!"
    show GG Costume_Chagrin
    "[gg]" "Ой. Молчу-молчу."
    show Milf Dress_Passion
    "Марина" "Теперь ты знаешь, кто доминирует в наших отношениях. "
    show GG Costume_Embarrassment
    "[gg]" "Ну хватит издеваться! Пойдём лучше в ресторан."
    show Milf Dress_Passion
    "Марина" "Идём. "

    scene black with Dissolve(.5)


    jump ep4_milf_47
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
