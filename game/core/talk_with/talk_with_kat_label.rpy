label talk_with_kat_label:
    call show_bg_image_label from _call_show_bg_image_label_107
    show Kat Normal
    show Kat Normal at go_from_right

    show GG Normal
    show GG Normal at go_from_left
    if preferences.language in (None, 'eng', 'rus'):
        'Кэт' "Соскучился, герой?"
    $ location_now_tmp = copy.deepcopy(location_now)
    $ location_now     = 'Cat'
    $ check_ev         = check_events()
    $ location_now     = copy.deepcopy(location_now_tmp)


    menu:
        "Поговорить." if check_ev:
            $ pass
            $ Jump(check_ev.label)()
        #"!Поговорить (in progress...)" if True:
        #    $ pass
        "Пошалить" if getattr(store, 'kat_shalost', False) and time.time_now == 'evening':
            jump cat_root_5
        #"!Сменить костюм (in progress...)" if True:
        #    $ pass
        "Уйти." if True:
            $ pass

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
