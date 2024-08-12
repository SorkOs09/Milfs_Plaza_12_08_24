label ep3_3_after_phone:
    
    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()






    $ descript = _('Поговорить с Игорем в парке')


    $ Event('ep3_4_talk_with_igor_in_park', 'Igor')


    $ Event('night_girl', 'GG_Room', 'pre_ep3_night_girl', day_start = time.day_now+2, time = ['morning'])


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
