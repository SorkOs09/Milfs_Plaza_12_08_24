image card_anim_1:

    'images/interface/cards/CardCover.png'

    .05

    '[card_now_1]'

image card_anim_1_hide:

    '[card_now_1]'

    .05

    'images/interface/cards/CardCover.png'

image card_anim_2:

    'images/interface/cards/CardCover.png'

    .05

    '[card_now_2]'

image card_anim_2_hide:

    '[card_now_2]'

    .05

    'images/interface/cards/CardCover.png'

transform cd_transform(xpos_now=0):



    on hide:

        xpos xpos_now

        linear .05 xzoom .01 xpos xpos_now+128

        linear .05 xzoom -1 xpos xpos_now
    on show:
        xpos xpos_now
        linear .05 xzoom .01 xpos xpos_now+128
        linear .05 xzoom -1 xpos xpos_now
init python:

    import copy, datetime

    def get_image_card(xpos, ypos):
        
        for im in cards_images:
            
            if im[1] == xpos and im[2] == ypos:
                
                return im[0]
        
        return False

    def image_on_table():
        
        global FirstCard, SecondCard, card_now_1, card_now_2
        
        a    = FirstCard
        
        a[0] = card_now_1
        
        cards_images.append(copy.deepcopy(a)) 
        
        
        
        
        
        
        
        cards_images.append(copy.deepcopy(a))
        
        SecondCard = None
        
        FirstCard  = None
        
        card_now_1 = None
        
        card_now_2 = None
    def get_cards_images(image):
        for i in xrange(len(cards_images)):
            if cards_images[i][0] == image:
                cards_images[i] = None
        for i in xrange(len(cards_images_time)):
            if cards_images_time[i][0] == image:
                cards_images_time[i]   = None
        if None in cards_images:
            
            cards_images.remove(None)
        if None in cards_images:
            
            cards_images.remove(None)
        if None in cards_images_time:
            
            cards_images_time.remove(None)
        if None in cards_images_time:
            
            cards_images_time.remove(None)
    class TimerClass(renpy.Displayable):
        
        
        
        def __init__(self, time,  label = 'CardGameLabelFail', **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            
            
            
            
            self.time_next = None
            
            self.time      = time
            self.label     = label
            
            
            
            
            
            self.time_wait  = 0
        
        def render(self, width, height, st, at):
            
            rend = renpy.Render(1920, 1080)
            
            rend.blit(renpy.render(Text(str(self.time), font = 'fonts/mini_game.ttf'), 38, 475, 0.3, at), (1760, 500))
            
            if self.time_next == None:
                
                self.time_next  = datetime.datetime.today() + datetime.timedelta(seconds=1)
            
            if datetime.datetime.today() >= self.time_next: 
                
                self.time -= 1
                
                self.time_next = None
                if hasattr(store, 'cards_images_time'):
                    for i in xrange(len(cards_images_time)):
                        if i < len(cards_images_time):
                            if cards_images_time[i][1] + 1 < 20:
                                cards_images_time[i][1] += 1
                            else:
                                get_cards_images(cards_images_time[i][0])
                                
                                renpy.restart_interaction()
            
            if self.time <= 0:
                
                renpy.jump(self.label)
            
            
            
            renpy.redraw(self, 0)
            
            return rend
screen CardGameScreenTimer(time=time_need_tmp):
    add timer_now
screen CardGameScreen(click=True, win='', CardAnimLabel='CardAnimLabel'):


























    viewport xpos 120 ypos 100:

        xmaximum 1920

        ymaximum 1080



        for i in xrange(0, 6):

            if get_image_card(125+275*(i), 100):

                if click:

                    imagebutton:

                        idle Transform(get_image_card(125+275*(i), 100), xzoom = -1)

                        hover Transform(get_image_card(125+275*(i), 100), xzoom = -1)

                        action NullAction()

                        at PulseButtonXzoom

                        xpos 275*(i)

                else:

                    add Transform(get_image_card(125+275*(i), 100), xzoom = -1) xpos 275*(i)

            else:

                if click:

                    imagebutton:

                        idle 'images/interface/cards/CardCover.png'

                        hover 'images/interface/cards/CardCover.png'



                        if card_now_1 == 'images/interface/cards/CardCover.png':

                            action SetVariable('card_now_1', cards[0][i]), Function(cards_images.append, [cards[0][i], 125+275*(i), 100]), SetVariable('FirstCard',  ['card_anim_1', 125+275*(i), 100]), Jump(CardAnimLabel)



                        else:

                            action SetVariable('card_now_2', cards[0][i]), Function(cards_images.append, [cards[0][i], 125+275*(i), 100]), SetVariable('SecondCard',  ['card_anim_1', 125+275*(i), 100]), Jump(CardAnimLabel)



                        at PulseButton

                        xpos 275*(i)

                else:

                    add 'images/interface/cards/CardCover.png':

                        xpos 275*(i)

        for i in xrange(0, 6):

            if get_image_card(125+275*(i), 400):

                if click:

                    imagebutton:

                        idle Transform(get_image_card(125+275*(i), 400), xzoom = -1)

                        hover Transform(get_image_card(125+275*(i), 400), xzoom = -1)

                        action NullAction()

                        at PulseButtonXzoom

                        xpos 275*(i)

                        ypos 300

                else:

                    add Transform(get_image_card(125+275*(i), 400), xzoom = -1) xpos 275*(i) ypos 300

            else:

                if click:

                    imagebutton:

                        idle 'images/interface/cards/CardCover.png'

                        hover 'images/interface/cards/CardCover.png'



                        if card_now_1 == 'images/interface/cards/CardCover.png':

                            action SetVariable('card_now_1', cards[1][i]), Function(cards_images.append, [cards[1][i], 125+275*(i), 400]), SetVariable('FirstCard',  ['card_anim_1', 125+275*(i), 400]), Jump(CardAnimLabel)



                        else:

                            action SetVariable('card_now_2', cards[1][i]), Function(cards_images.append, [cards[1][i], 125+275*(i), 400]), SetVariable('SecondCard',  ['card_anim_1', 125+275*(i), 400]), Jump(CardAnimLabel)



                        at PulseButton

                        xpos 275*(i)

                        ypos 300

                else:

                    add 'images/interface/cards/CardCover.png':

                        xpos 275*(i)

                        ypos 300

        for i in xrange(0, 6):

            if get_image_card(125+275*(i), 700):

                if click:

                    imagebutton:

                        idle Transform(get_image_card(125+275*(i), 700), xzoom = -1)

                        hover Transform(get_image_card(125+275*(i), 700), xzoom = -1)

                        action NullAction()

                        at PulseButtonXzoom

                        xpos 275*(i)

                        ypos 600

                else:

                    add Transform(get_image_card(125+275*(i), 700), xzoom = -1) xpos 275*(i) ypos 600





            else:

                if click:

                    imagebutton:

                        idle 'images/interface/cards/CardCover.png'

                        hover 'images/interface/cards/CardCover.png'



                        if card_now_1 == 'images/interface/cards/CardCover.png':

                            action SetVariable('card_now_1', cards[2][i]), Function(cards_images.append, [cards[2][i], 125+275*(i), 700]), SetVariable('FirstCard',  ['card_anim_1', 125+275*(i), 700]), Jump(CardAnimLabel)



                        else:

                            action SetVariable('card_now_2', cards[2][i]), Function(cards_images.append, [cards[2][i], 125+275*(i), 700]), SetVariable('SecondCard',  ['card_anim_1', 125+275*(i), 700]), Jump(CardAnimLabel)



                        at PulseButton

                        xpos 275*(i)

                        ypos 600

                else:

                    add 'images/interface/cards/CardCover.png':

                        xpos 275*(i)

                        ypos 600





label pre_card_game_label_1:


label card_game_label_1:

    $ timer_now = TimerClass(time_need)

    show screen CardGameScreenTimer

    $ bg_now = 'images/interface/pc_interface/pc_game_2_bg.png'

    $ time_need_tmp = time_need

    scene expression 'images/interface/pc_interface/pc_game_2_bg.png'

    $ CardCoverBlackImage2 = None

    $ CardCoverBlackImage  = None

    $ card_now_1   = 'images/interface/cards/CardCover.png'

    $ card_now_2   = 'images/interface/cards/CardCover.png'

    $ cards     = []

    $ all_cards = [

    'images/interface/cards/CardAdam.png', 

    'images/interface/cards/CardAday.png', 

    'images/interface/cards/CardCohan.png', 

    'images/interface/cards/CardLeo.png', 

    'images/interface/cards/CardLucky.png',

    'images/interface/cards/CardMaya.png',

    'images/interface/cards/CardRaj.png',

    'images/interface/cards/CardRatu.png', 

    'images/interface/cards/CardYua.png', 

    'images/interface/cards/CardAdam.png', 

    'images/interface/cards/CardAday.png', 

    'images/interface/cards/CardCohan.png', 

    'images/interface/cards/CardLeo.png', 

    'images/interface/cards/CardLucky.png',

    'images/interface/cards/CardMaya.png',

    'images/interface/cards/CardRaj.png',

    'images/interface/cards/CardRatu.png', 

    'images/interface/cards/CardYua.png', 

    ]

    $ cards_images = []

    python:

        for i in xrange(3):
            
            a = []
            
            for x in xrange(6):
                
                a.append(all_cards.pop(renpy.random.randint(0, len(all_cards)-1)))
            
            cards.append(a)





















    $ ball_now   = 3

    $ move       = 5

    $ FirstCard  = None

    $ SecondCard = None





label CardGameLabel:

    call screen CardGameScreen(win = 'CardGameLabelWin')

label CardAnimLabel:

    if card_now_2 != 'images/interface/cards/CardCover.png' and card_now_1 != 'images/interface/cards/CardCover.png':

        $ CardCoverBlackImage2 = Crop((SecondCard[1]-5, SecondCard[2], 155, 255), bg_now)

        $ CardCoverBlackImage = Crop((FirstCard[1]-5, FirstCard[2], 155, 255), bg_now)

    elif not card_now_2 != 'images/interface/cards/CardCover.png':

        $ CardCoverBlackImage = Crop((FirstCard[1]-5, FirstCard[2], 155, 255), bg_now)
    elif True:


        $ CardCoverBlackImage2 = Crop((SecondCard[1]-5, SecondCard[2], 155, 255), bg_now)



    show screen CardGameScreen(False)

























    if not card_now_2 != 'images/interface/cards/CardCover.png':

        show expression CardCoverBlackImage onlayer overlay:

            xpos FirstCard[1]-5

            ypos FirstCard[2]

        show card_anim_1 onlayer overlay:



            xpos FirstCard[1]-5

            ypos FirstCard[2]

            linear .05 xzoom .01 xpos FirstCard[1]-5+128

            linear .05 xzoom -1 xpos FirstCard[1]-5
    elif True:


        show expression CardCoverBlackImage2 onlayer overlay:

            xpos SecondCard[1]-5

            ypos SecondCard[2]

        show card_anim_2 onlayer overlay:



            xpos SecondCard[1]-5

            ypos SecondCard[2]

            linear .05 xzoom .01 xpos SecondCard[1]-5+128

            linear .05 xzoom -1 xpos SecondCard[1]-5



    pause 0.07

    if card_now_2 != 'images/interface/cards/CardCover.png' and card_now_1 != 'images/interface/cards/CardCover.png':

        pause 0.1

        if card_now_1 != card_now_2:



            show expression CardCoverBlackImage2 onlayer overlay:

                xpos SecondCard[1]-5

                ypos SecondCard[2]

            show expression CardCoverBlackImage onlayer overlay:

                xpos FirstCard[1]-5

                ypos FirstCard[2]

            show card_anim_2_hide onlayer overlay:



                xpos SecondCard[1]-5

                ypos SecondCard[2]

                linear .05 xzoom -.01 xpos SecondCard[1]-5+128

                linear .05 xzoom 1 xpos SecondCard[1]-5

            show card_anim_1_hide onlayer overlay:



                xpos FirstCard[1]-5

                ypos FirstCard[2]

                linear .05 xzoom -.01 xpos FirstCard[1]-5+128

                linear .05 xzoom 1 xpos FirstCard[1]-5



            pause .07

            hide card_anim_1_hide

            hide card_anim_2_hide

            hide card_anim_1

            hide card_anim_1

            hide CardCoverBlack

            hide CardCoverBlackImage

            python:

                for num in xrange(len(cards_images)):
                    
                    if cards_images[num][0] in [card_now_1, card_now_2]:
                        
                        cards_images[num] = None



                if None in cards_images:
                    
                    cards_images.remove(None)



                if None in cards_images:
                    
                    cards_images.remove(None)



        $ card_now_1 = 'images/interface/cards/CardCover.png'

        $ card_now_2 = 'images/interface/cards/CardCover.png'

        $ FirstCard  = None

        $ SecondCard = None



    if len(cards_images) != 18:

        jump CardGameLabel

label CardGameLabelWin:
    $ Hide('CardGameScreen')()
    $ Hide('CardGameScreenTimer')()
    scene expression 'images/interface/pc_interface/pc_game_bg.png'
    $ win_text   = _('Победа!')
    $ win_text_2 = _('You win: ')
    if not hasattr(store, 'ACH_1_count'):
        $ ACH_1_count = [False, False, False]
   
    if money_win_game  == 40:
        $ ACH_1_count[0] = True
    elif money_win_game  == 70:
        $ ACH_1_count[1] = True
    elif money_win_game  == 120:
        $ ACH_1_count[2] = True
    
   
    if all(ACH_1_count):
        $ add_ach('ACH_1')

    show expression Text(_(win_text), size = 75, font = 'fonts/mini_game.ttf'):
        xalign .5
        yalign .4

    show expression Text(_(win_text_2) + str(money_win_game)+'$', size = 75, font = 'fonts/mini_game.ttf', color = '#efff67'):
        xalign .5
        yalign .5
    with Dissolve(.5)
    $ money += money_win_game
    $ show_text_animation('+'+str(money_win_game)+'$')
    $ renpy.pause(1, hard = True)
    $ location_now = 'GG_Room'
    $ Hide('pc_game_interface')()
    $ time.time_forward()
    jump main_interface_label

label CardGameLabelFail:
    $ Hide('CardGameScreen')()
    $ Hide('CardGameScreenTimer')()
    scene expression 'images/interface/pc_interface/pc_game_bg.png'
    $ win_text   = _('Провал!')
    $ win_text_2 = _('You lose: ')

    show expression Text(_(win_text), size = 75, font = 'fonts/mini_game.ttf'):
        xalign .5
        yalign .4
    show expression Text(_(win_text_2) + str(money_win_game)+'$', size = 75, font = 'fonts/mini_game.ttf', color = '#8d1823'):
        xalign .5
        yalign .5
    with Dissolve(.5)
    $ money -= money_win_game
    $ show_text_animation(str(money_win_game)+'$')
    $ renpy.pause(1, hard = True)
    $ location_now = 'GG_Room'
    $ Hide('pc_game_interface')()
    $ time.time_forward()
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
