label tyan_falos_7_debug:
    $ location_now = 'Corridor'
    scene black
    show image Text('DEBUG: Переход к ивенту tyan_falos_7_0'):
        align (.5, .5)
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call wait_click_label from _call_wait_click_label_36
label tyan_falos_7_0:
    $ events.pop('tyan_falos_7_0', 0)
    
    call show_bg_image_label from _call_show_bg_image_label_176
    "[gg]" "Теперь мне нужно выждать момент, когда Кристи не будет дома и начать пилить стену."
    $ Event('tyan_falos_7_1', 'Hall', 'tyan_falos_7_1')
    $ Event('tyan_falos_7_2', 'Restroom', 'tyan_falos_7_2')
    $ Event('tyan_falos_7_3', 'Kitchen', 'tyan_falos_7_3')
    $ Event('tyan_falos_7_4', 'Sister_Room', 'tyan_falos_7_4')
    $ Event('tyan_falos_7_5', 'GG_Room', 'tyan_falos_7_5')
    $ block_milf_home_tmp   = copy.deepcopy(block_milf_home)
    $ block_sister_home_tmp = copy.deepcopy(block_sister_home)
    $ block_exit_home_tmp   = copy.deepcopy(block_exit_home)
    
    $ block_milf_home   = True
    $ block_sister_home = True
    $ block_exit_home   = True

    $ debug_next('tyan_falos_7_1_debug')
    jump main_interface_label
label tyan_falos_7_1_debug:
    $ location_now = 'Corridor'
    scene black
    show image Text('DEBUG: Переход к ивенту tyan_falos_7_1'):
        align (.5, .5)
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call wait_click_label from _call_wait_click_label_37
label tyan_falos_7_1:
    $ location_now = 'Hall'

    call show_all_images_label from _call_show_all_images_label_36

    $ events['tyan_falos_7_1'].complete = True
    "[gg]" "Судя по всему, в комнате её нет."

    $ debug_next('tyan_falos_7_2_debug')
    call tyan_falos_7_check_final from _call_tyan_falos_7_check_final

    jump main_interface_label


label tyan_falos_7_2_debug:
    $ location_now = 'Corridor'
    scene black
    show image Text('DEBUG: Переход к ивенту tyan_falos_7_2'):
        align (.5, .5)
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call wait_click_label from _call_wait_click_label_38
label tyan_falos_7_2:
    $ location_now = 'Restroom'
    $ Hide('main_interface', transition = Dissolve(.5))()
    call show_all_images_label from _call_show_all_images_label_37

    $ events['tyan_falos_7_2'].complete = True
    "[gg]" "Здесь никого."

    $ debug_next('tyan_falos_7_3_debug')
    call tyan_falos_7_check_final from _call_tyan_falos_7_check_final_1

    jump main_interface_label

label tyan_falos_7_3_debug:
    $ location_now = 'Corridor'
    scene black
    show image Text('DEBUG: Переход к ивенту tyan_falos_7_3'):
        align (.5, .5)
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call wait_click_label from _call_wait_click_label_39
label tyan_falos_7_3:
    $ location_now = 'Kitchen'
    $ Hide('main_interface', transition = Dissolve(.5))()
    call show_all_images_label from _call_show_all_images_label_38


    $ events['tyan_falos_7_3'].complete = True
    "[gg]" "Здесь чисто."

    $ debug_next('tyan_falos_7_4_debug')
    call tyan_falos_7_check_final from _call_tyan_falos_7_check_final_2

    jump main_interface_label
label tyan_falos_7_4_debug:
    $ location_now = 'Corridor'
    scene black
    show image Text('DEBUG: Переход к ивенту tyan_falos_7_4'):
        align (.5, .5)
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call wait_click_label from _call_wait_click_label_40
label tyan_falos_7_4:
    $ location_now = 'Sister_Room'
    $ Hide('main_interface', transition = Dissolve(.5))()
    call show_all_images_label from _call_show_all_images_label_39

    $ events['tyan_falos_7_4'].complete = True
    "[gg]" "Кристи, ты тут? "

    $ debug_next('tyan_falos_7_5_debug')
    call tyan_falos_7_check_final from _call_tyan_falos_7_check_final_3

    jump main_interface_label

label tyan_falos_7_5_debug:
    $ location_now = 'Corridor'
    scene black
    show image Text('DEBUG: Переход к ивенту tyan_falos_7_5'):
        align (.5, .5)
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call wait_click_label from _call_wait_click_label_41
label tyan_falos_7_5:
    $ location_now = 'Corridor'
    $ Hide('main_interface', transition = Dissolve(.5))()
    call show_all_images_label from _call_show_all_images_label_40


    "[gg]" "Сперва я должен проверить, осталась ли Кристи дома."

    $ debug_next('tyan_falos_7_final_debug')
    #call ep3_milf_16_check_final from _call_ep3_milf_16_check_final_4
    call tyan_falos_7_check_final from _call_tyan_falos_7_check_final_4
    jump main_interface_label




