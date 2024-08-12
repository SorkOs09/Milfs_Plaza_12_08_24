init python:
    unlock_shower_together_dict = {
    getattr(store, 'unlock_shower_together',   0):_('(1 ур)'),
    getattr(store, 'unlock_shower_together_2', 0):_('(2 ур)'),
    getattr(store, 'unlock_shower_together_3', 0):_('(3 ур)'),

    }




    def unlock_massage_def():
        
        global store
        if getattr(store, 'help_ep5_milf', 0) == 0:
            return _('(1 ур)')
        
        if getattr(store, 'help_ep5_milf', 0) == 1:
            return _('(2 ур)')
        
        if getattr(store, 'help_ep5_milf', 0) >= 2:
            return _('(3 ур)')

    def unlock_help_def():
        
        global store
        if getattr(store, 'help_ep3_milf_14', 0) == 0:
            return _('(1 ур)')
        
        if getattr(store, 'help_ep3_milf_14', 0) == 1:
            return _('(2 ур)')
        
        if getattr(store, 'help_ep3_milf_14', 0) >= 2:
            return _('(3 ур)')

    def unlock_shower_together_def():
        
        global store
        if getattr(store, 'unlock_shower_together_3', 0):
            return _('(3 ур)')
        
        if getattr(store, 'unlock_shower_together_2', 0):
            return _('(2 ур)')
        
        if getattr(store, 'unlock_shower_together', 0):
            return _('(1 ур)')

    def fix_descript_info(descript):
        if descript == "" or '[version_now]' in descript or descript in (   "Конец рута Кэт для эпизода 6",
            _("Конец рута Кэт для эпизода 6"),
            __("Конец рута Кэт для эпизода 6"),
            "Конец рута Кристи для эпизода 1.0",
            _("Конец рута Кристи для эпизода 1.0"),
            __("Конец рута Кристи для эпизода 1.0")

            ):
            return __("Конец истории этого персонажа.")
                


        return store._dscr_kostil_0(__(descript))
