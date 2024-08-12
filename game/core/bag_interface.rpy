
screen bag_interface():
    zorder 850
    imagebutton:
        idle '#000a'
        hover '#000a'
        action Hide('bag_interface')

    add i_path+'Inventory.png' xalign .5 yalign .5
    add i_path+'Grid.png' xalign .5 yalign .5
    default text_now_0 = None
    default text_now_1 = None
    vpgrid xpos 410 ypos 319:
        cols 8
        rows 20





        for i in inventory:
            if i:
                viewport:
                    xmaximum 136
                    ymaximum 140
                    add '#0000'
                    add i.image xpos 15 ypos 25


                    imagebutton xpos 15 ypos 25:
                        xmaximum 115
                        ymaximum 115

                        idle '#0000'
                        hover '#000a'
                        at ButtonEffect01
                        hovered SetScreenVariable('text_now_0', i.discription), SetScreenVariable('text_now_1', i.name)
                        unhovered SetScreenVariable('text_now_0', None), SetScreenVariable('text_now_1', None)
                        if type(i.use) == type([1,]):
                            action i.use
                        else:
                            action Function(i.use)






                    $ j = getattr(i, 'max_quant', None)
                    if i.quant > 1 or j:
                        hbox:
                            xalign .98 yalign .995
                            text str(i.quant) outlines [(3, "#000", 0, 0)] size 23 

                            if j:
                                text '/'  outlines [(3, "#000", 0, 0)] size 25 
                                text str(i.max_quant) outlines [(3, "#000", 0, 0)] size 23 
   

    use item_name_table(text_now_0, text_now_1)
    
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
