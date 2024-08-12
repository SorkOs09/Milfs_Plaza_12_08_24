label cat_root_1:
    $ events.pop('cat_root_1', 0)
    call show_bg_image_label from _call_show_bg_image_label_102


    with Dissolve(.5)
    show GG Think
    show GG Think:
        xalign .2
    with Dissolve(.5)
    show GG Think
    with my_dissolve
    "[gg]" "Хм… Куда это Кэт подевалась?"
    show GG Think
    "[gg]" "Нет, конечно, я рад, что в моём расположении целая кровать, и никто не станет меня толкать посреди ночи, но всё же..."
    show GG Think
    "[gg]" "Надеюсь, она не принялась за старое ремесло и не вступила в новую банду."
    $ old_descript_Cat = 'S'
    $ descript_Cat = _('Обсудить с Кэт, куда она уходит ночью.')

    $ Event('cat_root_2', 'Cat')

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
