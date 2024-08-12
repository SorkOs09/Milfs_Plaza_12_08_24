
label christie_night_mischief_lvl_2_gg_talk_hide:
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
        easein .2 ypos i[1]-50 alpha 0.0
    #$ renpy.pause(.21, hard = True)
    return 

label christie_night_mischief_lvl_2_gg_talk:
    show image comic_frame_v2_master:
        zoom .7
        xpos 780
        ypos 200
        xanchor 1.0
        yanchor .5
        alpha .0
        parallel:
            easein 0.2 ypos 150
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.21, hard = True)
    return 

label christie_night_mischief_lvl_2_gg_talk_shake:
    show image comic_frame_v2_master:
        zoom .7
        xpos 780
        ypos 140
        xanchor 1.0
        yanchor .5
        alpha .0
        
        parallel:
            ease .05 alpha 1.0
        parallel:
            ease .1 ypos 150
            ease .1 ypos 157
            ease .1 ypos 150
            ease .1 ypos 157
            ease .1 ypos 150
    $ renpy.pause(.51, hard = True)
    return 

label christie_night_mischief_lvl_2_christie_talk:
    show image comic_frame_v2_master:
        zoom .5
        xpos 1900
        ypos 200
        xanchor 1.0
        yanchor .53
        alpha .0
        parallel:
            easein 0.2 ypos 150
        parallel:
            ease .2 alpha 1.0
    $ renpy.pause(.21, hard = True)
    return 


label christie_night_mischief_lvl_2_christie_talk_shake:
    show image comic_frame_v2_master:
        zoom .5
        xpos 1880
        ypos 140
        xanchor 1.0
        yanchor .5
        alpha .0
        
        parallel:
            ease .05 alpha 1.0
        parallel:
            ease .1 ypos 150
            ease .1 ypos 157
            ease .1 ypos 150
            ease .1 ypos 157
            ease .1 ypos 150

    $ renpy.pause(.51, hard = True)
    return 
init 5 python:

    class FlashLight(renpy.Displayable):

        def __init__(self, image, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)
            self.image = image
            self.flashlight_mask = Transform('mini_games/flashlight_mask.png', zoom = .75)
            self.displayable = Composite(
                (1920, 1080),
                (0, 0), self.flashlight_mask
                )
            self.black = renpy.get_registered_image('black')


       
        def render(self, width, height, st, at):
            

            rend = renpy.Render(1920, 1080)
            mouse_pos = renpy.get_mouse_pos()
  
            x_0 = mouse_pos[0]-375

            x_1 = mouse_pos[0]+375


            y_0 = mouse_pos[1]-375

            y_1 = mouse_pos[1]+375
            # rend.blit(renpy.render(Text(
            #     str(st), 
            #     outlines = [(2, "#000a", 0, 0),], 
            #     size     = 30 
            #     ), 
            #     100, 475, st, at), (mouse_pos[0], mouse_pos[1]))


            self.displayable = AlphaMask(self.image, Composite(
                (3840, 2160),
                (0, 0), Crop((0, 0, x_0, 2160), self.black),
                (x_0, 0), Crop((0, 0, 3840, y_0), self.black),
                (x_1, y_0), Crop((0, 0, 3840, 2160), self.black),
                (0, y_1), Crop((0, 0, 3840, 2160), self.black),
                
                (mouse_pos[0]-375, mouse_pos[1]-375), self.flashlight_mask
                ))
            rend.blit(renpy.render(self.displayable,
                1920, 1080, st, at), (0, 0))

            

            # rend.blit(renpy.render(Text(str(mouse_pos[0]) + " : "+str(mouse_pos[1])),
            #     1920, 1080, st, at), (0, 0))


            
            #renpy.redraw(self, 0)
            
            return rend
        def event(self, ev, x, y, st):

          
            renpy.redraw(self, 0)
image flashlight_mask = 'mini_games/flashlight_mask.png'
image christie_night_mischief_lvl_2_bg = 'cg/ep95/christie_night_mischief/bg.png'
image christie_night_mischief_lvl_2_fg_0 = 'cg/ep95/christie_night_mischief/fg_0.png'
image christie_night_mischief_lvl_2_fg 0 = 'cg/ep95/christie_night_mischief/fg_0.png'
image christie_night_mischief_lvl_2_fg 1 = FlashLight('cg/ep95/christie_night_mischief/fg_0.png') #'cg/ep95/christie_night_mischief/fg_1.png'
image christie_night_mischief_lvl_2_shadow = 'cg/ep95/christie_night_mischief/shadow.png'

image christie_night_mischief_lvl_2 0 = 'cg/ep95/christie_night_mischief/0.png'
#-110, +120
image christie_night_mischief_lvl_2_circle_btn_1 = Composite((1920, 1080),
    (60, 600), Composite((350, 350), (0, 0), Transform(Solid("#0001"), alpha = 0.1))
    )

image christie_night_mischief_lvl_2_circle_btn_2 = Composite((1920, 1080),
    (670, 450), Composite((350, 350), (0, 0), Transform(Solid("#0001"), alpha = 0.1))
    )


image christie_night_mischief_lvl_2_sperm_1_s = Composite((1920, 1080),
    (-150, -150), 'cg/ep85/gg_milf_sex/1s.png',
    (-150, 150), Transform('cg/ep85/gg_milf_sex/1s.png', yzoom = -1.0),

    )

image christie_night_mischief_lvl_2_sperm_2_s = Composite((1920, 1080),
    (-150, -150), 'cg/ep85/gg_milf_sex/2s.png',
    (-150, 150), Transform('cg/ep85/gg_milf_sex/2s.png', yzoom = -1.0),

    )

image christie_night_mischief_lvl_2_sperm_3_s = Composite((1920, 1080),
    (-150, -150), 'cg/ep85/gg_milf_sex/3s.png',
    (-150, 150), Transform('cg/ep85/gg_milf_sex/3s.png', yzoom = -1.0),

    )


