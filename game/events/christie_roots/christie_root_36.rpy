label christie_root_36:









    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    scene black with Dissolve(.5)
    $ renpy.pause(.6, hard = True)

    scene expression 'cg/christie_root/Psi_Build.png'
    show expression 'cg/christie_root/officer_on_psi_build.png'

    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show Christie Harly_Normal
    show Christie Harly_Normal at go_from_right(xxalign=.9)

    show GG Joker_Normal
    show GG Joker_Normal at go_from_right(xxalign=1.15, xxzoom = -1)


    "[gg]" "Вон он, только-только вышел из дома."
    show Christie Harly_Skepticism:
        xalign .9
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .5
    with my_dissolve
    "Кристи" "Идти за ним?"
    show GG Joker_WTF:
        xalign 1.15
    with my_dissolve
    "[gg]" "Рано."

    "[gg]" "Пусть немного пройдёт вперёд. "

    "[gg]" "Приблизимся к нему позже. Когда он окажется в чуть более людных местах."
    show Christie Harly_Angry
    "Кристи" "А мы не слишком выделяемся из толпы?"
    show GG Joker_Angry
    "[gg]" "Кристи, сейчас не 18й век на дворе. "

    "[gg]" "Люди самовыражаются так, как пожелают. "

    "[gg]" "Красят волосы в зелёный цвет, протыкают кольца в ноздри, вставляют искусственные клыки себе в челюсть…"

    "[gg]" "По-твоему, на фоне такого числа фриков, кого-то удивят клоун с детского утренника и Харли Квин?"

    show Christie Harly_Skepticism
    "Кристи" "Надеюсь, ты прав. "

    hide expression 'cg/christie_root/officer_on_psi_build.png'
    show Officer Normal
    show Officer Normal:
        xalign .1
    with Dissolve(.5)
    $ renpy.pause(.9, hard = True)

    show Officer:
        xzoom -1
        easein 1.2 xalign -1.0
    show GG:
        ease .8 xalign .3

    show Christie:
        ease .8 xalign .8
    show expression 'cg/ep45/shower_3/shadow.png':
        ease .8 alpha 0.0
    $ renpy.pause(1, hard = True)


    show Officer:
        xzoom -1
        xalign -1.0
    show GG:
        xalign .3

    show Christie:
        xalign .8
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha 0.0


    "Кристи" "Гляди, он куда-то идёт."

    "[gg]" "Погнали."











    show GG Joker_Surprise:
        ease .8 xalign -1.6

    show Christie:
        ease .8 xalign -1.8
    $ renpy.pause(.85)



    scene black with Dissolve(.5)

    $ location_now  = 'City_Getto'

    $ renpy.pause(.5)

    scene expression 'locations/bg/City_Getto/morning.png'
    show expression 'cg/christie_root/officer_and_whore.png'
    with Dissolve(.5)


    show Christie Harly_Normal
    show Christie Harly_Normal at go_from_right(xxalign=.9)

    show GG Joker_Surprise
    show GG Joker_Surprise at go_from_right(xxalign=1.15, xxzoom = -1)


    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    call screen comic_frame(__("…Ведь ты знаешь, как я бываю зол."), 700, 600)
    call screen comic_frame(__("День только начался, ковбой. "), -150, 590, -1.0)
    call screen comic_frame(__("Могу отработать задницей, если желаешь."), -150, 590, -1.0)
    call screen comic_frame(__("Но за деньгами приходи позже."), -150, 590, -1.0)
    call screen comic_frame(__("Я с животными не сношаюсь."), 700, 600)
    call screen comic_frame(__("И в другой раз, просто прогоню тебя, если не прекратишь строить комедию. "), 700, 600)
    call screen comic_frame(__("Ой-ой-ой."), -150, 590, -1.0)
    call screen comic_frame(__("Уже боюсь."), -150, 590, -1.0)
    call screen comic_frame(__("Нарываешься. "), 700, 600)
    call screen comic_frame(__("Прекрати меня запугивать, ублюдок! "), -150, 590, -1.0)
    call screen comic_frame(__("Я же ясно тебе сказала – приходи ближе к ночи!"), -150, 590, -1.0)
    call screen comic_frame(__("Ты разочаровываешь меня."), 700, 600)
    with my_vpunch
    call screen comic_frame(__("Да пошёл ты."), -150, 590, -1.0)




    hide expression 'cg/christie_root/officer_and_whore.png'

    show Officer Normal
    show Officer Normal:
        xalign .1
    with Dissolve(.5)
    $ from_say_screen = False
    $ renpy.pause(.65, hard = True)

    show Officer:
        xzoom -1
        easein 1.2 xalign -1.0
    show GG Joker_Surprise:
        ease .8 xalign .1
        xzoom 1
    show Christie:
        ease .8 xalign .8
    $ renpy.pause(.85)







    "Кристи" "Он что, деньги у неё вымогал?"
    hide Officer
    show GG:
        xalign .1 xzoom 1
    show Christie:
        xalign .8
    with my_dissolve
    "[gg]" "Да, видимо это плата за место под солнцем. "
    show Christie Harly_Angry
    "Кристи" "Вот ублюдок!"
    show GG Joker_WTF
    "[gg]" "Поверь мне, в этой истории положительных героев нет."


    show GG Joker_Angry
    "[gg]" "Пошли скорее, а то упустим его!"
    show GG:
        xzoom -1
        easein 3 xalign -1.1
    show Christie:

        easein 3 xalign -1.1
    $ renpy.pause(.5, hard = True)
    scene black
    with Dissolve(.5)
    $ from_say_screen = False
    $ renpy.pause(.6)

    scene expression 'cg/misha_root/pereulok.png'

    with Dissolve(.5)


    show Christie Harly_Normal
    show Christie Harly_Normal at go_from_right(xxalign=.05)

    show GG Joker_Normal
    show GG Joker_Normal at go_from_right(xxalign=.9, xxzoom = -1)






    $ renpy.pause(1, hard = True)








    show Christie Harly_Normal:
        xzoom -1
        xalign .05
    show GG Joker_Angry:
        xzoom -1
        xalign .9
    with my_dissolve

    "[gg]" "Проклятье!"
    show GG Joker_Angry
    "[gg]" "Мы профукали его. "
    show Christie Harly_Surprise
    "Кристи" "Наверное он зашёл в один из домов."
    show GG Joker_Normal
    "[gg]" "Очевидно, но как мы теперь найдём его?"
    show Christie Harly_Normal
    "Кристи" "Никак…"


    show Officer Normal
    show Officer Normal:
        xalign -1.1
        easein .7 xalign .1
    show Christie:
        easein .7 xalign .5
        xzoom 1
    $ renpy.pause(.75, hard = True)
    $ from_say_screen = True
    show Officer Normal:
        xalign .1
    show Christie:
        xalign .5
        xzoom 1
    with my_dissolve
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Офицер" "Э..?"
    show Officer Normal
    with my_vpunch
    "Офицер" "Вы кто такие?! "

    show Christie:
        easein .25 xalign .9
    show GG:
        easein .25 xalign .7

    "[gg]" "А вы? Я и моя подруга просто гуляем."
    show Christie:
        xalign .9
    show GG:
        xalign .7
    show Officer Skepticism
    with my_dissolve
    "Офицер" "Ну да, конечно. Просто гуляете."
    show Officer Normal
    with my_vpunch
    "Офицер" "Вы решили здесь уединиться, верно? Но тут появился я и всё обломал."
    show Christie Harly_Passion
    "Кристи" "…"
    show GG Joker_Passion
    "[gg]" "Вы очень… проницательны, офицер. "
    show Officer Surprise
    "Офицер" "Ха-ха-ха!"

    "Офицер" "Ладно, молодёжь, не буду вас третировать лишний раз."
    show Officer Normal
    "Офицер" "Ну же, давайте! Чего стоите? "
    show GG Joker_Surprise
    show Christie Harly_Surprise
    with my_dissolve
    "[gg]" "Не понимаю вас, офицер. "
    show Officer Hm
    "Офицер" "Чего вылупился? Давай, еби её. Ты ж собирался или как?"
    show GG Joker_Angry
    with my_vpunch
    show Christie Harly_Skepticism
    with my_dissolve
    "[gg]" "Эй!!!"
    show GG Joker_Angry
    "[gg]" "Это очень грубо с вашей стороны!"
    show Christie Harly_Chagrin
    with my_dissolve
    "Кристи" "Я хочу уйти отсюда… "
    show Officer Say
    "Офицер" "Я могу заплатить. "
    show GG Joker_Surprise
    "[gg]" "…."
    show GG Joker_Surprise
    "[gg]" "Заплатить?"
    show Officer Normal
    "Офицер" "Да. Я заплачу вам за то, что вы потрахайтесь здесь и сейчас."
    show GG Joker_Surprise
    "[gg]" "Вы серьёзно?!"
    show Officer Normal
    "Офицер" "Абсолютно."
    show GG Joker_WTF
    "[gg]" "А вы что будете делать в этот момент?"
    show Officer Hm
    "Офицер" "Наблюдать и… получать удовольствие от процесса. "
    show Officer Hm
    "Офицер" "Ну так что? Идёт? Плачу пятьсот баксов. "
    show GG Joker_WTF
    "[gg]" "Вы ставите нас в неловкое положение, офицер. "
    show Christie Harly_Angry
    "Кристи" "Я хочу уйди отсюда. Сейчас же."
    show GG Joker_Angry
    "[gg]" "Моя подруга против. Мы уходим."
    show Officer Angry
    "Офицер" "Ну и валите!"

    show GG:
        xzoom 1
        easein 1.0 xalign 1.5

    show Christie:
        xzoom -1
        easein 1.0 xalign 1.5
    $ renpy.pause(.75, hard = True)




    show Officer Angry
    "Офицер" "Не шляйтесь здесь больше!"
    scene black with Dissolve(.5)
    $ time.time_now = "evening"


    $ location_now = "City_Home"

    call show_bg_image_label from _call_show_bg_image_label_145
    with Dissolve(.5)


    show Christie Harly_Normal
    show Christie Harly_Normal at go_from_left(xxalign=.1, xxzoom = -1)

    show GG Joker_Normal
    show GG Joker_Normal at go_from_left(xxalign=.9)

    $ renpy.pause(.8, hard = True)






    show GG:
        xzoom -1
        xalign .9
    show Christie Harly_Surprise:
        xzoom -1
        xalign .1
    with my_dissolve
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/full-moon-lofi-vibes-by-edikey20-from-filmmusic-io.mp3', fadein = 1.5)
    "Кристи" "Этот чёртов полицейский настоящий извращенец!!!"
    show Christie Harly_Chagrin
    "Кристи" "Я боюсь его, [gg]!"
    show Christie Harly_Surprise
    "Кристи" "А если в следующий раз он снова нас поймает так, что будет?"
    show GG Joker_Please
    "[gg]" "Ну всё-всё, вдох-выдох."
    show GG Joker_Normal
    "[gg]" "Да, он извращенец, но не маньяк же."
    show GG Joker_Smile
    "[gg]" "Наверное."
    show GG Joker_Normal
    "[gg]" "Просто увидел милую парочку и решил подколоть нас."
    show Christie Harly_Chagrin
    "Кристи" "У него получилось. Я вся дрожу! "
    show GG Joker_Angry
    "[gg]" "Кристи, я бы никогда не позволил причинить тебе вред. "
    show Christie Harly_Chagrin
    "Кристи" "У него есть оружие!"
    show Christie Harly_Chagrin
    "Кристи" "Он мог принудить нас! Это отвратительно!"
    show GG Joker_Chagrin
    "[gg]" "Да… Понимаю."
    show Christie Harly_Chagrin
    with my_vpunch
    "Кристи" "Нет-нет-нет!"
    show Christie Harly_Chagrin
    "Кристи" "Не такого ожидала от нашего «детективного» задания. "
    show GG Joker_Embarrassment
    "[gg]" "Чёрт…"
    show GG Joker_Chagrin
    "[gg]" "Извини, я слишком увлёкся своей ролью и подверг тебя опасности."
    show GG Joker_Chagrin
    "[gg]" "Мне не стоило тебя брать с собой."
    show Christie Harly_Chagrin
    "Кристи" "Здесь нет твоей вины, [gg], я сама согласилась тебя сопровождать. "
    show Christie Harly_Chagrin
    "Кристи" "Я знаю, ты привык рисковать и все, кто тебя окружали до этого, люди отчаянные…"
    show Christie Harly_Embarrassment
    "Кристи" "Я не такая."
    show Christie Harly_Chagrin
    "Кристи" "Я очень испугалась. Понимаешь? Для меня это огромный стресс. "
    show Christie Harly_Chagrin
    "Кристи" "Сейчас мне нужно время, чтобы прийти в себя."
    show Christie Harly_Chagrin
    "Кристи" "Не бери на свой счёт, [gg]. "
    show GG Joker_Please
    "[gg]" "Позволь мне…"

    hide Christie
    show GG Joker_Chagrin
    with my_dissolve
    "[gg]" "Эх…. Не стала слушать."
    show GG Joker_Chagrin
    "[gg]" "Да уж, будучи прилежной ученицей и примерным ребёнком, для неё этот эксцесс настоящий шок. "
    show GG Joker_WTF
    "[gg]" "Может, мне не стоило её вообще с собой брать?"
    show GG Joker_WTF
    "[gg]" "Сьюзен обещала мне совсем другого исхода…"
    show GG Joker_WTF
    "[gg]" "Нужно будет обговорить с ней этот вопрос."



    scene black with Dissolve(.5)

    $ time.time_now = "night"

    $ events.pop('christie_root_36', 0)

    $ Event('christie_root_37', "GG_Room", time = ['morning', ])


    $ descript_Christie= _("Сегодня я слишком устал, нужно просто лечь спать.")
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
