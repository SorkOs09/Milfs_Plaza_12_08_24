
image cinema_wine_sex_Ani:
    'cg/ep1/movie/cinema_wine_sex_8_1.png' with Dissolve(.5)
    1
    'cg/ep1/movie/cinema_wine_sex_8_2.png' with Dissolve(.5)
    1

    repeat
label hall_tumba_under_tv_lolita_label_ep3_1:
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    play sound 'audio/get_item.ogg'


    show screen give_item_screen(i_path+'/items/lolita.png', _('Фильм "Лолита"'), [_('Отличный фильм для'), _('просмотра с любимым человеком.')])



    with Dissolve(.5)
    $ renpy.pause(999999)

    $ locations['Hall'].buttons[0]['tumba_under_tv'] = ((1470, 725, 135, 180),   Jump('hall_tumba_under_tv_label'))

    $ add_to_inventory(name = 'Фильм "Лолита"')

    hide screen give_item_screen
    with Dissolve(.5)

    jump main_interface_label

label ep3_1_start:
    call show_bg_image_label from _call_show_bg_image_label_63
    call show_additional_images_label from _call_show_additional_images_label_57

    if not get_item('Фильм "Лолита"', True):
        call show_characters_images_label from _call_show_characters_images_label_1
        with my_dissolve
        "[gg]" "Мне еще нужен фильм"
        $ Event('ep3_1_start', 'Hall_Milf', time = ['evening'])
        jump main_interface_label
    if not get_item('Красное вино', True):
        call show_characters_images_label from _call_show_characters_images_label_2
        with my_dissolve
        "[gg]" "Мне еще нужно вино"
        $ Event('ep3_1_start', 'Hall_Milf', time = ['evening'])
        jump main_interface_label

    show Milf Night_Normal
    show Milf Night_Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)
    show GG Vine
    show GG Vine at go_from_left
    $ from_say_screen = False
    $ renpy.pause(1)




    $ events.pop('ep3_1_start', 0)

    '[gg]' "Как на счёт того, чтобы посмотреть «Лолиту» и выпить немножко вина? "

    show Milf Night_Passion
    show GG:
        xalign .15
    with my_dissolve


    'Марина' "Вау, [gg]. Ты меня поражаешь. "

    '[gg]' "Ну так что?"

    show Milf Night_Smile

    'Марина' "Включай кино, а я пока открою бутылку."

    #$ remove_from_inventory('Фильм "Лолита"')
    $ remove_from_inventory('Красное вино')


    $ location_now = 'Hall'
    call show_all_images_label from _call_show_all_images_label_87
    $ hall_mother_tmp = True
    $ descript = _('Я должен вставить диск в видео-проигрыватель.')


    $ Event('ep3_1_stumb_1', 'Corridor',  'ep3_1_stumb')
    $ Event('ep3_1_stumb_2', 'Milf_Room', 'ep3_1_stumb')


    $ block_time_forward_tmp_23432434 = copy.deepcopy(block_time_forward)
    $ block_time_forward = True
    $ milf_position['evening'] = ['None', 'milf_evening_hall']
    $ locations['Hall'].buttons[1]['video_player'] = ((1490, 699, 154, 45),   Jump('ep3_1_stumb_tumba_under_tv'))


    jump main_interface_label

label ep3_1_stumb_tumba_under_tv:
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    menu:
        "Вставить диск" if True:
            jump ep3_1_wine_sex_milf_label
        "Назад" if True:


            jump main_interface_label
    jump main_interface_label

label ep3_1_stumb:
    if 'ep3_1_stumb_1' in getattr(store, 'completed_events', [1, 0]):

        $ events.pop('ep3_1_stumb',   0)
        $ events.pop('ep3_1_stumb_1', 0)
        $ events.pop('ep3_1_stumb_2', 0)
        jump main_interface_label

    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    with my_dissolve
    '[gg]' "Я никуда отсюда не уйду."
    '[gg]' "Я должен вставить диск в видео-проигрыватель."
    $ Event('ep3_1_stumb_1', 'Corridor',  'ep3_1_stumb')
    $ Event('ep3_1_stumb_2', 'Milf_Room', 'ep3_1_stumb')

    $ location_now = 'Hall'









    jump main_interface_label