screen descript_screen:
    zorder 850
    imagebutton:
        idle '#000a'
        hover '#000a'
        action Hide('descript_screen')

    imagebutton:
        idle 'interface/Quest_Menu.png'
        hover 'interface/Quest_Menu.png'
        action NullAction()
        xalign .5 yalign .5
    text _('Заметки') xalign .52 outlines [(1, "#000", 0, 0)] ypos 190 size 55 bold True
    viewport xalign .5 yalign .5:
        xmaximum 1365
        ymaximum 817
        add '#0000'

        #if getattr(store, 'descript', '') != '':
        viewport:
            xmaximum 175
            ymaximum 212

            imagebutton:
                at ButtonEffect01
                idle '#0000'
                hover '#fffa'
                action SetVariable('old_descript', descript), Show('descript_screen_2', who = 'Milf', main = True)
            if not getattr(store, 'not_survival', False):
                $ _l_q = getattr(store, 'milf_love_quests', 0)+1
                add 'heart_icon' xpos 16 ypos 158
                viewport:
                    xmaximum 40
                    ymaximum 31
                    add '#0000'

                    xpos 30 ypos 162
                    if _l_q >= love_milf:
                        text str(love_milf) + "/"+str(_l_q) size 20 color '#fffa' xalign .5 yalign .5 bold True
                    else:
                        text str(love_milf) + "/"+str(love_milf+1) size 20 color '#fffa' xalign .5 yalign .5 bold True

                viewport:
                    xmaximum 50
                    ymaximum 35
                    add '#0000'
                    xpos 113 ypos 161
                    text str(relations_milf)+'/50' size 20 color '#000' xalign .5 yalign .5



            xpos 204 ypos 145
        imagebutton:
            if old_descript != descript:
                idle 'interface/new_quest.png'
                at NewEventEffect(157, 176, .25)
            else:
                xpos 157 ypos 176
                idle Transform('interface/new_quest.png', alpha = 0.0)
            hover 'interface/new_quest_red.png'
            action SetVariable('old_descript', descript), Show('descript_screen_2', who = 'Milf', main = True)

        imagebutton:
            if getattr(store, 'new_events', False):
                idle 'interface/new_event.png'
                at NewEventEffect(157, 236)
            else:
                idle Transform('interface/new_event.png', alpha = 0.0)
                xpos 157 ypos 236
            hover 'interface/new_event_red.png'
            action SetVariable('new_events', False), Show('descript_screen_3')

        if getattr(store, 'descript_Christie', '!') != '!':
            viewport:
                xmaximum 175
                ymaximum 212

                imagebutton:
                    at ButtonEffect01
                    idle '#0000'
                    hover '#fffa'
                    action SetVariable('old_descript_Christie', descript_Christie), Show('descript_screen_2', dscr = descript_Christie, who = 'Christie', main = True)
                xpos 460 ypos 145


        imagebutton:
            if getattr(store, 'new_events_christie', False):
                idle 'interface/new_event.png'
                at NewEventEffect(413, 236)
            else:
                idle Transform('interface/new_event.png', alpha = 0.0)
                xpos 413 ypos 236
            hover 'interface/new_event_red.png'
            action SetVariable('new_events_christie', False), Show('descript_screen_3', qeusts_for_christie = True)

















        if getattr(store, 'descript_Christie', '!') != '!':
            imagebutton:

                if old_descript_Christie != descript_Christie:
                    idle 'interface/new_quest.png'
                    at NewEventEffect(413, 176, .25)
                else:
                    idle Transform('interface/new_quest.png', alpha = 0.0)
                    xpos 413 ypos 176
                hover 'interface/new_quest_red.png'

                action SetVariable('old_descript_Christie', descript_Christie), Show('descript_screen_2', dscr = descript_Christie, who = 'Christie', main = True)


        if getattr(store, 'descript_Cat', '!') != '!':
            viewport:
                xmaximum 175
                ymaximum 212

                imagebutton:
                    at ButtonEffect01
                    idle '#0000'
                    hover '#fffa'
                    action SetVariable('old_descript_Cat', descript_Cat), Show('descript_screen_2', dscr = descript_Cat, who = 'Cat', main = True)
                xpos 716 ypos 145

            imagebutton:

                if old_descript_Cat != descript_Cat:
                    idle 'interface/new_quest.png'
                    at NewEventEffect(671, 176, .25)
                else:
                    idle Transform('interface/new_quest.png', alpha = 0.0)
                    xpos 671 ypos 176
                hover 'interface/new_quest_red.png'
                action SetVariable('old_descript_Cat', descript_Cat), Show('descript_screen_2', dscr = descript_Cat, who = 'Cat', main = True)

        if getattr(store, 'descript_Misha', '!') != '!':
            viewport:
                xmaximum 175
                ymaximum 212

                imagebutton:
                    at ButtonEffect01
                    idle '#0000'
                    hover '#fffa'
                    action SetVariable('old_descript_Misha', descript_Misha), Show('descript_screen_2', dscr = descript_Misha, who = 'Misha', main = True)
                xpos 716+257 ypos 145

            imagebutton:

                if old_descript_Misha != descript_Misha:
                    idle 'interface/new_quest.png'
                    at NewEventEffect(671+257, 176, .25)
                else:
                    idle Transform('interface/new_quest.png', alpha = 0.0)
                    xpos 671+257 ypos 176
                hover 'interface/new_quest_red.png'
                action SetVariable('old_descript_Misha', descript_Misha), Show('descript_screen_2', dscr = descript_Misha, who = 'Misha', main = True)
























label talk_with_igor_label_with_images:
    call show_all_images_label from _call_show_all_images_label_106
    with Dissolve(.5)
    jump talk_with_igor_label

label talk_with_milf_label_with_images:
    call show_all_images_label from _call_show_all_images_label_107
    with Dissolve(.5)
    jump talk_with_milf_label


label talk_with_sister_label_with_images:
    call show_all_images_label from _call_show_all_images_label_108
    with Dissolve(.5)
    jump talk_with_sister_label


