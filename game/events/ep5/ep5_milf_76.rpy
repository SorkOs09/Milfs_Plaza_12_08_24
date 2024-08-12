
label ep5_milf_76:























    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()
    $ events.pop('ep5_milf_76_stump', 0)



























    $ descript = _('Выйти из комнаты.')


    $ Event('ep5_milf_76_2', 'Corridor')
    jump main_interface_label
label ep5_milf_76_2:
    $ events.pop('ep5_milf_76_2', 0)

    call show_all_images_label from _call_show_all_images_label_20
    show Christie Surprise
    show Christie Surprise:

        xalign .9
    with Dissolve(.5)
    show GG Think
    show GG Think at go_from_left
    $ renpy.pause(1, hard = True)
    "Кристи" "Эй, что у вас тут произошло? "
    show GG Normal:
        xalign .15
    with my_dissolve
    "[gg]" "Ты уже слышала, да?"
    show Christie Surprise
    "Кристи" "Мама говорит, в дом проник грабитель, напал на маму и Джеймса… Кстати, когда он вернулся? И почему не отвечает на звонки?"
    show Christie Surprise
    "Кристи" "А потом, по словам мамы, рядом оказался полицейский… "
    show Christie Surprise
    "Кристи" "К слову о нём, что он у нас забыл? Кто-то может мне рассказать всё внятно?"
    show Christie Surprise
    "Кристи" "Но самое интересное, по словам мамы, конечно, что в конце появился ты и всех спас!!!"
    show Christie Surprise
    "Кристи" "Это правда? Звучит как полный бред."
    show GG Laughs
    "[gg]" "Я думаю, Марина сильно преувеличивает. "
    show Christie Normal
    "Кристи" "Тогда расскажи свою версию!"
    show GG Embarrassment
    "[gg]" "Знаешь, я и сам несколько обескуражен той ночью… И вряд ли адекватно оценил тогда обстановку. "
    show GG Embarrassment
    "[gg]" "Стечение обстоятельств… не более."
    show GG Embarrassment
    "[gg]" "Но у меня для тебя есть рассказчик, который с радостью поведает всё в мельчайших подробностях. "
    show Christie Surprise
    "Кристи" "Кто же это?"
    show GG Normal
    "[gg]" "Кэт. Моя подруга."
    show GG Normal
    "[gg]" "Она какое-то время поживёт у нас."
    show Christie Surprise
    "Кристи" "Чивоооо?! Какая ещё подруга?!"
    show GG Normal
    "[gg]" "Просто постучи в мою комнату, и сама всё узнаешь."
    show Christie Angry
    "Кристи" "Да вы тут рехнулись все, пока я гостила у подруги!"
    show GG Smile
    "[gg]" "Ха-ха-ха!"
    show GG Smile
    "[gg]" "Добро пожаловать в клуб шизов!"
    show Christie Normal
    "Кристи" "Мдэ… Пойду поздороваюсь с твоей Кэт."
    show GG Smile
    "[gg]" "Удачи."
    $ block_exit_home = True
    $ block_time_forward = True
















    $ descript = _("Поговорить с Мариной.")













    $ time.time_now = 'afternoon'
    $ Event('ep5_milf_76_3', 'Milf')
    $ milf_position = {
        'morning'   : ['Restroom',  'milf_kitchen'],
        'afternoon' : ['Kitchen',   'milf_kitchen'],
        'evening'   : ['Hall',      'milf_evening_hall'],
        'night'     : ['Milf_Room', 'milf_room'],
        }
    jump main_interface_label
label ep5_milf_76_3:
    call show_bg_image_label from _call_show_bg_image_label_19
    if time.time_now == 'evening':
        show Milf Night_Normal
        show Milf Night_Normal:
            xalign .8
    elif True:
        show Milf Normal
        show Milf Normal:
            xalign .8
    with Dissolve(.5)
    show GG Normal
    show GG Normal at go_from_left
    $ renpy.pause(1, hard = True)
    "[gg]" "Ты уже виделась с Кэт?"
    show GG:
        xalign .15
    "Марина" "Да, пока ты спал, эта шкодница напросилась в гости и всё у меня выведала."

    "Марина" "Она так сумбурно изъясняется, и постоянно бранится… её стоило бы поучить манерам, ты так не думаешь?"
    show GG Normal
    "[gg]" "Ей поздно меняться."

    "Марина" "Наверное ты прав."

    "Марина" "А ещё мне показалось… "

    "Марина" "Даже не знаю, как и сказать об этом, наверное я не так её поняла. "

    "Марина" "Но такое ощущение, будто бы она рассчитывает пожить с нами."
    show GG Normal
    "[gg]" "Ну…."
    show GG Laughs
    "[gg]" "На какое-то время."

    "Марина" "А разве ты не должен был сперва меня об этом спросить? "

    "Марина" "И Кристи предупредить, разумеется."
    show GG Chagrin
    "[gg]" "Извини… "
    show GG Chagrin
    "[gg]" "У неё сейчас некоторые трудности с жильём, а поскольку она сильно помогла мне, ну и вообще…"

    "Марина" "Да, я знаю, у вас получилось спасти Игоря. Очень рада за него."
    show GG Normal
    "[gg]" "Она опасается мести от людей Жлоба и рассчитывает на мою помощь."
    show Milf Smile
    "Марина" "Я не сержусь, милый. Пусть живёт, сколько нужно. "

    "Марина" "В рамках разумного, конечно."
    show Milf Chagrin
    "Марина" "Просто я чуточку… ревную."
    show Milf Chagrin
    "Марина" "Пойми и меня."
    show Milf Chagrin
    "Марина" " Молодая, похотливая плутовка в тесном пространстве с молодым, горячим парнем - мало ли, что может случиться!"
    show GG Smile
    "[gg]" "Хе-хе-хе!"
    show GG Smile
    "[gg]" "Если все силы я буду тратить исключительно на тебя, разве у меня будет повод заглядывать под трусики прочим девчонкам?"
    show Milf Passion
    "Марина" "Придётся привязать тебя к батарее, если я хочу быть уверенной в твоей благонадёжности. "
    show GG Laughs
    "[gg]" "Ээээ… Мне тяжело оправдаться."
    show Milf Passion
    "Марина" "Разве нам нужны слова, чтобы выразить друг другу чувства?"
    show GG Passion
    "[gg]" "Нет, но нам определённо нужна кровать. "
    show Milf Passion
    "Марина" "Тогда ты знаешь где меня найти сегодня ночью. "
    show Milf Passion
    "Марина" "И не шуми… теперь у нас слишком много соседей."
    show GG Smile
    "[gg]" "Пусть они стесняются, не мы."
    show Milf Passion
    "Марина" "Оу! Ты чертовски прав."



    $ block_time_forward = False
    $ events.pop('ep5_milf_76_3', 0)
    $ Event('ep5_milf_77', 'Milf_Room', time = ['night'])
    $ descript = _('Посетить спальню Марины сегодня ночью.')
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
