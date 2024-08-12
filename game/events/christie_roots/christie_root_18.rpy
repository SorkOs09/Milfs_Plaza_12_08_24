image christie_root_18_gg_listening = 'cg/christie_root/gg_listening.png'

label christie_root_18:

    $ events.pop('christie_root_18', 0)

    call show_bg_image_label from _call_show_bg_image_label_129








    "Какие-то звуки" "Ахххх!!..."
    "Какие-то звуки" "Оххх!!!...."
    "Какие-то звуки" "Уххх Уххх…. Ммммм!!"
    "Какие-то звуки" "Оооооххххх…!!!"

    show GG Surprise
    show GG Surprise at go_from_right(xxzoom = -1)

    "[gg]" "А?"
    "[gg]" "Кому-то плохо?"
    show GG Surprise:
        xalign .85
        xzoom -1.0
    with my_dissolve
    "[gg]" "Вздохи доносятся из комнаты Кристи."
    show GG Surprise:
        ease .8 xalign .2 alpha .0
    show christie_root_18_gg_listening:
        alpha .0
        ease 1.5 xalign .5 alpha 1.0







    "[gg]" "О нет, ей не плохо. "
    "[gg]" "Очень даже наоборот."

    "[gg]" "Она так страстно мастурбирует, что я едва сдерживаюсь, чтобы не вломиться к ней в комнату."
    "[gg]" "Проклятье, я хочу это видеть!"
    show christie_root_18_gg_listening:
        xalign .5 alpha 1.0
    "[gg]" "Но как? "
    "[gg]" "Игорь вставил новый замок, который я не могу взломать."
    "[gg]" "Сегодня я точно ничего не смогу сделать, надо придумать план на следующий раз. "



    $ check_var_christie_root_18 = True




    scene black with Dissolve(.5)


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
