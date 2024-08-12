label ep3_milf_33:
    $ events.pop('ep3_milf_33', 0)

    $ events.pop('ep3_milf_30_stump', 0)

    $ location_now = 'Hall'
    hide screen main_interface

    call show_all_images_label from _call_show_all_images_label_49
    with Dissolve(.5)





    show Igor Spec_Normal_1
    show Igor Spec_Normal_1:

        ypos 1085



        xalign .85




    show GG Normal
    show GG Normal:
        xalign .15
        ypos 1085


    with Dissolve(.5)




















    "[gg]" "Игорь! "
    "Игорь" "Опять ты…"
    "Игорь" "По крайней мере в штанах. "
    "[gg]" "Кончай трепаться. Я не могу сдерживать её бесконечно. "
    "Игорь" "Чувак, ещё пять минут."
    "[gg]" "…."
    "[gg]" "Окей."



    call show_all_images_label from _call_show_all_images_label_50
    show GG Normal
    show GG Normal:
        xalign .15
        ypos 1085
        zoom 1.0

    show Igor Spec_Normal_1
    show Igor Spec_Normal_1:
        ypos 1085

        xalign .85


    with Dissolve(.1)
    show Igor Spec_Normal_1:

        ypos 1085 xzoom -1



        linear .8 xalign 1.7



    $ renpy.pause(.8, hard = True)



    hide Igor

    show GG Think:
        xalign .5


    with my_dissolve


    "[gg]" "Полагаю, Марина уже помылась. Нужно искать её на кухне."

    $ descript = _("Полагаю, Марина уже помылась. Нужно искать её на кухне.")



    $ Event('ep3_milf_28',     'Milf_Room')

    $ Event('ep3_milf_34',     'Kitchen')


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
