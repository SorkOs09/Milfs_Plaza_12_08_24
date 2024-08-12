label ep3_milf_29:



    play sound 'audio/zvonok.mp3'
    hide screen main_interface

    show expression 'cg/gg_activities/gg_clothes_restroom_nude.png'

    with Dissolve(.5)

    $ renpy.pause(9999)

    $ block_exit_home = False

    $ locations['Restroom'].buttons[0]['washer'] = ((0, 650, 453, 429), [Jump('restroom_washer_label')])

    $ Event('ep3_milf_30',     'City_Home')

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
