label prison_talk_with_girl_officer_start:
    scene final_act_prison_large_bg night:
        xalign 1.0

    show GG Prison_WTF
    show GG Prison_WTF: 
        xzoom -1.0
        xalign .86 ypos 1081
    show GirlOfficer Normal
    show GirlOfficer Normal:
        xzoom -1.0
        xalign -.1 ypos 1081
       
    with my_dissolve
    $ renpy.pause(.35, hard = True)
    show final_act_prison_large_bg night:
        easein .75 xalign .47
    show GirlOfficer Normal:
        easein .75 xalign .15

    $ renpy.pause(.8, hard = True)
    scene final_act_prison_large_bg night:
        xalign .47
    show GirlOfficer Normal
    show GirlOfficer Normal:
        xzoom -1.0
        xalign .15 ypos 1081
    show GG Prison_WTF
    show GG Prison_WTF: #at go_from_right(xxzoom=-1.0, xxalign=.95)
        xzoom -1.0
        xalign .86 ypos 1081
    with my_dissolve

    $ locations['Prison'].image_buttons_times['night'].pop('food', 0)
    # $ locations['Prison'].image_buttons_times['night'].update(
    #     {'food':Jump('final_act_14_repeat')}
    #     )
    return

label prison_talk_with_milf_start:
    scene final_act_prison_large_bg morning:
        xalign 1.0
    show final_act_prison_milf_at_large_bg:
        xalign 1.0
    #show final_act_prison_officer_at_large_bg:
    #    xalign 1.0
    show GG Prison_WTF
    show GG Prison_WTF: 
        xzoom -1.0
        xalign .86 ypos 1081

    with my_dissolve
    $ renpy.pause(.35, hard = True)
    show final_act_prison_large_bg afternoon:
        easein .75 xalign .47
    show final_act_prison_milf_at_large_bg:
        easein .75 xalign .47
   # show final_act_prison_officer_at_large_bg:
   #     easein .75 xalign .47
    
    $ renpy.pause(.8, hard = True)
    scene final_act_prison_large_bg afternoon:
        xalign .47
    show Milf Street_Chagrin
    show Milf Street_Chagrin:
        xzoom -1.0
        xalign .15 ypos 1081
    show GG Prison_WTF
    show GG Prison_WTF: 
        xzoom -1.0
        xalign .86 ypos 1081
    with my_dissolve


    $ locations['Prison'].image_buttons_times['afternoon'].pop('milf', 0)
    
    return




label prison_talk_with_milf_sex_start:
    scene final_act_prison_large_bg morning:
        xalign 1.0
    show final_act_prison_milf_at_large_bg:
        xalign 1.0
    #show final_act_prison_officer_at_large_bg:
    #    xalign 1.0
    show GG Prison_WTF
    show GG Prison_WTF: 
        xzoom -1.0
        xalign .86 ypos 1081

    with my_dissolve
    $ renpy.pause(.35, hard = True)
    show final_act_prison_large_bg afternoon:
        easein .75 xalign .47
    show final_act_prison_milf_at_large_bg:
        easein .75 xalign .47
   # show final_act_prison_officer_at_large_bg:
   #     easein .75 xalign .47
    
    $ renpy.pause(.8, hard = True)
    scene final_act_prison_large_bg afternoon:
        xalign .47
    show Milf Street_0_Chagrin
    show Milf Street_0_Chagrin:
        xzoom -1.0
        xalign .15 ypos 1081
    show GG Prison_WTF
    show GG Prison_WTF: 
        xzoom -1.0
        xalign .86 ypos 1081
    with my_dissolve


    $ locations['Prison'].image_buttons_times['afternoon'].pop('milf', 0)
    
    return


    
label prison_talk_with_milf_masturbation_reject:
    hide shadow_full
    show Milf Street_0_Chagrin
    show GG Prison_Normal
    with my_dissolve
    "Марина" "Ох… Я понимаю тебя, [gg]."
    #show Milf Street_Chagrin
    "Марина" "Но знаешь, я буду приходить вновь и вновь, в надежде, что твоё желание и силы возобновятся. "
    #show Milf Street_Chagrin
    
    "Марина" "Не хочу, чтобы ты страдал в одиночестве."
    #show GG Prison_Angry
    show GG Prison_Embarrassment
    with my_dissolve
    "[gg]" "Спасибо, любовь моя. "
    return


label prison_talk_with_milf_masturbation_end:
    scene black
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    scene final_act_prison_large_bg evening:
        xalign .47
    show Milf Street_0_Passion
    show Milf Street_0_Passion:
        xzoom -1.0
        xalign .1 ypos 1081
    show GG Prison_Smile
    show GG Prison_Smile: 
        xzoom -1.0
        xalign .86 ypos 1081
    with my_dissolve
    "Марина" "Тебе полегчало, мой хороший?"
    #show GG Prison_Angry
    "[gg]" "Я буквально исцелён, хе-хе."
    show Milf Street_0_Smile
    with my_dissolve
    "Марина" "Тогда до встречи."
    return


label prison_talk_with_milf_cum:
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_22

    hide final_act_milf_gg_jerk
    show final_act_milf_gg_jerk_sperm_1
    show final_act_milf_gg_jerk anim_end
    $ renpy.pause(1.32, hard = True)
    hide final_act_milf_gg_jerk

    show image "cg/final_act/milf_cage/sperm/12.png":
        align (0, 0)
        alpha 1.0
        pos (0, 0)
        easein 1.5 pos (20, 20) alpha .5
    show final_act_milf_gg_jerk_sperm_2:
        align (0, 0)
        pos (0, 0)
        easein 1.0 pos(200, 0)
    show final_act_milf_gg_jerk anim_end
    $ renpy.pause(1.32, hard = True)
    hide final_act_milf_gg_jerk

    show final_act_milf_gg_jerk_sperm_3:
        align (0, 0)
        pos (0, 0)
        easein 1.0 pos(-110, 0)
    show final_act_milf_gg_jerk anim_end
    call wait_click_label from _call_wait_click_label_17
    return