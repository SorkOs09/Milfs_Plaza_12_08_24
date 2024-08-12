image hide_torchock:
    Transform('images/tests/nark.png', alpha = 0.0) with Dissolve(.1)


init 10 python:


    class TimerClassSellGame(renpy.Displayable):
        
        
        
        def __init__(self, time,  label = 'sell_game_end', with_restart = False, **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            
            
            
            
            self.time_next = None
            
            self.time      = time
            self.label     = label
            self.with_restart = with_restart
            
            
            
            
            self.time_wait  = 0
        
        def render(self, width, height, st, at):
            
            rend = renpy.Render(1920, 1080)
            if self.time <10:
                rend.blit(renpy.render(Text(str(self.time), font = 'fonts/mini_game.ttf'), 38, 475, 0.3, at), (1805, 944))
            else:
                rend.blit(renpy.render(Text(str(self.time), font = 'fonts/mini_game.ttf'), 38, 475, 0.3, at), (1796, 944))
            
            if self.time_next == None:
                
                self.time_next  = datetime.datetime.today() + datetime.timedelta(seconds=1)
                if self.with_restart:
                    renpy.restart_interaction()
            
            if datetime.datetime.today() >= self.time_next: 
            
                self.time -= 1
                
                self.time_next = None
            

            if self.time <= 0:
                
                renpy.jump(self.label)
            
            
            
            renpy.redraw(self, 0)
            
            return rend

    class SellMiniGame(renpy.Displayable):
        
        
        
        def __init__(self, **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            
            
            self.start_ticks    = pygame.time.get_ticks()
            
            self.tick_now       = None
            
            self.money          = 0
            
            self.f_time         = None 
            
            self.path           = 'images/characters/GG/emo/'
            
            self.gg_image       = Image(self.path + 'Work_1.png')
            
            self.buyers_right   = [1, 1920, 0, 0, 0, 0, 0] 
            
            self.buyers_left    = None
            
            self.factor_speed   = 9.5
            
            self.factor_spawn   = 4000
            
            
            
            self.spawn_now_left = pygame.time.get_ticks() + self.factor_spawn-500
            self.spawn_now      = pygame.time.get_ticks() + self.factor_spawn
            
            self.factor_left    = 1500
            
            self.buyer_now_right = None
            
            self.buyer_now_left = None
        
        
        
        
        
        
        
        def render(self, width, height, st, at):
            
            global stop, win, photo_game_over, player
            
            rend = renpy.Render(1920, 1080)
            
            
            if not self.tick_now:
                
                self.tick_now = pygame.time.get_ticks()
            
            self.f_time       = pygame.time.get_ticks() - self.tick_now
            
            self.tick_now     = pygame.time.get_ticks()
            
            rend.blit(renpy.render(self.gg_image, 0, 0, st, at), (660, 187))
            self.spawn      = pygame.time.get_ticks()
            self.spawn_left = pygame.time.get_ticks()
            if self.spawn_left >= self.spawn_now_left:
                self.spawn_buyer(right = False)
            if self.spawn >= self.spawn_now:
                self.spawn_buyer()
            
            
            
            i = self.buyers_right
            if i is not None:
                if i[2]:
                    if self.buyer_now_right == i:
                        self.gg_image = Image(self.path + 'Work_1.png')
                        rend.blit(renpy.render(Image('images/tests/r_g_'+str(i[0])+'.png'), 0, 0, st, at), (i[1]+210, 40))
                        rend.blit(renpy.render(Image('images/tests/nark_2.png'), 0, 0, st, at), (i[1], 187))
                    
                    else:
                        rend.blit(renpy.render(Image('images/tests/nark.png'), 0, 0, st, at), (i[1], 187))
                    
                    if i[1] < 1920:
                        i[1] += int(100*self.factor_speed*(float(self.f_time)/1000))
                    else:
                        self.buyers_right = None
                
                else:
                    if self.buyer_now_right == i:
                        self.gg_image = Image(self.path + 'Work_1.png')
                        rend.blit(renpy.render(Image('images/tests/r_g_'+str(i[0])+'.png'), 0, 0, st, at), (i[1]+180, 40))
                        rend.blit(renpy.render(Transform('images/tests/nark_2.png', xzoom = -1), 0, 0, st, at), (i[1], 187))
                    
                    else:
                        rend.blit(renpy.render(Transform('images/tests/nark.png', xzoom = -1), 0, 0, st, at), (i[1], 187))
                    
                    if i[1] > 1000:
                        i[1] -= int(100*self.factor_speed*(float(self.f_time)/600))
                    else:
                        if not i[6]:
                            i[5] = float(pygame.time.get_ticks())+self.factor_left
                            i[6] = 1
                        i[4] = float(pygame.time.get_ticks())
                        
                        if i[4] < i[5]:
                            if self.buyer_now_left is None: 
                                self.buyer_now_right = i
                        
                        else:
                            self.buyer_now_right = None
                            if self.money -2 >= 0:
                                self.money -= 2
                            show_text_animation('2$')
                            
                            tmp_text = renpy.random.choice([_('Не хочешь продавать? Ну и хер с тобой.'), _('Очередной тупой продавец.'), _('Ну и чё он встал сюда если не собирается продавать?')])
                            self.gg_image = Image(self.path + 'Work_1.png')
                            self.show_text_animation(tmp_text, 1000+300, y = 187)
                            i[2]  = 1
            
            
            x = self.buyers_left
            
            if x is not None:
                if x[2]:
                    if self.buyer_now_left == x:
                        self.gg_image = Transform(self.path + 'Work_1.png', xzoom = -1)
                        rend.blit(renpy.render(Image('images/tests/r_g_'+str(x[0])+'.png'), 0, 0, st, at), (x[1]+180, 40))
                        rend.blit(renpy.render(Transform('images/tests/nark_2.png', xzoom = -1), 0, 0, st, at), (x[1], 187))
                    
                    else:
                        rend.blit(renpy.render(Transform('images/tests/nark.png', xzoom = -1), 0, 0, st, at), (x[1], 187))
                    
                    
                    if x[1] > -300:
                        x[1] -= int(100*self.factor_speed*(float(self.f_time)/1000))
                    else:
                        self.buyers_left = None
                
                else:
                    if self.buyer_now_left == x:
                        self.gg_image = Transform(self.path + 'Work_1.png', xzoom = -1)
                        rend.blit(renpy.render(Image('images/tests/r_g_'+str(x[0])+'.png'), 0, 0, st, at), (x[1]+180, 40))
                        rend.blit(renpy.render(Image('images/tests/nark_2.png'), 0, 0, st, at), (x[1], 187))
                    
                    else:
                        rend.blit(renpy.render(Image('images/tests/nark.png'), 0, 0, st, at), (x[1], 187))
                    if x[1] < 200:
                        x[1] += int(100*self.factor_speed*(float(self.f_time)/600))
                    else:
                        if not x[6]:
                            x[5] = float(pygame.time.get_ticks())+self.factor_left
                            x[6] = 1
                        x[4] = float(pygame.time.get_ticks())
                        
                        if x[4] < x[5]:
                            if self.buyer_now_right is None: 
                                self.buyer_now_left = x
                        
                        else:
                            self.buyer_now_left = None
                            if self.money -2 >= 0:
                                self.money -= 2
                            show_text_animation('2$')
                            tmp_text = renpy.random.choice([_('Не хочешь продавать? \nНу и хер с тобой.'), _('Очередной тупой продавец.'), _('Ну и чё он встал сюда \nесли не собирается продавать?')])
                            self.gg_image = Image(self.path + 'Work_1.png')
                            self.show_text_animation(tmp_text,  100, y = 187)
                            x[2]  = 1
            
            rend.blit(renpy.render(Image('images/interface/Panel_Money.png'), 38, 475, 0.3, at), (1320, 930))
            rend.blit(renpy.render(Text(str(self.money), font = 'fonts/mini_game.ttf', outlines = [(2, "#000a", 0, 0)]), 38, 475, 0.3, at), (1380, 970))
            renpy.redraw(self, 0)
            
            return rend
        
        
        def action_button(self, good = True, left = True):
            global inventory_drugs
            inventory_drugs -= 1
            remove_from_inventory('Товар')
            x = None
            if self.buyer_now_left:
                x = self.buyer_now_left
                self.gg_image = Transform(self.path + 'Work_2.png', xzoom = -1)
            
            elif self.buyer_now_right:
                x = self.buyer_now_right
                self.gg_image = Image(self.path + 'Work_2.png')
            if x is not None:
                
                
                if x == self.buyer_now_right:
                    self.buyer_now_right = None
                else:
                    self.buyer_now_left = None
                if good == x[0]:
                    
                    self.money += 25
                    show_text_animation('+25$')
                    
                    tmp_text  = renpy.random.choice([_('Ахуенно'), _('Спасибо'), _('Супер'), _('То что я и хотел')])
                else:
                    if self.money -2 > 0:
                        self.money -= 2
                    show_text_animation('2$')
                    
                    tmp_text  = renpy.random.choice([_('Херня какая-то!'), _('Ну и зачем мне это?'), _('Что за херь ты мне всучил?')])
                x[3] = 1
                x[2] = 1
                self.show_text_animation(tmp_text, x[1]+300, y = 187)
                if inventory_drugs <= 0:
                    renpy.jump(timer_now.label)
        def spawn_buyer(self, right = True):
            
            if right:
                self.spawn = 0
                self.spawn_now = pygame.time.get_ticks() + self.factor_spawn
                self.buyers_right = [renpy.random.randint(1, 3), 1920, 0, 0, 0, 0, 0]
            else:
                self.spawn_left = 0
                self.spawn_now_left = pygame.time.get_ticks() + self.factor_spawn-500
                self.buyers_left = [renpy.random.randint(1, 3), -300, 0, 0, 0, 0, 0]
        
        
        def show_text_animation(self, text, x, y):
            Hide('text_animation_sell')()
            Show(
           'text_animation_sell', 
           text_now = str(text),
           x_now = x,
           y_now = y)()
        
        def event(self, event, x, y, st):
            pass













screen text_animation_sell(text_now, x_now, y_now):

    text unicode(text_now):
        color '#fff'
        font 'fonts/arialbi.ttf'

        italic True
        outlines [(3, "#000", 0, 0)]
        size 36
        at text_animation_up(x_now, y_now, y_now-100)


transform buyers_right_transform:

    xpos 1920 ypos 187

    linear 1.5 xpos 600

    linear 1.5 xpos 1920
transform ButtonZoomEffect:
    on idle:
        easein 0.2 zoom .9
    on hover:
        easein 0.2 zoom 1.0
screen SellMiniGameScreen:

    add sell_mini_game


    add 'sell_game_bg_interface' yalign .95 xalign .5 alpha .5
    add 'images/tests/Timer.png' xalign .5 yalign 0
    add 'search_game_2' yalign .027 xalign .5
    viewport:
        xmaximum 100
        ymaximum 100
        add '#0000'
        xalign .5 ypos 40
        text str(inventory_drugs) xalign .5 yalign .5 size 70 outlines [(2, "#000a", 0, 0)] font 'fonts/mini_game.ttf'

    hbox yalign .93 xalign .53:
        viewport:
            xmaximum 180
            ymaximum 90
            imagebutton:
                idle 'images/tests/r_g_1_s.png'
                hover 'images/tests/r_g_1_s.png'
                at ButtonZoomEffect
                action Function(sell_mini_game.action_button, good = 1)
                xanchor .5
                yanchor .5
                xalign .5
                yalign .5

        viewport:
            xmaximum 200
            ymaximum 90
            imagebutton:
                idle 'images/tests/r_g_2_s.png'
                hover 'images/tests/r_g_2_s.png'
                at ButtonZoomEffect
                action Function(sell_mini_game.action_button, good = 2)
                xanchor .5
                yanchor .5
                xalign .5
                yalign .5

        viewport:
            xmaximum 150
            ymaximum 90
            imagebutton:
                idle 'images/tests/r_g_3_s.png'
                hover 'images/tests/r_g_3_s.png'
                at ButtonZoomEffect
                action Function(sell_mini_game.action_button, good = 3)
                xanchor .5
                yanchor .5
                xalign .5
                yalign .5
    add 'images/tests/Timer.png' xalign .99 yalign .99
    add timer_now xpos -7 ypos 20

label test_lock_mini_game_screen:
    $ timer_now = TimerClassSellGame(30)
    $ sell_mini_game = SellMiniGame()

    call screen SellMiniGameScreen
    $ renpy.pause(9999999999, hard = True)



label sell_game_end:
    $ money       += sell_mini_game.money

    $ show_text_animation('+'+str(sell_mini_game.money)+' money')

    hide screen SellMiniGameScreen

    hide screen text_animation_sell

    $ time.time_now = 'night'

    $ location_now = 'City_Shop'
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
