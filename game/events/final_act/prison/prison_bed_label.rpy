label prison_bed_label:
    
    $ _block_time_forward_check = getattr(store, 'block_time_forward', False)

    menu:
        "Покушать" if time.time_now == 'night' and hasattr(store, 'prison_food_activate'):
            if 'food' in locations['Prison'].image_buttons_times['night']:
                $ locations['Prison'].image_buttons_times['night']['food']()
            jump final_act_12_repeat
        "Лечь спать." if time.time_now == 'night' and not _block_time_forward_check:

            call go_sleep_to_morning from _call_go_sleep_to_morning_2 

            scene black with Dissolve(.5)
            
            $ renpy.pause(1, hard = True)
            $ time.time_forward()


        "Отдохнуть." if time.time_now != 'night' and not _block_time_forward_check:
            scene black with Dissolve(.5)
            $ renpy.pause(1, hard = True)
            $ time.time_forward()


        "Отдыхать до вечера." if time.time_now in ('morning', 'afternoon') and not _block_time_forward_check:

            scene black with Dissolve(.5)
            $ renpy.pause(1, hard = True)
            $ time_tmp = 'evening'
            jump bed_no_night

        "Отдыхать до ночи." if time.time_now != 'night' and not _block_time_forward_check:

            scene black with Dissolve(.5)
            $ renpy.pause(1, hard = True)
            $ time_tmp = 'night'
            jump bed_no_night




        "Спать до следующего дня." if time.time_now != 'night' and not _block_time_forward_check:
            $ location_now = 'Prison'
            $ Hide('main_interface')()


            call go_sleep_to_morning from _call_go_sleep_to_morning_3
            $ time_tmp = 'morning'
            jump bed_no_night
        "Уйти." if True:






            pass

    jump main_interface_label