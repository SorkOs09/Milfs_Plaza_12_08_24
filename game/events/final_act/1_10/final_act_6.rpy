label final_act_6_debug:

    $ not_survival_final_act_4 = copy.deepcopy(not_survival)
    $ not_survival = True
    $ time.time_now = 'morning'
    scene black
    show image Text("DEBUG: переход к final_act_6"):
        align(.5, .5)
    with my_dissolve 
    call wait_click_label from _call_wait_click_label_32
label final_act_6:    #Final_Act_5 

    # if store.test_debug_mod:
    #     scene black
    #     with my_dissolve
    #     menu:
    #         "DEBUG: Этот ивент уже был в предыдущих сборках и возможно вы его уже проверяли.\nПропустить ивент?"

    #         "  Да  ":
    #             jump final_act_6_end
    #         "  Нет  ":
    #             pass
    #"Description" " Я в тюрьме…"



    #Активировать спрайт офицера.

    scene final_act_prison_large_bg morning:
        xalign 1.0
    show final_act_prison_officer_at_large_bg:
        xalign 1.0
    show GG Prison_Angry
    show GG Prison_Angry: #at go_from_right(xxzoom=-1.0, xxalign=.95)
        xzoom -1.0
        xalign .86 ypos 1081

    #show image "cg/final_act/prison/activities/sit_on_bed.png"
    #show Officer Smile
    #show Officer Smile:
    #   xalign -.15 ypos 1081
       
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    show final_act_prison_large_bg morning:
        easein 1.25 xalign .47
    show final_act_prison_officer_at_large_bg:
        easein 1.25 xalign .47
    
    $ renpy.pause(1.3, hard = True)
    hide final_act_prison_officer_at_large_bg
    show Officer Smile
    show Officer Smile:
       xalign .15 ypos 1081
    with my_dissolve
    #show Officer Smile:
    #    easein .75 xalign .185
    #$ renpy.pause(.75, hard = True)
    #$ renpy.pause(.6, hard = True)
    #hide image "cg/final_act/prison/activities/sit_on_bed.png"

        
    #show Officer Smile
    #show Officer Smile:
    #    xalign -0.05        
    #    ypos 1085
    #show image 'cg/final_act/prison/cage.png'

  
    "Офицер" "Ну, как тебе новая жилплощадь? ОСВАИВАЕШЬСЯ?"
    show shadow_full:
        alpha 0.0
        ease .5 alpha .5
    show GG Prison_Angry: #at go_from_right(xxzoom=-1.0, xxalign=.95)
        ease .5 xalign .845
    
    "[gg]" "….."

    scene final_act_prison_large_bg morning:
        xalign .47
    show Officer Laughs
    show Officer Laughs:
       xalign .15 ypos 1081
    show GG Prison_Angry
    show GG Prison_Angry: #at go_from_right(xxzoom=-1.0, xxalign=.95)
        xzoom -1.0 xalign .845
    show shadow_full:
        alpha .5
    with my_dissolve
    "Офицер" "Дерьмо полное, верно?"
    show Officer Smile
    with my_dissolve
    "Офицер" "И кровать, небось, такая, что аж жопа деревенеет. "
    "Офицер" "Я рад, что ты оценил."
    
    show shadow_full:
        ease .5 alpha .75
    show GG Prison_Angry: #at go_from_right(xxzoom=-1.0, xxalign=.95)
        ease .5 xalign .835
    
    "[gg]" "…."
    
    show shadow_full:
        easein .5 alpha .0
    
    show Officer Laughs:
        easein .1 ypos 1085
        easein .1 ypos 1080
        easein .1 ypos 1085
        easein .1 ypos 1080
        easein .1 ypos 1085
        easein .1 ypos 1080
        easein .1 ypos 1085
        easein .1 ypos 1080
    
    "Офицер" "Хе-хе-хе."

    "Офицер" "А уж остальные достопримечательности быта, наверное, просто загляденье!"
    hide shadow_full
    show Officer Say:
        xalign .15 ypos 1080 
    with my_dissolve
    "Офицер" "А чего это ты хмуришься, а? Я лично выбирал тебе камеру, [gg]. Скажи спасибо."
    show GG Prison_Angry
    "[gg]" "Спасибо."
    
    "Офицер" "Ха! Быстро учишься. Значит точно освоишься."
    #GG_Turma_Normal

    # show shadow_full:
    #     alpha 0.0
    #     easein .75 alpha .75
    "Офицер" "Значится так… Я обязан ввести тебя в курс дела, [gg]. Так что слушай и запоминай. "
    
    "Офицер" "Вскоре предстоит суд."
    
    "Офицер" "И тебе предъявят несколько обвинений…"
    
    "Офицер" "Кража, распространение наркотиков, участие в отмытые денежных средств и многое другое."
    
    "Офицер" "В довесок ко всему пойдут такие прекрасные нарушения как оскорбление офицера полиции и сопротивление аресту."
    #GG_Turma_Normal

    show GG Prison_Please
    with my_dissolve
    "[gg]" "Что?!"
    
    show GG Prison_WTF:
        easein 1.25 xalign .95
    #with my_dissolve
    "[gg]" "Какое ещё отмытые денежных средств? "
    show Officer Skepticism
    with my_dissolve
    "Офицер" "Ты бы видел своё лицо, [gg]! Тебя только это волнует? "
    #show GG:
        #xzoom 1.0

    
    "[gg]" "Ты прекрасно знаешь – меня подставили."
    
    "[gg]" "Может я и не самый законопослушный гражданин в этом городе, но ничем таким не промышляю."
    
    "Офицер" "А распространение наркотиков?"
    show GG Prison_Angry:
        #xzoom -1.0
        easein_cubic .3 xalign .79
    "[gg]" "У тебя нет доказательств!"
    show Officer Normal
    "Офицер" "Да ну? У меня есть свидетель."
    show GG Prison_Angry:
        #xzoom -1.0
        easein .1 xalign .72
    "[gg]" "Кто?!"
    show Officer Angry
    "Офицер" "А это не твоё собачье дело. Главное, что прокурора он устраивает. "
    show GG Prison_Please:
        easein .8 xalign .835
    "[gg]" "Понятно…"
    
    "[gg]" "Пришёл поиздеваться? "
    show Officer Laughs:
        easein .1 ypos 1085
        easein .1 ypos 1080
        easein .1 ypos 1085
        easein .1 ypos 1080
        easein .1 ypos 1085
        easein .1 ypos 1080
        easein .1 ypos 1085
        easein .1 ypos 1080
    "Офицер" "Ха-ха-ха."
    show Officer Smile
    with my_dissolve
    "Офицер" "И это тоже."
    show Officer Normal
    with my_dissolve
    "Офицер" "К тебе пришли посетители. "
    show Officer Smile
    with my_dissolve
    
    "Офицер" "Но я не мог отказаться себе в удовольствии предупредить тебя об этом лично, хе-хе-хе."
    show GG Prison_Angry
    "[gg]" "Марина?"
    show Officer Laughs
    with my_dissolve
    
    "Офицер" "Она самая. "
    #GG_Turma_Embarrassment 

    show Officer Smile
    with my_dissolve
    "Офицер" "Её грустный и подавленный вид заводит меня ещё сильнее."
    show Officer Smile:
        xzoom -1.0 xalign .135
    with my_dissolve
    "Офицер" "Аргх!"
    scene final_act_prison_large_bg morning:
        xalign .47
        easein 4.5 xalign 0.0
    show Officer Smile
    show Officer Smile:
        xalign .135 xzoom -1.0 ypos 1080
        easein 4.5 xalign -.05
    show GG Prison_Angry
    show GG Prison_Angry:
        xalign .835 ypos 1080 xzoom -1.0
        easein 4.5 xalign 1.0
    "Офицер" "Ей так горестно, что любимый кавалер взаперти. И вполне возможно, что на много-много лет."
    show Officer:
        xzoom 1.0
        xalign -.05
    with my_dissolve
    "Офицер" "Как жаль, не правда ли?"
    show GG Prison_Angry
    "[gg]" " …."
    show final_act_prison_large_bg morning:
        easein_cubic 6.0 xalign .35
    show Officer:
        xzoom 1.0
        easein_cubic 5.5 xalign .175
    show GG:
        easein_cubic 5.5 xalign .9
    show shadow_full:
        alpha 0.0
        easein_cubic 1.5 alpha .5
    
    "Офицер" "Ты не унывай, [gg]. Я позабочусь о ней."
    #GG_Turma_Surprise

    show shadow_full:
        easein 1.5 alpha .75
    
    "Офицер" "И о Кристи тоже."
    #GG_Turma_Angry

    "Офицер" "Твою соседку по комнате ведь так зовут, верно?"
    show GG Prison_Angry
    "[gg]" "Какая нелепая провокация. "
    show GG Prison_Angry
    "[gg]" " Может, придумаешь что-то по остроумнее, чем цитаты злодеев из боевиков 90х годов?"
    "Офицер" "Если продолжишь дерзить, я проведу с тобой разъяснительные работы."
    show GG Prison_Angry
    "[gg]" "Да пожалуйста. Я весь в нетерпении. "

    show Officer Laughs:
        easein .1 ypos 1085
        easein .1 ypos 1080
        easein .1 ypos 1085
        easein .1 ypos 1080
        easein .1 ypos 1085
        easein .1 ypos 1080
        easein .1 ypos 1085
        easein .1 ypos 1080
    show shadow_full:
        easein .1 alpha .0
    "Офицер" "Аха-ха-ха-ха!!"
    show Officer Laughs
    "Офицер" "Хорошая попытка."
    show Officer Smile
    "Офицер" "В другой раз. "
    show Officer Smile
    "Офицер" "Хочу сохранить свою энергию для Марины. "
    show Officer Smile
    "Офицер" "Да к тому же, судье не понравится, что заключённый явится на заседание в помятом виде."
    show Officer Normal
    "Офицер" "Но мы продолжим этот разговор. Обязательно продолжим."
    show Officer Normal
    "Офицер" "Сразу после того, как тебе вынесут вердикт."
    show GG Prison_Angry
    "[gg]" "….."
    show Officer Normal:
        xzoom -1
    with my_dissolve
    "Офицер" "Ещё увидимся."
    show Officer Laughs:
        xzoom -1
        easein 1.75 xalign -.65
    "Офицер" "Аха-ха-ха-ха!"
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label

    $ renpy.pause(.5, hard = True)
    #////Officer_Kamera исчезает

    call final_act_blind_transition_to_black_label from _call_final_act_blind_transition_to_black_label
    python:
    
        for i in range(1, 20):
            n = (i-1)*102
            j = Crop((n, 0, 102, 1080), 'cg/final_act/prison/0.png')
            

            dur = .2+i*.1,
            renpy.show('final_act_4_prison_0_'+str(i), what = j, 
                at_list=[
                final_act_4_blinds_transform(
                    xp  = n,
                    dur = .15+i*.1,
                    xp_fin = n,
                    )
                ])

        renpy.pause(2.5, hard = True)

    #//GG_Kamera_1

    scene image 'cg/final_act/prison/0.png'
    with my_dissolve

    "[gg]" "Подонок…"
    "[gg]" "Остаётся лишь надеяться, что он блефует."
    "[gg]" "Я должен сделать всё возможное, чтобы выбраться отсюда."
    call hide_say_screen_with_dissolve_label from _call_hide_say_screen_with_dissolve_label_1

    $ renpy.pause(.5, hard = True)


