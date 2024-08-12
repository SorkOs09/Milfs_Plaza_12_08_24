label christie_root_49:
    #Description: Вывести из строя кондиционер Ночью, пока никто не видит.

    $ events.pop('christie_root_48', 0)
    $ events.pop('christie_root_49', 0)
    #//GG_Condicer_Work_1
    $ add_items_for_storein_shop_fixed.remove(screw_at_shop)
    $ del screw_at_shop
    $ remove_from_inventory_by_id(33)
label christie_root_49_1:
    call show_bg_image_label from _call_show_bg_image_label_179
    show image 'cg/ep89/gg_cond.png'
    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    #Активировать кондиционер в зале.

    "[gg]" "Я нихрена не понимаю в кондиционерах…"
    "[gg]" "Вот здесь вроде бы какой-то проводок."
    "[gg]" "И вот тут какая-то хрень непонятная."
    "[gg]" "Кажется я копаю в правильном напра…"
    #//GG_Condicer_Work_1

    "" "Взззз-ззззз-зззззз-ззззз!!!"
    "[gg]" "ЭЭээээЭЭээээЭЭ—ээЭЭээ—Эээ."
    #//GG_Condicer_Work_3
    if not renpy.call_screen('qte_mini_game', ttimer = 20, qte_line = 'luulldlulr', shake = True):

        scene black
        with my_vpunch
        "" "Вас ударило током и вы погибли."
        "" "Попробовать снова?"
        if not hasattr(store, "christie_root_49_1_try"):
            $ christie_root_49_1_try = 0
        menu:
            "Да":
                
                $ christie_root_49_1_try += 1
                jump christie_root_49_1
            "Нет":
                $ renpy.full_restart()
                jump christie_root_49_1

            "Пропуск" if christie_root_49_1_try > 5:
                pass

    python:
        try:
            del christie_root_49_1_try
        except:
            pass

    "[gg]" "Твою мать, вроде бы отпустило."
    "[gg]" "Цель достигнута - кондиционер не пашет."
    
    
    #Tian_50

    $ descript_Christie = _("Установить мобильный телефон возле телевизора в Зале Ночью, пока никто не видит.")
    jump christie_root_50