label tyan_falos_7_check_final:
    python:
        if 'tyan_falos_7_1' not in events:
            Event('tyan_falos_7_1', 'Hall', 'tyan_falos_7_1')
        if 'tyan_falos_7_2' not in events:
            Event('tyan_falos_7_2', 'Restroom', 'tyan_falos_7_2')
        if 'tyan_falos_7_3' not in events:
            Event('tyan_falos_7_3', 'Kitchen', 'tyan_falos_7_3')
        if 'tyan_falos_7_4' not in events:
            Event('tyan_falos_7_4', 'Sister_Room', 'tyan_falos_7_4')
        if 'tyan_falos_7_5' not in events:
            Event('tyan_falos_7_5', 'GG_Room', 'tyan_falos_7_5')
        
        try:
                
            if all([

                events['tyan_falos_7_1'].complete,
                events['tyan_falos_7_2'].complete,
                events['tyan_falos_7_3'].complete,
                events['tyan_falos_7_4'].complete,

                ]):
                events['tyan_falos_7_5'].complete = True
                renpy.jump('tyan_falos_7')
        except:
            renpy.jump('tyan_falos_7')
            
    return

label tyan_falos_7_final_debug:
    $ location_now = 'Corridor'
    scene black
    show image Text('DEBUG: Переход к ивенту tyan_falos_7_final'):
        align (.5, .5)
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    call wait_click_label from _call_wait_click_label_42

label tyan_falos_7:
    $ location_now = 'GG_Room'
    $ events.pop('tyan_falos_7_1', 0)
    $ events.pop('tyan_falos_7_2', 0)
    $ events.pop('tyan_falos_7_3', 0)
    $ events.pop('tyan_falos_7_4', 0)
    
    $ events.pop('tyan_falos_7_5', 0)
    scene black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)

    call show_bg_image_label from _call_show_bg_image_label_167
    with Dissolve(.5)
    show GG Think
    show GG Think at go_from_left(xxzoom = -1, xxalign = .53)
    $ renpy.pause(1, hard = True)
    show image 'cg/ep86/wall_2.png' with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .0
        easein 1 alpha .75
    #"[gg]" "[gg]"
#   A task: 
#   1.  Активировать стену (возможно есть смысл иконку сделать для квеста).
    #Scene:
    #Wall_Rez_1
    "[gg]" "Только не отрежь себе чего-нибудь, только не отрежь!"
label tyan_falos_7_mini_game:
    show image 'cg/ep86/wall_2.png' 
    with Dissolve(.5)
    "[gg]" "Аккуратно… [gg], очень и очень аккуратно."
    with my_vpunch
    "[gg]" "Как же трясёт эту хрень."
    "[gg]" "Или это трясутся мои руки?.."
    #Wall_Rez_2
    if not renpy.call_screen('qte_mini_game'):

        show image 'cg/ep86/wall_5.png' 

        hide image 'cg/ep86/wall_2.png'

        with my_vpunch
        if preferences.language in (None, 'eng', 'rus'):
            "" "Инструмент оказался слишком тяжелым и вы уронили его"
            "" "Матерясь вы поднимаете его и пробуете снова"
        else:
            call wait_click_label from _call_wait_click_label_52

        hide image 'cg/ep86/wall_5.png'
        jump tyan_falos_7_mini_game
    show image 'cg/ep86/wall_3.png' 

    hide image 'cg/ep86/wall_2.png'

    with vpunch

    $ renpy.pause(.5, hard = True)


    show image 'cg/ep86/wall_4.png' 

    hide image 'cg/ep86/wall_3.png'

    with Dissolve(.5)

    "[gg]" "Ну вот, замечательная дырочка с идеальным диаметром. "
    "[gg]" "Теперь нужно закрыть её пробкой и смогу пользоваться этим отверстием всякий раз, когда Кристи захочет удовлетворить себя резиновым фалосом. "
    #// Wall_Rez_2 исчезает"
    hide image 'cg/ep86/wall_0.png' 
    hide image 'cg/ep86/wall_1.png' 
    hide image 'cg/ep86/wall_2.png' 
    hide image 'cg/ep86/wall_3.png' 
    hide image 'cg/ep86/wall_4.png' 
    hide image 'cg/ep86/wall_5.png' 
    with my_dissolve
#    show GG Think
    "[gg]" "Конечно, я не всегда могу знать заранее, когда захочет «поиграться» со своей игрушкой, и для этого, когда наступит ночь, должен заранее караулить её у стены. "
    show GG Think
    "[gg]" "Не самое весёлое занятие, но предстоящее наслаждение стоит любых лишений. "

    $ debug_next('tyan_falos_8_debug')
    $ tyan_falos_text = _("Активировать отверстие в стене при наступлении ночи. ")
    scene black with Dissolve(.5)
    $ block_milf_home   = copy.deepcopy(block_milf_home_tmp)
    $ block_sister_home = copy.deepcopy(block_sister_home_tmp)
    $ block_exit_home   = copy.deepcopy(block_exit_home_tmp)
    
    $ location_now = 'Corridor'
   # $ Event('tyan_falos_8', 'GG_Room', time = ['night',])
    $ fix_for_buttons_at_locations()
    $ locations['GG_Room'].image_buttons_times['night'].update({"hole_night":Jump("tyan_falos_8")})
    $ new_events_christie = True
    $ renpy.pause(.5, hard = True)
    jump main_interface_label