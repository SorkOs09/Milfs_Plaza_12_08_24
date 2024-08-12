
label christie_root_3:
    $ events.pop('christie_root_3', 0)
    call show_bg_image_label from _call_show_bg_image_label_101
    call show_additional_images_label from _call_show_additional_images_label_86

    show Christie Angry
    show Christie Angry:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left





    "[gg]" "Привет, Кристи, ты договорилась?"
    
    "Кристи" "Да, но прежде чем начнётся твоё преображение, я бы хотела быть первой, кто впишет «строчку кода» в твою новую личность."
    show GG Surprise:
        xalign .15
    with my_dissolve
    "[gg]" "О чём ты? Я тебя чем-то обидел?"
    show Christie Angry
    "Кристи" "Ты вошёл в мою комнату без стука, тем самым нарушив мои личные границы. "
    show GG Chagrin
    "[gg]" "Упс…"
    show Christie Angry
    "Кристи" "Я уже собиралась идти погулять, и должна была переодеваться."
    show Christie Angry
    "Кристи" "Если бы ты зашёл на пару минут позже, то застал бы меня без одежды!"
    show GG Embarrassment
    "[gg]" "Мне очень жаль…"
    show GG Chagrin
    "[gg]" "Но ведь ты же можешь закрыться на ключ."
    show Christie Chagrin
    "Кристи" "Дверь заедает. "
    show Christie Chagrin
    "Кристи" "Если я закроюсь, то не смогу открыть. Нужно вызвать мастера, да всё как-то времени нет. "
    show Christie Smile
    "Кристи" "Если хочешь, можешь сам починить замок. "
    show GG Smile
    "[gg]" "Я знаю толк в замках, это верно! Но моя квалификация несколько иного рода, хе-хе, если ты понимаешь, о чём я."
    show GG Smile
    "[gg]" "Зато я знаю человека, который сможет нам помочь. "
    show Christie Angry
    "Кристи" "Если ты имеешь в виду Игоря, то я против."
    show GG Normal
    "[gg]" "Это ещё почему? Он отличный парень и мой лучший друг."
    show Christie Skepticism
    "Кристи" "Он извращенец, который подглядывал за мной в школьном туалете и крал моё нижнее бельё из раздевалки. "
    show GG Laughs
    "[gg]" "Просто ты ему нравишься, вот и всё. "
    show Christie Skepticism
    "Кристи" "Я его боюсь. "
    show GG Laughs
    "[gg]" "Доверься мне, он надёжный парень. "
    show Christie Skepticism
    "Кристи" "Ага, и поэтому он где-то шляется, а ты состоишь на учёте в полицейском участке. "
    show GG Normal
    "[gg]" "Всё не так однозначно…."
    show Christie Skepticism
    "Кристи" "Ну да, ну да."
    show GG Normal
    "[gg]" "Короче, хватит! Я помогу тебе, а Игорь поможет мне, и твоя проблема будет решена."


    show GG Normal
    "[gg]" "Лучше скажи, когда и куда мне явиться к психологу?"
    show Christie Normal
    "Кристи" "Вот, её адрес я скину тебе на телефон. Она сказал, что можешь приходить в любое время днём. "
    show GG Normal
    "[gg]" "Она работает на дому? "
    show Christie Smile
    "Кристи" "Да, но ты не волнуйся. Я знакома с ней лично. Никто тебя на куски не порежет и в речку останки не скинет, хи-хи."
    show GG Normal
    "[gg]" "…"
    show GG Normal
    "[gg]" "Хорошо, спасибо. "

    $ descript_Christie = _("Теперь я могу отправиться к психологу, но сперва мне следует поговорить с Игорем и попросить его помочь с замком Кристи.")
    if getattr(store, 'block_igor_position', False):

       
        $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")
    
    $ Event('christie_root_4', 'Igor', 'christie_root_4', button_name = _('Обсудить психолога (Задание Кристи)'))

    $ block_exit_home = False
    $ block_map       = False
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
