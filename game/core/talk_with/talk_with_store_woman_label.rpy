init -1000 python:
    storein_shop_items_prices = {
_('Красное вино'):150, 
_('Сок') : 25,
_('Чипсы'):50,
_('Йогурт'):75,
_('Шоколад'):100,
_('Попкорн'):100,
_('Слабительное'):65,
_('Костюм 1'):100,
_('Костюм 2'):100,
_('Чёрные очки'):100,
_('Кикбоксёр'):100,
_('Фильм "Лолита"'):100,
_('Костюм Харли Квин.'):175,
_('Перцовый баллончик'):45,
_('Резак'):150,
_('Дон Кихот'):150,
_('Отвертка'): 50,
_('«Неизвестный» костюм для ролевых игр'):125,
_("Продукты для пикника"):150,

}

image text_info_bg_frame = Frame('text_info_bg', Borders(50, 50, 50, 50))
screen storein_shop(itms=storein_shop_items, itms_by_id=[]):

    imagebutton:
        idle 'alpha_solid'
        hover 'alpha_solid'
        action Return()
    default text_now = None
    default price_now = None
    default text_now_0 = None
    default text_now_1 = None
    default text_now_2 = None
    # viewport:
    #     maximum (1200, 800)
    #     scrollbars "vertical"
    #     mousewheel True
    #     draggable True
    #     xpos 410 ypos 319

    vpgrid:
        xpos 410 ypos 319
        cols 8
        rows 3
    
        for x in itms_by_id:
            $ i = get_item_by_id(x)
            if i:
                viewport:
                    xmaximum 136
                    ymaximum 138
                    add 'alpha_solid'
                    add i.image xpos 15 ypos 25


                    imagebutton xpos 15 ypos 25:
                        xmaximum 115
                        ymaximum 115
                        if get_item_by_id(x, True) == None:
                            idle 'alpha_solid'


                            hover '#000a'
                            at ButtonEffect01
                            unhovered SetScreenVariable('text_now', None), SetScreenVariable('price_now', None)

                            if money >= storein_shop_items_prices[_(i.name)]:
                                #hovered SetScreenVariable('text_now', i.discription), SetScreenVariable('price_now', str(storein_shop_items_prices[_(i.name)]) + '$')
                                
                                hovered SetScreenVariable('text_now_0', i.discription), SetScreenVariable('text_now_1', i.name), SetScreenVariable('text_now_2', str(storein_shop_items_prices[_(i.name)]) + '$') 
                                unhovered SetScreenVariable('text_now_0', None), SetScreenVariable('text_now_1', None), SetScreenVariable('text_now_2', None)
                                action Function(renpy.play, 'audio/money.ogg'), Function(add_to_inventory, name = i.name), SetVariable('money', money - storein_shop_items_prices[_(i.name)]), SetScreenVariable('text_now', None), SetScreenVariable('price_now', None), Function(show_text_animation, '-'+str(storein_shop_items_prices[_(i.name)])+' money')
                            else:
                                #hovered SetScreenVariable('text_now', i.discription), SetScreenVariable('price_now', '{color=#f00}' + str(storein_shop_items_prices[_(i.name)])+'${/color}')
                                hovered SetScreenVariable('text_now_0', i.discription), SetScreenVariable('text_now_1', i.name), SetScreenVariable('text_now_2', '{color=#f00}' + str(storein_shop_items_prices[_(i.name)]) + '${/color}') 
                                unhovered SetScreenVariable('text_now_0', None), SetScreenVariable('text_now_1', None), SetScreenVariable('text_now_2', None)
                                
                                action NullAction()

                        else:
                            idle '#000a'
                            hover '#000a'


                            action NullAction()

        if location_now != 'ClothesStore':

            for x in getattr(store, 'add_items_for_storein_shop_fixed', []):
                $ i = get_item_by_id(x)
                if i:
                    viewport:
                        xmaximum 136
                        ymaximum 138
                        add 'alpha_solid'
                        add i.image xpos 15 ypos 25


                        imagebutton xpos 15 ypos 25:
                            xmaximum 115
                            ymaximum 115
                            if get_item_by_id(x, True) == None:
                                idle 'alpha_solid'


                                hover '#000a'
                                at ButtonEffect01
                                unhovered SetScreenVariable('text_now', None), SetScreenVariable('price_now', None)

                                if money >= storein_shop_items_prices[_(i.name)]:
                                    #hovered SetScreenVariable('text_now', i.discription), SetScreenVariable('price_now', str(storein_shop_items_prices[_(i.name)]) + '$')
                                    
                                    hovered SetScreenVariable('text_now_0', i.discription), SetScreenVariable('text_now_1', i.name), SetScreenVariable('text_now_2', str(storein_shop_items_prices[_(i.name)]) + '$') 
                                    unhovered SetScreenVariable('text_now_0', None), SetScreenVariable('text_now_1', None), SetScreenVariable('text_now_2', None)
                                    action Function(renpy.play, 'audio/money.ogg'), Function(add_to_inventory, name = i.name), SetVariable('money', money - storein_shop_items_prices[_(i.name)]), SetScreenVariable('text_now', None), SetScreenVariable('price_now', None), Function(show_text_animation, '-'+str(storein_shop_items_prices[_(i.name)])+' money')
                                else:
                                    #hovered SetScreenVariable('text_now', i.discription), SetScreenVariable('price_now', '{color=#f00}' + str(storein_shop_items_prices[_(i.name)])+'${/color}')
                                    hovered SetScreenVariable('text_now_0', i.discription), SetScreenVariable('text_now_1', i.name), SetScreenVariable('text_now_2', '{color=#f00}' + str(storein_shop_items_prices[_(i.name)]) + '${/color}') 
                                    unhovered SetScreenVariable('text_now_0', None), SetScreenVariable('text_now_1', None), SetScreenVariable('text_now_2', None)
                                    
                                    action NullAction()

                            else:
                                idle '#000a'
                                hover '#000a'


                                action NullAction()

        for x in itms:#all_items: #storein_shop_items_prices:#
            $ i = get_item(x)
            #$ i = x
            $ price = storein_shop_items_prices.get(_(i.name), 9999)
            if i:
                viewport:
                    xmaximum 136
                    ymaximum 138
                    add 'alpha_solid'
                    add i.image xpos 15 ypos 25


                    imagebutton xpos 15 ypos 25:
                        xmaximum 115
                        ymaximum 115
                        if get_item(x, True) == None:
                            idle 'alpha_solid'


                            hover '#000a'
                            at ButtonEffect01
                            unhovered SetScreenVariable('text_now', None), SetScreenVariable('price_now', None)

                            if money >= price:
                                #hovered SetScreenVariable('text_now', i.discription), SetScreenVariable('price_now', str(storein_shop_items_prices[_(i.name)]) + '$')
                                hovered SetScreenVariable('text_now_0', i.discription), SetScreenVariable('text_now_1', i.name), SetScreenVariable('text_now_2', '$' + str(storein_shop_items_prices[_(i.name)])) 
                                unhovered SetScreenVariable('text_now_0', None), SetScreenVariable('text_now_1', None), SetScreenVariable('text_now_2', None)

                                action Function(renpy.play, 'audio/money.ogg'), Function(add_to_inventory, name = x), SetVariable('money', money - price), SetScreenVariable('text_now', None), SetScreenVariable('price_now', None), Function(show_text_animation, '-'+str(price)+' money')
                            else:
                                #hovered SetScreenVariable('text_now', i.discription), SetScreenVariable('price_now', '{color=#f00}' + str(storein_shop_items_prices[_(i.name)])+'${/color}')
                                hovered SetScreenVariable('text_now_0', i.discription), SetScreenVariable('text_now_1', i.name), SetScreenVariable('text_now_2', '{color=#f00}$' + str(price) + '{/color}') 
                                unhovered SetScreenVariable('text_now_0', None), SetScreenVariable('text_now_1', None), SetScreenVariable('text_now_2', None)
                                
                                action NullAction()

                        else:
                            idle '#000a'
                            hover '#000a'


                            action NullAction()

    # if text_now is not None:
    #     vbox xalign .5 yalign .76:
    #         for i in text_now:

    #             text _(str(i)) xalign .5
    #         if price_now is not None:


    #             text str(price_now) xalign .5

    use item_name_table(text_now_0, text_now_1, text_now_2)

