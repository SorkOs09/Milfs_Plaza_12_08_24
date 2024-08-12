init -100 python:
    class Item():
        def __init__(self, name, discription, image, use, item_id = -999, max_quant = None):
            self.name        = name
            self.discription = discription
            self.image       = image 
            self.use         = use
            self.quant       = 1
            self.max_quant   = max_quant
            self.item_id     = item_id
        def set_quant(self, value):
            self.quant = min(value, self.max_quant or 999)

    def locker_use():
        Hide('bag_interface')()
        SetField(config, 'mouse', {"default":[ ("images/tests/locker_cursor.png", 1, 1) ] })()
        Show('lock_pick_screen', transition = Dissolve(.3))()

    def wine_use():
        Hide('bag_interface')()
        SetField(config, 'mouse', {"default":[ ("images/tests/locker_cursor.png", 1, 1) ] })()
        Show('lock_pick_screen', transition = Dissolve(.3))()


    def solar_oil_use():
        Hide('bag_interface')()
        SetField(config, 'mouse', {"default":[ ("images/tests/solar_oil_cursor.png", 1, 1) ] })()
        Show('solar_oil_pick_screen', transition = Dissolve(.3))()

    def lolita_use():
        Hide('bag_interface')()
        SetField(config, 'mouse', {"default":[ ("images/tests/locker_cursor.png", 1, 1) ] })()
        Show('lolita_pick_screen', transition = Dissolve(.3))()

    def tree_use_ep5():
        Hide('bag_interface')()
        SetField(config, 'mouse', {"default":[ ("images/tests/locker_cursor.png", 1, 1) ] })()
        Show('tree_screen_ep5', transition = Dissolve(.3))()

    def watering_can_use_ep5():
        Hide('bag_interface')()
        SetField(config, 'mouse', {"default":[ ("images/tests/locker_cursor.png", 1, 1) ] })()
        Show('watering_can_screen_ep5', transition = Dissolve(.3))()


    def binoculars_use():
        Hide('bag_interface')()
        SetField(config, 'mouse', {"default":[ ("images/tests/binoculars_cursor.png", 1, 1) ] })()
        Show('binoculars_pick_screen', transition = Dissolve(.3))()

    def eat_apple():
        
        eat_food(10, 'Яблоко')
        renpy.play("audio/eat.ogg")

    def eat_chocko():
        
        eat_food(30, 'Шоколад')
        renpy.play("audio/eat.ogg")



    def eat_yogurt():
        
        eat_food(30, 'Йогурт')
        renpy.play("audio/eat.ogg")

    def eat_juice():
        
        eat_food(10, 'Сок')
        renpy.play("audio/eat.ogg")



    def eat_chips():
        
        eat_food(20, 'Чипсы')
        renpy.play("audio/eat.ogg")



    def eat_food(sit, name = None):
        global sitost
        
        sitost = min(100, sitost+sit)
        
        show_text_animation(_('+'+str(sit)+' sitost'))
        
        remove_from_inventory(name)









    def add_to_inventory_by_id(id, ncopy = True):
        global all_items, inventory
        try:
            if ncopy:
                tmps = get_item_by_id(id, True)
                if tmps:
                    tmps.quant += 1
                else:
                    inventory.append(copy.deepcopy(get_item_by_id(id, False)))
            
            else:
                inventory.append(copy.deepcopy(get_item_by_id(id, False)))
        
        except:
            pass

    def item_set_quant(item, quant_value):
        if hasattr(item, 'set_quant'):
            item.set_quant(quant_value)
        else:
            item.quant = quant_value

    def add_to_inventory(name, ncopy = True, quant = 1):
        global all_items, inventory
        try:
            if ncopy:
                tmps = get_item(name, True)
                if tmps:
                    item_set_quant(tmps, tmps.quant+quant)

                else:
                    item = copy.deepcopy(get_item(name))
                    item_set_quant(item, quant)
                    inventory.append(item)

            else:
                
                inventory.append(get_item(name))
        
        except:
            pass

    def remove_from_inventory(name):
        global all_items, inventory
        try:
            tmps = get_item(name, True)
            if tmps:
                tmps.quant -= 1
            if tmps.quant <= 0:
                inventory.remove(tmps)
            if preferences.language in (None, 'eng', 'rus'):
                show_text_animation(__('Использован предмет: ') + __(tmps.name))
        except:
            pass


    def remove_from_inventory_by_id(item_id):
        global all_items, inventory
        try:
            tmps = get_item_by_id(item_id, True)
            if tmps:
                tmps.quant -= 1
            if tmps.quant <= 0:
                inventory.remove(tmps)
            if preferences.language in (None, 'eng', 'rus'):
                show_text_animation(__('Использован предмет: ') + __(tmps.name))
        except:
            pass

    def get_item(name, inventory_check = False, r_bool = False):
        global all_items, inventory
        if inventory_check:
            for i in inventory:
                if i:
                    if i.name == name:
                        if r_bool:
                            return True
                        else:
                            return i
        else:
            for i in all_items:
                if i:
                    if i.name == name:
                        if r_bool:
                            return True
                        else:
                            return i


    def get_item_by_id(item_id, inventory_check = False, r_bool = False):
        global all_items, inventory
        if inventory_check:
            for i in inventory:
                if getattr(i, 'item_id', -999) == item_id:
                    if r_bool:
                        return True
                    else:
                        return i
        else:
            for i in all_items:
                if getattr(i, 'item_id', -999) == item_id:
                    if r_bool:
                        return True
                    else:
                        return i







screen give_item_screen(item, name, discription):
    zorder 900
    default lng_check = preferences.language in ('eng', None, 'rus')
    
    if lng_check:
        add 'give_item_bg'
    
        add item xalign .51 yalign .37
        text _(name) size 40 xalign .5 yalign .47 outlines [(2, "#000", 0, 0)]
        viewport:
            xpos 678
            ypos 538
            xmaximum 590
            ymaximum 150

            add '#0000'
            if type(discription) == type([]):
                vbox xalign .5 yalign .5:
                    for i in discription:


                        text _(i) size 25 xalign .5

            else:
                text _(discription) size 25 xalign .5 yalign .5
    else:
        #image '#000a'
        add 'give_item_bg_2'
        add item xalign .51 yalign .4
        
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
