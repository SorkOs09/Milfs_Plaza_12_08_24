init -5 python:
    class CharacterSprite():
        
        def __init__(self, name, folder):
            
            self.name     = name
            
            self.poses    = []
            
            self.eays     = []
            
            self.mouths   = []
            
            self.emotions = []
            
            self.folder   = folder
            
            for fn in renpy.list_files(): 
                
                if fn.startswith(folder + '/mouths') and fn.endswith((".jpg", ".png")):
                    self.mouths.append(fn)
            
            for fn in renpy.list_files(): 
                
                if fn.startswith(folder + '/eays') and fn.endswith((".jpg", ".png")):
                    self.eays.append(fn)
            
            for fn in renpy.list_files(): 
                
                if fn.startswith(folder + '/poses') and fn.endswith((".jpg", ".png")):
                    self.poses.append(fn)

    def CreateLayeredImageNew(Character, folder):
        
        layeredimages = []
        
        
        
        for r in check_all_folders_new(folder):
            
            tmp = []
            i   = (tmp, r)
            
            for fn in renpy.list_files(): 
                
                if fn.startswith(folder + i[1]) and fn.endswith((".jpg", ".png")):
                    i[0].append(fn)
            for x in i[0]:
                a       = x[len(folder)+len(i[1])+1:-4]
                default = False
                if '_default' in a:
                    a       = a[:-8]
                    default = True
                layeredimages.append(

                layeredimage.Attribute(i[1], a, x, default = default))
        
        
        
        
        renpy.image(Character,    LayeredImage(layeredimages))







    custom_sprites = {

    }


    def CreateLayeredImageOld(Character, folder):
        
        layeredimages = []
        
        custom_sprites.update({Character:[]})
        
        for r in check_all_folders_old(folder):
            
            tmp = []
            i   = (tmp, r)
            
            for fn in renpy.list_files(): 
                
                if fn.startswith(folder + i[1]) and fn.endswith((".jpg", ".png")):
                    i[0].append(fn)
            for x in i[0]:
                a       = x[len(folder)+len(i[1])+1:-4]
                default = False
                if '_default' in a:
                    a       = a[:-8]
                    default = True
                layeredimages.append(

                layeredimage.Attribute(i[1], a, x, default = default))
                if '1poses' not in x.lower():
                    custom_sprites[Character].append(a)
        
        
        
        renpy.image(Character,    LayeredImage(layeredimages))

    def check_all_folders_new(folder):
        return_list = {
        'body'  : [],
        'emo'   : [],
        'exc'   : [],

        }
        for fn in renpy.list_files():
            if fn.startswith(folder) and fn.endswith((".jpg", ".png")):
                
                for i in ('body', 'emo', 'exc'):
                    if i + '/' in fn:
                        
                        a = fn[::-1][:fn[::-1].find('/')][::-1][:-4]
                        return_list[i].append(a)
        
        
        
        
        
        
        
        return return_list




    def check_all_folders_old(folder):
        return_list = []
        for fn in renpy.list_files():
            if fn.startswith(folder) and fn.endswith((".jpg", ".png")):
                if fn[len(folder):].count('/') == 1:
                    a = fn[::-1][fn[::-1].find('/'):][1:]
                    b = a[:a.find('/')][::-1]
                    if b not in return_list:
                        return_list.append(b) 
        
        
        
        return return_list



    CreateLayeredImageOld('GG',  'images/characters/GG/')

    _custom_sprites_gg = custom_sprites['GG']

    for i in (
        'Passion', 'Embarrassment', 
        'Normal',  'Silence', 
        'WTF',     'Speak', 
        'Black',   'Please', 
        'Smile',   'Chagrin', 
        'Surprise'):
        if i not in _custom_sprites_gg:
            _custom_sprites_gg.append(i)
        for j in ('B', 'Jaket', 'Costume', 'Night', 'Joker', 'Bat', 'Prison'):
            if j+'_'+i not in _custom_sprites_gg:
                _custom_sprites_gg.append(j+'_'+i)
        
    _custom_sprites_gg.append('Jaket_Skepticism')

    _custom_sprites_gg.append('Costume_Skepticism')
    
    _custom_sprites_gg.append('Prison_Angry')
    for i in (
        'emo_atlas', 
        'Sperm 1',
        'Sperm 2',
        'Sperm 3',
        'Sperm 4',
        'Sperm 5',
        ):
        
        if i in _custom_sprites_gg:
            _custom_sprites_gg.remove(i)
    
    try:
        del _custom_sprites_gg
    except:
        pass


    CreateLayeredImageOld('Prostitute', 'images/characters/Prostitute/')
    
    CreateLayeredImageOld('Milf', 'images/characters/Milf/')

    CreateLayeredImageOld('GirlOfficer', 'images/characters/GirlOfficer/')

    CreateLayeredImageOld('Officer', 'images/characters/Officer/')

    CreateLayeredImageOld('Christie', 'images/characters/Christie/')

    CreateLayeredImageOld('Jay', 'images/characters/Jay/')

    CreateLayeredImageOld('Bob', 'images/characters/Bob/')

    CreateLayeredImageOld('Igor', 'images/characters/Igor/')

    CreateLayeredImageOld('Misha', 'images/characters/Misha/')

    CreateLayeredImageOld('Psi', 'images/characters/Psi/')

    CreateLayeredImageOld('GirlInStore', 'images/characters/GirlInStore/')

    CreateLayeredImageOld('WomanTrade', 'images/characters/WomanTrade/')

    CreateLayeredImageOld('RestAdmin', 'images/characters/RestAdmin/')

    CreateLayeredImageOld('RestFamily', 'images/characters/RestFamily/')

    CreateLayeredImageOld('Nikolaya', 'images/characters/Nikolaya/')

    CreateLayeredImageOld('Kat', 'images/characters/Kat/')



    CreateLayeredImageOld('Bandit', 'images/characters/Bandit/')




    CreateLayeredImageOld('Masha', 'images/characters/Masha/')

    CreateLayeredImageOld('BandtiWithPistol', 'images/characters/BandtiWithPistol/')

    CreateLayeredImageOld('BiblioGirl', 'images/characters/BiblioGirl/')

    custom_sprites['Misha'].append('Water_Embarrassment')

    custom_sprites['Misha'].append('Water_Passion')

    custom_sprites['Misha'].append('Water_Normal')

    custom_sprites['Misha'].append('Water_Surprise')

    custom_sprites['Misha'].append('Water_Laughs')

    custom_sprites['Misha'].append('Water_Read')

    custom_sprites['Misha'].append('Water_Chagrin')

    custom_sprites['Misha'].append('Water_Smile')



    custom_sprites['Milf'].append('Passion')

    custom_sprites['Milf'].append('Smile')

    custom_sprites['Milf'].append('Chagrin')

    custom_sprites['Milf'].append('Normal')

    custom_sprites['Milf'].append('Embarrassment')

    custom_sprites['Milf'].append('Gipno')

    custom_sprites['Milf'].append('Surprise')

    custom_sprites['Milf'].append('Night_Angry')

    custom_sprites['Milf'].append('Night_Chagrin')

    custom_sprites['Milf'].append('Night_Embarrassment')

    custom_sprites['Milf'].append('Night_Gipno')

    custom_sprites['Milf'].append('Night_Normal')

    custom_sprites['Milf'].append('Night_Passion')

    custom_sprites['Milf'].append('Night_Smile')

    custom_sprites['Milf'].append('Night_Surprise')


    custom_sprites['Milf'].append('Night_Angry_pose_2')

    custom_sprites['Milf'].append('Night_Chagrin_pose_2')

    custom_sprites['Milf'].append('Night_Embarrassment_pose_2')

    custom_sprites['Milf'].append('Night_Gipno_pose_2')

    custom_sprites['Milf'].append('Night_Normal_pose_2')

    custom_sprites['Milf'].append('Night_Passion_pose_2')

    custom_sprites['Milf'].append('Night_Smile_pose_2')

    custom_sprites['Milf'].append('Night_Surprise_pose_2')

    custom_sprites['Milf'].append('Night_Angry_pose_3')

    custom_sprites['Milf'].append('Night_Chagrin_pose_3')

    custom_sprites['Milf'].append('Night_Embarrassment_pose_3')

    custom_sprites['Milf'].append('Night_Gipno_pose_3')

    custom_sprites['Milf'].append('Night_Normal_pose_3')

    custom_sprites['Milf'].append('Night_Passion_pose_3')

    custom_sprites['Milf'].append('Night_Smile_pose_3')

    custom_sprites['Milf'].append('Night_Surprise_pose_3')



