label milf_root_6:
    $ events.pop('milf_root_6', 0)
    show GG Normal
    show GG Normal at go_from_left
    "[gg]" "Марина, открой, это я."
    show GG Think
    "[gg]" "Слышишь?.."
    show GG Normal:
        xalign .15
    with my_dissolve
    "[gg]" "Это я, [gg]. "
    show GG Normal
    "[gg]" "Я пришёл вынуть из тебя анальную пробку."
    show GG Embarrassment
    "[gg]" "Марина?.."
    show GG Think
    "[gg]" "Хм, она или уснула, или её нет."
    show GG Think
    "[gg]" "Придётся взламывать замок."



    $ lockergame = LockerGame(lvl = 1, image_now = 'images/mini_games/lock_mini_game/locker.png')
    play music 'audio/mini_game.mp3' fadein 1.5
    call screen LockerGameScreen
    $ unlock_milf_room = True

    $ Hide('main_interface')()
    play music 'audio/night.mp3' fadein 1.5
    play sound 'audio/lock.ogg'
    scene black with Dissolve(.5)
    $ time.time_now = 'evening'
    call show_bg_image_label from _call_show_bg_image_label_114
    call show_additional_images_label from _call_show_additional_images_label_94
    with Dissolve(.5)
    show GG Surprise
    show GG Surprise at go_from_left

    "[gg]" "Действительно нет."
    show GG Surprise:
        xalign .15
    with my_dissolve
    "[gg]" "Ну и куда она запропостилась?"
    show GG Think
    "[gg]" "Нужно написать ей СМС."


    $ milf_root_1_text = _("Отправить Марине СМС.")
    $ new_events = True

    $ ep2_milf_room_unlock = False
    $ location_now  = 'Hall'
    $ time.time_now = 'night'
    scene black with Dissolve(.5)

    jump milf_root_7
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
