
transform ButtonEffect07:
    on idle:
        easein 0.2 alpha 0.7
    on hover:
        easein 0.2 alpha 1.0
init python:

    def get_sms_block_by_id(who, id):
        global phone_sms_screen
        for i in phone_sms_screen[who]:
            if i.id == id:
                return i 
    class SmsBlock():
        
        def __init__(self, who, avatar, id = "1", func=NullAction()):
            global phone_sms_screen
            self.who    = who
            self.id     = id
            self.avatar = avatar
            self.func   = func
            self.check  = False
            self.list   = []
            self.readed = 0
            if get_sms_block_by_id(who, id) is None:
                
                phone_sms_screen[who].append(self)
        
        def back(self):
            if not self.check:
                self.check = True
                self.func()
        
        def add_sms(self, what):
            self.list.append(what)











    def add_sms_func(who = 'Игорь', what = NullAction()):
        if who in phone_sms_screen:
            if what not in phone_sms_screen[who]['Func']:
                phone_sms_screen[who]['Func'].append(what)

    def del_sms_func(who = 'Игорь', what = NullAction()):
        if who in phone_sms_screen:
            if what in phone_sms_screen[who]['Func']:
                phone_sms_screen[who]['Func'].remove(what)

    def phone_sms_screen_unset_func(who = 'Игорь'): 
        phone_sms_screen[who]['Func'] = []
    def set_sms_check(who):
        global phone_sms_screen
        pass


    def get_sms_check(who = None):
        global phone_sms_screen
        if hasattr(store, 'phone_sms_screen'):
            if who:
                for i in phone_sms_screen[who]:
                    if not i.check:
                        
                        return True
                return None
            for w in phone_sms_screen:
                for i in phone_sms_screen[w]:
                    if not i.check:
                        
                        return True


    eng_contacts_names = {

    'Игорь' : 'Igor'
    }

    # _ava_to_names = {



    # 'milf' : 'Mary'
    
    # }

    def get_not_empty_sms():
        global phone_sms_screen
        rtrn = []
        for i in phone_sms_screen:
            if len(phone_sms_screen[i]):
                rtrn.append(i)
        return rtrn



screen phone_contacts_screen():

    zorder 20
    
    default not_empty_sms = get_not_empty_sms()

    imagebutton:
        idle '#0000'
        hover '#0000'
        action Hide('phone_contacts_screen')
    add 'interface/phone_interface/phone_contacts_bg.png'
    viewport xpos 795 ypos 232:
        xmaximum 410
        ymaximum 80
        add '#0000'

        text __('Контакты') xalign .5 yalign .5 outlines [(2, "#000", 0, 0)]


    viewport:
        xpos 790 ypos 315
        xmaximum 420
        ymaximum 610

        if len(not_empty_sms) > 4:
            scrollbars 'vertical'
            mousewheel True

        vbox:
            for i in not_empty_sms:
                $ n_ava  = phone_sms_screen[i][0].avatar
                $ ava    = 'interface/phone_interface/Contacts_ava_'+n_ava+'.png'
                if n_ava == 'milf':

                    $ n_name = 'Mary'

                else:
                    $ n_name = n_ava.title()

                $ n_name = _get_translated_name_kostil(n_name)

                viewport:

                    xmaximum 422
                    ymaximum 143
                    add ava
                    
                    text n_name xalign .9 yalign .5 outlines [(2, "#000", 0, 0)]
                    imagebutton:
                        idle ava
                        hover im.MatrixColor(ava, im.matrix.brightness(.3))
                        at ButtonEffect07

                        action Function(renpy.play, 'audio/mobile.ogg'), Show('phone_contacts_screen_2', who = i)


                    if get_sms_check(unicode(i)):
                        add 'warning_icon' ypos 100 xpos 125
    add 'interface/phone_interface/phone_frame_bg.png'
    
init python:
    def _short_sms_kostil(sms):
        try:
            Text(sms)
            return sms
            
        except:
            sms = sms.replace('[', '')
            sms = sms.replace(']', '')
            sms = sms.replace('{', '')
            sms = sms.replace('}', '')
            sms = sms.replace('\\', '')
            return sms
            

