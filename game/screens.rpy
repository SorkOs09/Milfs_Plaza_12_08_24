init offset = -1




image alpha_solid = Solid('#0000')


image red_solid = Solid('#F00a')



style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)




















init python:
    def custom_pause_statement(delay=None, music=None, with_none=None, hard=False, predict=False, checkpoint=None, modal=True):
        store.from_say_screen = False
        if hasattr(store, 'name_boxes_displ'):
        
            nameboxes = store.name_boxes_displ.nameboxes
            for i in nameboxes:
                namebox       = nameboxes[i]
                if store.who_say_now != namebox.sprite:
                    namebox.yp    = 745
                    namebox.state = "down"
                    namebox.alpha = 0.0
            
        store.who_say_now = "with_statement"
        if renpy.config.skipping == "fast":
            return False

        if checkpoint is None:
            if delay is not None:
                checkpoint = False
            else:
                checkpoint = True

        roll_forward = renpy.exports.roll_forward_info()

        if roll_forward not in [ True, False ]:
            roll_forward = None

        if (delay is not None) and renpy.game.after_rollback and not renpy.config.pause_after_rollback:

            rv = roll_forward
            if rv is None:
                rv = False

            if checkpoint:
                renpy.exports.checkpoint(rv, keep_rollback=True, hard=False)

            return rv

        renpy.exports.mode('pause')

        if music is not None:
            newdelay = renpy.audio.music.get_delay(music)

            if newdelay is not None:
                delay = newdelay

        if (delay is not None) and renpy.game.after_rollback and roll_forward is None:
            delay = 0

        if delay is None:
            afm = " "
        else:
            afm = None

        if hard or not renpy.store._dismiss_pause:
            renpy.ui.saybehavior(afm=afm, dismiss='dismiss_hard_pause', dismiss_unfocused=[])
        else:
            renpy.ui.saybehavior(afm=afm)

        if predict:
            renpy.display.interface.force_prediction = True
            renpy.ui.add(renpy.display.behavior.PredictPauseBehavior())

        try:
            rv = renpy.ui.interact(mouse='pause', type='pause', roll_forward=roll_forward, pause=delay, pause_modal=modal)
        except (renpy.game.JumpException, renpy.game.CallException) as e:
            rv = e

        if checkpoint:
            renpy.exports.checkpoint(rv, keep_rollback=True, hard=renpy.config.pause_after_rollback or (delay is None))

        if with_none is None:
            with_none = renpy.config.implicit_with_none

        if with_none:
            renpy.game.interface.do_with(None, None)

        if isinstance(rv, (renpy.game.JumpException, renpy.game.CallException)):
            raise rv

        return rv

    def custom_with_statement(trans, always=False, paired=None, clear=True):
        if hasattr(store, 'name_boxes_displ'):

            nameboxes = store.name_boxes_displ.nameboxes
            for i in nameboxes:
                namebox       = nameboxes[i]
                if store.who_say_now != namebox.sprite:
                    namebox.yp    = 745
                    namebox.state = "down"
                    namebox.alpha = 0.0
        store.who_say_now = "with_statement"
        if renpy.game.context().init_phase:
            raise Exception("With statements may not run while in init phase.")

        if renpy.config.skipping:
            trans = None

        if not (renpy.game.preferences.transitions or always): # type: ignore
            trans = None

        renpy.exports.mode('with')

        if isinstance(trans, dict):

            for k, v in trans.items():
                if k is None:
                    continue

                renpy.exports.transition(v, layer=k)

            if None not in trans:
                return

            trans = trans[None]

        return renpy.game.interface.do_with(trans, paired, clear=clear)
    
    renpy.exports.with_statement = custom_with_statement

    renpy.with_statement = custom_with_statement
    renpy.exports.pause  = custom_pause_statement
    renpy.pause          = custom_pause_statement

    def get_who_color(who):
        global gg

        if who == getattr(store, 'gg', 0) or who == '[gg]' or who == '[player_name]':
            return '#e5e349'
        if preferences.language in (None, 'rus'):
            who_colors = {
            "Жлоб" : '#8383ec',
            "Марина" : '#e1bdff',
            "Кристи" : '#FF69B4',
            "Игорь"  : '#8383ec',

            "Ночная Гостья": '#30D5C8',
            "Ночная гостья": '#30D5C8',
            "Кэт"          : '#30D5C8',
            
            "[gg]"        : '#e5e349',

            "Администратор"  : "#f192d8",

            "Мишванда"       : "#f8bc6e",

            "Миша"           : "#f8bc6e",

            }
        
        else:
            who_colors = {
            "Goon" : '#8383ec',
            "Mary" : '#e1bdff',
            "Christie" : '#FF69B4',
            "Igor"  : '#8383ec',

            "Night Stalker": '#30D5C8',
            "Night Guest": '#30D5C8',
            "Kat"          : '#30D5C8',
            
            "[gg]"        : '#e5e349',

            "Administrator"  : "#f192d8",

            "Mishvanda"      : "#f8bc6e",

            "Misha"          : "#f8bc6e",


            }
        
        
        return who_colors.get(who.title(), '#FFF') 


    def get_size(displayable, x = 0, y = 0):
        return renpy.render(renpy.easy.displayable(displayable), x, y, 0, 0).get_size()




    def create_line_for_script(name, attributes):
        
        
        def write_show_img(name, c, sprite_now):
            dspl_img = renpy.display.core.displayable_by_tag("master", name)
            return_line = sprite_now
            if dspl_img is None:
                return
            
            if getattr(dspl_img, "block", None) is None:
                return        
            
            if dspl_img.block is None:
                return
            return_line += ":\n"
            for i in dspl_img.block.statements:
                return_line +=" "*c+"    "
                if i.warper != "instance":
                    
                    return_line += i.warper + " " + str(i.duration) + " "
                
                for x in i.properties:
                    for v in x:
                        return_line += " "+ str(v)
                
                return_line += "\n"
            
            return(return_line)
        
        
        
        
        line_for_script = "show " + name
        
        
        
        line_for_script += " " + attributes
        
        
        
        filename  = renpy.game.context().next_node.filename.split("/")
        file_path = os.path.join(renpy.config.gamedir.replace("game", ""), *filename)
        
        old_name  = file_path
        
        new_name  = file_path.replace(".rpy", ".txt")
        
        line      = renpy.game.context().next_node.linenumber
        
        old_file  = open(file_path, encoding = 'utf-8')
        
        new_file  = open(file_path.replace(".rpy", ".txt"), 'w', encoding = 'utf-8')
        
        nma       = 0
        nmb       = 0
        
        already_showing = False
        
        
        c = 0
        
        
        dialogue_nodes    = []
        
        dialogue_node_tmp = []
        
        dialogue_node_change = -1
        
        
        for i in old_file:
            nmb += 1
            if '    "' in i:
                if nmb == line:
                    dialogue_node_change = nma
                dialogue_nodes.append([i, dialogue_node_tmp])
                dialogue_node_tmp = []
                nma    += 1
            else:
                dialogue_node_tmp.append(i)
        nmb = 0
        for i in range(len(dialogue_nodes)):
            get_show_st = False
            for j in dialogue_nodes[i][1]:
                if dialogue_node_change == i:
                    
                    if "show " + name in j:
                        get_show_st = True
                        c = 0
                        for x in j:
                            if x != " ":
                                break
                            c += 1
                        if ":" in j:
                            
                            new_file.write(" "*c + line_for_script+":\n")
                        elif " at " in j:
                            
                            new_file.write(" "*c + line_for_script+ " at " + j.split(" at ")[1]+"\n")
                        else:
                            new_file.write(" "*c + line_for_script+"\n")
                        nmb += 1
                        continue
                nmb += 1
                
                new_file.write(j)
            if dialogue_node_change == i:
                if not get_show_st:
                    c = 0
                    for x in dialogue_nodes[i][0]:
                        if x != " ":
                            break
                        c += 1
                    new_file.write(" "*c + line_for_script+"\n")
                    new_file.write(" "*c + "with my_dissolve\n")
            
            new_file.write(dialogue_nodes[i][0])
        
        for i in dialogue_node_tmp:
            new_file.write(i)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        new_file.close()
        
        old_file.close()
        
        os.unlink(old_name)
        
        os.rename(new_name, old_name)
        persistent.reload_for_update_sprites = True
        
        renpy.reload_script()

    music_now = None

    def close_change_music_screen():
        global music_now
        if music_now != None:
            renpy.music.stop(fadeout=.5)
            renpy.music.play(music_now, fadein = 1.5)
        Hide('change_music_screen')()

    def open_change_music_screen():
        global music_now
        music_now = renpy.music.get_playing()
        Show('change_music_screen')()

    def change_music(new_audio):
        
        renpy.music.stop(fadeout=.5)
        renpy.music.play(new_audio, fadein = 1.5)

    def create_line_for_script_audio(new_audio):
        
        
        
        line_for_script  = "$ renpy.music.stop(fadeout=.5)\n    " 
        line_for_script += "$ renpy.music.play('"+new_audio+"', fadein = 1.5)"
        
        filename  = renpy.game.context().next_node.filename.split("/")
        file_path = os.path.join(renpy.config.gamedir.replace("game", ""), *filename)
        
        old_name  = file_path
        
        new_name  = file_path.replace(".rpy", ".txt")
        
        line      = renpy.game.context().next_node.linenumber
        
        old_file  = open(file_path, encoding = 'utf-8')
        
        new_file  = open(file_path.replace(".rpy", ".txt"), 'w', encoding = 'utf-8')
        
        nma       = 0
        nmb       = 0
        
        already_showing = False
        
        
        c = 0
        
        
        dialogue_nodes    = []
        
        dialogue_node_tmp = []
        
        dialogue_node_change = -1
        
        
        for i in old_file:
            nmb += 1
            if '    "' in i:
                if nmb == line:
                    dialogue_node_change = nma
                dialogue_nodes.append([i, dialogue_node_tmp])
                dialogue_node_tmp = []
                nma    += 1
            else:
                dialogue_node_tmp.append(i)
        nmb = 0
        for i in range(len(dialogue_nodes)):
            get_show_st = False
            for j in dialogue_nodes[i][1]:
                if dialogue_node_change == i:
                    
                    if "music.play(" in j or "renpy.music.stop(" in j:
                        get_show_st = True
                        
                        c = 0
                        for xvf in j:
                            if xvf != " ":
                                break
                            c += 1
                        if "music.play(" in j:
                            
                            new_file.write(" "*c + line_for_script+"\n")
                        
                        
                        nmb += 1
                        
                        continue
                
                nmb += 1
                
                new_file.write(j)
            if dialogue_node_change == i:
                if not get_show_st:
                    c = 0
                    for x in dialogue_nodes[i][0]:
                        if x != " ":
                            break
                        c += 1
                    new_file.write(" "*c + line_for_script+"\n")
            
            
            new_file.write(dialogue_nodes[i][0])
        
        for i in dialogue_node_tmp:
            new_file.write(i)
        
        new_file.close()
        
        old_file.close()
        
        os.unlink(old_name)
        
        os.rename(new_name, old_name)
        persistent.reload_for_update_sprites = True
        
        renpy.reload_script()







