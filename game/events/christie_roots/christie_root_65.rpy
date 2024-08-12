image christie_root_65_tea 0 = 'cg/ep10/susan_scene/tea_0.png'
image christie_root_65_tea 1 = 'cg/ep10/susan_scene/tea_1.png'
image christie_root_65_tea 2 = 'cg/ep10/susan_scene/tea_2.png'

image christie_root_65_sex 0_1 = 'cg/ep10/susan_scene/continue/sex_1/0_1.png'
image christie_root_65_sex 0_2 = 'cg/ep10/susan_scene/continue/sex_1/0_2.png'

image christie_root_65_hat_1 = 'cg/ep10/susan_scene/continue/police_hat.png'
image christie_root_65_hat_2 = 'cg/ep10/susan_scene/continue/police_hat.png'
image christie_root_65_hat_3 = 'cg/ep10/susan_scene/continue/police_hat.png'


image christie_root_65_bat_sfx_1_1 = 'cg/ep10/susan_scene/continue/bat_sfx_1.png'

image christie_root_65_bat_sfx_1_2 = 'cg/ep10/susan_scene/continue/bat_sfx_1.png'

image christie_root_65_bat_sfx_1_3 = 'cg/ep10/susan_scene/continue/bat_sfx_1.png'

image christie_root_65_bat_sfx_2 = 'cg/ep10/susan_scene/continue/bat_sfx_2.png'

image christie_root_65_bat_sfx_3 = 'cg/ep10/susan_scene/continue/bat_sfx_3.png'

image christie_root_65_bat_sfx_4 = 'cg/ep10/susan_scene/continue/bat_sfx_4.png'


image christie_root_65_psi_grab_officer = Composite((749, 1080),
    (0, 235), 'cg/ep10/susan_scene/continue/psi_grab_officer.png')

transform christie_root_65_sex_1_transform(t_1 = .1, t_2 = .05):
    pos (960, 1080)
    easein t_1 pos (960, 1085)
    easeout t_2 pos (960, 1080)

transform change_alpha_with_easein(t = .3, a = .0):
    easein .2 alpha .0

image christie_root_65_christie_sex pose_1_0 = 'cg/ep10/susan_scene/end/pose_1/1.png'


image christie_root_65_christie_sex pose_3_cum = 'cg/ep10/susan_scene/end/pose_3/cum.png'


transform christie_root_65_cum_transform:
    xzoom .01
    easeout 1.5 xzoom 1

label christie_root_65_psi_talk_1:
    show image comic_frame_v2_master:
        zoom .8
        xpos 950
        ypos 250
        xanchor 1.0
        yanchor .0
        alpha .0

        parallel:
            easein 0.2 ypos 200
        parallel:
            ease .2 alpha 1.0

    $ renpy.pause(.2, hard = True)
    return



label christie_root_65_chrisite_talk_shake:
    show image comic_frame_v2_master:
        zoom .7
        xpos 1140
        ypos 170
        xanchor 1.0
        yanchor .0
        alpha .0
        alpha .0
        parallel:
            easein 0.1 ypos 176
            easein 0.1 ypos 170
            easein 0.1 ypos 176
            easein 0.1 ypos 170
            
        parallel:
            ease .1 alpha 1.0

    $ renpy.pause(.2, hard = True)
    return

label christie_root_65_psi_talk_2:
    show image comic_frame_v2_master:
        zoom .8
        xpos 20
        ypos 1050
        xanchor 0.0
        yanchor 1.0
        alpha .0

        parallel:
            easein 0.2 ypos 1000
        parallel:
            ease .2 alpha 1.0

    $ renpy.pause(.2, hard = True)
    return


label christie_root_65_psi_talk_3:
    show image comic_frame_v2_master:
        zoom .8
        xpos 20
        ypos 100
        xanchor 0.0
        yanchor 0.0
        alpha .0

        parallel:
            easein 0.2 ypos 50
        parallel:
            ease .2 alpha 1.0

    $ renpy.pause(.2, hard = True)
    return


label christie_root_65_psi_talk_4_hide:
    $ j = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
    $ i = list(j.get_placement()) + [j.xzoom, j.yzoom, j.zoom, j.alpha, j.xanchor, j.yanchor]
    
    $ store.comic_frame_v2_slave  = store.comic_frame_v2_master

    show image comic_frame_v2_master:
        alpha 0.0
        xpos i[0]
        ypos i[1]
        xanchor i[2]
        yanchor i[3]
        xoffset i[4]
        yoffset i[5]
        subpixel i[6]
        xzoom i[7]
        yzoom i[8]
        zoom  i[9]
        xanchor i[11]
        yanchor i[12]
    show image comic_frame_v2_slave:
        xpos i[0]
        ypos i[1]
        xanchor i[2]
        yanchor i[3]
        xoffset i[4]
        yoffset i[5]
        subpixel i[6]
        xzoom i[7]
        yzoom i[8]
        zoom  i[9]
        alpha i[10]
        xanchor i[11]
        yanchor i[12]
        easein .2  alpha 0.0
    #$ renpy.pause(.21, hard = True)
    return 

label christie_root_65_psi_talk_4:
    show image comic_frame_v2_master:
        zoom .65
        xpos 700
        ypos 100
        xanchor 0.0
        yanchor 0.0
        alpha .0

        parallel:
            #easein store._st_65_t ypos 180
            #block:
            #№    easeout 0.85 ypos 230
            easein 0.51 ypos 50
            #    repeat
        parallel:
            ease .2 alpha 1.0

    $ renpy.pause(.2, hard = True)
    return



label christie_root_65_psi_talk_5:
    show image comic_frame_v2_master:
        zoom .75
        xpos 900
        ypos 30 #store._st_65_y
        xanchor 0.0
        yanchor 0.0
        alpha .0

        parallel:
            #easein store._st_65_t ypos 20
            
            #block:
                #easein 1.5  ypos 50
            easein 0.433 ypos 20
                #repeat
        parallel:
            ease .2 alpha 1.0

    $ renpy.pause(.2, hard = True)
    return



label christie_root_65_psi_talk_6:
    show image comic_frame_v2_master:
        zoom .75
        xpos 900
        ypos 30 #store._st_65_y
        xanchor 0.0
        yanchor 0.0
        alpha .0

        parallel:
            #easein store._st_65_t ypos 20
            
            #block:
                #easein 1.0  ypos 50
            easein 0.33 ypos 20
            #    repeat
        parallel:
            ease .2 alpha 1.0

    $ renpy.pause(.2, hard = True)
    return

label christie_root_65_gg_talk_shake:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1300
        ypos 300
        xanchor 0.0
        yanchor 1.0
        alpha .0
        parallel:
            easein 0.1 ypos 306
            easein 0.1 ypos 300
            easein 0.1 ypos 306
            easein 0.1 ypos 300
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return

label christie_root_65_gg_talk_1:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1895
        ypos 670
        xanchor 1.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.1 ypos 650
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return


label christie_root_65_gg_talk_2:

    show image comic_frame_v2_master:
        zoom .7
        xpos 480
        ypos 600
        xanchor 1.0
        yanchor 1.0
        alpha .0
        parallel:
            easein 0.1 ypos 630
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return



label christie_root_65_gg_talk_3:

    show image comic_frame_v2_master:
        zoom .85
        xpos 700
        ypos 650
        xanchor 1.0
        yanchor 1.0
        alpha .0
        parallel:
            easein 0.1 ypos 680
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return



label christie_root_65_gg_talk_4:

    show image comic_frame_v2_master:
        zoom .85
        xpos 1905
        ypos 550
        xanchor 1.0
        yanchor 1.0
        alpha .0
        parallel:
            easein 0.1 ypos 580
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return




label christie_root_65_gg_talk_5:

    show image comic_frame_v2_master:
        zoom .85
        xpos 1905
        ypos 750
        xanchor 1.0
        yanchor 1.0
        alpha .0
        parallel:
            easein 0.1 ypos 780
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return


label christie_root_65_gg_talk_shake_4:

    show image comic_frame_v2_master:
        zoom .85
        xpos 1905
        ypos 570
        xanchor 1.0
        yanchor 1.0
        alpha .0
        parallel:
            easein 0.1 ypos 588
            easein 0.1 ypos 580
            easein 0.1 ypos 588
            easein 0.1 ypos 580
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return


label christie_root_65_christie_talk_1:

    show image comic_frame_v2_master:
        zoom .65
        xpos 1320
        ypos 350
        xanchor 0.0
        yanchor 0.5
        alpha .0
        parallel:
            easein 0.1 ypos 380
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return



label christie_root_65_christie_talk_2:

    show image comic_frame_v2_master:
        zoom .65
        xpos 930
        ypos 250
        xanchor 1.0
        yanchor 0.5
        alpha .0
        parallel:
            easein 0.1 ypos 280
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return



label christie_root_65_christie_talk_3:

    show image comic_frame_v2_master:
        zoom .7
        xpos 100
        ypos 70
        xanchor 0.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.1 ypos 100
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return


label christie_root_65_christie_talk_shake_2:

    show image comic_frame_v2_master:
        zoom .65
        xpos 930
        ypos 275
        xanchor 1.0
        yanchor 0.5
        alpha .0
        parallel:
            easein 0.1 ypos 288
            easein 0.1 ypos 280
            easein 0.1 ypos 288
            easein 0.1 ypos 280

            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return

label christie_root_65_gg_talk_shake_3:

    show image comic_frame_v2_master:
        zoom .7
        xpos 480
        ypos 636
        xanchor 1.0
        yanchor 1.0
        alpha .0
        parallel:
            easein 0.1 ypos 630
            easein 0.1 ypos 636
            easein 0.1 ypos 630
            easein 0.1 ypos 636
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return

label christie_root_65_gg_talk_shake_2:

    show image comic_frame_v2_master:
        zoom .7
        xpos 1910
        ypos 650
        xanchor 1.0
        yanchor 0.0
        alpha .0
        parallel:
            easein 0.1 ypos 656
            easein 0.1 ypos 650
            easein 0.1 ypos 656
            easein 0.1 ypos 650
            
        parallel:
            ease .1 alpha 1.0
    $ renpy.pause(.2, hard = True)
    return
