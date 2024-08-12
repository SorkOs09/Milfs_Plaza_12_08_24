init python:
    gifts_for_mother = (
        'Шоколад',
        'Букет из милых цветков'
        )

    def _check_talk_with_milf():
        if location_now == 'Restroom':
            return False
        if _milf_costume != "n_body":
            for i in store.check_ev:
                if i.name in store._events_need_costume:
                    if _milf_costume == store._events_need_costume[i.name]:
                        return True
        if (_milf_costume != "n_body" or len(check_ev_buttons) == 0) and preferences.language in (None, 'eng', 'rus'):
            
            return True
        elif _milf_costume == "n_body" and len(check_ev_buttons):
            return True

image laskat_block = Transform("#0000", size = (10, 10))

label talk_with_milf_label:
    if not getattr(store, 'block_time_forward', False):
        call check_surv_label from _call_check_surv_label








    if getattr(store, 'block_milf_events', None):
        $ renpy.jump(block_milf_events)

    if time.time_now == 'night' and location_now == 'Milf_Room':
        jump milf_sleep_label
    python:

        tmp_location_now  = copy.deepcopy(location_now) 
        check_ev          = []



        for i in ['Corridor', 'Kitchen', 'Hall']:
            
            if location_now == i:
                
                
                location_now      = i + '_Milf'
                
                check_ev          = get_all_events_from_location()
                
                location_now      = copy.deepcopy(tmp_location_now)


        location_now = 'Milf'
        check_ev    += get_all_events_from_location()

        location_now      = copy.deepcopy(tmp_location_now)
        check_ev_buttons  = get_check_ev_buttons(check_ev)
        




        create_talk_with_translates()



        _milf_costume = getattr(store, 'milf_costume', 'n_body')
        
        _hall_evening_check   = location_now == 'Hall' and time.time_now == 'evening' and _milf_costume == 'n_body'
        
        _film_kickboxer_check = getattr(store, 'unlock_film_kickboxer', False)
        _film_lolita_check    = getattr(store, 'unlock_film_lolita', False)
        _film_alexandr_check  = getattr(store, 'unlock_film_alexandr', False)
        _watch_line           = __("Смотреть")


        _watch_kickboxer_line = _watch_line + " " + __("\"Кикбоксёр\"")
        _watch_lolita_line    = _watch_line + " " + __("\"Лолита\"")
        _watch_alexandr_line  = _watch_line + " " + __("\"Александр\"")
        
        if not _film_kickboxer_check:
            _watch_kickboxer_line = "{alpha=*0.5}"+_watch_kickboxer_line+"{/alpha}"
        if not _film_lolita_check:
            _watch_lolita_line = "{alpha=*0.5}"+_watch_lolita_line+"{/alpha}"
        if not _film_alexandr_check:
            _watch_alexandr_line = "{alpha=*0.5}"+_watch_alexandr_line+"{/alpha}"

        if _milf_costume != 'n_body':
            renpy.music.stop(fadeout=.5)
            renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
        if not hasattr(store, "laskat_image"):
            laskat_image = "warning_icon"

    menu talk_with_milf_menu:
            

        "Говорить" if _check_talk_with_milf():

            if _milf_costume == "n_body" or (len(check_ev) and check_ev[0].name in _events_need_costume and _events_need_costume[check_ev[0].name] == _milf_costume):
                if len(check_ev_buttons) == 1:
                    $ renpy.jump(check_ev[0].label)
                else:
                    menu:

                        "[tmp_names_tmp_0]" if len(check_ev_buttons) >= 1:
                            $ renpy.jump(check_ev[0].label)
                        "[tmp_names_tmp_1]" if len(check_ev_buttons) >= 2:
                            $ renpy.jump(check_ev[1].label)
                        "[tmp_names_tmp_2]" if len(check_ev_buttons) >= 3:
                            $ renpy.jump(check_ev[2].label)
                        "[tmp_names_tmp_3]" if len(check_ev_buttons) >= 4:
                            $ renpy.jump(check_ev[3].label)
                        "[tmp_names_tmp_4]" if len(check_ev_buttons) >= 5:
                            $ renpy.jump(check_ev[4].label)
                        "[tmp_names_tmp_5]" if len(check_ev_buttons) >= 6:
                            $ renpy.jump(check_ev[5].label)
                        "[tmp_names_tmp_6]" if len(check_ev_buttons) >= 7:
                            $ renpy.jump(check_ev[6].label)
                        "[tmp_names_tmp_7]" if len(check_ev_buttons) >= 8:
                            $ renpy.jump(check_ev[7].label)
                        "[tmp_names_tmp_8]" if len(check_ev_buttons) >= 9:
                            $ renpy.jump(check_ev[8].label)
                        "[tmp_names_tmp_9]" if len(check_ev_buttons) >= 10:
                            $ renpy.jump(check_ev[9].label)
                        "Назад":
                            jump talk_with_milf_menu


            
            elif _milf_costume != "n_body" or len(check_ev_buttons) == 0 and preferences.language in (None, 'eng', 'rus'):
                
                if _milf_costume in milf_additional_costumes:
                
                    $ renpy.jump("milf_standart_talk_" + str(_milf_costume))
                
                else:

                    jump milf_standart_talk_n_body


        "Комплимент (+5 Отношения)" if getattr(store, 'kompliment_day', False):
            call already_did_it_today from _call_already_did_it_today
            jump main_interface_label
        "Комплимент (+5 Отношения)" if not getattr(store, 'kompliment_day', False) and location_now != 'Restroom':
            if preferences.language not in (None, 'eng', 'rus'):
                $ show_text_animation('+5 milf')
                $ kompliment_day = True
                play audio 'audio/rest.ogg'

                jump main_interface_label

            call show_bg_image_label from _call_show_bg_image_label_75
            call show_additional_images_label from _call_show_additional_images_label_61

            show Milf Normal
            if time.time_now == 'evening':
                show Milf Night_Normal:
                    xalign .9
                    ypos 1085
                    zoom 1.0-0.035
            elif location_now == 'Hall':
                show Milf Losi_Embarrassment:
                    xalign .75
                    ypos 1085
                    zoom 1.0-0.035
            elif True:

                show Milf Normal:
                    xalign .75
                    ypos 1085
                    zoom 1.0-0.035
            with Dissolve(.5)
            show GG Embarrassment

            show GG Embarrassment at go_from_left








            "[gg]" "Ты знаешь, у меня не всегда получается быть искреннем с тобой, Маришка, но знай, я восхищаюсь твой естественной красотой зрелой женщины."


            show GG:
                xalign .15
            with my_dissolve



            "Марина" "[gg], у тебя хорошее настроение или же ты просто хочешь меня раздобрить?"





            '[gg]' "Совмещаю приятное с полезным."
            $ show_text_animation('+5 milf')




            if _milf_costume == "n_body" and time.time_now in ['evening', 'night']:

                show Milf Night_Passion:
                    easein 5 xalign .5
            elif _milf_costume == "n_body" and location_now == 'Hall':
                show Milf Losi_Passion:
                    easein 5 xalign .5            
            else:

                show Milf Passion:
                    easein 5 xalign .5

            show GG Surprise:
                easein 9 xalign .05


            show expression 'cg/ep45/shower_3/shadow.png':
                alpha .0
                easein 5 alpha .75

            "Марина" "У тебя получается."
            $ kompliment_day = True
            play audio 'audio/rest.ogg'

            jump main_interface_label



        "Сделать подарок (+5 Отношения)" if getattr(store, 'gift_day', False) and location_now != 'Restroom':
            call already_did_it_today from _call_already_did_it_today_1
            jump main_interface_label


        "Сделать подарок (+5 Отношения)" if (not getattr(store, 'gift_day', False) and location_now != 'Restroom'):
            python:
                gifts_for_mother_tmp = []
                gifts_for_mother_back_tmp = _('Назад')
                for i in gifts_for_mother:
                    if get_item(i, True):
                        gifts_for_mother_tmp.append(My_C_Item(i))
                    else:
                        gifts_for_mother_tmp.append(My_C_Item('!'+i))

                gifts_for_mother_tmp.append(My_C_Item(_('Назад')))

            $ menu_gifts_for_mother_tmp = renpy.call_screen('choice', gifts_for_mother_tmp)

            if menu_gifts_for_mother_tmp == _('Назад'):
                jump talk_with_milf_label

            $ remove_from_inventory(menu_gifts_for_mother_tmp)
            if preferences.language not in (None, 'eng', 'rus'):
                $ show_text_animation('+5 milf')
                
                $ gift_day = True
                play audio 'audio/rest.ogg'

                jump main_interface_label
            call show_bg_image_label from _call_show_bg_image_label_76
            call show_additional_images_label from _call_show_additional_images_label_62
            with Dissolve(.5)
            show GG Normal



            show GG Normal:
                xalign .1
                ypos 1085
                zoom 1.0-0.035
            show Milf Normal
            if _milf_costume == "n_body" and time.time_now == 'evening':
                show Milf Night_Normal:
                    xalign .75
                    ypos 1085
                    zoom 1.0-0.035
            elif _milf_costume == "n_body" and location_now == 'Hall':
                show Milf Losi_Embarrassment:
                    xalign .75
                    ypos 1085
                    zoom 1.0-0.035
            elif True:

                show Milf Normal:
                    xalign .75
                    ypos 1085
                    zoom 1.0-0.035
            with Dissolve(.5)

            "Марина" "[gg], у тебя хорошее настроение или же ты просто хочешь меня раздобрить?"
            '[gg]' "Совмещаю приятное с полезным."
            $ show_text_animation('+5 milf')
            "Марина" "У тебя получается."
            $ gift_day = True
            play audio 'audio/rest.ogg'


            jump main_interface_label



        "Помощь" if location_now == 'Corridor' and hasattr(store, 'help_ep3_milf_14'):
            call show_bg_image_label from _call_show_bg_image_label_77
            call show_additional_images_label from _call_show_additional_images_label_63
            with Dissolve(.5)
            jump ep3_milf_14_korridor










        "Предложить массаж" if location_now == 'Hall' and time.time_now != 'evening':

            call show_bg_image_label from _call_show_bg_image_label_78
            call show_additional_images_label from _call_show_additional_images_label_64
            with Dissolve(.5)
            call ep5_milf_help from _call_ep5_milf_help
        "Смотреть кино" if _hall_evening_check:
            jump _movie_menu

        "Использовать магию" if get_item('Магические часы', True) is not None and location_now not in ['Restroom', 'Milf_Room', 'Hall'] and _milf_costume == 'n_body':
            jump milf_magic_label

        "Посмотреть на задницу" if 'nude' in milf_position[time.time_now][1] and 'Kitchen' in location_now:
            call show_bg_image_label from _call_show_bg_image_label_80
            call show_additional_images_label from _call_show_additional_images_label_66
            with Dissolve(.5)
            if not hasattr(store, 'milf_check_ass'):
                $ milf_check_ass = True
                $ show_text_animation(_('+10 milf'))

            call talk_with_milf_fix_label_ass from _call_talk_with_milf_fix_label_ass
        "Голод" if hasattr(store, 'gg_hungry_ep1075') and location_now == 'Kitchen' and _milf_costume == 'n_body':
            
            $ laskat_image = "laskat_block"
            $ ass_day = True
            if not hasattr(store, 'milf_check_ass'):
                $ milf_check_ass = True
                $ show_text_animation(_('+5 milf'))
            call show_bg_image_label from _call_show_bg_image_label_230
            call show_additional_images_label from _call_show_additional_images_label_70 
            with Dissolve(.5)
            jump gg_hungry_lvl_1

        "Ласкать" if hasattr(store, 'milf_shower_ep3') and location_now == 'Kitchen' and _milf_costume == 'n_body':

            if getattr(store, 'ass_day', False):
                call already_did_it_today from _call_already_did_it_today_2
                jump main_interface_label
           
            $ ass_day = True
            if not hasattr(store, 'milf_check_ass'):
                $ milf_check_ass = True
                $ show_text_animation(_('+5 milf'))
            call show_bg_image_label from _call_show_bg_image_label_81
            call show_additional_images_label from _call_show_additional_images_label_67
            with Dissolve(.5)

            jump ep3_milf_14_kitchen



        "Смотреть" if location_now == 'Restroom' and _milf_costume == 'n_body':
            call show_bg_image_label from _call_show_bg_image_label_82
            call show_additional_images_label from _call_show_additional_images_label_68
            with Dissolve(.5)
            jump ep3_milf_14_shower_0

        "Дрочить" if location_now == 'Restroom' and getattr(store, 'unlock_masturbation_restroom', 0) and _milf_costume == 'n_body':
            call show_bg_image_label from _call_show_bg_image_label_83
            call show_additional_images_label from _call_show_additional_images_label_69
            with Dissolve(.5)
            jump ep3_milf_14_shower
        "{alpha=*0.5}Дрочить{/alpha}" if location_now == 'Restroom' and not getattr(store, 'unlock_masturbation_restroom', 0):
            call _not_to_fast_label from _call__not_to_fast_label



        "Душ вместе" if location_now == 'Restroom' and getattr(store, 'unlock_shower_together', 0) and _milf_costume == 'n_body':
            #call show_bg_image_label from _call_show_bg_image_label_84
            #call show_additional_images_label from _call_show_additional_images_label_70
            #with Dissolve(.5)
            call ep5_milf_shower from _call_ep5_milf_shower
        "{alpha=*0.5}Душ вместе{/alpha}" if location_now == 'Restroom' and not getattr(store, 'unlock_shower_together', 0) and _milf_costume == 'n_body':

            call _not_to_fast_label from _call__not_to_fast_label_1

        "{alpha=*0.5}Сменить костюм{/alpha} {image=star.png}" if location_now != 'Restroom' and not getattr(store, 'unlock_milf_costumes', False):

            call _not_to_fast_label from _call__not_to_fast_label_2

        "Сменить костюм {image=star.png}" if location_now != 'Restroom' and getattr(store, 'unlock_milf_costumes', False):
            call milf_costume_0 from _call_milf_costume_0

        "Уйти." if True:
            $ location_now = copy.deepcopy(tmp_location_now)

    jump main_interface_label















