label christie_root_47_restroom:
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    scene image 'locations/bg/Restroom/morning.png'
    
    show image 'cg/milf_and_sister_activities/sister_restroom.png' 

    show expression 'cg/christie_root/GG_See_PsiKri_w_bg.png'
    
    show expression 'cg/christie_root/GG_See_PsiKri_0.png'
    with my_dissolve


    call screen christie_root_30_screen(2)
    
    scene image 'locations/bg/Restroom/morning.png'
    
    show image 'cg/milf_and_sister_activities/sister_restroom.png' 

    show expression 'cg/christie_root/GG_See_PsiKri_w_bg.png'
    
    show expression 'cg/christie_root/GG_See_PsiKri_0.png':

        xpos 0
        easein_cubic 1.5 xpos -780
    $ renpy.pause(1, hard = True)

    $ location_now = 'Corridor'
    "[gg]" "Ничего не выйдет, она принимает только ванну, а Игорь ясно дал понять, что такие видео ему не нужны."
    $ christie_root_47_restroom = True
    jump christie_root_47_check 

    #//Руки с дверьми

    #//На фоне тупо Чёрный экран
label christie_root_47_sister_room:
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    scene image 'locations/bg/Sister_Room/night.png'
    
    show image 'cg/milf_and_sister_activities/sister_room_night.png' 

    show image '#000c'



    show expression 'cg/christie_root/falos/0.png'
    show expression 'cg/christie_root/falos/1_0.png'
    with Dissolve(.5)

    hide expression 'cg/christie_root/falos/1_0.png'

    
    call screen christie_root_30_screen(1, 'cg/christie_root/falos/1_0.png')
    show expression 'cg/christie_root/falos/1_0.png'
    with None
    show expression 'cg/christie_root/falos/1_1.png':
        xpos 0
    with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    hide expression 'cg/christie_root/falos/1_0.png'
    call screen christie_root_30_screen(2, 'christie_root_43 door_bg')
    show expression 'cg/christie_root/falos/1_1.png':
        xpos 0
        easein_cubic 1.5 xpos -800

    $ renpy.pause(1, hard = True)

    $ location_now = 'Corridor'
    "[gg]" "Нет, так не получится. Слишком темно. Если я сниму видео, там всё будет чёрное. "
    $ christie_root_47_sister_room = True
    jump christie_root_47_check


label christie_root_47_check:
    if hasattr(store, 'christie_root_47_restroom'): 
        if hasattr(store, 'christie_root_47_sister_room'):

            jump christie_root_47
    
    jump main_interface_label

label christie_root_47:

    $ block_change_milf_position = copy.deepcopy(block_change_milf_position_christie_root_46)    
    $ block_milf_home = copy.deepcopy(block_milf_home_christie_root_46)

    $ del block_change_milf_position_christie_root_46 
    $ del block_milf_home_christie_root_46


    $ del christie_root_47_sister_room
    $ del christie_root_47_restroom


    $ events.pop('christie_root_47_sister_room', 0)
    $ events.pop('christie_root_47_restroom', 0)
    $ location_now = 'Corridor'
    call show_bg_image_label from _call_show_bg_image_label_184

    
    #//После того, как Игрок активировать оба пункта

    #"Scene" ""
    show GG Think
    show GG Think:
        xalign .5
    with my_dissolve
    "[gg]" "Хм…."
    show GG Think
    "[gg]" "Может, спровоцировать её как-то?"
    show GG Think
    "[gg]" "После моего массажа, она, как правило, убегала в комнату, чтобы кончить самостоятельно."
    show GG Think
    "[gg]" "И что мне, снимать мастурбацию Кристи для Игоря?.."
    show GG Think
    "[gg]" "Нет, это чересчур. "
    show GG Think
    "[gg]" "А что если…"
    show GG Think
    "[gg]" "В дневное время Кристи обожает читать электронную книгу в зале."
    show GG Think
    "[gg]" "В её комнате слишком душно, и она любит сидеть под лёгкой прохладой кондиционера. "
    show GG Think
    "[gg]" "Можно попробовать сломать его и, возможно, Кристи захочет снять с себя одежду."
    show GG Think
    "[gg]" "Ну а я, чтобы не пропустить этот момент, заранее установлю телефон возле телевизора."
    show GG Think
    "[gg]" "Что ж, это план. Надо пробовать."
    show GG Think
    "[gg]" "Прежде чем лезть в кондиционер, мне пригодится отвёртка. Куплю её в магазине."
    
    
    #Tian_48

    $ descript_Christie = _("Купить отвёртку в Магазине.")
    $ screw_at_shop = 33
    if not hasattr(store, 'add_items_for_storein_shop_fixed'):
        $ add_items_for_storein_shop_fixed = []
    $ add_items_for_storein_shop_fixed.append(screw_at_shop)
    $ Event('christie_root_48', location = 'City_Shop', need_items = [33,])

    $ Event('christie_root_49', location = 'Hall', need_items = [33,], time = ['night', ])

    jump main_interface_label