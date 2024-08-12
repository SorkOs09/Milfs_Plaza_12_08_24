define time_tmp = 'night'
label go_sleep_to_morning:
    
    if all(store.ACH_5_count):
        $ store.add_ach('ACH_5')
    $ ACH_5_count = [False, False, False, False]
    scene black with Dissolve(.5)
    $ renpy.pause(1, hard = True)
    $ kompliment_day = False
    $ kompliment_day_christie = False
    $ podarok_day    = False
    $ gift_day       = False
    $ gift_day_christie = False
    $ film_today     = False
    if hasattr(store, 'milf_drunk'):
        $ milf_drunk = False
    $ ass_day        = False
    if hasattr(store, 'unlock_stirka'):
        $ block_wash_posuda = False
        $ block_stirka      = False
        $ block_uborka      = False
    if hasattr(store, 'christie_every_day_events_block'):
        $ christie_every_day_events_block = []
        $ events.pop('christie_night_mischief_night', 0)
        $ christie_night_mischief_text = _("Кристи мучают ночные кошмары. Стоит поговорить с ней об этом, может я смогу ей помочь.")

    $ sitost    = max(0,  sitost-2)
    $ gigiena   = max(0,  gigiena-2)
    $ nastroi   = min(100,  nastroi+3)

    $ block_gigiena = False
    $ block_eat     = False
    $ block_nastroi = False

    if hasattr(store, 'ACH_21_count'):
        $ ACH_21_count += 1
        if ACH_21_count >= 7:
            $ add_ach('ACH_21')


    $ money_boost_labels_click_today = []

    return
label bed_no_night:
    $ time.time_forward(jump_to_main_interface = False)
    if time.time_now != time_tmp:
        jump bed_no_night
    elif True:
        jump main_interface_label
label gg_room_bed:
    hide screen icons_interface
    with Dissolve(.2)
    python:
        location_now = 'gg_room_bed'
        check_ev = check_events()

        if check_ev:
            renpy.jump(check_ev.label)

        location_now = 'GG_Room'

        _block_time_forward_check = getattr(store, 'block_time_forward', False)

    if getattr(store, 'block_gg_room_bed', False):
        "[gg]" "Моя мягкая постель."
        jump main_interface_label

    menu:
        "Лечь спать." if time.time_now == 'night' and not _block_time_forward_check:

            call go_sleep_to_morning from _call_go_sleep_to_morning_1
            
            scene expression '#000' with Dissolve(.5)
            
            $ renpy.pause(1, hard = True)
            $ time.time_forward()


        "Отдохнуть." if time.time_now != 'night' and not _block_time_forward_check:
            scene expression '#000' with Dissolve(.5)
            $ renpy.pause(1, hard = True)
            $ time.time_forward()


        "Отдыхать до вечера." if time.time_now in ['morning', 'afternoon'] and not _block_time_forward_check:

            scene expression '#000' with Dissolve(.5)
            $ renpy.pause(1, hard = True)
            $ time_tmp = 'evening'
            jump bed_no_night

        "Отдыхать до ночи." if time.time_now != 'night' and not _block_time_forward_check:

            scene expression '#000' with Dissolve(.5)
            $ renpy.pause(1, hard = True)
            $ time_tmp = 'night'
            jump bed_no_night




        "Спать до следующего дня." if time.time_now != 'night' and not _block_time_forward_check:
            $ location_now = 'GG_Room'
            $ Hide('main_interface')()


            call go_sleep_to_morning from _call_go_sleep_to_morning
            $ time_tmp = 'morning'
            jump bed_no_night
        "Уйти." if True:






            pass

    jump main_interface_label
label gg_room_pc_black:
    scene expression '#000' with Dissolve(.5)
label gg_room_pc:
    if getattr(store, 'watch_porn_ep2', False) and time.time_now == 'night':
        jump watch_porn_ep2
    $ location_now = 'gg_room_pc_enter'
    $ check_ev = check_events()

    if check_ev:
        $ renpy.jump(check_ev.label)

    scene pc_bg with Dissolve(.5)
    call screen pc_interface
    scene expression '#000' with Dissolve(.5)
    $ location_now = 'gg_room_pc_exit'
    $ check_ev = check_events()

    if check_ev:
        $ renpy.jump(check_ev.label)

    $ location_now = 'GG_Room'
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