label talk_with_milf_fix_label_ass:

    call show_all_images_label from _call_show_all_images_label_4

    show expression 'images/cg/ep1/nude_kitchen.png'
    with Dissolve(.5)
    if not renpy.music.get_playing() or 'shower_milf' not in renpy.music.get_playing():
        play music 'audio/shower_milf.mp3'

    '[gg]' "Какие же сочные у неё булочки. "
    '[gg]' "Как бы мне хотелось ухватиться за них, крепко сжать и… "
    '[gg]' "Так, стоп, это уже слишком!"


    if not renpy.music.get_playing() or 'day' not in renpy.music.get_playing():
        $ renpy.music.stop(fadeout=1.5)
        $ renpy.music.play('audio/day.mp3', fadein = 1.5)

    return



























label milf_love_1:
    $ milf_love_quests = 0

    $ descript = _('Я срочно должен рассказать Игорю о ночном посетителе.')

    $ sms_now = SmsBlock('Игорь', 'igor', "1", Jump('ep1_7_phone'))

    $ sms_now.add_sms(_('GG: Чувак, ты не поверишь, что со мной случилось этой ночью.\n\n'))
    $ sms_now.add_sms(_('TT: Попробуй удивить.'))
    $ sms_now.add_sms(_('GG: Какая-то деваха залезла ко мне в комнату и угрожала ножом, чтобы я поскорее отдал наш долг.\n\n\n'))
    $ sms_now.add_sms(_('TT: Деваха?! Вчера, когда я впрягался вместо тебя в парке, ко мне подошёл один из бугаёв Жлоба \nи тоже, знаешь ли, угрожал.\n\n'))
    $ sms_now.add_sms(_('GG: Чувак… Надеюсь, всё обошлось?'))
    $ sms_now.add_sms(_('TT: Не считая пару сломанных рёбер и угроз с требованием отдать кучу денег в кратчайшие сроки, всё ОХУЕНО обошлось.\n\n\n'))
    $ sms_now.add_sms(_('GG: Слушай, я пока не знаю, где мы можем достать столько денег, кроме как грабежом.\n\n'))
    $ sms_now.add_sms(_('TT: Скорее всего нас просто посадят. А потом, по просьбе Жлоба, \nпревратят в двух пидарастических сучек.\n\n'))
    $ sms_now.add_sms(_('GG: И что ты предлагаешь?!'))
    $ sms_now.add_sms(_('TT: Я ничего не предлагаю, чувак. Я в отчаянии. '))
    $ sms_now.add_sms(_('GG: Ладно, спишемся позже.'))
    $ sms_now.add_sms(_('TT: ББ'))

    jump main_interface_label



