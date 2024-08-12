
transform info_panel_transform:

    xpos 1920 ypos 200
    linear .7 xpos 1920-320
    1.5
    linear .7 xpos 1920


transform text_animation_up(x_start, y_start, shift_y, ln=2):
    xpos x_start
    ypos y_start
    on show:
        linear ln xpos x_start ypos shift_y alpha 0.0

transform ButtonEffect00:
    on idle:
        easein 0.2 alpha 0.1
    on hover:
        easein 0.2 alpha .7

transform ButtonEffect001:
    on idle:
        easein 0.2 alpha 0.01
    on hover:
        easein 0.2 alpha .7


transform EventEffect:
    easein 0.2 alpha 1.0
    .25
    easein 0.2 alpha 0.0
    .25
    easein 0.2 alpha 1.0
    .25
    easein 0.2 alpha 0.0
    .25
    easein 0.2 alpha 1.0

    2
    repeat

transform NewEventEffect(x_start, y_start, tm=.2):
    xpos x_start ypos y_start
    easein tm ypos y_start-5
    easein tm ypos y_start
    easein tm ypos y_start-5
    easein tm ypos y_start

    2
    repeat

transform ButtonEffect01:
    
    alpha 0.1
    
    on idle:
        easein 0.2 alpha 0.1
    on hover:
        easein 0.2 alpha .7



transform ButtonEffect01_full:
    
    alpha 0.1
    
    on idle:
        easein 0.2 alpha 0.1
    on hover:
        easein 0.2 alpha 1.0
transform hehe_transform(yp=1085):
    easein .1 ypos yp
    easein .1 ypos yp-5
    easein .1 ypos yp
    easein .1 ypos yp-5
    easein .1 ypos yp
    easein .1 ypos yp-5
    easein .1 ypos yp
    easein .1 ypos yp-5
transform go_from_right(xxzoom=1.0, xxalign=.85, ttimer=1.0, yyzoom=1.0, xxalign_start = 1.5):
    xalign xxalign_start
    xzoom xxzoom
    yzoom yyzoom
    ypos 1085

    pause .1
    easein_cubic ttimer xalign xxalign

transform go_from_left(xxzoom=1.0, xxalign=.15, ttimer=1.0, minus_zoom=0.035, yyzoom=1.0, xxalign_start = -0.5):
    xalign xxalign_start
    xzoom xxzoom
    yzoom yyzoom
    ypos 1085

    pause .1
    easein_cubic ttimer xalign xxalign

transform show_hide_screen():
    on hide:
        alpha 1.0
        linear .3 alpha 0
    on show:

        alpha .0
        linear .3 alpha 1.0


transform PulseButtonXzoom09:
    on hover:
        easein .25 zoom 1.0
    on idle:

        easein .25 zoom .9


transform PulseButtonXzoom09Alpha:
    on hover:
        easein .25 zoom 1.0 alpha 1.0
    on idle:

        easein .25 zoom .9 alpha .75


transform PulseButtonXzoom:
    on hover:
        easein .25 zoom 1.1
    on idle:

        easein .25 zoom 1.0


transform PulseButton:
    on hover:
        easein .25 zoom 1.05
    on idle:

        easein .25 zoom 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