screen change_music_screen():

    imagebutton:
        idle '#000b'
        hover '#000b'
        action Function(close_change_music_screen)
    vbox:
        text "Сейчас играет: " outlines [(3, '#000c', 0, 0)]
        text str(renpy.music.get_playing()) outlines [(3, '#000c', 0, 0)]
        if music_now != renpy.music.get_playing():
            textbutton " Сохранить" action Function(create_line_for_script_audio, renpy.music.get_playing()) text_outlines [(1, '#000c', 0, 0)]
    viewport:
        xalign .5
        yalign .5

        xmaximum 1300
        ymaximum 850
        add "#000a"


        viewport:
            xalign .5
            yalign .5

            xmaximum 1300
            ymaximum 850

            scrollbars 'vertical'
            mousewheel True


            has vbox
            for i in list_files:
                if "audio/" in i:
                    textbutton i[6:] action Function(change_music, i) text_outlines [(1, '#fffc', 0, 0)]



init 20 python:
    def _sorted_spirtes(sprite='GG'):
        
        if sprite not in store.custom_sprites_groups:
            return None
        
        l = list(store.custom_sprites_groups[sprite])

        l.sort()

        return l

screen change_sprite_screen(sprite="GG", attributes="Smile"):
    default group_now   = None
    
    default with_groups = _sorted_spirtes(sprite)
    
    
    default sprite_list = custom_sprites[sprite]
    
    if attributes in sprite_list:
        default sprite_n = sprite_list.index(attributes)
    else:
        default sprite_n = 0


    default dspl_img = renpy.display.core.displayable_by_tag("master", sprite)
    default get_placement = list(dspl_img.get_placement()) + [dspl_img.xzoom, dspl_img.yzoom, dspl_img.zoom, dspl_img.alpha]
    default point = get_placement[0]
    
    default x_size = get_size(dspl_img)[0]

    if type(point) == float:
        default xp = int(1920.0*point-(float(x_size) *point ))
        
    else:
        default xp = point


    imagebutton:
        idle '#000b'
        hover '#000b'
        action Hide('change_sprite_screen')
    

    

    add sprite + ' ' + sprite_list[sprite_n]:

        xpos get_placement[0]
        ypos get_placement[1]
        xanchor get_placement[2]
        yanchor get_placement[3]
        xoffset get_placement[4]
        yoffset get_placement[5]
        subpixel get_placement[6]
        xzoom get_placement[7]
        yzoom get_placement[8]
        zoom  get_placement[9]

    viewport:
        xmaximum int(x_size)
        ymaximum 100
        image 'alpha_solid'
        text str(xp+x_size+720) + ":" + str(xp)
        text str(sprite_list[sprite_n]) xalign .5 yalign .5 size 45 outlines [(1, '#fffc', 0, 0)]
        xpos int(xp)
        ypos 100

    viewport:
        xmaximum 700
        ymaximum 830






        if xp < 960:
            if xp+x_size+720 > 1920:
                xpos 1210
            else:

                xpos int(xp+x_size+20)
        else:
            xpos int(xp-720)
        #else:
        #    xpos 920
        

        imagebutton:
            idle '#000b'
            hover '#000b'
            action NullAction()
        
        textbutton "save to script file" action Function(create_line_for_script, sprite, sprite_list[sprite_n]) text_outlines [(1, '#fffc', 0, 0)]
            
        if with_groups:
            if group_now:
                hbox:
                    spacing 5
                    xalign 1.0
                    text "|" + str(group_now[2:]) + "|" ypos 5
                    textbutton "Back" action SetScreenVariable("group_now", None) text_outlines [(1, '#fffc', 0, 0)]

        viewport:
            xmaximum 700
            ymaximum 830

            scrollbars 'vertical'
            mousewheel True
            ypos 50
            has vbox
            if with_groups:
                if not group_now:
                    
                    for i in with_groups:
                        textbutton '> ' + i[2:] action SetScreenVariable('group_now', i) text_outlines [(1, '#fffc', 0, 0)]

                else:
                    for i in custom_sprites_groups[sprite][group_now]:
                        textbutton i action SetScreenVariable("sprite_n", sprite_list.index(i)) text_outlines [(1, '#fffc', 0, 0)]
            else:
                for i in sprite_list:
                    textbutton i action SetScreenVariable("sprite_n", sprite_list.index(i)) text_outlines [(1, '#fffc', 0, 0)]
            
            text '__'
   


transform SaveLoadFocusTransformUp:
    ypos 0
    easein_cubic .3 ypos 400

transform SaveLoadFocusTransformDown:
    ypos 400
    easein_cubic .3 ypos 0