image christie_night_mischief_lvl_2_sperm_4_s = Composite((1920, 1080),
    (-150, -150), 'cg/ep85/gg_milf_sex/3s.png',
    (-150, 150), Transform('cg/ep85/gg_milf_sex/4s.png', yzoom = -1.0),
    )



image christie_night_mischief_lvl_2_sperm 1:
    '#0000'
    .17
    .17
    'christie_night_mischief_lvl_2_sperm_1_s' with Dissolve(.1)
    .16
    'christie_night_mischief_lvl_2_sperm_2_s'
    .17
    'christie_night_mischief_lvl_2_sperm_3_s'
    .17
    'christie_night_mischief_lvl_2_sperm_4_s'
    .16
    '#0000' with Dissolve(.1)
    
    repeat


image christie_night_mischief_lvl_2_sperm 2:
    '#0000'
    .12
    .12
    'christie_night_mischief_lvl_2_sperm_1_s' with Dissolve(.1)
    .11
    'christie_night_mischief_lvl_2_sperm_2_s'
    .12
    'christie_night_mischief_lvl_2_sperm_3_s'
    .12
    'christie_night_mischief_lvl_2_sperm_4_s'
    .11
    '#0000' with Dissolve(.1)
    
    repeat


image christie_night_mischief_lvl_2_sperm 3:
    '#0000'
    .08
    .08
    'christie_night_mischief_lvl_2_sperm_1_s' with Dissolve(.1)
    .07
    'christie_night_mischief_lvl_2_sperm_2_s'
    .08
    'christie_night_mischief_lvl_2_sperm_3_s'
    .08
    'christie_night_mischief_lvl_2_sperm_4_s'
    .07
    '#0000' with Dissolve(.1)
    
    repeat



image christie_night_mischief_lvl_2_sperm 4:
    '#0000'
    .06
    .06
    'christie_night_mischief_lvl_2_sperm_1_s' with Dissolve(.1)
    .05
    'christie_night_mischief_lvl_2_sperm_2_s'
    .06
    'christie_night_mischief_lvl_2_sperm_3_s'
    .06
    'christie_night_mischief_lvl_2_sperm_4_s'
    .05
    '#0000' with Dissolve(.1)
    
    repeat

image christie_night_mischief_lvl_2 0_5:
    'cg/ep95/christie_night_mischief/1.png'
    .9
    'cg/ep95/christie_night_mischief/2.png'
    2.5
    # 'cg/ep95/christie_night_mischief/3.png'
    # .17
    # 'cg/ep95/christie_night_mischief/4.png'
    # .17
    # 'cg/ep95/christie_night_mischief/3.png'
    # .17
    # 'cg/ep95/christie_night_mischief/2.png'
    # .17
    repeat

image christie_night_mischief_lvl_2 0_75:
    'cg/ep95/christie_night_mischief/1.png'
    .9
    'cg/ep95/christie_night_mischief/2.png'
    2.5
    'cg/ep95/christie_night_mischief/1.png'
    .9
    'cg/ep95/christie_night_mischief/2.png'
    2.5
    'cg/ep95/christie_night_mischief/1.png'
    .6
    'cg/ep95/christie_night_mischief/2.png'
    .6
    'cg/ep95/christie_night_mischief/3.png'
    2.5
    'cg/ep95/christie_night_mischief/1.png'
    .3
    'cg/ep95/christie_night_mischief/1.png'
    .3
    'cg/ep95/christie_night_mischief/2.png'
    .3
    'cg/ep95/christie_night_mischief/3.png'
    .3
image christie_night_mischief_lvl_2_1_tmp:

    'cg/ep95/christie_night_mischief/1.png'
    .5
    'cg/ep95/christie_night_mischief/2.png'
    .5
    'cg/ep95/christie_night_mischief/3.png'
    .35
    'cg/ep95/christie_night_mischief/2.png'
    .5
    'cg/ep95/christie_night_mischief/1.png'
    .35
    'cg/ep95/christie_night_mischief/2.png'
    .35
    'cg/ep95/christie_night_mischief/3.png'
    .35
    'cg/ep95/christie_night_mischief/2.png'
    .5
    'cg/ep95/christie_night_mischief/3.png'
    .35
    'cg/ep95/christie_night_mischief/2.png'
    .32
    'cg/ep95/christie_night_mischief/3.png'
    .32
    'cg/ep95/christie_night_mischief/2.png'
    .3
    block:
        'cg/ep95/christie_night_mischief/1.png'
        .3
        'cg/ep95/christie_night_mischief/2.png'
        .3
        'cg/ep95/christie_night_mischief/3.png'
        .3
        'cg/ep95/christie_night_mischief/4.png'
        .3
        'cg/ep95/christie_night_mischief/3.png'
        .3
        'cg/ep95/christie_night_mischief/2.png'
        .3
        repeat



image christie_night_mischief_lvl_2_2_tmp:

    'cg/ep95/christie_night_mischief/1.png'
    .17
    'cg/ep95/christie_night_mischief/2.png'
    .17
    'cg/ep95/christie_night_mischief/3.png'
    .17
    'cg/ep95/christie_night_mischief/4.png'
    .17
    'cg/ep95/christie_night_mischief/3.png'
    .17
    'cg/ep95/christie_night_mischief/2.png'
    .17
    repeat


image christie_night_mischief_lvl_2_3_tmp:
    'cg/ep95/christie_night_mischief/1.png'
    .08
    'cg/ep95/christie_night_mischief/2.png'
    .08
    'cg/ep95/christie_night_mischief/3.png'
    .08
    'cg/ep95/christie_night_mischief/4.png'
    .08
    'cg/ep95/christie_night_mischief/3.png'
    .08
    'cg/ep95/christie_night_mischief/2.png'
    .08
    repeat

image christie_night_mischief_lvl_2_4_tmp:
    'cg/ep95/christie_night_mischief/1.png'
    .06
    'cg/ep95/christie_night_mischief/2.png'
    .06
    'cg/ep95/christie_night_mischief/3.png'
    .06
    'cg/ep95/christie_night_mischief/4.png'
    .06
    'cg/ep95/christie_night_mischief/3.png'
    .06
    'cg/ep95/christie_night_mischief/2.png'
    .06
    repeat