screen phone_contacts_screen_2(who):
    default sms_list = phone_sms_screen[who]
    zorder 20
    imagebutton:
        idle '#0000'
        hover '#0000'
        action Hide('phone_contacts_screen_2')
    add 'interface/phone_interface/phone_contacts_bg.png'
    viewport xpos 795 ypos 232:
        xmaximum 410
        ymaximum 80
        add '#0000'

        text __('Сообщения') xalign .5 yalign .5 outlines [(2, "#000", 0, 0)]
    viewport:
        xpos 790 ypos 315
        xmaximum 420
        ymaximum 610

        if len(sms_list) > 4:
            scrollbars 'vertical'
            mousewheel True

        vbox:
            for i in sms_list[::-1]:

                $ ava = 'interface/phone_interface/Contacts_ava_'+i.avatar+'.png'
                $ txt = i.list[0]
                viewport:
                    xmaximum 422
                    ymaximum 143
                    add ava
                    if txt[4:].upper() in ('[NPHOTO]', '[NPHOTO_2]'):
                        text _('{i}Фото{/i}') size 19 xpos 170 yalign .5 outlines [(2, "#000", 0, 0)]
                    else:
                        if len(txt) > 25:
                            

                            text _short_sms_kostil(__(txt)[4:25]) + "..." size 19 xpos 170 yalign .5 outlines [(2, "#000", 0, 0)]
                        else:
                            text __(txt)[4:] size 19 xpos 170 yalign .5 outlines [(2, "#000", 0, 0)]
                    imagebutton:
                        idle ava
                        hover im.MatrixColor(ava, im.matrix.brightness(.3))
                        at ButtonEffect07
                        if i.check:
                            action Function(renpy.play, 'audio/mobile.ogg'), Show('phone_sms_screen', text_now=i.list, who = i.who, len_text_now = len(i.list), back = Function(i.back))
                        else:
                            action Function(renpy.play, 'audio/mobile.ogg'), Show('phone_sms_screen', text_now=i.list, who = i.who, len_text_now = 1, back = Function(i.back))
                    if not i.check:
                        add 'warning_icon' ypos 100 xpos 125
    add 'interface/phone_interface/phone_frame_bg.png'



init python:
    def sms_kostil(text):
        ret_text = []
        for i in xrange(3):
            try:
                ret_text.append(text.pop(len(text)-1))
            
            
            except:
                pass
        return ret_text[::-1]


    phone_func_now = -1
    phone_who_now  = None

init 110 python:
    def _get_translated_name_kostil(name):
        if preferences.language == 'eng':
            return name

        eng_names   = store._translated_names['eng']
        if name not in eng_names:
            return name
        
        names  = store._translated_names[preferences.language]
        name_index = eng_names.index(name)
        name       = names[name_index]
        return name
