label ep5_milf_64:
    scene black
    with Dissolve(.5)
    $ events.pop('ep5_milf_64', 0)

    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    call show_all_images_label from _call_show_all_images_label_65
    with Dissolve(.5)













    $ renpy.pause(.5, hard = True)
    $ renpy.music.stop(fadeout=.5)

    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)
    show expression 'cg/ep5/Officer_Kick.png'
    with vpunch


    "Офицер" "Вот ты и попался, придурок!"

    "[gg]" "А я как раз о вас вспоминал…"


    "Офицер" "Сейчас я вылечу твой склероз."


    "Офицер" "И начну с разъяснительных работ на твоём самодовольной ебальнике."


    "[gg]" "Офицер?!"


    "Офицер" "Тебе повезло, что мне нравится Марина. "


    "Офицер" "Только поэтому ты сядешь в тюрьму нетронутым, а я, в свою очередь, смогу беспрепятственно встречаться с твоей подружкой."


    "[gg]" "Постойте! Послушайте меня!"


    "Офицер" "Ха-ха-ха!"


    "Офицер" "Вот как ты залепетал, сучоныш! "


    "Офицер" "Сейчас отведу тебя в участок, оформлю как барыгу галимого, а дальше пусть суд разбирается. "


    "[gg]" "С гонцами так не поступают…"


    "Офицер" "Кем?!"


    "[gg]" "С теми, кто приносят добрую весть…"


    "Офицер" "И что ты можешь мне сообщить, недоумок?!"


    "[gg]" "Что-то на счёт Марины, и вам определённо понравится эта информация."


    "Офицер" "Да ну?"


    "[gg]" "Ага. Но сперва вам стоило бы отпустить меня."


    "Офицер" "В последний раз я пожалел об этом. GG"


    "Офицер" "…."
    call show_all_images_label from _call_show_all_images_label_66
    show GG Normal
    show GG Chagrin:
        xalign .85
        ypos 1085
        xzoom -1
    show Officer Normal
    show Officer Normal:
        xalign .1
        ypos 1085


    with Dissolve(.5)

    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/loopster-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    show Officer Normal
    "Офицер" "И так."
    show Officer Normal
    "Офицер" "У тебя три секунды."
    show GG Normal
    "[gg]" "Так-то лучше."
    show Officer Normal
    "Офицер" "Моё терпение не безгранично."
    show GG Normal
    "[gg]" "Марина попросила передать вам, что приглашает вас вечером на ужин. "
    show Officer Skepticism
    "Офицер" "С чего вдруг?"
    show GG Normal
    "[gg]" "Я рассказал ей о вашем подарке."
    show Officer Surprise
    "Офицер" "О!"
    show Officer Surprise
    "Офицер" "Значит она в курсе?"
    show GG Smile
    "[gg]" "Ага."
    show Officer Surprise
    "Офицер" "А как мне понять, что ты не врёшь?"
    show GG Normal
    "[gg]" "Вы можете позвонить ей и уточнить день и время."
    show Officer Normal
    "Офицер" "Так и сделаю."
    show Officer Normal
    "Офицер" "Но потом."
    show Officer Normal
    "Офицер" "Можешь идти. Я знаю, где ты живёшь."
    show Officer Normal
    "[gg]" "До встречи, офицер. "

    show GG:
        linear 1 xalign .5

    show Officer Angry:
        xzoom -1
        linear 1 xalign -0.7


    $ renpy.pause(1)
    hide Officer

    show GG Think:
        xalign .5
    with my_dissolve
    "[gg]" "Подумать только, и этого хмыря я буду спасать от рук моего брата?!"
    show GG Think
    "[gg]" "Может, пусть задушит его и поделом?"
    show GG Think
    "[gg]" "Нет. Так нельзя."
    show GG Think
    "[gg]" "Я, конечно, зол на этого кретина, но не настолько, чтобы лишать его жизни. "
    show GG Think
    "[gg]" "Что ж. Мне пора в магазин, купить слабительное для этого дамского угодника."
    $ storein_shop_items = [_('Красное вино'), _('Попкорн'), _('Слабительное')]


    $ Event('ep5_milf_65_1', 'StoreIn')
    $ events.pop('talk_with_store_woman_label', 0)
    $ location_now = 'City_Home'

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