label ep3_1_wine_sex_milf_label:
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    if not from_gallery_check():
        $ locations['Hall'].buttons[1]['video_player'] = ((1490, 699, 154, 45),   Jump('hall_video_player_label'))
        $ milf_position['evening'] = ['Hall', 'milf_evening_hall']
    $ location_now  = 'Hall'
    $ time.time_now = 'evening'
    call show_bg_image_label from _call_show_bg_image_label_95
    show expression 'cg/gg_activities/active_cinema_cg.png'
    with Dissolve(.5)


    '[gg]' "Кино готово к просмотру. "




    if not get_item('Фильм "Лолита"', True):

        $ add_to_inventory(name = 'Фильм "Лолита"')


    #$ remove_from_inventory('Фильм "Лолита"')
    stop music fadeout 1.5
    play music 'audio/movie_event.mp3' fadein 1.5
    scene expression 'cg/ep1/movie/cinema_screen_3.png' with Dissolve(.5)
    'Лолита' "Давай уедем. Далеко-далеко. Только ты и я."
    'Мужчина' "Это опрометчиво."
    'Лолита' "Но здесь нам не позволят быть вместе. Никогда…"
    scene expression 'cg/ep1/movie/cinema_wine_normal_0.png' with Dissolve(.5)
    '[gg]' "Как тебе вино?"
    'Марина' "Прекрасное. И кажется, я немного перебрала."
    scene expression 'cg/ep1/movie/cinema_wine_normal_1.png' with Dissolve(.5)
    '[gg]' "Слушай, подруга, пока мы ещё окончательно не напились, я хотел бы…"
    'Марина' "Нет, позволь мне первой."
    '[gg]' "Да?"
    'Марина' "Я хочу обсудить твой проступок, [gg]. "
    '[gg]' "О нет, только не вздумай портить наш вечер!"
    scene expression 'cg/ep1/movie/cinema_wine_normal_1a.png' with Dissolve(.5)
    'Марина' "Если ты и далее намерен жить в этом доме, следует придерживаться определённых правил. Главное из которых – никакой уголовщины."
    scene expression 'cg/ep1/movie/cinema_wine_normal_2.png' with Dissolve(.5)
    '[gg]' "Ну… Ты преувеличиваешь. Всего-лишь небольшая шалость. "
    scene expression 'cg/ep1/movie/cinema_wine_normal_3.png' with Dissolve(.5)
    'Марина' "Из-за которой тебя могли посадить на пару лет."
    '[gg]' "Кто ж знал, что всё так обернётся? Мы не собирались ничего воровать, просто шутили. "
    '[gg]' "Это самая нелепая отмазка, которую я только смог из себя выдавить. "
    scene expression 'cg/ep1/movie/cinema_wine_normal_4.png' with Dissolve(.5)
    'Марина' "Как я уже сказала, ворам здесь не место. "
    '[gg]' "Дааааа?"
    'Марина' "Да. Вор должен сидеть в тюрьме. "
    '[gg]' "Даже если это я?"
    'Марина' "Даже если и ты."
    '[gg]' "…"
    '[gg]' "Что ж! ЧТО ЖЕ!"
    scene expression 'cg/ep1/movie/cinema_wine_normal_5.png' with Dissolve(.5)
    '[gg]' "Тогда, если ты, вдруг, заболеешь раком и нам срочно понадобится огромная сумма денег на лечебные процедуры, не проси меня ограбить банк! Я, знаешь ли, не преступник."
    scene expression 'cg/ep1/movie/cinema_wine_normal_6.png' with Dissolve(.5)
    'Марина' "Ха-ха-ха-ха! "
    'Марина' "Какой ты дурашка."
    scene expression 'cg/ep1/movie/cinema_wine_normal_7.png' with Dissolve(.5)
    'Марина' "Я бы ни за что не стала о таком просить. Лучше мучительная смерть, чем видеть, как твой друг разлагается, теряя всякую человечность."
    scene expression 'cg/ep1/movie/cinema_wine_normal_2.png' with Dissolve(.5)
    '[gg]' "Я всё равно ограблю банк. Не смогу смотреть, как ты корчишься от боли!"
    scene expression 'cg/ep1/movie/cinema_wine_normal_1a.png' with Dissolve(.5)
    'Марина' "Эй, прекрати меня хоронить! Я ничем не болею. И уж тем более не планирую умирать."
    scene expression 'cg/ep1/movie/cinema_wine_normal_8.png' with Dissolve(.5)
    'Марина' "У меня имеются кое-какие сбережения для экстренных случаев. Так что, можешь оставить свои амбиции в сфере криминала."
    '[gg]' "Ах вот как… И много там, в заначке твоей? "
    'Марина' "Не твоего ума дела, хи-хи."
    scene expression 'cg/ep1/movie/cinema_wine_normal_0.png' with Dissolve(.5)
    '[gg]' "Ты права, я слишком перегибаю палку."
    'Марина' "Верно замечено, [gg]."
    '[gg]' "Учитывая, как я влип в этот самый криминал, лучше и не пытаться просить занять у неё денег."
    scene expression 'cg/ep1/movie/cinema_wine_normal_9.png' with Dissolve(.5)
    '[gg]' "Знаешь… Хочу ещё раз извиниться, что подвёл тебя. "
    '[gg]' "Прости меня, за эту дурость с кражей из магазина. Пожалуйста, поверь, я сделаю всё возможное, чтобы загладить свою вину перед тобой."
    'Марина' "Не надо ничего заглаживать, [gg]. Просто не совершай ничего такого, что может создать нам проблемы. "
    scene expression 'cg/ep1/movie/cinema_wine_normal_10.png' with Dissolve(.5)
    '[gg]' "По рукам."
    'Марина' "Вот и чудненько. Тогда, быть может, наконец-то посмотрим сериал?"
    '[gg]' "Конечно! "
    scene expression 'cg/ep1/movie/cinema_wine_normal_11.png' with Dissolve(.5)
    'Марина' "Если ты не против, я прилягу к тебе. Вино ударило мне в голову. "
    '[gg]' "Я полностью в твоём распоряжении. "
    scene black with Dissolve(1)
    $ renpy.pause(.5, hard = True)
    scene expression 'cg/ep1/movie/cinema_wine_sex_1.png' with Dissolve(1)
    'Марина' "Ах, как хорошо. "
    'Марина' "Мы так давно не были по-настоящему вместе. "
    'Марина' "С объятиями и дружеской беседой. "
    'Марина' "Как старые добрые друзья."
    '[gg]' "В-верно…"
    scene expression 'cg/ep1/movie/cinema_wine_sex_2.png' with Dissolve(.5)
    '[gg]' "О, Господи, её тело такое горячее!"
    '[gg]' "И её спокойное, протяжное дыхание… "
    '[gg]' "Только не смотри на неё! Только не смотри!"
    scene expression 'cg/ep1/movie/cinema_wine_sex_3.png' with Dissolve(.5)
    '[gg]' "Проклятье! "
    '[gg]' "Разве можно устоять перед этими огромными, сладкими дыньками?!"
    '[gg]' "Я бы отдал всё на свете, только бы попить из них молочко."
    scene expression 'cg/ep1/movie/cinema_wine_sex_4.png' with Dissolve(.5)
    '[gg]' "Марина?.."
    '[gg]' "Ты спишь?"
    scene expression 'cg/ep1/movie/cinema_wine_sex_5.png' with Dissolve(.5)
    '[gg]' "И очень вовремя. От разглядывания её сексуальных форм, у меня случился деревянный стояк. "
    '[gg]' "Что же мне делать? Разбудить её, пока ещё не слишком поздно? "
    '[gg]' "Или… Быть может…."
    scene expression 'cg/ep1/movie/cinema_wine_sex_6.png' with Dissolve(.5)
    '[gg]' "Аккуратно… Нежно… "
    '[gg]' "Я точно сошёл с ума!"
    '[gg]' "Если моя подруга проснётся, я вряд ли смогу оправдаться. "
    '[gg]' "Она наверняка решит, что её друг извращенец!"
    '[gg]' "Плевать."
    '[gg]' "Я слишком близко, чтобы отступать. "
    scene expression 'cg/ep1/movie/cinema_wine_sex_7.png' with Dissolve(.5)
    stop music fadeout 1.5
    play music 'audio/Erotic.mp3' fadein 1.5
    '[gg]' "O, даааааа!!! "
    '[gg]' "Как же они хороши!!!"
    scene expression 'cg/ep1/movie/cinema_wine_sex_8_1.png' with Dissolve(.5)
    '[gg]' "Я так взбудоражен, что, наверное, вот-вот взорвусь."
    scene cinema_wine_sex_Ani with Dissolve(.5)
    '[gg]' "Её мягкие, сочные груди просто таят в моих руках."
    '[gg]' " Марина так усиленно дышит, что это заводит меня ещё сильнее."
    '[gg]' "Ещё чуточку… Пожалуйста. Ещё чуточку."
    scene expression 'cg/ep1/movie/cinema_wine_sex_8_3.png' with Dissolve(.5)
    '[gg]' "Каааааайф!!!..."
    scene expression 'cg/ep1/movie/cinema_wine_sex_9.png' with Dissolve(.5)
    '[gg]' "Чёрт… Я так увлёкся, что чуть не разбудил её."
    scene expression 'cg/ep1/movie/cinema_wine_sex_6.png' with Dissolve(.5)
    '[gg]' "Нужно прекращать это безобразие и возвращаться в свою комнату. "
    scene expression 'cg/ep1/movie/cinema_wine_sex_2.png' with Dissolve(.5)
    play music 'audio/movie_event.mp3' fadein 1.5
    'Марина' "Ой, [gg], кажется я уснула на тебе."
    '[gg]' "Н-ничего страшного. Ты вовсе не стеснила меня. "
    scene expression 'cg/ep1/movie/cinema_wine_sex_1.png' with Dissolve(.5)
    'Марина' "Ну и хорошо. Мне сладко спалось."
    '[gg]' "Рад был провести с тобой время, подружка."
    'Марина' "И я…"
    scene expression 'cg/ep1/movie/cinema_wine_sex_10.png' with Dissolve(.5)
    'Марина' "Надеюсь, он не заметил, что я давно уже не сплю."
    'Марина' "И то, как сильно я возбудилась от его прикосновений…"
    'Марина' "Мне не стоило позволять ему делать это. "
    'Марина' "Это неправильно. "
    'Марина' "Больше я не совершу эту ошибку."
    $ location_now = 'Hall'
    scene black
    with Dissolve(.5)

    $ renpy.pause(.5)

    call show_bg_image_label from _call_show_bg_image_label_64
    call show_additional_images_label from _call_show_additional_images_label_58
    with Dissolve(.5)

    show GG Normal
    show GG Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    show Milf Night_Normal
    show Milf Night_Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with my_dissolve
    'Марина' "Сладких снов, [gg]."
    '[gg]' "И тебе, Марина."
    hide Milf

    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)






    $ milf_drunk = True
    
    if hasattr(store, 'events'):
            
        $ events.pop('ep3_1_stumb',   0)
        $ events.pop('ep3_1_stumb_1', 0)
        $ events.pop('ep3_1_stumb_2', 0)


    if not from_gallery_check() and not hasattr(store, 'unlock_film_lolita'):

        show GG:


            linear .5 xalign .5
        $ renpy.pause(.5, hard = True)

        show GG Think with Dissolve(.5)
        '[gg]' "Сегодня у меня прошёл потрясающий вечер с Мариной."
        '[gg]' "Я ещё не скоро его забуду, как и её груди."
        '[gg]' "Но не это сейчас важно. В ходе нашей беседы она призналась, что у неё имеется какая-то заначка. "
        '[gg]' "Это всё меняет!"
        '[gg]' "Если у неё действительно имеется сумма, которая покроет мой долг, мне никуда не придётся уезжать. "
        '[gg]' "Естественно, что как только я расплачусь, я буду работать как чёрт, только бы верну ей поскорее деньги!"
        '[gg]' "Но сперва мне нужно спасти свою задницу."
        '[gg]' "Следует обыскать комнату Марины и узнать, где именно она прячет свою «заначку». "
        $ add_to_gallery(5)
        $ unlock_film_lolita   =  True
        $ ep2_milf_room_unlock = True
        $ descript = _('Следует обыскать комнату Марины и узнать, где именно она прячет свою «заначку». ')




        $ locations['Milf_Room'].buttons[0].update({'pictures':[(425, 0, 175, 235,), [Jump('ep3_3_pictures')]]})

        $ block_time_forward = copy.deepcopy(block_time_forward_tmp_23432434)
        $ del block_time_forward_tmp_23432434







        $ Event('ep3_2_morning', 'GG_Room', time = ['morning',])

        $ time.time_forward()

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
