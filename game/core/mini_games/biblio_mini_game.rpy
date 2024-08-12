
transform biblio_search_book_shake(y=100):
    easein_cubic 0.1 ypos y
    easein_cubic 0.1 ypos y-4
    easein_cubic 0.1 ypos y
    easein_cubic 0.1 ypos y-4
    easein_cubic 0.1 ypos y
    easein_cubic 0.1 ypos y-4
    easein_cubic 0.1 ypos y

transform biblio_search_book_arrow_transform(pos_finish=1650):
    yalign .5
    easein .5 xpos pos_finish

    # on idle:
    #     easein .5 yalign .5 xpos 1650
    # on hover:
    #     easein .5 yalign .5 xpos 1720

init -100 python:
    def _add_book_to_inventory(book_dict):

        if not hasattr(store, '_ttdd_ll'):
            store._ttdd_ll = [None, None, None]

        if book_dict in store._ttdd_ll: 
            return

        
        if store._ttdd_ll[0] is None:

            book_x = 0
        
        elif store._ttdd_ll[1] is None:

            book_x = 1

        elif store._ttdd_ll[2] is None:

            book_x = 2

        else:
            renpy.show( 
            'biblio_search_book_inventory', what = Image('mini_games/biblio/books_search/inventory.png'), 
            
            at_list=[
            biblio_search_book_shake(
            
                 y = 700,

                         )
            
            ])

            return






        x = 847

        x += 112*book_x

        store._ttdd_ll[book_x] = book_dict



        book_number = book_dict['book']
        

        img = Image('mini_games/biblio/books_search/'+str(book_number)+'.png')

        renpy.show('biblio_search_book_'+str(book_number), at_list = [Transform(pos=(2200, 100))])

        renpy.show( 
            'biblio_search_book_inv_'+str(book_number)+'_shadow_1', what = img, 
            at_list=[
                ])
        renpy.show( 
            'biblio_search_book_inv_'+str(book_number)+'_shadow_1', what = img, 
            at_list=[
                Transform(pos=book_dict['pos'])
                ])

        renpy.show( 
            'biblio_search_book_inv_'+str(book_number)+'_shadow_2', what = img, 
            at_list=[
                ])
        renpy.show( 
            'biblio_search_book_inv_'+str(book_number)+'_shadow_2', what = img, 
            at_list=[
                Transform(pos=book_dict['pos'])
                ])

        renpy.show( 
            'biblio_search_book_inv_'+str(book_number), what = img, 
            at_list=[
                ])
        renpy.show( 
            'biblio_search_book_inv_'+str(book_number), what = img, 
            at_list=[
                Transform(pos=book_dict['pos'])
                ])



        renpy.show('biblio_search_book_inv_'+str(book_number)+'_shadow_1', what = Transform(img, alpha = .8), at_list=[
            
            #(765+75+7, 935)
            final_act_7_action_arrow_transform(
                     pos_finish=(x, 935),
                     dur = .8, 
                     rot = 0.0,
                     alpha_finish = 1.0,
                     )
                ] )



        renpy.show('biblio_search_book_inv_'+str(book_number)+'_shadow_2', what = Transform(img, alpha = .5), at_list=[
            
            #(765+75+7, 935)
            final_act_7_action_arrow_transform(
                     pos_finish=(x, 935),
                     dur = 1.0, 
                     rot = 0.0,
                     alpha_finish = 1.0,
                     )
                ] )
        

        renpy.show('biblio_search_book_inv_'+str(book_number), what = img, at_list=[
            
            #(765+75+7, 935)
            final_act_7_action_arrow_transform(
                     pos_finish=(x, 935),
                     dur = .6, 
                     rot = 0.0,
                     alpha_finish = 1.0,
                     )
                ] )