image christie_night_mischief_lvl_2 1 = Composite((1920, 1080),
    (0, 0), 'christie_night_mischief_lvl_2_1_tmp',
    (0, 0), 'christie_night_mischief_lvl_2_sperm 1',
    )


image christie_night_mischief_lvl_2 2 = Composite((1920, 1080),
    (0, 0), 'christie_night_mischief_lvl_2_2_tmp',
    (0, 0), 'christie_night_mischief_lvl_2_sperm 2',
    )


image christie_night_mischief_lvl_2 3 = Composite((1920, 1080),
    (0, 0), 'christie_night_mischief_lvl_2_3_tmp',
    (0, 0), 'christie_night_mischief_lvl_2_sperm 3',
    )


image christie_night_mischief_lvl_2 4 = Composite((1920, 1080),
    (0, 0), 'christie_night_mischief_lvl_2_4_tmp',
    (0, 0), 'christie_night_mischief_lvl_2_sperm 4',
    )



image christie_night_mischief_lvl_2 end = 'cg/ep95/christie_night_mischief/end.png'

label christie_night_mischief:

    #Для Этого Комплекса Ивентов Будет Такой Общий Диалог, 
    #Который Игрок Сам Активирует Утром, Днём Или Вечером, 
    #Обращаясь К Кристи

    call show_bg_image_label from _call_show_bg_image_label_227
    call show_additional_images_label from _call_show_additional_images_label_112

    show Christie Normal
    show Christie Normal:
        xalign .85
        ypos 1085
    with Dissolve(.5)

    show GG Think
    show GG Think at go_from_left
    "[gg]" "Тебя всё ещё мучают кошмары?"
    show Christie Chagrin
    with my_dissolve
    "Кристи" "Иногда. "
    show GG Embarrassment
    with my_dissolve
    "[gg]" "Если хочешь, я могу переночевать эту ночь у тебя."
    show Christie Embarrassment
    with my_dissolve
    "Кристи" "Очень мило с твоей стороны, [gg]. "
    show GG Laughs
    with my_dissolve
    show Christie Passion
    with my_dissolve
    "Кристи" "Приходи, я только рада твоей компании. "
    $ christie_night_mischief_text = _("Зайти в спальню Кристи ночью.")
    $ new_events_christie = True
    $ Event("christie_night_mischief_night", location = "Sister_Room", button_name = "Ночные кошмары", time = ["night",])
                

    jump main_interface_label