init 100 python:
    
    import math
    class SaveLoadFocus(renpy.Displayable):
        
        
        
        def __init__(self, **kwargs):

            renpy.Displayable.__init__(self, **kwargs)
            self.distance = [0, 0]
            self.focused = False

            self.t_v = 1.0

            self.yp     = 300

            self.up_time_len = .75

            self.down_time_len = 1.0
            

            self.yp_len = 0

            self.yp_at_start_focused = 400

            self.yp_at_finish_focused = 400

            self.anim_time       = 0
            self.anim_time_start = datetime.datetime.now()

            _frame = AlphaMask(Solid("#000a"), 'bg_frame')
            _imagebutton = ImageButton(
            idle_image = _frame, 
            hover_image = _frame, 
            clicked = NullAction())

            self.frame  = Composite(
                (163, 400),
                (0, 0), _imagebutton,
                (47, 25), _save_load_save,
                (47, 80), _save_load_load,
                (32, 135), _save_load_q_save,
                (32, 190), _save_load_q_load,
                
                ) 
            self.width  = 163
            self.height = 400
            #self.image = SaveLoadFocusTransformDown(child = self.frame) 
        def set_focused(self, value):
            self.anim_time_start = datetime.datetime.now()
            
            # self.yp_at_start_focused = self.yp
            
            if value:
                self.yp_at_start_focused = self.yp
                self.yp_len              = self.yp
            else:
                self.yp_at_start_focused = self.yp
                self.yp_len              = 300-self.yp
                
            #if value:
            #    self.image = SaveLoadFocusTransformUp(child = self.frame)
            #else:
            #    self.image = SaveLoadFocusTransformDown(child = self.frame)
            
            self.focused = value
            renpy.restart_interaction()
        def anim_get_cords(self):

            x  = (datetime.datetime.now() - self.anim_time_start).total_seconds()
            if self.focused:
                x += .3
                x = x/self.up_time_len
            else:
                x = x/self.down_time_len

            c1 = 1.70158
            c2 = c1 * 1.525

            if x < 0.5:
                t_r = (math.pow(2 * x, 2) * ((c2 + 1) * 2 * x - c2)) / 2
            else:
                t_r = (math.pow(2 * x - 2, 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2;
            

            if x < 1.0:
                self.anim_time = x
                self.t_v = t_r
                renpy.redraw(self, 0)


            else:
                if self.anim_time != 1.0:
                    self.t_v = t_r
                    renpy.redraw(self, 0)
                self.anim_time = 1.0

            if self.focused:
                self.yp = self.yp_at_start_focused - self.t_v * self.yp_len
            else:
                self.yp = self.yp_at_start_focused + self.t_v * self.yp_len

            return t_r


            # x   = (datetime.datetime.now() - self.anim_time_start).total_seconds()*1.8
            # c1  = 1.50158
            # c3  = c1 + 1
            # t_r = 1 + c3 * math.pow(x - 1, 3) + c1 * math.pow(x - 1, 2)
            

            
            # if x < 1.0:
            #     self.anim_time = x
            #     self.t_v = t_r
            #     renpy.redraw(self, 0)


            # else:
            #     if self.anim_time != 1.0:
            #         self.t_v = t_r
            #         renpy.redraw(self, 0)
            #     self.anim_time = 1.0

            # if self.focused:
            #     self.yp = self.yp_at_start_focused - self.t_v * self.yp_len
            # else:
            #     self.yp = self.yp_at_start_focused + self.t_v * self.yp_len
            # return t_r


        def force_update(self):

            renpy.redraw(self, 0)

        def render(self, width, height, st, at):
            global persistent
            
            rend = renpy.Render(self.width, self.height+400)

            #if self.focused:
            #    if self.yp > 0:



            # rend.blit(renpy.render(Text(str(self.anim_time)), 
            #     38, 475, st, at), (0, 0))


            rend.blit(renpy.render(

                self.frame, 
            
                163, 400, st, at), (0, self.yp+30))


            if self.focused:
                
                #mouse_pos = renpy.get_mouse_pos()
                if any(
                    (
                    self.distance[0] > self.width, 
                    self.distance[1] > self.height,
                    self.distance[1] < 0,
                    self.distance[0] < 0
                    )
                    ):
                    

                    self.set_focused(False)

            self.anim_get_cords()

            
            #renpy.redraw(self, 0)
            

            
            
            
            return rend
        

        def event(self, ev, x, y, st):

            # Compute the distance between the center of this displayable and
            # the mouse pointer. The mouse pointer is supplied in x and y,
            # relative to the upper-left corner of the displayable.

            # # Base on the distance, figure out an alpha.
            # if distance <= self.opaque_distance:
            #     alpha = 1.0
            # elif distance >= self.transparent_distance:
            #     alpha = 0.0
            # else:
            #     alpha = 1.0 - 1.0 * (distance - self.opaque_distance) / (self.transparent_distance - self.opaque_distance)

            # # If the alpha has changed, trigger a redraw event.
            # if alpha != self.alpha:
            #     self.alpha = alpha
            if self.focused:
                self.distance = [x, y]
                renpy.redraw(self, 0)

            # Pass the event to our child.
            return #self.event(ev, x, y, st)

init 100 python:
    
    import math
    class ChooseQuestContext(renpy.Displayable):
        
        
        
        def __init__(self, need_end, **kwargs):

            renpy.Displayable.__init__(self, **kwargs)
            
            self.need_end = need_end
        
        def rollback(self):
            global persistent

            persistent.need_rollback_on_quest_context = False

            Rollback()()

        def render(self, width, height, st, at):
            global persistent
            
            rend = renpy.Render(1, 1)
            
            if self.need_end:
                if persistent.need_rollback_on_quest_context:
                    self.rollback()
                else:
                    renpy.end_interaction("return")

            
            
            
            return rend

    clicks = 0

    class GetMousePos(renpy.Displayable):

        def __init__(self, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)
            
       
        def render(self, width, height, st, at):
            

            rend = renpy.Render(1, 1)
            mouse_pos = renpy.get_mouse_pos()
  
            
            rend.blit(renpy.render(Text(
                str(mouse_pos), 
                outlines = [(2, "#000a", 0, 0),], 
                size     = 30 
                ), 
                100, 475, st, at), (mouse_pos[0], mouse_pos[1]))

            
            renpy.redraw(self, 0)
            
            return rend

    my_get_mouse_pos = GetMousePos()


init -500 python:
    
    names_to_sprites = {
    'Texic' : 'Texic',
    'Джеймс': 'Nikolaya',
    'James': 'Nikolaya',
    'Nikolaya': 'Nikolaya',
    'Николя': 'Nikolaya',
    'Маша':'Masha',
    'Helene':'Masha',
    'Masha':'Masha',
    'Жлоб':'Goon',
    'Марина':'Milf',
    'Mary':'Milf',
    '[gg]':'GG',
    '[player_name]':'GG',
    'Мишванда': 'Misha',
    'Misha': 'Misha',
    'Mishvanda':'Misha',
    'Mishwanda':'Misha',
    'Сьюзен':'Psi',
    'Сьюзан':'Psi',
    'BiblioGirl' : 'BiblioGirl',
    'Библиотекарша':'BiblioGirl',
            

    'Susan':'Psi',
    
    'Бандит':'BandtiWithPistol',
    'BandtiWithPistol':'BandtiWithPistol',

    'Качок':'Bandit',
    'Bandit':'Big Guy',
    'Officer':'Officer',
    'Нэнси' : 'BiblioGirl',
    'Офицер':'Officer',
    'Офицерша':'GirlOfficer',


    'Christie':'Christie',
    'Кристи':'Christie',
    'Night Stalker':'Night Stalker',

    'Ночная Гостья':'Night Stalker',
    'Ночная гостья':'Night Stalker',
    'Night Guest':'Night Guest',

    'Игорь':'Igor',

    'Igor':'Igor',
    'Зудила':'Jay',
    'Зудило':'Jay',
    'Jay':'Jay',
    'Бубнило':'Bob',
    'Bob':'Bob',
    'Кэт':'Kat',
    'Kat':'Kat',
    'Девушка':'Girl',
    'Парень':'Guy',

    }



    sprites_to_names = {

    'Goon': 'Жлоб',
    'Milf': 'Марина',
    'GG'  : '[gg]',
    }

    def get_sprite_from_name(name):
        if name == getattr(store, 'officer_name', ''):
            return 'Officer'
        if name == getattr(store, 'gg', ''):
            return 'GG'
        if name in names_to_sprites:
            return names_to_sprites[name]

    # class NameBox():
    #     def __init__(self, name, color):
    #         self.caption = caption
    #         self.action  = Return(self.caption)
init python:
    
    who_sprite = None 
    old_who_sprite = None
    #get_sprite_from_name(who)

    test_screen = None

transform show_hide_with_dur_transform(
    alpha_start = 0.0, 
    alpha_finish=1.0, 
    dur=.3,
    zoom_finish = 1.0,
    ):

    alpha alpha_start zoom zoom_finish
    easein_cubic dur alpha alpha_finish


transform show_hide_transform(
    alpha_finish=1.0, 
    zoom_finish = 1.0,
    ):
    alpha alpha_finish zoom zoom_finish
    

image textbox_flashlight = SexSayFlashLight(
    Composite(
    (1920, 1080),
    (0, 720), 'gui/textbox_flashlight.png'),
    )

init 100 python:
    store.sex_text_color = '#fffa'
    
    class SexSayFlashLight(FlashLight):

        def __init__(self, image, **kwargs):
            store.FlashLight.__init__(self, image, **kwargs)
            
        def event(self, ev, x, y, st):
            if x > 200 and x < 1820:
                if y > 820:
                    if store.sex_text_color != '#fff1':
                        store.sex_text_color = '#fff1'
                        renpy.restart_interaction()
                elif y > 780:
                    if store.sex_text_color != '#fff5':
                        store.sex_text_color = '#fff5'
                        renpy.restart_interaction()
                elif y > 720:
                    if store.sex_text_color != '#fff9':
                        store.sex_text_color = '#fff9'
                        renpy.restart_interaction()
                elif y > 700:
                    if store.sex_text_color != '#fffa':
                        store.sex_text_color = '#fffa'
                        renpy.restart_interaction()
                else:
                    if store.sex_text_color != gui.text_color:
                        store.sex_text_color = gui.text_color
                        renpy.restart_interaction()
            else:
                if store.sex_text_color != gui.text_color:
                    store.sex_text_color = gui.text_color
                    renpy.restart_interaction()

          
            renpy.redraw(self, 0)

screen say(who, what, rollback=False):
    style_prefix "say"

    $ check_for_choose_quest_context = (who == what) and who == "choose_quest_context"

    $ check_for_comic = ((who == what) and who == "COMIC_TEST") or (str(who) == "None" and str(what) == "")

    on "show" action Hide('phone_contacts_screen_2')

    default who_say_now_sprite = get_sprite_from_name(who)
    default hide_check    = who == "func" and what == "hide"
    default to_hide_check =  who == "func" and what == "to_hide"
    default to_hide_return_check =  who == "func" and what == "to_hide_return"
    
    if hide_check:

        default _dur = .28
        default _alpha_start = 0.0
        default _alpha_finish = 0.0
    elif to_hide_check or to_hide_return_check:

        default _dur = .28
        default _alpha_start = 1.0
        default _alpha_finish = 0.0
        if to_hide_return_check:
            timer .5 action Return()
    elif not from_say_screen: 
        default _dur = .28
        default _alpha_start = 0.0
        default _alpha_finish = 1.0
        timer .1 action SetVariable('from_say_screen', True)
    else:
        default _dur = 0
        default _alpha_finish = 1.0
            


    default _zoom = min(mp.dialogue_interface_scale_number, 1.4)

    add ChooseQuestContext(check_for_choose_quest_context)

    if renpy.get_screen('say') and not check_for_comic:
        
        #if who_say_now_sprite:
        on "show" action [
            SetVariable('showing_tags', renpy.get_showing_tags()),
            SetVariable('who_say_now', who_say_now_sprite),
            ]
    if store.sex_name_box:
        add store.name_boxes_displ_flashlight
    else:
        add store.name_boxes_displ
 
    if store.sex_name_box:
        image 'textbox_flashlight'
        viewport:
            ypos 720
            maximum (1920, 360)
            image 'alpha_solid'

            
            
            if _dur == 0:
                at show_hide_transform(
                    alpha_finish=_alpha_finish, 
                    zoom_finish=_zoom
                    )                    

            else:
                at show_hide_with_dur_transform(
                    alpha_start=_alpha_start,
                    alpha_finish=_alpha_finish, 
                    zoom_finish=_zoom, dur = _dur)   

            

            if not (to_hide_check or to_hide_return_check):
                use say_what_viewport(what, gui.dialogue_xpos, int(gui.dialogue_ypos*3), store.sex_text_color)
            


    window:
        id "window"

                         

                
        if check_for_choose_quest_context or check_for_comic or who == "." or store.sex_name_box:
            ypos 3000
        elif _dur == 0:
            at show_hide_transform(
                alpha_finish=_alpha_finish, 
                zoom_finish=_zoom
                )                    

        else:
            at show_hide_with_dur_transform(
                alpha_start=_alpha_start,
                alpha_finish=_alpha_finish, 
                zoom_finish=_zoom, dur = _dur)   

        if who is not None:


            window:
                id "namebox"
                style "namebox"
                text who id "who" ypos 1000

        if to_hide_check or to_hide_return_check or store.sex_name_box:
            text what xpos 1920 id "what"
        else:
            text what xpos 1920 id "what" 
            use say_what_viewport(what, gui.dialogue_xpos, gui.dialogue_ypos)
            



 

    if rollback:
        imagebutton:
            idle 'alpha_solid'
            hover 'alpha_solid'
            action Function(renpy.rollback)
    
    use debug_say_screen

screen say_what_viewport(what, xp, yp, clr = gui.text_color):
    viewport:
        xpos xp ypos yp
        maximum (1300, 170)
        image 'alpha_solid'
        text _dscr_kostil(what) color clr


init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False











screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width









init -300 python:
    class My_C_Item():
        def __init__(self, caption):
            self.caption = caption
            self.action  = Return(self.caption)

    add_translate = {
    'Спросить про духи' : 'Ask about Perfume',
    "Подарить анальную пробку" : "Gift Butt Plug",
    "Дневные шалости" : 'Let\'s "play"',
    "Ночные кошмары" : "Nightmares",
    "Лягушка":"Frog",
    "Замок на двери":"Locker on the door",
    "Говорить":"Talk",
    "Линейка":"Ruler",
    "Пикник":"Picnic",
    "Сьюзан":"Susan",
    "Отдать костюм":"Give costume",
    }

    def create_talk_with_translates():
        for i in range(len(store.check_ev_buttons)):
            j = 'tmp_names_tmp_'+str(i)
            setattr(store, j, store.check_ev_buttons[i])
            if preferences.language == 'eng':
                n = getattr(store, j, -1)
                if n in store.add_translate:
                    setattr(store, j, store.add_translate[n])

    choice_with_transform = False
    def _choice_kostil(dscr):
        
        r_dscr   = dscr
        len_dscr = len(dscr)
        if len_dscr >= 1:    
            if dscr[len_dscr-1] == '.':
                return r_dscr[:-1]

        if len_dscr >= 2:    
            if dscr[len_dscr-2] == '.' and dscr[len_dscr-2] == ' ':
                return r_dscr[:-2]

        if len_dscr >= 3:    
            if dscr[len_dscr-2] == '.' and dscr[len_dscr-2] == ' ' and dscr[len_dscr-3] == ' ':
                return r_dscr[:-3]
        

        return r_dscr
screen choice(items):
    style_prefix "choice"
    default text_now = ''


    if hasattr(store, 'tmp_menu_info'):
        if len(tmp_menu_info[1]) > 0:
            if text_now == tmp_menu_info[0]:
                add 'classic_mode'
            if text_now == tmp_menu_info[1]:
                add 'story_mode'
        else:
            if text_now != '':
                add 'mode_frame'

        viewport:
            xpos 450 ypos 635
            xmaximum 1000
            ymaximum 260
            add '#fff0'

            text str(__(text_now)) color '#fff' xalign .0 yalign .5 size 30
    vbox yalign .5:
        spacing 10
        if store.choice_with_transform:
            at show_hide_with_dur_transform(
                alpha_start=0.0,
                alpha_finish=1.0, 
                zoom_finish=mp.dialogue_interface_scale_number, dur = .28) 
             
        elif mp.dialogue_interface_scale_number != 1.0:
            at transform:
                zoom mp.dialogue_interface_scale_number


        for i in xrange(len(items)):
            if items[i].caption[0] == '!':
                textbutton _choice_kostil(__(items[i].caption[1:])):
                    if hasattr(store, 'tmp_menu_info'):
                        hovered SetScreenVariable('text_now', tmp_menu_info[i])
                        unhovered SetScreenVariable('text_now', '')

                    action NullAction()
                    text_color "#33ACFF"

                    text_font gui.text_font
            else:
                textbutton _choice_kostil(__(items[i].caption)):
                    if hasattr(store, 'tmp_menu_info'):
                        hovered SetScreenVariable('text_now', tmp_menu_info[i])
                        unhovered SetScreenVariable('text_now', '')
                    action [SetVariable('choice_with_transform', False), items[i].action]
                    text_font gui.text_font

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


init 90 python:

    _save_load_q_save_text = Text(_('Q. Save'),    font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])

    _save_load_q_load_text = Text(_('Q. Load'),    font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])
    
    _save_load_save_text = Text(_('Save'),    font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])

    _save_load_load_text = Text(_('Load'),    font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])


    _save_load_q_save = PulseButtonXzoom09Alpha(child = ImageButton(
        idle_image = _save_load_q_save_text, 
        hover_image = _save_load_q_save_text, 
        clicked = QuickSave()))

    _save_load_q_load = PulseButtonXzoom09Alpha(child = ImageButton(
        idle_image = _save_load_q_load_text, 
        hover_image = _save_load_q_load_text, 
        clicked = QuickLoad()))


    _save_load_save = PulseButtonXzoom09Alpha(child = ImageButton(
        idle_image = _save_load_save_text, 
        hover_image = _save_load_save_text, 
        clicked = ShowMenu('save')))

    _save_load_load = PulseButtonXzoom09Alpha(child = ImageButton(
        idle_image = _save_load_load_text, 
        hover_image = _save_load_load_text, 
        clicked = ShowMenu('load')))