label christie_root_65:
    #Явиться в гости к Сьюзен. 
    #"ext" "Активировать Сьюзен Утром или Днём."

    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    scene expression 'cg/christie_root/Psi_Build.png'
    with Dissolve(.25)

    $ renpy.pause(.25, hard = True)

    call comic_frame_v2_predict_label(images=comic_frame_v2_predict_list+[
        'cg/christie_root/psi_corridor.png', 
        'Psi *',
        'Christie *',
        'Officer *',
        'christie_root_65_tea *',
        'christie_root_65_sex *',
        'cg/ep10/susan_scene/start/*.*',
        'christie_root_65_christie_sex *',
        'cg/ep10/susan_scene/continue/sex_2/bg.png',
        'cg/ep10/susan_scene/continue/sex_1/bg.png',
        'cg/ep10/susan_scene/continue/*.*',
        'cg/ep10/susan_scene/continue/sex_1/gg.png',
        'cg/ep10/susan_scene/end/pose_1/bg.png',
        'cg/ep10/susan_scene/end/pose_1/fg.png',
        'cg/ep10/susan_scene/end/pose_2/bg.png',
        'cg/ep10/susan_scene/end/pose_3/bg.png',

        ]) from _call_comic_frame_v2_predict_label_2 
    call screen rtrn_screen('cg/christie_root/Psi_Build_Door.png')

    scene black with Dissolve(.25)
    $ renpy.music.stop(fadeout=1.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    scene expression 'cg/christie_root/psi_corridor.png'
    with Dissolve(.25)
    $ renpy.pause(.5, hard = True)
    call screen rtrn_screen

    $ Hide('main_city_screen')()
    $ Hide('main_interface')()
    $ Hide('icons_interface')()
    if not from_gallery_check():
        $ events.pop('christie_root_65', 0)

    scene black with Dissolve(.5)

    # $ renpy.music.stop(fadeout=1.5)

    # $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    $ renpy.pause(.5, hard = True)

    scene expression 'cg/christie_root/psi_corridor.png'
    show Psi Normal
    show Psi Normal:
        xalign .8
        ypos 1085

    with Dissolve(.5)


    show GG Normal
    show GG Normal at go_from_left

    "Сьюзан" "Ох, [gg], как хорошо, что ты пришёл!"
    show GG Laughs:
        xalign .15
    with my_dissolve
    "[gg]" "Пришлось."
    show Psi Normal
    "Сьюзан" "Знаю, я требую слишком много…"
    show GG Normal
    "[gg]" "Вы вообще не имеете права от меня что-либо требовать."
    show Psi Normal
    "Сьюзан" "Верно. Но у меня нет выбора."
    show Psi Normal
    "Сьюзан" "Могу я предложить чай, кофе? "
    show GG Think
    "[gg]" "Надеюсь, беседа будет короткой?"
    show Psi Normal
    "Сьюзан" "Пожалуйста, [gg], я всего лишь пытаюсь быть дружелюбной."
    show GG Normal
    "[gg]" "Хорошо. От кружки чая, пожалуй, я не откажусь."
    show Psi Normal
    "Сьюзан" "Тогда добро пожаловать в мой кабинет. "

    show Psi:
        xzoom -1

        easein_cubic 2 xalign 1.5
    
    show GG:
        easein_cubic 3 xalign 1.5
    $ renpy.pause(1.5, hard = True)

    scene black
    with Dissolve(.4)

    $ renpy.pause(.5, hard = True)
    #"ext" "Psi_1"


    scene christie_root_65_tea 0
    show GG Invis
    show GG Invis:
        xalign .1
    
    show Psi Invis
    show Psi Invis:
        xalign .9
    with my_dissolve

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    #"ext" "//Psi_Tea"
    "[gg]" "Буду с вами откровенным, Сьюзен, я нахожусь здесь только по просьбе Кристи."
    "[gg]" "Я не хочу вам помогать, и я не стану вам помогать."
    "[gg]" "Поэтому всё, чтобы вы не сказали, или не пытались сделать…"
    "[gg]" "Я отвечу заранее – нет, нет, и ещё раз нет."
    "Сьюзен" "Понимаю."
    "Сьюзен" "Я поступила опрометчиво в прошлую нашу встречу."

    show christie_root_65_tea 1
    with my_dissolve
    "[gg]" "Да, вы раскрылись в полной мере."
    "[gg]" "Вы хитрая, расчётливая и эгоистичная…"
    "[gg]" "…"
    "Сьюзен" "Продолжай."
    "[gg]" "Сучка."

    show christie_root_65_tea 0
    with my_dissolve
    "Сьюзен" "Ну вот теперь, наконец, мы можем быть откровенными друг с другом. "
    "[gg]" "Давно пора."
    "Сьюзен" "Прежде чем протестовать, [gg], сперва выслушай. "
    "[gg]" "Мне понадобится всё моё терпение. "
    "Сьюзен" "…."
    "Сьюзен" "Видео, которое ты мне предоставил, очень многое меняет."
    "Сьюзен" "Что бы ты про меня не думал, я не собиралась разводиться с мужем из корыстных целей. "
    "Сьюзен" "Да, мне было очень обидно потерять его любовь и преданность, но я-то всё равно люблю его…"
    "Сьюзен" "Так вот, видео, на котором он… ну ты видел…."
    

    show christie_root_65_tea 1
    with my_dissolve
    "[gg]" "Мастурбирует, пока какой-то хрыч трахает «шоколадку». "
    "Сьюзен" "Да…"
    "Сьюзен" "Это натолкнуло меня на мысль, что мой муж тоже всё ещё любит меня."
    "[gg]" "Да ну?.."
    
    show christie_root_65_tea 0
    with my_dissolve
    "Сьюзен" "Возможно, конечно, он изменял мне и прочими способами."
    "Сьюзен" "Но данный эпизод явно демонстрирует обиду мужа на тот «тройничок», который состоялся не в его пользу."
    "Сьюзен" "Что-то сломалось у него внутри."
    "Сьюзен" "И теперь ему сложно воспринимать меня в качестве сексуального объекта, если роль исполнителя супружеских обязанностей лежит на нём самом."
    "[gg]" "…"
    "Сьюзен" "Я думаю…"
    "Сьюзен" "Нет, я уверена – любовь мужа ко мне простилается через секс с другим мужчиной."
    "Сьюзен" "И эту самую участь, для сохранения моего брака, я хочу предложить тебе, [gg]."
    
    show christie_root_65_tea 1
    with my_dissolve
    "[gg]" "Пффффффф…."
    "[gg]" "Нет уж, спасибо."
    "[gg]" "Я ещё хочу пожить. "
    "Сьюзен" "Это абсолютно безопасно. Уверяю тебя!"
    "Сьюзен" "Мой муж сам этого хочет!"
    "[gg]" "Хочет, чтобы я трахнул вас?!"
    "Сьюзен" "Ну… Он, конечно, не говорил об этом прямо, но я в этом совершенно уверена. "
    "[gg]" "Ах, уверены…"
    
    show christie_root_65_tea 0
    with my_dissolve
    "Сьюзен" "Можешь на меня в этом положиться. "
    "Сьюзен" "Я знаю своего мужа. "
    "Сьюзен" "Ему просто не хватает смелости сознаться в этом."
    "[gg]" "Почему вы сами с ним об этом не поговорите?"
    "Сьюзен" "О нет. Он слишком гордый. "
    "[gg]" "Я тоже гордый, знаете ли. Поэтому отказываюсь участвовать в самоубийственной операции по «куколдизации» вашего мужа. "
    "Сьюзен" "Проси всё, что хочешь, [gg]! Я исполню любое желание, даже больше."
    "Сьюзен" "Секс? "
    "Сьюзен" "Унижение? "
    "Сьюзен" "Деньги? "
    "Сьюзен" "Ты же мужчина – только скажи, и я сделаю!"
    show christie_root_65_tea 1
    with my_dissolve
    "[gg]" "Чёрт… Сьюзен, вы совсем чокнулись!!!"
    "[gg]" "Я уже дал свой ответ. "
    "[gg]" "И мне, пожалуй, пора идти."
    "Сьюзен" "Что ж… "
    "Сьюзен" "Значит, у меня нет выбора."


    "[gg]" "Ага."
    "[gg]" "Прощайте."
    show christie_root_65_tea 0
    with my_dissolve
    "Сьюзен" "Никуда ты не уйдёшь, [gg]."
    "[gg]" "Вы угрожаете мне? Достанете оружие и будете тыкать мне в лицо?"
    "Сьюзен" "Нет, милый. Я же женщина. А женщина действует более элегантным способом."
    "[gg]" "Охх…"
    
    show christie_root_65_tea 2
    with my_dissolve
    "[gg]" "Меня что-то укачало. "
    "Сьюзен" "Мой чай."
    "Сьюзен" "Я подложила туда снотворное. "
    "[gg]" "Суууукаааа….."
    "[gg]" "….."
    scene image '#000'
    with my_vpunch
    #"ext" "//Экран темнеет"
    #"ext" "Какое-то время спустя"
    $ from_say_screen = False

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    $ renpy.pause(.75, hard = True)
    show image Text(__("Какое-то время спустя"), size = 54, bold = True):
        align (.5, .5)
    #"ext" "//Так же тёмный экран"
    show GG Invis
    show GG Invis:
        xalign .5
    with my_dissolve
    "[gg]" "Где я?..."
    scene image '#000'
    show GG Invis
    show GG Invis:
        xalign .5
    with my_dissolve
    "[gg]" "Я чувствую себя странно. "
    "[gg]" "Почему я не могу открыть глаза?.."
    "[gg]" "Кто-нибудь!.."
    show Psi Invis
    show Psi Invis:
        xalign .85
    with my_dissolve
    "Сьюзен" "Расслабься, [gg]."
    "Сьюзен" "Сейчас я сниму повязку. "
    scene image 'cg/ep10/susan_scene/start/bg.png'
    show image 'cg/ep10/susan_scene/start/shine.png':
        alpha .0

    show image '#000'
    show image 'cg/ep10/susan_scene/start/shadow.png'

    $ renpy.pause(.1, hard = True)
    show image '#000':
        alpha .3
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    show image '#000':
        alpha 1.0
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    show image '#000':
        alpha .3
    with my_dissolve
    $ renpy.pause(.5, hard = True)
    show image '#000':
        alpha 1.0
    with my_dissolve
    $ renpy.pause(1.5, hard = True)
    show image '#000':
        alpha .2
    with my_dissolve
    $ renpy.pause(1.0, hard = True)

    # show image '#000':
    #     alpha 1.0
    # with my_dissolve
    # $ renpy.pause(1.0, hard = True)
    # show image '#000':
    #     alpha .3
    # with my_dissolve
    # $ renpy.pause(1.0, hard = True)
    show image 'cg/ep10/susan_scene/start/shadow.png':
        easein_cubic .5 alpha 0.0
    show image '#000':
        easein_cubic .5 alpha 0.0
    
    # with my_dissolve
    # $ renpy.pause(1.5, hard = True)

    # scene image 'cg/ep10/susan_scene/start/bg.png'
    show image 'cg/ep10/susan_scene/start/shine.png':
        alpha 0.0
        easein_cubic .5 alpha 1.0

        easeout_cubic .5 alpha 0.0
        easein_cubic .5 alpha 1.0
        easeout_cubic .5 alpha 0.0

    #with my
    #"ext" "//GG_Bed_Psi"
    #"ext" "// г прикован к кровати"

    show GG Invis
    show GG Invis:
        xalign .5
    
    
    "[gg]" "Какого лешего?!!"
    show image 'cg/ep10/susan_scene/start/bg_2.png'

    with my_dissolve

    "[gg]" "Почему я привязан к кровати?!!"
    "[gg]" "Кто-нибудь!!! Спасите! Помогите!"

    #show image '#000':
    #    easein .3 alpha 1.0

    #$ renpy.pause(.35, hard = True)
    #scene image '#000'
    #$ renpy.pause(.1)
    scene image 'cg/ep10/susan_scene/continue/bg.png'
    show image 'cg/ep10/susan_scene/continue/psi_1.png'
    if preferences.language in (None, 'eng', 'rus'):
        show image comic_frame_v2_master:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0
        with my_dissolve
        

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Прошу, не кричи так громко. "),

            ), 
            size   = 50,
            plus_y = 55,
           #line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
            
        ) from _call_comic_frame_v2_label_362 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Иначе мне придётся"),
            __("залепить твой рот"),
            __("{size=65}скотчем{/size}")

            ), 
            size   = 50,
            #plus_y = 55,
           #line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
            
        ) from _call_comic_frame_v2_label_363 


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

            __("А я вовсе не хочу"),
            __("лишать себя твоего"),
            __("нежного придыхания")
            ), 
            size   = 50,
            #plus_y = 55,
           #line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
            
        ) from _call_comic_frame_v2_label_364 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Да пошла ты нахрен,"),
            __("больная дура!")

            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 200],
         show_label = "christie_root_65_gg_talk_shake",        
        ) from _call_comic_frame_v2_label_365 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Отпусти меня,"),
            __("{size=65}сейчас же!{/size}")

            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 200],
         show_label = "christie_root_65_gg_talk_shake",        
        ) from _call_comic_frame_v2_label_366 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

            __("С минуты на минуту"),
            __("явится муж с работы."),
            ), 
            size   = 50,
            #plus_y = 55,
           #line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_psi_talk_1",
            
        ) from _call_comic_frame_v2_label_367 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

            __("Он застанет нас"),
            __("{size=65}в самом разгаре...{/size}")
            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_psi_talk_1",
            
        ) from _call_comic_frame_v2_label_368 
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

            __("И, наверняка обрадуется, видя,"),
            __("как его сексуальные фантазии"),
            __("материализуются, и вновь"),
            __("{size=65}{color=#FF0833}{i}полюбит{/i}{/color} меня.{/size}")
            ), 
            size   = 40,
            plus_y = 20,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_psi_talk_1",
            
        ) from _call_comic_frame_v2_label_369 
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Ты больная,"),
            __("просто {size=65}больная{/size} сука!")

            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 200],
         show_label = "christie_root_65_gg_talk_shake",        
        ) from _call_comic_frame_v2_label_370 
        show image 'cg/ep10/susan_scene/start/shadow.png':
            alpha 0.0
            easein_cubic .5 alpha 0.6


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

            __("{i}Тсссс{/i}, милый."),
            __("Сейчас тебе будет"),
            __("{size=65}очень хорошо.{/size}"),
            
            ), 
            size   = 40,
            plus_y = 20,
            line_spasing = 5, 
            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_psi_talk_1",
            
        ) from _call_comic_frame_v2_label_371 

        # show image 'cg/ep10/susan_scene/start/shine.png':
        #     alpha 0.0
        #     easein_cubic .5 alpha 1.0

        #     easeout_cubic .5 alpha 0.0
        #     easein_cubic .5 alpha 1.0
        #     easeout_cubic .5 alpha 0.0

        # $ renpy.pause(1.6, hard = True)
    else:

        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve

        "Сьюзен" "Прошу, не кричи так громко. "
        "Сьюзен" "Иначе мне придётся залепить твой рот скотчем, а я вовсе не хочу лишать тебя нежного придыхания. "
        "[gg]" "Да пошла ты нахрен, больная дура!"
        "[gg]" "Отпусти меня, сейчас же."
        "Сьюзен" "С минуты на минуту явиться муж с работы."
        "Сьюзен" "Он застанет нас в самом разгаре. "
        "Сьюзен" "И наверняка обрадуется, видя, как его сексуальные фантазии материализуются, и вновь полюбит меня. "
        "[gg]" "Ты больная, просто больная сука!"
        show image 'cg/ep10/susan_scene/start/shadow.png':
            alpha 0.0
            easein_cubic .5 alpha 0.6

        "Сьюзен" "Тсссс, милый. Сейчас тебе будет очень хорошо."
    show image 'cg/ep10/susan_scene/start/shadow.png':
        #alpha 0.0
        easeout_cubic .5 alpha 1.0
    show image '#000':
        alpha 0.0
        easeout_cubic .5 alpha 1.0
    $ renpy.pause(1.0, hard = True)
    scene image 'cg/ep10/susan_scene/continue/sex_1/bg.png'
    show christie_root_65_sex 0_1
    show image 'cg/ep10/susan_scene/continue/sex_1/1.png':
        alpha 0.0
        #easein 2.0 alpha 0.0
    show image 'cg/ep10/susan_scene/continue/sex_1/gg.png'
    if preferences.language in (None, 'eng', 'rus'):
        show image comic_frame_v2_master:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0
        #with my_dissolve
        with my_dissolve
        #"ext" "Psi_Sex_GG_1"
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            " ",
            "  …?!!  ",
            " ",


            ), 
            size =  70,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", yzoom = -1, xzoom = -1),
            say_pos = ["u", 100],
         show_label = "christie_root_65_gg_talk_shake_2",        
        ) from _call_comic_frame_v2_label_372 


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Ха! Только не"),
            __("говори, что не"),
            __("грезил об этом с"),
            __("момента нашей"),
            __("первой встречи.")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", yzoom = -1),
            say_pos = ["u", 300],
         show_label = "christie_root_65_psi_talk_2",        
        ) from _call_comic_frame_v2_label_373 


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("А уж как ты"),
            __("подсматривал за мной"),
            __("{size=100}В окно…{/size}"),



            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", yzoom = -1),
            say_pos = ["u", 300],
         show_label = "christie_root_65_psi_talk_2",        
        ) from _call_comic_frame_v2_label_374 




        show christie_root_65_sex 0_2
        with my_dissolve

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Твой член"),
            __("давно"),
            __("норовит"),
            __("облизать"),
            __("мою"),
            __("{size=60}{i}киску{/i}…{/size}")


            ), 
            size   = 40,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4"),
            say_pos = ["r", 290],
         show_label = "christie_root_65_psi_talk_3",        
        ) from _call_comic_frame_v2_label_375 





        #"ext" "Psi_Sex_GG_2"
        #"ext" "//Скорость х1"

        #"[gg]" 
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Как только"),
            __("я получу свободу,"),
            __("тебе не"),
            __("поздоровится!")


            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", yzoom = -1, xzoom = -1),
            say_pos = ["u", 100],
         show_label = "christie_root_65_gg_talk_shake_2",        
        ) from _call_comic_frame_v2_label_376 
        $ store._st_65_y = 180
        $ store._st_65_t = 0.0
        #play ero 'audio/sex_susan.mp3'


        show christie_root_65_sex 1_1
        with my_dissolve
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("К тому моменту,"),
            __("как это случится..."),
            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_4",   
      #   hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_377   
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve

        "[gg]" "…?!!"
        "Сьюзен" "Ха! Только не говори, что не грезил об этом с момента нашей первой встречи."
        "Сьюзен" "А уж как ты подсматривал за мной в окно…"


        show christie_root_65_sex 0_2
        with my_dissolve
        "Сьюзен" "Твой член давно норовит облизать мою киску. "
        "[gg]" "Как только я получу свободу, тебе не поздоровится."

        show christie_root_65_sex 1_1
        with my_dissolve
        "Сьюзен" "К тому моменту, как это случится, ты будешь умолять меня о продолжении, милый. "