label milf_love_2:

    $ milf_love_quests = 0

    $ descript = _("Купить покорн и предложить Марине посмотреть сериал «Сладкий кексик». \nДополнительно: Накопить 150$ для перевода Игорю.")

    $ Event('ep2_11_film', 'Milf', time = ['evening'])

    jump main_interface_label













label milf_love_3:

    $ milf_love_quests = 0

    $ descript = _("Лучшее, что я сейчас могу сделать, это провести свой последний вечер с единственным человеком, которому я неравнодушен: следует купить красное вино и подобрать подходящий фильм.\nДиск с подходящим фильмом можно найти в зале.")
    $ locations['Hall'].buttons[0]['tumba_under_tv'] = ((1470, 725, 135, 180),   Jump('hall_tumba_under_tv_lolita_label_ep3_1'))


    $ Event('ep3_1_start', 'Hall_Milf', time = ['evening'])

    jump main_interface_label



label milf_love_4:

    $ milf_love_quests = 0

    $ descript = _('Теперь я знаю предположительный пароль от сейфа. Нужно дождаться, когда никого не будет дома, и перебрать все комбинации. \nЧтобы с пользой для себя убить время, посмотрю с Мариной ужастик. ')

    $ Event('ep3_milf_12', 'Hall_Milf', button_name = _('Смотреть хоррор'), time = ['evening',])
    jump main_interface_label


