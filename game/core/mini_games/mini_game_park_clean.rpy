init python:
    def check_search_game():
        global search_game_ep5_arr_tmp
        for i in search_game_ep5_arr_tmp:
            for j in i:
                if not j:
                    return False
        return True    

    class CheckClickClass(renpy.Displayable):
        
        def __init__(self, **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            self.click = False
        
        def render(self, width, height, st, at):
            
            rend = renpy.Render(1920, 1080)
            
            renpy.redraw(self, 0)
            
            return rend
        
        
        def event(self, event, x, y, st):
            
            
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                self.click = True                    



    def search_game_ep5_func(y, x):
        global money, search_game_ep5_arr, search_game_ep5_arr_tmp, search_game_ep5_need_find
        
        
        if search_game_ep5_arr[y][x] == 7:
            arr = []
            
            renpy.play('audio/search_game_click_mouse.ogg')
            
            if y - 1 >= 0:
                arr.append(
                    ('mini_games/search_mini_game/items/search_game_'+str(search_game_ep5_arr[y-1][x])+'.png', 
                        280+x*129, 78+(y-1)*130,))
                search_game_ep5_arr[y-1][x] = 8
                search_game_ep5_arr_tmp[y-1][x] = 1
                
                if x-1 >= 0:
                    arr.append(
                    ('mini_games/search_mini_game/items/search_game_'+str(search_game_ep5_arr[y-1][x-1])+'.png', 
                        280+(x-1)*129, 78+(y-1)*130,))
                    search_game_ep5_arr[y-1][x-1] = 8
                    search_game_ep5_arr_tmp[y-1][x-1] = 1
                if x+1 < len(search_game_ep5_arr[y]):
                    
                    arr.append(
                    ('mini_games/search_mini_game/items/search_game_'+str(search_game_ep5_arr[y-1][x+1])+'.png', 
                        280+(x+1)*129, 78+(y-1)*130,))
                    search_game_ep5_arr[y-1][x+1] = 8
                    search_game_ep5_arr_tmp[y-1][x+1] = 1
            
            if y+1 < len(search_game_ep5_arr):
                arr.append(
                    ('mini_games/search_mini_game/items/search_game_'+str(search_game_ep5_arr[y+1][x])+'.png', 
                        280+(x)*129, 78+(y+1)*130,))
                search_game_ep5_arr[y+1][x] = 8
                search_game_ep5_arr_tmp[y+1][x] = 1
                if x-1 >= 0:
                    arr.append(
                    ('mini_games/search_mini_game/items/search_game_'+str(search_game_ep5_arr[y+1][x-1])+'.png', 
                        280+(x-1)*129, 78+(y+1)*130,))
                    search_game_ep5_arr[y+1][x-1] = 8
                    search_game_ep5_arr_tmp[y+1][x-1] = 1
                if x+1 < len(search_game_ep5_arr[y]):
                    arr.append(
                    ('mini_games/search_mini_game/items/search_game_'+str(search_game_ep5_arr[y+1][x+1])+'.png',
                        280+(x+1)*129, 78+(y+1)*130,))
                    search_game_ep5_arr[y+1][x+1] = 8
                    search_game_ep5_arr_tmp[y+1][x+1] = 1
            if x+1 < len(search_game_ep5_arr[y]):
                arr.append(
                    ('mini_games/search_mini_game/items/search_game_'+str(search_game_ep5_arr[y][x+1])+'.png', 
                        280+(x+1)*129, 78+(y)*130,))
                search_game_ep5_arr[y][x+1] = 8
                search_game_ep5_arr_tmp[y][x+1] = 1
            if x-1 >= 0:
                arr.append(
                    ('mini_games/search_mini_game/items/search_game_'+str(search_game_ep5_arr[y][x-1])+'.png', 
                        280+(x-1)*129, 78+(y)*130,))
                search_game_ep5_arr[y][x-1] = 8
                search_game_ep5_arr_tmp[y][x-1] = 1
            
            clean_game_ep5_tmp_list_func(arr)
            clean_game_ep5_tmp_func('mini_games/search_mini_game/items/search_game_7.png', 
            280+x*129, 78+y*130, .5) 
        
        else:
            renpy.play('audio/search_game_click.ogg')
            clean_game_ep5_tmp_func('mini_games/search_mini_game/search_game_block.png', 
            280+x*129, 78+y*130, .5) 
        
        search_game_ep5_arr_tmp[y][x] = 1
        if check_search_game():
            Show('end_2_search_game_ep5', transition = Dissolve(.4))()

    def search_game_ep5_func_2(y, x, image):
        global money, search_game_ep5_arr, search_game_ep5_arr_tmp, search_game_ep5_need_find
        clean_game_ep5_tmp_func(image, 
        280+x*129, 78+y*130, .5) 
        
        
        if search_game_ep5_arr[y][x] in search_game_ep5_need_find:
            search_game_ep5_need_find[search_game_ep5_arr[y][x]][2] += 1
        
        if search_game_ep5_arr[y][x] == 1:
            random_money = renpy.random.randint(1, 3)
            Hide('text_animation_sell')()
            Show(
           'text_animation_sell', 
           text_now = '+'+str(random_money)+'$',
           x_now = 1450,
           y_now = 900)()
            money += random_money
            
            renpy.play('audio/search_game_click_money.ogg')
        else:
            
            renpy.play('audio/search_game_click.ogg')
        
        search_game_ep5_arr[y][x]     = 0
        search_game_ep5_arr_tmp[y][x] = 1
        if check_search_game():
            Show('end_2_search_game_ep5', transition = Dissolve(.4))()



    def clean_game_ep5_tmp_list_func(arr):
        
        renpy.hide_screen('clean_game_ep5_tmp_list')
        renpy.show_screen('clean_game_ep5_tmp_list', arr)

    def clean_game_ep5_tmp_func(img, xp, yp, ln = 1.5):
        if xp == 'mouse':
            xp = renpy.get_mouse_pos()[0]-100
        if yp == 'mouse':
            yp = renpy.get_mouse_pos()[1]-100
        renpy.hide_screen('clean_game_ep5_tmp')
        renpy.show_screen('clean_game_ep5_tmp', img, xp, yp, ln)
    class CleaningLeafEp5(object):
        
        def __init__(self, xpos, ypos, image):
            self.xpos   = xpos + renpy.random.randint(-200, 200)
            if self.xpos <= 0:
                self.xpos = 50
            if self.xpos >= 1500:
                self.xpos = 1430
            self.ypos   = ypos + renpy.random.randint(-100, 100)
            if self.ypos <= 0:
                self.ypos = 50
            if self.ypos >= 700:
                self.ypos = 600
            
            rotate  = renpy.random.choice([10, 45, 70, 25, 85])
            zoom    = renpy.random.choice([1.0, .75, 0.9, .5])
            image = 'images/mini_games/cleaning_mini_game/'+image+'.png'
            self.image  = Transform(image, rotate = rotate, zoom = zoom)
            self.hover  = Transform(im.MatrixColor(image, im.matrix.brightness(.3)), rotate = rotate, zoom = zoom)
            
            self.click  = False


















screen clean_game_ep5_tmp(img, xp, yp, ln=1.5):

    add img at text_animation_up(xp, yp, yp-100, ln)

screen clean_game_ep5_tmp_list(arr):
    for img in arr:
        if img[0] != 'mini_games/search_mini_game/items/search_game_0.png':
            add img[0] at text_animation_up(img[1], img[2], img[2]-100, 1)


screen end_search_game_ep5:

    timer 1.5 action Show('end_2_search_game_ep5', transition = Dissolve(.5))

    imagebutton:
        idle '#0000'
        hover '#0000'
        action NullAction()


screen end_2_search_game_ep5:

    timer .5 action Function(renpy.play, 'audio/search_game_end.ogg')
    imagebutton:
        idle '#0000'
        hover '#0000'
        action Return()

    add 'search_cleaning_end'




screen search_game_ep5():
    add 'search_cleaning_bg'
    add 'search_bg' xalign .5 yalign .5
    viewport:
        xpos 282
        ypos 92
        xmaximum 900
        ymaximum 910
        add '#000a'
    vbox:
        for i in search_game_ep5_need_find:
            if search_game_ep5_need_find[i][2]:
                hbox:
                    xpos 1220 ypos 200
                    add 'search_game_' + str(i)
                    viewport:
                        pos (5, 10)
                        xmaximum 290
                        ymaximum 110
                        add '#0000'

                        $ _tmp_text = __(str(search_game_ep5_need_find[i][0]))
                        text _tmp_text color '#d5cd58' size 45-max(len(_tmp_text)-8, 0) xalign .5

                        if search_game_ep5_need_find[i][1]:
                            text str(search_game_ep5_need_find[i][2]) + '/' + str(search_game_ep5_need_find[i][1]) color '#d5cd58' size 45 yalign .7 xalign .5
                        else:
                            text str(search_game_ep5_need_find[i][2]) color '#d5cd58' size 45 yalign .75 xalign .5




    text '$'+ str(money) xpos 1450 color '#000' ypos 910
    viewport:
        xpos 260
        ypos 75
        xmaximum 1405
        ymaximum 950
        add '#0000'
        vpgrid:
            cols 7
            rows 7
            xpos 22
            ypos 22
            spacing -1
            for y in xrange(len(search_game_ep5_arr_tmp)):
                for x in xrange(len(search_game_ep5_arr_tmp[y])):
                    if search_game_ep5_arr_tmp[y][x]:
                        viewport:
                            xmaximum 130
                            ymaximum 130
                            if search_game_ep5_arr[y][x] not in [7, 8, 0]:
                                imagebutton:
                                    idle 'mini_games/search_mini_game/search_game_block_0.png'
                                    hover im.MatrixColor(
                                    'mini_games/search_mini_game/search_game_block_0.png', 
                                    im.matrix.brightness(.3))
                                    action Function(search_game_ep5_func_2, y, x, 'mini_games/search_mini_game/items/search_game_'+str(search_game_ep5_arr[y][x])+'.png')

                            add 'search_game_'+str(search_game_ep5_arr[y][x])

                    else:
                        imagebutton:
                            idle 'mini_games/search_mini_game/search_game_block.png'
                            hover im.MatrixColor(
                            'mini_games/search_mini_game/search_game_block.png', 
                            im.matrix.brightness(.3))
                            action Function(search_game_ep5_func, y, x)









































    imagebutton:
        idle 'mini_games/search_mini_game/search_close.png'
        hover im.MatrixColor(
            'mini_games/search_mini_game/search_close.png', 
            im.matrix.brightness(.3))
        focus_mask None
        xpos 1600
        ypos 20
        action Show('end_2_search_game_ep5', transition = Dissolve(.4))


screen clean_game_ep5:
    add 'search_cleaning_bg'
    add 'cleaning_bg' xalign .5 yalign .5
    default cl_fix = False

    viewport:
        xpos 158
        ypos 50
        xmaximum 1600
        ymaximum 793
        add '#000a'

        for i in clean_game_ep5_arr:

            imagebutton:
                idle i.image
                hover i.hover
                if len(clean_game_ep5_arr) == 1:


                    hovered Return()
                    action Return()

                else:

                    hovered Function(clean_game_ep5_tmp_func, i.hover, i.xpos+155, i.ypos+50), SetScreenVariable('cl_fix', True), Function(clean_game_ep5_arr.remove, i)
                    action NullAction()
                focus_mask None

                xpos i.xpos ypos i.ypos
            if cl_fix:
                add i.image xpos i.xpos ypos i.ypos

                timer .1 action SetScreenVariable('cl_fix', False)
    if not len(clean_game_ep5_arr):
        timer 2 action Return()
    viewport:
        xpos 950
        ypos 900
        xmaximum 180
        ymaximum 100
        add '#0000'



        text str(100-len(clean_game_ep5_arr)) + '%' size 65 bold True xalign .5 yalign .5 color '#000'







label search_game_label:
    $ location_now_tmp = copy.deepcopy(location_now)
    $ location_now = "City_Park_Search"
    $ check_ev         = check_events()
    $ location_now     = copy.deepcopy(location_now_tmp)
    if check_ev:
        $ Jump(check_ev.label)()

    hide  screen main_interface
    scene expression 'images/mini_games/search_cleaning_bg.png'
    $ nastroi   = max(0,  nastroi-5)
    with Dissolve(.5)

    if not getattr(store, 'cupon_search_game', False):
        $ search_game_ep5_all_items  = [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        
        15, 15, 15, 15, 15, 2, 2, 2, 2, 2, 2,

        9, 9, 9, 9, 9, 9, 11, 11, 11, 11,

        11, 11, 11, 11, 11, 1, 1, 1, 7, 7,
        
        
        7,  7, 7, 7, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 
        ]
    else:
        $ search_game_ep5_all_items  = [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        
        0, 0, 0, 0, 2, 2, 2, 2, 2, 2,

        9, 9, 9, 9, 9, 9, 11, 11, 11, 11,

        11, 11, 11, 11, 11, 1, 1, 1, 7, 7,
        
        
        7, 7, 7, 7, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 
        
        ]







    $ search_game_ep5_arr = []

    python:
        for i in xrange(7):
            search_game_ep5_arr.append([])
            for j in xrange(7):
                tmtmtmtmt = renpy.random.choice(search_game_ep5_all_items)
                search_game_ep5_all_items.remove(tmtmtmtmt)
                search_game_ep5_arr[i].append(tmtmtmtmt)










    $ search_game_ep5_arr_tmp = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    
    ]
    python:
        renpy.random.shuffle(search_game_ep5_arr)
        for i in search_game_ep5_arr:
            renpy.random.shuffle(i)

    $ search_game_ep5_need_find = {
        2:  ['Товар',   0, 0],
       
        9:  ['Яблоко',  0, 0],
        11: ['Цветок', 0, 0],
        


        
        }
    
    if not getattr(store, 'cupon_search_game', False):
        $ search_game_ep5_need_find.update({15: ['Купон «кекса»', 0, 0]})

    call screen search_game_ep5
    show screen search_game_ep5
    with None


    hide screen search_game_ep5
    hide screen end_search_game_ep5
    hide screen end_2_search_game_ep5
    hide screen text_animation_sell
    hide screen clean_game_ep5_tmp_list
    hide screen clean_game_ep5_tmp
    with Dissolve(.5)

    python:

        if not hasattr(store, 'inventory_drugs'):
            inventory_drugs = 0
        for i in xrange(min(30, search_game_ep5_need_find[2][2])):
            inventory_drugs += 1
            add_to_inventory('Товар', ncopy = True)
        for i in xrange(search_game_ep5_need_find[11][2]):
            add_to_inventory(name = 'Милый цветок', ncopy = True)

        for i in xrange(search_game_ep5_need_find[9][2]):
            add_to_inventory(name = 'Яблоко', ncopy = True)
        if 15 in search_game_ep5_need_find:
            if search_game_ep5_need_find[15][2]:
                add_to_inventory(name = 'Купон «кекса»', ncopy = True)
                store.cupon_search_game = True
            
        tmp_check_flower = get_item('Милый цветок', True)
        if tmp_check_flower and tmp_check_flower.quant >= 7:
            tmp_check_flower.quant = 0
            remove_from_inventory('Милый цветок')
            if not get_item('Букет из милых цветков', True):
                add_to_inventory(name = 'Букет из милых цветков')
            del tmp_check_flower


        if getattr(get_item('Товар', True), 'quant', 0) >= 30:
            add_ach('ACH_2')





    $ time.time_now = 'evening'
    jump main_interface_label