label final_act_6_end:
    $ debug_next('final_act_7_debug',)
    python:
        #for i in ('morning', 'afternoon'):
        locations['Prison'].image_buttons_times['afternoon'].update(
                {'milf':Jump('final_act_7')}
                )

        locations['Prison'].image_buttons_times['morning'].update(
                {'officer': Jump('final_act_13_officer_repeat')}
                )

        for i in range(1, 20):
            n = (i-1)*100
            j = Crop((0, 0, 120, 1080), 'black')
            renpy.show('black_'+str(i), what = j, 
                at_list=[
                final_act_4_blinds_transform(
                    xp  = n,
                    dur = i*.075,
                    xp_fin = n,
                    )
                ])
        
        renpy.pause(1.5, hard = True)
    
        for i in range(1, 20):
            n = (19-i)*102
            j = Crop((n, 0, 102, 1080), 'locations/bg/Prison/afternoon.png')
            

            dur = .2+i*.1,
            renpy.show('final_act_4_prison_morning_'+str(i), what = j, 
                at_list=[
                final_act_4_blinds_transform(
                    xp  = n+102,
                    dur = .25+i*.08,
                    xp_fin = n,
                    )
                ])

        #time.time_forward(jump_to_main_interface = False)
        descript = _("Я на грани срыва…")
    
        renpy.pause(2.5, hard = True)

        time.time_now = 'afternoon'


    
    jump main_interface_label #final_act_7 

