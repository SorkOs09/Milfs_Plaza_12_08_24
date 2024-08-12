label final_act_20:    #Final_Act_20
    $ events.pop('final_act_20', 0)
    #$ time.time_now = "evening"

    #with Dissolve(.4)
    #$ renpy.pause(.5, hard = True)
    # show GirlOfficer Normal
    # show GirlOfficer Normal:
    #     xalign -.75
    #     xzoom -1
    #     ypos 1085
    #     easein_cubic 1.0 xalign .2
    $ from_say_screen = False
    #$ renpy.pause(1.0, hard = True)
    #"Description" "Я практически расшатал болты унитаза. Остался последний рывок. Надо подкачаться. Сильнее. Намного сильнее. Чтоб аж вены на лбу выскочили. "


    #Успешно активировать Унитаз 3 уровня (то есть, Ночью, при 70 СИЛЫ), после чего унитаз перестанет быть активным.




    #//GG_vs_Tualet_2

    "[gg]" "Воооооо!"
    "[gg]" "Наконец-то всё идёт как по маслу."
    "[gg]" "Унитаз сдвигается… "
    "[gg]" "Ещё… Ещё чуть-чуть."
    show final_act_gg_push_toilet 1
    with my_vpunch
    "[gg]" "ПОЛУЧИЛОСЬ!"
    hide final_act_gg_push_toilet# 1
    show GG Prison_Surprise
    show GG Prison_Surprise:
        xalign .85
        xzoom -1
    with my_dissolve
    #//Tablet_Box

    "[gg]" "Коробка?"
    "[gg]" "Интересно…"
    show GG Prison_WTF
    with my_dissolve
    "[gg]" "Что там внутри?"
    "[gg]" "Тааааак…."
    "//Add Item" "Таблетка"
    "//Описание" "Упакованная в целлофан таблетка. Состав неизвестен. "
    "[gg]" "Вместо с таблеткой была записка…"
    "[gg]" "На ней написано «Съешь меня, если хочешь выбраться». "
    show GG Prison_Surprise
    with my_dissolve
    "[gg]" "Чтобы это могло значить?"
    show GG Prison_Angry
    with my_dissolve
    "[gg]" "Не стану же я глотать хрен пойми что, найденное под дном унитаза."
    show GG Prison_Please
    with my_dissolve
    "[gg]" "А учитывая, что это «камера смертников», то таблетка с таким описанием явно не предвещает ничего хорошего."
    show GG Prison_Angry
    with my_dissolve
    "[gg]" "Я не собираюсь «выбираться» путём самоубийства."
    #//Функция занятия спортом тоже теперь недоступна
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_15
    $ renpy.pause(.3, hard = True)
    $ locations['Prison'].buttons[0].pop('toilet', 0)
    $ locations['Prison'].image_buttons_times['afternoon'].update(
        {'milf':Jump('final_act_21')}
        )
    $ descript = _("Отодвинув унитаз, я нашёл таблетку неизвестного содержания. К ней прилагалась записка «Съешь меня, если хочешь выбраться». Судя по всему, я потратил время впустую.")
    
    $ locations['Prison'].buttons[0].pop('toilet', 0)
        

    call final_act_blind_transition_to_black_label from _call_final_act_blind_transition_to_black_label_9
    
    $ time.time_forward(jump_to_main_interface = False)
        #time.time_now = 'morning'

    return