label christie_root_54:
    if getattr(store, 'block_igor_position', False):

        $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")

        $ events['christie_root_54'].day_start = time.day_now + 1
        jump main_interface_label
    $ events.pop('christie_root_54', 0)
    #Поговорить с Игорем в парке Утром, узнав у него, смог он взломать телефон Маши или нет.
    #"ext" "Активировать Игоря в Парке"
    #"ext" "GG_Normal"
    #"ext" "Igor_Normal"
    call show_bg_image_label from _call_show_bg_image_label_223

    call show_additional_images_label from _call_show_additional_images_label_111

    show Igor Normal
    show Igor Normal:
        xalign .85
        ypos 1085

    with Dissolve(.5)

    show GG Normal
    show GG Normal at go_from_left
    
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/funk-game-loop-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Ну как, получилось найти что-нибудь интересное?"
    show GG:
        xalign .15
    with my_dissolve
    "Igor" "Давай отложим этот вопрос на десять секунд позже."
    show Igor Surprise
    "Igor" "Сейчас меня больше всего на свете волнует вопрос, как ты, говнюк ты эдакий, смог убедить Кристи раздеться на камеру?!"
    show Igor Surprise
    "Igor" "Ты заплатил ей? Угрожал? Подсыпал ей наркотики?!"
    show GG Surprise
    "[gg]" "Кто я, по-твоему, отпетый сутенёр?"
    show Igor Angry
    "Igor" "Ты чёрный колдун, который продал душу дьяволу, иначе я не могу объяснить, как Кристи согласилась бы на такой отвязный шаг!"
    show GG Laughs
    "[gg]" "Ха-ха-ха-ха!"
    show GG Smile
    "[gg]" "Я думал, ты будешь доволен. "
    show Igor Surprise
    "Igor" "Доволен ли я?! Да я готов сожрать свои яйца, отвисающие у меня до колен со вчерашнего вечера!!!"
    show Igor Normal
    "Igor" "Но я не успокоюсь, пока не узнаю правду. Как?! Как тебе удалось?!"
    show Igor Embarrassment
    "Igor" "Она сделала это ради меня, да?"
    show Igor Embarrassment
    "Igor" "Это такой тонкий… точнее даже ТОЛСТЫЙ намёк на то, что я ей нравлюсь?"
    show Igor Embarrassment
    "Igor" "ООООООЧЕНЬ НРАВЛЮСЬ!"
    show GG Smile
    "[gg]" "Эй, выдохни, бро."
    show GG Normal
    "[gg]" "Кристи нужен этот телефон ровно так же, как и мне, и она согласилась на твои условия."
    show Igor Skepticism
    "Igor" "Хочешь сказать, это просто плата за мою работу?"
    show GG Normal
    "[gg]" "Всё верно."
    show Igor Skepticism
    "Igor" "Ты врёшь! Она хочет меня, а ты просто завистник!"
    show GG Angry
    "[gg]" "Я не вру, чувак. Это правда."
    show Igor Chagrin
    "Igor" "Мне трудно в это поверить, [gg]."
    show Igor Chagrin
    "Igor" "Это видео… Это словно любовное послание, понимаешь?"
    show GG Normal
    "[gg]" "Я опасался, что ты воспримешь так..."
    show GG Normal
    "[gg]" "Но это правда. Я и Кристи помогаем одному человеку, и информация на этом телефоне очень важна для нас."
    show Igor Chagrin
    "Igor" "Что ж..."
    show Igor Chagrin
    "Igor" "Лучше воробей в руках, чем синица в небе."
    show GG Normal
    "[gg]" "Ты всегда правильно мыслил."
    show Igor Chagrin
    "Igor" "Ну да, ну да…"
    show Igor Normal
    "Igor" "Ладно, вот твой мобильник, который ты дал мне для хакинга."
    show GG Surprise
    "[gg]" "Ну и как, получилось?"
    show GG Surprise
    "[gg]" "Что там?!"
    show Igor Skepticism
    "Igor" "Какая-то феерия."
    show Igor Normal
    "Igor" "Обаятельная «шоколадка» резвится с темнокожим парнем, а мент стоит рядом и мастурбирует."
    show GG Skepticism
    "[gg]" "Да ладно?!"
    show Igor Normal
    "Igor" "Ага."
    show Igor Embarrassment
    "Igor" "Смотреть это так же стыдно, как и думать, что женский оргазм существует."
    show Igor Troll
    "Igor" "Качество видео дерьмо, конечно, ракурс ужасный, но лица видны отчётливо... Короче, 3 из 10."
    show GG Normal
    "[gg]" "Отвратительно…"
    show GG Normal
    "[gg]" "А кто это всё заснял? Кто оператор?"
    show Igor Normal
    "Igor" "Судя по ракурсу, камера установлена в одной из раздевалок магазина."
    show GG Normal
    "[gg]" "Интересно, зачем?"
    show Igor Normal
    "Igor" "Предполагаю, наша темнокожая красотка или оставляет их для возможного шантажа, или продаёт в интернете."
    show GG Normal
    "[gg]" "Ох чёрт…"
    show GG Normal
    "[gg]" "Теперь мне становится кое-что понятно…"
    show Igor Normal
    "Igor" "Только меня не приплетай, пожалуйста."
    show GG Normal
    "[gg]" "И в мыслях не было. Этого более чем достаточно."
    show GG Normal
    "[gg]" "Спасибо, ты очень выручил нас."
    show Igor Smile
    "Igor" "Ах да, в следующий раз, если что-то понадобится, в качестве награды хочу пригласить Кристи на свидание."
    show GG Chagrin
    "[gg]" "Извини, чувак, но такого раза никогда не предвидится. "
    show Igor Normal
    "Igor" "Что ты этим хочешь сказать?.."
    show GG Normal
    "[gg]" "Уверен, ты и сам уже обо всём догадался."
    show Igor Surprise
    "Igor" "Чо?!"
    show Igor Surprise
    "Igor" "Ты и Кристи?"
    show GG Normal
    "[gg]" "Мгу."
    show Igor Laughs
    "Igor" "Да не, бред какой-то!"
    show GG Embarrassment
    "[gg]" "Я люблю её, Игорь."
    show Igor Angry
    "Igor" "Пока не увижу, как вы трахаетесь, не поверю."
    show GG Smile
    "[gg]" "Это похоже на провокацию."
    show Igor Embarrassment
    "Igor" "Так что, скинете видосик?"
    show GG Laughs
    "[gg]" "Чёрт, Кристи права – ты извращенец!"
    show Igor Angry
    "Igor" "Я учёный и требую доказательств!"
    show Igor Angry
    "Igor" "Чтобы к вечеру порнушка у меня была на столе!"
    show GG Skepticism:
        xzoom -1
        easein 2 xalign .05
    "[gg]" "Хорошего дня, Игорь!"
    #"ext" "//GG_Normal  начинает отъезжать в сторону"
    show Igor Angry
    show GG Surprise:
        xzoom 1
    with my_vpunch
    "Igor" "ПОРНО!!! ВЫШЛИТЕ МНЕ ПОРНО!!!!"
    show GG:
        parallel:
            xzoom -1
            pause 1.0
            xzoom 1
            pause 1.0
            xzoom -1
            pause 1.0
            xzoom -1
        parallel:
            easein .25 ypos 1100
            pause .75
            easein .25 ypos 1085
            pause .75
            easein .25 ypos 1100
            pause .75
            easein .25 ypos 1085       
    show shadow_full:
        alpha .0
        easein .25 alpha 1.0
        pause .75
        easein .25 alpha .5
        pause .75
        easein .25 alpha 1.0
        pause .75
        easein .25 alpha .5
    "[gg]" "Мать твою, Игорь, на нас же люди пялятся. "
    #"ext" "//GG_Surprise начинает отъезжать ещё дальше"
    show Igor Angry
    "Igor" "ИЛИ ТЫ ТРАХНЕШЬ КРИСТИ ПРЯМ НА МОЕЙ КРОВАТИ, ИЛИ Я НЕ ПОВЕРЮ!!!"
    #"ext" "//GG_Surprise начинает отъезжать ещё дальше"
    show GG Surprise:
        xzoom -1
        easein 2 xalign -1.5
    show shadow_full:
        easein 3 alpha 1.0

    "[gg]" "Пора сваливать…"
    
    
    call christie_root_try_to_del_descript_christie_block_igor from _call_christie_root_try_to_del_descript_christie_block_igor_7
    
    $ descript_Christie = __("Отправиться к Сьюзен и показать ей доказательства измены мужа. ")
    
    $ Event('christie_root_55', 'City_Psi', time = ['morning', 'afternoon'])
    scene black with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    $ location_now = "City_Home"
    jump main_interface_label