init python:
    def my_rollback():
        global persistent
        persistent.need_rollback_on_quest_context = True
        Rollback()()

    def chage_scale(new_scale):
        if new_scale < 5:
            new_scale = 5

        elif new_scale > 20:
            new_scale = 20
        
        
        mp.interface_scale = new_scale
        mp.interface_scale_number = float(mp.interface_scale)/10
        mp.save()
        renpy.restart_interaction()
        #_screen = renpy.get_screen('need_change_scale_screen')
        
        #if _screen:
        #    renpy.display.render.redraw(_screen, 0)

    
    def chage_dialogue_scale(new_scale):
        if new_scale < 5:
            new_scale = 5

        elif new_scale > 20:
            new_scale = 20
        
        
        mp.dialogue_interface_scale = new_scale
        mp.dialogue_interface_scale_number = float(mp.dialogue_interface_scale)/10
        mp.save()
        renpy.restart_interaction()
        #_screen = renpy.get_screen('need_change_scale_screen')
        
        #if _screen:
        #    renpy.display.render.redraw(_screen, 0)
    def _save_load_focus_on_show_set_up():
        if hasattr(store, '_save_load_focus_on_show'):
            store._save_load_focus_on_show.yp = 0
            renpy.redraw(store._save_load_focus_on_show, 0)
    
    def _save_load_focus_on_show_set_down():
        if hasattr(store, '_save_load_focus_on_show'):
            store._save_load_focus_on_show.yp = 300
            renpy.redraw(store._save_load_focus_on_show, 0)
    
    def scale_tutorial_def():
        #if hasattr(store, '_save_load_focus_on_show'):
            # store._save_load_focus_on_show.yp = 0
            # renpy.redraw(store._save_load_focus_on_show, 0)
        mp.scale_tutorial = True
        mp.save()
    need_change_scale = False

    def my_null():
        pass

    _default_obj_text = Text(_('Save-Load'),    font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])

    def _save_load_focus_on_show_set_focused(value):
        store._save_load_focus_on_show.set_focused(value)

    _save_load_menu_button_to_true = ImageButton(idle_image = "zero_solid", hover_image = "zero_solid", hovered = Function(_save_load_focus_on_show_set_focused, True),  clicked = NullAction()) 
    
    _save_load_menu_button_to_false = ImageButton(idle_image = "zero_solid", hover_image = "zero_solid", hovered = Function(_save_load_focus_on_show_set_focused, False),  clicked = NullAction()) 
    
    _save_load_focus = False

    _scale   = Text(_('Scale'),   font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])
    _prefs   = Text(_('Prefs '),   font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])



   #_alpha_0 =  Text(_('Save-Load'),    font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)], alpha = 0.0)
    _quick_menu_idle  = "interface/quick_menu_idle.png"

    _quick_menu_hover = "interface/quick_menu_hover.png"


    def _do_actions(actions):
        for i in actions:
            i()

    _quick_menu_back_idle = Crop((0,35,52,50), _quick_menu_idle)

    _quick_menu_back_hover = Crop((0,35,52,50), _quick_menu_hover)

    _quick_menu_play_idle  = Crop((52,35,40,50), _quick_menu_idle)

    _quick_menu_play_hover = Crop((52,35,40,50), _quick_menu_hover)




    
    _quick_menu_pause_idle  =  Composite(
                                (40, 85),
                                (10, 0), Crop((325,35,25,50), _quick_menu_idle))

    _quick_menu_pause_hover  =  Composite(
                                (40, 85),
                                (10, 0), Crop((325,35,25,50), _quick_menu_hover))




    _quick_menu_skip_idle  = Crop((92,35,33,50), _quick_menu_idle)

    _quick_menu_skip_hover = Crop((92,35,33,50), _quick_menu_hover)


    _quick_menu_q_load_idle  = Crop((125,35,50,50), _quick_menu_idle)

    _quick_menu_q_load_hover = Crop((125,35,50,50), _quick_menu_hover)




    _quick_menu_q_save_idle  = Crop((175,35,50,50), _quick_menu_idle)

    _quick_menu_q_save_hover = Crop((175,35,50,50), _quick_menu_hover)



    _quick_menu_prefs_idle  = Crop((225,35,40,50), _quick_menu_idle)

    _quick_menu_prefs_hover = Crop((225,35,40,50), _quick_menu_hover)



    _quick_menu_scale_idle  = Crop((265,35,40,50), _quick_menu_idle)

    _quick_menu_scale_hover = Crop((265,35,40,50), _quick_menu_hover)



    





    _alpha_0_imagebutton = Transform(child =ImageButton(idle_image = _default_obj_text, hover_image = _default_obj_text, clicked = NullAction()), alpha = .0 ) #ImageButton(idle_image = _alpha_0, hover_image = _alpha_0, clicked=[NullAction(), ])
    _q_load  = Transform(Text(_('Q.Load'),  font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)]))#, alpha = 0.0)
    _q_save  = Transform(Text(_('Q.Save'),  font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)]))#, alpha = 0.0)
    _save    = Transform(Text(_('Save'),    font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)]))#, alpha = 0.0)
    _load    = Text(_('Load'),    font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])#, alpha = 0.0)
    
    _save_load = Text(_('Save-Load'),    font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])
        
    _auto_en = Text(_('|>'), bold = True, font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])
    
    _skip    = Text(_('>>'),    font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])
    
    _history = Text(_('History'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])
    
    _back    = Text(_('<<'),    font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])

    _pause    = Text(_('Stop'),    font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])

    _play    = Text(_('Auto'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])

    _send_bug_report_t = 'interface/report_button.png' #Text(_('Send Bug Report'), font = 'fonts/mini_game.ttf', outlines = [
        #(3, '#F00c', 0, 0)])

    _send_bug_report_t_hover = 'interface/report_button_hover.png' #Text(_('Send Bug Report'), font = 'fonts/mini_game.ttf', outlines = [
    

    def _get_quick_menu_button_image(idle = "zero_solid", hover = "zero_solid", clicked = [NullAction(), ], alternate = None):
        if type(clicked) not in (tuple, list):
            clicked = (clicked, )
        


        clicked = Function(_do_actions, clicked)

        if alternate != None:
            if type(alternate) not in (tuple, list):
                alternate = (alternate, )
            alternate =  Function(_do_actions, alternate)


        return _quick_menu_transform(child = 
            ImageButton(
                idle_image  = idle, 
                hover_image = hover, 
                clicked     = clicked, 
                alternate   = alternate,
                focus_mask  = None,
                )
            )

    _quick_menu_send_bug_report_hover_check = False
    _quick_menu_send_bug_report_hover_check_to_True  = Function(_do_actions, (SetVariable('_quick_menu_send_bug_report_hover_check', True), renpy.restart_interaction))
    _quick_menu_send_bug_report_hover_check_to_False = Function(_do_actions, (SetVariable('_quick_menu_send_bug_report_hover_check', False), renpy.restart_interaction))
    



