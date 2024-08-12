
label cat_root_3_0:
    $ events.pop('cat_root_3_0', 0)
    $ Event('talk_with_clothes_store_woman_menu', 'ClothesStore')

    $ Event('cat_root_3_1', 'City_Home')

    $ location_now = 'ClothesStore'
    jump talk_with_clothes_store_woman_menu

label cat_root_3_1:

    $ location_now = 'City_Home'
    $ renpy.play('audio/Door.mp3')
    scene expression '#000' with Dissolve(.5)
    $ events.pop('cat_root_3_1', 0)
    if get_item('Чёрные очки', True, True):
        call show_bg_image_label from _call_show_bg_image_label_106
        $ events.pop('cat_root_3_0', 0)
        show GG Think
        with Dissolve(.5)
        "[gg]" "Отлично, теперь я могу заделался «частным сыщиком» и устраивать настоящие слежки."
        show GG Think
        "[gg]" "Мне лишь нужно дождаться, пока Кэт будет выходить из дома поздно вечером и проследить за ней."
        $ descript_Cat = _('Проследить за Кэт вечером у входа в дом.')
        $ Event('cat_root_4', 'City_Home', time = ['evening'])

        jump main_interface_label
    elif True:
        $ location_now = 'City_Home'
        $ events.pop('talk_with_clothes_store_woman_menu', 0)
        $ Event('cat_root_3_0', 'ClothesStore')


        $ JumpToLocation('City_Home')
        jump main_interface_label

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