label talk_with_jay_bob_label_with_images:
    call show_all_images_label from _call_show_all_images_label_109
    with Dissolve(.5)
    jump talk_with_jay_bob_label



image activate_quest_hover = Text('Активировать квест\n         (WIP)', color = '#ae845e', font = 'fonts/FUTURA-N.ttf', bold = True, size = 40)

image activate_quest_idle = Transform('activate_quest_hover', alpha = .55)

init python:
    def _dscr_kostil_0(dscr):
        if '\n' in dscr and '{s}' in dscr:
            rdvv = ''
            bdsl = dscr.split('\n')
            j    = 0
            for i in bdsl:
                
                
                blldd = _dscr_kostil(__(i.replace('{s}', '').replace('{/s}','')))
                if '{s}' in i:
                    blldd = "{s}" + blldd + "{/s}"
                rdvv += blldd
                

                j    += 1
                #if j != len(bdsl) -1: 
                rdvv += '\n'
            return rdvv
        return _dscr_kostil(dscr)
    def _dscr_kostil(dscr):
        if preferences.language in ('chinese_trad', 'chinese_simpl', 'kor', 'jap'):
            return dscr
        chars_list = ('.', ',', '?', '!', ':', '…', ')', '}')

        r_dscr   = dscr
        len_dscr = len(dscr)
        check_1  = True
        check_2  = True
        check_3  = True
        if len_dscr >= 1:    
            check_1  = dscr[len_dscr-1] not in chars_list
        if len_dscr >= 2:
            check_2 = dscr[len_dscr-2] not in chars_list
        if len_dscr >= 3:
            check_3 = dscr[len_dscr-3] not in chars_list

        

        if check_1 and check_2 and check_3:
            r_dscr += '.'
        r_dscr = r_dscr.replace('Marina', 'Mary')
        r_dscr = r_dscr.replace('marina', 'mary')
        r_dscr = r_dscr.replace('MARINA', 'MARY')
        return r_dscr

screen descript_screen_2(dscr=descript, who=None, main = False):
    zorder 870
    imagebutton:
        idle '#000a'
        hover '#000a'
        action Hide('descript_screen_2')
    add 'interface/Quest_Text.png' xalign .5 yalign .5

    text _('Заметки') xalign .52 outlines [(1, "#000", 0, 0)] ypos 190
    viewport xalign .52 yalign .541:
        xmaximum 900
        ymaximum 597

        vbox:
            text store.fix_descript_info(dscr) color '#000' line_spacing 0
            if dscr == getattr(store, 'descript_Christie', '@!@!@!'):
                use ep4_milf_37_block_igor_descript_screen_2

    
    if who:
        default describe_text = False
        
        $ events_list_6_28 = test_get_events_list(who, main)
        
        # imagebutton:
        #     xalign .5
        #     ypos 700+patreon_descript_ypos
        #     idle 'activate_quest_idle'
        #     hover 'activate_quest_hover'

        #     hovered SetScreenVariable('describe_text', True)
        #     unhovered SetScreenVariable('describe_text', False)

            
        #     action Function(test_event_check_jump, events_list_6_28)

            

        # if describe_text:
        #     vbox:
        #         xalign .5
        #         ypos 800+patreon_descript_ypos
        #         spacing 5
        #         #image 'activate_quest_info_0' xalign .5
        #         #image 'activate_quest_info_1' xalign .5
        #         #image 'activate_quest_info_2' xalign .5
        