screen biblio_search_book_timer_screen:




    timer 1 repeat True action SetVariable('biblio_search_book_time_line', biblio_search_book_time_line-.01)

    $ x_biblio_search_book_time_line = int(850 * biblio_search_book_time_line)
    $ x_biblio_search_book_time_line_start = 1100-x_biblio_search_book_time_line-150



    # viewport:
    #     maximum(175, 300)
    #     yalign .5 xpos 1650
    #     imagebutton:
    #         idle  '#fffa'
    #         hover '#fffa'
    #         hovered Function(renpy.show, 
    #             'biblio_search_book_arrow', what = Image('mini_games/biblio/books_search/arrow.png'), 
    #             at_list=[
    #             biblio_search_book_arrow_transform(
    #                  pos_finish=1700
    #                  )
    #             ])
    #         unhovered Function(renpy.show, 
    #             'biblio_search_book_arrow', what = Image('mini_games/biblio/books_search/arrow.png'), 
    #             at_list=[
    #             biblio_search_book_arrow_transform(
    #                  pos_finish=1650
    #                  )
    #             ])
    #         action Jump('biblio_mini_games_test_books')
    viewport:
        maximum (1100, 250)
        align   (.5, 1.0)
        image 'mini_games/biblio/books_search/time_line/idle.png'
        image Crop((x_biblio_search_book_time_line_start, 0, 1100, 250), 'mini_games/biblio/books_search/time_line/hover.png'):
            xpos x_biblio_search_book_time_line_start
        viewport:
            maximum(140, 140)
            image '#fff0'
            pos (890, 62)
            if biblio_search_book_time_line > .3:
                image 'mini_games/biblio/books_search/time_line/happy.png':
                    align (.5, .5)
            else:
                image 'mini_games/biblio/books_search/time_line/sad.png':
                    align (.5, .5)
    # vbox:
    #     textbutton '-' action SetVariable('biblio_search_book_time_line', biblio_search_book_time_line-.1)
    #     textbutton '+' action SetVariable('biblio_search_book_time_line', biblio_search_book_time_line+.1)
    #     text str(biblio_search_book_time_line)
transform easein_back_transform(dur, ypos_finish):
    easein_back dur ypos ypos_finish

label biblio_mini_games_test_start:
    $ biblio_search_book_time_line = .55
    
    call biblio_mini_games_test_create_books_list from _call_biblio_mini_games_test_create_books_list
    jump biblio_mini_games_test

label biblio_mini_games_test_create_books_list:
    python:
        _t = range(1, 21)
        _r = [(20, 280),
            (380, 300),
            (1060, 218),
            (1250, 280),
            (525, 260),
            (640, 237),]
        renpy.random.shuffle(_t)
        renpy.random.shuffle(_r)
        biblio_mini_games_books_need = []
        for i in range(3):
            biblio_mini_games_books_need.append({'book':_t[0], 'pos':_r[0]})
            _t.pop(0)
            _r.pop(0)



    return

label biblio_mini_games_end:
    python:
        try:
            del _t
        except:
            pass



        try:
            del _r
        except:
            pass
        try:
            del _pos
        except:
            pass

        try:
            del _img
        except:
            pass

    return

label biblio_mini_games_test:
    call final_act_blind_transition_to_black_fast_label from _call_final_act_blind_transition_to_black_fast_label
    python:
        for i in range(1, 20):
            n = (19-i)*102
            j = Crop((n, 0, 102, 1080), 'mini_games/biblio/books_search/bg.png')
            

            dur = .2+i*.1,
            renpy.show('books_search_bg_2_'+str(i), what = j, 
                at_list=[
                final_act_4_blinds_transform(
                    xp  = n+102,
                    dur = .25+i*.015,
                    xp_fin = n,
                    )
                ])
        renpy.pause(0.3, hard = True)
    scene image 'mini_games/biblio/books_search/bg.png'

    show  image 'mini_games/biblio/books_search/green_shadow.png'
    python:
        j = 1
        for i in biblio_mini_games_books_need:
            _pos = i['pos']
            _img = LiveComposite(
                (150, 180),
                (0, 0), 'mini_games/biblio/books_search/frame.png',
                (0, 0), Image('mini_games/biblio/books_search/'+str(i['book'])+'.png'),
                )
            renpy.show( 
            'biblio_search_book_'+str(j), what = _img, 
            at_list=[
            Transform(
                     pos   = (_pos[0], _pos[1]+50),
                     alpha = .0,
                     )
                ])


            renpy.show( 
            'biblio_search_book_'+str(j), what = _img, 
            at_list=[
            final_act_7_action_arrow_transform(
                     pos_finish=_pos,
                     dur = .15, 
                     rot = 0.0,
                     alpha_finish = 1.0,
                     )
                ])
            j += 1




    $ renpy.show( 
        'biblio_search_book_arrow_button', what = ImageButton(
    idle_image  = 'alpha_solid', 
    hover_image = 'alpha_solid', 
    hovered     = Function(renpy.show, 
        'biblio_search_book_arrow', what = Image('mini_games/biblio/books_search/arrow.png'), 
        at_list=[
        biblio_search_book_arrow_transform(
             pos_finish=1700
             )
        ]),
    unhovered = Function(renpy.show, 
    'biblio_search_book_arrow', what = Image('mini_games/biblio/books_search/arrow.png'), 
    at_list=[
    biblio_search_book_arrow_transform(
         pos_finish=1650
         )
    ]),
    clicked    = Jump('biblio_mini_games_test_books'),
    focus_mask = None,
    ),

        at_list=[
        Transform(
            size   = (175, 300),
            yalign = .5, 
            xpos   = 1650,
            ),
        ])


    
    $ renpy.show( 
        'biblio_search_book_arrow', what = Image('mini_games/biblio/books_search/arrow.png'), 
        at_list=[
        Transform(xpos = 1650, yalign = .5),
        ])
    show screen biblio_search_book_timer_screen

    with my_dissolve
    $ renpy.game.log.block()
    call screen empty_screen

