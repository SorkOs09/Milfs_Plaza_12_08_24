label tyan_falos_4_debug:
    $ location_now = 'Hall'
    scene black
    show image Text('DEBUG: Переход к ивенту tyan_falos_4'):
        align (.5, .5)
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call wait_click_label from _call_wait_click_label_46

label tyan_falos_4:
    $ events.pop('tyan_falos_4', 0)
#A task: 
    call show_bg_image_label from _call_show_bg_image_label_171
#1. Активировать Кристи Утром или Днём.
    show Christie Normal
    show Christie Normal:
        xalign .85
        ypos 1085
    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left

    "[gg]" "Вот твоя лягушка."
    "Кристи" "Вау!"
    show GG:
        xalign .15
    with my_dissolve
    "Кристи" "Видимо, ты основательно решил сделать перестановку в комнате, раз тебе НАСТОЛЬКО СИЛЬНО понадобилась линейка."
    
    "[gg]" "Это ещё и хороший повод помочь тебе вернуть свою вещь."
    "Кристи" "Хи-хи-хи! Ты прав. Спасибо."
    "Кристи" "На днях позвоню ей и заберу линейку."

    $ debug_next('tyan_falos_5_debug')
    $ tyan_falos_text = _("Подождать 2 дня, прежде чем я смогу получить линейку у Кристи.")

    $ Event('tyan_falos_5', 'Christie', button_name = _("Линейка"), day_start = time.day_now+2)
    $ new_events_christie = True
    jump main_interface_label