image Misha Water_Embarrassment = Composite((596, 1080),
(112, 201),  Crop((0,306,462,879), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png"),
(196, 303),  Crop((0,0,116,100), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png")
)


image Misha Water_Passion = Composite((596, 1080),
(112, 201),  Crop((0,306,462,879), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png"),
(195, 304),  Crop((126,0,126,97), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png")
)



image Misha Water_Surprise = Composite((596, 1080),
(112, 201),  Crop((0,306,462,879), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png"),
(198, 299),  Crop((0,100,111,110), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png")

)


image Misha Water_Laughs = Composite((596, 1080),
(112, 201),  Crop((0,306,462,879), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png"),
(198, 303),  Crop((336,0,112,103), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png")
)




image Misha Water_Read = Composite((596, 1080),
(112, 201),  Crop((0,306,462,879), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png"),
(196, 302),  Crop((508,0,127,99), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png")
)



image Misha Water_Normal = Composite((596, 1080),
(112, 201),  Crop((0,306,462,879), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png"),
(196, 303),  Crop((732,0,122,98), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png")
)


image Misha Water_Chagrin = Composite((596, 1080),
(112, 201),  Crop((0,306,462,879), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png"),
(197, 305),  Crop((0,210,126,96), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png"),
)


image Misha Water_Smile = Composite((596, 1080),
(112, 201),  Crop((0,306,462,879), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png"),

(199, 303),  Crop((880,0,110,101), "cg/christie_root/misha_store/misha_water/misha_water_atlas.png")
)




# image Milf_Chagrin = Crop((0, 0, 170, 170), "characters/Milf/atlas/emo_atlas.png")
# image Milf_Embarrassment = Crop((170, 0, 170, 170), "characters/Milf/atlas/emo_atlas.png")
# image Milf_Normal = Crop((340, 0, 170, 170), "characters/Milf/atlas/emo_atlas.png")



# image Milf_Passion = Crop((0, 170, 170, 170), "characters/Milf/atlas/emo_atlas.png")
# image Milf_Sad = Crop((170, 170, 170, 170), "characters/Milf/atlas/emo_atlas.png")
# image Milf_Silence = Crop((340, 170, 170, 170), "characters/Milf/atlas/emo_atlas.png")


# image Milf_Smile = Crop((0, 340, 170, 170), "characters/Milf/atlas/emo_atlas.png")
# image Milf_Surprise = Crop((170, 340, 170, 170), "characters/Milf/atlas/emo_atlas.png")
# image Milf_Troll = Crop((340, 340, 170, 170), "characters/Milf/atlas/emo_atlas.png")





image Milf Passion = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_costume].png",
(227, 154),  Crop((0,0,122,111), "characters/Milf/atlas/emo_atlas.png"))


image Milf Smile = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_costume].png",
(227, 154),  Crop((123,0,122,111), "characters/Milf/atlas/emo_atlas.png"))



image Milf Chagrin = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_costume].png",
(227, 154),  Crop((246,0,122,111), "characters/Milf/atlas/emo_atlas.png"))



image Milf Normal = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_costume].png",
(227, 154),  Crop((369,0,122,111), "characters/Milf/atlas/emo_atlas.png"))


image Milf OK = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_costume].png",
(227, 154),  Crop((369,0,122,111), "characters/Milf/atlas/emo_atlas.png"))




image Milf Embarrassment = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_costume].png",
(227, 154),  Crop((492,0,122,111), "characters/Milf/atlas/emo_atlas.png"))



image Milf Gipno = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_costume].png",
(227, 154),  Crop((615,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Surprise = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_costume].png",
(227, 154),  Crop((738,0,122,111), "characters/Milf/atlas/emo_atlas.png"))





image Milf Night_Angry = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_1].png",
(227, 154),  Crop((984,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Chagrin = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/Night_Pose_1.png",
(227, 154),  Crop((246,0,122,111), "characters/Milf/atlas/emo_atlas.png"))



image Milf Night_Embarrassment = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_1].png",
(227, 154),  Crop((492,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Gipno = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_1].png",
(227, 154),  Crop((615,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Normal = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_1].png",
(227, 154),  Crop((369,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Passion = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_1].png",
(227, 154),  Crop((0,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Smile = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_1].png",
(227, 154),  Crop((123,0,122,111), "characters/Milf/atlas/emo_atlas.png"))


image Milf Night_Surprise = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_1].png",
(227, 154),  Crop((738,0,122,111), "characters/Milf/atlas/emo_atlas.png"))




image Milf Night_Angry_pose_2 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_2].png",
(227, 154),  Crop((984,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Chagrin_pose_2 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_2].png",
(227, 154),  Crop((246,0,122,111), "characters/Milf/atlas/emo_atlas.png"))


image Milf Night_Embarrassment_pose_2 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_2].png",
(227, 154),  Crop((492,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Gipno_pose_2 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_2].png",
(227, 154),  Crop((615,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Normal_pose_2 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_2].png",
(227, 154),  Crop((369,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Passion_pose_2 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_2].png",
(227, 154),  Crop((0,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Smile_pose_2 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_2].png",
(227, 154),  Crop((123,0,122,111), "characters/Milf/atlas/emo_atlas.png"))


image Milf Night_Surprise_pose_2 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_2].png",
(227, 154),  Crop((738,0,122,111), "characters/Milf/atlas/emo_atlas.png"))




image Milf Night_Angry_pose_3 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_3].png",
(190, 155),  Crop((984,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Chagrin_pose_3 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_3].png",
(189, 154),  Crop((246,0,122,111), "characters/Milf/atlas/emo_atlas.png"))


