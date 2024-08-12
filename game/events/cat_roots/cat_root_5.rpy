

image cat_root_minet:
    'cg/cat_root/minet/k2.png' with Dissolve(.15)
    1.2
    'cg/cat_root/minet/k3.png' with Dissolve(.15)
    1.2
    repeat


image cat_root_minet_2:
    'cg/cat_root/minet/k2a.png' with Dissolve(.15)
    1.2
    'cg/cat_root/minet/k3a.png' with Dissolve(.15)
    1.2
    repeat


image cat_root_minet_3:
    'cg/cat_root/minet/k2a.png' with Dissolve(.15)
    1
    'cg/cat_root/minet/k3a.png' with Dissolve(.15)
    1
    repeat


image cat_root_minet_4:
    'cg/cat_root/minet/k2a.png' with Dissolve(.15)
    .7
    'cg/cat_root/minet/k3a.png' with Dissolve(.15)
    .7
    repeat


label cat_root_5_0:
    $ location_now = 'GG_Room'
    "[gg]" "Я хотел \"Пошалить\" с кэт."
    jump main_interface_label



label cat_root_5:
    $ time.time_now = 'evening'
    $ location_now  = 'GG_Room'
    call show_bg_image_label from _call_show_bg_image_label_163
    show image 'locations/imagebuttons/GG_Room/kat_on_bed_2.png'
    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)

    if not getattr(store, 'kat_shalost', False):
        $ events.pop('cat_root_5_0', 0)

        $ events.pop('cat_root_5', 0)

        show GG Normal
        show GG Normal at go_from_left(xxalign = .07)

        show GG Think
        "[gg]" "Всю ночь я думал о том, как мы проведём утро, и вот, она вернулась с работы и попросту уснула."
        show GG Think
        "[gg]" "Значит, мы не повеселимся, как она того хотела…"
        show GG Think
        "[gg]" "Чёрт."
        show GG Think
        "[gg]" "Она спит в такой… неестественной позе."
        show GG Think
        "[gg]" "Её вид словно приглашает меня на маленький сексуальный пикничок, а мой заведённый член выступает главным десертом."




        $ renpy.music.stop(fadeout=1.5)
        $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

        hide GG
        show gg_gipno_jerk
        show gg_gipno_jerk:
            xalign .1
            ypos 1085
            zoom 1.0-0.035
        with Dissolve(.5)
        $ renpy.pause(999)
        "[gg]" "Она ведь сама меня пригласила вчера."
        show GG Dick
        "[gg]" "Было бы странно отказываться от столь чудесного предложения…"
        show GG Dick
        "[gg]" "Наверное."
    elif True:


        $ renpy.music.stop(fadeout=1.5)
        $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.5)
    scene expression 'cg/cat_root/minet/k1.png'
    with Dissolve(.5)
    "[gg]" "Как же она вульгарна в этой вызывающей позе. "
    "[gg]" "Каким-то странным образом она совмещает в себе невинность уснувшей Белоснежки и пошлость дерзкой бандитки."
    "[gg]" "Ох… Я с трудом сдерживаюсь, чтобы не кончил прямо сейчас."
    "[gg]" "Как же её манящий ротик заводит меня."
    "[gg]" "Нужно быть осторожным и нежным."
    "[gg]" "Я же не хочу, чтобы мне откусили член."

    scene expression 'cg/cat_root/minet/k2.png'
    with my_dissolve
    "[gg]" "Аххх, я вошёл."
    "Кэт" "Мгл?!!"
    "[gg]" "Не бойся, Кэт, это всего лишь я."
    "[gg]" "Точнее, мой член, который всю ночь не давал мне уснуть и третировал меня ожиданием тебя."
    "[gg]" "Но ты так не вовремя уснула…"

    scene cat_root_minet
    with my_dissolve
    "Кэт" "Мгл!!!…"
    "[gg]" "О дааа, твой ротик ни чуть ни хуже твоей вагины."
    "[gg]" "Он горячий и мокрый, а твой нежный язычок сладко трётся об кожу моего члена."
    "[gg]" "Это потрясающее чувство, Кэт."
    "[gg]" "Тебе ведь тоже, нравится, да?"
    "Кэт" "Мгл!!!… Мгл!!!… Мгл!!!… Мгл!!!…"
    "[gg]" "Полагаю, что так. "
    "[gg]" "Ведь тебе ничего не мешает сомкнуть челюсти, хе-хе. Или оттолкнуть руками."

    scene cat_root_minet_2
    with my_dissolve
    "Кэт" "Ммммм…."
    "Кэт" "Омном-ном-ном!..."
    "[gg]" "Охххх, я чувствую как ты стала плотнее меня сжимать, это блаженное чувство от наслаждения."
    "[gg]" "Твои мягкие губки взмокли, будто бы ты облизываешь вкусное, но горячее мороженное. "
    "[gg]" "Я чувствую, как как мой член касается твоего горла. "
    "[gg]" "Надеюсь, тебе хорошо так же как и мне, потому что я едва ли сейчас смогу остановиться."


