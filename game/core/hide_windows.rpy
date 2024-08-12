
label hide_windows:

    if renpy.context()._menu:
        return

    if _windows_hidden:
        return

    $ _master_comic = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
    if _master_comic:
        show image comic_frame_v2_master:
            alpha 0.0

    $ _master_comic = renpy.display.core.displayable_by_tag("master", "comic_frame_v3_master")
    if _master_comic:
        show image comic_frame_v3_master:
            alpha 0.0
   
    $ _master_comic = None
    #"[gg]" "!"
    #show image '#fff'
    return
