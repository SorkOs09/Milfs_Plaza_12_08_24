init python:

    import pygame, random


    class LockerGame(renpy.Displayable):
        
        
        
        def __init__(self, lvl = 0, image_now = 'images/mini_games/lock_mini_game/locker.png', **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            
            
            self.start_ticks    = pygame.time.get_ticks()
            
            self.tick_now       = None
            
            self.f_time         = None 
            
            self.bar_len        = 0
            
            self.lvl            = lvl
            
            self.locker_x       = 100
            
            self.right          = False
            
            self.score          = 0
            
            self.image_now      = image_now
            
            self.mouse          = False
            
            self.locker_y       = 400
            
            self.win            = 5
            
            self.fail           = False
            
            self.shaft          = False
            x_tmp = [
            -650,
            -550,
            -450,
            -350,
            -250,
            -150,
            -50,
            50,
            150,            
            ]
            y_tmp =[
            
            150,
            150, 
            100,
            150,
            110,
            100,
            150,
            70,
            120,
            ]
            random.shuffle(x_tmp)
            self.lockers_tmp = []
            for i in xrange(len(x_tmp)):
                self.lockers_tmp.append([x_tmp[i], y_tmp[i]])
            
            
            self.lockers_start = []
            self.lockers       = []
            for i in xrange(len(self.lockers_tmp)):
                
                
                self.lockers_start.append(copy.deepcopy(self.lockers_tmp[i]))
                
                self.lockers.append(copy.deepcopy(self.lockers_tmp[i]))                
        
        
        
        def copy_copy_self_lockers_start(self):
            return_lock = []
            self.win    = 5
            renpy.restart_interaction()
            for i in self.lockers_start:
                return_lock.append(copy.deepcopy(i))
            return return_lock
        def render(self, width, height, st, at):
            
            global stop, win, photo_game_over, player
            
            rend = renpy.Render(1920, 1080)
            
            if True:
                
                if not self.tick_now:
                    
                    self.tick_now = pygame.time.get_ticks()
                
                self.f_time       = pygame.time.get_ticks() - self.tick_now
                
                self.tick_now     = pygame.time.get_ticks()
                if not self.mouse:
                    if self.locker_y+160 > 560:
                        
                        self.locker_y -= int(self.lvl*400*(float(self.f_time)/1000))
                    else:
                        if self.right:
                            
                            if self.locker_x < -150:
                                
                                self.locker_x += int(self.lvl*400*(float(self.f_time)/1000))
                            
                            else:
                                
                                self.right = False
                        
                        else:
                            
                            if self.locker_x > -1200:
                                
                                self.locker_x -= int(self.lvl*400*(float(self.f_time)/1000))
                            
                            else:
                                
                                self.right = True
                
                
                if   self.locker_y+160 < 560:
                    rend.blit(renpy.render(Image(self.image_now), 38, 475, 0.3, at), (self.locker_x, 560))
                elif self.locker_y+160 > 150+500:
                    rend.blit(renpy.render(Image(self.image_now), 38, 475, 0.3, at), (self.locker_x, 150+500))
                else:
                    rend.blit(renpy.render(Image(self.image_now), 38, 475, 0.3, at), (self.locker_x, self.locker_y+160))
                
                
                
                
                for i in self.lockers:
                    rend.blit(renpy.render(Image('images/mini_games/lock_mini_game/locker_block.png'), 38, 475, 0.3, at), (i[0]+1200, i[1]+602))
                i = None
                if self.mouse:
                    i = self.check_lockers()
                if i is not None:
                    
                    
                    
                    
                    self.locker_y += int(self.lvl*400*(float(self.f_time)/1000))
                    if self.locker_y+160 > i[1]+500:
                        if i[1] < 150:
                            if not self.shaft:
                                
                                renpy.play('audio/shaft.ogg')
                                self.shaft = True
                            i[1] += int(self.lvl*400*(float(self.f_time)/1000))
                        else:
                            i[1] = 150
                            self.mouse = False
                            if self.fail:
                                renpy.play('audio/shaft.ogg')
                                self.fail = False 
                                self.lockers = self.copy_copy_self_lockers_start()
                                self.shaft = False
                            else:
                                self.shaft = False
                                self.check_end()
                else:
                    self.mouse = False
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            renpy.redraw(self, 0)
            
            
            
            
            
            return rend
        
        def check_lockers(self):
            for i in self.lockers:
                if self.locker_x+350 > i[0]-10 and self.locker_x+350 < i[0] + 90:
                    
                    
                    return i
        def check_end(self):
            self.win -= 1
            renpy.restart_interaction()
            if not self.win:
                
                renpy.end_interaction('win')
        def event(self, event, x, y, st):
            
            
            
            
            
            
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    i = self.check_lockers()
                    if i is not None and i[1] >= 150:
                        self.fail = True
                    self.mouse  = True

screen LockerGameScreen(lvl=1, image_now='images/mini_games/lock_mini_game/locker.png'):

    imagebutton:
        idle '#0009'
        hover '#0009'
        action NullAction()
    add 'locker_bg_0' ypos -100



    add lockergame ypos -100


    add 'locker_bg_1' ypos -100

    viewport xpos 1580 ypos 450:
        ymaximum 220
        xmaximum 145
        add '#0000'
        text '[lockergame.win]' xalign .5 yalign .5 bold True size 90 color '#000'

    viewport xpos 1575 ypos 760:
        imagebutton:
            idle '#0000'
            hover '#000a'
            action Function(renpy.rollback)

        xmaximum 155
        ymaximum 40

        text _('Отмена') xalign .5 yalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