transform _quick_menu_transform:
    alpha 1.0

    on idle:
        alpha 1.0 

    on hover:
        alpha .5
        easein .25 alpha 1.0










image _quick_menu_back_button = _get_quick_menu_button_image(
    _quick_menu_back_idle,
    _quick_menu_back_hover,
    Rollback(),
    )

    
image _quick_menu_pause_idle = _quick_menu_pause_idle

image _quick_menu_pause_hover = _quick_menu_pause_hover




image _quick_menu_play_pause_button_False_idle = _quick_menu_play_idle


image _quick_menu_play_pause_button_True_idle = _quick_menu_pause_idle

image _quick_menu_play_pause_button_False = _get_quick_menu_button_image(
    _quick_menu_play_idle,
    _quick_menu_play_hover,
    Preference("auto-forward", "enable"),
    )

image _quick_menu_play_pause_button_True = _get_quick_menu_button_image(
    _quick_menu_pause_hover,
    _quick_menu_pause_hover,
    Preference("auto-forward", "disable"),
    )

image _quick_menu_skip_button = _get_quick_menu_button_image(
    _quick_menu_skip_idle,
    _quick_menu_skip_hover,
    Skip(),
    Skip(fast=True, confirm=True)
    )



image _quick_menu_q_load_button = _get_quick_menu_button_image(
    _quick_menu_q_load_idle,
    _quick_menu_q_load_hover,
    QuickSave(),
    )



image _quick_menu_q_save_button = _get_quick_menu_button_image(
    _quick_menu_q_save_idle,
    _quick_menu_q_save_hover,
    QuickLoad(),
    )



image _quick_menu_prefs_button = _get_quick_menu_button_image(
    _quick_menu_prefs_idle,
    _quick_menu_prefs_hover,
    ShowMenu('preferences'),
    )

image _quick_menu_scale_button = _get_quick_menu_button_image(
    _quick_menu_scale_idle,
    _quick_menu_scale_hover,
    [Function(scale_tutorial_def), ShowMenu("preferences", need_change_scale_screen = True)],
    )


                






image _quick_menu = Composite(

(350, 50),

(0, 0), "_quick_menu_back_button", 

(52, 0), "_quick_menu_play_pause_button_[preferences.afm_enable]",

(92, 0), "_quick_menu_skip_button",

(125, 0), "_quick_menu_q_load_button",

(175, 0), "_quick_menu_q_save_button",

(225, 0), "_quick_menu_prefs_button",

(265, 0), "_quick_menu_scale_button",




#175

)


image player_button_play  = 'images/interface/player/play.png'
image player_button_pause = 'images/interface/player/pause.png'
image player_button_stop  = 'images/interface/player/stop.png'

image player_button_forward = 'images/interface/player/forward.png'
image player_button_back    = Transform('player_button_forward', xzoom = -1)


image zero_solid = Solid("#f000")


image _quick_menu_version_False = Composite(

(320, 95),
#(0, 0), Solid("#f00"),
(60, 0),   "_text_info_report_bg_56",
(30, 43), "_text_info_report_bg_56",

(83, 12), Transform("_version_text", alpha = .42),
(53, 55), Transform("_platform_text", alpha = .42),

(183, 25), ImageButton(
    idle_image = _send_bug_report_t, 
    hover_image = _send_bug_report_t, 
    hovered = _quick_menu_send_bug_report_hover_check_to_True, 
    clicked = NullAction(),
    focus_mask = None,
    )
) 

init python:
    def _switch_debug_mod():
        pass
        #store.my_debug_mode = not store.my_debug_mode

image _quick_menu_version_True = Composite(

(320, 95),
#(0, 0), Solid("#f00"),
(50, 0), Transform('text_info_bg', zoom = .53),
(30, 43), Transform('text_info_bg', zoom = .53),

(83, 12), Transform(Text(version_now + " (" + sub_version_now + ")", font = 'fonts/mini_game.ttf', size = 25, color = "#000"), alpha = .7),
(53, 55), Transform(Text(str(platform), font = 'fonts/mini_game.ttf', size = 25, color = "#000"), alpha = .7),
(183, 25), ImageButton(
    idle_image = _send_bug_report_t_hover, 
    hover_image = _send_bug_report_t_hover, 
    hovered = _quick_menu_send_bug_report_hover_check_to_True, 
    clicked = NullAction(), #Show("bug_report_screen"),
    focus_mask = None,
    ),  
) 




image _quick_menu_version = "_quick_menu_version_[_quick_menu_send_bug_report_hover_check]"


image _text_info_report_bg_56 = Transform('text_info_bg', zoom = .53, alpha = .56)

image _text_info_report_bg_1_0 = Transform('text_info_bg', zoom = .53)

image _zero_image_button = ImageButton(
    idle_image  = "alpha_solid", 
    hover_image = "alpha_solid", 
    clicked = NullAction()
    )

#Transform('text_info_bg', zoom = .53, alpha = .56)

image _platform_text = Text(str(platform), font = 'fonts/mini_game.ttf', size = 25) 

image _version_text  = Text(version_now + " (" + sub_version_now + ")", font = 'fonts/mini_game.ttf', size = 25,)

image _quick_menu_version = "_quick_menu_version_[_quick_menu_send_bug_report_hover_check]"



init 1000 python:
    
    zero_button = ImageButton(idle_image = "zero_solid", hover_image = "zero_solid", clicked = NullAction())

screen quick_menu():
    
 
    # if my_debug_mode:
    #     key "K_TAB" action NullAction()
    #     text "Debug: toggle skip is disabled." xalign .5 yalign 1.0 outlines [(3, '#000c', 0, 0)]
    
    #textbutton "Test" text_outlines [(3, '#000c', 0, 0)] action Jump('tyan_falos_1') ypos 100
    zorder 100
    # if _quick_menu_send_bug_report_hover_check:
    #     imagebutton:
    #         idle  'alpha_solid'
    #         hover 'alpha_solid'
    #         hovered _quick_menu_send_bug_report_hover_check_to_False
    #         action NullAction()
 
    image "_quick_menu" yalign 1.0 zoom mp.interface_scale_number

    

    image '_quick_menu_version': 
        xpos 1970 ypos 1075
        yanchor 1.0 xanchor 1.0 zoom mp.interface_scale_number
    

    # use debug_screen
        
