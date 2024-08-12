# image activate_quest_info_0 = Text(__('Это функция принудительного запуска сцены по текущему квесту.'), color = '#ae845e', font = 'fonts/FUTURA-N.ttf', size = 31)
# image activate_quest_info_1 = Text(__('Использовать только в {b}крайних{/b} случаях, например, когда задание не проходимо из-за бага.'), color = '#ae845e', font = 'fonts/FUTURA-N.ttf', size = 31)
# image activate_quest_info_2 = Text(__("Только для подписчиков Boosty"), color = '#ae845e', font = 'fonts/FUTURA-N.ttf', size = 31)

# init 1000 python:
#     config.version += "_public"

# init -500 python:
#     patreon_descript_ypos = 0

#     for i in images_exts_list:

#         build.classify('game/images/characters/Milf/EMO/**.'+i,  'images')
#         build.classify('game/images/characters/Milf/atlas/**.'+i,  'images')
    
#         for j in ('Blin','n_body','Night_Pose_1','Night_Pose_2','Night_Pose_3'):
#             build.classify('game/images/characters/Milf/1POSES/' + j + "." + i, "images")

#     build.classify('game/images/characters/Milf/1POSES/bdsm.png', None)

#     build.classify('game/images/characters/Milf/1POSES/cow.png', None)

#     build.classify('game/images/characters/Milf/1POSES/gantz.png', None)

#     only_for_subs = Function(show_text_animation, __('Только для подписчиков Boosty'))

#     def unlock_gallery():
#         only_for_subs()


#     def gallery_return():
#         mp.gallery_save = None
#         mp.save()
#     def test_check_evnt_label(event_label, labels_list):
        
#         return False
#     def test_get_events_list(for_who='Milf', main = False):
#         need_return = []
#         return need_return


#     def test_event_check_jump(_list):
        
#         Show('descript_screen_activate_quest')()




#     def test_event_jump(event_name = None):
#         only_for_subs()
        


# screen descript_screen_activate_quest(events_list_to_show=[]):
#     zorder 890
#     imagebutton:
#         idle '#000a'
#         hover '#000a'
#         action Hide('descript_screen_activate_quest')
#     add 'interface/Quest_Text.png' xalign .5 yalign .5
#     vbox:
#         xalign .5
#         yalign .5
#         spacing 5

#         add Text(__("Только для подписчиков Boosty"), color = '#ae845e', font = 'fonts/FUTURA-N.ttf', bold = True, size = 40)




# ###############################
# #phone



# init python:
#     def plus_nastroi(plus=0):
#         only_for_subs()

#     def plus_gigiena(plus=0):
#         only_for_subs()

#     def plus_sitost(plus=0):
#         only_for_subs()

#     def plus_money(plus=0):
#         only_for_subs()


# screen Phone_Cheats_Screen:
#     zorder 20
#     imagebutton:
#         idle '#000a'
#         hover '#000a'
#         action Hide('Phone_Cheats_Screen')
    

# image phone_cheats = 'interface/phone_interface/phone_cheats.png'

# screen phone_cheats_patreon:
#     imagebutton:
#         idle 'phone_cheats'
#         hover 'phone_cheats'
#         action only_for_subs
#         xpos 1100
#         ypos 240
#         at ButtonEffect07


# #phone
# ###############################





# ###############################
# #costume

# init -500 python:
#     milf_additional_costumes = list()


# label milf_standart_talk_gantz:
# label milf_standart_talk_cow:
# label milf_standart_talk_bdsm:

# label milf_costume_0:


#     '[gg]' "Только для подписчиков Boosty"
#     return





# #costume
# ###############################

