init 1 python:
    enough_money_game_var = 'pc'

screen pc_interface:
    imagebutton:
        idle '#0000'
        hover '#0000'
        action NullAction()
    add 'pc_bg'
    imagebutton xalign .93 ypos 130:
        idle 'pc_exit'
        hover 'pc_exit'
        xanchor .5
        yanchor .5
        at PulseButtonXzoom09
        action Return()
    viewport:
        maximum (130, 130)
        pos     (100, 140)
        image '#0000'
        imagebutton:
            idle 'pc_cards_icon'
            hover 'pc_cards_icon'
            anchor (.5, .5)
            align (.5, .4)
            at PulseButtonXzoom
            if money >= 300:
                action SetVariable('enough_money_game_var', 'pc'), Jump('enough_money_game')
            elif time.time_now == 'night':
                action Jump('bored_now_game')
            else:
                action Show('pc_game_interface', transition = Dissolve(.3))
        text _('Казино') outlines [(2, "#213c0f", 0, 0)] size 25 align (.5, 1.0)

    viewport:
        maximum (130, 130)
        pos     (100, 300)
        image '#0000'
        imagebutton:
            idle 'pc_bag_icon'
            hover 'pc_bag_icon'
            anchor (.5, .5)
            align (.5, .4)
            at PulseButtonXzoom
            action Jump('online_shop_label')
        text __('Магазин') outlines [(2, "#213c0f", 0, 0)] size 25 align (.5, 1.0)



    viewport:
        maximum (130, 130)
        pos     (100, 460) #pos     (100, 620)
        image '#0000'
        imagebutton:
            idle 'pc_porn_icon'
            hover 'pc_porn_icon'
            anchor (.5, .5)
            align (.5, .4)
            at PulseButtonXzoom
            action Jump('not_now_pc')
        text _('Порно') outlines [(2, "#213c0f", 0, 0)] size 25 align (.5, 1.0)

    $ _tmp_text = __('Купон «кекса»')
    viewport:
        maximum (150, 120)
        pos     (85, 610)
        image 'alpha_solid'
        imagebutton:
            idle 'pc_cam_icon'
            hover 'pc_cam_icon'
            anchor (.5, .5)
            align (.5, .4)
            at PulseButtonXzoom
            action Show('cards_screen', transition = Dissolve(.3))
        #text str(len(_tmp_text))
        text _tmp_text outlines [(2, "#213c0f", 0, 0)] size 18-max(len(_tmp_text)-15, 0) align (.5, 1.0)






screen pc_game_interface:
    add 'pc_game_bg'
    text '$' + str(money) xalign .5 ypos 120 font store.mini_game_font
    add 'pc_rules' xpos 100 ypos 200
    default info = None
    imagebutton xpos 270 ypos 240:


        idle Text(_('Правила'), font = store.mini_game_font)
        hover Text(_('Правила'), font = store.mini_game_font)

        yanchor .5
        xanchor .5
        unhovered SetScreenVariable('info', None)


        hovered SetScreenVariable('info', (__('Цель игры: Найти парные картинки и очистить игровую арену как можно быстрее.'),
__('Для этого следует открывать по две карты, щёлкая на каждую из них на игровом столе.'),
__('Если они окажутся одинаковыми, карты останутся открыты.'),
__('Финал: Когда все карты будут открыты, игра завершится.'),

__('Условия: Для начала игры вам необходима сумма, равная сумме за победу.'),
__('В случае проигрыша вы теряете сумму, указанную под уровнем сложности игры.')
))
        at PulseButtonXzoom09
        action NullAction()
    if info is not None:
        vbox xalign .5 yalign .85:
            for i in info:
                text '[i]' size 42 font store.mini_game_font xalign .5
    for i, j, v, t in ((40, .4, .5, 120), (70, .5, .5, 60), (120, .6, .49, 30)):
        $ img = 'pc_game_' + str(i)
        if money < i:
            $ img += '_red'
        imagebutton:
            xalign j
            yalign v
            idle img
            hover img
            xanchor .5
            yanchor .5
            at PulseButtonXzoom
            if money < i:
                action NullAction()
            else:
                action Function(jump_to_card_game, i = i, t = t)
    default _back_text = __('Назад')
    default _back_text_obj = Text(_back_text,  font = store.mini_game_font)
    default _back_text_obj_size = store.get_size(_back_text_obj)
   

    viewport xalign .95 yalign .092:
        ymaximum 90
        xmaximum 52+int(_back_text_obj_size[0])
        image 'alpha_solid'
        add 'pc_back'
        imagebutton xalign .99 yalign .5:

            idle _back_text_obj
            hover _back_text_obj
            yanchor .5
            at PulseButtonXzoom09
            action Hide('pc_game_interface', transition = Dissolve(.3))


init python:
    def jump_to_card_game(i, t):
        global money_win_game, time_need, nastroi
        store.ACH_5_count[2] = True

        Hide('pc_game_interface')() 
        Hide('pc_interface')()
        money_win_game = i
        time_need = t
        nastroi   = max(0,  nastroi-5)
        Jump('pre_card_game_label_1')()

label bored_now_game:

    $ Hide('pc_interface')()
    scene expression '#000'
    with Dissolve(.5)
    '[gg]' "Я слишком устал.. Нужно пойти поспать"
    jump gg_room_pc_black

