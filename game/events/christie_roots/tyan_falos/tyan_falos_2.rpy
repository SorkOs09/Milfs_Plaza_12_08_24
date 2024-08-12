label tyan_falos_2_debug:
    $ location_now = 'Hall'
    scene black
    show image Text('DEBUG: Переход к ивенту tyan_falos_2'):
        align (.5, .5)
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call wait_click_label from _call_wait_click_label_45

label tyan_falos_2:
    #1. Активировать Кристи Утром или Днём (не в ванной, разумеется).
    #Scene:"
    $ events.pop('tyan_falos_2', 0)
    call show_bg_image_label from _call_show_bg_image_label_170

    show Christie Normal
    show Christie Normal:
        xalign .85
        ypos 1085
    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left

    "[gg]" "Можно одолжить у тебя линейку?"
    "Кристи" "Можно, но сперва скажи зачем?"
    show GG Normal:
        xalign .15
    with my_dissolve
    "[gg]" "Да так, планирую сделать небольшую перестановку в комнате."
    "Кристи" "Так тебе не просто линейка, а рулетка нужна."
    show GG Normal
    "[gg]" "Верно."
    "Кристи" "Блин, мне не жалко, но свою рулетку я отдала одногруппнице из универа, а она не хочет возвращать её."
    show GG Normal
    "[gg]" "Почему?"
    "Кристи" "Как-то мне понадобилась лягушка на биологии, и подружка отдала мне свою. Но лягушка сбежала, и вернуть её я уже не смогла…"
    show GG Normal
    "[gg]" "Понял. Она взяла рулетку в качестве платы."
    "Кристи" "Ага."
    "[gg]" "Не такая уж она и подруга."
    "Кристи" "Тоже верно. "
    show GG Normal
    "[gg]" "Но если я добуду тебе лягушку, ты сможешь выменять её на свою рулетку?"
    "Кристи" "Вполне."
    show GG Normal
    "[gg]" "Тогда, я скоро вернусь. "
    hide Christie
    with Dissolve(.5)
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .0
        easein 3 alpha .75
    show GG Think:
        easein 3 xalign .5
    "[gg]" "{i}Вполне вероятно, что в Парке, где я роюсь в поисках закладки, я смогу поймать какую-нибудь заблудшую лягушку.{/i}"
    
    $ debug_next('tyan_falos_4_debug')
    $ tyan_falos_text = _("Вполне вероятно, что в Парке, где я роюсь в поисках закладки, я смогу поймать какую-нибудь заблудшую лягушку. ")
    $ new_events_christie = True
    $ Event('tyan_falos_3', 'City_Park_Search', button_name = _("Линейка"))
    
    jump main_interface_label 
