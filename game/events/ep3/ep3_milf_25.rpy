label ep3_milf_25:

    $ events.pop('ep3_milf_24', 0)

    $ events.pop('ep3_milf_25', 0)

    call show_bg_image_label from _call_show_bg_image_label_66
    call show_additional_images_label from _call_show_additional_images_label_60
    hide screen main_interface

    with Dissolve(.5)




    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085



    show Milf Street_Normal
    show Milf Street_Normal:
        ypos 1085

        xalign .65

    show Christie Street
    show Christie Street:
        xalign .5
        ypos 1085

        xalign .95
    with Dissolve(.5)















    "Марина" "[gg], ты решил пойти с нами?"
    show GG Normal
    "[gg]" "К сожалению."
    show GG Smile
    "[gg]" "Просто хотел пожелать вам удачи."
    show Christie Street
    "Кристи" "Удачи, дружок!"

    show Milf Street_Normal
    "Марина" "Нам будет тебя не хватать, [gg]. "
    "[gg]" "Постараюсь не грустить."



    hide Milf
    hide Christie
    with Dissolve(.5)
    $ renpy.pause(.2, hard = True)
    show GG Think:
        xalign .5
    with Dissolve(.5)


    "[gg]" "Готово. Теперь нужно отправить смс Игорю и пригласить его на задание. "
    $ descript = _("Написать СМС Игорю.")
    $ block_exit_home    = True
    $ block_milf_home    = True
    $ block_sister_home  = True
    $ block_time_forward = True
    $ ShowPhone = Show('phone_interface')


    $ sms_now = SmsBlock('Игорь', 'igor', "12", Jump('ep3_milf_26'))
    $ sms_now.add_sms(_('GG: Сектор очищен. \nВечером жду у себя.'))
    $ sms_now.add_sms(_('TT: Понял-принял.'))
            
    $ phone_warning = True


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
