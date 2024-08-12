transform circle_mini_game_transform(tm):
    linear tm zoom 0

transform circle_attention_transform(zm):
    block:
        zoom zm*.9
        pause .2
        easeout .25 zoom zm
        easein .25 zoom zm*.8
        easeout .25 zoom zm
        easein .25 zoom zm*.9
        pause 1.0
        repeat
screen circle_mini_game_screen(xp=0, yp=0, tm=10):
    imagebutton:
        xpos xp
        ypos yp
        idle 'circle_mini_game'
        hover 'circle_mini_game'
        xanchor .5
        yanchor .5
        focus_mask None
        at circle_mini_game_transform(tm)
        action Return(1)

    timer tm action Return(0)


screen circle_attention_screen(xp=0, yp=0, zm=1.0):
    imagebutton:
        xpos xp
        ypos yp
        idle 'circle_mini_game'
        hover 'circle_mini_game'
        xanchor .5
        yanchor .5
        focus_mask None
        at circle_attention_transform(zm)
        action Return(1)

   # timer tm action Return(0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
