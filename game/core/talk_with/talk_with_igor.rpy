label talk_with_igor_label:
    call check_surv_label from _call_check_surv_label_3
    $ tmp_location_now  = copy.deepcopy(location_now)

    $ location_now = 'Igor'
    $ check_ev     = get_all_events_from_location()

    $ location_now      = copy.deepcopy(tmp_location_now)
    $ check_ev_buttons  = get_check_ev_buttons(check_ev)
    if len(check_ev_buttons) > 1:
        if 'christie' in check_ev[0].label:
            $ tmp_names_tmp_0 = check_ev_buttons[0]
            $ tmp_names_tmp_1 = __('Говорить (Задание Мэри)')
        elif 'christie' in check_ev[1].label:
            $ tmp_names_tmp_0 = __('Говорить (Задание Мэри)')
            $ tmp_names_tmp_1 = check_ev_buttons[1]
        elif True:
            $ tmp_names_tmp_0 = check_ev_buttons[0]
            $ tmp_names_tmp_1 = check_ev_buttons[1]

    $ create_talk_with_translates()

    menu:




        "[tmp_names_tmp_0]" if len(check_ev_buttons) > 1:
            $ Jump(check_ev[0].label)()
        "[tmp_names_tmp_1]" if len(check_ev_buttons) > 1:
            $ Jump(check_ev[1].label)()
        "Говорить." if len(check_ev_buttons) == 1:
            $ location_now = 'Igor'
            $ check_ev = check_events()
            $ location_now = 'City_Park'
            if check_ev:
                $ Jump(check_ev.label)()
        "Говорить." if not len(check_ev_buttons) and preferences.language in (None, 'eng', 'rus'):
            

            call show_bg_image_label from _call_show_bg_image_label_62
            call show_additional_images_label from _call_show_additional_images_label_56

            show Igor Normal
            show Igor Normal:
                xalign .85
                ypos 1085
                zoom 1.0-0.035
            with Dissolve(.5)
            show GG Normal
            show GG Normal at go_from_left
            '[gg]' "Как работа?"
            show Igor Ok
            'Игорь' "Пошёл в жопу."
            show Igor Normal
            'Игорь' "Ты уже придумал, где раздобыть деньги?"
            show GG Passion
            '[gg]' "Пошёл в жопу."

            jump main_interface_label




























        "Уйти" if True:
            $ location_now = 'City_Park'
            $ pass
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
