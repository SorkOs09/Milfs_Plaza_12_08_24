label tyan_falos_6_debug:
    $ location_now = 'Sister_Room'
    scene black
    show image Text('DEBUG: Переход к ивенту tyan_falos_6'):
        align (.5, .5)
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call wait_click_label from _call_wait_click_label_48

label tyan_falos_6:
    $ events.pop('tyan_falos_6', 0)
    #A task: 
    #1. Активировать комнату Кристи (тут надо чот придумать, чтобы не было конфликтов с другими квестами).
    #Scene:
    #// Wall_Kristy
    call show_bg_image_label from _call_show_bg_image_label_169
    with Dissolve(.5)
    show GG Think
    show GG Think at go_from_right(xxzoom = -1, xxalign = .53)
    $ renpy.pause(1, hard = True)
    show image 'cg/ep86/wall_0.png' with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .0
        easein 1 alpha .75
    "[gg]" "Ха, судя по отпечатку, она часто использует свой резиновый фалос."
    show GG:
        xzoom -1
        xalign .53
    with my_dissolve
    "[gg]" "Бедняжка… Но ничего, в этот раз я улучшу её опыт от «самоудовлетворения». "
    show image 'cg/ep86/wall_1.png' with my_dissolve
    "[gg]" "Всё, измерил." 

    $ debug_next('tyan_falos_7_debug')
    $ tyan_falos_text = _("Теперь мне нужно выждать момент, когда Кристи не будет дома и начать пилить стену. Лучше всего делать это Вечером.")

    $ Event('tyan_falos_7_0', 'Corridor', button_name = _("Линейка"), time = ['evening',])
    $ new_events_christie = True
    jump main_interface_label