label milf_love_5:


    $ milf_love_quests = 0

    $ descript = _("Убедить Марину и Кристи отправиться в театр.")
    $ Event('ep3_milf_24',     'Milf')
    $ Event('ep3_milf_24_2',   'Christie')




    jump main_interface_label


label milf_love_6:

    $ milf_love_quests = 0

    $ descript = _('Пригласить Марину вечером в ресторан.')

    $ Event('ep4_milf_44', 'Milf', button_name = _('Пригласить в ресторан'), time = ['evening', ])
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc








label milf_standart_talk_n_body:


    call show_bg_image_label from _call_show_bg_image_label_173
    call show_additional_images_label from _call_show_additional_images_label_104
    show Milf Normal
    if time.time_now == 'evening':
        show Milf Night_Normal:
            xalign .9
            ypos 1085
            zoom 1.0-0.035
    elif location_now == 'Hall':
        show Milf Losi_Embarrassment:
            xalign .75
            ypos 1085
            zoom 1.0-0.035
    elif True:

        show Milf Normal:
            xalign .75
            ypos 1085
            zoom 1.0-0.035
    with Dissolve(.5)
    show GG Normal

    show GG Normal at go_from_left
    if time.time_now != "evening":
        "Марина" "Как проходит твой день, [gg]?"
        '[gg]' "Просто бездельничаю."

        "Марина" "Я не удивлена. "
    elif True:
        "Марина" "Пожалуйста, не тревожь меня. Ты же знаешь, я терпеть не могу, когда меня отвлекают от любимого сериала."

        "[gg]" "Я всего лишь хотел…"
        "Марина" "Нет-нет, не сейчас."
    jump main_interface_label