label christie_night_mischief_night:
    #В эту же ночь моделька GG_Night_Normal 
    #должна переместиться вон из комнаты.

    #Войти в комнату Кристи, где 
    #его ожидает Kristy_Night_Normal

    $ _just_scene = False
    scene black with Dissolve(.25)
    $ renpy.pause(.25, hard = True)
    if from_gallery_check():
        $ location_now  = "Sister_Room"
        $ time.time_now = "Night"
    else:
        call show_bg_image_label from _call_show_bg_image_label_228
        call show_additional_images_label from _call_show_additional_images_label_113

        show Christie Night_Normal
        show Christie Night_Normal:
            xalign .85
            ypos 1085
        with Dissolve(.5)

        show GG Night_Normal
        show GG Night_Normal at go_from_left
        "Кристи" "Спасибо, что снова пришёл."
        "[gg]" "Всегда рад. "
        "Кристи" "Хи-хи. Давай ложиться спать."
        show GG:
            xalign .15
        with my_dissolve
        "[gg]" "Давай."

        show GG:
            easein .75 xalign .5 alpha .0
        show Christie:
            easein .75 xalign .5 alpha .0
        $ renpy.pause(.8, hard = True)
        show GG:
            xalign .5 alpha .0
        show Christie:
            xalign .5 alpha .0
        with my_dissolve
        menu:
            "1 уровень":
                $ _just_scene = True
                jump christie_root_37_scene
                #$ renpy.jump('christie_root_37_scene', _just_scene=True)
            "2 уровень":
                pass
        #"1й уровень – повторяется сцена где у нас ГГ и Кристи спят вместе."

    $ from_say_screen = False
    scene black with Dissolve(.3)
    $ renpy.pause(.3, hard = True)
    scene christie_night_mischief_lvl_2_bg




    show christie_night_mischief_lvl_2 0


    show christie_night_mischief_lvl_2_fg 0
    
    show christie_night_mischief_lvl_2_fg_0:
        alpha 0.0

    show shadow_full:
        alpha .0

    show christie_night_mischief_lvl_2_shadow
    with Dissolve(.5)






    $ renpy.pause(.2, hard = True)
    show image comic_frame_v2_master:
        zoom .7
        xpos 780
        ypos 150
        xanchor 1.0
        yanchor .47
        alpha .0

    show image comic_frame_v2_slave:
        zoom .7
        xpos 780
        ypos 150
        xanchor 1.0
        yanchor .47
        alpha .0

    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/chill-wave-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    #"2й уровень"


    #Kristy_Sleep_1
    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Я измываюсь сам{/i}"),
            __("{i}над собой, оказываясь с{/i}"),
            __("{i}ней так близко...{/i}")
            

            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7"),
            say_pos = ["r", 10],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_236 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Но не могу сдержаться{/i}"),
            __("{i}от соблазна. Она слишком{/i}"),
            __("{i}притягательная.{/i}")
            

            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7"),
            say_pos = ["r", 20],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_237 


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Её тело будоражит{/i}"),
            __("{i}мои мысли…{/i}"),
            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7_2"),
            say_pos = ["r", 20],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_238 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Руки норовят сорвать{/i}"),
            __("{i}с неё одежду, крепко{/i}"),
            __("{i}{b}{size=60}сжав{/size}{/b} её сиськи.{/i}")
            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7_2"),
            say_pos = ["r", 20],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_239 
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Кристи прекрасно{/i}"),
            __("{i}понимает это,{/i}"),
            __("{i}я уверен.{/i}")
            ), 
            size =  50,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7_2"),
            say_pos = ["r", 20],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_240 
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Хоть она и{/i}"),
            __("{i}подыгрывает мне,{/i}"),
            __("{i}соглашаясь провести{/i}"),
            __("{i}со мной ночь...{/i}")
            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7_2"),
            say_pos = ["r", 20],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_241 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}...она не торопится быть{/i}"),
            __("{i}откровенной со мной.{/i}")
            ), 
            size   = 50,
            plus_y = 7,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7_2"),
            say_pos = ["r", 20],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_242 


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Кристи снова{/i}"),
            __("{i}ожидает первых шагов…{/i}")
            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7_2"),
            say_pos = ["r", 20],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_243 


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Что ж, если от меня{/i}"),
            __("{i}требуется инициатива...{/i}")
            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7_2"),
            say_pos = ["r", 20],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_244 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}...то мне лишь остаётся{/i}"),
            __("{i}поддаться на провокацию.{/i}")
            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7_2"),
            say_pos = ["r", 20],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_245 



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Я постараюсь быть{/i}"),
            __("{i}уважительным к её сну, но…{/i}"),
            __("{i}не обещаю, что не потревожу{/i}"),
            __("{i}{size=60}её тело.{/size}{/i}")
            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7"),
            say_pos = ["r", 30],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_246 



    #Kristy_Sleep_Anal_1

        show image comic_frame_v2_master:    
            easein .2 ypos 100 alpha 0.0
        $ renpy.pause(.1, hard = True)
        
    else:


        "[gg]" "Я измываюсь сам над собой, оказываясь с ней так близко."

        "[gg]" "Но не могу сдержаться от соблазна. Она слишком притягательная. "

        "[gg]" "Её тело будоражит мои мысли…"

        "[gg]" "Руки норовят сорвать с неё одежду, крепко сжав её сиськи."

        "[gg]" "Кристи прекрасно понимает это, я уверен. "

        "[gg]" "Хоть она и подыгрывает мне, соглашаясь провести с ней ночь, она не торопится быть откровенной со мной…"

        "[gg]" "Кристи снова ожидает первых шагов…"

        "[gg]" "Что ж, если от меня требуется инициатива, то мне лишь остаётся поддаться на провокацию."

        "[gg]" "Я постараюсь быть уважительным к её сну, но… не обещаю, что не потревожу её тело."

    show image '#000a':
        alpha .0
        easein .5 alpha 1.0
    show circle_mini_game_black:
        anchor (.5, .5) alpha .0 xpos 240 ypos 770 zoom .8
        easein .5 alpha 1.0
        block:
            zoom .8
            pause .2
            easeout .25 zoom .9
            easein .25 zoom .75
            easeout .25 zoom .9
            easein .25 zoom .8
            pause 1.0
            repeat
   

    call screen rtrn_screen("christie_night_mischief_lvl_2_circle_btn_1", "christie_night_mischief_lvl_2_circle_btn_1", show_icons_interface = False, with_hovered = True)
    
    show christie_night_mischief_lvl_2_fg_0:
        alpha 1.0
        easeout .45 alpha .0

    show christie_night_mischief_lvl_2_fg 1:
       alpha .0
       easein .3 alpha 1.0
    

    #$ renpy.pause(.1, hard = True)
    show image '#000a':
        
        easein .5 alpha .5
    show circle_mini_game_black:
        
        easein .5 zoom .8 xpos 850 ypos 620 #alpha .7
        block:
            zoom .8
            pause .2
            easeout .25 zoom .9
            easein .25 zoom .75
            easeout .25 zoom .9
            easein .25 zoom .8
            pause 1.0
            repeat
    call screen rtrn_screen("christie_night_mischief_lvl_2_circle_btn_2", "christie_night_mischief_lvl_2_circle_btn_2", show_icons_interface = False, with_hovered = True)
    show circle_mini_game_black:
        
        easein .5 alpha .0
    show image '#000a':
        
        easein .5 alpha .0
    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Даааа, её мягкая попка так{/i}"),
            __("{i}рядом, и так невинна,{/i}"),
            __("{i}что мне придётся{/i}"),
            __("{i}воспользоваться именно ею.{/i}"),
            ), 
            size   = 42,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7_2"),
            say_pos = ["r", 40],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_247 



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Мой член уже достаточно{/i}"),
            __("{i}намок от возбуждения,{/i}"),
            __("{i}чтобы проникновение{/i}"),
            __("{i}было лёгким...{/i}"),
            ), 
            size   = 45,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7_2"),
            say_pos = ["r", 40],

            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_248 

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}...И приятным для{/i}"),
            __("{i}нас обоих, хе-хе.{/i}"),
            
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7"),
            say_pos = ["r", 30],

            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            
        ) from _call_comic_frame_v2_label_249 
        
    else:

        "[gg]" "Даааа, её мягкая попка так рядом, и так невинна, что мне придётся воспользоваться именно ею. "

        "[gg]" "Мой член уже достаточно намок от возбуждения, чтобы проникновение было лёгким."

        "[gg]" "И приятным для нас обоих, хе-хе."

    hide christie_night_mischief_lvl_2_fg_0
    hide image '#000a'
    hide circle_mini_game_black
    #Kristy_Sleep_Anal_2 Animation


    show christie_night_mischief_lvl_2 0_5

    with my_dissolve
    #"//Скорость х1"

    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Какого?!{/i}"),
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  80,
            plus_y = 42,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8"),
            say_pos = ["d", 30],

            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_christie_talk_shake" 
        ) from _call_comic_frame_v2_label_250

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Что он делает?..{/i}"),
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  80,
            plus_y = 42,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 400],
            show_label = "christie_night_mischief_lvl_2_christie_talk_shake",\

            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
        ) from _call_comic_frame_v2_label_251

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Я ожидала{/i}"),
            __("{i}другого.{/i}")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  80,
            plus_y = 30,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 120],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_252

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Но…{/i}"),
            __("{i}Почему бы и нет.{/i}"),
            
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  70,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 200],

            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
                ) from _call_comic_frame_v2_label_253


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}    [gg] так    {/i}"),
            __("{i}страдает по мне.{/i}")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  57,
            plus_y = 9,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 100],        
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
                ) from _call_comic_frame_v2_label_254


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Ему нужна хоть{/i}"),
            __("{i}какая-то разрядка.{/i}")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  60,
            plus_y = 10,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 250],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
                ) from _call_comic_frame_v2_label_255



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Да и я, если быть{/i}"),
            __("{i}откровенной, тоже{/i}"),
            __("{i}хочу секса…{/i}")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  70,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 400],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
                ) from _call_comic_frame_v2_label_256


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Просто, не до{/i}"),
            __("{i}конца уверена{/i}"),
            __("{i}что нужный момент{/i}"),
            __("{i}наступил.{/i}")
            
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  60,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 300],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
                ) from _call_comic_frame_v2_label_257


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Ладно, пусть{/i}"),
            __("{i}пошалит чуточку.{/i}"),
            

            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  70,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 400],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
                ) from _call_comic_frame_v2_label_258

     

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Уфф…{/i}"),
            #__("{i}Я ошибался. Туго идёт…{/i}")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  100,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .8),
            say_pos = ["r", 10],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_gg_talk_shake" 
        ) from _call_comic_frame_v2_label_259

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
           # __("{i}Уфф….{/i}"),
            __("{i}Я ошибался. Туго идёт…{/i}"),
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  60,
            plus_y = 42,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7"),
            say_pos = ["r", 5],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_gg_talk_shake"  
        ) from _call_comic_frame_v2_label_260



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Странные ощущения.{/i}"),
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  65,
            plus_y = 42,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 400],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_261

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Мне приятны его{/i}"),
          #  __("{i}{/i}"),
            __("{i}касания, но{/i}"),
            __("{size=60}{i}анус ещё противится.{/i}{/size}"),
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size   = 70,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 400],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
                ) from _call_comic_frame_v2_label_262



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i} Ах, [gg], {/i}"),
            __("{i}постарайся{/i}"),
            __("{i}быть нежнее.{/i}"),
            
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  80,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 270],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
                ) from _call_comic_frame_v2_label_263


    else:

        "Кристи" "Какого?!"

        "Кристи" "Что он делает?.."

        "Кристи" "Я ожидала другого."

        "Кристи" "Но…"

        "Кристи" "Почему бы и нет."

        "Кристи" "[gg] так страдает по мне. Ему нужна хоть какая-то разрядка. "

        "Кристи" "Да и я, если быть откровенной, тоже хочу секса…"

        "Кристи" "Просто, не до конца уверена, что нужный момент наступил."

        "Кристи" "Ладно, пусть пошалит чуточку."

        "[gg]" "Уфф…."

        "[gg]" "Я ошибался. Туго идёт…"

        "Кристи" "Странные ощущения."

        "Кристи" "Мне приятны его касания, но анус ещё противится."

        "Кристи" "Ах, [gg], постарайся быть нежнее. "


    show shadow_full:
        easein 1 alpha .2


    if preferences.language in ('eng', None, 'rus'):


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("    {i}...{/i}    "),
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  100,
            plus_y = 42,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .99),
            say_pos = ["d", -10],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_christie_talk_shake" 
        ) from _call_comic_frame_v2_label_264


        show shadow_full:
            easein 1 alpha .5
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("    {i}...{/i}    "),
            __("    {i}...{/i}    "),
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  100,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .99),
            say_pos = ["d", -10],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_christie_talk_shake" 
        ) from _call_comic_frame_v2_label_265

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Стоило бы сказать{/i}"),
            __("{i}ему это прямо,{/i}"),
            __("{i}но нет.{/i}")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  70,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 400],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_266
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Тогда он поймёт, что{/i}"),
            __("{i}я увлечена его ласками и{/i}"),
            __("{i}начнёт склонять меня{/i}"),
            #{size=100}
            __("{i}к {b}реальному{/b} сексу.{/i}")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  50,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 400],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_267

        if preferences.language == 'eng':
            $ i = 180
        else:
            $ i = 400
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Я ещё не готова…{/i}"),

            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  80,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", i],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_268



    #    "//Скорость х2"



        show image comic_frame_v2_master:    
            easein .2 ypos 200 alpha 0.0

        show shadow_full:
            easein .4 alpha .0

        $ renpy.pause(.5, hard = True)
    else:

        "Кристи" "….."

        show shadow_full:
            easein 1 alpha .5
        "Кристи" "Стоило бы сказать ему это прямо, но нет."

        "Кристи" "Тогда он поймёт, что я увлечена его ласками и начнёт склонять меня к реальному сексу."

        "Кристи" "Я ещё не готова…."


    menu christie_night_mischief_speed_up_1:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_night_mischief_speed_up_1
    show christie_night_mischief_lvl_2 1


    with my_dissolve
    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}  Ага…  {/i}"),
            __("{i}Вот так…{/i}"),
            
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            say_pos = ["r", 30],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            
        ) from _call_comic_frame_v2_label_269 
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Член уже куда{/i}"),
            __("{i}глубже проникает.{/i}"),
            
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            say_pos = ["r", 30],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            
        ) from _call_comic_frame_v2_label_270 


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}И трение стало более{/i}"),
            __("{i}мягким и приятным.{/i}"),
            
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            say_pos = ["r", 30],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            
        ) from _call_comic_frame_v2_label_271  

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Мне повезло, что я{/i}"),
            __("{i}разработал её анус раньше,{/i}"),
            __("{i}чем она успела проснуться.{/i}")
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            say_pos = ["r", 30],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            
        ) from _call_comic_frame_v2_label_272   

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Поверить не могу…{/i}"),

            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  70,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            say_pos = ["d", 400],
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_273

        if preferences.language == 'eng':
            $ i = 180
        else:
            $ i = 400
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Мне начинает{/i}"),
            __("{i}{b}нравиться{/b}…{/i}"),
            __("{size=70}{i}Я вхожу в {b}кураж{/b}…{/i}{/size}")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  80,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", i],
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_274


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i} [gg] слишком {/i}"),
            __("{i}осторожничает…{/i}")
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  80,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", 400],
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_275


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Ему стоило бы{/i}"),
            __("{i}ускориться...{/i}"),
            

            #__("{i}...иначе я сама начну двигать{/i}"),
            #__("{i}попкой, чтоб он вошёл{/i}"),
           # __("{i}в меня как можно глубже.{/i}"),
            
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  80,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", 320],
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_276

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
           # __("{i}Ему стоило бы ускориться...{/i}"),
            __("{i}...иначе я сама начну двигать{/i}"),
            __("{i}попкой, чтоб он вошёл{/i}"),
            __("{i}в меня как можно глубже.{/i}"),
            
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  40,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", 400],
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_277


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Мой член такой мокрый,{/i}"),
            __("{i}будто бы я трахаю её не{/i}"),
            __("{i}в задницу, а в киску.{/i}")
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7"),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 30],
            show_label = "christie_night_mischief_lvl_2_gg_talk_shake" 
            
        ) from _call_comic_frame_v2_label_278   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Ощущения обострились…{/i}"),
            __("{i}Мне хочется проникать{/i}"),
            __("{i}сильнее и резче.{/i}")
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7"),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 30],
            show_label = "christie_night_mischief_lvl_2_gg_talk_shake" 
            
        ) from _call_comic_frame_v2_label_279    

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Я начинаю терять над{/i}"),
            __("{i}собой контроль,{/i}"),
            __("{i}{size=55}пренебрегая осторожностью.{/size}{/i}")
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7"),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 30],
            show_label = "christie_night_mischief_lvl_2_gg_talk_shake" 
            
        ) from _call_comic_frame_v2_label_280    



        show image comic_frame_v2_master:    
            easein .2 ypos 200 alpha 0.0



        $ renpy.pause(.25, hard = True)
    else:




        "[gg]" "Ага… Вот так."

        "[gg]" "Член уже куда глубже проникает."

        "[gg]" "И трение стало более мягким и приятным."

        "[gg]" "Мне повезло, что я разработал её анус раньше, чем она успела проснуться. "

        "Кристи" "Поверить не могу…"

        "Кристи" "Мне начинает нравиться. Я вхожу в кураж. "

        "Кристи" "[gg] слишком осторожничает…"

        "Кристи" "Ему стоило бы ускориться, иначе я сама начну двигать попкой, чтоб он вошёл в меня как можно глубже."

        "[gg]" "Мой член такой мокрый, будто бы я трахаю её не в задницу, а в киску."

        "[gg]" "Ощущения обострились… Мне хочется проникать сильнее и резче. "

        "[gg]" "Я начинаю терять над собой контроль, пренебрегая осторожностью. "



    menu christie_night_mischief_speed_up_2:
        "Ускориться":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_night_mischief_speed_up_2
    show christie_night_mischief_lvl_2 2

    with my_dissolve
    if preferences.language in ('eng', None, 'rus'):
        if preferences.language == 'eng':
            $ i = 30
        else:
            $ i = 200
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("  {i}{b}Ахх…{/b}{/i}  "),
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  145,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .87),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", i],
            show_label = "christie_night_mischief_lvl_2_christie_talk_shake" 
        ) from _call_comic_frame_v2_label_281
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
           # __("{i}Ему стоило бы ускориться...{/i}"),
            __("{i}Мою попку буквально{/i}"),
            __("{i}жарят. И анус{/i}"),
            __("{i}горит от наслаждения.{/i}"),

            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  55,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", 370],
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_282
        if preferences.language == 'eng':
            $ i = 140
        else:
            $ i = 400
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
           # __("{i}Ему стоило бы ускориться...{/i}"),
            __("{i}Я чувствую эти{/i}"),
            __("{i}разряды удовольствия{/i}"),
            __("{i}по всему телу.{/i}"),

            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  55,
            plus_y = 22,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", i],
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_283


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Теперь всё выглядит{/i}"),
            __("{i}значительно лучше…{/i}"),
            
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 10],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            
        ) from _call_comic_frame_v2_label_284   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Я чуть ли не{/i}"),
            __("{i}сталкиваю её с кровати.{/i}"),
            
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 10],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            
        ) from _call_comic_frame_v2_label_285   


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Обалдеть, у{/i}"),
            __("{i}Кристи на{/i}"),
            __("{i}редкость крепкий сон.{/i}")
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 15],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            
        ) from _call_comic_frame_v2_label_286    


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Мне везёт…{/i}"),
            __("{i}Даже слишком.{/i}"),
            
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 10],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            
        ) from _call_comic_frame_v2_label_287    



        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Её дырочка плотно{/i}"),
            __("{i}сжимает мой член,{/i}"),
            __("{size=50}{i}словно удерживает насильно.{/i}{/size}")
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 10],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            
        ) from _call_comic_frame_v2_label_288     


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}С каждым движением мне{/i}"),
            __("{i}всё больше кажется, что{/i}"),
            __("{i} это не я вхожу в неё...{/i}")
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 10],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            
        ) from _call_comic_frame_v2_label_289     

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}...а она втягивает{/i}"),
            __("{i}меня в себя.{/i}"),


            ), 
            size   = 75,
            plus_y = 10,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 15],
            show_label = "christie_night_mischief_lvl_2_gg_talk_shake" 
            
        ) from _call_comic_frame_v2_label_290     
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Я начинаю думать, что она{/i}"),
            __("{i}и не спит вовсе. Всего{/i}"),
            __("{i}лишь притворяется.{/i}")
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 10],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            ) from _call_comic_frame_v2_label_291


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Но зачем ей{/i}"),
            __("{i}подыгрывать мне?..{/i}"),
            #__("{i}лишь притворяется.{/i}")
            ), 
            size   = 60,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 10],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            ) from _call_comic_frame_v2_label_292


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Разве ей не хочется придаться{/i}"),
            __("{i}этим ощущениям в открытую,{/i}"),
            __("{i}разделив со мной радость?...{/i}")
            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 15],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            ) from _call_comic_frame_v2_label_293

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Чёрт поймёт{/i}"),
            __("{i}этих женщин…{/i}"),

            ), 
            size   = 65,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 10],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            ) from _call_comic_frame_v2_label_294




        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Я вот-вот {b}{size=80}кончу{/size}{/b}…{/i}"),
            #__("{i}этих женщин…{/i}"),
            
            ), 
            size   = 70,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .8),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 10],
            show_label = "christie_night_mischief_lvl_2_gg_talk_shake" 
            ) from _call_comic_frame_v2_label_295


        show image comic_frame_v2_master:    
            easein .2 ypos 200 alpha 0.0


        $ renpy.pause(.25, hard = True)
    else:


        "Кристи" "Ахх… "

        "Кристи" "Мою попку буквально жарят."

        "Кристи" "И анус горит от наслаждения. "

        "Кристи" "Я чувствую эти разряды удовольствия по всему телу."

        "[gg]" "Теперь всё выглядит значительно лучше…"

        "[gg]" "Я чуть ли не сталкиваю её с кровати."

        "[gg]" "Обалдеть, у Кристи на редкость крепкий сон."

        "[gg]" "Мне везёт… Даже слишком."

        "[gg]" "Её дырочка плотно сжимает мой член, словно удерживает насильно."

        "[gg]" "С каждым движением мне всё больше кажется, что это не я вхожу в неё, а она втягивает меня в себя."

        "[gg]" "Я начинаю думать, что она и не спит вовсе. Всего лишь притворяется. "

        "[gg]" "Но зачем ей подыгрывать мне?.. "

        "[gg]" "Разве ей не хочется придаться этим ощущениям в открытую, разделив со мной радость?..."

        "[gg]" "Чёрт поймёт этих женщин…"

        "[gg]" "Я вот-вот кончу…"

    menu christie_night_mischief_end:
        "Кончить":
            $ pass
        "Продолжить в том же темпе":
            window hide
            $ renpy.pause(9999)
            jump christie_night_mischief_end
    show christie_night_mischief_lvl_2 3
    
    with my_dissolve
    #//Скорость х4
    if preferences.language in ('eng', None, 'rus'):
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __(" {i}{b}О боже…{/b}{/i} "),
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  110,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", 170],
            show_label = "christie_night_mischief_lvl_2_christie_talk_shake" 
        ) from _call_comic_frame_v2_label_296
        if preferences.language == 'eng':
            $ i = 120
        else:
            $ i = 280
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}{size=50}Кажется он собирается{/size}{/i}"),
            __("{i}кончить мне{/i}"),
            __("{i}прямо в попку.{/i}"),

            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  60,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", i],
            show_label = "christie_night_mischief_lvl_2_christie_talk_shake" 
        ) from _call_comic_frame_v2_label_297

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Понятия не имею,{/i}"),
            __("{i}как мне объяснить{/i}"),

            __("{i}эту ситуацию на утро.{/i}"),


            ), 
            size   = 65,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 30],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            ) from _call_comic_frame_v2_label_298

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Просто позволь мне{/i}"),
            __("{i}насладиться твоим,{/i}"),

            __("{i}телом Кристи...{/i}"),


            ), 
            size   = 70,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 30],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            ) from _call_comic_frame_v2_label_299

        if preferences.language == 'eng':
            $ i = 250
        else:
            $ i = 160
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}{b}Началось!!!{/b}{/i}"),
            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  95,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .75),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", i],
            show_label = "christie_night_mischief_lvl_2_christie_talk_shake" 
        ) from _call_comic_frame_v2_label_300
        #// Kristy_Sleep_Anal_3


       # "[gg]" "{i}Уфффффффф!!!{/i}"




        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Уфффффффф!!!{/i}"),
            #__("{i}этих женщин…{/i}"),
            
            ), 
            size   = 70,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .8),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 10],
            show_label = "christie_night_mischief_lvl_2_gg_talk_shake" 
            ) from _call_comic_frame_v2_label_301


        $ christie_night_mischief_cum_1 = Composite((1050, 180), (0, 0), Solid("#000"))
        #$ renpy.pause(.1, hard = True)
        # show image christie_root_52_cum_1:
        #     ypos  800
        #     xpos  100
        #     yanchor .5
        #     alpha 1.0

        $ christie_night_mischief_cum_2 = Composite((1020, 180), 
            #(0, 0), Solid("#000"),
            (0, 0), Frame(Transform('interface/comic_v2/bg_frame_2.png', alpha = .8), Borders(64, 64, 64, 64)),
            (20, 50), Text(
                            __("Даааааааа!....."), 
                            kerning  = 5,
                            size     = 100,
                            outlines = [(2, "#000a", 0, 0),],
                            font = "fonts/mango_comics_er.ttf",
                            
                            ),
            (1020, 60), Transform("comic_frame_say_3")
            )

        show image AlphaMask(christie_night_mischief_cum_2, At(christie_night_mischief_cum_1, christie_root_52_cum_transform)): #comic_frame_v2_0:
            
            zoom .7
            ypos  70
            xpos  150
            yanchor .5
            alpha 1.0
        hide image comic_frame_v2_master
        hide image comic_frame_v2_slave
        #show image christie_root_52_cum_2
        #show
        with my_dissolve
        $ renpy.pause(1.0)
        
        # show christie_night_mischief_lvl_2 end
        # with my_dissolve
        # $ renpy.pause(.05)
        
        
        show image '#fff'
        with Dissolve(.15)
        $ renpy.pause(.85, hard = True)

        #"[gg]" "Невозможноооооооооо!!!"
        #"ext" "Psi_Minet_END"

        #show image '#fff'
        #with Dissolve(.3)
        #$ renpy.pause(.7, hard = True)
        scene christie_night_mischief_lvl_2_bg




        show christie_night_mischief_lvl_2 end

        show christie_night_mischief_lvl_2_sperm 3
        show christie_night_mischief_lvl_2_fg 1
        


        show christie_night_mischief_lvl_2_shadow
        with Dissolve(.5)






        $ renpy.pause(.2, hard = True)
        show image comic_frame_v2_master:
            zoom .7
            xpos 780
            ypos 150
            xanchor 1.0
            yanchor .47
            alpha .0

        show image comic_frame_v2_slave:
            zoom .7
            xpos 780
            ypos 150
            xanchor 1.0
            yanchor .47
            alpha .0







        if preferences.language == 'eng':
            $ i = 320
        else:
            $ i = 160


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Внутри меня{/i}"),
            __("{i}словно целое{/i}"),
            __("{i}озеро…{/i}"),



            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  75,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .75),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", i],
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_302
        #// K

        show christie_night_mischief_lvl_2_sperm 2
        with my_dissolve
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Я сейчас запищу!!!{/i}"),
            __("{i}{size=10}{/size}{/i}"),


            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  72,
            plus_y = 50,
            line_spasing = -20, 
            say_image = Transform("comic_frame_say_8", zoom = .75),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", 250],
            show_label = "christie_night_mischief_lvl_2_christie_talk_shake" 
        ) from _call_comic_frame_v2_label_303



        if preferences.language == 'eng':
            $ i = 320
        else:
            $ i = 190
        show christie_night_mischief_lvl_2_sperm 1
        with my_dissolve
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Молчи, дурочка,{/i}"),
            __("{i}{size=90}молчи!{/size}{/i}"),


            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  75,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .75),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", i],
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_304

        hide christie_night_mischief_lvl_2_sperm
        with my_dissolve
        
        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            __("{i}Иначе вся эта ситуация{/i}"),
            __("{i}будет самым неловким{/i}"),
            __("{i}событием в твоей жизни.{/i}"),




            #, и я бы попросила не тревожить нас какое-то время.",

            ), 
            size =  50,
            plus_y = 12,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_8", zoom = .75),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["d", 240],
            show_label = "christie_night_mischief_lvl_2_christie_talk" 
        ) from _call_comic_frame_v2_label_305

        

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Чёрт, это{/i}"),
            __("{i}был странный{/i}"),

            __("{i}секс…{/i}"),


            ), 
            size   = 70,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 30],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            ) from _call_comic_frame_v2_label_306


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Да и можно ли его{/i}"),
            __("{i}таковым назвать, если{/i}"),

            __("{i}он был с девушкой, которая{/i}"),
            __("{i}спала всё это время.{/i}"),


            ), 
            size   = 50,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 30],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            ) from _call_comic_frame_v2_label_307

        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Но я в{/i}"),
            __("{i}полнейшем{/i}"),
            __("{i}восторге.{/i}"),




            ), 
            size   = 70,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 30],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            ) from _call_comic_frame_v2_label_308


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}И совершенно{/i}"),
            __("{i}измождён...{/i}"),



            ), 
            size   = 90,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 30],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            ) from _call_comic_frame_v2_label_309
        


        call comic_frame_v2_label((
            
            #_generate_text("Уффф...", size = 60), 
            
            __("{i}Наверное, просплю{/i}"),
            __("{i}до самого обеда.{/i}"),



            ), 
            size   = 75,
            plus_y = 20,
            line_spasing = 0, 
            say_image = Transform("comic_frame_say_7", zoom = .9),
            hide_label = "christie_night_mischief_lvl_2_gg_talk_hide",
            say_pos = ["r", 30],
            show_label = "christie_night_mischief_lvl_2_gg_talk" 
            ) from _call_comic_frame_v2_label_310 
    else:

        "Кристи" "О боже… Кажется он собирается кончить мне прямо в попку."

        "[gg]" "Понятия не имею, как мне объяснить эту ситуацию на утро."

        "[gg]" "Просто позволь мне насладиться твоим телом, Кристи."

        "Кристи" "Началось!!!!"

        "[gg]" "Уфффффффф!!!"

        "[gg]" "Даааааааа!....."
        scene image '#fff'
        with my_dissolve
        $ renpy.pause(1.5, hard = True)
        scene christie_night_mischief_lvl_2_bg




        show christie_night_mischief_lvl_2 end

        show christie_night_mischief_lvl_2_sperm 3
        show christie_night_mischief_lvl_2_fg 1
        with my_dissolve
        "Кристи" "Внутри меня словно целое озеро…."
        

        show christie_night_mischief_lvl_2_sperm 2
        with my_dissolve

        "Кристи" "Я сейчас запищу….!!!"
        show christie_night_mischief_lvl_2_sperm 1
        with my_dissolve

        "Кристи" "Молчи, дурочка, молчи."

        "Кристи" "Иначе вся эта ситуация будет самым неловким событием в твоей жизни."

        "[gg]" "Чёрт, это был странный секс…"

        "[gg]" "Да и можно ли его таковым назвать, если он был с девушкой, которая спала всё это время."

        "[gg]" "Но я в полнейшем восторге."

        "[gg]" "И совершенно измождён."

        "[gg]" "Наверное, просплю до самого обеда. "

    #$ add_to_gallery(38)
    python:
        try:
            del christie_night_mischief_cum_1
        except:
            pass
        
        try:
            del christie_night_mischief_cum_2
        except:
            pass

    $ add_ach('ACH_18')
    if not from_gallery_check():

        $ add_to_gallery(40)
        $ events.pop('christie_night_mischief_night', 0)
    
        $ christie_night_mischief_text = _("Надеюсь она чувствует себя лучше.")

        $ new_events_christie = True
    
        $ location_now = "Corridor"
    


        scene black with Dissolve(.5)
        $ time.time_now = "afternoon"
        $ renpy.pause(.75, hard = True)
        #$ renpy.pause(9999)


    jump main_interface_label
