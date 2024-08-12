

label christie_root_19:
    if get_item("Реферат", True):
        $ events.pop("christie_root_19", 0)









        call show_all_images_label from _call_show_all_images_label_97
        show GG Think
        show GG Think:
            xalign .5
        with Dissolve(.5)

        "[gg]" "Вот и всё. Теперь надо поговорить с Кристи и вручить ей реферат."

        $ Event('christie_root_20', 'Christie', button_name = "Отдать реферат")
        $ descript_Christie= _("Отдать Кристи реферат.")



    $ location_now = "GG_Room"
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