label _not_to_fast_label:
    '[gg]' "Мне ещё рано предлагать ей это."
    return

label _need_buy_film_label:
    
    "[gg]" "Сначала мне нужно купить нужный фильм в магазине."
    jump talk_with_milf_label

label _film_today_check_label:
    if getattr(store, 'film_today', False):
        "[gg]" "Мы уже смотрели фильм сегодня."
        jump talk_with_milf_label

    return
    

label _start_film_label:
    call show_bg_image_label from _call_show_bg_image_label_110
    call show_additional_images_label from _call_show_additional_images_label_87
    with Dissolve(.5)
    $ film_today = True
    return

label _movie_menu:
    menu:
        "[_watch_alexandr_line]":
            if not hasattr(store, 'ACH_16_count'):
                $ ACH_16_count = [False, False, False]
            
            $ ACH_16_count[0] = True


            if all(ACH_16_count):
                $ add_ach('ACH_16')
            $ store._from_talk_with_milf = True
            jump ep2_11_film

        "[_watch_lolita_line]" if _hall_evening_check: 
            if not _film_lolita_check:

                call _not_to_fast_label from _call__not_to_fast_label_3
                jump talk_with_milf_label

            call _film_today_check_label from _call__film_today_check_label            

            if not get_item('Фильм "Лолита"', True):
                jump _need_buy_film_label



            if not get_item('Красное вино', True):
                '[gg]' "Для начала нужно купить вино"
                jump main_interface_label

            $ remove_from_inventory('Красное вино')
            $ milf_drunk = True
            if not hasattr(store, 'ACH_16_count'):
                $ ACH_16_count = [False, False, False]
            
            $ ACH_16_count[1] = True


            if all(ACH_16_count):
                $ add_ach('ACH_16')


            call _start_film_label from _call__start_film_label
            call ep5_milf_cinema_2 from _call_ep5_milf_cinema_2





        "[_watch_kickboxer_line]" if _hall_evening_check: 
            if not _film_kickboxer_check:

                call _not_to_fast_label from _call__not_to_fast_label_4
                jump talk_with_milf_label

            call _film_today_check_label from _call__film_today_check_label_1            

            if not get_item('Кикбоксёр', True):
                jump _need_buy_film_label
            if not hasattr(store, 'ACH_16_count'):
                $ ACH_16_count = [False, False, False]
            
            $ ACH_16_count[2] = True


            if all(ACH_16_count):
                $ add_ach('ACH_16')
            call _start_film_label from _call__start_film_label_1

            call ep5_milf_cinema_1 from _call_ep5_milf_cinema_1

        "Назад":
            jump talk_with_milf_label

    jump main_interface_label

