label milf_root_10:
    show black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    $ events.pop('milf_root_10', 0)





    $ add_items_for_storein_shop_fixed.remove(perec_at_web_shop)
    $ del perec_at_web_shop

    hide black
    call show_bg_image_label from _call_show_bg_image_label_162
    show GG Think
    with my_dissolve
    "[gg]" "Теперь Марина будет в относительной безопасности. "
    $ Event('milf_root_11', button_name = _("Подарить перцовый баллончик"), location = 'milf', need_items = [10,])




    $ milf_root_9_text= _("Отдать перцовый баллончик Марине.")
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