label christie_root_65_jump:
    
    # if renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master").ypos > 182:
    #     $ renpy.pause(.01, hard = True)
    #     $ renpy.jump('christie_root_65_jump')
    if preferences.language in (None, 'eng', 'rus'):
        $ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = _st_65.ypos
        $ store._st_65_t = 1.36 - 1.36*(_st_65.st/1.36 - _st_65.st//1.36)
        

        #"" "[rd]"
    #        $ renpy.pause(.01, hard = True)
    #        $ renpy.jump('christie_root_65_jump')
        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            # __("К тому моменту,"),
            # __("как это случится..."),
            __("...ты будешь умолять"),
            __("меня о продолжении,"),
            __("{size=100}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_4", 

         hide_label = "christie_root_65_psi_talk_4_hide",  
         ) from _call_comic_frame_v2_label_378     
    #     ) 
    #     $ store.comic_frame_v2_master = comic_frame_v2_say(text_list =(
            
    #         #_generate_text("Уффф...", size = 60), 
    #         # __("К тому моменту,"),
    #         # __("как это случится..."),
    #         __("...ты будешь умолять"),
    #         __("меня о продолжении,"),
    #         __("{size=60}милый.{/size}")


    #         ),  kerning = 6, size = 50, outlines = [(2, "#000a", 0, 0),], font = "fonts/mango_comics_er.ttf", 
    # say_image = Transform("comic_frame_say_4", xzoom = -1.0), plus_y = 20, say_pos = ["l", 90], line_spasing = 10, minimum_size_y = 128.0,)


    #     "COMIC_TEST" "COMIC_TEST"

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            " ",
            __(" Уффф!.. "),
            " ",


            ), 
            size =  70,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", yzoom = -1, xzoom = -1),
            say_pos = ["u", 100],
         show_label = "christie_root_65_gg_talk_shake_2",        
        ) from _call_comic_frame_v2_label_379 

        show shadow_full:
            alpha .0
            easein .5 alpha .7


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Сложно отрицать{/i}"),
            __("{i}моё влечение{/i}"),
            __("{size=90}{i}к ней.{/i}{/size}"),


            ), 
            size =  70,
            plus_y = 20,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_380 
        show image 'cg/ep10/susan_scene/continue/sex_1/1.png':
            alpha 1.0
            easein 1.0 alpha 0.0
        show christie_root_65_sex 1_2
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Её изгибы...{/i}"),


            


            ), 
            size =  70,
            plus_y = 32,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 200],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_381 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Шикарная задница...{/i}"),


            


            ), 
            size =  70,
            plus_y = 32,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_382 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Мокрая от{/i}"),
            __("{i}возбуждения киска...{/i}")

            


            ), 
            size =  70,
            plus_y = 25,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_383 
              

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}и дерзкая поза{/i}"),
            __("{i}наездницы...{/i}")

            


            ), 
            size =  70,
            plus_y = 32,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_384 

            
            
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

            
            __("{i}Этому невозможно{/i}"),
            __("{i}противиться.{/i}"),
            ), 
            size =  70,
            plus_y = 32,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_385 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

            
            __("{i}Отказываться от секса{/i}"),
            __("{i}с такой женщиной{/i}"),
            __("{size=90}{i}преступление.{/i}{/size}")
            ), 
            size =  50,
            plus_y = 32,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_386 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

            
            __("{i}Но и соглашаться{/i}"),
            __("{i}на это тоже{/i}"),
            __("{size=90}{i}нельзя!{/i}{/size}")
            ), 
            size =  50,
            plus_y = 32,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_387 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

            
            __("{i}Да, внутри неё{/i}"),
            __("{i}настоящее{/i}"),
            __("{size=90}{i}блаженство.{/i}{/size}")
            ), 
            size =  50,
            plus_y = 32,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_388 


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

            
            __("{i}Прикованные к кровати{/i}"),
            __("{i}руки напряжены до{/i}"),
            __("{size=90}{i}предела!{/i}{/size}")
            ), 
            size =  50,
            plus_y = 32,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_389 


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

            
            __("{i}Что есть мочи,{/i}"),
            __("{i}я пытаюсь{/i}"),
            __("{size=90}{i}вырваться…{/i}{/size}")
            ), 
            size =  50,
            plus_y = 32,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_390 


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

            
            __("{i}Но не для того,{/i}"),
            __("{i}чтобы сбежать...{/i}"),

            ), 
            size =  50,
            plus_y = 32,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_391 


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

     
            __("{i}а для того, чтобы{/i}"),
            __("{i}схватить её за бёдра{/i}"),
            __("{i}и трахать ещё{/i}"),
            __("{size=90}{i}яростней!{/i}{/size}")
            ), 
            size =  50,
            plus_y = 32,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_392 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 

            __("{i}Здравый смысл{/i}"),
            __("{i}покидает{/i}"),
            __("{size=90}{i}меня…{/i}{/size}")
            ), 
            size =  50,
            plus_y = 32,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 200],
         show_label = "christie_root_65_gg_talk_1",        
        ) from _call_comic_frame_v2_label_393 



       
        #"ext" "// Конец Мысли"
        #"ext" "//Скорость х2"

        show image comic_frame_v2_master:    
            easein .2 ypos 700 alpha 0.0
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "[gg]" "Уффф!..."


        show shadow_full:
            alpha .0
            easein .5 alpha .7
        "[gg]" "{i}Сложно отрицать моё влечение к ней.{/i}"
        "[gg]" "{i}Её изгибы, шикарная задница, мокрая от возбуждения киска и дерзкая поза наездницы… Этому невозможно противиться.{/i}"
        "[gg]" "{i}Отказываться от секса с такой женщиной – преступление.{/i}"
        "[gg]" "{i}Но и соглашаться на это тоже нельзя!{/i}"
        "[gg]" "{i}Да, внутри неё настоящее блаженство.{/i}"
        "[gg]" "{i}Прикованные к кровати руки напряжены до предела!{/i}"
        "[gg]" "{i}Xто есть мочи я пытаюсь вырваться…{/i}"
        "[gg]" "{i}Но не для того, чтобы сбежать, а для того, чтобы схватить её за бёдра и трахать ещё яростней.{/i}"
        "[gg]" "{i}Здравый смысл покидает меня…"
    show shadow_full:
        easein .2 alpha .0
    $ renpy.pause(.1, hard = True)

    menu christie_root_65_change_pose_1:
        "Сменить позу":
            $ pass
        "Продолжить в той же позе":
            window hide
            $ renpy.pause(9999)
            jump christie_root_65_change_pose_1
    scene image '#000'
    with Dissolve(.3)
    $ renpy.pause(.4, hard = True)

    #$ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
    $ store._st_65_y = 20
    $ store._st_65_t = 0.0 #1.36 - 1.36*(_st_65.st/1.36 - _st_65.st//1.36)
    
    scene image 'cg/ep10/susan_scene/continue/sex_2/bg.png'
    show image 'cg/ep10/susan_scene/continue/sex_1/1.png':
        alpha 0.0
        #easein 2.0 alpha 0.0
    show christie_root_65_sex 2_2
    show image 'cg/ep10/susan_scene/continue/sex_1/gg.png':
        alpha .0
    if preferences.language in (None, 'eng', 'rus'):
        show image comic_frame_v2_master:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0
        with my_dissolve
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            " ",
            __("Оууууу!..."),
            " ",
            # __("Кажется, твой член"),
            # __("предал тебя,"),
            # __("[gg].")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_5",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_394   
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Оууууу!..."