image Milf Night_Embarrassment_pose_3 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_3].png",
(188, 154),  Crop((492,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Gipno_pose_3 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_3].png",
(188, 154),  Crop((615,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Normal_pose_3 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_3].png",
(188, 154),  Crop((369,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Passion_pose_3 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_3].png",
(188, 154),  Crop((0,0,122,111), "characters/Milf/atlas/emo_atlas.png"))

image Milf Night_Smile_pose_3 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_3].png",
(188, 154),  Crop((123,0,122,111), "characters/Milf/atlas/emo_atlas.png"))


image Milf Night_Surprise_pose_3 = Composite((638, 976),
(0, 0),     "characters/Milf/1POSES/[milf_night_costume_3].png",
(188, 154),  Crop((738,0,122,111), "characters/Milf/atlas/emo_atlas.png"))



image GG Pose_0 = 'characters/GG/1POSES/0.png'

image GG Pose_1 = 'characters/GG/1POSES/1.png'

image GG Pose_2 = 'characters/GG/1POSES/2.png'

image GG Pose_3 = 'characters/GG/1POSES/3.png'

image GG Pose_4 = 'characters/GG/1POSES/4.png'

image GG Pose_5 = 'characters/GG/1POSES/5.png'

#image GG Pose_6 = 'characters/GG/1POSES/6.png'

