
init 999 python:
    renpy.config.rollback_enabled = True
    renpy.config.hard_rollback_limit = 256
    renpy.config.rollback_length = 256
    def unren_noblock( *args, **kwargs ):
        return
    renpy.block_rollback = unren_noblock
    try:
        config.keymap['rollback'] = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK', 'mousedown_4' ]
    except:
        pass

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
