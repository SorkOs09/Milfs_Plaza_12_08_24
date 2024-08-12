screen in_clothes_store_screen:
    imagebutton:
        idle 'cg/ep89/shop/masha.png'
        hover im.MatrixColor('cg/ep89/shop/masha.png', im.matrix.brightness(.3))
        focus_mask True
        at ButtonEffect01
        action Return()

    add 'back_button'
    imagebutton:

        idle 'back_button_hover'
        hover 'back_button_hover'
        focus_mask True
        at ButtonEffect01

        action Function(JumpToLocation, 'City_Home')

    use icons_interface


label talk_with_clothes_store_woman_label:
    scene expression '#000' with Dissolve(.5)
    $ renpy.play('audio/Door.mp3')



label talk_with_clothes_store_woman_menu:
    scene image 'locations/bg/ClothesStore/afternoon.png'
    hide screen icons_interface

    show image 'cg/ep89/shop/masha.png'
    with Dissolve(.5)


    $ location_now = 'Store_Masha'
    $ check_ev     = check_events()



    $ location_now = 'ClothesStore'
    call screen in_clothes_store_screen

label talk_with_clothes_store_woman_menu_2:
    
    

    menu:
        "Говорить" if check_ev:
            $ renpy.jump(check_ev.label)
        "Магазин." if True:
            call check_surv_label from _call_check_surv_label_2
            show expression '#000a'
            show expression 'interface/Inventory.png':
                xalign .5
                yalign .5
            show expression 'interface/Grid.png':
                xalign .5
                yalign .5

            with Dissolve(.5)
            $ storein_costumes_shop_items_fix_0_8_9_d = []

            

            if events.get('christie_root_33'):
                if 'Костюм Харли Квин.' not in storein_costumes_shop_items:
                    $ storein_costumes_shop_items_fix_0_8_9_d.append('Костюм Харли Квин.')

            if events.get('cat_root_3_0'):
                if 'Чёрные очки' not in storein_costumes_shop_items:
                    $ storein_costumes_shop_items_fix_0_8_9_d.append('Чёрные очки')

            

            python:
                store_events_items_fix_0_9      = []
                for evn in fashion_store_events_items:
                    if evn in events:
                        for i in fashion_store_events_items[evn]: 
                            store_events_items_fix_0_9.append(i) 


            call screen storein_shop(storein_costumes_shop_items+storein_costumes_shop_items_fix_0_8_9_d, store_events_items_fix_0_9)     
            scene image 'locations/bg/ClothesStore/afternoon.png'
            show image 'cg/ep89/shop/masha.png'
            with Dissolve(.5)
            jump talk_with_clothes_store_woman_menu_2
        "Назад." if True:
            $ location_now = 'talk_with_clothes_store_woman_menu_after'
            $ check_ev     = check_events()

            if check_ev:
                $ Jump(check_ev.label)()

            $ location_now = 'City_Home'
            $ check_ev     = check_events()

            if check_ev:
                $ Jump(check_ev.label)()

            $ renpy.play('audio/Door.mp3')
            scene expression '#000' with Dissolve(.5)


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
