label cat_root_2:
    $ events.pop('cat_root_2', 0)
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/sneaky-adventure-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)



    "[gg]" "Как поживаешь? "
    show Kat Normal
    "Кэт" "Нормально, а что? Уже планируешь меня выгнать?"


    show GG Surprise
    "[gg]" "Эй, что ты! Конечно нет."
    show GG Skepticism
    "[gg]" "Всего лишь хочу узнать, где именно ты пропадаешь посреди ночи? "
    show Kat Angry
    "Кэт" "Моя личная жизнь тебя не касается."
    show GG Normal
    "[gg]" "Мне важно понимать, что ты не ищешь неприятностей, которые, раз уже ты живёшь здесь, могут коснуться и меня."
    show Kat Normal
    "Кэт" "Ах, ты об этом…"
    show Kat Normal
    "Кэт" "Нет, [gg], я ведь уже говорила тебе, что с криминалом покончено. "
    show GG Embarrassment
    "[gg]" "Хех… Ты стала называть меня по имени."
    show Kat Embarrassment
    "Кэт" "Пффф! Только из вежливости."
    show Kat Embarrassment
    "Кэт" "В конце-концов ты дал мне кров и всё такое."
    show GG Normal
    "[gg]" "Тогда скажи мне правду! "
    show Kat Normal
    "Кэт" "Не могу."
    show GG Normal
    "[gg]" "Но почему?"
    show GG Chagrin
    "[gg]" "Стыдно…"
    show GG Normal
    "[gg]" "Если у тебя какие-то проблемы, скажи мне! Я буду рад помочь."
    show Kat Angry
    "Кэт" "Хватит сверлить меня взглядом. Я не нуждаюсь в помощь, да и проблем никаких нет. "
    show Kat Angry
    "Кэт" "Если ты не доверяешь мне, и думаешь, что я снова погрязлаа в дерьме, я сегодня же съеду от тебя. "
    show Kat Angry
    "Кэт" "Cпасибо за гостеприимство и оривидерчи! "

    show Kat:
        linear 1 xalign .1
    show GG:
        linear 1 xalign .5
    $ renpy.pause(1)
    show GG Please:
        xzoom -1 xalign .5
    with my_dissolve


    "[gg]" "Останься, пожалуйста!"

    "[gg]" "Придёт время, и ты сам скажешь мне всё. Верно?"


    show Kat Normal:
        xzoom -1
    "Кэт" "Верно."
    show GG Normal
    "[gg]" "Вот и отлично. Чувствуй себя как дома."

    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/happy-days-in-summer-by-musiclfiles-from-filmmusic-io.mp3', fadein = 1.5)

    hide Kat
    show GG Think
    with Dissolve(.5)
    "[gg]" "Может скажет, а может и не скажет."
    show GG Think
    "[gg]" "Я слишком часто врал людям, чтобы доверять им на слово. "
    show GG Think
    "[gg]" "Придётся самому выяснить, куда это она пропадает каждую ночь. "
    show GG Think
    "[gg]" "Дождусь её вечером у подъезда, и прослежу, куда она идёт."
    show GG Think
    "[gg]" "Но прежде, мне нужна небольшая маскировка. "
    show GG Think
    "[gg]" "Чёрные очки, например."
    $ block_exit_home = False
    $ Event('cat_root_3_0', 'ClothesStore')
    $ events.pop('talk_with_clothes_store_woman_menu', 0)

    $ storein_costumes_shop_items = ['Чёрные очки']
    $ old_descript_Cat = 'S'
    $ descript_Cat = _('Купить чёрные очки.')
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