image GG Pose_7 = 'characters/GG/1POSES/7.png'

image GG Pose_8 = 'characters/GG/1POSES/8.png'

image GG Emo_Passion =  Crop((0,0,106,108), "characters/GG/atlas/emo_atlas.png")#(306, 297),

image GG Emo_Embarrassment = Crop((206,0,103,107), "characters/GG/atlas/emo_atlas.png")#(307, 298)



image GG Emo_Normal = Crop((321,0,107,106), "characters/GG/atlas/emo_atlas.png") #(305, 299)

image GG Emo_WTF = Crop((525,0,105,104), "characters/GG/atlas/emo_atlas.png") #(307, 301)

image GG Emo_Speak = Crop((0,108,108,109), "characters/GG/atlas/emo_atlas.png")#(304, 298),  

image GG Emo_Black = Composite((161, 106),
(46, -19),  'GG Emo_Normal',
(0, 0),  Crop((644,0,161,55), "characters/GG/atlas/emo_atlas.png"),
)

 #(259, 318),  

image GG Emo_Please = Crop((824,0,103,111), "characters/GG/atlas/emo_atlas.png") # (307, 300),  

image GG Emo_Smile = Crop((936,0,104,108), "characters/GG/atlas/emo_atlas.png") # (307, 299),  

 
image GG Emo_Chagrin = Crop((1040,0,104,105), "characters/GG/atlas/emo_atlas.png")# (307, 299),


image GG Emo_Surprise = Crop((1155,0,105,115), "characters/GG/atlas/emo_atlas.png") #(307, 295),



# #################################################################################

