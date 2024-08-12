label christie_root_29:






    $ time.time_now   = 'night'

    call show_all_images_label from _call_show_all_images_label_3

    with my_dissolve
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/full-moon-lofi-vibes-by-edikey20-from-filmmusic-io.mp3', fadein = 1.5)
    "Кристи" "Охххх!!!..."
    "Кристи" "Аааххааааххх!"
    "Кристи" "ООоооооо!!!!"
    "Кристи" "Ууууухх!!!"

    show GG Surprise
    show GG Surprise at go_from_right(xxzoom = -1)
    "[gg]" "Кристи снова взялась за старое…"
    show GG Think:
        xalign .85
    with my_dissolve
    "[gg]" "Что вообще она там такое делает, что аж стена трясётся?"
    #show GG Think
    "[gg]" "И судя по крикам, она не в состоянии утолить свою жажду…"
   # show GG Think
    "[gg]" "Что ж, пришло время узнать правду."

    if not hasattr(store, 'allowed_events'):
        $ allowed_events = []
    $ allowed_events.append("christie_root_30")
    
    $ block_exit_home_tmp = copy.deepcopy(block_exit_home)
    $ block_exit_home     = True
    $ block_milf_home_tmp = copy.deepcopy(block_milf_home)
    $ block_milf_home     = True



    $ block_time_forward_tmp = copy.deepcopy(block_time_forward)
    $ block_time_forward     = True

    $ descript_Christie= _("Открыть дверь Кристи.")
    $ Event('christie_root_30', 'Sister_Room')

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
