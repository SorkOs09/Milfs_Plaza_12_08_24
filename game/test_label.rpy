image test 0_1 = "cg/final_act/threesome/0/1.jpg"
image test 0_2 = "cg/final_act/threesome/0/2.jpg"

image test 1:
    "cg/final_act/threesome/1/1.png"
    .16
    "cg/final_act/threesome/1/2.png"
    .16
    "cg/final_act/threesome/1/3.png"
    .16
    "cg/final_act/threesome/1/4.png"
    .16
    "cg/final_act/threesome/1/5.png"
    .16
    "cg/final_act/threesome/1/4.png"
    .16
    "cg/final_act/threesome/1/3.png"
    .16
    "cg/final_act/threesome/1/2.png"
    .16
    repeat

image test 2:
    "cg/final_act/threesome/2/1.png"
    .16
    "cg/final_act/threesome/2/2.png"
    .16
    "cg/final_act/threesome/2/3.png"
    .16
    "cg/final_act/threesome/2/4.png"
    .16
    "cg/final_act/threesome/2/5.png"
    .16
    "cg/final_act/threesome/2/4.png"
    .16
    "cg/final_act/threesome/2/3.png"
    .16
    "cg/final_act/threesome/2/2.png"
    .16
    repeat


image test 3:
    "cg/final_act/threesome/3/1.png"
    .16
    "cg/final_act/threesome/3/2.png"
    .16
    "cg/final_act/threesome/3/3.png"
    .16
    "cg/final_act/threesome/3/4.png"
    .16
    "cg/final_act/threesome/3/3.png"
    .16
    "cg/final_act/threesome/3/2.png"
    .16
    repeat
init python:
    class TestDispl(renpy.Displayable):
        
        
        
        def __init__(self, **kwargs):

            renpy.Displayable.__init__(self, **kwargs)
            self.live2d = Live2D(
        'Resources/Bar_Tualet_5_anim', loop=False, fade = 1.0, seamless=True) #Image('Bar_Tualet_5_anim_test_0 slo')
            self.slow   = self.live2d.common.motions['slo']
            # Live2D(
            # 'Resources/Bar_Tualet_5_anim', loop=False, fade = 1.0, seamless=True)


        def render(self, width, height, st, at):
            
            rend = renpy.Render(1920, 1080)

            rend.blit(renpy.render(

                self.slow, 
            
                1920, 1080, st, at), (0, 0))


            rend.blit(renpy.render(

                Text(self.slow.st), 
            
                100, 100, st, at), (0, 0))

            
            renpy.redraw(self, 0)
            

            
            
            
            return rend
    
    ldd = TestDispl()
screen test_screen_live2d:
    add ldd

image GG_Milf_First_Sex_1_anim_test_0 = Live2D(
        'Resources/GG_Milf_First_Sex_1_anim', loop=False, seamless=True)

image Bar_Tualet_5_anim_test_0 = Live2D(
        'Resources/Bar_Tualet_5_anim', loop=True, default_fade = 1.0, seamless=True)

image Bar_Tualet_5_anim_test_1 = Live2D(
        'Resources/Bar_Tualet_5_anim', loop=True, fade = 1.0, seamless=True)


image Milf_Sex_GG_3_test_0 = Live2D(
        'Resources/Milf_Sex_GG_3', loop=True, seamless=True)


image Bar_Tualet_5_anim_test:
    'Bar_Tualet_5_anim_test_0 slo slo slo slo med med med med fast'
image GG_Milf_First_Sex_1_anim_test: 
    'GG_Milf_First_Sex_1_anim_test_0 slo slo slo slo slo slo slo slo slo slo med med med med med med med med med med med med fast'
image Milf_Sex_GG_3_test:
    'Milf_Sex_GG_3_test_0 slo slo slo slo slo slo slo slo slo slo slo med med slo slo med med med med med med med med fast'
image New_Costume_Milf_3_anim_test:
    'New_Costume_Milf_3_anim slo slo slo med med med med med med fast'
image New_Costume_Milf_2_anim_test:

    'New_Costume_Milf_2_anim slo slo slo slo med med med med fast'
    #30.0
#    '#fff' with Dissolve(.5)
    
    
    # 'Bar_Tualet_5_anim_test_1 slo'
    # 2.367
    # 'Bar_Tualet_5_anim_test_1 slo' with Dissolve(.5)
    # 2.367
    # 'Bar_Tualet_5_anim_test_1 slo' with Dissolve(.5)
    # 2.367
    # 'Bar_Tualet_5_anim_test_1 slo' with Dissolve(.1)
    # 2.367
    #9.468
    #9.465
    #'Bar_Tualet_5_anim_test_0 med'
    #2.567
    #10.268
    #10.265
    #'Bar_Tualet_5_anim_test_0 fast'
    #1.967
    #9.835
    #9.83 







image test_fg_1 = 'cg/ep4/Restaurant_Tualet/Frontground.png'
image test_fg_2 = 'cg/ep4/Restaurant_Tualet/Frontground.png'
    
label test_label:
    
    scene black

    $ renpy.pause(5.0,)
    $ location_now  = 'Hall'
    $ time.time_now = 'afternoon'
    call show_bg_image_label from _call_show_bg_image_label_246 


    show image 'cg/milf_and_sister_activities/milf_hall.png'
    with my_dissolve

    $ events.pop('steam_bonus_2', 0)
    
    show GG Passion
    show GG Passion at go_from_left()
    $ renpy.pause(.5, hard = True)
    $ from_say_screen = False
    $ renpy.pause(.5, hard = True)
    show GG Think
    with my_dissolve
    $ renpy.pause(.75, hard = True)
    
    
    #2 Ивент

    # "Разблокировка" "GREEDISGOOD"

    #Uborka_1


    # "Description" "Почему бы не составить компанию Марине, когда она убирает в Зале? Возможно, ей пригодилась бы моя помощь."


    #Активировать спрайт Марины в Зале когда она убирает. 



    #//ASS_Uborka

    

    show GG Passion
    with my_dissolve
    $ renpy.pause(.3, hard = True)
    show GG:
        easein_cubic 1.0 xalign .8
    show black
    show black:
        alpha 0.0
        easein_cubic 1.5 alpha 1.0
    $ renpy.pause(1.5, hard = True)
    scene work_ass_bg

    show work_ass 1

    show work_ass_face 1
    show Milf Invis
    show Milf Invis:
        xalign .9

    show GG Invis
    show GG Invis:
        xalign .03
    
    with my_vpunch
    $ sex_name_box = True
    $ renpy.pause(1.5, hard = True)
    show work_ass 2
    
    with my_vpunch
    $ renpy.pause(1.5, hard = True)
    #//ASS_Uborka_1anim
    show work_ass anim
    show work_ass_face 1
    with my_dissolve
    
    $ renpy.pause(6, hard = True)
    #//x2
    show work_ass anim2
    show work_ass_face 2
    with my_dissolve

    $ renpy.pause(6, hard = True)
    
    show work_ass anim3
    show work_ass_face 1
    with my_dissolve

    $ renpy.pause(6, hard = True)

    show work_ass 6

    show work_ass_face 2
    with my_vpunch
    show work_ass_cum1

    $ renpy.pause(3, hard = True)
    
    show work_ass_cum2
    show work_ass_cum2:
        pos (960, 1080) alpha 1.0
        easein_cubic 1.5 pos (960+45, 1080+35) alpha .8
    
    $ renpy.pause(6, hard = True)
    
    scene black with my_dissolve
    $ renpy.pause(10.0)
    
    "!" "!"
    jump test_label