screen need_change_scale_screen(what_change_default=None):
    zorder 2000
    #if not what_change_default:
    default what_change = what_change_default or "main_interface"

    image 'locations/bg/GG_Room/evening.png'
    add store._save_load_menu_button_to_false

    image "_quick_menu" yalign 1.0 zoom mp.interface_scale_number
    

    image '_quick_menu_version': 
        xpos 1970 ypos 1075
        yanchor 1.0 xanchor 1.0 zoom mp.interface_scale_number

    if what_change == "main_interface":


        viewport:
            xmaximum 340
            ymaximum 135
            if mp.interface_scale_number != 1.0:
                if mp.interface_scale_number == 2.0:
                    at transform:
                        xalign 1.0
                        yalign .4
                        zoom mp.interface_scale_number
                    
                elif mp.interface_scale_number > 1.3:
                    at transform:
                        xalign 1.0
                        yalign .3
                        zoom mp.interface_scale_number
                    
                else:
                    at transform:
                        xalign 1.0
                        yalign .0
                        zoom mp.interface_scale_number
                    
            else:
                xalign 1.0
            
            image '#fff0'
            image 'interface/Panel_Money.png'
            
            text '$300' xalign .35 color '#000' ypos 40



        viewport:
            xmaximum 740
            ymaximum 220
            image '#fff0'
            if mp.interface_scale_number != 1.0:
                if mp.interface_scale_number == 2.0:
                    at transform:
                        xalign .8
                        yalign .0
                        zoom mp.interface_scale_number
               
                    
                else:
                    at transform:
                        xalign .5
                        yalign .0
                        zoom mp.interface_scale_number
                    
            else:
                xalign .5 yalign .0
                

            add 'survival_icons' xalign .5 ypos 100
            
            viewport:
                xmaximum 50
                ymaximum 30
                xpos 250
                ypos 132
                add 'alpha_solid'
                text "50" xalign .5 yalign .5 size 20 color '#000'


            viewport:
                xmaximum 50
                ymaximum 30
                xpos 360
                ypos 165
                add 'alpha_solid'
                text "50" xalign .5 yalign .5 size 20 color '#000'



            viewport:
                xmaximum 50
                ymaximum 30
                xpos 460
                ypos 132
                add 'alpha_solid'
                text "50" xalign .5 yalign .5 size 20 color '#000'


            button:
                add 'evening_button'
                xalign .5
                action NullAction()

            add 'play_icon' xalign .5
            
            add 'interface/Panel_Day.png' xpos -3 ypos 30
            add 'interface/Panel_Day.png' xpos 430 ypos 30 xzoom -1
            viewport:
                xmaximum 310
                ymaximum 90
                add 'alpha_solid'
                $ times = getattr(store, 'time', Time()).tdtd.title()
                text _(str(times)) color '#000' xalign .5 yalign .5 size 25
                xpos -3 ypos 30
            viewport:
                xmaximum 310
                ymaximum 90
                add 'alpha_solid'

                $ times = rus_time["evening"].title()
                text _(str(times)) xalign .5 yalign .5 color '#000' size 25
                xpos 430 ypos 30


           

        viewport:
            image '#fff0'
            

            if mp.interface_scale_number > 1.5:
                at transform:
                    yalign .5
                    zoom mp.interface_scale_number
                xmaximum 150
                ymaximum 550
                        
            elif mp.interface_scale_number > 1.0:
                at transform:
                    yalign .0
                    zoom mp.interface_scale_number
                xmaximum 300
                ymaximum 300

            else:
                at transform:
                    yalign .0
                    xalign .0 
                    zoom mp.interface_scale_number
                
                xmaximum 600
                ymaximum 170
            button:
                if mp.interface_scale_number > 1.0:
                    if mp.interface_scale_number > 1.5:
                        ypos 295 xpos 0
                    else:
                        ypos 165 xpos 0
                else:
                    ypos 20 xpos 260
                add 'quest_button'
                action NullAction()
            
            add 'warning_icon': 
                if mp.interface_scale_number > 1.0:
                    if mp.interface_scale_number > 1.5:
                        xpos 82 ypos 375
                    else:
                        xpos 80 ypos 245
                else:
                    xpos 340 ypos 100
            

            button: 
                if mp.interface_scale_number > 1.5:
                    ypos 165 xpos 0
                else:
                    ypos 20 xpos 130
                add 'bag_button'
                action NullAction()


            button:
                add 'mobile_button'
                action NullAction()
            add 'warning_icon' xpos 60 ypos 115


            button:
                if mp.interface_scale_number > 1.0:
                    if mp.interface_scale_number > 1.5:
                        ypos 425 xpos 0
                    else:
                        ypos 165 xpos 130
                else:
                    ypos 20 xpos 400
                add 'map_button'
                action NullAction()


    else:

        vbox:
            style_prefix "choice"
            spacing 10
            at transform:
                zoom mp.dialogue_interface_scale_number

            textbutton "Answer 1" action NullAction()
            textbutton "Answer 2" action NullAction()
        


        window:
            style_prefix "say"
            if mp.dialogue_interface_scale_number != 1.0:
                if mp.dialogue_interface_scale_number < 1.5:
                    at transform:
                        zoom mp.dialogue_interface_scale_number
                
                else:
                    at transform:
                        zoom 1.4
                

            text __("Бла")*3 xpos gui.dialogue_xpos ypos gui.dialogue_ypos





    if True:

        
    


        imagebutton:
            idle  '#fff1'
            hover '#fff1'
            action Function(_save_load_focus_on_show_set_down), Hide('need_change_scale_screen'), ShowMenu("preferences", need_change_scale_screen = False)
        if not what_change_default:
            hbox:
                align .5, .7
                spacing 10
                viewport:
                    xmaximum 400
                    ymaximum 100
                    imagebutton:
                        idle  '#000a'
                        hover '#000a'
                        action NullAction()
                    imagebutton:
                        align .5, .5
                       # yalign .97
                       # xpos 10
                        #xalign 1.0
                        #ypos 10

                        idle  Text(_('Main Interface'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)], size = 50)
                        hover Text(_('Main Interface'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)], size = 50)

                        yanchor .5
                        at PulseButtonXzoom09
                        action Function(_save_load_focus_on_show_set_up), SetScreenVariable("what_change", "main_interface")
                    if what_change == 'main_interface':
                        image '#000a'


                viewport:
                    xmaximum 400
                    ymaximum 100
                    imagebutton:
                        idle  '#000a'
                        hover '#000a'
                        action NullAction()
                    imagebutton:
                        align .5, .5
                   # yalign .97
                   # xpos 10
                    #xalign 1.0
                    #ypos 10

                        idle  Text(_('Dialogue interface'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)], size = 50)
                        hover Text(_('Dialogue interface'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)], size = 50)

                        yanchor .5
                        at PulseButtonXzoom09
                        action Function(_save_load_focus_on_show_set_down), SetScreenVariable("what_change", "dialogue_interface")
                    if what_change == 'dialogue_interface':
                        image '#000a'
        viewport:
            maximum(400, 130)
            align (.5, .5)
            image '#fffa'
            hbox:
                align .5, .5
                spacing 10
                viewport:
                    xmaximum 100
                    ymaximum 100
                    imagebutton:
                        idle  '#000a'
                        hover '#000a'
                        action NullAction()
                    imagebutton:
                        align .5, .3
                       # yalign .97
                       # xpos 10
                        #xalign 1.0
                        #ypos 10

                        idle  Text(_('-'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)], size = 200)
                        hover Text(_('-'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)], size = 200)

                        yanchor .5
                        at PulseButtonXzoom09
                        if what_change == "main_interface":
                            action Function(_save_load_focus_on_show_set_up), Function(chage_scale, new_scale = mp.interface_scale - 1)
                        else:
                            action Function(_save_load_focus_on_show_set_down), Function(chage_dialogue_scale, new_scale = mp.dialogue_interface_scale - 1)

                viewport:
                    xmaximum 150
                    ymaximum 100
                    imagebutton:
                        idle  '#000a'
                        hover '#000a'
                        action NullAction()
                    if what_change == "main_interface":

                        $ _interface_scale = mp.interface_scale
                    else:
                        $ _interface_scale = mp.dialogue_interface_scale
                    if len(str(_interface_scale)) == 1:
                        $ _interface_scale = "."+str(_interface_scale)
                    else:
                        $ _interface_scale = str(_interface_scale)[0] + "." + str(_interface_scale)[1:]

                    image Text(_interface_scale, font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)], size = 100) align .5, .5
                
                viewport:
                    xmaximum 100
                    ymaximum 100
                    imagebutton:
                        idle  '#000a'
                        hover '#000a'
                        action NullAction()
                    imagebutton:
                        align .5, .5
                   # yalign .97
                   # xpos 10
                    #xalign 1.0
                    #ypos 10

                        idle  Text(_('+'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)], size = 200)
                        hover Text(_('+'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)], size = 200)

                        yanchor .5
                        at PulseButtonXzoom09
                        if what_change == "main_interface":
                            action Function(_save_load_focus_on_show_set_up), Function(chage_scale, new_scale = mp.interface_scale + 1)
                        else:
                            action Function(_save_load_focus_on_show_set_down), Function(chage_dialogue_scale, new_scale = mp.dialogue_interface_scale + 1)


init python:
    config.overlay_screens.append("quick_menu")

    who_say_now = None
    showing_tags = []

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")











screen navigation():

    vbox:
        style_prefix "navigation"

        xpos 85
        ypos 345
        spacing -25


        if main_menu:









            hbox:
                viewport:
                    xmaximum 440
                    ymaximum 105
                    button:
                        add 'main_menu_button'
                        action Start()

                    text _("Новая игра") xalign .5 yalign .6 color '#000'
                add 'images/new_item.png' xpos -60 ypos -10














        else:

            viewport:
                xmaximum 440
                ymaximum 105
                button:
                    add 'main_menu_button'
                    action ShowMenu("history")

                text _("История") xalign .5 yalign .6 color '#000'


            viewport:
                xmaximum 440
                ymaximum 105
                button:
                    add 'main_menu_button'
                    action ShowMenu("save")

                text _("Сохранить") xalign .5 yalign .6 color '#000'



        viewport:
            xmaximum 440
            ymaximum 105
            button:
                add 'main_menu_button'
                action ShowMenu("load")

            text _("Загрузить") xalign .5 yalign .6 color '#000'
        if main_menu:
            viewport:
                xmaximum 440
                ymaximum 105
                button:
                    add 'main_menu_button'
                    action Show('Gallery_screen', transition = config.window_show_transition)

                text _("Галерея") xalign .5 yalign .6 color '#000'


        viewport:
            xmaximum 440
            ymaximum 105
            button:
                add 'main_menu_button'
                action ShowMenu("preferences")

            text _("Настройки") xalign .5 yalign .6 color '#000'




        if not main_menu:
            viewport:
                xmaximum 440
                ymaximum 105
                button:
                    add 'main_menu_button'
                     
                    action Function(reset_perisistent_from_gallery), MainMenu()
                    

                text _("Главное меню") xalign .5 yalign .6 color '#000'

        viewport:
            xmaximum 440
            ymaximum 105
            button:
                add 'main_menu_button'
                action ShowMenu("about")

            text _("Титры") xalign .5 yalign .6 color '#000'















        if main_menu:






            viewport:
                xmaximum 440
                ymaximum 105
                button:
                    add 'main_menu_button'
                    action Quit(confirm=not main_menu)

                text _("Выход") xalign .5 yalign .6 color '#000'
            viewport:
               maximum (400, 45)
               image 'alpha_solid'
            viewport pos (-22, 15):
                add 'images/steam_icon.png'
                imagebutton:
                    idle 'images/steam_icon.png'
                    hover 'images/steam_icon_hover.png' #im.MatrixColor('images/steam_icon_hover.png', im.matrix.brightness(.3))
                    at ButtonEffect00
                    action OpenURL('https://store.steampowered.com/app/2706300/MILFs_Plaza?utm_source=MILFsPlaza&utm_campaign=Build&utm_content=Button')



                xmaximum 503
                ymaximum 175
        else:




            viewport:
                xmaximum 440
                ymaximum 105
                button:
                    add 'main_menu_button'
                    action Return()

                text _("Назад") xalign .5 yalign .6 color '#000'

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")





