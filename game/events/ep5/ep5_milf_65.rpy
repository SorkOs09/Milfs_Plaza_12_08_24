label ep5_milf_65_1:

    $ events.pop('ep5_milf_65_1', 0)
    $ Event('talk_with_store_woman_label', 'StoreIn')

    $ Event('ep5_milf_65_2', 'City_Shop')

    $ location_now = 'StoreIn'
    jump main_interface_label
label ep5_milf_65_2:
    $ location_now = 'City_Shop'
    $ renpy.play('audio/Door.mp3')
    scene expression '#000' with Dissolve(.5)
    $ events.pop('ep5_milf_65_2', 0)
    if not get_item('Слабительное', True):
        $ location_now = 'City_Shop'
        $ events.pop('talk_with_store_woman_label', 0)
        $ Event('ep5_milf_65_1', 'StoreIn')


        $ JumpToLocation('City_Shop')
        jump main_interface_label
    $ events.pop('ep5_milf_65_1', 0)
    call show_all_images_label from _call_show_all_images_label_5
    show GG Think
    with Dissolve(.5)
    "[gg]" "Вот и всё."

    "[gg]" "Теперь я смогу избавиться от офицера полиции и отправиться освобождать Игоря."

    $ Event('ep5_milf_67', 'Milf')
    $ block_change_milf_position = True
    $ events.pop('ep5_milf_65', 0)
    $ milf_position = {
        'morning'   : ['Kitchen',  'milf_kitchen'],
        'afternoon' : ['Corridor',  'milf_corridor'],
        'evening'   : ['Hall',      'milf_evening_hall'],
        'night'     : ['Milf_Room', 'milf_room'],
        
        }
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
