
label gg_room_bita_jay_bob_label:
    $ locations['GG_Room'].image_buttons.pop('bita', 0)
    $ events.pop('ep2_4_5_igor', 0)



    '[gg]' "Теперь мы посмотрим, как Зудило и Бубнило заговорят по новому."
    '[gg]' "Хотя, справедливости ради, Бубнило ничего не говорил."
    $ Event('ep2_4_jay_bob', 'JayBob')

    play sound 'audio/get_item.ogg'


    show screen give_item_screen(i_path+'/items/bita.png', _('Бейсбольная бита'), [_('Бейсбольная бита'), _('для пробивания человеческих черепов.')])


    with Dissolve(.5)
    $ renpy.pause(99999999)
    hide screen give_item_screen
    with Dissolve(.5)

    $ add_to_inventory(name = 'Бейсбольная бита')

    jump main_interface_label




label ep2_4_jay_bob:
    $ Event('ep2_4_jay_bob', 'JayBob')
    call show_bg_image_label from _call_show_bg_image_label_86
    call show_additional_images_label from _call_show_additional_images_label_72
    
    if get_item('Бейсбольная бита', inventory_check = True):
        show Jay OMG
        show Jay OMG:
            xalign .35
            ypos 1085
            zoom 1.0-0.035
            xalign .65
        show Bob OMG
        show Officer Normal
        show Officer Normal:
            xalign -1.2
            ypos 1085
            zoom 1.0-0.035

        show Bob OMG:
            xalign .65
            ypos 1085
            zoom 1.0-0.035
            xalign .95
        with my_dissolve

        show GG Bita
        show GG Bita at go_from_left
        '[gg]' "А ну валите нахер с моей точки, пока я вам все кости не переломал!!!"

        'Зудило' "Ладно-ладно, чувак! Только не по лицу!"

        show GG Bita_Normal:
            xalign .15
        '[gg]' "Так бы и сразу!"

        show Officer Normal:
            linear 1 xalign -.1
            ypos 1085
            zoom 1.0-0.035

        $ renpy.pause(1.2, hard = True)

        show Officer Normal:
            xalign -.1
            ypos 1085
            zoom 1.0-0.035


        show GG Normal:
            xzoom -1
            xalign .4
        with Dissolve(.5)
        $ renpy.pause(.1, hard = True)


        show Officer Normal
        show Jay Normal
        show Bob Normal
        "Офицер" "Так-так-так."
        show Officer Normal
        "Офицер" "Что тут у нас? Дуэль трёх мушкетёров"
        show Officer Normal
        "Офицер" "А где же Атос?"


        "Зудило" "Офицер, вы на каком языке сейчас говорите?"
        show Officer Normal
        "Офицер" "На языке Александра Дюма, бестолочи. "


        show Officer Normal
        "Офицер" "Зачем тебе бита, [gg]? "


        "[gg]" "Собираюсь заняться бейсболом"
        show Officer Normal
        "Офицер" "Я так понимаю, в качестве мячей выступают эти два обкурыша? "


        "Зудило" "Бубнило, это он про нас?"


        "Бубнило" "…."


        "Бубнило" "!!!!"


        "[gg]" "Нет, офицер. Мы просто беседовали."
        show Officer Normal
        "Офицер" "Это правда?"

        show Jay Normal
        "Зудило" "Правда-правда."
        show Officer Normal
        "Офицер" "И вам никто не угрожал минуту назад?"


        "Зудило" "Нет, офицер. "


        "Зудило" "Этот парень наш друг, и мы обсуждали нашу игру в бейсбол."
        show Officer Normal
        "Офицер" "«Этот парень»? Вы не знаете как звать вашего друга?"


        "Зудило" "Мы только что познакомились. "
        show Officer Normal
        "Офицер" "Как скажешь, Зудило. "
        show Officer Normal
        "Офицер" "Ваши проблемы останутся с вами, но биту я всё же заберу."
        show GG Angry
        "[gg]" "Но это моя бита!"


        show Officer Normal
        "Офицер" "Или ты мне её сейчас же отдашь, или мы поедем в участок."
        show GG Normal
        "[gg]" "Ладно, забирайте биту. "




        "Зудило" "Хорошего дня, офицер."
        show Officer Normal
        "Офицер" "Берегите головы, парни. "
        hide Officer
        show GG Angry:
            xzoom 1
            xalign .1
        with my_dissolve







        "Зудило" "Теперь тебе нечем угрожать, чувачок."


        "Бубнило" "…."
        show GG Angry
        "[gg]" "В следующий раз возьму кастет, и так же проломлю ваши черепа. "
        show GG Angry
        "[gg]" "Вы хотите испытывать меня на прочность? Я с радостью принимаю это вызов."


        "Зудило" "Ладно-ладно, парень. Остынь!"


        "Зудило" "Мы прекрасно тебя поняли и не хотим лишних проблем. "


        'Зудило' "Слушай, нас уже с третей точки прогоняют. Давай договоримся…"

        '[gg]' "Слушаю."
        show Jay Normal
        show Bob Normal
        'Зудило' "В любой момент, когда ты захочешь работать, мы освободим место. "
        'Зудило' "А в свою очередь, когда тебе понадобится какая-то особенная информация, или что-то, что не получится достать законным путём, мы всегда поможет тебе в этом."
        'Зудило' "Идёт?"

        '[gg]' "Звучит здраво."

        'Зудило' "Чувак, ты не пожалеешь!"
        hide Jay
        hide Bob
        with Dissolve(.5)
        $ renpy.pause(.6, hard = True)
        show GG Think:
            easein_cubic .75 xalign .5
        "[gg]" "Теперь я могу торговать наркотиками. Но прежде, чем делать это, я должен отправиться в парк и откопать несколько закладок"


        $ events.pop('ep2_4_jay_bob', 0)

        $ descript = _('Заработать немного денег на продаже наркотиков. Если мне понадобится товар для сбыта, я всегда могу добыть новые закладки в Парке. ')

        $ location_now = 'City_Shop'
        $ remove_from_inventory('Бейсбольная бита')
        if not hasattr(store, 'inventory_drugs'):
            $ inventory_drugs = 0

        $ Event('ep2_5_jay_bob_work_1', 'JayBob')

        jump main_interface_label






    show Bob Normal
    show Bob Normal:
        xalign .65
    show Jay Normal
    show Jay Normal:
        xalign .35
    with my_dissolve
    'Зудило' "{cps=25}Бля-бля-бля!{/cps}"
    show Jay dancing
    show Bob dancing
    'Зудило' "{cps=25}Сука твою мать{cps=3},{/cps} сука твою мать!{/cps}"
    show Jay dancing
    show Bob dancing
    'Зудило' "{cps=25}Бля-сука-бля{cps=3},{/cps} бля-сука-бля!{/cps}"
    show Jay Normal:
        linear .2 zoom 1.0-0.035
        xzoom -1
        linear .2 zoom 1.0
        xzoom 1
        linear .2 zoom 1.0-0.035
        pause .5
        xzoom -1
        linear .2 zoom 1.0
        xzoom 1
        linear .2 zoom 1.0-0.035
        xzoom -1
        linear .2 zoom 1.0
        xzoom 1
        linear .2 zoom 1.0-0.035

    'Зудило' "{cps=25}Шмалим дурь{cps=3}!{/cps} Курим шмаль!{/cps}"
    show Jay dancing
    show Bob dancing
    'Зудило' "{cps=25}Пиво пьём{cps=3}-{/cps}пьём{cps=3}-{/cps}пьём!{/cps}"
    show Jay dancing
    show Bob dancing
    'Зудило' "{cps=25}Косяки{cps=3},{/cps} бля{cps=3},{/cps} продаём!{/cps}"


    show GG Passion
    show GG Passion:
        xalign .1
        ypos 1085
        zoom 1.0-0.035
    show Jay Normal:
        xalign .35
        ypos 1085
        zoom 1.0-0.035
        xalign .65
    show Bob Normal:
        xalign .65
        ypos 1085
        zoom 1.0-0.035
        xalign .95
    with my_dissolve

    '[gg]' "Ёу, чуваки. А вы ещё кто такие?"
    'Зудило' "Меня звать Зудило, а это мой кореш – Бубнило."
    'Зудило' "Мы самые крутые торгаши в этом городе."
    'Зудило' "Кайфануть хочешь?"
    show GG Think
    with my_dissolve
    '[gg]' "Это мне стоило бы вас об этом спросить. Это моя точка."
    'Зудило' "Твоя? Это наша точка, чувак, и мы её доем. Вали, давай, не мешай вести бизнес."
    show GG Angry
    with my_vpunch
    '[gg]' "Вы сами напросились."
    
    'Зудило' "Ха, и что ты нам сделаешь?"
    
    '[gg]' "Скоро узнаете."
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_31
    hide Jay
    hide Bob
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    $ from_say_screen = False
    show GG Think:
        linear 1 xalign .5
    
    '[gg]' "Вот ублюдки. Надо их как-то прогнать отсюда. "
    '[gg]' "Мне нужно что-то, или кто-то, кто помог бы мне в этом деле."
    $ Event('ep2_4_5_igor', 'Igor', button_name = _("Помощь с Зудилой и бубнилой."))
    $ locations['GG_Room'].image_buttons['bita'] = [Jump('gg_room_bita_jay_bob_label')]

    $ location_now = 'City_Shop'
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