label biblio_mini_games_test_books:
    call final_act_blind_transition_to_black_fast_label from _call_final_act_blind_transition_to_black_fast_label_1
    python:
        for i in range(1, 20):
            n = (19-i)*102
            j = Crop((n, 0, 102, 1080), 'mini_games/biblio/books_search/bg_2.png')
            

            dur = .2+i*.1,
            renpy.show('books_search_bg_2_'+str(i), what = j, 
                at_list=[
                final_act_4_blinds_transform(
                    xp  = n+102,
                    dur = .25+i*.015,
                    xp_fin = n,
                    )
                ])
        renpy.pause(0.3, hard = True)
    scene image 'mini_games/biblio/books_search/bg_2.png'
    show  image 'mini_games/biblio/books_search/green_shadow.png'
    with my_dissolve

    python:

        renpy.show( 
            'biblio_search_book_inventory', what = Image('mini_games/biblio/books_search/inventory.png'), 
            at_list=[
            Transform(xalign = .5, ypos = 1100),
            ])

        renpy.show( 
            'biblio_search_book_inventory', what = Image('mini_games/biblio/books_search/inventory.png'), 
            at_list=[
            easein_back_transform(
                 dur = .7,
                 ypos_finish=700,
                         )
            ])
        renpy.pause(.2, hard = True)
        _t = range(1, 21)
        _r = [
            (300, 965),
            (150, 350),
            (300, 440),
            (150, 565),
            (250, 765),

            (645, 240),
            (680, 510),
            (645, 780),

            (1070, 260),
            (1080, 550),
            (1100, 730),


            (1660, 965),
            (1850, 350),
            (1630, 440),
            (1810, 565),
            (1640, 765),

            ]
        renpy.random.shuffle(_t)
        renpy.random.shuffle(_r)
        biblio_mini_games_books = []
        for i in range(len(_r)):
            biblio_mini_games_books.append({'book':_t[0], 'pos':_r[0]})
            _t.pop(0)
            _r.pop(0)

        j = 1
        for i in biblio_mini_games_books:
            _pos = i['pos']
            _book_number = i['book']
            _img = 'mini_games/biblio/books_search/frame.png'
            if _pos[0] > 1000:
                _img = Transform(_img, xzoom = -1.0)
            
            _idle = LiveComposite(
                (150, 180),
                (0, 0), _img,
                (0, 0), 'mini_games/biblio/books_search/'+str(i['book'])+'.png',
                )

            _hover = LiveComposite(
                (150, 180),
                
                (0, 0), _img,
                
                (-4, -3), 
                    Transform(
                        
                        im.MatrixColor('mini_games/biblio/books_search/'+str(i['book'])+'.png', im.matrix.brightness(.1)), 
                        zoom = 1.05

                    ),
                
                )

            _img = ImageButton(
        idle_image  = _idle, 
        hover_image = _hover, 

        clicked    = Function(_add_book_to_inventory, i),
        focus_mask = True,
        )

            renpy.show( 
            'biblio_search_book_'+str(_book_number), what = _img, 
            at_list=[
                ])


            renpy.show( 
            'biblio_search_book_'+str(_book_number), what = _img, 
            at_list=[
            Transform(
                     pos   = (_pos[0], _pos[1]+50),
                     alpha = .0,
                     )
                ])

            renpy.show( 
            'biblio_search_book_'+str(_book_number), what = _img, 
            at_list=[
            final_act_7_action_arrow_transform(
                     pos_finish=_pos,
                     dur = .35, 
                     rot = 0.0,
                     alpha_finish = 1.0,
                     )
                ])
            j += 1


        try:
            del _book_number
        except:
            pass



    show screen biblio_search_book_timer_screen
    show screen biblio_search_book_inventory_screen
    with my_dissolve

    $ renpy.game.log.block()
    call screen empty_screen

call screen empty_scree

#label biblio_mini_games_add_book_to_inventory:

screen biblio_search_book_inventory_screen:
    if hasattr(store, '_ttdd_ll'):
        for i in range(3):
            $ _book = store._ttdd_ll[i]
            if _book is not None:

                
                imagebutton:
                    pos     (800+110*i+3*(i==2), 743)
                    maximum (96, 130)
                    idle    'alpha_solid'
                    hover   'red_solid'
                    action  NullAction()
