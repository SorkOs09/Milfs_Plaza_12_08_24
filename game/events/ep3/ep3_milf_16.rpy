

label ep3_milf_16:



label ep3_milf_16_1:
    $ location_now = 'Corridor'

    call show_all_images_label from _call_show_all_images_label_41 #from _call_show_all_images_label_36


    $ events['ep3_milf_16_1'].complete = True
    "[gg]" "Судя по всему, в комнате её нет."
    call ep3_milf_16_check_final from _call_ep3_milf_16_check_final #from _call_ep3_milf_16_check_final

    jump main_interface_label



label ep3_milf_16_2:
    $ location_now = 'Restroom'
    $ Hide('main_interface', transition = Dissolve(.5))()
    call show_all_images_label from _call_show_all_images_label_98 #from _call_show_all_images_label_37

    $ events['ep3_milf_16_2'].complete = True
    "[gg]" "Здесь никого."
    call ep3_milf_16_check_final from _call_ep3_milf_16_check_final_1 #from _call_ep3_milf_16_check_final_1

    jump main_interface_label

label ep3_milf_16_3:
    $ location_now = 'Kitchen'
    $ Hide('main_interface', transition = Dissolve(.5))()
    call show_all_images_label from _call_show_all_images_label_102 #from _call_show_all_images_label_38


    $ events['ep3_milf_16_3'].complete = True
    "[gg]" "Здесь чисто."
    call ep3_milf_16_check_final from _call_ep3_milf_16_check_final_2 #from _call_ep3_milf_16_check_final_2

    jump main_interface_label

label ep3_milf_16_4:
    $ location_now = 'Hall'
    $ Hide('main_interface', transition = Dissolve(.5))()
    call show_all_images_label from _call_show_all_images_label_103 #from _call_show_all_images_label_39

    $ events['ep3_milf_16_4'].complete = True
    "[gg]" "Кристи, ты тут? "
    call ep3_milf_16_check_final from _call_ep3_milf_16_check_final_3 #from _call_ep3_milf_16_check_final_3

    jump main_interface_label


label ep3_milf_16_5:
    $ location_now = 'Hall'
    $ Hide('main_interface', transition = Dissolve(.5))()
    call show_all_images_label from _call_show_all_images_label_104 #from _call_show_all_images_label_40


    "[gg]" "Сперва я должен проверить, осталась ли Кристи дома."

    call ep3_milf_16_check_final from _call_ep3_milf_16_check_final_4 #from _call_ep3_milf_16_check_final_4

    jump main_interface_label




label ep3_milf_16_check_final:

    if all([

        events['ep3_milf_16_1'].complete,
        events['ep3_milf_16_2'].complete,
        events['ep3_milf_16_3'].complete,
        events['ep3_milf_16_4'].complete,

        ]):
        $ events['ep3_milf_16_5'].complete = True
        jump ep3_milf_16_final
    return

label ep3_milf_16_final:
    if hasattr(store, 'milf_15_audio'):
        $ del milf_15_audio
    if time.time_now == 'night':
        if not renpy.music.get_playing() or 'night' not in renpy.music.get_playing():
            $ renpy.music.stop(fadeout=1.5)
            $ renpy.music.play('audio/night.mp3', fadein = 1.5)

    elif time.time_now == 'morning':
        if not renpy.music.get_playing() or 'morning' not in renpy.music.get_playing():
            $ renpy.music.stop(fadeout=1.5)
            $ renpy.music.play('audio/morning.mp3', fadein = 1.5)
    elif True:


        if not renpy.music.get_playing() or 'day' not in renpy.music.get_playing():
            $ renpy.music.stop(fadeout=1.5)
            $ renpy.music.play('audio/day.mp3', fadein = 1.5)
    $ location_now = 'Corridor'

    $ events.pop('ep3_milf_16_1', 0)
    $ events.pop('ep3_milf_16_2', 0)
    $ events.pop('ep3_milf_16_3', 0)
    $ events.pop('ep3_milf_16_4', 0)
    $ events.pop('ep3_milf_16_5', 0)

    call show_all_images_label from _call_show_all_images_label_105 #from _call_show_all_images_label_41
    with Dissolve(.5)
    show GG Think
    show GG Think:
        xalign .5
        yalign 1.0
    "[gg]" "Квартира абсолютно пустая. Пора действовать!"





    $ locations['Milf_Room'].buttons[0]['picture_2'] = [(425, 0, 175, 235,), [Jump('ep3_milf_17')]]


    $ descript = _('Опробовать все комбинации цифр для открытия сейфа.')


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
