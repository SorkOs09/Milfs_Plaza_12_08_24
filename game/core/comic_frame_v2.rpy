
init python:
    class ComicFrameV2(renpy.Displayable):

        def __init__(self, text = ("!",), text_style = None, plus_y = 20, line_spasing = -5, say_point = None, name = "comic_frame", say_image = None, say_pos = ["r", 0], minimum_size_y = 128.0, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)
            self.name         = name
            self.x_size       = 100
            self.y_size       = 0
            self.say_point    = say_point
            self.say_image    = say_image
            self.say_pos      = say_pos
            self.plus_y       = plus_y+17
            self.line_spasing = line_spasing
            self.x           = []
            self.y           = []
            self.minimum_size_y = float(minimum_size_y)
            self.need_redraw = False
            if type(text_style) == Text:
                self.text_style = text_style.style
            else:
                self.text_style = Text("!", kerning = 5, size = 40, outlines = [(2, "#000a", 0, 0),], font = "fonts/mango_comics_er.ttf",).style
            #self.bg = Solid("#F00") #
            self.bg  = Frame('interface/comic_v2/bg_frame_2.png', Borders(64, 64, 64, 64)) 

            self.lines = []
            
            self.is_resized = False
            self.lines.append((0, 0))
            self.lines.append(self.bg)
            for i in text:
                if type(i) == str:
                    i = Text(
                        i, 
                        kerning  = self.text_style.kerning,
                        size     = self.text_style.size,
                        outlines = self.text_style.outlines,
                        font = "fonts/mango_comics_er.ttf",
                        
                        )
                
                x, y = i.size()
                
                self.lines.append([0, 0])
                self.lines.append(i)
                #self.y_size += y

            self.img = Composite(
                (128, 128),
                *self.lines

                )


        def set_need_redraw(self, value):
            self.need_redraw

            renpy.redraw(self, 0)

       
        def render(self, width, height, st, at):
            


            rend = renpy.Render(self.x_size, self.y_size)
            #mouse_pos = renpy.get_mouse_pos()
  

            rend.blit(renpy.render(self.img, 
                self.x_size, self.y_size, st, at), (0, 0))
            # if self.say_point:
            #     say_point_placement = renpy.display.core.displayable_by_tag("master", self.say_point).get_placement()
            #     self_placement = renpy.display.core.displayable_by_tag("master", self.comic_frame).get_placement()

            #     if say_point_placement != None and self_placement != None:
            #         p_x_0_y_0 = say_point_placement[0]
            #         p_x_5_y_0 = say_point_placement[0] + float(self.x_size)/2
            #         p_x_1_y_0 = say_point_placement[0] + self.x_size

            #         p_x_0_y_0 = say_point_placement[1]
                    
            #         p_1_1 = say_point_placement[1] + self.y_size 
            #         if say_point_placement[0] > p_0_0:
            #             if say_point_placement[1] > p_5_0
            
            if not self.is_resized:
                self.resize()
                
            
            if self.need_redraw:
                renpy.redraw(self, 0)
            return rend

        def resize(self):
            _lines = []
            _lines.append((0, 0))
            _lines.append(self.bg)
            i = 2
            max_x  = 0
            max_y  = 0
            minimum_size_x = 128.0
            

            while i < len(self.lines):
    
                if not i%2:
                    x, y = self.lines[i+1].size()
                    
                    self.lines[i][1] = max_y

                    max_y += int(y+self.line_spasing)

                    if max_x  < x:
                        max_x = x

                i += 1 

            i = 2

            
            # if max_x < minimum_size_x:
            #     max_x = minimum_size_x
            
            # if max_y < self.minimum_size_y:
            #     max_y = self.minimum_size_y
            if max_x < minimum_size_x:
                max_x  = minimum_size_x
            else:
                max_x += 80



            if max_y < self.minimum_size_y:
                move_y = True
                max_y = self.minimum_size_y
            else:
                move_y = False
                max_y += 25

            while i < len(self.lines):
    
                if not i%2:
                    
                    x = int(self.lines[i][0])
                    
                    mid = (self.lines[i+1].size()[0]/2)

                    self.lines[i][0] = int( ((max_x/2)-mid))
                    if move_y:
                        self.lines[i][1] += self.plus_y#int(self.minimum_size_y/3)
                    else:
                        self.lines[i][1] += self.plus_y
                    #int( ((max_y/2)-mid))

                    #max_y
                i += 1    
                    
            self.is_resized = True

            self.x_size = int(max_x)
            if move_y:
                self.y_size = int(max_y+self.plus_y)
            else:
                self.y_size = int(max_y+self.plus_y)

            self.y_size += 5
            if self.say_image:
                if self.say_pos[0] == "r":
                    self.lines.append((self.x_size, self.say_pos[1]))
                elif self.say_pos[0] == "l":
                    self.lines.append((-45, self.say_pos[1]))
                elif self.say_pos[0] == "u":
                    self.lines.append((self.say_pos[1], -45))
                elif self.say_pos[0] == "d":
                    self.lines.append((self.say_pos[1], self.y_size))
                
                self.lines.append(Transform(self.say_image))

            self.img = Composite(
                (self.x_size, self.y_size),
                *self.lines

                )

            renpy.redraw(self, 0)

    def _generate_text(text, kerning = 6, size = 45, outlines = [(2, "#000a", 0, 0),], font = "fonts/mango_comics_er.ttf"):
        return Text(text, kerning = kerning, size=size, outlines =outlines, font = font)
    _trd = (
            _generate_text('А может, в ней всегда', size = 20, kerning = 5),
            _generate_text('теплилась эта самоуверенность,', size = 20, kerning = 5),
            _generate_text('просто сейчас она смогла', size = 20, kerning = 6),
            _generate_text('раскрыть себя "настоящей"?', size = 20, kerning = 6),)
    


    _vdd = ComicFrameV2(_trd, plus_y = 2, line_spasing = -2)

    def comic_frame_v2_say(text_list =[],  kerning = 6, size = 45, outlines = [(2, "#000a", 0, 0),], font = "fonts/mango_comics_er.ttf", say_image = "comic_frame_say_3", plus_y = 17, say_pos = ["r", 20], line_spasing = -5, minimum_size_y = 128.0):
        r_list = []
        if type(text_list) in (unicode, str):
            text_list = __(text_list).split('\n')
        for i in text_list:
            if type(i) == Text:
                r_list.append(i)
            else:
                r_list.append(_generate_text(i, kerning = kerning, size = size, outlines = outlines, font = font))



        return ComicFrameV2(r_list, say_image = say_image, plus_y = plus_y, say_pos = say_pos, line_spasing = line_spasing, minimum_size_y = minimum_size_y)#, plus_y = 2, line_spasing = -2)
        
    i = 2

    comic_frame_v2_predict_list = ["interface/comic_v2/bg_frame_2.png",]

    for i in range(1, 10):

        comic_frame_v2_predict_list.append("interface/comic_v2/comic_frame_say_"+str(i)+".png")