screen item_name_table(text_0 = None, text_1=None, text_2=None):
    if preferences.language in (None, 'rus'):
        if text_0 is not None:
            vbox xalign .5 yalign .76:
                for i in range(len(text_0)):
                    viewport:
                        add '#0000'
                        xalign .5
                        xmaximum 1000
                        ymaximum 33
                        if i == len(text_0)-1:
                            text _dscr_kostil(str(__(text_0[i]))) xalign .5 size 27

                        else:
                            text str(__(text_0[i])) xalign .5 size 27

    if text_1 is not None:
        if text_2 is not None:
            $ _tmp_text = str(__(text_1)) + " " + str(__(text_2))
            
        else:
            $ _tmp_text = str(__(text_1))

        $ _len_tmp_text = len(str(_tmp_text).replace('{color=#f00}', '').replace('{/color}', ''))
        
        viewport:

            #xmaximum 541
            #xmaximum 720

            if _len_tmp_text > 25:
                xmaximum 720
            else:
                xmaximum 541
            ymaximum 97
            #image '#000a'
            xalign .5 yalign .95
            image 'text_info_bg_frame'
            
            text _tmp_text xalign .5 yalign .5 size max(10, 30-max(_len_tmp_text-44, 0)) color '#000'

    add 'interface/Panel_Money.png' xalign 1.0
    text '$' + str(store.money) xalign .9 color '#000' ypos 40