label cat_root_minet_menu:

    menu:
        "Ускориться" if True:
            scene cat_root_minet_3
            with Dissolve(.5)
        "Продолжить в том же темпе" if True:
            $ pass
            window hide
            $ renpy.pause(9999)
            jump cat_root_minet_menu


    "[gg]" "Ахх… Дааа. Я завёлся ещё сильнее."
    "[gg]" "Твой шаловливый ротик творит настоящие чудеса."
    "[gg]" "Ускорившись, я многократно ускорил остроту ощущений, ну а ты, разумеется, делаешь этот миг фантастически прекрасным."
    "[gg]" "Если позволишь, я хочу трахать тебя чуть более жостче. "
    "Кэт" "Мгл!... Мммм…. Мном-мном…"
    "[gg]" "Хех…"
    "[gg]" "Пожалуй, я истолкую это как «да, выеби меня как можно сильнее!»"


label cat_root_minet_menu_2:

    menu:
        "Ускориться" if True:
            scene cat_root_minet_4
            with Dissolve(.5)
        "Продолжить в том же темпе" if True:
            $ pass
            window hide
            $ renpy.pause(9999)
            jump cat_root_minet_menu_2



    "Кэт" "Мгл!!!"
    "Кэт" "Облм… млном-млном!!.."
    "[gg]" "Да-да, я чувствую ровно тоже самое, детка."
    "[gg]" "Ещё мгновение, и я кончу тебе в самую глотку."
    "[gg]" "Ага, я чувствую как ты дрожишь от нетерпения…"
    "[gg]" "Твоё сонливое тело уже изрядно вспотело, а мурашки по коже говорят сам за себя. "
    "Кэт" "Мглм! Мглм! Мглм! Мглм! Мглм!"
    "[gg]" "О даа, ещё-ещё!!!"
    "[gg]" "Не могу передать словами, какую бурю эмоций я испытывая сейчас, но количество спермы, что зальёт твой рот, расскажет об этом наглядно."
    "[gg]" " Я чувствую, как приближается кульминация…"
    "[gg]" " В глазах искры от торжественного предвкушения финала!"
    "[gg]" "Ещё-ещё-ещё!!! Почти…."
    "Кэт" "Мглм! Мглм! Мглм!"
    "[gg]" "Кончааааааааааюююююю!!!"
    menu:
        "Кончить" if True:
            $ pass

    scene expression '#fff'
    with Dissolve(.5)

    $ renpy.pause(.5)
    scene expression 'cg/cat_root/minet/k4.png'
    with Dissolve(.5)
    "Кэт" "Буль-буль-буль-буль…"
    "Кэт" "Мгл…."
    "[gg]" "Ошалеееееть."
    "[gg]" "Ты просто супер."


    $ location_now = 'GG_Room'
    if getattr(store, 'kat_shalost', False):
        scene expression '#000' with Dissolve(.5)

        $ time.time_forward()
        jump main_interface_label
    
    call show_bg_image_label from _call_show_bg_image_label_105
    show Kat Normal
    show Kat Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Normal
    show GG Normal:
        xalign .1
        ypos 1085
    with Dissolve(.5)






    show Kat Skepticism
    "Кэт" "Что это было, [gg]?"
    show GG Embarrassment
    "[gg]" "Я… Не сдержался, извини. Ты так вызывающе спала."
    show Kat Skepticism
    "Кэт" "Что значит «вызывающе»? Я просто СПАЛА!"
    show GG Chagrin
    $ renpy.block_rollback()
    "[gg]" "Да, мною овладела неконтролируемое влечение…"
    show Kat Surprise
    "Кэт" "Я заметила."
    show Kat Surprise
    "Кэт" "Но знаешь, мне понравилось."
    show GG Surprise
    "[gg]" "О… Значит ты не хочешь меня убить?!"

    "Кэт" "Не притворяйся, дурачок, ты же сам прекрасно видел, что я получила не меньшее удовольствие от процесса."
    show GG Passion
    "[gg]" "Ещё как. Но я до последнего боялся, что это похоть затуманила мне голову."
    show Kat Surprise
    "Кэт" "Если хочешь, можешь каждое утро меня так будить. "
    show GG Laughs
    "[gg]" "Буду рад услужить, спасибо."
    show Kat Smile
    "Кэт" "Сексуальный будильник. "
    show GG Smile
    "[gg]" "Ага."

    $ kat_shalost   = True
    $ descript_Cat  = _("Конец рута Кэт для эпизода 6")

    if not from_gallery_check():

        $ add_to_gallery(20)

    $ time.time_forward()

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
