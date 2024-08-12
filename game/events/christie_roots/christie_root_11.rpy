
image christie_root_11_JayBob_Store_original = Composite((1920, 1080),
(338, 422),  Crop((532,0,532,658), "cg/christie_root/misha_store/misha_store_atlas.png"))

image christie_root_11_JayBob_Store_blur = Composite((1920, 1080),
(324, 407),  Crop((562,673,562,673), "cg/christie_root/misha_store/misha_store_atlas.png"))





label christie_root_11:
    $ events.pop("christie_root_11", 0)



    $ location_now = 'StoreIn'

    scene expression 'locations/bg/StoreIn/afternoon_without_girl.png'
    show Misha Normal
    show Misha Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Costume_Normal
    show GG Costume_Normal at go_from_left





    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/late-night-radio-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    show GG Costume_Normal
    "[gg]" "Привет, скучаешь?"
    show Misha Passion
    show GG:
        xalign .15
    with my_dissolve
    "Мишванда" "Привееееет, красавчик."
    show Misha Surprise
    "Мишванда" "Что это… за?... Крепкий, душный, убойный…"
    show Misha Surprise
    "Мишванда" "Запах!..."
    show Misha Surprise
    "Мишванда" "Я… Сейчас…. Потеряю сознание."
    show Misha Surprise
    "Мишванда" "Помо… "
    show Misha Surprise
    "Мишванда" "Ги… "

    hide Misha

    show GG Costume_Surprise
    with vpunch


    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)

    "[gg]" "Чёрт!"
    show GG Costume_WTF
    "[gg]" "Она потеряла сознание."
    
    $ store.who_say_now = None
    
    $ store.nameboxes['GG'].state = "need_down"
    $ store.name_boxes_displ.force_update = True
    #$ renpy.pause(.1, hard = True)
    show Jay OMG
    show Jay OMG at go_from_left(xxalign = .0, xxzoom = -1)


    show Bob OMG
    show Bob OMG at go_from_left(xxalign = .15, xxzoom = -1)

    show GG:
        ease 1 xalign .6
    $ store.name_boxes_displ.force_update = False
    $ renpy.pause(1.2, hard = True)
    show Bob:
        xalign .15
        xzoom -1.0
    show Jay:
        xalign .0
        xzoom -1.0
    show GG:
        xalign .6
        xzoom 1
    with vpunch
    "Зудило" "Мать твою, чувак, мы просили её отвлечь, а не убивать!"
    "Зудило" "Ты зачем пришил сучку?!"
    show GG Costume_Angry:
        xzoom -1
    "[gg]" "Заткнитесь, придурки. Я её не касался."
    show GG Costume_WTF
    "[gg]" "Наверное, всё дело в моём одеколоне."
    "Зудило" "Верно подмечено, больной ублюдок, от тебя прёт как от дихлофоса!"
    "Зудило" "Ещё пять минут, и я сам отброшу копыта… "
    show GG Costume_Angry
    "[gg]" "Тогда поторопитесь, утырки, и сделайте столько снимков, чтобы дважды ходить не пришлось. "
    "Зудило" "Понял, шэф! "
    show GG Costume_WTF
    "[gg]" "А я пока попробую привести её в сознание."
    
    $ store.name_boxes_displ.block_render = True
    hide Jay
    hide Bob
    show christie_root_11_JayBob_Store_original
    with vpunch

    $ renpy.pause(.5, hard = True)








    show GG:
        ease 1.2 xalign .8
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    $ renpy.pause(1.5, hard = True)
    $ store.name_boxes_displ.block_render = False

    show GG:
        xalign .8
    with my_dissolve
    "Зудило" "Давай, Бубнило, жги!"
    "Зудило" "Я хочу, чтобы ты передал всю страсть, которую я истощаю здесь!"
    "Зудило" "Мы должен выдать качественный контент, а иначе нам не заплатят и цента."
    "Зудило" "Настоящие ценители прекрасного будут в полном восторге от моей персоны!"
    "Зудило" "Сделай как можно больше фоточек. Двадцать, нет, пятьдесяток фоток!"
    "Зудило" "С разных ракурсов, разумеется."
    show GG Costume_Skepticism
    "[gg]" "{i}Ну и придурки.{/i}"
    show GG Costume_Normal
    "[gg]" "{i}Мне срочно нужна вода, чтобы привести девчонку в порядок.{/i}"




    $ descript_Christie= _("Найти воду на полках магазина, чтобы привести продавщицу в порядок.")
    jump christie_root_12
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