# image GG Bat_Passion = Composite((596, 1080),
# (0, 0),  'GG Pose_6',
# (306, 297),  'GG Emo_Passion',
# )


# image GG Bat_Embarrassment = Composite((596, 1080),
# (0, 0),  'GG Pose_6',
# (307, 298),  'GG Emo_Embarrassment',
# )

# image GG Bat_Normal = Composite((596, 1080),
# (0, 0),  'GG Pose_6',
# (305, 299),  'GG Emo_Normal',
# )


# image GG Bat_WTF = Composite((596, 1080),
# (0, 0),  'GG Pose_6',
# (307, 301),  'GG Emo_WTF',
# )

# image GG Bat_Speak = Composite((596, 1080),
# (0, 0),  'GG Pose_6',
# (304, 298),  'GG Emo_Speak',
# )


# image GG Bat_Black = Composite((596, 1080),
# (0, 0),  'GG Pose_6',
# (259, 318),  'GG Emo_Black',
# )

# image GG Bat_Please = Composite((596, 1080),
# (0, 0),  'GG Pose_6',
# (307, 300),  'GG Emo_Please',
# )

# image GG Bat_Smile = Composite((596, 1080),
# (0, 0),  'GG Pose_6',
# (307, 299),  'GG Emo_Smile',
# )


# image GG Bat_Chagrin = Composite((596, 1080),
# (0, 0),  'GG Pose_6',
# (307, 299),  'GG Emo_Chagrin',
# )


# image GG Bat_Surprise = Composite((596, 1080),
# (0, 0),  'GG Pose_6',
# (307, 295),  'GG Emo_Surprise',
# )




#################################################################################



image GG Prison_Passion = Composite((596, 1080),
(0, 0),  'GG Pose_8',
(306, 297),  'GG Emo_Passion',
)


image GG Prison_Embarrassment = Composite((596, 1080),
(0, 0),  'GG Pose_8',
(307, 298),  'GG Emo_Embarrassment',
)

image GG Prison_Normal = Composite((596, 1080),
(0, 0),  'GG Pose_8',
(305, 299),  'GG Emo_Normal',
)

image GG Prison_WTF = Composite((596, 1080),
(0, 0),  'GG Pose_8',
(307, 301),  'GG Emo_WTF',
)



image GG Prison_Speak = Composite((596, 1080),
(0, 0),  'GG Pose_8',
(304, 298),  'GG Emo_Speak',
)


image GG Prison_Black = Composite((596, 1080),
(0, 0),  'GG Pose_8',
(259, 318),  'GG Emo_Black',
)

image GG Prison_Please = Composite((596, 1080),
(0, 0),  'GG Pose_8',
(307, 300),  'GG Emo_Please',
)

image GG Prison_Smile = Composite((596, 1080),
(0, 0),  'GG Pose_8',
(307, 299),  'GG Emo_Smile',
)


image GG Prison_Chagrin = Composite((596, 1080),
(0, 0),  'GG Pose_8',
(307, 299),  'GG Emo_Chagrin',
)


image GG Prison_Surprise = Composite((596, 1080),
(0, 0),  'GG Pose_8',
(307, 295),  'GG Emo_Surprise',
)



#################################################################################

image GG B_Passion = Composite((596, 1080),
(0, 0),  'GG Pose_0',
(306, 297),  'GG Emo_Passion',
)


image GG B_Embarrassment = Composite((596, 1080),
(0, 0),  'GG Pose_0',
(307, 298),  'GG Emo_Embarrassment',
)

image GG B_Normal = Composite((596, 1080),
(0, 0),  'GG Pose_0',
(305, 299),  'GG Emo_Normal',
)

image GG B_Silence = 'GG B_Normal'


image GG B_WTF = Composite((596, 1080),
(0, 0),  'GG Pose_0',
(307, 301),  'GG Emo_WTF',
)



image GG B_Speak = Composite((596, 1080),
(0, 0),  'GG Pose_0',
(304, 298),  'GG Emo_Speak',
)


image GG B_Black = Composite((596, 1080),
(0, 0),  'GG Pose_0',
(259, 318),  'GG Emo_Black',
)

image GG B_Please = Composite((596, 1080),
(0, 0),  'GG Pose_0',
(307, 300),  'GG Emo_Please',
)

