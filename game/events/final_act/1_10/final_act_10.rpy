label final_act_10:    #Final_Act_9 


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

   # "Description" "Судя по царапинам на полу, под унитазом расположен тайник. Неплохо было бы узнать, что там.  Для этого я должен расшатать конструкцию, но мне не хватает сил. Надо подкачаться, как бы смешно это не звучало."



    #Пропустить 1 день.

    #Активировать спрайт Офицера, который появляется только вечером.

    #// Игрок смело можно пропускать сколько угодно дней, 
    #но новый квест он не получит, пока не активирует этот, 
    #так же как и не сможет возобновить ВЫНОСЛИВОСТЬ, чтобы качнуть СИЛУ. 
    #Так как доступ к возобновлению ВЫНОСЛИВОСТИ появится позже.



    #//Kamera_Scene

    "Офицер" "О чём думаешь?"
    show Officer Normal
    "Офицер" "О том, как стоило бы поступить ИНАЧЕ или о том, как вообще не стоило бы  поступать?"
    show Officer Smile
    "Офицер" "Например, не мешать мне общаться с Мариной, хе-хе-хе."
    show GG Prison_Angry
    "[gg]" "…."
    show Officer Smile
    "Офицер" "Ой какие мы обидчивые. "
    show Officer Smile
    "Офицер" "Ну и куда подевалась твоя спесь?"
    show Officer Smile
    "Офицер" "Одно удовольствие видеть твою унылую рожу."
    show Officer Normal
    "Офицер" "Надеюсь, ты проводишь это время с толком. "
    show Officer Normal
    "Офицер" "В такие мгновения люди много думают о прожитой жизни, обо всех ошибках или делах, которые не успели совершить. "
    show Officer Normal
    "Офицер" "Есть какие выводы, [gg]?"
    show GG Prison_Angry
    "[gg]" "Да."
    show GG Prison_Angry
    "[gg]" "Почему меня не кормят? "
    show Officer Laughs
    "Офицер" "Аха-ха-ха-ха!"
    show Officer Normal
    "Офицер" "Это не санаторий, а полицейский участок. "
    show Officer Normal
    "Офицер" "Еду приносят только по расписанию, идиот. А не тогда, когда тебе вздумается."
    show GG Prison_Angry
    "[gg]" "И когда же, наконец-то, это случится?!"
    show Officer Normal
    "Офицер" "По твоему, я стану отвечать на твои вопросы, поставленные в таком тоне?"
    show Officer Normal
    "Офицер" "Знай своё место, щенок."
    show Officer Normal
    "Офицер" "Если, конечно, ты не хочешь сдохнуть как бешенная псина. "
    show GG Prison_Angry
    "[gg]" "…."
    show Officer Normal
    "Офицер" "Прекрати так пялиться, будто бы я садист какой-то. "
    show Officer Normal
    "Офицер" "Я здесь только для формального осмотра. "
    show GG Prison_Angry
    "[gg]" "Лучше бы тебе постараться, чтобы я остался здесь навсегда."
    show Officer Smile
    "Офицер" "А иначе что? "
    show Officer Angry
    "Офицер" "ИНАЧЕ ЧТО?!"
    show GG Prison_Angry
    "[gg]" "……"
    show Officer Smile
    "Офицер" "До новых встреч, хе-хе-хе."
    #"//Time" "+1"

    
    $ locations['Prison'].image_buttons_times['morning'].update(
        {'officer': Jump('final_act_13_officer_repeat')}
        )
    $ locations['Prison'].image_buttons_times['afternoon'].update(
                {'milf':Jump('final_act_11')}
                )
    
    call final_act_blind_transition_to_black_label from _call_final_act_blind_transition_to_black_label_3
    
    $ time.time_now = 'afternoon'
    
    jump main_interface_label
