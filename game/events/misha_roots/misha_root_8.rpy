label misha_root_7_5:

    $ events.pop('misha_root_7_5', 0)






    $ renpy.pause(.5, hard   = True)
    $ sms_now = SmsBlock('Мишванда', 'misha', "24", Jump('misha_root_8'))
   
    $ sms_now.add_sms(_("GG: Дай мне ещё один шанс!\n"))
    $ sms_now.add_sms(_("TT: Зайди ко мне завтра.\n"))
    $ sms_now.add_sms(_("GG: Имеешь в виду провести тебя?\n"))
    $ sms_now.add_sms(_("TT: Нет. На работу ко мне зайди.\n"))
    $ sms_now.add_sms(_("GG: Хорошо.\n"))

    
    jump main_interface_label





label misha_root_8:



    $ Event('misha_root_9', 'Store_Misha', day_start = time.day_now+1, priority = -10)



    $ descript_Misha     = _("Повидаться с Мишвандой в магазине.")

    $ events.pop('misha_root_7_5', False)
    $ events.pop('misha_root_7_75', False)
    $ events.pop('misha_root_8', False)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