image GG B_Smile = Composite((596, 1080),
(0, 0),  'GG Pose_0',
(307, 299),  'GG Emo_Smile',
)


image GG B_Chagrin = Composite((596, 1080),
(0, 0),  'GG Pose_0',
(307, 299),  'GG Emo_Chagrin',
)


image GG B_Surprise = Composite((596, 1080),
(0, 0),  'GG Pose_0',
(307, 295),  'GG Emo_Surprise',
)

######################



image GG Joker_Passion = Composite((596, 1080),
(0, 0),  'GG Pose_5',
(306, 297),  'GG Emo_Passion',
)


image GG Joker_Embarrassment = Composite((596, 1080),
(0, 0),  'GG Pose_5',
(307, 298),  'GG Emo_Embarrassment',
)

image GG Joker_Normal = Composite((596, 1080),
(0, 0),  'GG Pose_5',
(305, 299),  'GG Emo_Normal',
)


image GG Joker_WTF = Composite((596, 1080),
(0, 0),  'GG Pose_5',
(307, 301),  'GG Emo_WTF',
)

image GG Joker_Speak = Composite((596, 1080),
(0, 0),  'GG Pose_5',
(304, 298),  'GG Emo_Speak',
)


image GG Joker_Black = Composite((596, 1080),
(0, 0),  'GG Pose_5',
(259, 318),  'GG Emo_Black',
)

image GG Joker_Please = Composite((596, 1080),
(0, 0),  'GG Pose_5',
(307, 300),  'GG Emo_Please',
)

image GG Joker_Smile = Composite((596, 1080),
(0, 0),  'GG Pose_5',
(307, 299),  'GG Emo_Smile',
)


image GG Joker_Chagrin = Composite((596, 1080),
(0, 0),  'GG Pose_5',
(307, 299),  'GG Emo_Chagrin',
)


image GG Joker_Surprise = Composite((596, 1080),
(0, 0),  'GG Pose_5',
(307, 295),  'GG Emo_Surprise',
)










#####################
image GG Costume_Passion = Composite((596, 1080),
(0, 0),  'GG Pose_3',
(306, 297),  'GG Emo_Passion',
)


image GG Costume_Embarrassment = Composite((596, 1080),
(0, 0),  'GG Pose_3',
(307, 298),  'GG Emo_Embarrassment',
)

image GG Costume_Normal = Composite((596, 1080),
(0, 0),  'GG Pose_3',
(305, 299),  'GG Emo_Normal',
)

image GG Costume_WTF = Composite((596, 1080),
(0, 0),  'GG Pose_3',
(307, 301),  'GG Emo_WTF',
)

image GG Costume_Skepticism = 'GG Costume_WTF' 
image GG Costume_Silence = "GG Costume_Normal"

image GG Costume_Speak = Composite((596, 1080),
(0, 0),  'GG Pose_3',
(304, 298),  'GG Emo_Speak',
)


image GG Costume_Black = Composite((596, 1080),
(0, 0),  'GG Pose_3',
(259, 318),  'GG Emo_Black',
)

image GG Costume_Please = Composite((596, 1080),
(0, 0),  'GG Pose_3',
(307, 300),  'GG Emo_Please',
)

image GG Costume_Smile = Composite((596, 1080),
(0, 0),  'GG Pose_3',
(307, 299),  'GG Emo_Smile',
)


image GG Costume_Chagrin = Composite((596, 1080),
(0, 0),  'GG Pose_3',
(307, 299),  'GG Emo_Chagrin',
)


image GG Costume_Surprise = Composite((596, 1080),
(0, 0),  'GG Pose_3',
(307, 295),  'GG Emo_Surprise',
)
















#####################################



image GG Jaket_Passion = Composite((596, 1080),
(0, 0),  'GG Pose_2',
(306, 297),  'GG Emo_Passion',
)


image GG Jaket_Embarrassment = Composite((596, 1080),
(0, 0),  'GG Pose_2',
(307, 298),  'GG Emo_Embarrassment',
)

image GG Jaket_Normal = Composite((596, 1080),
(0, 0),  'GG Pose_2',
(305, 299),  'GG Emo_Normal',
)

image GG Jaket_Silence = 'GG Jaket_Normal'


image GG Jaket_WTF = Composite((596, 1080),
(0, 0),  'GG Pose_2',
(307, 301),  'GG Emo_WTF',
)