#image comic_frame_say_3 = Transform("interface/comic_v2/comic_frame_say_3.png", alpha = .8)
    
image comic_frame_say_1 = Transform("interface/comic_v2/comic_frame_say_1.png")

image comic_frame_say_2 = Transform("interface/comic_v2/comic_frame_say_2.png")
    
image comic_frame_say_3 = Transform("interface/comic_v2/comic_frame_say_3.png")
image comic_frame_say_4 = Transform("interface/comic_v2/comic_frame_say_4.png")

image comic_frame_say_5 = Transform("interface/comic_v2/comic_frame_say_5.png")

image comic_frame_say_6 = Transform("interface/comic_v2/comic_frame_say_6.png")



image comic_frame_say_6_2 = Transform("interface/comic_v2/comic_frame_say_6_2.png")

image comic_frame_say_7 = Transform("interface/comic_v2/comic_frame_say_7.png", zoom = .67)



image comic_frame_say_7_2 = Transform("interface/comic_v2/comic_frame_say_7.png", zoom = .47)




image comic_frame_say_8 = Transform("interface/comic_v2/comic_frame_say_8.png")    


image comic_frame_say_9 = Transform("interface/comic_v2/comic_frame_say_9.png")    


image comic_frame_say_9_2 = Composite((100, 97),
            (0, -50), Transform("comic_frame_say_9", yzoom = -1.0),)

image comic_frame_say_10 = Transform("interface/comic_v2/comic_frame_say_10.png")    



label comic_frame_v2_label(text_list =[],  kerning = 6, size = 45, outlines = [(2, "#000a", 0, 0),], font = "fonts/mango_comics_er.ttf", say_image = "comic_frame_say_3", plus_y = 10, say_pos = ["r", 20], line_spasing = -5, minimum_size_y = 128.0, show_label = None, hide_label = None):

 #   if not store.comic_frame_v2_swap:

#        $ store.comic_frame_v2_swap = True
        
    
    if hide_label:
        $ renpy.call(hide_label)
    else:
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
            easein .2 ypos i[1]+50 alpha 0.0
        #$ renpy.pause(.2, hard = True)
    $ store.comic_frame_v2_master = comic_frame_v2_say(text_list,  kerning, size, outlines, font, say_image, plus_y, say_pos, line_spasing, minimum_size_y)

    
    if show_label:
        $ renpy.call(show_label)
    else:
        $ j = renpy.display.core.displayable_by_tag("master", "comic_frame_v2_master")
        $ i = list(j.get_placement()) + [j.xzoom, j.yzoom, j.zoom, j.alpha, j.xanchor, j.yanchor]
        

        show image comic_frame_v2_master:
            alpha 0.0
            ypos i[1]+50
            pause .1
            parallel:
                easein 0.2 ypos i[1]
            parallel:
                ease .2 alpha 1.0

        $ renpy.pause(.21, hard = True)

    "COMIC_TEST" "COMIC_TEST"


    return

        #else:

style vdd_style:
    xalign .5

screen comic_frame_v2_screen():
    
    add _vdd xalign .9 yalign .2



label comic_frame_v2_predict_label(action=renpy.start_predict, images=comic_frame_v2_predict_list):


    python:
        
        for i in images:

            action(str(i))

    return


