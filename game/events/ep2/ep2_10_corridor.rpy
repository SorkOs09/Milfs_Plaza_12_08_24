label ep2_10_corridor:
    call show_bg_image_label from _call_show_bg_image_label_61

    call show_additional_images_label from _call_show_additional_images_label_55

    $ events.pop('ep2_10_corridor', 0)

    show Christie Angry
    show Christie Angry:
        xalign .32
        xzoom -1

        ypos 1085
        zoom 1.0-0.035
    show Milf Angry
    show Milf Angry:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)





    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    show Milf Angry
    "Марина" "Почему ты такая эгоистка?!"
    show Milf Angry
    "Марина" "Я всего лишь попросила тебя о маленьком одолжении!"
    show Christie Angry
    "Кристи" "Я не служанка, мама!"
    show Christie Angry
    "Кристи" "И не обязана слушать каждое твоё слово."
    show Milf Angry
    "Марина" "Что?!"
    show Milf Angry
    "Марина" "Ты уже не можешь зайти в магазин и купить продукты на завтрак?"
    show Christie Angry
    "Кристи" "Я же сказала, что просто забыла о твоей просьбе!"
    show Christie Angry
    "Кристи" "Это было не со зла. Чего ты ко мне привязалась?! "
    show Milf Angry
    "Марина" "Да, но зачем ты потратила все деньги?"
    show Christie Embarrassment
    "Кристи" "Я…"


    show GG Smile
    show GG Smile:
        xalign 0

        ypos 1085
        zoom 1.0-0.035
    show Christie Angry:

        xalign .4

        xzoom 1
        ypos 1085
        zoom 1.0-0.035

    with Dissolve(.5)
    "[gg]" "Что за шум, а драки нет?"
    show Christie Embarrassment
    "Кристи" "О, [gg], как хорошо, что ты пришёл."
    show Christie Skepticism
    "Кристи" "Мама обвиняет меня в краже денег!"


    show Milf Normal
    "Марина" "Я такого не говорила."
    show Christie Skepticism
    "Кристи" "Для меня это одно и тоже!"
    show Milf Normal
    "Марина" "Не строй из себя дуру."
    show Milf Normal
    "Марина" "Ты наказана. Марш в свою комнату!"
    show Christie Angry:
        xzoom -1
    "Кристи" "Эй!"
    show Milf Normal
    "Марина" "Живо, я сказала!"

    hide Christie
    show GG Normal
    with Dissolve(.5)
    "[gg]" "Ты не слишком строга с ней? "
    show Milf Normal
    "Марина" "Слишком добра, ты хотел сказать?"
    show GG Smile
    "[gg]" "Хе-хе-хе. "

    show GG Normal
    show Milf Chagrin
    "Марина" "Боже, ты прав. Я вспылила. "
    show Milf Chagrin
    "Марина" "Сейчас такой период, понимаешь…"
    show GG Normal
    "[gg]" "Я готов тебя поддержать, выкладывай."
    show Milf Chagrin
    "Марина" "Не сейчас, прости."



    hide Milf

    show GG Think
    with Dissolve(.5)
    "[gg]" "Я не могу бросить Марину в подавленном настроении и просить её о помощи, когда она сама в ней нуждается."

    show GG Think
    "[gg]" "Мои проблемы подождут."
    show GG Think
    "[gg]" "Уверен, совместный киносеанс под карамельный попкорн приведёт её в порядок."


    if love_milf >= 2:
        $ descript = _("Купить покорн и предложить Марине посмотреть сериал «Сладкий кексик». \nДополнительно: Накопить 150$ для перевода Игорю.")

        $ Event('ep2_11_film', 'Milf', time = ['evening'])
    elif True:


        $ descript = _('Требование: Привязанность Марины (2)')

        $ milf_love_quests = 2


    $ milf_position['evening'] = ['Hall', 'milf_evening_hall']

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