image GG Jaket_Skepticism = 'GG Jaket_WTF' 


image GG Jaket_Speak = Composite((596, 1080),
(0, 0),  'GG Pose_2',
(304, 298),  'GG Emo_Speak',
)


image GG Jaket_Black = Composite((596, 1080),
(0, 0),  'GG Pose_2',
(259, 318),  'GG Emo_Black',
)

image GG Jaket_Please = Composite((596, 1080),
(0, 0),  'GG Pose_2',
(307, 300),  'GG Emo_Please',
)

image GG Jaket_Smile = Composite((596, 1080),
(0, 0),  'GG Pose_2',
(307, 299),  'GG Emo_Smile',
)


image GG Jaket_Chagrin = Composite((596, 1080),
(0, 0),  'GG Pose_2',
(307, 299),  'GG Emo_Chagrin',
)


image GG Jaket_Surprise = Composite((596, 1080),
(0, 0),  'GG Pose_2',
(307, 295),  'GG Emo_Surprise',
)






##########################################


image GG Night_Passion = Composite((596, 1080),
(0, 0),  'GG Pose_4',
(306, 297),  'GG Emo_Passion',
)


image GG Night_Embarrassment = Composite((596, 1080),
(0, 0),  'GG Pose_4',
(307, 298),  'GG Emo_Embarrassment',
)

image GG Night_Normal = Composite((596, 1080),
(0, 0),  'GG Pose_4',
(305, 299),  'GG Emo_Normal',
)


image GG Night_WTF = Composite((596, 1080),
(0, 0),  'GG Pose_4',
(307, 301),  'GG Emo_WTF',
)

image GG Night_Speak = Composite((596, 1080),
(0, 0),  'GG Pose_4',
(304, 298),  'GG Emo_Speak',
)


image GG Night_Black = Composite((596, 1080),
(0, 0),  'GG Pose_4',
(259, 318),  'GG Emo_Black',
)

image GG Night_Please = Composite((596, 1080),
(0, 0),  'GG Pose_4',
(307, 300),  'GG Emo_Please',
)

image GG Night_Smile = Composite((596, 1080),
(0, 0),  'GG Pose_4',
(307, 299),  'GG Emo_Smile',
)


image GG Night_Chagrin = Composite((596, 1080),
(0, 0),  'GG Pose_4',
(307, 299),  'GG Emo_Chagrin',
)


image GG Night_Surprise = Composite((596, 1080),
(0, 0),  'GG Pose_4',
(307, 295),  'GG Emo_Surprise',
)



























########################################
image GG Passion = Composite((596, 1080),
(0, 0),  'GG Pose_1',
(306, 297),  'GG Emo_Passion',
)


image GG Embarrassment = Composite((596, 1080),
(0, 0),  'GG Pose_1',
(307, 298),  'GG Emo_Embarrassment',
)

image GG Normal = Composite((596, 1080),
(0, 0),  'GG Pose_1',
(305, 299),  'GG Emo_Normal',
)

image GG Silence = 'GG Normal'


image GG WTF = Composite((596, 1080),
(0, 0),  'GG Pose_1',
(307, 301),  'GG Emo_WTF',
)



image GG Speak = Composite((596, 1080),
(0, 0),  'GG Pose_1',
(304, 298),  'GG Emo_Speak',
)


image GG Black = Composite((596, 1080),
(0, 0),      'GG Pose_1',
(259, 318),  'GG Emo_Black',
)

image GG Please = Composite((596, 1080),
(0, 0),  'GG Pose_1',
(307, 300),  'GG Emo_Please',
)

image GG Smile = Composite((596, 1080),
(0, 0),  'GG Pose_1',
(307, 299),  'GG Emo_Smile',
)


image GG Chagrin = Composite((596, 1080),
(0, 0),  'GG Pose_1',
(307, 299),  'GG Emo_Chagrin',
)


image GG Surprise = Composite((596, 1080),
(0, 0),  'GG Pose_1',
(307, 295),  'GG Emo_Surprise',
)


image GG Skepticism = 'GG Think'



image black = Solid('#000')

image white = Solid('#fff')

#fixes

image invis = Composite((638, 976),
    (0, 0), "#0000",

)

image Goon Invis = 'invis'


init python:


    for i in custom_sprites:
        renpy.image(i + " Invis", 'invis')