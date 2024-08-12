label christie_root_32:





    call show_bg_image_label from _call_show_bg_image_label_146

    show Christie Normal
    show Christie Normal:
        xalign .85
    with my_dissolve


    show GG Normal
    show GG Normal at go_from_left


    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/plain-loafer-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Ну что, ты готова повеселиться? "
    show GG:
        xalign .15
    show Christie Smile
    with my_dissolve
    "Кристи" "Нет, но раз уж я согласилась, придётся принять участие. "
    show GG Normal
    "[gg]" "Вот и отлично, отбрось всякие сомнения."
    show GG Normal
    "[gg]" "Первым делом мне нужно раздобыть маскировку."
    show GG Normal
    "[gg]" "Офицер меня знает в лицо и я бы не хотел загреметь в тюрячку из-за такой глупости. "
    show Christie Normal
    "Кристи" "Меня он тоже знает, я ведь со Сьюзен давно знакома."
    show GG Normal
    "[gg]" "Чёрт… Об это я как-то не подумал. "
    show GG Normal
    "[gg]" "Значит, нам обоим нужен костюм."
    show Christie Surprise
    "Кристи" "Прям костюм?!"
    show Christie Surprise
    "Кристи" "Накладных усов или покрашенных волос будет недостаточно? "
    show GG Passion
    "[gg]" "Только дилетанты себя ограничивают, а мы должны действовать творчески!"
    show Christie Laughs
    "Кристи" "Теперь не знаю, бояться мне или радоваться?.."
    show GG Silence
    "[gg]" "Довериться, Кристи. Просто доверься мне."
    show GG Normal
    "[gg]" "Я куплю нам обоим клёвые костюмы и мы сможем выдвинуться на слежку."
    show Christie Angry
    "Кристи" "Ну уж нет, я так не играю!"
    show GG Laughs
    "[gg]" "Хорошо-хорошо. Ты выберешь костюм себе, а я – себе. "
    show Christie Normal
    "Кристи" "Предлагаю вариант поинтереснее – я выберу тебе, а ты – мне! Идёт?"
    show GG Smile
    "[gg]" "Ха-ха-ха! Идёт!"
    show Christie Normal
    "Кристи" "Тогда до встречи. Скоро пойду за покупками."

    show Christie:
        linear 1.0 xalign -1.1
    show GG Think:
        linear 1.0 xalign .5
    $ renpy.pause(1, hard = True)
    hide Christie
    
    show GG:
        xalign .5
    with my_dissolve
    "[gg]" "Хм…"
   # show GG Think
    "[gg]" "Думаю, костюм Харли Квин подойдёт ей как нельзя кстати! "
  #  show GG Think
    "[gg]" "Раз уж она строит из себя пай-девочку, пусть побудет в роли отвязной бандитки."



    $ block_exit_home = False



    $ Event('christie_root_33', 'talk_with_clothes_store_woman_menu_after')

    $ Event('talk_with_clothes_store_woman_menu', 'ClothesStore')

    if not hasattr(store, 'storein_costumes_shop_items'):
        $ storein_costumes_shop_items = []
    if "Чёрные очки" in storein_costumes_shop_items:
        $ storein_costumes_shop_items.remove("Чёрные очки")

    $ storein_costumes_shop_items.append('Костюм Харли Квин.')


    $ descript_Christie= _("Сходить в магазин и купить костюм Харли Квин для Кристи.")
    $ events.pop('christie_root_32', 0)
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
