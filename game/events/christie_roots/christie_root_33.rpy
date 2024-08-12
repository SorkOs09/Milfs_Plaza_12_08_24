
label christie_root_33:
    if get_item('Костюм Харли Квин.', True, True):
        $ events.pop('christie_root_33', 0)
        $ storein_costumes_shop_items.remove('Костюм Харли Квин.')






        show GG Think
        show GG Think:
            xalign .5
        with my_dissolve

        "[gg]" "Готово!"
        #show GG Think
        "[gg]" "Вернусь обрадую Кристи."
        $ descript_Christie= _("Если я ГОТОВ выдвинуться на слежку за офицером - отдать Кристи её костюм Харли Квин.")

        $ Event('christie_root_34', 'Christie', time = ["morning", "afternoon"])

    $ renpy.play('audio/Door.mp3')
    scene black with Dissolve(.5)

    $ location_now = 'City_Home'
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
