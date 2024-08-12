label tyan_falos_0:

#Tian_Falos_1

    $ tyan_falos_text = _("Ночные услады Кристи с фалосом не дают мне покоя. Было бы замечательно заменить её секс-игрушку на свой член, но как это сделать? Для начала нужно купить резак для стены, чтобы вырезать отверстие в месте куда Кристи клеит фалос. ")
#A task:
    $ new_events_christie = True
    #1. Купить Резак (150 баксов).
    $ rezak_at_web_shop = 11
    if not hasattr(store, 'add_items_for_storein_shop_fixed'):
        $ add_items_for_storein_shop_fixed = []
    $ add_items_for_storein_shop_fixed.append(rezak_at_web_shop)
    $ Event('tyan_falos_1', location = 'City_Shop', need_items = [11,])
    
    return

label tyan_falos_1:

    show black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    




    $ events.pop('tyan_falos_1', 0)

    $ add_items_for_storein_shop_fixed.remove(rezak_at_web_shop)
    $ del rezak_at_web_shop

    hide black
    call show_bg_image_label from _call_show_bg_image_label_165 
    show GG Think
    with my_dissolve 
    show GG Think
    "[gg]" "Уххх… Вот это агрегат!"
    show GG Think
    "[gg]" "Надеюсь, я не отхреначу себе палец или… Короче, надо быть осторожнее! "
    show GG Think
    "[gg]" "Прежде чем резать, мне нужно измерить расстояние, на котором располагается резиновый фалос Кристи."
    show GG Think
    "[gg]" "Конечно, лучше это делать, пока Кристи нет в комнате, но для этого мне нужна линейка."
    show GG Think
    "[gg]" "Где её взять? Купить? Нет, снова тратить деньги."
    show GG Think
    "[gg]" "Хм… Я могу попросить линейку у Кристи! Почему бы и нет, отличная идея!"


    $ tyan_falos_text = _("Попросить у Кристи линейку.")

    $ debug_next('tyan_falos_2_debug')
    
    $ Event('tyan_falos_2', 'Christie', button_name = _("Линейка"))
    jump main_interface_label