label christie_root_65_jump_2:
    #$ store.dlddr = 
    #$ renpy.restart_interaction()
    # if renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master").ypos > 22:
    #     $ renpy.pause(.01, hard = True)
    #     $ renpy.jump('christie_root_65_jump_2')
    if preferences.language in (None, 'eng', 'rus'):
        $ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = _st_65.ypos
        $ store._st_65_t = 1.933 - 1.933*(_st_65.st/1.933 - _st_65.st//1.933)
        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            

            __("Кажется, твой член"),
            __("предал тебя,"),
            "[gg]."

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_5",   
      #   hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_395   
        $ christie_root_65_tmp = Composite((700, 180), 
            #(0, 0), Solid("#000"),
            (0, 0), Frame(Transform('interface/comic_v2/bg_frame_2.png', alpha = .8), Borders(64, 64, 64, 64)),
            (40, 58), Text(
                            __("Отвали, извращенка!"), 
                            kerning  = 5,
                            size     = 50,
                            outlines = [(2, "#000a", 0, 0),],
                            font = "fonts/mango_comics_er.ttf",
                            
                            ),
            (1020, 60), Transform("comic_frame_say_2", yzoom = -1, xzoom = -1)
            )
        show image christie_root_65_tmp:
            zoom .5
            xpos 100
            ypos 450
            xanchor 0.0
            yanchor 0.0
            alpha .0
            parallel:
                easein 0.1 ypos 456
                easein 0.1 ypos 450
                easein 0.1 ypos 456
                easein 0.1 ypos 450
                
            parallel:
                ease .1 alpha 1.0
        $ renpy.pause(.2, hard = True)
        $ renpy.pause(99999)
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Кажется, твой член предал тебя, [gg]."
        "[gg]" "Отвали, извращенка!"

label christie_root_65_jump_3:
    
    # if renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master").ypos > 22:
    #     $ renpy.pause(.01, hard = True)
    #     $ renpy.jump('christie_root_65_jump_3')
    if preferences.language in (None, 'eng', 'rus'):
        $ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = _st_65.ypos
        $ store._st_65_t = 1.933 - 1.933*(_st_65.st/1.933 - _st_65.st//1.933)
        
        hide image christie_root_65_tmp
        with my_dissolve
        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            

            __("Ха-ха-ха!"),
            __("Как нелепо ты отыгрываешь "),
            __("«отрицание».")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_5",   
        hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_396   
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Ха-ха-ха!"
        "Сьюзен" "Как нелепо ты отыгрываешь роль «отрицания»."
    python:
        try:
            del christie_root_65_tmp
        except:
            pass

label christie_root_65_jump_4:
    
    # if renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master").ypos > 22:
    #     $ renpy.pause(.01, hard = True)
    #     $ renpy.jump('christie_root_65_jump_4')
    if preferences.language in (None, 'eng', 'rus'):
        $ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = _st_65.ypos
        $ store._st_65_t = 1.933 - 1.933*(_st_65.st/1.933 - _st_65.st//1.933)
        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            

            __("Но в этом нет"),
            __("никакого смысла,"),
            __("{size=90}милый.{/size}")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_5",   
        hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_397 
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Но в этом нет никакого смысла, милый. " 

label christie_root_65_jump_5:
    # if renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master").ypos > 22:
    #     $ renpy.pause(.01, hard = True)
    #     $ renpy.jump('christie_root_65_jump_5')
    if preferences.language in (None, 'eng', 'rus'):
        $ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = _st_65.ypos
        $ store._st_65_t = 1.933 - 1.933*(_st_65.st/1.933 - _st_65.st//1.933)
        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            

            __("Вот-вот явится"),
            __("мой муж, и твои слова"),
            __("потеряют всякий смысл.")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_5",   
        hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_398  
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Вот-вот явится мой муж, и твои слова потеряют всякий смысл."


label christie_root_65_jump_6:
    # if renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master").ypos > 22:
    #     $ renpy.pause(.01, hard = True)
    #     $ renpy.jump('christie_root_65_jump_6')
    if preferences.language in (None, 'eng', 'rus'):
        $ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = _st_65.ypos
        $ store._st_65_t = 1.933 - 1.933*(_st_65.st/1.933 - _st_65.st//1.933)
        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            

            __("Просто получай"),
            __("{size=80}удовольствие!{/size}"),
            __("{size=65}Наслаждайся!{/size}")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_5",   
        hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_399  
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Просто получай удовольствие! Наслаждайся!"


label christie_root_65_jump_7:
    # if renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master").ypos > 22:
    #     $ renpy.pause(.01, hard = True)
    #     $ renpy.jump('christie_root_65_jump_7')
    if preferences.language in (None, 'eng', 'rus'):
        $ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = _st_65.ypos
        $ store._st_65_t = 1.933 - 1.933*(_st_65.st/1.933 - _st_65.st//1.933)
        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            

            __("Твоё тело буквально"),
            __("{size=65}пищит{/size} от восторга, дрожа"),
            __("{size=65}и дёргаясь{/size}"),
            __("в такт моим движениям.")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_5",   
        #hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_400
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Твоё тело буквально пищит от восторга, дрожа и дёргаясь в такт с моими движениями. "
    show christie_root_65_sex 1_3
    show image 'cg/ep10/susan_scene/continue/sex_1/gg.png':
        alpha 1.0
    show shadow_full:
        alpha .7

    with my_dissolve
    if preferences.language in (None, 'eng', 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            

            __("Высокомерная"),
            __("сучка!")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",   
     #   hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_401  



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            

            __("Нетрудно управлять"),
            __("членом мужчины, когда"),
            __("он скован по рукам"),
            __("и ногам!")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 40,
            plus_y = 20,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",   
     #   hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_402  


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            "{size=10} {/size}",
            __("Оххх… "),
            "{size=10} {/size}",

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 70,
            plus_y = 20,
            line_spasing = -5, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 100],
         show_label = "christie_root_65_gg_talk_1",   
     #   hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_403  


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            

            __("Стоит признать, утопать"),
            __("членом в её киске"),
            __("на редкость приятно."),
            

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 45,
            plus_y = 20,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",   
     #   hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_404  

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            

            __("Но мне нельзя"),
            __("обманываться!"),
            

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",   
     #   hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_405  

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            

            __("Полицейский пристрелит"),
            __("меня как собаку,"),
            __("если застанет нас.")
            

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 40,
            plus_y = 20,
            line_spasing = 10, 
            say_image = 'comic_frame_say_9_2',
            say_pos = ["u", 400],
         show_label = "christie_root_65_gg_talk_1",   
     #   hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_406  
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "[gg]" "{i}Высокомерная сучка!{/i}"
        "[gg]" "{i}Не трудно управлять членом мужчины, когда он скован по рукам и ногам!{/i}"
        "[gg]" "{i}Оххх… {/i}"
        "[gg]" "{i}Стоит признать, утопать членом в её киске на редкость приятно. {/i}"
        "[gg]" "{i}Но мне нельзя обманываться!{/i}"
        "[gg]" "{i}Полицейский пристрелит меня как собаку, если застанет нас.{/i}"
    show shadow_full:
        easein .2 alpha .0
    if preferences.language in (None, 'eng', 'rus'):
        show image comic_frame_v2_master:    
            easein .2 ypos 600 alpha 0.0

        $ renpy.pause(.1, hard = True)
        #$ store._st_65   = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = 20# _st_65.ypos
        $ store._st_65_t = 0.0 #1.33 - 1.33*(_st_65.st/1.33 - _st_65.st//1.33)
    
    menu christie_root_65_speed_up_1:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_root_65_speed_up_1

    show christie_root_65_sex 2_3
    show image 'cg/ep10/susan_scene/continue/sex_1/gg.png':
        alpha 0.0
    with my_dissolve
    if preferences.language in (None, 'eng', 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("О даааа,"),
            __("твой член"),
            __("разгорячился"),
            __("не на шутку!")
            # __("Кажется, твой член"),
            # __("предал тебя,"),
            # __("[gg].")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_407 
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "О даааа, твой член разгорячился не на шутку!"  
    #"ext" "// Конец Мысли"
    #"ext" "//Скорость х3"

label christie_root_65_jump_8:
    # if renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master").ypos > 22:
    #     $ renpy.pause(.01, hard = True)
    #     $ renpy.jump('christie_root_65_jump_8')
    if preferences.language in (None, 'eng', 'rus'):
        $ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = _st_65.ypos
        $ store._st_65_t = 1.33 - 1.33*(_st_65.st/1.33 - _st_65.st//1.33)

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Давай, трахай меня"),
            __("как можно сильнее!"),

            # __("Кажется, твой член"),
            # __("предал тебя,"),
            # __("[gg].")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_408   
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Давай, трахай меня как можно сильнее!"
label christie_root_65_jump_9:
    # if renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master").ypos > 22:
    #     $ renpy.pause(.01, hard = True)
    #     $ renpy.jump('christie_root_65_jump_9')
    if preferences.language in (None, 'eng', 'rus'):
        $ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = _st_65.ypos
        $ store._st_65_t = 1.33 - 1.33*(_st_65.st/1.33 - _st_65.st//1.33)

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Я хочу больше страсти,"),
            __("больше экспрессии."),
            __("Мой муж должен видеть"),
            __("эту сцену в самом разгаре!")

            # __("Кажется, твой член"),
            # __("предал тебя,"),
            # __("[gg].")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_409   
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Я хочу больше страсти, больше экспрессии. Мой муж должен видеть эту сцену в самом разгаре!"
label christie_root_65_jump_10:
    # if renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master").ypos > 22:
    #     $ renpy.pause(.01, hard = True)
    #     $ renpy.jump('christie_root_65_jump_10')
        
    if preferences.language in (None, 'eng', 'rus'):
        $ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = _st_65.ypos
        $ store._st_65_t = 1.33 - 1.33*(_st_65.st/1.33 - _st_65.st//1.33)

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Он должен испытать тоже"),
            __("чувство радости, что и я,"),
            
            __("пока прыгаю на твоём члене,"),
            __("[gg]!")

            # __("Кажется, твой член"),
            # __("предал тебя,"),
            # __("[gg].")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_410
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Он должен испытать тоже чувство радости, что и я, пока прыгаю на твоём члене, [gg]."
label christie_root_65_jump_11:
    # if renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master").ypos > 22:
    #     $ renpy.pause(.01, hard = True)
    #     $ renpy.jump('christie_root_65_jump_11')
    if preferences.language in (None, 'eng', 'rus'):
        $ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = _st_65.ypos
        $ store._st_65_t = 1.33 - 1.33*(_st_65.st/1.33 - _st_65.st//1.33)

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Не подведи"),
            __("меня,"),
            __("милый!"),

            # __("Кажется, твой член"),
            # __("предал тебя,"),
            # __("[gg].")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 70,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_411   
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Не подведи меня, милый. "
label christie_root_65_jump_12:
    # if renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master").ypos > 22:
    #     $ renpy.pause(.01, hard = True)
    #     $ renpy.jump('christie_root_65_jump_12')
    if preferences.language in (None, 'eng', 'rus'):        
        $ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = _st_65.ypos
        $ store._st_65_t = 1.33 - 1.33*(_st_65.st/1.33 - _st_65.st//1.33)

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Ахххх!"),
            __("{size=90}Аххх…!!!!{/size}"),
            __("Охххх!!!"),

            # __("Кажется, твой член"),
            # __("предал тебя,"),
            # __("[gg].")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_412   
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Ахххх! Аххх…!!!! Охххх!!!"


label christie_root_65_jump_13:
    # if renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master").ypos > 22:
    #     $ renpy.pause(.01, hard = True)
    #     $ renpy.jump('christie_root_65_jump_13')
    if preferences.language in (None, 'eng', 'rus'):
        $ store._st_65 = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ store._st_65_y = _st_65.ypos
        $ store._st_65_t = 1.33 - 1.33*(_st_65.st/1.33 - _st_65.st//1.33)

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Да, быстрее,"),
            __("{size=90}ещё быстрее!{/size}"),
            

            # __("Кажется, твой член"),
            # __("предал тебя,"),
            # __("[gg].")

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_413   
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Да, быстрее, ещё быстрее. "
    scene image '#fff'
    with Dissolve(.75)

    stop ero fadeout 1.0
    $ renpy.pause(1.3, hard = True)
    scene image 'cg/ep10/susan_scene/continue/bg_2.png'
    show image 'cg/ep10/susan_scene/continue/psi_2.png'

    show Officer Angry
    show Officer Angry at go_from_left(xxalign = .1)
    with my_vpunch
    #"ext" "//Off_1"
    #"ext" "//Мент припёрся"
    "Офицер" "Какого хрена, Сьюзен?!!!"
    "Офицер" "Я думал тебя убивают, а Ты… а Он!!!..."
    show Officer Angry_Pistol
    with my_vpunch
    "Офицер" "Я убью вас обоих!!!"
    #"ext" "//Off_2"
    show image 'cg/ep10/susan_scene/continue/sex_2/bg.png':
        alpha 0.0
        easein .75 alpha 1.0
    show christie_root_65_sex 2_3:
        alpha 0.0
        easein .75 alpha 1.0
    show image comic_frame_v2_master:
        zoom .8
        xpos 950
        ypos 200
        xanchor 1.0
        yanchor .0
        alpha .0

    show image comic_frame_v2_slave:
        zoom .8
        xpos 950
        ypos 200
        xanchor 1.0
        yanchor .0
        alpha .0
    if preferences.language in (None, 'eng', 'rus'):
        call comic_frame_v2_label((
            
            __("Пожалуйста, любимый."),
            __("Взгляни внутрь себя!"),
            

            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_465 

        call comic_frame_v2_label((
            
            __("Я всё знаю!"),
            __("Это считывается"),
            __("на твоём"),
            __("{size=90}лице!{/size}")
            

            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_466 
        


        call comic_frame_v2_label((
            
            __("Ты не смог себя простить за то,"),
            __("что получал удовольствие"),
            __("от моего секса"),
            __("с {b}другим{/b} парнем.")
            

            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_467 




        call comic_frame_v2_label((
            
            __("Но ты закрылся."),
            __("Ушёл из моей жизни!"),
            

            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_468 


        call comic_frame_v2_label((
            
            __("А я люблю тебя,"),
            __("{size=90}дорогой,{/size}"),
            __("люблю так же сильно,"),
            __("как и прежде!")
            
            
            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_469 
        show image comic_frame_v2_slave:
            alpha 0.0
        show image comic_frame_v2_master:
            alpha 0.0
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Пожалуйста, любимый. Взгляни внутрь себя!"
        "Сьюзен" "Я всё знаю! Это считывается на твоём лице!"
        "Сьюзен" "Ты не смог себя простить за то, что получал удовольствие от моего секса с другим парнем."
        "Сьюзен" "Но ты закрылся. Ушёл из моей жизни!"
        "Сьюзен" "А я люблю тебя дорогой, люблю так же сильно, как и прежде!"

    show image 'cg/ep10/susan_scene/continue/sex_2/bg.png':
        alpha 0.0
    show christie_root_65_sex:
        alpha 0.0 
    with my_vpunch
    "Офицер" "Это враньё!.."
    show image 'cg/ep10/susan_scene/continue/sex_2/bg.png':
        alpha 1.0
    show christie_root_65_sex 2_3:
        alpha 1.0
    with my_dissolve
    if preferences.language in (None, 'eng', 'rus'):
        call comic_frame_v2_label((
            
            __("Ты сомневаешься!"),
            __("Ты всегда сомневаешься,"),
            __("дорогой!"),
            
            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_470

        call comic_frame_v2_label((
            
            __("Но взгляни на меня,"),
            __("взгляни на то, с каким"),
            __("чувством наслаждения"),
            __("меня трахает [gg]!")
            
            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_471 

        call comic_frame_v2_label((
            
            __("Это всё ради тебя,"),
            __("{size=90}любимый!{/size}"),
            

            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_472 


        call comic_frame_v2_label((
            
            __("Чтобы ты вновь"),
            __("испытал чувство влечения"),
            __("ко мне!")
            
            
            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_473 

        show image comic_frame_v2_slave:
            alpha 0.0
        show image comic_frame_v2_master:
            alpha 0.0
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Ты сомневаешься! Ты всегда сомневаешься, дорогой! "
        "Сьюзен" "Но взгляни на меня, взгляни на то, с каким чувством наслаждения меня трахает [gg]!"
        "Сьюзен" "Это всё ради тебя, любимый!"
        "Сьюзен" "Чтобы ты вновь испытал чувство влечения ко мне! "

    show image 'cg/ep10/susan_scene/continue/sex_2/bg.png':
        alpha 0.0
    show christie_root_65_sex:
        alpha 0.0
    with my_vpunch
    "Офицер" "Безумие…"
    "Офицер" "Ещё секунда и я прикончу вас обоих."
    #hide Psi
    show GG Invis
    show GG Invis:
        xalign .95
    with my_dissolve
    "[gg]" "Эй, офицер, вы мой должник! "
    "[gg]" "Я спас вашу жизнь! А может, и честь!"
    show Officer Angry
    with my_vpunch
    "Офицер" "Проклятье!"

    "Офицер" "Я ненавижу вас!"
    show Officer:
        xzoom -1
    show shadow_full:
        alpha .0
        easein .5 alpha .7
    "Офицер" "Ненавижу вас обоих!"
    #"ext" "//Скорость х4"
    #hide GG
    # show Psi Invis
    # show Psi Invis:
    #     xalign .75
    # with my_dissolve
    hide GG Invis
    show image 'cg/ep10/susan_scene/continue/sex_2/bg.png':
        alpha 1.0
    show christie_root_65_sex 2_3:
        alpha 1.0
    show shadow_full:
        alpha 0.0
    with my_dissolve

    if preferences.language in (None, 'eng', 'rus'):
        call comic_frame_v2_label((
            
            __("Оххх, дорогой!"),
            __("Аххх!..."),
            __("Не говори так.")
            
            
            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_474 

        call comic_frame_v2_label((
            
            __("Ещё немного,"),
            __("и я кончу!!!"),

            
            
            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_475 


        call comic_frame_v2_label((
            
            __("Отдайся на"),
            __("милость чувств!"),
            
            
            
            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_476 

        call comic_frame_v2_label((
            
            __("Будь искренним!"),
            __("Будь любимым!"),
            __("Будь со мной!"),
            
            
            
            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_6",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_477  

        #"ext" "//Off_3"
        show image comic_frame_v2_slave:
            alpha 0.0
        show image comic_frame_v2_master:
            alpha 0.0
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "Оххх, дорогой! Аххх!... Не говори так."
        "Сьюзен" "Ещё немного и я кончу!!!"
        "Сьюзен" "Отдайся на милость чувств!"
        "Сьюзен" "Будь искренним! "
        "Сьюзен" "Будь любимым! "
        "Сьюзен" "Будь со мной!"

    show image 'cg/ep10/susan_scene/continue/sex_2/bg.png':
        alpha 0.0
    show christie_root_65_sex:
        alpha 0.0
    
    with my_vpunch
    "Офицер" "Аргх…"
    

    "Офицер" "Кажется, я сейчас сам сойду с ума!"
    
    hide shadow_full

    show Officer Hm:
        xzoom 1
    with my_dissolve
    "Офицер" "Ладно…"
    show Officer Jerking:
        ypos 1115
    with my_dissolve
    "Офицер" "Я сделаю, как ты хочешь…"
    "Офицер" "Но потом я убью вас!"
    hide image comic_frame_v2_master
    hide image comic_frame_v2_slave
    show image 'cg/ep10/susan_scene/continue/sex_2/bg.png':
        alpha 1.0
    show christie_root_65_sex 1_3:
        alpha 1.0
    show image 'cg/ep10/susan_scene/continue/sex_1/gg.png':
        alpha 1.0
    if preferences.language in (None, 'eng', 'rus'):
        show image comic_frame_v2_master:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0
        with my_dissolve
        call comic_frame_v2_label((
            
            __("После - можешь делать"),
            __("с нами всё,"),
            __("что захочешь!.."),
            
            
            
            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_4", xzoom = -1.0, yzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_psi_talk_4",   
         hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_478  
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            

            __("Ау! Я на"),
            __("такое не"),
            __("подписывался!")
            

            # __("ты будешь умолять"),
            # __("меня о продолжении,"),
            # __("{size=60}милый.{/size}")


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 10, 
            say_image = Transform("comic_frame_say_2", yzoom = -1,),
            say_pos = ["u", 200],
         show_label = "christie_root_65_gg_talk_1",   
     #   hide_label = "christie_root_65_psi_talk_4_hide",
         ) from _call_comic_frame_v2_label_479 

        # hide Psi
        # show GG Invis
        # show GG Invis:
        #     xalign .75

        with my_vpunch

        #"ext" "//Harly_Kri_Fight"
        #"ext" "//Off_3"
        #"ext" "//Кристи в одежде Харли Квин бьёт битой офицера"
        #"ext" "//вздрагивание экрана и всё такое"
        #"ext" "//Harly_Kri"
        show image comic_frame_v2_slave:
            easein .5 alpha 0.0
        show image comic_frame_v2_master:
            easein .5 alpha 0.0
    else:
        show GG Invis
        show GG Invis:
            xalign .92
        show Psi Invis
        show Psi Invis:
            xalign .5
        with my_dissolve
        "Сьюзен" "После можешь делать с нами всё что захочешь!.."
        "[gg]" "Ау! Я на такое не подписывался!"
    hide shadow_full 
    with my_dissolve
   # play ero 'audio/sex_susan.mp3'
    
label christie_root_65_kick:
    menu:
        

        "Сменить позу (1)":
            scene image 'cg/ep10/susan_scene/continue/sex_1/bg.png'
            show image 'cg/ep10/susan_scene/continue/sex_1/1.png'
            show image 'cg/ep10/susan_scene/continue/sex_1/gg.png'
            with my_dissolve
            menu:
                "Скорость 1":
                    scene image 'cg/ep10/susan_scene/continue/sex_1/bg.png'
    
                    show image 'cg/ep10/susan_scene/continue/sex_1/1.png':
                        alpha 1.0
                        easein 2.0 alpha 0.0
                    show christie_root_65_sex 1_1
                    show image 'cg/ep10/susan_scene/continue/sex_1/gg.png'
                    #with my_dissolve
                    window hide
                    $ renpy.pause(9999)
                "Скорость 2":
                    scene image 'cg/ep10/susan_scene/continue/sex_1/bg.png'
                    show image 'cg/ep10/susan_scene/continue/sex_1/1.png':
                        alpha 1.0
                        easein 2.0 alpha 0.0
                    #with my_dissolve
                    show christie_root_65_sex 1_2

                    show image 'cg/ep10/susan_scene/continue/sex_1/gg.png'
                    window hide
                    $ renpy.pause(9999)
                "Скорость 3":
                    scene image 'cg/ep10/susan_scene/continue/sex_1/bg.png'
                    show image 'cg/ep10/susan_scene/continue/sex_1/1.png':
                        alpha 1.0
                        easein 2.0 alpha 0.0
                    show christie_root_65_sex 1_3

                    show image 'cg/ep10/susan_scene/continue/sex_1/gg.png'
                    #with my_dissolve
                    window hide
                    $ renpy.pause(9999)
                "Назад":
                    $ pass
            
            jump christie_root_65_kick
            

        "Сменить позу (2)":
            scene image 'cg/ep10/susan_scene/continue/sex_2/bg.png'
            show image 'cg/ep10/susan_scene/continue/sex_2/1.png'
            with my_dissolve
            menu:
                "Скорость 1":

                    scene image 'cg/ep10/susan_scene/continue/sex_2/bg.png'
                    show image 'cg/ep10/susan_scene/continue/sex_2/1.png':
                        alpha 1.0
                        easein 2.0 alpha 0.0
                    show christie_root_65_sex 2_1

                    #with my_dissolve
                    window hide
                    $ renpy.pause(9999)
                "Скорость 2":
                    scene image 'cg/ep10/susan_scene/continue/sex_2/bg.png'
                    show image 'cg/ep10/susan_scene/continue/sex_2/1.png':
                        alpha 1.0
                        easein 2.0 alpha 0.0
                    show christie_root_65_sex 2_2

                    #with my_dissolve
                    window hide
                    $ renpy.pause(9999)
                "Скорость 3":
                    scene image 'cg/ep10/susan_scene/continue/sex_2/bg.png'
                    show image 'cg/ep10/susan_scene/continue/sex_2/1.png':
                        alpha 1.0
                        easein 2.0 alpha 0.0
                    show christie_root_65_sex 2_3

                    #with my_dissolve
                    window hide
                    $ renpy.pause(9999)
                "Назад":
                    $ pass
            
            jump christie_root_65_kick

        
        
        "Кончить":
            pass
    
    # $ i = renpy.call_screen('circle_mini_game_screen', xp = 500, yp = 300, tm = 10)
    # if not i:
    #     jump christie_root_65_kick
    show image '#fff':
        alpha 0.0
        easein .5 alpha 1.0

    stop ero fadeout 1.0
    $ renpy.pause(.1, hard = True)
    $ renpy.play('audio/punch.mp3')
    $ renpy.pause(.65, hard = True)

    scene image 'cg/ep10/susan_scene/continue/bg_2.png'
    show image 'cg/ep10/susan_scene/continue/psi_2.png'
    show Christie Harly_Bat
    show Christie Harly_Bat:
        pos (250, 1080)
        easein 3.5 pos (350, 1080)     
    show christie_root_65_bat_sfx_1_1:
        pos (1100-600, 270) alpha 1.0
        parallel:
            easein 9.5 pos (1400-600, 270) 
        parallel:
            easein 3.5 alpha .1
    show christie_root_65_bat_sfx_1_2:
        pos (1100-600, 270)
        parallel:
            easein 6.0 pos (1400-600, 270) 
        parallel:
            easein 3.5 alpha .1
    show christie_root_65_bat_sfx_1_3:
        pos (1100-600, 270)
        easein 3.5 pos (1400-600, 270)
    
    show christie_root_65_bat_sfx_2:
        pos (1100-300, 170)
        easein 4.0 pos (1400-300, 70)

    show christie_root_65_bat_sfx_3:
        pos (1100-200, 170)
        easein 3.5 pos (1400-200, 70)


    show christie_root_65_bat_sfx_4:
        pos (1100-100, 170)
        easein 3.0 pos (1400-100, 70)
    
    show Officer Bited
    show Officer Bited:
        pos (100, 1300) rotate 0 anchor (0.0, 1.0)
        easein 2.0 pos (400, 1400) rotate 15
    show christie_root_65_hat_3:

        pos (1100, 200) alpha 1.0 rotate 30
        easein 2.7 pos (1400, 400) alpha .1 rotate 70
    show christie_root_65_hat_2:

        pos (1100, 200) alpha 1.0 rotate 30
        easein 2.3 pos (1400, 400) alpha .1 rotate 70
    show christie_root_65_hat_1:
        pos (1100, 200) rotate 30
        easein 1.9 pos (1400, 400) rotate 70
    with my_vpunch
    python:

        from_say_screen = False
        renpy.pause(1.75, hard = True)
        for i in (
            'Officer',
            'christie_root_65_hat_1',
            'christie_root_65_hat_2',
            'christie_root_65_hat_3',
            'christie_root_65_bat_sfx_1_1',
            'christie_root_65_bat_sfx_1_2',
            'christie_root_65_bat_sfx_1_3',
            'christie_root_65_bat_sfx_2',
            'christie_root_65_bat_sfx_3',
            'christie_root_65_bat_sfx_4'

            ):
            renpy.show(i, what = i, 
                at_list = [change_alpha_with_easein(t = .2, a = .0),])
    
    with my_vpunch
    $ renpy.pause(.75, hard = True)
    hide Christie
    show Christie Harly_Bat_Laughs
    show Christie Harly_Bat_Laughs:
        xzoom -1
        xalign .1
        ypos 1080
    show Psi Invis
    show Psi Invis:
        xalign .9
    show GG Invis
    show GG Invis:
        xalign .95
    with my_dissolve
    "Кристи" "[gg], я пришла на помощь!!!"
    python:
        for i in ('Officer', 
            'christie_root_65_hat_1', 
            'christie_root_65_hat_2',
            'christie_root_65_hat_3',
            'christie_root_65_bat_sfx_1_1',
            'christie_root_65_bat_sfx_1_2',
            'christie_root_65_bat_sfx_1_3',
            'christie_root_65_bat_sfx_2',
            'christie_root_65_bat_sfx_3',
            'christie_root_65_bat_sfx_4'
            ):

            renpy.hide(i)

    #"ext" "//Psi_Sex_GG_3"


    "Сьюзен" "Ты очень не вовремя… Кристи!"
    show Christie Harly_Bat_Embarrassment
    with my_dissolve
    "Сьюзен" "Я практически кончила и мне ещё надо… мгновение!"
    "Сьюзен" "Уйди, прошу тебя!"
    show Christie Harly_Bat_Angry
    with my_vpunch
    "Кристи" "Если ты сейчас же не слезешь с члена моего парня, я раскрошу твой череп! "
    "Сьюзен" "Чёрт!!... Ладно!"
    "Сьюзен" "Сейчас ты вряд ли станешь слушать мои оправдания, но я послушаюсь тебя и уйду."
    "Кристи" "Заодно уведи своего муженька, мразь!"
    "Сьюзен" "Не нужно кричать. Я всё прекрасно понимаю."
    hide image 'cg/ep10/susan_scene/continue/psi_2.png'
    with my_dissolve
    $ renpy.pause(.2, hard = True)
    $ from_say_screen = False
    hide Christie Harly_Angry
    hide Psi
    show christie_root_65_psi_grab_officer:
        pos (600, 800) alpha 1.0 #xzoom -1
        #parallel:
        #    alpha 1.0
        #parallel:
        
        parallel:
            pause .65
            easein_back 1.0 ypos 150
            easein_back 1.0 ypos 50
            easein_back 1.0 ypos 150
            easein_back 1.0 ypos 50

        parallel:
            easein_back .75 pos(600, 100)
            easein_back 1.0 xpos 300
            easein_back 1.0 xpos 0
            easein_back 1.0 xpos -300
            easein_back 1.0 xpos -800

            #easein_back 1.0 xpos -100
            #easein_back 1.0 xpos -200

    show Christie Harly_Bat_Angry
    show Christie Harly_Bat_Angry:
        xzoom -1
        xalign .1
        ypos 1080
        pause 1.75
        easein .5 xalign .3
        xzoom 1
    $ renpy.pause(4.75, hard = True)

    #"ext" "//Psi_Off_Hand появлется (Сьюзен тащит мужа)"
    #"ext" "//Psi_Off_Hand исчезают влево"
    "[gg]" "Кристи… Наконец-то ты пришла…"
    hide christie_root_65_psi_grab_officer
    show Christie Harly_Bat_2_Chagrin
    with my_dissolve
    show Christie Harly_Bat_2_Chagrin:
        xalign .3
        easein .75 xalign .1
        xzoom -1
    
    "Кристи" "Боже, какая же я дура!.."


    "Кристи" "Это всё из-за меня…"
    show Christie Harly_Bat_2_Chagrin:
        easein .75 xalign .1 ypos 1095
    
    show shadow_full:
        alpha .0
        easein .5 alpha .7

    "Кристи" "Даже не знаю, что и сказать теперь… "

    "[gg]" "Ты спасла меня, Кристи…"
    show Christie Harly_Bat_2_Chagrin:
        easein .75 xalign .3 ypos 1080
    
    show shadow_full:
        alpha .7
        easein .5 alpha .0
    "Кристи" "Нет. Я подставила тебя!"
    show Christie Harly_Bat_2_Chagrin:
        xzoom 1
    with my_dissolve_fast
    "Кристи" "И теперь мне нет прощения! "
    show Christie:
        easein 1.75 xalign .1 ypos 1080
        #xzoom -1
    "Кристи" "Но…"
    show Christie:
        xzoom -1 xalign .1 ypos 1080
    with my_vpunch
    "Кристи" "Я умоляю, [gg], как бы ты не был зол, прошу, извини!"
    "Кристи" "Тысячу раз извини, что я такая дура!"
    show christie_day_mischief_lvl_2_water_drop:
        xpos 1470
        ypos 390
       # zoom .05
        zoom .8
        alpha .0
        easein .7 ypos 410 alpha 1.0

    show shadow_full:
        alpha .0
        easein .5 alpha .7

    "[gg]" "Знаешь, этот разговор несколько смущает меня, учитывая, что я всё ещё прикован к кровати."
    show Christie Harly_Bat_2_Passion
    with my_dissolve
    "Кристи" "А ещё у тебя член напряжённо дрожит…"

    show shadow_full:
        alpha .7
        easein .5 alpha 1.0
    "[gg]" "Это потому что я вот-вот должен был кончить, но…"
    show Christie Harly_Bat_2_Angry:
        xzoom 1 ypos 1090
    "Кристи" "Даже здесь я подвела тебя."
    

    "[gg]" "Эй…"
    hide christie_day_mischief_lvl_2_water_drop
    show shadow_full:
        alpha 1.0
        easein .5 alpha .0
    show Christie Harly_Bat_2_Chagrin:
        xzoom -1
    "Кристи" "Но я исправлю это."
    show Christie:
        easein .5 xalign .3 ypos 1085
    "Кристи" "Честное слово, исправлю!"
    "[gg]" "Ч-что?!!"
    show Christie Harly_Bat_2_Passion:
        easein .5 xalign .6 ypos 1080
    "Кристи" "Я доведу тебя до эякуляции! "
    "[gg]" "Кристи, ты же понимаешь как нелепо это выглядит…"
    "Кристи" "Плевать! Я достаточно уже напортачила и больше совершать ошибок не намерена! "


    if preferences.language in (None, 'eng', 'rus'):
        hide Christie
        hide GG
        show image 'cg/ep10/susan_scene/continue/christie_1.png'

        show image comic_frame_v2_master:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0
        with my_vpunch
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("Я трахну тебя так, как"),
            __("{b}{i}{size=70}ни одна{/size}{/i}{/b} милфа"),
            __("не сможет этого сделать!")

            ), 
            size   = 50,
           # plus_y = 55,
           #line_spasing = -2, 
            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
            show_label = "christie_root_65_chrisite_talk_shake"
            
        ) from _call_comic_frame_v2_label_414 

        scene image '#000'
        with Dissolve(.5)

        $ renpy.music.stop(fadeout=1.5)
        $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
        $ renpy.pause(.75)

        scene image 'cg/ep10/susan_scene/end/pose_1/bg.png'
        show image 'cg/ep10/susan_scene/end/pose_1/1.png':
            alpha 1.0

        show christie_root_65_christie_sex pose_1_0

        show image 'cg/ep10/susan_scene/end/pose_1/fg.png':
            pos (0, 0)
        show image comic_frame_v2_master:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0
        with my_dissolve

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            "",
            __("Постой-постой…"),
            "",
            ), 
            size   = 50,
           # plus_y = 55,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2"),
            say_pos = ["d", 200],
         show_label = "christie_root_65_gg_talk_3", 
            
        ) from _call_comic_frame_v2_label_415 

            #renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

        #play ero 'audio/sex_christie.mp3'

        #"[gg]" 
        show image 'cg/ep10/susan_scene/end/pose_1/1.png':
            easein 1.5 alpha .0
        show christie_root_65_christie_sex pose_1_2

        # show image 'cg/ep10/susan_scene/end/pose_1/fg.png':
        #     pos (0, 0)
        #     pause .25
        #     easein 0.5 pos (0, 5)
        #     easein .1 pos (0, 0)
        #     repeat
        #"ext" "//Kristy_Sex_Psi_1"

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            "{size=25}{/size}",
            __("Ты заслуживаешь лучшего,"),
            "[gg]!",
            "{size=25}{/size}",
            ), 
            size   = 50,
           # plus_y = 55,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", xzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_christie_talk_1", 
            
        ) from _call_comic_frame_v2_label_416 

        hide image 'cg/ep10/susan_scene/end/pose_1/1.png'
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #"",

            "{size=25}{/size}",
            __("А я - это и есть лучшее,"),
            __("хи-хи-хи!"),

            "{size=25}{/size}",
            #"",
            ), 
            size   = 50,
           # plus_y = 55,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", xzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_christie_talk_1", 
            
        ) from _call_comic_frame_v2_label_417 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #"",
            __("Поэтому, позволь мне,"),
            __("пожалуйста, сделать"),
            __("тебе {size=70}{i}приятно!{/i}{/size}")
            #"",
            ), 
            size   = 50,
           # plus_y = 55,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", xzoom = -1.0),
            say_pos = ["l", 90],
         show_label = "christie_root_65_christie_talk_1", 
            
        ) from _call_comic_frame_v2_label_418 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Хех… Как будто"),
            __("у меня есть выбор.")
            
            ), 
            size   = 50,
           # plus_y = 55,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", xzoom = -1.0),
            say_pos = ["d", 540],
         show_label = "christie_root_65_gg_talk_3", 
            
        ) from _call_comic_frame_v2_label_419 

        show image comic_frame_v2_master:    
            easein .2 ypos 700 alpha 0.0
    else:
        
        hide Christie
        hide GG
        show image 'cg/ep10/susan_scene/continue/christie_1.png'
        with my_vpunch
        show GG Invis
        show GG Invis:
            xalign .92
        show Christie Invis
        show Christie Invis:
            xalign .5
        with my_dissolve
        "Кристи" "Я трахну тебя так, как ни одна милфа не сможет этого сделать!"

        scene image '#000'
        with Dissolve(.5)

        $ renpy.music.stop(fadeout=1.5)
        $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
        $ renpy.pause(.75)

        scene image 'cg/ep10/susan_scene/end/pose_1/bg.png'
        show image 'cg/ep10/susan_scene/end/pose_1/1.png':
            alpha 1.0

        show christie_root_65_christie_sex pose_1_0

        show image 'cg/ep10/susan_scene/end/pose_1/fg.png':
            pos (0, 0)
        show GG Invis
        show GG Invis:
            xalign .1
        show Christie Invis
        show Christie Invis:
            xalign .6

        with my_dissolve
        "[gg]" "Постой-постой…"
        show image 'cg/ep10/susan_scene/end/pose_1/1.png':
            easein 1.5 alpha .0
        show christie_root_65_christie_sex pose_1_2
        "Кристи" "Ты заслуживаешь лучшего, [gg]!"

        hide image 'cg/ep10/susan_scene/end/pose_1/1.png'
        "Кристи" "А я – это и есть лучшее, хи-хи-хи!"
        "Кристи" "Поэтому позволь мне, пожалуйста, сделать тебе приятно."
        "[gg]" "Хех… Как будто у меня есть выбор."

    menu christie_root_65_change_pose_2:
        "Сменить позу":
            $ pass
        "Продолжить в той же позе":
            window hide
            $ renpy.pause(9999)
            jump christie_root_65_change_pose_2
    scene image 'cg/ep10/susan_scene/end/pose_2/bg.png'
    show christie_root_65_christie_sex pose_2_2
    if preferences.language in (None, 'eng', 'rus'):
        show image comic_frame_v2_master:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0
        with my_dissolve

        #"ext" "//Kristy_Sex_Psi_2"
        #"ext" "//Скорость х1"
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #"",
            __("О {size=65}даааа{/size}, сразу"),
            __("такая {size=65}чувствительность{/size}!"),
            #__("тебе {size=70}{i}приятно!{/i}{/size}")
            #"",
            ), 
            size   = 50,
           # plus_y = 55,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_2", 
            ) from _call_comic_frame_v2_label_420

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            #"",
            __("Столько нереализованной"),
            __("{size=65}энергии{/size} и {size=65}страсти{/size}."),
            #__("тебе {size=70}{i}приятно!{/i}{/size}")
            #"",
            ), 
            size   = 50,
           # plus_y = 55,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_2", 
            
        ) from _call_comic_frame_v2_label_421 



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
          #  "{size=5}{/size}",
            __("Ты словно побывал в"),
            __("{i}горячем душе{/i}…"),

            #__("тебе {size=70}{i}приятно!{/i}{/size}")
            #"{size=5}{/size}",
            ), 
            size   = 50,
           # plus_y = 55,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_2", 
            
        ) from _call_comic_frame_v2_label_422 
        
       # "Кристи" 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
          #  "{size=5}{/size}",
            __("Ещё каком,"),
            __("хе-хе…"),

            #__("тебе {size=70}{i}приятно!{/i}{/size}")
            #"{size=5}{/size}",
            ), 
            size   = 55,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", xzoom = -1.0),
            say_pos = ["l", 50],
         show_label = "christie_root_65_gg_talk_4", 
            
        ) from _call_comic_frame_v2_label_423 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            "{size=5}{/size}",
            __("{i}Подлая сука!{/i}"),


            #__("тебе {size=70}{i}приятно!{/i}{/size}")
            "{size=5}{/size}",
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_shake_2", 
            
        ) from _call_comic_frame_v2_label_424 
        


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Чёртова бестия"),
            __("воспользовалась твоей слабостью,"),
            __("[gg], но я уничтожу"),
            __("её мерзкие зловония.")

            #__("тебе {size=70}{i}приятно!{/i}{/size}")
            
            ), 
            size   = 50,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_2", 
            
        ) from _call_comic_frame_v2_label_425 


       # "[gg]" 


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Я не успокоюсь, пока не"),
            __("замещу мерзкий запах"),
            __("Сьюзен своим.")

            #__("тебе {size=70}{i}приятно!{/i}{/size}")
            
            ), 
            size   = 55,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_2", 
            
        ) from _call_comic_frame_v2_label_426 


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            "{size=5}{/size}",
            __("Ты мой и только мой!!"),


            #__("тебе {size=70}{i}приятно!{/i}{/size}")
            "{size=5}{/size}",
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_shake_2", 
            
        ) from _call_comic_frame_v2_label_427 


        show shadow_full:
            alpha .0
            easein .2 alpha 1.0
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            "{size=5}{/size}",
            __("{i}Охренеть!{/i}"),


            #__("тебе {size=70}{i}приятно!{/i}{/size}")
            "{size=5}{/size}",
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_8", zoom = .8),
            say_pos = ["d", 30],
         show_label = "christie_root_65_gg_talk_shake_4", 
            
        ) from _call_comic_frame_v2_label_428 

        call comic_frame_v2_label((
            
            __("{i}Подумать только,{/i}"),
            __("{i}ещё минуту{/i}"),
            __("{i}назад на мне{/i}"),
            __("{i}сидела другая{/i}"),
            __("{i}женщина…!{/i}")

            ), 
            size   = 40,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_8", zoom = .8),
            say_pos = ["d", 30],
         show_label = "christie_root_65_gg_talk_4", 
            
            
        ) from _call_comic_frame_v2_label_429 



        call comic_frame_v2_label((
            
            __("{i}Но уже сейчас Кристи{/i}"),
            __("{i}сжимает моей член{/i}"),
            __("{i}своей киской{/i}")
            ), 
            size   = 40,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_8", zoom = .8),
            say_pos = ["d", 30],
         show_label = "christie_root_65_gg_talk_4", 
            
        ) from _call_comic_frame_v2_label_430 


        call comic_frame_v2_label((
            
            __("{i}и её ни капли не смущает,{/i}"),
            __("{i}что внутри неё{/i}"),
            __("{i}остатки выделений{/i}"),
            __("{i}Сьюзен...{/i}")

            ), 
            size   = 35,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_8", zoom = .8),
            say_pos = ["d", 30],
         show_label = "christie_root_65_gg_talk_4", 
            
            
        ) from _call_comic_frame_v2_label_431 

        call comic_frame_v2_label((
            "",
            __("{i}Это настолько пошло,{/i}"),
            __("{i}что мне даже{/i}"),
            __("{i}стыдно думать о таком.{/i}"),
            "",

            ), 
            size   = 35,
            plus_y = 0,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_8", zoom = .8),
            say_pos = ["d", 30],
         show_label = "christie_root_65_gg_talk_4", 
            
            
        ) from _call_comic_frame_v2_label_432 


        call comic_frame_v2_label((
          #  "",
            __("{i}К чёрту{/i}"),
            __("{i}рациональность,{/i}"),
            __("{i}к чёрту логику!{/i}"),
           # "",

            ), 
            size   = 50,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_8", zoom = .8),
            say_pos = ["d", 30],
         show_label = "christie_root_65_gg_talk_shake_4", 
            
            
        ) from _call_comic_frame_v2_label_433 


        call comic_frame_v2_label((
            #"",
            __("{i}Пора получить{/i}"),
            __("{i}желаемое{/i}"),
            __("{i}в полной мере!!{/i}"),
            #"",

            ), 
            size   = 50,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_8", zoom = .8),
            say_pos = ["d", 30],
         show_label = "christie_root_65_gg_talk_shake_4", 
            
            
        ) from _call_comic_frame_v2_label_434 

        #"ext" "//Конец мысли"

        show image comic_frame_v2_master:    
            easein .2 ypos 700 alpha 0.0
    else:
        show GG Invis
        show GG Invis:
            xalign .9
        show Christie Invis
        show Christie Invis:
            xalign .45

        with my_dissolve

        "Кристи" "О даааа, сразу такая чувствительность."
        "Кристи" "Столько нереализованной энергии и страсти."
        "Кристи" "Ты словно побывал в горячем душе…"
        "[gg]" "Ещё каком, хе-хе…"
        "Кристи" "Подлая сука!"
        "Кристи" "Чёртова бестия воспользовалась твоей слабостью, [gg], но я уничтожу её мерзкие зловония. "
        "Кристи" "Я не успокоюсь, пока не замещу мерзкий запах Сюзен своим."
        "Кристи" "Ты мой и только мой!!"

        show shadow_full:
            alpha .0
            easein .2 alpha 1.0
        "[gg]" "{i}Охренеть!{/i}"
        "[gg]" "{i}Подумать только, ещё минуту назад на мне сидела другая женщина…{/i}"
        "[gg]" "{i}Но уже сейчас Кристи сжимает моей член своей киской, и её ни капли не смущает, что внутри неё остатки выделений Сьюзен.{/i}"
        "[gg]" "{i}Это настолько пошло, что мне даже стыдно думать о таком.{/i}"
        "[gg]" "{i}К чёрту рациональность, к чёрту логику…{/i}"
        "[gg]" "{i}Пора получить желаемое в полной мере!!{/i}"






    show shadow_full:
        easein .2 alpha .0

    $ renpy.pause(.1, hard = True)


    menu christie_root_65_speed_up_2:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_root_65_speed_up_2

    show christie_root_65_christie_sex pose_2_3
    with my_dissolve
    if preferences.language in (None, 'eng', 'rus'):
    #"ext" "//Скорость х2"
        call comic_frame_v2_label((
            
            __("Ахххх!"),
            __("{size=80}Охххх!!{/size}"),
            __("Ухххх!..")


            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_shake_2", 
            
        ) from _call_comic_frame_v2_label_435 

        call comic_frame_v2_label((
            
            __("Я боялась, что"),
            __("после Сьюзен, ты"),
            __("кончишь почти сразу...")

            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_2", 
            
        ) from _call_comic_frame_v2_label_436 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            "{size=5}{/size}",
            __("Не дождёшься!"),


            #__("тебе {size=70}{i}приятно!{/i}{/size}")
            "{size=5}{/size}",
            ), 
            size   = 52,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 50],
         show_label = "christie_root_65_gg_talk_shake_4", 
            
        ) from _call_comic_frame_v2_label_437 

        call comic_frame_v2_label((
            
            __("Ты, как всегда,"),
            __("непредсказуемо"),
            __("хорош!")

            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_2", 
            
        ) from _call_comic_frame_v2_label_438 

        call comic_frame_v2_label((
            
            __("Эта сучка только"),
            __("простимулировала твою"),
            __("эрекцию, а я забрала у"),
            __("неё самое лучшее!")

            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_2", 
            
        ) from _call_comic_frame_v2_label_439 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("Воу! Ты"),
            __("злорадствуешь"),
            __("так, словно так"),
            __("и задумано.")

            ), 
            size   = 50,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", xzoom = -1),
            say_pos = ["d", 90],
         show_label = "christie_root_65_gg_talk_shake_4", 
            
        ) from _call_comic_frame_v2_label_440 

        call comic_frame_v2_label((
            
            __("О нет."),
            __("Я ненавижу её!"),



            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_shake_2", 
            
        ) from _call_comic_frame_v2_label_441 

        call comic_frame_v2_label((
            
            __("Но, стоит отдать"),
            __("ей должное, она"),
            __("хорошо тебя разогрела.")
            


            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_2", 
            
        ) from _call_comic_frame_v2_label_442 


        call comic_frame_v2_label((
            
            __("Пусть теперь кусает"),
            __("локти и бьётся"),
            __("в истерике от зависти!")
            


            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_2", 
            
        ) from _call_comic_frame_v2_label_443 

        call comic_frame_v2_label((
            
            __("Надеюсь, мои"),
            __("стоны хорошо"),
            __("ей слышны!..")
            


            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_4", yzoom = -1),
            say_pos = ["r", 50],
         show_label = "christie_root_65_christie_talk_shake_2", 
            
        ) from _call_comic_frame_v2_label_444 
        show shadow_full:
            alpha .0
            easein .2 alpha 1.0
        call comic_frame_v2_label((
            "",
            __("{i}Более чем…{/i}"),
            "",

            ), 
            size   = 70,
            plus_y = 0,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_8", zoom = .8),
            say_pos = ["d", 60],
         show_label = "christie_root_65_gg_talk_4", 
            
            
        ) from _call_comic_frame_v2_label_445 
        show image comic_frame_v2_master:    
            easein .2 ypos 700 alpha 0.0

        show shadow_full:
            easein .2 alpha .0

        $ renpy.pause(.1, hard = True)
    else:


        show GG Invis
        show GG Invis:
            xalign .8
        show Christie Invis
        show Christie Invis:
            xalign .45

        with my_dissolve
        "Кристи" "Ахххх! Охххх!! Ухххх!.."
        "Кристи" "Я боялась, что после Сьюзен, ты кончишь почти сразу..."
        "[gg]" "Не дождёшься!"
        "Кристи" "Ты как всегда непредсказуемо хорОш! "
        "Кристи" "Эта сучка только простимулировала твою эрекцию, а я забрала у неё самое лучшее! "
        "[gg]" "Воу! Ты злорадствуешь так, словно так и задумано."
        "Кристи" "О нет. Я ненавижу её!"
        "Кристи" "Но стоит отдать ей должное, она хорошо тебя разогрела. "
        "Кристи" "Пусть теперь кусает локти и бьётся в истерике от зависти! "
        "Кристи" "Надеюсь, мои стоны хорошо ей слышны!.."
        "[gg]" "Более чем…"


    menu christie_root_65_change_pose_3:
        "Сменить позу":
            $ pass
        "Продолжить в той же позе":
            window hide
            $ renpy.pause(9999)
            jump christie_root_65_change_pose_3
    scene image 'cg/ep10/susan_scene/end/pose_3/bg.png'
    show christie_root_65_christie_sex pose_3_3
    if preferences.language in (None, 'eng', 'rus'):
        show image comic_frame_v2_master:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0
        with my_dissolve

        #"ext" "//Скорость х3"
        call comic_frame_v2_label((
            
            __("Ах!"),
            __("{size=75}Ахх!!{/size}"),
            __("{size=80}Аххх!!!{/size}")
            


            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", yzoom = -1,),
            say_pos = ["u", 100],
         show_label = "christie_root_65_christie_talk_3", 
            
        ) from _call_comic_frame_v2_label_446 


        call comic_frame_v2_label((
            
            __("Ещё!"),
            __("{size=75}Ещё!{/size}"),
            __("{size=80}Ещё!!!{/size}")
            


            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", yzoom = -1, ),
            say_pos = ["u", 100],
         show_label = "christie_root_65_christie_talk_3", 
            
        ) from _call_comic_frame_v2_label_447 


        call comic_frame_v2_label((
            
            __("  Твой член  "),
            __("творит {i}чудеса{/i},"),
            "[gg]!"
            


            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", yzoom = -1, ),
            say_pos = ["u", 100],
         show_label = "christie_root_65_christie_talk_3", 
            
        ) from _call_comic_frame_v2_label_448 


        call comic_frame_v2_label((
            
            __("Я - словно бомба"),
            __("с часовым механизмом…"),
            __("вот-вот {size=85}{color=#FF0833}{i}взорвусь{/i}{/color}{/size}"),
            __("от удовольствия!")
            


            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", yzoom = -1, ),
            say_pos = ["u", 100],
         show_label = "christie_root_65_christie_talk_3", 
            
        ) from _call_comic_frame_v2_label_449 



        call comic_frame_v2_label((
            
            __("Значит, ты уже"),
            __("приближаешься"),

            __("к катарсису?"),
            
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", xzoom = -1.0 ),
            say_pos = ["d", 100],
         show_label = "christie_root_65_gg_talk_5", 
            
        ) from _call_comic_frame_v2_label_450 



        call comic_frame_v2_label((
            
            __("Ага, и за"),
            __("последствия"),
            __("не ручаюсь!")



            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", yzoom = -1, ),
            say_pos = ["u", 100],
         show_label = "christie_root_65_christie_talk_3", 
            
        ) from _call_comic_frame_v2_label_451 

        call comic_frame_v2_label((
            
            __("Тогда двигайся"),
            __("как можно сильнее,"),

            __("   Кристи.   "),
            
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", xzoom = -1.0 ),
            say_pos = ["d", 400],
         show_label = "christie_root_65_gg_talk_5", 
            
        ) from _call_comic_frame_v2_label_452 

        call comic_frame_v2_label((
            
            __("Я практически"),
            __("{size=85}на грани…!{/size}"),

            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", xzoom = -1.0 ),
            say_pos = ["d", 100],
         show_label = "christie_root_65_gg_talk_5", 
            
        ) from _call_comic_frame_v2_label_453 
    else:
        show GG Invis
        show GG Invis:
            xalign .1
        show Christie Invis
        show Christie Invis:
            xalign .6

        with my_dissolve

        "Кристи" "Ах! Ахх!! Аххх!!!"
        "Кристи" "Ещё-ещё-ещё!"
        "Кристи" "Твой член творит чудеса, [gg]! "
        "Кристи" "Я словно бомба с часовым механизмом… вот-вот взорвусь от удовольствия!"
        "[gg]" "Значит, мы уже приближаешься к катарсису? "
        "Кристи" "Ага, и за последствия не ручаюсь!"
        "[gg]" "Тогда двигайся как можно сильнее, Кристи."
        "[gg]" "Я практически на грани…!"
    menu christie_root_65_change_pose_4:
        

        "Сменить позу (1)":

            scene image 'cg/ep10/susan_scene/end/pose_1/bg.png'

            show christie_root_65_christie_sex pose_1_1

            show image 'cg/ep10/susan_scene/end/pose_1/fg.png'
            with my_dissolve
            window hide
            $ renpy.pause(9999)
            jump christie_root_65_change_pose_4
        
        "Сменить позу (2)":
            scene image 'cg/ep10/susan_scene/end/pose_2/bg.png'
            show christie_root_65_christie_sex pose_2_2
            with my_dissolve
            window hide
            $ renpy.pause(9999)
            jump christie_root_65_change_pose_4
        
        "Сменить позу (3)":
            scene image 'cg/ep10/susan_scene/end/pose_3/bg.png'
            show christie_root_65_christie_sex pose_3_3
            with my_dissolve
            window hide
            $ renpy.pause(9999)
            jump christie_root_65_change_pose_4
        
        "Кончить":
            pass
    scene image 'cg/ep10/susan_scene/end/pose_3/bg.png'
    show christie_root_65_christie_sex pose_3_3
    if preferences.language in (None, 'eng', 'rus'):
        show image comic_frame_v2_master:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0
        with my_dissolve
        call comic_frame_v2_label((
            
            __("Давай кончим вместе…"),
            __("{i}{size=90}Одновременно!{/size}{/i}"),

            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", yzoom = -1, ),
            say_pos = ["u", 100],
         show_label = "christie_root_65_christie_talk_3", 
            
        ) from _call_comic_frame_v2_label_454 



        call comic_frame_v2_label((
            "",        
            __("{size=85}Давай!{/size}"),
            "",
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", xzoom = -1.0 ),
            say_pos = ["d", 100],
         show_label = "christie_root_65_gg_talk_5", 
            
        ) from _call_comic_frame_v2_label_455 


        


        call comic_frame_v2_label((
            
            __("  Я…  "),
            __("ещё {i}{size=90}мгновение,{/size}{/i}"),

            __("ещё {i}{size=90}секунда…{/size}{/i}"),
            
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", yzoom = -1, ),
            say_pos = ["u", 100],
         show_label = "christie_root_65_christie_talk_3", 
            
        ) from _call_comic_frame_v2_label_456 


        
        #"ext" "//Кончают"
        #"ext" "// Kristy_Sex_Psi_3"
        #"Кристи" "!!!!"
        #"[gg]" ""


        $ christie_root_65_cum_1 = Composite((1050, 180), (0, 0), Solid("#000"))
        $ christie_root_65_cum_4 = Composite((1050, 180), (0, 0), Solid("#000"))

        $ christie_root_65_cum_2 = Composite((1020, 180), 
            #(0, 0), Solid("#000"),
            (0, 0), Frame(Transform('interface/comic_v2/bg_frame_2.png', alpha = .8), Borders(64, 64, 64, 64)),
            (20, 50), Text(
                            __("Коооончаааааааюююююуууууууу!!!"), 
                            kerning  = 5,
                            size     = 50,
                            outlines = [(2, "#000a", 0, 0),],
                            font = "fonts/mango_comics_er.ttf",
                            
                            ),
            (1020, 60), Transform("comic_frame_say_3")
            )


        $ christie_root_65_cum_3 = Composite((1020, 180), 
            #(0, 0), Solid("#000"),
            (0, 0), Frame(Transform('interface/comic_v2/bg_frame_2.png', alpha = .8), Borders(64, 64, 64, 64)),
            (20, 50), Text(
                            __("Кончаааааааююююююуууууу!!!"), 
                            kerning  = 5,
                            size     = 50,
                            outlines = [(2, "#000a", 0, 0),],
                            font = "fonts/mango_comics_er.ttf",
                            
                            ),
            (1020, 60), Transform("comic_frame_say_3")
            )



        show image AlphaMask(christie_root_65_cum_2, At(christie_root_65_cum_1, christie_root_52_cum_transform)): #comic_frame_v2_0:
            zoom .7
            xpos 100
            ypos 70
            xanchor 0.0
            yanchor 0.0
            alpha 1.0



        show image AlphaMask(christie_root_65_cum_3, At(christie_root_65_cum_4, christie_root_65_cum_transform)): #comic_frame_v2_0:
            zoom .85
            xpos 1800
            ypos 570
            xanchor 1.0
            yanchor 0.0
            alpha 1.0
        hide image comic_frame_v2_master
        hide image comic_frame_v2_slave
        #show image christie_root_52_cum_2
        #show
        with my_dissolve
        $ renpy.pause(.9)
        #show ep9_strip_gg 7
        $ renpy.pause(.1)
        
        
        show white
        with Dissolve(.3)

        stop ero fadeout 1.0
        # $ renpy.music.stop( 
        #     channel=renpy.config.play_channel, 
        #     fadeout=.75)
        $ renpy.pause(1.2, hard = True)
        
        scene image 'cg/ep10/susan_scene/end/pose_3/bg.png'
        show christie_root_65_christie_sex pose_3_cum
        show image comic_frame_v2_master:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0
            alpha .0

        show image comic_frame_v2_slave:
            zoom .8
            xpos 950
            ypos 200
            xanchor 1.0
            yanchor .0  
            alpha .0
        with my_dissolve
        $ renpy.pause(999)
        call comic_frame_v2_label((
            
            __("  Я не могу  "),
            __("подобрать подходящих слов,"),

            __("чтобы выразить свои чувства."),
            
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", yzoom = -1, ),
            say_pos = ["u", 100],
         show_label = "christie_root_65_christie_talk_3", 
            
        ) from _call_comic_frame_v2_label_457 



        call comic_frame_v2_label((
            __("Главное, что"),
            __("это взаимно.")

            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", xzoom = -1.0 ),
            say_pos = ["d", 150],
         show_label = "christie_root_65_gg_talk_5", 
            
        ) from _call_comic_frame_v2_label_458 




        call comic_frame_v2_label((
            
            __("О нет, я"),
            __("обожаю тебя в"),

            __("сто раз больше."),
            
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", yzoom = -1, ),
            say_pos = ["u", 100],
         show_label = "christie_root_65_christie_talk_3", 
            
        ) from _call_comic_frame_v2_label_459 



        call comic_frame_v2_label((
            __("Тогда развяжи"),
            __("меня поскорее.")
            
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", xzoom = -1.0 ),
            say_pos = ["d", 100],
         show_label = "christie_root_65_gg_talk_5", 
            
        ) from _call_comic_frame_v2_label_460 


        call comic_frame_v2_label((
            "",
            __("Ты прав."),
            
            "",
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", yzoom = -1, ),
            say_pos = ["u", 100],
         show_label = "christie_root_65_christie_talk_3", 
            
        ) from _call_comic_frame_v2_label_461 


        call comic_frame_v2_label((
            __("Из головы совсем вылетело,"),
            __("что мы в чужом доме,"),
            __("и я избила копа…"),
            __("хи-хи!")
            
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", yzoom = -1, ),
            say_pos = ["u", 100],
         show_label = "christie_root_65_christie_talk_3", 
            
        ) from _call_comic_frame_v2_label_462 


        call comic_frame_v2_label((
            "",
            __("Это всё"),
            __("адреналин."),
            ""
            
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", xzoom = -1.0 ),
            say_pos = ["d", 100],
         show_label = "christie_root_65_gg_talk_5", 
            
        ) from _call_comic_frame_v2_label_463 



        call comic_frame_v2_label((
            "",
            __("Или слепая любовь."),
            
            "",
            ), 
            size   = 70,
            plus_y = 5,
            line_spasing = 0, 

            say_image = Transform("comic_frame_say_2", yzoom = -1, ),
            say_pos = ["u", 100],
         show_label = "christie_root_65_christie_talk_3", 
            
        ) from _call_comic_frame_v2_label_464 
    else:
        show GG Invis
        show GG Invis:
            xalign .1
        show Christie Invis
        show Christie Invis:
            xalign .6

        with my_dissolve
        "Кристи" "Давай кончим вместе… Одновременно!"
        "[gg]" "Давай!"
        "Кристи" "Я… ещё мгновение, ещё секунда…"
        "Кристи" "Коооончаааааааюююююуууууууу!!!!"
        "[gg]" "Кончаааааааююююююуууууу!!!"
        scene image 'cg/ep10/susan_scene/end/pose_3/bg.png'
        show christie_root_65_christie_sex pose_3_cum
        show GG Invis
        show GG Invis:
            xalign .1
        show Christie Invis
        show Christie Invis:
            xalign .6

        with my_dissolve
        "[gg]" "Кончаааааааююююююуууууу!!!"

        stop ero fadeout 1.0

        "Кристи" "Я не могу подобрать походящих слов, чтобы выразить свои чувства."
        "[gg]" "Главное, что это взаимно."
        "Кристи" "О нет, я обожаю тебя в сто раз больше."
        "[gg]" "Тогда развяжи меня поскорее."
        "Кристи" "Ты прав. "
        "Кристи" "Из головы совсем вылетело, что мы в чужом доме, и я избила копа…хи-хи!"
        "[gg]" "Это всё адреналин."
        "Кристи" "Или слепая любовь."
    scene black with Dissolve(.3)

    python:
        try:
            del christie_root_65_cum_1
        except:
            pass
        
        try:
            del christie_root_65_cum_2
        except:
            pass
        
        try:
            del christie_root_65_cum_3
        except:
            pass
        
        try:
            del christie_root_65_cum_4
        except:
            pass

        try:
            del _st_65_y
        except:
            pass

        try:
            del _st_65
        except:
            pass

        
        try:
            del _st_65_t
        except:
            pass

        


        renpy.pause(.5, hard = True)


        renpy.music.stop(fadeout=1.5)

        renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)


    scene expression 'cg/christie_root/psi_corridor.png'
    show Officer Normal
    show Officer Normal:
        xalign .0
        ypos 1085

    show Psi Normal
    show Psi Normal:
        xalign .3
        xzoom -1
        ypos 1085

    with Dissolve(.5)


    show Christie Harly_Angry
    show Christie Harly_Angry at go_from_right(xxalign = .95)

    show GG Angry
    show GG Angry at go_from_right(xxzoom = -1.0, xxalign = .7)

    #"ext" "//Psi_Room"
    #"ext" "//Psi_Normal стоит слева"
    #"ext" "//Officer_Normal стоит слева"
    #"ext" "//GG_Normal двигаются справа налево, приближаясь к офицеру и Сьюзен"
    #"ext" "//Harly_Kristy_Normal двигаются справа налево, приближаясь к офицеру и Сьюзен"
  #  show GG Normal
    "[gg]" "Дайте пройти."
    show Officer Angry
    with my_dissolve
    "Officer" "Стоило бы израсходовать на тебя всю обойму. Чтоб наверняка."
    #show Officer Normal
    show GG:
        xalign .7
        xzoom -1.0
    show Christie:
        xalign .95
    with my_dissolve
    "Officer" "Но тебе, придурку, посчастливилось меня спасти."
    show GG:
        easein .3 xalign .5
    show Psi:
        easein .3 xalign .2
    "[gg]" "Ты всё сказал?"
    #show Officer Normal
    show Psi:
        easein .3 xalign .0
    show Officer Angry:
        easein .3 xalign .3
    show GG:
        easein .3 xalign .6
    "Officer" "Пошли нахер отсюда."
    #"ext" "//Сьюзен подмигивает вам (написать это текстом)"
    show shadow_full:
        alpha .0
        easein .5 alpha 1.0
        easeout .5 alpha 0.0
    show Psi:
        xalign .0
        easein .5 ypos 1095
        easeout .5 ypos 1085
    "Сьюзан" "{i}Сьазен подмигивает вам{/i}"
    show Officer:
        xalign .3
    show GG:
        xalign .6
        easein 1.5 xalign -1.5
    show Christie:
        xalign .95
        easein 1.5 xalign -1.5
    $ renpy.pause(.75, hard = True)
    scene expression 'cg/christie_root/Psi_Build.png'
    with Dissolve(.25)
    $ from_say_screen = False
    $ renpy.pause(.25, hard = True)

    show Christie Harly_Angry
    show Christie Harly_Angry at go_from_left(xxalign = .9, xxzoom = -1.0)

    show GG Passion
    show GG Passion at go_from_left(xxalign = .1)


    #"ext" "//Psi_House"
    #show GG Normal
    "[gg]" "Интересно, ему понравилось или нет?"
    show Christie:
        xalign .9 xzoom 1.0
    with my_dissolve
    #show Harly KristyNormal
    "Кристи" "О чём это ты?.."
    #show GG Normal
    show GG:
        xalign .1
    with my_dissolve
    "[gg]" "Да так, уже неважно."
    
    call comic_frame_v2_predict_label(action=renpy.stop_predict,
        images=comic_frame_v2_predict_list+[
        'cg/christie_root/psi_corridor.png', 
        'Psi *',
        'Christie *',
        'Officer *',
        'christie_root_65_tea *',
        'christie_root_65_sex *',
        'cg/ep10/susan_scene/start/*.*',
        'christie_root_65_christie_sex *',
        'cg/ep10/susan_scene/continue/sex_2/bg.png',
        'cg/ep10/susan_scene/continue/sex_1/bg.png',
        'cg/ep10/susan_scene/continue/*.*',
        'cg/ep10/susan_scene/continue/sex_1/gg.png',
        'cg/ep10/susan_scene/end/pose_1/bg.png',
        'cg/ep10/susan_scene/end/pose_1/fg.png',
        'cg/ep10/susan_scene/end/pose_2/bg.png',
        'cg/ep10/susan_scene/end/pose_3/bg.png',
        
        ]

        ) from _call_comic_frame_v2_predict_label_3
    if not from_gallery_check():
        $ descript_Christie = __("Конец рута Кристи для эпизода 1.0")
        if hasattr(store, 'unlock_milf_costumes'):
            call final_act_setup from _call_final_act_setup
        $ christie_root_65_end = True
        $ add_to_gallery(42)
    #"ext" " "
    
    jump main_interface_label
    
    
