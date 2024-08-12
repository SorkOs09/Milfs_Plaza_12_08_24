

label ep5_milf_72:

    $ block_exit_home = False
    $ block_time_forward = True
    scene expression 'images/interface/city_interface/city_bg_' + time.time_now + '.png'
    with Dissolve(.5)
    call screen ep4_milf_70_city_screen('city_home_button')


























    $ location_now  = 'City_Home'
    $ time.time_now = 'night'
    call show_all_images_label from _call_show_all_images_label_47

    show GG Bat_Normal:
        xalign -1.5

    with Dissolve(.5)


    show GG Bat_Normal:
        linear 1 xalign .1
    $ renpy.pause(1)

    show GG Bat_Normal:
        xalign .1
    with my_dissolve
    $ stnd_music_play()
    "[gg]" "Ну вот, я опоздал. Уже совсем позднее время…"
    show GG Bat_Sad
    "[gg]" "Надеюсь, мой план хотя бы частично реализовался."
    show GG Bat_Smile
    "[gg]" "Или вообще ничего не произошло."
    $ block_map = True
    $ descript = _('Вернуться домой.')


    $ Event('ep5_milf_72_2', 'Corridor')
    $ block_igor_position = False
    # $ igor_position = {
    #     'morning'   : ('City_Park',  'igor_park'),
    #     'afternoon' : ('City_Park',  'igor_park'),
    #     'evening'   : ('None',       'None'),
    #     'night'     : ('None',       'None'),
        
    #     }
    jump main_interface_label






























label ep5_milf_72_2:
    $ events.pop('ep5_milf_72_2', 0)
    scene black
    with Dissolve(.5)
    call show_all_images_label from _call_show_all_images_label_48
    show GG Bat_Normal
    show GG Bat_Normal:
        xalign .1

    with my_dissolve
    "[gg]" "Подозрительно тихо…"
    show GG Bat_Normal
    "[gg]" "Даже слишком…"
    show GG Bat_Normal
    "[gg]" "Ну и чего я паникую? Может, Марина уже давно выпроводила офицера домой и легла спать."
    show GG Bat_Normal
    "[gg]" " Да и брат, судя по всему, или не явился, или его убедили, что он заблуждается. "
    show GG Bat_Normal
    "[gg]" "Иначе я и не могу… Да и не хочу объяснять эту гробовую тишину."
    show GG Bat_Normal
    "[gg]" "Да если предположить… "
    show GG Bat_Normal
    "[gg]" "Нет, не хочу даже думать о таком. "
    show GG Bat_Normal
    "[gg]" "Но хорошо- хорошо! Подумаю!"
    show GG Bat_Normal
    "[gg]" " Даже если предположить в самом дурном сне, что брат застукал Марину с офицером в момент приёма пищи, офицер не успел спрятаться в туалет, или вовсе не стал прятаться… слово за слово, и кто-то кого-то убил…."
    show GG Bat_Normal
    "[gg]" "Если бы офицер оборонялся и застрелил брата, то здесь давно уже толпились бы куча легавых, убийство оформили бы как самозащиту, а мне бы пришло смс от Марины с просьбой приехать в полицейский участок."
    show GG Bat_Normal
    "[gg]" "Если бы всё брат взял вверх в схватке, то смс мне пришла бы от него."
    show GG Bat_Normal
    "[gg]" "Как бы я не осуждал его поступок, но я единственный, кому он доверяет на 146%%."
    show GG Bat_Normal
    "[gg]" "А значит, здесь точно никто и никого не убивал…"
    show GG Bat_Normal
    "[gg]" "Что ж, это меня несколько успокаивает."
    show GG Bat_Normal
    "[gg]" "Пожалуй, прежде чем проверить Марину у себя в комнате, я должен переодеться. "



    $ descript = _('Переодеться в повседневную одежду у себя в комнате.')

    $ block_exit_home   = True
    $ block_milf_home   = True
    $ block_sister_home = True

    $ Event('ep5_milf_73_stump_1', 'Hall', 'ep5_milf_73_stump')
    $ Event('ep5_milf_73_stump_2', 'Restroom', 'ep5_milf_73_stump')
    $ Event('ep5_milf_73_stump_3', 'Kitchen', 'ep5_milf_73_stump')
    $ Event('ep5_milf_73_stump_4', 'Sister_Room', 'ep5_milf_73_stump')

    $ locations['GG_Room'].image_buttons.update({
            'pants_ep5_milf_72': Jump('ep5_milf_73'),

            })



    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
