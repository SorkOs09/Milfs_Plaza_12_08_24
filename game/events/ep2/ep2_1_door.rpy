label ep2_1_door:



    show GG Think
    show GG Think:
        xalign .1


    with Dissolve(.5)

    '[gg]' "Хм… Дверь заперта, и ключей нигде нет."
    '[gg]' "Нужно спросить об этом Марину."

    $ descript = _("Спросить Марину про запертую дверь.")

    $ Event('ep2_2_blin', 'Kitchen_Milf')

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
