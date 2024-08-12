image christie_root_20_gg_touch_ass = 'cg/christie_root/gg_touch_ass.png'
label christie_root_20:
    $ events.pop('christie_root_20', 0)








    call show_bg_image_label from _call_show_all_images_label_101

    show Christie Normal
    show Christie Normal:
        xzoom -1
        xalign .12
        ypos 1085

    with Dissolve(.5)

    show GG Passion
    show GG Passion at go_from_right(xxzoom=-1)


    "[gg]" "Профессионал в деле. "
    show Christie Surprise
    "Кристи" "А?"
    show GG Normal:
        xalign .85
        xzoom -1.0
    with my_dissolve
    "[gg]" "Ну как же, ты просила реферат по «Обществознанию», и вот, пожалуйста, горяченький, только-только из печати."
    show Christie Surprise
    "Кристи" "Чтооооооооооо?!!"
    show Christie Surprise
    "Кристи" "Так скоро?!"
    show GG Smile
    "[gg]" "Ну дык, ёмаё!"

    show Christie:
        easein 1.0 xalign .5
    $ renpy.pause(1.4, hard = True)
    show black with vpunch
    $ renpy.pause(.75, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_130
    show christie_root_20_gg_touch_ass:
        xpos 100
    with my_dissolve





    "Кристи" "Спасибо тебе, [gg], ты замечательный друг!"
    "[gg]" "Ммммм!"
    "[gg]" "Ты тоже замечательная. "
    "Кристи" "…."
    "[gg]" "{i}Боже, у неё роскошная, кругленькая попочка.{/i}"
    "[gg]" "{i}Как же приятно её касаться.{/i}"
    "[gg]" "{i}Мне не стоило бы распускать руки, но раз уж она сама запрыгнула на меня, это очевидный рефлекс, без которого я бы не смог удержать её на себе.{/i}"
    "[gg]" "{i}Надеюсь, она и сама это понимает.{/i}"
    "Кристи" "Ты уже принялся изучать награду?"

    show black with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    call show_bg_image_label from _call_show_bg_image_label_131

    show Christie Normal
    show Christie Normal:
        xzoom -1
        xalign .12
        ypos 1085

    show GG Embarrassment
    show GG Embarrassment:
        xzoom -1
        xalign .9
        ypos 1085
    with my_dissolve
    "[gg]" "Ой, извини. Я перехожу границы."
    show Christie Embarrassment
    "Кристи" "Нет, ты меня извини. Я сама виновата, что запрыгнула на тебя."
    show Christie Embarrassment
    "Кристи" "В конце концов ты парень, и для тебя… или для вас, это нормальная реакция, ведь так?"
    show GG Embarrassment
    "[gg]" "Абсолютно."
    show Christie Embarrassment
    "Кристи" "Хи-хи-хи…."
    show Christie Embarrassment
    "Кристи" "Тогда до встречи."
    show GG Embarrassment
    "[gg]" "Мгу…"

    show Christie Embarrassment:
        xzoom 1
        ease 1.5 xalign 0.0
    $ renpy.pause(1.5, hard =True)
    show Christie Surprise:
        xalign 0.0
        xzoom 1.0

    with vpunch
    "Кристи" "…."
    show GG Skepticism
    with my_dissolve
    "[gg]" "Что-то не так?"
    show Christie Surprise

    "Кристи" "…."
    show Christie Surprise:
        xzoom -1
    with my_dissolve
    "Кристи" "Реферат."

    show Christie Skepticism:
        xzoom -1
        easein 1 xalign .55
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .0
        easein 1 alpha .5
    show GG Surprise:
        ease 1 xalign .95

    "Кристи" "Ты что, скачал его из интернета?"
    "[gg]" "Ну да, а как ещё?"
    hide expression 'cg/ep45/shower_3/shadow.png'
    show Christie Skepticism:

        easein_cubic 1 xalign .15
    show GG Surprise:
        ease 1 xalign .9
    with None
    "Кристи" "Действительно…"
    show Christie Chagrin
    "Кристи" "Извини, я наверное грубо выразилась, но такой реферат мне совсем не подходит."
    show Christie:
        xalign .15
    show GG:
        xalign .9
    with my_dissolve
    "Кристи" "Наш преподаватель довольно строг к проверкам и, боюсь, если я всучу ему «платный» продукт, он поставит мне неуд, ну, или, потребует взятку, а мне совсем не хотелось бы портить свою репутацию в колледже. "
    show GG Normal
    "[gg]" "Я не знал."
    show Christie Chagrin
    "Кристи" "Поэтому я и не обижаюсь. "
    show Christie Chagrin
    "Кристи" "Здесь нет твоей вины."
    show Christie Chagrin
    "Кристи" "Извини, что ты вынужден был зря потратить деньги."
    show Christie Chagrin
    "Кристи" "Сколько стоил этот реферат? "
    show GG Angry
    "[gg]" "Эй, не надо так! "
    show GG Angry
    "[gg]" "Я делал это не из меркантильных побуждений."
    show GG Angry
    "[gg]" "И раз уж на то пошло, я помогу тебе снова, и в этот раз, уже по-настоящему. "
    show Christie Surprise
    "Кристи" "А?.."
    show GG Angry
    "[gg]" "Жди! Я скоро вернусь!"





    scene black with Dissolve(.5)
    if not getattr(store, 'block_time_forward', False):
        $ time.time_now   = 'evening'

    $ unlock_city_library = True
    $ Location(
            'City_Library',
            buttons       = [],
            image_buttons = {
            'biblio_girl':Jump("christie_root_21_pre_menu")
            }
            )
    $ descript_Christie   = _("Отправиться в библиотеку Утром или Днём, чтобы составить реферат по теме «Обществознании».")

    $ remove_from_inventory(name = 'Реферат')
    $ Event('christie_root_21', 'City_Library_BiblioGirl', button_name = _("Реферат"), time = ['morning', 'afternoon'], priority = -1)

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
