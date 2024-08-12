
label christie_root_24b:



    $ Hide('lock_pick_screen', transition = Dissolve(.5))()

    $ renpy.music.stop(fadeout=1.5)

    $ lockergame = LockerGame(lvl = 1, image_now = 'images/mini_games/lock_mini_game/locker.png')

    play music 'audio/mini_game.mp3' fadein 1.5

    call screen LockerGameScreen

    $ Hide('main_interface')()

    play sound 'audio/lock.ogg'

    $ renpy.pause(.5, hard = True)

    scene black with Dissolve(1)

    $ location_now = "Sister_Room"

    call show_all_images_label from _call_show_all_images_label_100

    with Dissolve(1)

    $ renpy.pause(.5, hard = True)

    show GG Think

    show GG Think at go_from_right




    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    "[gg]" "Бороться со своим прошлым «я» не так-то просто…"

    "[gg]" "Теперь я снова чувствую себя преступником, нарушающего покой другого человека."
    show GG:
        xalign .85
    with my_dissolve
    "[gg]" "Но я же не собираюсь никому причинить вреда, верно?"

    "[gg]" "Я руководствуюсь исключительно любопытством, и не более."

    "[gg]" "Разве можно за это меня корить?"

    "[gg]" "Стоило бы спросить об этом саму Кристи, наверное."

    "[gg]" "Она бы точно сказала, что я не прав…"

    "[gg]" "Но… Речь ведь идёт о ней, а значит, она ангажирована в данном вопросе. "

    "[gg]" "Лучше спрошу об этом Сьюзен, когда буду у неё на приёме. "

    show GG Think:
        linear 1 xalign 1.3

    $ location_now = "Corridor"
    $ events.pop('christie_root_24b', 0)

    $ events.pop('christie_root_23_block', 0)
    $ descript_Christie_tmp_1 = ''
    if not len(getattr(store, 'descript_Christie_tmp_0', '')):
        $ descript_Christie = _("Дождаться завтра и отдать Кристи реферат по «Обществознанию».")

        $ Event('christie_root_25', 'GG_Room', time = ['morning',], button_name = _("Реферат"), priority = -1)
    $ debug_exit()

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
