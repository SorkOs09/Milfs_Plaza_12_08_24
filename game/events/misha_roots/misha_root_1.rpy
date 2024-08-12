image BlackGuy_1 = Transform("images/characters/BlackGuy/EMO/Normal.png", xzoom = -1)
image BlackGuy_2 = Transform("images/characters/BlackGuy/EMO/Normal.png", xzoom = -1)
image BlackGuy_3 = Transform("images/characters/BlackGuy/EMO/Normal.png", xzoom = -1)

image BlackGuy_4 = "images/characters/BlackGuy/EMO/Normal.png"
image BlackGuy_5 = "images/characters/BlackGuy/EMO/Normal.png"
image BlackGuy_6 = "images/characters/BlackGuy/EMO/Normal.png"

label misha_root_1:
    $ events.pop("misha_root_1", 0)





    call show_bg_image_label from _call_show_bg_image_label_137

    show Misha Surprise
    show Misha Surprise:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left







    "[gg]" "Привет."
    show Misha Surprise
    show GG:
        xalign .15
    with my_dissolve
    "Мишванда" "П-привет!"
    show Misha Surprise
    "Мишванда" "Откуда ты здесь взялся? "
    show GG Laughs
    "[gg]" "Да так, проходил рядом. "
    show GG Laughs
    "[gg]" "Увидел знакомую мордашку и решил подойти поздороваться. "
    show Misha Smile
    "Мишванда" "Значит, ты здесь не для того, чтобы ограбить меня?"
    show GG Smile
    "[gg]" "Хех…"
    show GG Smile
    "[gg]" "Меня зовут [gg]."
    show GG Smile
    "[gg]" "Я часто покупаю у тебя продукты."
    show Misha Normal
    "Мишванда" "Я прекрасно тебя помню, парень."
    show Misha Normal
    "Мишванда" "В магазине ты чуть не убил меня своим запахом одеколона. "
    show GG Chagrin
    "[gg]" "А ещё я привёл тебя в чувства. "
    show Misha Chagrin
    "Мишванда" "И мог обнести кассу, пока я был в отключке."
    show GG Chagrin
    "[gg]" "Я просто хотел тебя впечатлить…"
    show Misha Embarrassment
    "Мишванда" "Серьёзно? "
    show Misha Embarrassment
    "Мишванда" "Это ты ради меня так надушился?"
    show GG Embarrassment
    "[gg]" "Ну, если честно, то да."
    show Misha Embarrassment
    "Мишванда" "Даже не знаю, как на это реагировать…."
    show Misha Normal
    "Мишванда" "Я смущена и озадачена одновременно. "
    show GG Normal
    "[gg]" "Если хочешь, мы можем это обсудить, пока я провожу тебя домой."
    show Misha Normal
    "Мишванда" "….."
    show Misha Normal
    "Мишванда" "Ты вроде бы клёвый парень, но, знаешь ли, я не хочу показывать первому встречному, где я живу. "
    show GG Normal
    "[gg]" "Я могу провести тебя столько, сколько ты позволишь."
    show Misha Normal
    "Мишванда" "Хм…."
    show Misha Smile
    "Мишванда" "Ну ладно, чем чёрт не шутит. Погнали."
    show Misha Smile
    "Мишванда" "Меня зовут Мишванда, но если хочешь, можешь называть меня Миша."
    show GG Smile
    "[gg]" "Приятно познакомиться, Миша. Идём?"
    show Misha Normal
    "Мишванда" "Пошли."


    scene black with Dissolve(.5)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    $ location_now  = 'City_Getto'

    $ renpy.pause(.5)

    show expression 'cg/misha_root/pereulok.png'

    with Dissolve(.5)

    show Misha Normal
    show Misha Normal at go_from_right(xxalign=.7)

    show GG Normal
    show GG Normal at go_from_right(xxalign=.99, xxzoom = -1)




    $ renpy.pause(.5, hard = True)
    "[gg]" "Ну и райончик…"
    show GG:
        xalign .99 xzoom -1.0
    show Misha Chagrin:
        xalign .70
        xzoom -1
    with my_vpunch
    "Мишванда" "Какой уж есть. "
    show Misha Normal
    "Мишванда" "Если хочешь, можешь вернуться назад."

    show GG Embarrassment
    with my_dissolve
    "[gg]" "Нет-нет, я не боюсь, просто удивлён, что каждый день после работы ты возвращаешься через эти переулки, где в лучшем случае у тебя просто отнимут кошелёк, но поскольку ты девушка…"
    show Misha Smile
    "Мишванда" "Ха-ха-ха!"
    show Misha Laugh
    "Мишванда" "У тебя фантазия работает в «нужном» направлении."
    show GG Chagrin
    "[gg]" "Всего лишь пытаюсь трезво смотреть на вещи."
    show Misha Normal
    "Мишванда" "Я здесь выросла, [gg]."
    show Misha Normal
    "Мишванда" "Знаю здесь каждого наркомана, бомжа и дилера. "
    show Misha Normal
    "Мишванда" "Понимаю, с моих слов это звучит дико, но кроме полного отребья, в этом месте живёт полно хороших людей."
    show Misha Smile
    "Мишванда" "Например я, хи-хи!"


    $ renpy.pause(.4, hard = True)
    show Misha Smile:
        xzoom 1
    with my_dissolve

    $ renpy.pause(.3, hard = True)
    show GG Smile:
        ease 1.3 xalign .85

    show Misha Smile:

        ease 1.3 xalign .55
    $ renpy.pause(1.5, hard = True)
    "[gg]" "Ты украшение этого места."

    show Misha Laugh:
        xzoom -1
        xalign .55

    "Мишванда" "Ха-ха-ха!"
    show Misha Laugh
    "Мишванда" "Вот это умора, жги ещё!"
    show GG Surprise
    "[gg]" "Я сказал что-то не то?"
    show Misha Laugh
    "Мишванда" "Ха-ха-ха!"
    show Misha Laugh
    "Мишванда" "Вы только посмотрите на него, он даже не врубается!"
    show GG Chagrin
    "[gg]" "Эй, ну хватит!"
    show GG Chagrin
    "[gg]" "Я хотел сделать тебе комплимент…"
    show Misha Normal
    "Мишванда" "О да, у тебя шикарно получилось."
    show Misha Normal
    "Мишванда" "Разве ты не понимаешь, что ЛЮБОЙ более-менее вменяемый человек будет лучше этого места?"
    show Misha Normal
    "Мишванда" "Ты бы ещё ляпнул, что «я лучшая из худших!»"
    show GG Embarrassment
    "[gg]" "Воу…"
    show GG Embarrassment
    "[gg]" "И вправду неловко вышло."

    $ renpy.pause(.4, hard = True)
    show Misha Smile:
        xzoom 1
    with my_dissolve

    $ renpy.pause(.3, hard = True)
    show GG Smile:
        ease 1.3 xalign .7

    show Misha Smile:

        ease 1.3 xalign .35
    $ renpy.pause(1.5, hard = True)

    show Misha Laugh:
        xzoom -1
        xalign .35

    with my_dissolve

    "Мишванда" "Расслабься, [gg]. "
    show Misha Smile
    "Мишванда" "Ты прикольный парень, просто из другого мира."
    show GG Normal
    "[gg]" "Не торопись с выводами, ты плохо меня знаешь."
    show Misha Normal
    "Мишванда" "Хочешь сказать, тебе знакома жизнь в нищете? "
    show GG Normal
    "[gg]" "Нет, но хорош знаю тех, кто устраивает перестрелки у вас каждую ночь."
    show Misha Surprise
    "Мишванда" "Ты бандит?!"
    show GG Normal
    "[gg]" "Ну…"
    show GG Normal
    "[gg]" "Скорее я тот, кто пытается перестать им быть. "
    show Misha Normal
    "Мишванда" "Разве от прошлого можно убежать?"
    show GG Normal
    "[gg]" "Пытаюсь это выяснить на собственной шкуре."
    show Misha Normal
    "Мишванда" "И как, получается?"

    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    show Bandit Normal
    show Bandit Normal at go_from_left(xxzoom = -1, xxalign = -0.1)
    show BandtiWithPistol Normal
    show BandtiWithPistol Normal at go_from_left(xxzoom = -1, xxalign = 0.3)
    with None
    show Misha Chagrin:
        xzoom 1
        ease .5 xalign 0.6

    show GG Angry:
        ease .5 xalign 0.95
    with my_vpunch






    "Бандит" "О, какие люди в Голливуде!"
    show BandtiWithPistol:
        xzoom -1
        xalign .3
    show Bandit:
        xzoom -1
        xalign -.1
    with my_dissolve
    "Качок" "Сладкая парочка “Твикс», хе-хе-хе."



    show Misha Chagrin:
        ease 1 xalign .99
        xzoom 1

    show GG Angry:
        ease .5 xalign .75



    "[gg]" "Вот и ответ на твой вопрос, Миша."

    show Misha Chagrin:
        xalign .99
        xzoom 1
    with my_dissolve
    "Мишванда" "Вижу…"

    "Бандит" "Заткнись, мудак."

    "Бандит" "Это наше шоу, и мы в нём ведущие. "

    show GG Angry:
        xalign .75
    with my_dissolve
    "[gg]" "...."

    "Бандит" "Выворачивайте карманы, если не хотите быть выебаными в задницу. "

    "Качок" "При чём оба."
    show Misha Chagrin
    "Мишванда" "Ублюдки, я живу в этом районе. "
    show Misha Chagrin
    "Мишванда" "Когда ни будь я найду вас и…"

    show Misha Chagrin
    with my_dissolve
    "Бандит" "Ууууу, как страшно!"

    "Бандит" "Так может мне, чтобы избежать наказания, сразу прикончить тебя?"

    "Бандит" "Здесь и сейчас."
    show Misha Surprise
    "Мишванда" "[gg], мне страшно."

    "[gg]" "Сколько вам нужно денег, чтобы вы отстали?"

    "Бандит" "Таааак… Дай-ка посчитаю."

    "Бандит" "Ага, посчитал."
    with my_vpunch
    "Бандит" "ВСЕ ВАШИ ДЕНЬГИ!"

    "[gg]" "…."

    "Бандит" "А за то, что твоя сучка не умеет держать язык за зубами, пусть отсосёт мне. "
    show Misha Surprise
    "Мишванда" "[gg]… "
    show GG Skepticism
    "[gg]" "Альтернативные варианты имеются?"

    "Качок" "Ага. Можешь сам отсосать."

    "Бандит" "Ха-ха-ха-ха!!!"

    "Качок" "Ха-ха-ха!!!"

    "Качок" "Но если что, я не шучу. "
    show Misha Surprise
    "Мишванда" "Кажется у нас нет выхода, [gg]."
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .5
    with my_dissolve

    show Misha Normal
    with my_dissolve
    "Мишванда" "(шёпотом) Если хочешь, я сделаю как они говорят, и мы свободны."

    show GG Angry:
        xalign .65
        xzoom 1
    with my_dissolve
    "[gg]" "(шёпотом) Я не дам тебя в обиду."
    hide expression 'cg/ep45/shower_3/shadow.png'

    show GG Normal:
        xalign .75
        xzoom -1

    with my_dissolve

    "[gg]" "Эй, а если я дам вам больше денег, чем вы просите?"

    show BandtiWithPistol Asking
    with my_dissolve
    "Бандит" "Больше чем ВСЕ? "

    show BandtiWithPistol Passion
    with my_dissolve
    "Бандит" "Ты за кого нас держишь, мудак? "

    "Бандит" "Мы и так заберём все ваши деньги."
    show GG Normal
    "[gg]" "Речь идёт о тех деньгах, которых со мной нет."

    "Бандит" "Если их нет, значит их не существует."

    "Качок" "Дело говоришь. "
    show GG Skepticism
    "[gg]" "Моя подруга сходит за деньгами, а я останусь у вас в заложниках. "
    show GG Skepticism
    "[gg]" "Идёт?"

    "Бандит" "Я хочу, чтобы осталась твоя сисястая дамочка. И если ты сбежишь, нам будет с кем поразвлечься. "

    "Качок" "Нет, я не согласен."

    show GG Surprise
    show BandtiWithPistol Normal:
        xzoom -1
    with my_dissolve




    "Бандит" "Что?!"

    "Качок" "Пусть парень остаётся. Мне незачем развлекаться с этой шлюшкой."

    "Бандит" "Какого чёрта, братан?"

    "Качок" "В предыдущий раз мы делали так, как было угодно тебе, теперь мой черёд. "

    "Бандит" "Но у парня больше мотивации вернуться за девушкой!"

    "Качок" "Плевать. Пусть эта сучка валит на все четыре стороны."

    "Качок" "Мне нравится парнишка. "

    "Качок" "И я хочу, чтобы остался именно он."
    show GG Skepticism
    "[gg]" "Ну так что?"

    "Бандит" "Ладно, хер с тобой."

    show BandtiWithPistol Normal
    with my_dissolve
    "Бандит" "Точнее, видимо, твой хер останется с нами, а твоя тёлка пусть бежит за деньгами. "

    "Бандит" "И да, сколько она принесёт?"
    show Misha Surprise
    "Мишванда" "…."
    show GG Smile
    "[gg]" "Две штуки баксов. "

    "Бандит" "Ладно, ждём час."

    "Бандит" "Если она не вернётся, за твою жопу не ручаемся."
    show Misha Surprise

    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .5

    with my_dissolve

    "Мишванда" "(шёпот) Что мне делать, [gg]? У меня нет таких денег."
    show GG Normal:
        xalign .65
        xzoom 1
    with my_dissolve
    "[gg]" "(шёпот) Ты говорила, у тебя здесь полно знакомых."
    show Misha Chagrin
    "Мишванда" "(шёпот) Ага."
    show GG Normal
    "[gg]" "(шёпот) Ну вот и приведи кого-нибудь на помощь."
    show Misha Normal
    "Мишванда" "(шёпот) Поняла."
    hide expression 'cg/ep45/shower_3/shadow.png'

    show Misha:
        xzoom -1
    with Dissolve(.5)
    $ renpy.pause(.1, hard = True)
    show Misha:
        easeout_cubic .75 xalign 1.5
    show GG:
        xzoom 1
        ease .75 xalign .97
        xzoom -1
    $ renpy.pause(.75, hard = True)
    hide Misha
    with my_dissolve

    "Бандит" "Как думаешь, какова вероятность, что твоя подружка вернётся?"
    show GG Skepticism:
        xalign .97
        xzoom -1
    with my_dissolve
    "[gg]" "Ровно такая же, как та, что вы ничего не получите."

    "Качок" "Знаешь, парень, у тебя знакомая рожа."
    show GG Skepticism
    "[gg]" "У вас тоже запоминающиеся хари."
    show GG Skepticism
    "[gg]" "Вы работаете на Жлоба, верно?"

    "Качок" "А ты тот, кто торчит ему кучу бабок, да?"
    show GG Smile
    "[gg]" "Ха!"
    show GG Skepticism
    "[gg]" "Надеюсь, вы понимаете, что ограбив меня, вы ограбите своего босса, ведь все мои деньги – это его деньги? "

    "Качок" "….Чёрт."

    "Бандит" "Ты заговариваешь нам зубы, чувак!"


    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)

    show GG:
        ease 1 xalign 1.15
    show Bandit WTF:
        xzoom 1
        ease 1 xalign .2
    show BandtiWithPistol WTF:
        ease 1 xalign .45
    show BlackGuy_1
    show BlackGuy_1:
        xalign -1.5
        ease 1 xalign -.3

    show BlackGuy_2
    show BlackGuy_2:
        xalign -1.5
        ease 1 xalign -.15

    show BlackGuy_3
    show BlackGuy_3:
        xalign -1.5
        ease 1 xalign 0.0







    show BlackGuy_5
    show BlackGuy_5:
        xalign 1.5
        ease 1 xalign .87

    show BlackGuy_6
    show BlackGuy_6:
        xalign 1.5
        ease 1 xalign .7






    $ renpy.pause(1.2, hard = True)
    hide GG
    hide Misha
    show Misha Chagrin
    show Misha Chagrin:
        xzoom 1 xalign 1.5
    show GG Think
    show GG Think:
        xzoom -1
        xalign 1.15
    with my_dissolve
    show GG Think:

        ease .75 xalign .97
    show Misha:
        ease .75 xalign 1.15


    with None

    $ renpy.pause(.85, hard = True)

    show Misha:
        xalign 1.15
    show GG:
        xalign .97
    with my_dissolve
    "Мишванда" "Ну, что, сволочи, вам ещё охота со мной поразвлечься?!"
    with my_vpunch
    "Качок" "ЭЭээ… Пацаны-ребята!"

    "Качок" "Мы приносим свои глубочайшие извинения…"

    "Бандит" "Бес попутал, чувачки."

    "Бандит" "Просто хотели вас припугнуть, не более. "
    show Misha Chagrin
    with my_vpunch
    "Мишванда" "Чтоб я вас здесь не видела больше!"

    "Бандит" "Нам дважды повторять не надо…"
    show BandtiWithPistol:
        ease 1.0 xalign -1.5
    show Bandit:
        ease 1.0 xalign -1.5
    show BlackGuy_1:
        ease 1.0 xalign -1.5
    show BlackGuy_2:
        ease 1.0 xalign -1.5
    show BlackGuy_3:
        ease 1.0 xalign -1.5

    show BlackGuy_5:
        ease 1.0 xalign -1.5

    show BlackGuy_6:
        ease 1.0 xalign -1.5












    $ renpy.pause(1, hard = True)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    show GG Smile:
        ease 1.2 xalign .2

    show Misha Smile:
        ease 1.2 xalign .7

    $ renpy.pause(1.4, hard = True)
    show Misha Smile:
        xalign .7
    show GG:
        xalign .2
        xzoom 1
    with my_dissolve
    "[gg]" "Вау, Миша, на тебя можно положиться!"
    show GG Smile
    "[gg]" "Откуда ты знаешь этих ребят?"
    show Misha Normal
    "Мишванда" "Парни из баскетбольная команды."
    show Misha Normal
    "Мишванда" "Они играли на улице, где я живу. "
    show GG Normal
    "[gg]" "Нам повезло."
    show Misha Passion
    "Мишванда" "Нет, это мне повезло."
    show GG Surprise
    "[gg]" "А?.."
    show Misha Passion
    "Мишванда" "Ты сделал всё возможное, чтобы уберечь меня от беды."
    show GG Laughs
    "[gg]" "Ха! Разве я мог поступить иначе?"
    show Misha Passion
    "Мишванда" "Скромняжка."
    show GG Embarrassment
    "[gg]" "Конечно."
    show Misha Passion
    "Мишванда" "Обменяемся номерами?"
    show GG Embarrassment
    "[gg]" "Конечно."
    show Misha Smile
    "Мишванда" "Мы почти пришли, можешь возвращаться домой. Я живу прямо за углом. "
    show GG Normal
    "[gg]" "Ты уверена?"
    show Misha Smile
    "Мишванда" "Да, не волнуйся. Эти бандиты вряд ли захотят сюда вернуться. "
    show GG Normal
    "[gg]" "Ну ладно. До встречи."
    show Misha Smile
    "Мишванда" "До встречи."

    show Misha:
        easeout_cubic 1.5 xalign -.6
    $ renpy.pause(2, hard = True)

    scene black
    with Dissolve(.5)





    $ location_now   = "City_Home"



    $ descript_Misha = _("Подкатывать к Мише дальше.")

    $ Event('misha_root_1_5', 'GG_Room', priority = 10, day_start = time.day_now + 1)

    $ locations['City_Shop'].image_buttons_times['evening'].pop('misha', 0)

    $ locations['City_Shop'].image_buttons_times['night'].pop('misha', 0)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