label enough_money_game:
    $ Hide('pc_interface')()
    scene expression '#000'
    with Dissolve(.5)
    '[gg]' "У меня уже достаточно денег на мелкие расходы, я не собираюсь рисковать."
    if getattr(store, 'enough_money_game_var', 'pc') == 'pc':


        jump gg_room_pc_black
    elif True:
        jump main_interface_label

label wip_game:

    $ Hide('pc_interface')()
    scene expression '#000'
    with Dissolve(.5)
    '[gg]' "..."
    jump gg_room_pc_black


label not_now_pc:

    $ Hide('pc_interface')()

    scene expression 'cg/ep2/porn_site.png'
    with Dissolve(.5)
    menu:
        "1. Смотреть порно (+100 ед. Настроение, -2 Сытость)" if True:
            $ ACH_5_count[1] = True

            if getattr(store, 'block_nastroi', 0):

                '[gg]' "Сегодня я уже не буду этого делать."

                jump gg_room_pc_black

            $ block_nastroi = True

            if not hasattr(store, 'ACH_0_count'):
                $ ACH_0_count = 0

            $ ACH_0_count += 1
            if ACH_0_count >= 10:
                $ add_ach('ACH_0')


            $ nastroi  = min(100, nastroi+100)
            $ sitost   = max(0,   sitost-2)
            $ show_text_animation(_('+100 nastroi'))
            play audio 'audio/rest.ogg'

            "[gg]" "После продолжительного отдыха я начинаю чувствовать себя намного лучше."
            $ show_text_animation(_('-2 sitost'))
        "2. Не сейчас" if True:
            $ pass






    jump gg_room_pc_black


label online_shop_label:

    $ Show('online_shop', transition = Dissolve(.3))()
    call screen empty_screen

    jump gg_room_pc_black
init python:
    def set_final_trig(i):
        global final_trig
        if hasattr(store, 'final_trig') and type(final_trig) == type([]):
            final_trig[i] = 1
screen online_shop:
    imagebutton:
        idle '#000a'
        hover '#000a'
        action NullAction()
    add 'pc_shop'
    imagebutton xalign .93 ypos 130:
        idle 'pc_exit'
        hover 'pc_exit'
        xanchor .5
        yanchor .5
        at PulseButtonXzoom09
        if get_item('Красное вино', True) is not None:
            action Function(set_final_trig, i = 0), Hide('online_shop', transition = Dissolve(.5)), Jump('gg_room_pc_black')
        else:
            action Hide('online_shop', transition = Dissolve(.5)), Jump('gg_room_pc_black')



    default text_now = None
    add 'interface/Panel_Money.png' xalign .95 ypos 100+70
    text '$'+ str(money) xalign .85 color '#000' ypos 140+70

    text __('Онлайн') + ' ' + __('Магазин') size 70 xalign .5 ypos 130 outlines [(2, "#000", 0, 0)]

    vpgrid xpos 350 ypos 280:
        cols 5
        rows 2




        spacing 10
        for x in [('Купон «кекса»', 3000), ('Магические часы', 70), ('Бинокль', 100)] + getattr(store, 'add_items_for_web_shop', []) + getattr(store, 'add_items_for_web_shop_fixed', []):
            $ i = get_item(x[0])


            viewport:
                xmaximum 243
                ymaximum 228+100
                add '#0000'
                $ text_now = i.name






                viewport:
                    xmaximum 243
                    ymaximum 100
                    add '#0000'
                    text _(str(text_now)) xalign .5 yalign .5 size 30 outlines [(1, "#fff", 0, 0)]

                add 'pc_bag_one_item' ypos 100
                add Transform(i.image, zoom = .6) xpos 90 ypos 150
                imagebutton xpos 67 ypos 125:
                    xmaximum 115
                    ymaximum 115
                    if x[0] == 'Купон «кекса»':
                        if not getattr(store, 'cupon_buy_pc', False):
                            idle '#0000'
                            hover '#000a'
                            at ButtonEffect01

                            if money >= x[1]:

                                action SetVariable('cupon_buy_pc', True), Function(add_to_inventory, name = x[0], ncopy = True), SetVariable('money', money - x[1]), SetScreenVariable('text_now', None), Function(show_text_animation, str(x[1])+'$')
                            else:

                                action NullAction()
                        else:
                            idle '#000a'
                            hover '#000a'


                            action NullAction()
                    else:
                        if get_item(x[0], True) == None:
                            idle '#0000'
                            hover '#000a'
                            at ButtonEffect01

                            if money >= x[1]:

                                action Function(add_to_inventory, name = x[0]), SetVariable('money', money - x[1]), SetScreenVariable('text_now', None), Function(show_text_animation, str(x[1])+'$')
                            else:

                                action NullAction()
                        else:
                            idle '#000a'
                            hover '#000a'


                            action NullAction()
                viewport ypos 272:
                    xmaximum 243
                    ymaximum 50
                    add '#fff0'
                    if money >= x[1]:
                        text str(x[1])+'$' outlines [(2, "#0000", 0, 0)] xalign .5 yalign .5 color '#000'
                    else:
                        text str(x[1])+'$' outlines [(2, "#0000", 0, 0)] xalign .5 yalign .5 color '#f00'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