screen change_language_screen:
    zorder 4500
    image '#000b'
    style_prefix "choice"
    #default text_now = ''
    viewport:
        image 'alpha_solid'
        imagebutton: 
            idle  'alpha_solid'
            hover 'alpha_solid'
            action Hide('change_language_screen')
    viewport:
        image 'alpha_solid'
        align (.5, .5)
        maximum (800, 870)
        imagebutton: 
            idle  'alpha_solid'
            hover 'alpha_solid'
            action NullAction()
    vbox yalign .5:
        spacing 10
        for i in (
('RUSSIAN'     , 'rus'),
('ENGLISH'    , 'eng'),
('CHINESE (SIMPL)' ,  "chinese_simpl"),
('CHINESE (TRAD)' , "chinese_trad"),    
('FRENCH'     , 'french'),  
('DUTCH'      , 'dutch'),   
('SPANISH'    , 'spn'), 
('PORTUGUESE' , 'por'),
('GERMAN'   , 'germ'),  
('POLISH'   , 'pol'),  
('TURKISH'  , 'turk'), 
#('THAI'     , 'thai'),    
#('ITALIAN'  , 'ital'), 
('JAPANESE' , 'jap'),    
('KOREAN' , 'kor'),

        ):
            
            textbutton i[0]:
                
                action Function(change_language_confirm, i[1].upper())

       # textbutton '{i}'+_("Назад")+'{/i}' action Hide('change_language_screen')
screen change_language_button():
    # textbutton _("RUS") text_outlines [(3, '#000c', 0, 0)] text_color '#fff' text_hover_color '#fffa' action Function(change_language_confirm, 'RUS')
    # textbutton _("ENG") text_outlines [(3, '#000c', 0, 0)] text_color '#fff' text_hover_color '#fffa' action Function(change_language_confirm, 'ENG')
    
    default language = preferences.language or "RUS"

    textbutton str(language).upper() + " (change)": 
        text_outlines [(3, '#000c', 0, 0)] 
        text_size 30
        text_color '#fff' 
        text_hover_color '#fffa'
        text_font gui.text_font 
        action Show('change_language_screen')

screen main_menu():




    style_prefix "main_menu" tag menu

    add gui.main_menu_background


    frame
    hbox:
        ypos 10
        xpos 20
        
        use change_language_button()
       
    use navigation

    if gui.show_name:




        hbox:
            textbutton "Version: " + str(config.version): 
                action NullAction() 
                text_outlines [(3, '#000c', 0, 0)] 
                text_color '#fff' 
                text_hover_color '#fff' 
                text_size 30 
                ypos 45

            xalign 0.05 yalign .98

            add 'interface/click_here_button.png' alpha 0.0 ypos 25

    use subscribe_buttons_screen
    
    #if persistent.new_patch != config.version:
    #   use patch_note_screen


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")











screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"




    add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        viewport xpos 600:
            if renpy.get_screen('save') or renpy.get_screen('load'):
                xmaximum 1270
            else:
                xmaximum 1200
            add '#000a'


        hbox xpos 200:


            frame:
                style "game_menu_navigation_frame"

            frame:
                xmaximum 1200

                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        has vbox
                        transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation








    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45






screen credits_screen(pr_transform=None, pr_text_xalign=None, pr_outlines=None, pr_size = None, pr_spacing = 5):
    vbox:

        if pr_transform is not None:
            at pr_transform
        text ''
        text "Milf's Plaza":
            if pr_text_xalign is not None:
                xalign pr_text_xalign
            if pr_outlines:
                outlines pr_outlines
            if pr_size:
                size pr_size+25
        text ''
        text ''

        text __('Над игрой работали:'):
            if pr_text_xalign is not None:
                xalign pr_text_xalign
            if pr_outlines:
                outlines pr_outlines
            if pr_size:
                size pr_size+15

        # if pr_xalign is not None:
        #     xalign pr_xalign
        # if pr_yalign is not None:
        #     yalign pr_yalign
        spacing pr_spacing
        for i in (
        (__('Автор проекта'), 'Texic'),
        (__('Художник'), 'Texic'),
        (__('Сценарист'), 'Texic'),
        (__('Программист'), 'SorkOs'),
        (__('Режисер сцен'), 'SorkOs'),
        (__('Издатель'), 'TopHouse Studio'),):
            hbox:
                text '    ': 
                    if pr_size:
                        size pr_size
                text i[0] + ":" font gui.interface_text_font:
                    if pr_text_xalign is not None:
                        xalign pr_text_xalign
                    if pr_outlines:
                        outlines pr_outlines
                    if pr_size:
                        size pr_size
                text ' '
                text i[1] font store.proxima_nova_font:
                    if pr_text_xalign is not None:
                        xalign pr_text_xalign
                    if pr_outlines:
                        outlines pr_outlines
                    if pr_size:
                        size pr_size
        text ''
        text __('Переводчики') + ":":
            if pr_text_xalign is not None:
                xalign pr_text_xalign
            if pr_outlines:
                outlines pr_outlines
            if pr_size:
                size pr_size+15
        for i in (
        (__('Китайский упрощённый'), 'piaozhu'),
        (__('Китайский традиционный'), 'Asobi & Nya'),
        (__('Французский'), 'DarkLight, dinozavr_tonya'),
        (__('Голландский'), 'Goatism'),
        (__('Испанский'), 'Mustadio7813'),
        (__('Португальский'), 'Danma'),
        (__('Немецкий'), 'Bane'),
        (__('Польский'), 'Onion Juice'),
        (__('Турецкий'), 'alwan545'),


        (__('Японский'), 'Asobi & Nya'),
        (__('Корейский'), 'Asobi & Nya'),
        ):
            hbox:
                text '    ': 
                    if pr_size:
                        size pr_size
                text i[0] + ":" font gui.interface_text_font:
                    if pr_text_xalign is not None:
                        xalign pr_text_xalign
                    if pr_outlines:
                        outlines pr_outlines
                    if pr_size:
                        size pr_size
                text ' '
                text i[1] font store.proxima_nova_font:
                    if pr_text_xalign is not None:
                        xalign pr_text_xalign
                    if pr_outlines:
                        outlines pr_outlines
                    if pr_size:
                        size pr_size



screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        vbox:

            # text ''
            # text "Milf's Plaza" outlines [(3, '#000c', 0, 0)]
            # text ''
            # text ''

            # text __('Над игрой работали:')
            text ''

            use credits_screen

        
            
            text '______________________________'
            text 'Music:'

            text '    UI Completed Status Alert Notification SFX001'
            text '    Link: {a=https://freesound.org/people/Headphaze/sounds/277033/}https://freesound.org/people/Headphaze/sounds/277033/{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}a=http://creativecommons.org/licenses/by/4.0/{/a}'

            text '    Yobomo Ambient - mo_Opacity_complete'
            text '    Link: {a=https://freesound.org/people/Yobomo/sounds/570310/}https://freesound.org/people/Yobomo/sounds/570310/{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}a=http://creativecommons.org/licenses/by/4.0/{/a}'

            text '    Skibka - Music_Happy_7'
            text '    Link: {a=https://freesound.org/people/SkibkaMusic/sounds/477602/} https://freesound.org/people/SkibkaMusic/sounds/477602/{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}a=http://creativecommons.org/licenses/by/4.0/{/a}'

            text '    Past Sadness by Kevin MacLeod'
            text '    Link: {a=https://incompetech.filmmusic.io/song/5024-past-sadness} https://incompetech.filmmusic.io/song/5024-past-sadness{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}a=http://creativecommons.org/licenses/by/4.0/{/a}'

            text '    Glitter Blast by Kevin MacLeod'
            text '    Link: {a=https://incompetech.filmmusic.io/song/4707-glitter-blast} https://incompetech.filmmusic.io/song/4707-glitter-blast{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}a=http://creativecommons.org/licenses/by/4.0/{/a}'

            text '    SCP-x6x (Hopes) by Kevin MacLeod'
            text '    Link: {a=https://incompetech.filmmusic.io/song/6736-scp-x6x-hopes-}https://incompetech.filmmusic.io/song/6736-scp-x6x-hopes-{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}a=http://creativecommons.org/licenses/by/4.0/{/a}'

            text '    Deliberate Thought by Kevin MacLeod'
            text '    Link: {a= https://incompetech.filmmusic.io/song/3635-deliberate-thought}https://incompetech.filmmusic.io/song/3635-deliberate-thought{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}a=http://creativecommons.org/licenses/by/4.0/{/a}'


            text '    Chill Wave by Kevin MacLeod'
            text '    Link: {a= https://incompetech.filmmusic.io/song/3498-chill-wave} https://incompetech.filmmusic.io/song/3498-chill-wave{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}http://creativecommons.org/licenses/by/4.0/{/a}'

            text '    Hard Boiled by Kevin MacLeod'
            text '    Link: {a= https://incompetech.filmmusic.io/song/3857-hard-boiled} https://incompetech.filmmusic.io/song/3857-hard-boiled{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}http://creativecommons.org/licenses/by/4.0/{/a}'

            text '    Smooth Lovin by Kevin MacLeod'
            text '    Link: {a= https://incompetech.filmmusic.io/song/4379-smooth-lovin} https://incompetech.filmmusic.io/song/4379-smooth-lovin{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}http://creativecommons.org/licenses/by/4.0/{/a}'

            text '    Windswept by Kevin MacLeod'
            text '    Link: {a= https://incompetech.filmmusic.io/song/4629-windswept} https://incompetech.filmmusic.io/song/4629-windswept{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}http://creativecommons.org/licenses/by/4.0/{/a}'

            text '    Inner Light by Kevin MacLeod'
            text '    Link: {a= https://incompetech.filmmusic.io/song/3916-inner-light} https://incompetech.filmmusic.io/song/3916-inner-light{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}http://creativecommons.org/licenses/by/4.0/{/a}'


            text '    Almost Bliss by Kevin MacLeod'
            text '    Link: {a=https://incompetech.filmmusic.io/song/5032-almost-bliss}https://incompetech.filmmusic.io/song/5032-almost-bliss{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}http://creativecommons.org/licenses/by/4.0/{/a}'


            text '    Aerosol Of My Love by Kevin MacLeod'
            text '    Link: {a=https://incompetech.filmmusic.io/song/7013-aerosol-of-my-love}https://incompetech.filmmusic.io/song/7013-aerosol-of-my-love{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}http://creativecommons.org/licenses/by/4.0/{/a}'


            text '    Call by Kevin MacLeod'
            text '    Link: {a=https://incompetech.filmmusic.io/song/3399-awesome-call}https://incompetech.filmmusic.io/song/3399-awesome-call{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}http://creativecommons.org/licenses/by/4.0/{/a}'


            text '    Your Call by Kevin MacLeod'
            text '    Link: {a=https://incompetech.filmmusic.io/song/5018-your-call}https://incompetech.filmmusic.io/song/5018-your-call{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}http://creativecommons.org/licenses/by/4.0/{/a}'


            text '    Plain Loafer by Kevin MacLeod'
            text '    Link: {a=https://incompetech.filmmusic.io/song/4223-plain-loafer}https://incompetech.filmmusic.io/song/4223-plain-loafer{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}http://creativecommons.org/licenses/by/4.0/{/a}'


            text '    Aces High by Kevin MacLeod'
            text '    Link: {a=https://incompetech.filmmusic.io/song/3337-aces-high}https://incompetech.filmmusic.io/song/3337-aces-high{/a}'
            text '    License: {a=http://creativecommons.org/licenses/by/4.0/}http://creativecommons.org/licenses/by/4.0/{/a}'



            for mus in [

            ['Style Funk by Kevin MacLeod', 'https://incompetech.filmmusic.io/song/4428-style-funk',],
            ['Funky One by Kevin MacLeod', 'https://incompetech.filmmusic.io/song/3790-funky-one'],
            ]:

                text '    ' + str(mus[0])
                text '    Link: {a='+str(mus[1])+'}'+str(mus[1])+'{/a}'
                text '    License: {a=http://creativecommons.org/licenses/by/4.0/}http://creativecommons.org/licenses/by/4.0/{/a}'


            for mus in [

            ['District Four', 'https://filmmusic.io/song/3662-district-four',],
            ['Loopster', 'https://filmmusic.io/song/4991-loopster'],
            ['Sunny Morning by MusicLFiles', 'https://filmmusic.io/song/7813-sunny-morning'],
            ['Full Moon Lofi Vibes by EdiKey20', 'https://filmmusic.io/song/7672-full-moon-lofi-vibes'],
            ['Lo Fi Hip Hop 02 by WinnieTheMoog', 'Lo Fi Hip Hop 02 by WinnieTheMoog'],
            ['Late Night Radio by Kevin MacLeod', 'https://filmmusic.io/song/7613-late-night-radio',],
            ['Deadly Roulette', 'https://filmmusic.io/song/3625-deadly-roulette'],

            ]:





                text '    The following music was used for this media project:'
                text '    Music: ' + mus[0] + ' by Kevin MacLeod'
                text '    Free download:' + mus[1]
                text '    License (CC BY 4.0): https://filmmusic.io/standard-license'
                text '    Artist website: https://incompetech.com'

            text '    The following music was used for this media project:'
            text '    Music: Sad Reflection and Grief Piano by MusicLFiles'
            text '    Free download: https://filmmusic.io/song/8272-sad-reflection-and-grief-piano'
            text '    License (CC BY 4.0): https://filmmusic.io/standard-license'
            text '    Artist website: https://cemmusicproject.wixsite.com/musiclibraryfiles'

            text '    The following music was used for this media project:'
            text '    Music: Happy Days In Summer by MusicLFiles'
            text '    Free download: https://filmmusic.io/song/8020-happy-days-in-summer'
            text '    License (CC BY 4.0): https://filmmusic.io/standard-license'
            text '    Artist website: https://cemmusicproject.wixsite.com/musiclibraryfiles'

            text '    The following music was used for this media project:'
            text '    Music: New Sky by Rafael Krux'
            text '    Free download: https://filmmusic.io/song/5693-new-sky'
            text '    License (CC BY 4.0): https://filmmusic.io/standard-license'
            text '    Artist website: https://www.orchestralis.net/'






            text '______________________________'
            text _("Version [config.version!t]\n")

            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size











screen save():
    tag menu


    use file_slots("Save")


screen load():
    tag menu


    use file_slots("Load")


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:



            order_reverse True

            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        if title == "Load":
                            action Function(reset_perisistent_from_gallery), FileAction(slot)
                            
                        else:
                            action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()



style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")









screen preferences(need_change_scale_screen = False):
    tag menu



    use game_menu(_("Preferences"), scroll="viewport"):
        default volume_text = __("Volume")
        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window") text_font gui.interface_text_font
                        textbutton _("Fullscreen") action Preference("display", "fullscreen") text_font gui.interface_text_font

                vbox:
                    style_prefix "radio"
                    label _("Language")
                    
                    use change_language_button()
                    # textbutton _("RUS") action Function(change_language_confirm, 'RUS')
                    # textbutton _("ENG") action Function(change_language_confirm, 'ENG')

                    # textbutton _("SPN") action Function(change_language_confirm, 'SPN')



                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle") text_font gui.interface_text_font
                    textbutton _("After Choices") action Preference("after choices", "toggle") text_font gui.interface_text_font
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")) text_font gui.interface_text_font




            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True
















                vbox:
                    vbox:

                        label _("Auto-Forward Time")

                        bar value Preference("auto-forward time")



                    vbox:
                        for rrr in ("music", "sound", "voice"):
                            if rrr == "music":
                                $ j = False
                            else:
                                $ j = getattr(config, 'sample_'+rrr, False)
                            if getattr(config, "has_"+rrr, False):
                                label __(rrr.title()) + " " + volume_text text_font gui.interface_text_font

                                hbox:
                                    bar value Preference(rrr+" volume")
                                    if j:
                                        textbutton _("Test") action Play(rrr, j)

                        text " "
                        text " "
                        text " "

                text " "

                vbox:
                    style_prefix "radio"
                    label __("Interface scale")
                    textbutton __(" Main: ")+str(mp.interface_scale_number): 
                        text_font gui.interface_text_font
                        action Show("need_change_scale_screen", what_change_default = "main_interface")
                    textbutton __(" Dialogue: ")+str(mp.dialogue_interface_scale_number):
                        text_font gui.interface_text_font
                        action Show("need_change_scale_screen", what_change_default = "dialogue_interface")

                    # label _("Text Speed")
                    # bar value Preference("text speed")

    if need_change_scale_screen:
        image '#000'
        timer .5 action Function(_save_load_focus_on_show_set_up), Show('need_change_scale_screen')



style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675










screen history():




    predict False tag menu

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")




define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5








screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















screen confirm(message, yes_action, no_action, yes_text = "Yes", no_text = "No", font = None):

    default asian_check = preferences.language in ('chinese_trad', 'chinese_simpl', 'jap', 'kor')
    modal True

    zorder 5000

    style_prefix "confirm"
    imagebutton:
        idle  'alpha_solid'
        hover 'alpha_solid'
        action no_action

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 45

        label _(message):
            style "confirm_prompt"
            xalign 0.5
            if font:
                text_font font
            elif asian_check:
                text_font gui.text_font

        hbox:
            xalign 0.5
            spacing 150
            

            textbutton yes_text action yes_action: 
                if font:
                    text_font font
                elif asian_check:
                    text_font gui.text_font
            textbutton no_text action no_action: 
                if font:
                    text_font font
                elif asian_check:
                    text_font gui.text_font

            


    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id

screen nonclick_back_screen:
    imagebutton:
        idle '#000'
        hover '#000'
        action NullAction() 


define config.nvl_list_length = gui.nvl_list_length





style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 675


label hide_menu_label:
    "func" "hide"
    $ from_say_screen = False
    return

label before_menu_label:
    "func" "to_hide"
    $ from_say_screen = False
    return


label hide_say_screen_with_dissolve_label:
    "func" "to_hide_return"
    $ from_say_screen = False
    return

    
label at_menu_label:
    $ choice_with_transform = True
    return

label wait_click_label:
    $ renpy.pause(9999)
    $ from_say_screen = False
    return