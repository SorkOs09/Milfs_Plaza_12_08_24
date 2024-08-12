label check_surv_label:
    if getattr(store, 'block_time_forward', False):
        return

    if gigiena < 15:
        "[gg]" "От меня воняет, как от козла, и не хочу сейчас ни с кем контактировать."
        jump main_interface_label
    if nastroi < 15:
        "[gg]" "Я в плохом настроении и не хочу сейчас ни с кем контактировать."
        jump main_interface_label
    if sitost < 15:
        "[gg]" "Я практически обессилен и не хочу сейчас ни с кем контактировать."
        jump main_interface_label

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
