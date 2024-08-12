init 102 python:
    _original_names   = [
    "Кристи",
    "Офицер",
    "Зудила",
    "Бубнило",
    "Марина",
    "Мишванда",
    "Миша",
    "Кэт",
    "Сьюзан",
    "Джеймс",
    "Жлоб",
    "Маша",
    "Офицер",
    "Девушка-Офицер",
    "Игорь",
    "Девушка",
    "Парень",
    "Ночная Гостья",
    "Бандит",
    "Качок",
    "Грабитель",
    ]
    _translated_names = {
None  : store._original_names,
"rus" : store._original_names,

"eng" :["Christie", "Officer", "Itcher", "Mumbler", "Mary", "Mishvanda", "Misha", "Kat", "Susan", "James", "Goon", "Helene", "Officer", "Girl-Officer", "Igor", "Girl", "Guy", "Night Guest", "Bandit", "Big Guy", "Robber", ],

"french" :["Christie", "Agent", "Itchy", "Mumbler", "Mary", "Mishvanda", "Misha", "Kat", "Susan", "James", "Goon", "Hélène", "Agent", "Femme officier", "Igor", "Fille", "Mec", "Visiteuse nocturne", "Bandit", "Grand type", "Voleur", ],

"dutch" :["Christie", "Agent", "Itchy", "Mumbler", "Mary", "Mishvanda", "Misha", "Kat", "Susan", "James", "Goon", "Helene", "Agent", "Vrouwelijke Officier", "Igor", "Meisje", "Jongen", "Nacht Gast", "Bandiet", "Grote Gast", "Overvaller", ],

"spn" :["Christie", "Oficial", "Itcher", "Mumbler", "Mary", "Mishvanda", "Misha", "Kat", "Susan", "James", "Goon", "Helene", "Oficial", "Chica-Oficial", "Igor", "Chica", "Novio", "Visitante nocturno", "Bandido", "Grandote", "Ladrón", ],

"por" :["Christie", "Oficial", "Itcher", "Mumbler", "Mary", "Mishvanda", "Misha", "Kat", "Susan", "James", "Goon", "Helene", "Oficial", "Oficial mulher", "Igor", "Garota", "Homem", "Convidado noturno", "Bandido", "Cara grande", "Ladrão", ],

"germ" :["Christie", "Wachmeister", "Itcher", "Mumbler", "Mary", "Mishwanda", "Misha", "Kat", "Susan", "James", "Goon", "Helene", "Wachmeister", "weiblicher Beamter", "Igor", "Mädchen", "Junge", "Nächtlicher Besucher", "Bandit", "Großer Typ", "Dieb", ],

"pol" :["Christie", "Oficer", "Itchy", "Blubbermouth", "Mary", "Mishwanda", "Misha", "Kat", "Susan", "James", "Zbir", "Helene", "Oficer", "Pani oficer", "Igor", "Dziewczyna", "Facet", "Nocny Gość", "Bandyta", "Duży koleś", "Złodziej", ],

"turk" :["Christie", "Memur", "Itcher", "Mumbler", "Mary", "Mishvanda", "Misha", "Kat", "Susan", "James", "Goon", "Helene", "Memur", "Kadın Memur", "Igor", "Kız", "Erkek", "Gece Misafiri", "Haydut", "Koca Adam", "Hırsız", ],

"jap" :["クリスティ", "警官", "イッチー", "ブラバーマウス", "メリー", "ミシュバンダ", "ミーシャ", "キャット", "スーザン", "ジェームス", "グーン", "ヘレン", "警官", "婦人警官", "イゴール", "若い女性", "若い男", "夜のゲスト", "極道", "キン肉マン", "強盗", ],

"chinese_trad" :["克里斯蒂", "警官", "痒痒皮", "碎碎嘴", "瑪麗", "米莎旺達", "米沙", "凱特", "蘇珊", "詹姆斯", "古恩", "海倫娜", "警官", "女警官", "伊戈爾", "女孩", "男孩", "夜晚不速之客", "強盜", "大塊頭", "劫匪", ],

"chinese_simpl" :["克里斯蒂", "警官", "痒痒皮", "碎碎嘴", "玛丽", "米莎旺达", "米莎", "凯特", "苏珊", "詹姆斯", "古恩", "海伦娜", "警官", "女警官", "伊戈尔", "女孩", "男孩", "夜间的不速之客", "强盗", "大块头", "劫匪", ],

"kor" :["크리스티", "경관", "이처", "멈블러", "메리", "미슈반다", "미샤", "캣", "수잔", "제임스", "구운", "헬렌", "경관", "여성 경관", "이고르", "젊은 여성", "젊은 남성", "밤 손님", "조폭", "근육맨", "강도", ],


    }

    class NameBox():
        
        
        
        def __init__(self, name, sprite, color, x_size = 638, **kwargs):

            self.name   = name.replace('_', '{color=#0000}_{/color}')


            self.sprite = sprite

            self.color  = color
            

            self.yp = 745
            

            self.xp     = 267

            self.xzoom  = 1.0

            self.alpha  = 0.0

            self.x_size = x_size

            self.text_obj = Text("None")

            self.transform_obj = Transform(self.text_obj)

            self._image        = 'interface/bg_frame.png'

            self.transform_obj_image = Transform(self._image)

            self.text_obj_size_x = 0

            self.text_obj_size_y = 0

            self.create_text_obj()

            self.state = None
            
            self.anim_yp_len = 710 

            self.anim_time_start = datetime.datetime.now()

        def create_text_obj(self):
            eng_names   = store._translated_names['eng']
            lang_check  = preferences.language not in (None, 'rus', 'eng')
            index_check = self.name in eng_names
            if lang_check and index_check:
                names      = _translated_names[preferences.language]
                name_index = eng_names.index(self.name)
                name       = names[name_index]
            else:
                name = self.name
            self.text_obj = Text(
                name, 
                color    = self.color, 
                outlines = [(2, "#000a", 0, 0),], 
                size     = 30 
                )
            text_obj_size = self.text_obj.size()

            self.text_obj_size_x = text_obj_size[0] 
            self.text_obj_size_y = text_obj_size[1] 
        def start_anim_down(self):
            if self.yp >= 745:
                #self.yp = 755
                self.state = "down"
                return
            
            self.anim_yp_len = 745 - self.yp

            self.anim_time_start = datetime.datetime.now()
            self.state = "need_down"

        def start_anim_up(self):
            if self.yp <= 725:
                #self.yp = 735
                self.state = "up"
                return
            
            self.state = "need_up"
            self.anim_yp_len = self.yp - 725
            self.anim_time_start = datetime.datetime.now()
            
        def anim_get_cords(self):
            x = (datetime.datetime.now() - self.anim_time_start).total_seconds()

            c1 = 1.70158
            c3 = c1 + 1

            r = 1 + c3 * math.pow(x - 1, 3) + c1 * math.pow(x - 1, 2);

            return int(r*self.anim_yp_len) 


    def create_nameboxes():
        
        if preferences.language not in (None, 'rus'):
            store.nameboxes = {
            'Texic'   : NameBox('Texic',   'Texic', '#e5e349'),
            'GG'   : NameBox('gg',   'GG', '#e5e349'),
            'Milf' : NameBox('Mary', 'Milf', '#e1bdff'),
            'Misha': NameBox('Mishvanda', 'Misha', '#fff'),
            'Officer': NameBox('Officer', 'Officer', '#fff'),

            'GirlOfficer': NameBox('Girl Officer', 'GirlOfficer', '#FF69B4', 800),
            'Christie': NameBox('Christie', 'Christie', '#FF69B4'),
            'Igor': NameBox('Igor', 'Igor', '#FF69B4'),
            'Jay': NameBox('Itcher', 'Jay', '#ffaa85'),
            'Bob': NameBox('Mumbler', 'Bob', '#c2a191'),
            'Kat': NameBox('Kat', 'Kat', '#30D5C8'),

            'Night Stalker': NameBox('Night_Stalker', 'Kat', '#30D5C8'),
            'Night Guest': NameBox('Night_Guest', 'Kat', '#30D5C8'),
            'Psi': NameBox("Susan", 'Psi', '#30D5C8'),
           
            'Bandit' : NameBox("Big_Guy", 'Bandit', '#ddd4b5', 800),

            'BandtiWithPistol' : NameBox("Robber", 'BandtiWithPistol', '#30D5C8', 800),
           
            'BiblioGirl' : NameBox("Nancy", 'BiblioGirl', '#FF69B4'),
            'Nikolaya': NameBox('James', 'Nikolaya', '#fff'),
            'Masha' : NameBox('Helene', 'Masha', '#FF69B4'),
            'Helene' : NameBox('Helene', 'Masha', '#FF69B4'),
            'Girl': NameBox('Girl', 'Girl', '#30D5C8'),
            'Guy': NameBox('Guy', 'Guy', '#fff'),
            'Goon': NameBox('Goon', 'Goon', '#fff'),
            
            


            }



        else:
            store.nameboxes = {
            'Texic'   : NameBox('Texic',   'Texic', '#e5e349'),
            'GG'   : NameBox('gg',   'GG', '#e5e349'),
            'Milf' : NameBox('Марина', 'Milf', '#e1bdff'),
            'Misha': NameBox('Мишванда', 'Misha', '#fff'),
            'GirlOfficer': NameBox('Офицерша', 'GirlOfficer', '#FF69B4', 800),
            'Officer': NameBox('Офицер', 'Officer', '#fff'),
            'Christie': NameBox('Кристи', 'Christie', '#FF69B4'),
            'Igor': NameBox('Игорь', 'Igor', '#FF69B4'),
            'Jay': NameBox('Зудило', 'Jay', '#ffaa85'),
            'Bob': NameBox('Бубнило', 'Bob', '#c2a191'),
            'Night Stalker': NameBox('Ночная_Гостья', 'Kat', '#30D5C8'),
            'Night Guest': NameBox('Ночная_Гостья', 'Kat', '#30D5C8'),
            'Psi': NameBox("Сьюзан", 'Psi', '#30D5C8'),
            'Bandit' : NameBox("Качок", 'Bandit', '#ddd4b5', 800),

            'BandtiWithPistol' : NameBox("Бандит", 'BandtiWithPistol', '#30D5C8', 800),
            'BiblioGirl' : NameBox("Нэнси", 'BiblioGirl', '#FF69B4'),
            'Masha' : NameBox('Маша', 'Masha', '#FF69B4'),
            'Kat': NameBox('Кэт', 'Kat', '#30D5C8'),
            'Nikolaya': NameBox('Джеймс', 'Nikolaya', '#fff'),
            'Girl': NameBox('Девушка', 'Girl', '#30D5C8'),
            'Guy': NameBox('Парень', 'Guy', '#fff'),
            'Goon': NameBox('Жлоб', 'Goon', '#fff'),
            
            
            
            }
        # if preferences.language == 'spn':
        #     store.nameboxes['Officer'] = NameBox('Oficial', 'Officer', '#fff')

        #     store.nameboxes['GirlOfficer'] = NameBox('Chica-Oficial', 'GirlOfficer', '#FF69B4', 800)
        #nameboxes = {}
        # for i in store.nameboxes:
        #     char = store.nameboxes[i]
        #     nameboxes.update({i:
        #         {
        #         'name':char.name,
        #         'sprite':char.sprite,
        #         'color':char.color,
        #         },
        #         })
        #     if char.x_size != 638:
        #         nameboxes[i].update({'x_size':char.x_size})

        store.name_boxes_displ = NameBoxesDispl(store.nameboxes)
        store.name_boxes_displ_flashlight = FlashLight(store.name_boxes_displ)


    CustomNameBox = NameBox
    class NameBoxesDispl(renpy.Displayable):
        
        
        
        def __init__(self, nameboxes, **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
           
            self.nameboxes = nameboxes


            for i in self.nameboxes:
                self.nameboxes[i].create_text_obj()

            self.force_update = False

            self.block_render = False
            
        def render(self, width, height, st, at):
            global persistent
            global store
            rend = renpy.Render(1920, 1080)
            if self.block_render:
                return rend
            say  = store.who_say_now

            blits = []

            if say not in store.showing_tags:
                if say in self.nameboxes:
                    blits.append(self.nameboxes[say])


            for sprite in store.showing_tags:

                if sprite in self.nameboxes:
                    blits.append(self.nameboxes[sprite])
            
            need_update = False
            # rend.blit(renpy.render(Text(str(say) + " " + str(len(blits))), 38, 475, 0.3, at), 
            #                (0, 0))
            # rrdd = 0
            if say != "with_statement":
                for namebox in blits:
                    # rrdd+=1
                    # rend.blit(renpy.render(Text(str(namebox.name)), 38, 475, 0.3, at), 
                    #        (0, rrdd*20))
                    dspl_img = renpy.display.core.displayable_by_tag(
                        "master", namebox.sprite)
                    alpha = namebox.alpha
                    if say == namebox.sprite:
                        if namebox.state not in ['up', 'need_up']:
                            namebox.start_anim_up()
                    else:
                        if namebox.state not in ['down', 'need_down']:
                            namebox.start_anim_down()
                
                    if dspl_img is not None:
                        _image = 'interface/custom_namebox.png'
                        get_placement = list(dspl_img.get_placement()) + [dspl_img.xzoom, dspl_img.yzoom, dspl_img.zoom, dspl_img.alpha]
                        point = get_placement[0]

                       # alpha = get_placement[10]
                        

                        if type(point) == float:
                            xp_tmp = int(1920.0*point-(float(namebox.x_size) *point ))
                            
                        else:
                            xp_tmp = point



                        namebox.xp = int(xp_tmp + (float(namebox.x_size)/2) - 177)

                        text_xp = int(namebox.xp + (float(355)/2) - float(namebox.text_obj_size_x)/2)
                        if not store.from_say_screen:
                            namebox.yp = 745
                            namebox.state = "down"
                            namebox.alpha = 0.0

                        elif namebox.state == "need_down":
                            
                            if namebox.yp >= 745:
                                namebox.yp = 745
                                namebox.state = "down"
                                namebox.alpha = 0.0

                            else:
                                namebox.yp = int(745.1 - (namebox.anim_yp_len - namebox.anim_get_cords()) )
                                namebox.alpha = (745.0 - namebox.yp)/10.0

                        elif namebox.state == "need_up":
                            
                            if namebox.yp <= 725:
                                namebox.yp = 725
                                namebox.state = "up"
                                namebox.alpha = 1.0

                            else:
                                namebox.yp = int(724.9 + (namebox.anim_yp_len - namebox.anim_get_cords()) )
                                namebox.alpha = (745.0 - namebox.yp)/10.0
                    else:
                        #alpha   = 1.0
                        namebox.alpha = 1.0
                        namebox.xp = 300
                        text_xp = int(namebox.xp + (float(355)/2) - float(namebox.text_obj_size_x)/2) 
                        namebox.yp = 744
     
                        _image = 'interface/custom_namebox_main.png'

                    xzoom = 1 


                    if store.mp.dialogue_interface_scale_number > 1.0:
                        _yp = namebox.yp - 100
                    else:
                        _yp = namebox.yp


                    if _image != namebox._image or xzoom != namebox.xzoom or alpha != namebox.alpha:
                        alpha  = namebox.alpha 
                        namebox._image = _image
                        namebox.xzoom  = xzoom
                        namebox.transform_obj_image = Transform(_image, alpha = namebox.alpha)

                        namebox.transform_obj = Transform(namebox.text_obj, alpha = namebox.alpha)
                        need_update = True

                    if namebox.state and namebox.state.startswith('need_'):
                        need_update = True                

                    if _yp > 724 and _yp < 745:
                        rend.blit(renpy.render(

                            namebox.transform_obj_image, 
                        
                            38, 475, st, at), (namebox.xp, _yp))
                        
                        

                        rend.blit(renpy.render(namebox.transform_obj, 500, 475, 0.3, at), 
                           (text_xp, namebox.yp+15))
                        
               
                
            #if need_update or self.force_update:
            renpy.redraw(self, 0)
            
            return rend