screen in_store_screen:
    imagebutton:
        idle 'images/locations/imagebuttons/StoreIn/misha_in_store.png'
        hover im.MatrixColor('images/locations/imagebuttons/StoreIn/misha_in_store.png', im.matrix.brightness(.3))
        focus_mask True
        at ButtonEffect01
        action Return()

    add 'back_button'
    imagebutton:

        idle 'back_button_hover'
        hover 'back_button_hover'
        focus_mask True
        at ButtonEffect01

        action Function(JumpToLocation, 'City_Shop')

    use icons_interface

label talk_with_store_woman_label:
    $ renpy.play('audio/Door.mp3')
    scene expression '#000' with Dissolve(.5)
label talk_with_store_woman_label_menu:
    call show_all_images_label from _call_show_all_images_label_90
    with Dissolve(.5)


    $ location_now = 'Store_Misha'
    $ check_ev     = check_events()



    $ location_now = 'StoreIn'
    call screen in_store_screen
label talk_with_store_woman_label_menu_2:
    menu:
        "Говорить." if check_ev:
            $ renpy.jump(check_ev.label)
        "Магазин." if True:
            call check_surv_label from _call_check_surv_label_4

            show expression '#000a'
            show expression 'interface/Inventory.png':
                xalign .5
                yalign .5
            show expression 'interface/Grid.png':
                xalign .5
                yalign .5

            with Dissolve(.5)

            $ storein_costumes_shop_items_fix_0_8_9_d = []
            if events.get('cat_root_3_0'):
                if 'Чёрные очки' not in storein_costumes_shop_items:
                    $ storein_costumes_shop_items_fix_0_8_9_d.append('Чёрные очки')

            # if events.get('christie_root_33'):
            #     if 'Костюм Харли Квин.' not in storein_costumes_shop_items:
            #         $ storein_costumes_shop_items_fix_0_8_9_d.append('Костюм Харли Квин.')

            python:
                store_events_items_fix_0_9      = []
                for evn in mishwanda_store_events_items:
                    if evn in events:
                        for i in mishwanda_store_events_items[evn]: 
                            store_events_items_fix_0_9.append(i) 
            if getattr(store, 'unlock_film_1', 0) or getattr(store, "unlock_film_lolita", 0):

                call screen storein_shop(storein_shop_items+storein_costumes_shop_items_fix_0_8_9_d+['Шоколад', 'Йогурт', 'Чипсы', 'Сок', 'Кикбоксёр', 'Фильм "Лолита"'], store_events_items_fix_0_9)   
            elif True:


                call screen storein_shop(storein_shop_items+storein_costumes_shop_items_fix_0_8_9_d+['Шоколад', 'Йогурт', 'Чипсы', 'Сок', 'Кикбоксёр'], store_events_items_fix_0_9)   
            hide expression '#000a'
            hide expression 'interface/Inventory.png'

            hide expression 'interface/Grid.png'

            with my_dissolve
            $ location_now = 'After_StoreIn'
            $ check_ev     = check_events()
            $ location_now = 'StoreIn'
            if check_ev:
                $ Jump(check_ev.label)()





            jump talk_with_store_woman_label_menu_2

        #"!Пошалить (WIP)" if getattr(store, 'misha_shalost', False):
        #    pass
        "Назад." if True:









            jump talk_with_store_woman_label_menu

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