screen phone_sms_screen(text_now, who='Игорь', len_text_now=0, rtrn=None, back=NullAction()):
    zorder 20
    default check_preferences_language = preferences.language not in (None, 'rus', 'eng')
    imagebutton:
        idle '#0000'
        hover '#0000'
        if len_text_now != len(text_now):
            action NullAction()
        else:
            if rtrn is not None:
                action Return()
            else:
                action [Hide('phone_sms_screen'),]+[back, ]




    add 'phone_sms_bg'

    viewport ypos 232 xpos 790:
        ymaximum 64
        xmaximum 240
        add '#0000'
        if preferences.language in (None, 'eng', 'rus'):
            text _get_translated_name_kostil(str(who)) outlines [(2, "#000", 0, 0)] xalign .5 yalign .5

    if len_text_now != len(text_now):


        imagebutton:
            idle '#0000'
            hover '#0000'

            action Function(renpy.play, 'audio/mobile.ogg'), Show('phone_sms_screen', text_now = text_now, who = who, len_text_now = len_text_now+1, rtrn = rtrn, back = back)
    viewport ypos 300 xpos 810:
        xmaximum 100000000
        ymaximum 534
        scrollbars 'vertical'
        mousewheel True
        add '#0000'
        vbox yalign .99 ypos 534:
        #vbox:
            spacing 10
            for i in sms_kostil(text_now[:len_text_now]):





                if 'GG' in i:
                    hbox:
                        add 'interface/phone_interface/SMS_ava_gg.png'
                        vbox:
                            add Crop((0,   0,  320, 30), 'interface/chat.png')



                            $ cc = __(i)[4:].count('\n')
                            if not cc:
                                $ cc = 75
                            else:
                                $ cc = cc*70

                            if check_preferences_language:
                                $ cc += 10

                            viewport:
                                xmaximum 320
                                ymaximum cc
                                add Frame(Crop((0,   40, 320, 100), 'interface/chat.png'))
                                viewport xpos 20:
                                    image 'alpha_solid'
                                    maximum (290, cc)

                                    text __(i)[4:]: 
                                        yalign .5 
                                        color '#000'

                                        if check_preferences_language:
                                            size 20
                                        else:
                                            size 22

                            add Crop((0,   200, 320, 30), 'interface/chat.png')
                else:
                    hbox:
                        vbox:
                            add Crop((0,   0,  320, 30), 'interface/chat.png') xzoom -1
                            $ cc = __(i)[4:].count('\n')
                            
                            if not cc:
                                $ cc = 75
                            else:
                                $ cc = cc*70

                            if check_preferences_language:
                                $ cc += 10
                            viewport:
                                xmaximum 320
                                add Frame(Crop((0,   40, 320, 100), 'interface/chat.png')) xzoom -1
                                if hasattr(store, 'NPHOTO') and _(i)[4:].upper() == '[NPHOTO]':
                                    ymaximum 320
                                    add NPHOTO xalign .5 yalign .5
                                    viewport:
                                        xmaximum 300
                                        xalign .5 yalign .5
                                        imagebutton:
                                            idle '#0000'
                                            hover '#fffa'
                                            action Show('sms_photo_full_screen', n_image = NPHOTO.replace('_mini.', '.'))
                                elif hasattr(store, 'NPHOTO_2') and _(i)[4:].upper() == '[NPHOTO_2]':
                                    ymaximum 320
                                    add NPHOTO_2 xalign .5 yalign .5
                                    viewport:
                                        xmaximum 300
                                        xalign .5 yalign .5
                                        imagebutton:
                                            idle '#0000'
                                            hover '#fffa'
                                            action Show('sms_photo_full_screen', n_image = NPHOTO_2.replace('_mini.', '.'))
                                else:
                                    ymaximum cc

                                    viewport xpos 10:
                                        image 'alpha_solid'
                                        maximum (290, cc)

                                        text __(i)[4:]: 
                                            yalign .5 
                                            color '#000' 
                                            if check_preferences_language:
                                                size 20
                                            else:
                                                size 22


                            add Crop((0,   200, 320, 30), 'interface/chat.png') xzoom -1
                        add 'interface/phone_interface/SMS_ava_'+phone_sms_screen[who][0].avatar+'.png'


            if len_text_now != len(text_now):








                viewport:
                    xmaximum 920
                    ymaximum 130
                    if 'GG' not in i:
                        hbox:
                            add 'interface/phone_interface/SMS_ava_gg.png'
                            vbox:
                                add Crop((0,   0,  320, 30), 'interface/chat.png')

                                $ cc = __(i)[4:].count('\n')
                                if not cc:
                                    $ cc = 1
                                viewport:
                                    xmaximum 320
                                    ymaximum 50
                                    add Frame(Crop((0,   40, 320, 100), 'interface/chat.png'))
                                    hbox xalign .5 yalign .5:
                                        text "•" at delayed_blink(0.0, 1.0) style "skip_triangle" color '#000'
                                        text "•" at delayed_blink(0.2, 1.0) style "skip_triangle" color '#000'
                                        text "•" at delayed_blink(0.4, 1.0) style "skip_triangle" color '#000'
                                add Crop((0,   200, 320, 30), 'interface/chat.png')

                    else:
                        hbox:
                            vbox:
                                add Crop((0,   0,  320, 30), 'interface/chat.png') xzoom -1

                                $ cc = __(i)[4:].count('\n')
                                if not cc:
                                    $ cc = 1
                                viewport:
                                    xmaximum 320
                                    ymaximum 50
                                    add Frame(Crop((0,   40, 320, 100), 'interface/chat.png')) xzoom -1
                                    hbox xalign .5 yalign .5:
                                        text "•" at delayed_blink(0.0, 1.0) style "skip_triangle" color '#000'
                                        text "•" at delayed_blink(0.2, 1.0) style "skip_triangle" color '#000'
                                        text "•" at delayed_blink(0.4, 1.0) style "skip_triangle" color '#000'
                                add Crop((0,   200, 320, 30), 'interface/chat.png') xzoom -1
                            add 'interface/phone_interface/SMS_ava_'+phone_sms_screen[who][0].avatar+'.png'
            else:
                viewport:
                    ymaximum 20

    add 'phone_frame_bg'


screen phone_interface:
    zorder 20
    imagebutton:
        idle '#000a'
        hover '#000a'
        action Hide('phone_interface')
    imagebutton:
        idle 'interface/phone_interface/phone_main_bg.png'
        hover 'interface/phone_interface/phone_main_bg.png'
        action NullAction()
        focus_mask True


    hbox xalign .525 yalign .84:
        $ link = 'images/interface/phone_interface/phone_'
        spacing 10
        for i in ('char', 'internet', 'option', ('sms', [Show('phone_contacts_screen')])):
            imagebutton:
                if type(i) != type(()):
                    idle link+i+'.png'
                    hover link+i+'.png'
                    at ButtonEffect07
                    action Function(renpy.play, 'audio/mobile.ogg'), NullAction()

                else:
                    idle link+i[0]+'.png'
                    hover link+i[0]+'.png'
                    at ButtonEffect07
                    action Function(renpy.play, 'audio/mobile.ogg'), i[1]
    if get_sms_check():
        add 'warning_icon' yalign .85 xpos 1165
    add 'interface/phone_interface/phone_frame_bg.png'
    if store.test_debug_mod or store.patreon_cheats or getattr(store, 'jun_2024_dlc', False):
        use phone_cheats_patreon

screen sms_photo_full_screen(n_image='#000'):
    zorder 100
    imagebutton:
        idle '#0000'
        hover '#0000'
        action Hide('sms_photo_full_screen')
    add n_image xalign .5 yalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