label mini_game_park_clean_label:
    show expression 'images/mini_games/search_cleaning_bg.png'
    show expression 'images/mini_games/cleaning_mini_game/cleaning_bg.png'
    show expression Crop((0, 0, 1600, 793),'#000a'):
        xpos 158
        ypos 50

    with Dissolve(.5)

    $ clean_game_ep5_arr = [
CleaningLeafEp5(0, 0,    'l_1'), 
CleaningLeafEp5(100, 0,  'l_2'),
CleaningLeafEp5(300, 0,  'l_3'), 
CleaningLeafEp5(400, 0,  'l_4'), 
CleaningLeafEp5(500, 0,  'l_5'), 
CleaningLeafEp5(600, 0,  'l_6'),
CleaningLeafEp5(600, 0,  'l_1'),
CleaningLeafEp5(700, 0,  'l_4'),
CleaningLeafEp5(800, 0,  'l_3'),
CleaningLeafEp5(900, 0,  'l_2'),

CleaningLeafEp5(1000, 0,  'l_1'),
CleaningLeafEp5(1100, 0,  'l_2'),
CleaningLeafEp5(1200, 0,  'l_3'),
CleaningLeafEp5(1100, 0,  'l_4'),
CleaningLeafEp5(1200, 0,  'l_5'),
CleaningLeafEp5(1200, 0,  'l_6'),

CleaningLeafEp5(0, 100,    'l_1'), 
CleaningLeafEp5(100, 100,  'l_2'),
CleaningLeafEp5(300, 100,  'l_3'), 
CleaningLeafEp5(400, 100,  'l_4'), 
CleaningLeafEp5(500, 100,  'l_5'), 
CleaningLeafEp5(600, 100,  'l_6'),
CleaningLeafEp5(600, 100,  'l_1'),
CleaningLeafEp5(700, 100,  'l_6'),
CleaningLeafEp5(800, 100,  'l_3'),
CleaningLeafEp5(900, 100,  'l_4'),

CleaningLeafEp5(1000, 100,  'l_1'),
CleaningLeafEp5(1100, 100,  'l_5'),
CleaningLeafEp5(1200, 100,  'l_2'),
CleaningLeafEp5(1300, 100,  'l_5'),
CleaningLeafEp5(1200, 100,  'l_4'),
CleaningLeafEp5(1400, 100,  'l_2'),


CleaningLeafEp5(0, 200,    'l_1'), 
CleaningLeafEp5(100, 200,  'l_5'),
CleaningLeafEp5(300, 200,  'l_3'), 
CleaningLeafEp5(400, 200,  'l_4'), 
CleaningLeafEp5(500, 200,  'l_5'), 
CleaningLeafEp5(600, 200,  'l_6'),
CleaningLeafEp5(600, 200,  'l_5'),
CleaningLeafEp5(700, 200,  'l_4'),
CleaningLeafEp5(800, 200,  'l_3'),
CleaningLeafEp5(900, 200,  'l_2'),

CleaningLeafEp5(1000, 200,  'l_1'),
CleaningLeafEp5(1100, 200,  'l_6'),
CleaningLeafEp5(1100, 200,  'l_5'),
CleaningLeafEp5(850, 200,  'l_4'),
CleaningLeafEp5(900, 200,  'l_3'),
CleaningLeafEp5(1400, 200,  'l_2'),


CleaningLeafEp5(0, 300,    'l_1'), 
CleaningLeafEp5(100, 300,  'l_2'),
CleaningLeafEp5(300, 300,  'l_3'), 
CleaningLeafEp5(400, 300,  'l_4'), 
CleaningLeafEp5(500, 300,  'l_5'), 
CleaningLeafEp5(600, 300,  'l_6'),
CleaningLeafEp5(600, 300,  'l_1'),
CleaningLeafEp5(700, 300,  'l_2'),
CleaningLeafEp5(800, 300,  'l_1'),
CleaningLeafEp5(900, 300,  'l_2'),

CleaningLeafEp5(1000, 300,  'l_4'),
CleaningLeafEp5(1100, 300,  'l_3'),
CleaningLeafEp5(900, 300,  'l_6'),
CleaningLeafEp5(950, 300,  'l_5'),
CleaningLeafEp5(850, 300,  'l_4'),
CleaningLeafEp5(1300, 300,  'l_3'),


CleaningLeafEp5(0, 400,    'l_2'), 
CleaningLeafEp5(100, 400,  'l_1'),
CleaningLeafEp5(300, 400,  'l_6'), 
CleaningLeafEp5(400, 400,  'l_5'), 
CleaningLeafEp5(500, 400,  'l_4'), 
CleaningLeafEp5(600, 400,  'l_3'),
CleaningLeafEp5(600, 400,  'l_2'),
CleaningLeafEp5(700, 400,  'l_3'),
CleaningLeafEp5(800, 400,  'l_2'),
CleaningLeafEp5(900, 400,  'l_3'),

CleaningLeafEp5(1000, 400,  'l_4'),
CleaningLeafEp5(1100, 400,  'l_5'),
CleaningLeafEp5(1050, 400,  'l_6'),
CleaningLeafEp5(1200, 400,  'l_5'),
CleaningLeafEp5(1300, 400,  'l_4'),
CleaningLeafEp5(1200, 400,  'l_3'),


CleaningLeafEp5(0, 500,    'l_1'), 
CleaningLeafEp5(100, 500,  'l_2'),
CleaningLeafEp5(300, 500,  'l_1'), 
CleaningLeafEp5(400, 500,  'l_3'), 
CleaningLeafEp5(500, 500,  'l_4'), 
CleaningLeafEp5(600, 500,  'l_5'),
CleaningLeafEp5(600, 500,  'l_6'),
CleaningLeafEp5(700, 500,  'l_5'),
CleaningLeafEp5(800, 500,  'l_4'),
CleaningLeafEp5(900, 500,  'l_3'),

CleaningLeafEp5(1000, 500,  'l_2'),
CleaningLeafEp5(1050, 500,  'l_1'),
CleaningLeafEp5(1350, 500,  'l_3'),
CleaningLeafEp5(1450, 500,  'l_4'),
CleaningLeafEp5(1450, 550,  'l_5'),
CleaningLeafEp5(980, 500,  'l_6'),

CleaningLeafEp5(50, 0,  'l_3'),
CleaningLeafEp5(100, 100,  'l_4'),
CleaningLeafEp5(50, 100,  'l_5'),
CleaningLeafEp5(0, 100,  'l_6'),

    ]
    call screen clean_game_ep5

    $ clean_game_ep5_arr = []
    show expression '#000a'

    hide screen clean_game_ep5_tmp
    show screen clean_game_ep5
    show search_cleaning_end
    with Dissolve(.5)

    call screen end_2_search_game_ep5
    call show_all_images_label from _call_show_all_images_label_16
    hide expression 'images/mini_games/cleaning_mini_game/cleaning_bg.png'
    hide expression 'images/mini_games/search_cleaning_bg.png'
    hide expression '#000a'
    hide expression Crop((0, 0, 1600, 793), '#000a')
    hide screen search_cleaning_end
    hide screen clean_game_ep5
    hide screen end_2_search_game_ep5


    with Dissolve(.5)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
