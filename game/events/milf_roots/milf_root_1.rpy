label milf_root_1_setup:
    $ Event('milf_root_1', button_name = _("Подарить анальную пробку"), location = 'milf')
    $ Event('cat_root_1', 'GG_Room', time = ['night'])
    if not hasattr(store, 'add_items_for_web_shop'):
        $ add_items_for_web_shop = []
    $ milf_root_1_text = _('Купить Марине анальную пробку в интернет-магазине и подарить ей.')
    $ new_events       = True
    $ add_items_for_web_shop.append(('Анальная пробка', 100))
    $ block_change_milf_position   = False


    return

label milf_root_1:
    if not get_item('Анальная пробка', True):
        "[gg]" "Сначала мне нужно купить анальную пробку."
        jump main_interface_label
    $ block_change_milf_position   = False
    $ events.pop('milf_root_1', 0)
    call show_bg_image_label from _call_show_bg_image_label_104
    call show_additional_images_label from _call_show_additional_images_label_89

    show Milf Normal
    show Milf Normal:
        xalign .85
        ypos 1085
    with Dissolve(.5)
    show GG Embarrassment
    show GG Embarrassment at go_from_left

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Последнее время я мало уделял тебе времени и, как мне кажется, это пора исправить."
    show Milf Chagrin
    show GG:
        xalign .15
    "Марина" "А я уже начала думать, что ты просто забыл про моё существование…"
    show GG Embarrassment
    "[gg]" "Не говори так! "
    show GG Embarrassment
    "[gg]" "Ты навсегда в моём сердце, Марина. Никто и никогда не сможет сравниться с тобой. "
    show Milf Embarrassment
    "Марина" "Всего-лишь слова."
    show GG Smile
    "[gg]" "Вот поэтому, чтобы доказать тебе мою искренность, я решил сделать тебе интересный подарок."
    show Milf Surprise
    with my_vpunch
    "Марина" "Подарок? Мне?"
    show GG Laughs
    "[gg]" "Ага."
    show GG Laughs
    "[gg]" "Вот, держи. "
    show Milf Embarrassment
    "Марина" "Ух ты… Что это за штучка?"
    show GG Chagrin
    "[gg]" "Анальная пробка. "
    show Milf Passion
    "Марина" "Вау…"
    show Milf Passion
    "Марина" "Я воодушевлена и готова к новым экспериментам, [gg]."
    show GG Chagrin
    "[gg]" "Я жутко рад, что тебе понравилось."
    show Milf Passion
    "Марина" "Мне нравится всё, что ты делаешь для меня."
    show GG Embarrassment
    "[gg]" "Значит ты…"
    show Milf Passion
    "Марина" "Ага. Сколько прикажешь носить её, любименький?"
    show GG Embarrassment
    "[gg]" "Ну… "
    show GG Embarrassment
    "[gg]" "Могу я сказать об этом ровно тогда, когда нужно будет её вытащить?"
    show Milf Passion
    "Марина" "Хи-хи-хи!"
    show Milf Passion
    "Марина" "Хорошо. Я принимаю правила игры."
    show Milf Passion
    "Марина" "Но не мучай меня слишком долго…."
    show Milf Embarrassment
    "Марина" "Боюсь, что не смогу удержаться, чтобы не наброситься на тебя самой. "
    show GG Passion
    "[gg]" "Нет, так не пойдёт. "
    show GG Passion
    "[gg]" "Если ты сорвёшься, не жди от меня ласок."
    show Milf Embarrassment
    "Марина" "Оооо, ты жесток…"
    show Milf Embarrassment
    "Марина" "Оооо, ты жесток…"
    show Milf Passion
    "Марина" "Ведь я уже тебя хочу, и неизвестно, как скоро ты соблаговолишь пошалить со мной…"
    show GG Passion
    "[gg]" "Скоро."
    show GG Passion
    "[gg]" "А пока что будь хорошей девочкой, засунь себе эту штучку и жди моей команды."
    show Milf Embarrassment
    "Марина" "Хорошо, любименький."

    show Milf Embarrassment:
        xzoom -1
    with Dissolve(.2)
    show Milf Embarrassment:
        xzoom -1
        linear 1 xalign 1.5

    $ renpy.pause(1)
    $ stnd_music_play()
    hide Milf
    show GG Think
    with my_dissolve

    "[gg]" "Мне следует прождать какое-то время, доведя Марину до экстаза. "
    #show GG Think
    "[gg]" "Чтобы она не сдалась раньше времени, и для скорейшей стимуляции я буду реже появляться ей на глаза."
    #show GG Think
    "[gg]" "Моё отсутствие будет сводить её с ума, а её жажда секса выйдет на новый уровень раскрепощения. "

    $ remove_from_inventory('Анальная пробка')
    $ Event('milf_root_2', 'City_Home', time = ['evening', 'night'])
    $ block_milf_events = 'milf_root_2_tmp'
    $ new_events        = True
    $ milf_root_1_text  = _("Прождать какое-то время, доведя Марину до экстаза. Чтобы ускорить стимуляцию, мне стоит избегать Марину, и возвращаться домой поздно ночью.")
    $ add_items_for_web_shop = []
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
