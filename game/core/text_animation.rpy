




screen text_animation(text_now, x_now, y_now):
    zorder 1000
    if type(text_now) in (tuple, list):
        default ntfont = gui.text_font

        default noutlines = [(7, "#000", 0, 0)]
        default ncolor = '#FFF'
        
        vbox:
            for i in text_now:
                text str(i):
                    color ncolor
                    font ntfont
                    italic True
                    outlines noutlines
                    xalign .5
                    size 36
                
            at text_animation_up(x_now, y_now, y_now-200, ln = 3.5)
            timer 4 action Hide('text_animation')


    else:

        if '$' in text_now:
            default ntfont = "fonts/ARMB.ttf"
        else:
            default ntfont = gui.text_font

        if '+' in text_now:
            default noutlines = [(3, "#000", 0, 0)]
            default ncolor = '#0F0'

        elif '-' in text_now:
            default noutlines = [(7, "#000", 0, 0)]
            default ncolor = '#F00'
        else:
            default noutlines = [(7, "#000", 0, 0)]
            default ncolor = '#FFF'

        text str(text_now):
            color ncolor
            if preferences.language in ('chinese_trad', 'chinese_simpl', 'kor', 'jap'):
                font gui.text_font
            else:                
                font ntfont
            italic True
            outlines noutlines
            size 36
            at text_animation_up(x_now, y_now, y_now-100)

        timer 2 action Hide('text_animation')






screen info_panel(ttext='-5', iimage='info_panel_sitost'):
    zorder 1000
    viewport:
        at info_panel_transform

        xmaximum 320
        ymaximum 167
        add 'info_panel_bg'
        viewport:
            ypos 25
            xpos 10
            xmaximum 120
            ymaximum 120
            add '#0000'
            add iimage xalign .5 yalign .5

        viewport:
            ypos 55
            xpos 115
            xmaximum 205
            ymaximum 62
            add '#0000'

            text str(ttext):
                xalign .5
                yalign .5
                if '-' in str(ttext):
                    color '#F00'
                else:
                    color '#0F08'
                size 50
                bold True
                outlines [(2, "#000", 0, 0),]





init -1500 python:
    def check_words(words, string):
        for word in words:
            i

    def show_text_animation(text):
        global relations_milf
        def check_info_panel_0(text):
            
            for i in ('gigiena', 'sitost', 'prison', 'nastroi', 'milf',):
                if i in text:
                    return i

        def check_info_panel_1(text):
            if 'money' in text:
                return 'money'

        
        Hide('text_animation')()
        Hide('info_panel')()
        if getattr(store, 'not_survival', False) and check_info_panel_0(text):
            return None
        elif check_info_panel_0(text) or check_info_panel_1(text):
            ttext   = text.lower().split(' ')[0]
            ttpanel = text.lower().split(' ')[1]
            iimage  = 'info_panel_' + ttpanel
            if ttpanel.lower() == 'milf':
                
                if hasattr(store, 'relations_milf'):
                    
                    relations_milf += int(ttext)

            Show('info_panel', ttext = ttext, iimage = iimage)()
        
        
        
        
        else:
            if type(text) not in (tuple, list):
                text = str(text)
            mouse_pos = renpy.get_mouse_pos()

            Hide('text_animation')()
            _xp = mouse_pos[0]-20
            if _xp >= 1850:
                _xp -= 200
            Show(
       'text_animation', 
       text_now = text,
       x_now = _xp, 
       y_now = mouse_pos[1]-50)()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
