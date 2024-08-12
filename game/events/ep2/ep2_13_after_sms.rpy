


image fap_time_anim:
    'images/cg/ep2/fap_time_ep2/fap_time_1.png' with Dissolve(.5)
    .5
    'images/cg/ep2/fap_time_ep2/fap_time_2.png' with Dissolve(.5)
    .5
    repeat

image fap_time_milf_anim:
    'images/cg/ep2/fap_time_ep2/fap_time_milf_1.png' with Dissolve(.5)
    .5
    'images/cg/ep2/fap_time_ep2/fap_time_milf_2.png' with Dissolve(.5)
    .5
    repeat
label ep2_13_after_sms:

    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    show GG Think
    show GG Think:
        xalign .5
        ypos 1085
        zoom 1.0-0.035
    with my_dissolve
    '[gg]' "Последнее время моя жизнь весит на волоске. И вряд ли пистолет, что я получу, как-то поспособствует улучшению моей ситуации. Скорее наоборот."
    '[gg]' "Но чёрт меня дери, мне совершенно плевать на это! Моя голова забита исключительно Мариной?!"
    '[gg]' "Её мокрые трусики, что она забыла на ночнике, не дают мне покоя."
    '[gg]' "Я снова хочу их понюхать… Снова ощутить их прикосновение у своего лица."


    $ descript = _('Нужно проникнуть в ванну, когда там будет Марина, и украсть её трусики. ')





    $ block_change_milf_position = True
    $ milf_position['morning']   = ['Restroom',  'milf_restroom']
    $ milf_position['morning']   = ['Restroom',  'milf_restroom']
    if sister_position['morning'] == ['Restroom',  'sister_restroom']:
        $ sister_position['morning']    = ['Hall', 'sister_hall']

    $ Event('ep2_14_milf_restroom',  'Restroom', time = ['morning'])

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