screen descript_screen_3(qeusts_for_christie=False):

    zorder 870
    imagebutton:
        idle '#000a'
        hover '#000a'
        action Hide('descript_screen_3')
    add 'interface/Quest_Text.png' xalign .5 yalign .5

    text _('Заметки') xalign .52 outlines [(1, "#000", 0, 0)] ypos 190 size 40
    viewport xalign .52 ypos 250:
        xmaximum 900
        ymaximum 597

        has vbox:
            spacing -5
        if qeusts_for_christie:

            viewport:
                xmaximum 400
                ymaximum 50
                add '#0000'
                if hasattr(store, 'tyan_falos_text'):
                    textbutton _('Ночная услада'):
                        text_font gui.text_font
                        text_color '#000'
                        text_hover_color '#000a'
                        if str(tyan_falos_text) not in descript_screen_3_list:
                            text_outlines [(3, "#fff", 0, 0)]
                            at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                            action Function(descript_screen_3_list.append, str(tyan_falos_text)), Show('descript_screen_2', dscr = str(tyan_falos_text))

                        else:
                            action Show('descript_screen_2', dscr = str(tyan_falos_text))
                else:
                    textbutton _('Ночная услада'):
                        text_font gui.text_font
                        text_color '#0006'
                        text_hover_color '#0006'
                        action NullAction()
            viewport:
                xmaximum 400
                ymaximum 50
                add '#0000'
                if hasattr(store, 'christie_night_mischief_text'):
                    textbutton _('Ночные кошмары'):
                        text_font gui.text_font
                        text_color '#000'
                        text_hover_color '#000a'
                        if str(christie_night_mischief_text) not in descript_screen_3_list:
                            text_outlines [(3, "#fff", 0, 0)]
                            at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                            action Function(descript_screen_3_list.append, str(christie_night_mischief_text)), Show('descript_screen_2', dscr = str(christie_night_mischief_text))

                        else:
                            action Show('descript_screen_2', dscr = str(christie_night_mischief_text))
                else:
                    textbutton _('Ночные кошмары'):
                        text_font gui.text_font
                        text_color '#0006'
                        text_hover_color '#0006'
                        action NullAction()

            viewport:
                xmaximum 400
                ymaximum 50
                add '#0000'
                if hasattr(store, 'tyan_falos_text'):
                    $ i = 'Ванна' not in descript_screen_3_list
                    textbutton _('Ванна'):
                        text_font gui.text_font
                        text_color '#000'
                        text_hover_color '#000a'
                        if i:
                            text_outlines [(3, "#fff", 0, 0)]
                            at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                            action Function(descript_screen_3_list.append, 'Ванна'), Show('descript_screen_2', dscr = __("Зайти в ванную комнату когда там Кристи"))

                        else:
                            action Show('descript_screen_2', dscr = __("Зайти в ванную комнату когда там Кристи"))
                    if i:
                        add 'warning_icon' ypos 10 xpos 140
                else:
                    textbutton _('Ванна'):
                        text_font gui.text_font
                        text_color '#0006'
                        text_hover_color '#0006'
                        action NullAction()

            viewport:
                xmaximum 400
                ymaximum 50
                add '#0000'
                if hasattr(store, 'tyan_mischief_text'):
                    textbutton _('Дневные шалости'):
                        text_font gui.text_font
                        text_color '#000'
                        text_hover_color '#000a'
                        if str(tyan_mischief_text) not in descript_screen_3_list:
                            text_outlines [(3, "#fff", 0, 0)]
                            at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                            action Function(descript_screen_3_list.append, str(tyan_mischief_text)), Show('descript_screen_2', dscr = str(tyan_mischief_text))

                        else:
                            action Show('descript_screen_2', dscr = str(tyan_mischief_text))
                else:
                    textbutton _('Дневные шалости'):
                        text_font gui.text_font
                        text_color '#0006'
                        text_hover_color '#0006'
                        action NullAction()


        else:

            viewport:
                xmaximum 400
                ymaximum 50
                add '#0000'

                textbutton _('Магия'):
                    text_font gui.text_font
                    text_color '#000'
                    text_hover_color '#000a'
                    if 'Магия' not in descript_screen_3_list:
                        text_outlines [(3, "#fff", 0, 0)]
                        at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                        action Function(descript_screen_3_list.append, 'Магия'), Show('descript_screen_2', dscr = _('Необходимо купить магические-часы в интернет-магазине.'))


                    else:
                        action Show('descript_screen_2', dscr = _('Необходимо купить магические-часы в интернет-магазине.'))


            viewport:
                xmaximum 400
                ymaximum 50
                add '#0000'

                textbutton __('Массаж'):
                    text_font gui.text_font
                    text_color '#000'
                    text_hover_color '#000a'
                    if 'Массаж ' + unlock_massage_def() not in descript_screen_3_list:
                        text_outlines [(3, "#fff", 0, 0)]
                        at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                        action Function(descript_screen_3_list.append, 'Массаж ' + unlock_massage_def()), Show('descript_screen_2', dscr = _('Необходимо поговорить с Мариной в зале днём, когда она делает уборку.'))

                    else:
                        action Show('descript_screen_2', dscr = _('Необходимо поговорить с Мариной в зале днём, когда она делает уборку.'))
            viewport:

                xmaximum 400
                ymaximum 50
                add '#0000'
                if hasattr(store, 'help_ep3_milf_14'):
                    textbutton __('Помощь'):
                        text_font gui.text_font

                        text_color '#000'
                        text_hover_color '#000a'
                        if 'Помощь ' + unlock_help_def() not in descript_screen_3_list:
                            text_outlines [(3, "#fff", 0, 0)]
                            at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                            action Function(descript_screen_3_list.append, 'Помощь ' + unlock_help_def()), Show('descript_screen_2', dscr = _('Необходимо поговорить с Мариной в коридоре днём.'))

                        else:
                            action Show('descript_screen_2', dscr = _('Необходимо поговорить с Мариной в коридоре днём.'))
                else:
                    textbutton __('Помощь') + ' ' + __(unlock_help_def()):
                        text_font gui.text_font
                        text_color '#0006'
                        text_hover_color '#0006'
                        action NullAction()
            viewport:
                xmaximum 400
                ymaximum 50
                add '#0000'
                if getattr(store, 'unlock_shower_together', 0):
                    textbutton __('Душ вместе'):
                        text_font gui.text_font
                        text_color '#000'
                        text_hover_color '#000a'
                        if 'Душ вместе ' + unlock_shower_together_def() not in descript_screen_3_list:
                            text_outlines [(3, "#fff", 0, 0)]
                            at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                            action Function(descript_screen_3_list.append, 'Душ вместе ' + unlock_shower_together_def()), Show('descript_screen_2', dscr = _('Необходимо поговорить с Мариной в ванной утром.'))

                        else:
                            action Show('descript_screen_2', dscr = _('Необходимо поговорить с Мариной в ванной утром.'))
                else:
                    textbutton __('Душ вместе')+' ' + __('(1 ур)'):
                        text_font gui.text_font
                        text_color '#0006'
                        text_hover_color '#0006'
                        action NullAction()

            viewport:
                xmaximum 400
                ymaximum 50
                add '#0000'
                if getattr(store, 'unlock_masturbation_restroom', 0):
                    textbutton __('Наблюдение в душе'):
                        text_font gui.text_font
                        text_color '#000'
                        text_hover_color '#000a'
                        if 'Наблюдение в душе' not in descript_screen_3_list:
                            text_outlines [(3, "#fff", 0, 0)]
                            at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                            action Function(descript_screen_3_list.append, 'Наблюдение в душе'), Show('descript_screen_2', dscr = _('Необходимо зайти в ванну когда там Марина.'))
                        else:
                            action Show('descript_screen_2', dscr = _('Необходимо зайти в ванну когда там Марина.'))
                else:
                    textbutton __('Наблюдение в душе'):
                        text_font gui.text_font
                        text_color '#0006'
                        text_hover_color '#0006'
                        action NullAction()

            viewport:
                xmaximum 400
                ymaximum 50
                add '#0000'
                if getattr(store, 'milf_shower_ep3', 0):
                    $ i = 'Ласкать' not in descript_screen_3_list
                    textbutton __('Ласкать'):
                        text_font gui.text_font
                        text_color '#000'
                        text_hover_color '#000a'
                        if i:
                            text_outlines [(3, "#fff", 0, 0)]
                            at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                            action Function(descript_screen_3_list.append, 'Ласкать'), Show('descript_screen_2', dscr = _('Надо подойти к марине на кухне'))


                        else:
                            action Show('descript_screen_2', dscr = _('Надо подойти к марине на кухне'))
                    if i:
                        add 'warning_icon' ypos 10 xpos 140
                else:
                    
                    textbutton __('Ласкать'):
                        text_font gui.text_font
                        text_color '#0006'
                        text_hover_color '#0006'
                        action NullAction()

            viewport:
                xmaximum 400
                ymaximum 50
                add '#0000'
                if getattr(store, 'gg_hungry_ep1075', 0):
                    
                    $ i = 'Голод' not in descript_screen_3_list
                    textbutton __('Голод'):
                        text_font gui.text_font
                        text_color '#000'
                        text_hover_color '#000a'
                        if i:
                            text_outlines [(3, "#fff", 0, 0)]
                            at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                            action Function(descript_screen_3_list.append, 'Голод'), Show('descript_screen_2', dscr = _("Я проголодался… Стоит заглянуть на кухню."))


                        else:
                            action Show('descript_screen_2', dscr = _("Я проголодался… Стоит заглянуть на кухню."))
                    if i:
                        add 'warning_icon' ypos 10 xpos 140
                else:
                    
                    textbutton __('Голод'):
                        text_font gui.text_font
                        text_color '#0006'
                        text_hover_color '#0006'
                        action NullAction()
                

            viewport:
                xmaximum 400
                ymaximum 50
                add '#0000'
                if getattr(store, 'unlock_film_1', 0) or getattr(store, "unlock_film_lolita", 0):
                    textbutton _('Фильм'):
                        text_font gui.text_font
                        text_color '#000'
                        text_hover_color '#000a'
                        if 'Фильм' not in descript_screen_3_list:
                            text_outlines [(3, "#fff", 0, 0)]
                            at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                            action Function(descript_screen_3_list.append, 'Фильм'), Show('descript_screen_2', dscr = _('Необходимо иметь диск с необходимым фильмом и предложить Марине посмотреть его в зале вечером.'))

                        else:
                            action Show('descript_screen_2', dscr = _('Необходимо иметь диск с необходимым фильмом и предложить Марине посмотреть его в зале вечером.'))
                else:
                    textbutton _('Фильм'):
                        text_font gui.text_font
                        text_color '#0006'
                        text_hover_color '#0006'
                        action NullAction()

            viewport:

                xmaximum 400
                ymaximum 50
                add '#0000'
                if hasattr(store, 'milf_root_1_text'):
                    textbutton __('Пробка'):
                        text_font gui.text_font

                        text_color '#000'
                        text_hover_color '#000a'
                        if str(milf_root_1_text) not in descript_screen_3_list:
                            text_outlines [(3, "#fff", 0, 0)]
                            at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                            action Function(descript_screen_3_list.append, str(milf_root_1_text)), Show('descript_screen_2', dscr = str(milf_root_1_text))

                        else:
                            action Show('descript_screen_2', dscr = str(milf_root_1_text))
                else:
                    textbutton __('Пробка'):
                        text_font gui.text_font
                        text_color '#0006'
                        text_hover_color '#0006'
                        action NullAction()

            viewport:

                xmaximum 400
                ymaximum 50
                add '#0000'
                if hasattr(store, 'milf_root_9_text'):
                    textbutton __('Грязная игра'):
                        text_font gui.text_font

                        text_color '#000'
                        text_hover_color '#000a'
                        if str(milf_root_9_text) not in descript_screen_3_list:
                            text_outlines [(3, "#fff", 0, 0)]
                            at NewEventEffect(0, 0, renpy.random.choice([.2, .25, .175]))
                            action Function(descript_screen_3_list.append, str(milf_root_9_text)), Show('descript_screen_2', dscr = str(milf_root_9_text))

                        else:
                            action Show('descript_screen_2', dscr = str(milf_root_9_text))
                else:
                    textbutton __('Грязная игра'):
                        text_font gui.text_font
                        text_color '#0006'
                        text_hover_color '#0006'
                        action NullAction()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
