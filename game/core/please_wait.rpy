

label my_load_label:



    call screen predict_load_screen(images_load_now, percent_load_now)

    return


screen broken_save():
    zorder 2000
    imagebutton:
        idle '#000'
        hover '#000'
        action Return()
    vbox:
        xalign .5 yalign .5
        if mp.language == 'ENG':
            text "Sorry, this save file is not available in this version of the game because we have reworked a lot of the game content." xalign .5
            text "Please start the game from the beginning." xalign .5

        else:
            text "Извините, этот файл сохранения не доступен в этой версии игры, потому что мы переделали большую часть контента." xalign .5
            text "Пожалуйста, начните игру с начала." xalign .5



screen please_wait_screen(tmr=False, prcnt='0%'):
    zorder 1000
    viewport:
        xmaximum 1920
        ymaximum 1080
        imagebutton:
            idle '#000'
            hover '#000'
            action Return()
        add 'loading_bg'
        add Crop((0, 0, int(float(prcnt[:-1])/100*845), 40), 'interface/load_bar.png') ypos 571 xpos 530
        text 'Loading, please wait... ' + prcnt xalign .5 yalign .5



screen please_wait_screen_tmp():

    timer .05 action Return()


screen predict_load_screen(images_list=[], prcnt='0%'):
    zorder 900

    for i in images_list:
        if i in renpy.list_files():
            add i
            add i
            imagebutton:
                idle i
                hover im.MatrixColor(i, im.matrix.brightness(.3))
                focus_mask True
                at ButtonEffect01
                action NullAction()

    use please_wait_screen(prcnt=prcnt)

    timer .5 action Return()


image please_wait black = Solid('#000')

image please_wait 5_per = "images/please_wait_5_per.png"

image please_wait 100_per = "images/please_wait_100_per.png"

translate eng strings:

    old "Предзагрузка данных"
    new "Preloading data"

    old "При смене параметра игра будет перезапущена."
    new "If you change the parameter, the game will restart."

    old "Включить"
    new "On"

    old "Выключить"
    new "Off"

    old "В Milf's Plaza доступен режим предзагрузки данных."
    new "Milf's Plaza has a 'preload data mode'."

    old "Когда этот режим включен вы будете видеть короткое окно загрузки при каждом запуске игры и при загрузке сохранений, а также игра будет занимать больше оперативной памяти ({i}1.5-2{/i} гигабайта), но благодаря этому она не будет тормозить при встрече новых изображений."
    new "When this mode is enabled, you will see a short loading window every time when you start the game and when loading saves, and the game will take more RAM ({i}1.5-2{/i} gigabytes). But thanks to this - game will not freeze when you will meeting new images."

    old "Когда этот режим выключен игра и сохранения будут запускаться моментально, а оперативная память будет занята по минимуму, но когда на экране будут появлятся изображения которые вы не видели до этого - будет происходить небольшой фриз для загрузки данных в память."
    new "When this mode is turned off the game and save will run instantly, and the RAM will be occupied to a minimum, but when the screen will appear images that you have not seen before - there will be a small freeze to load data into memory."

    old "Вы в любой момент можете поменять этот параметр в настройках."
    new "You can change this parameter in the settings at any time."

    old "Включить предзагрузку"
    new "Enable preloading"

    old " (Игра будет перезагружена)"
    new " (Game will be restart)"

    old "Не включать предзагрузку"
    new "Disable preloading"




init python:
    def change_skip_loading(i, restart = True):
        global mp
        mp.skip_loading = i
        mp.save()
        if restart:
            mp.need_full_load = True
            mp.save()
            renpy.reload_script()
screen preload_data_info:
    zorder 1000
    add '#000b'

    default text_now = None
    viewport:
        xmaximum 1485
        ymaximum 730
        add 'big_frame.png' xalign .5 yalign .5
        xalign .5 yalign .2
        viewport:
            xmaximum 1400
            ymaximum 700
            xalign .5
            yalign .5
            add '#0000'
            vbox:
                xalign .5 yalign .5

                text __("В Milf's Plaza доступен режим предзагрузки данных.") xalign .5
                text "------" xalign .5
                text __("Когда этот режим включен вы будете видеть короткое окно загрузки при каждом запуске игры и при загрузке сохранений, а также игра будет занимать больше оперативной памяти ({i}1.5-2{/i} гигабайта), но благодаря этому она не будет тормозить при встрече новых изображений.") xalign .5
                text "------" xalign .5
                text __("Когда этот режим выключен игра и сохранения будут запускаться моментально, а оперативная память будет занята по минимуму, но когда на экране будут появлятся изображения которые вы не видели до этого - будет происходить небольшой фриз для загрузки данных в память.") xalign .5
                text "------" xalign .5
                text __("Вы в любой момент можете поменять этот параметр в настройках.") xalign .5

    hbox:
        spacing 100
        xalign .5 yalign .85
        for i in (False, True):
            viewport:
                xmaximum 650
                ymaximum 55
                add '#0000'
                imagebutton:
                    idle "interface/comic_frame_blue.png"
                    hover im.MatrixColor("interface/comic_frame_blue.png", im.matrix.brightness(.3))
                    action Function(change_skip_loading, i, False), Return(i)
                if i:
                    hbox:
                        text __("Включить предзагрузку") size 30 yalign .5
                        text __(" (Игра будет перезагружена)") size 20 ypos 10
                        xalign .5 yalign .5
                else:
                    text __("Не включать предзагрузку") size 30 xalign .5 yalign .5









label please_wait_for_splashscreen:




    if mp.skip_loading is True:

        return

    show please_wait black with Dissolve(.15)

    $ renpy.pause(.17, hard = True)

    show please_wait 5_per with Dissolve(.3)

    $ renpy.pause(.35, hard = True)





    $ renpy.pause(.2, hard = True)

    $ percent_load_now = '15%'

    $ images_load_now  = [

# 'images/locations/bg/Hall/night.png',
# 'images/locations/bg/Hall/morning.png',
# 'images/locations/bg/Hall/evening.png',
# 'images/locations/bg/Hall/afternoon.png',

# 'images/cg/window_event/woman_2.png',
# 'images/cg/window_event/night.png',
# 'images/cg/window_event/evening.png',
# 'images/locations/imagebuttons/GG_Room/bita.png',
# 'images/locations/imagebuttons/GG_Room/pants.png',
# 'images/locations/imagebuttons/City_Park/search_game_icon.png',
# 'images/locations/imagebuttons/Restroom/hair_pin.png',

    ]

    call my_load_label from _call_my_load_label_11


    $ percent_load_now = '30%'

    $ images_load_now  = [
#     'images/interface/Grid.png',
# 'images/interface/profile.png',
# 'images/interface/Icon_Quest.png',
# 'images/interface/loading_bg.png',
# 'images/interface/back_button_hover.png',
# 'images/interface/error_background.png',
# 'images/interface/Time_Evening.png',
# 'images/interface/Icon_Mobile.png',
# 'images/interface/back_button.png',
# 'images/interface/Icon_Map.png',


# 'images/cg/gg_activities/cg_surv_gg_dush.png',
# 'images/cg/gg_activities/gg_clothes_restroom.png',
# 'images/cg/gg_activities/gg_wash_kitchen.png',
# 'images/cg/gg_activities/gg_clothes_restroom_nude.png',
# 'images/cg/gg_activities/cg_surv_gg_tv.png',
# 'images/cg/gg_activities/active_cinema_cg.png',
# 'images/cg/gg_activities/cg_surv_gg_game.png',
# 'images/cg/gg_activities/gg_clean_hall.png',
# 'images/cg/gg_activities/cg_surv_gg_vanna.png',
# 'images/cg/gg_activities/cg_surv_gg_eat.png',

    ]

    call my_load_label from _call_my_load_label

    $ percent_load_now = '50%'

    $ images_load_now  = [
# 'images/characters/GG/emo/Pancu_1.png',
# 'images/characters/GG/emo/Passion.png',
# 'images/characters/GG/emo/Blin.png',
# 'images/characters/GG/emo/Blin_embr.png',
# 'images/characters/GG/emo/Laughs.png',
# 'images/characters/GG/emo/Bita_Normal.png',
# 'images/characters/GG/emo/GivePhone.png',
# 'images/characters/GG/emo/Blin_dick.png',
# 'images/characters/GG/emo/Smile.png',
# 'images/characters/GG/emo/Skepticism.png',
# 'images/characters/GG/emo/Embarrassment.png',
# 'images/characters/GG/emo/Nude_Normal.png',
# 'images/characters/GG/emo/Flower.png',
# 'images/characters/GG/emo/Dick 2.png',
# 'images/characters/GG/emo/Think.png',
# 'images/characters/Milf/EMO/Pussy.png',
# 'images/characters/Milf/EMO/Street_Silence.png',
# 'images/characters/Milf/EMO/Polu_2.png',
# 'images/characters/Milf/EMO/Night_Normal.png',
# 'images/characters/Milf/1POSES/Blin.png',



    ]

    call my_load_label from _call_my_load_label_12


    $ percent_load_now = '85%'

    $ images_load_now  = [

# 'images/characters/GG/emo/Costume_Please.png',
# 'images/characters/GG/emo/Costume_Embarrassment.png',
# 'images/characters/GG/emo/Costume_Passion.png',

# 'images/characters/Igor/EMO/Spec_Normal_1.png',
# 'images/characters/Igor/EMO/Angry.png',
# 'images/characters/Igor/EMO/Agr.png',
# 'images/characters/Igor/EMO/Normal.png',
# 'images/characters/Igor/EMO/Ok.png',
# 'images/characters/Igor/EMO/Spec_Normal_2.png',
# 'images/characters/Igor/EMO/Bad.png',
# 'images/characters/Jay/EMO/Silence.png',
# 'images/characters/Jay/EMO/OMG.png',
# 'images/characters/Jay/EMO/Normal.png',
# 'images/characters/Jay/EMO/Mobile.png',
# 'images/characters/Milf/EMO/LOL.png',
# 'images/characters/Milf/EMO/Night_Passion.png',
# 'images/characters/Milf/EMO/Dress_Normal.png',
# 'images/characters/Milf/EMO/Street_Sad.png',
# 'images/characters/Milf/EMO/Passion.png',
# 'images/characters/Milf/EMO/Dress_Passion.png',
# 'images/characters/Milf/EMO/Dress_Chagrin.png',
# 'images/characters/Milf/EMO/Laughs.png',
# 'images/characters/Milf/EMO/Dress_Pose_3.png',


    ]

    call my_load_label from _call_my_load_label_13



    $ percent_load_now = '100%'

    $ images_load_now = [

# 'images/interface/click_here_button.png',
# 'images/interface/Button_No.png',
# 'images/interface/gradient_up.png',
# 'images/interface/Time_Morning.png',
# 'images/interface/heart_icon.png',
# 'images/interface/Inventory.png',
# 'images/interface/Icon_Bag.png',
# 'images/interface/give_item_bg.png',
# 'images/interface/Button_Yes.png',

# 'images/locations/imagebuttons/Kitchen/solar_oil.png',
# 'images/locations/imagebuttons/City_Home/Door.png',
# 'images/locations/imagebuttons/Milf_Room/phone_underpants_table.png',
# 'images/locations/imagebuttons/City_Shop/jay_bob.png',
# 'images/locations/imagebuttons/City_Shop/door.png',
# 'images/locations/buttons/Restroom_hover_1.png',
# 'images/locations/buttons/Hall_hover_0.png',
# 'images/locations/buttons/GG_Room_hover_1.png',
# 'images/locations/buttons/Corridor_hover_0.png',
# 'images/locations/buttons/Restroom_hover_0.png',
# 'images/locations/buttons/Hall_hover_1.png',
# 'images/locations/buttons/Milf_Room_hover_0.png',
# 'images/locations/buttons/kitchen_hover_0.png',
# 'images/locations/buttons/GG_Room_hover_0.png',


    ]




    show please_wait 100_per
    call my_load_label from _call_my_load_label_1

    hide please_wait
    hide screen please_wait_screen
    hide screen predict_load_screen
    hide screen please_wait_screen_tmp
    hide screen broken_save

    with Dissolve(.5)
    return

label please_wait_for_load:
    if mp.skip_loading is None:
        show expression '#000a'
        with Dissolve(.25)
        $ renpy.pause(.5, hard = True)
        $ i = renpy.call_screen('preload_data_info')

        if i:
            $ mp.need_full_load = True
            $ mp.save()
            $ renpy.reload_script()



    if mp.skip_loading is True:
        return
    show please_wait black with Dissolve(.15)

    $ renpy.pause(.17, hard = True)

    show please_wait 5_per with Dissolve(.3)

    $ renpy.pause(.35, hard = True)






    $ percent_load_now = '15%'


    $ images_load_now = [

# 'images/interface/Quest_Text.png',
# 'images/interface/Warning.png',
# 'images/interface/Time_Night.png',
# 'images/interface/chat.png',
# 'images/interface/message_line.png',
# 'images/interface/Quest_Menu.png',
# 'images/interface/pause_icon.png',
# 'images/interface/Panel_Money.png',
# 'images/interface/city_interface/city_park_button.png',
# 'images/interface/city_interface/city_bg_afternoon.png',
# 'images/interface/city_interface/city_bg_night.png',
# 'images/interface/city_interface/city_clothes_shop_button.png',
# 'images/interface/city_interface/city_home_button.png',
# 'images/interface/city_interface/city_bg_morning.png',
# 'images/interface/city_interface/city_shop_button.png',
# 'images/interface/city_interface/city_bg_evening.png',
# 'images/interface/city_interface/city_restaurant_button.png',
# 'images/interface/city_interface/city_buttons.png',
# 'images/interface/items/unlocker.png',
    ]


    if mp.need_full_load:
        $ images_load_now += [
#         'images/locations/bg/Hall/night.png',
# 'images/locations/bg/Hall/morning.png',
# 'images/locations/bg/Hall/evening.png',
# 'images/locations/bg/Hall/afternoon.png',
]


    call my_load_label from _call_my_load_label_2

    $ percent_load_now = '30%'

    $ images_load_now = [


# 'images/cg/window_event/woman_1.png',
# 'images/interface/survival_icons.png',
# 'images/interface/Time_Afternoon.png',
# 'images/interface/load_bar.png',
# 'images/interface/Panel_Day.png',
# 'images/interface/phone_bg.png',
# 'images/interface/play_icon.png',

# 'images/interface/items/keks.png',
# 'images/interface/items/phone.png',
# 'images/interface/items/bita.png',
# 'images/interface/items/hairpin.png',
# 'images/interface/phone_interface/phone_internet.png',
# 'images/interface/phone_interface/phone_frame_bg.png',

    ]


    if mp.need_full_load:
        $ images_load_now += [
# 'images/cg/window_event/woman_2.png',
# 'images/cg/window_event/night.png',
# 'images/cg/window_event/evening.png',
# 'images/locations/imagebuttons/GG_Room/bita.png',
# 'images/locations/imagebuttons/GG_Room/pants.png',
# 'images/locations/imagebuttons/City_Park/search_game_icon.png',
# 'images/locations/imagebuttons/Restroom/hair_pin.png',
]


    call my_load_label from _call_my_load_label_3


    $ percent_load_now = '50%'

    $ images_load_now = [
# 'images/cg/window_event/day.png',
# 'images/cg/igor_activities/igor_park.png',
# 'images/cg/milf_and_sister_activities/sister_restroom.png',
# 'images/cg/milf_and_sister_activities/milf_evening_hall.png',

# 'images/interface/phone_interface/phone_contacts_bg.png',
# 'images/interface/phone_interface/phone_option.png',


# 'images/cg/gg_activities/gg_tooth_restroom.png',



    ]

    if mp.need_full_load:
        $ images_load_now += [
#     'images/interface/Grid.png',
# 'images/interface/profile.png',
# 'images/interface/Icon_Quest.png',
# 'images/interface/loading_bg.png',
# 'images/interface/back_button_hover.png',
# 'images/interface/error_background.png',
# 'images/interface/Time_Evening.png',
# 'images/interface/Icon_Mobile.png',
# 'images/interface/back_button.png',
# 'images/interface/Icon_Map.png',


# 'images/cg/gg_activities/cg_surv_gg_dush.png',
# 'images/cg/gg_activities/gg_clothes_restroom.png',
# 'images/cg/gg_activities/gg_wash_kitchen.png',
# 'images/cg/gg_activities/gg_clothes_restroom_nude.png',
# 'images/cg/gg_activities/cg_surv_gg_tv.png',
# 'images/cg/gg_activities/active_cinema_cg.png',
# 'images/cg/gg_activities/cg_surv_gg_game.png',
# 'images/cg/gg_activities/gg_clean_hall.png',
# 'images/cg/gg_activities/cg_surv_gg_vanna.png',
# 'images/cg/gg_activities/cg_surv_gg_eat.png',

]



    call my_load_label from _call_my_load_label_14



    $ percent_load_now = '65%'

    $ images_load_now = [
# 'images/interface/info_panel/info_panel_milf.png',
# 'images/interface/info_panel/info_panel_nastroi.png',
# 'images/interface/info_panel/info_panel_sitost.png',
# 'images/interface/info_panel/info_panel_bg.png',

    ]
    if mp.need_full_load:
        $ images_load_now += [
# 'images/characters/GG/emo/Pancu_1.png',
# 'images/characters/GG/emo/Passion.png',
# 'images/characters/GG/emo/Blin.png',
# 'images/characters/GG/emo/Blin_embr.png',
# 'images/characters/GG/emo/Laughs.png',
# 'images/characters/GG/emo/Bita_Normal.png',
# 'images/characters/GG/emo/GivePhone.png',
# 'images/characters/GG/emo/Blin_dick.png',
# 'images/characters/GG/emo/Smile.png',
# 'images/characters/GG/emo/Skepticism.png',
# 'images/characters/GG/emo/Embarrassment.png',
# 'images/characters/GG/emo/Nude_Normal.png',
# 'images/characters/GG/emo/Flower.png',
# 'images/characters/GG/emo/Dick 2.png',
# 'images/characters/GG/emo/Think.png',
# 'images/characters/Milf/EMO/Pussy.png',
# 'images/characters/Milf/EMO/Street_Silence.png',
# 'images/characters/Milf/EMO/Polu_2.png',
# 'images/characters/Milf/EMO/Night_Normal.png',
# 'images/characters/Milf/1POSES/Blin.png',
]



    call my_load_label from _call_my_load_label_4



    $ percent_load_now = '80%'

    $ images_load_now = [

# 'images/interface/phone_interface/phone_sms.png',
# 'images/interface/phone_interface/phone_sms_bg.png',
# 'images/interface/phone_interface/SMS_ava_noname.png',
# 'images/interface/phone_interface/SMS_ava_igor.png',
# 'images/interface/info_panel/info_panel_gigiena.png',
# 'images/interface/info_panel/info_panel_money.png',


    ]

    if mp.need_full_load:
        $ images_load_now += [

# 'images/characters/GG/emo/Costume_Please.png',
# 'images/characters/GG/emo/Costume_Embarrassment.png',
# 'images/characters/GG/emo/Costume_Passion.png',

# 'images/characters/Igor/EMO/Spec_Normal_1.png',
# 'images/characters/Igor/EMO/Angry.png',
# 'images/characters/Igor/EMO/Agr.png',
# 'images/characters/Igor/EMO/Normal.png',
# 'images/characters/Igor/EMO/Ok.png',
# 'images/characters/Igor/EMO/Spec_Normal_2.png',
# 'images/characters/Igor/EMO/Bad.png',
# 'images/characters/Jay/EMO/Silence.png',
# 'images/characters/Jay/EMO/OMG.png',
# 'images/characters/Jay/EMO/Normal.png',
# 'images/characters/Jay/EMO/Mobile.png',
# 'images/characters/Milf/EMO/LOL.png',
# 'images/characters/Milf/EMO/Night_Passion.png',
# 'images/characters/Milf/EMO/Dress_Normal.png',
# 'images/characters/Milf/EMO/Street_Sad.png',
# 'images/characters/Milf/EMO/Passion.png',
# 'images/characters/Milf/EMO/Dress_Passion.png',
# 'images/characters/Milf/EMO/Dress_Chagrin.png',
# 'images/characters/Milf/EMO/Laughs.png',
# 'images/characters/Milf/EMO/Dress_Pose_3.png',
]


    call my_load_label from _call_my_load_label_6

    $ percent_load_now = '90%'

    $ images_load_now = [

# 'images/characters/Christie/emo/Passion.png',
# 'images/characters/Christie/emo/Laughs.png',
# 'images/characters/Christie/emo/Smile.png',
# 'images/characters/Christie/emo/Skepticism.png',
# 'images/characters/Christie/emo/Embarrassment.png',
# 'images/characters/Christie/emo/Surprise.png',
# 'images/characters/Christie/emo/Angry.png',
# 'images/characters/Christie/emo/Street.png',
# 'images/characters/Christie/emo/Normal.png',
# 'images/characters/Christie/emo/Chagrin.png',
# 'images/characters/Misha/emo/Passion.png',
# 'images/characters/Misha/emo/Laugh.png',


    ]


    if mp.need_full_load:
        $ images_load_now += [


# 'images/interface/click_here_button.png',
# 'images/interface/Button_No.png',
# 'images/interface/gradient_up.png',
# 'images/interface/Time_Morning.png',
# 'images/interface/heart_icon.png',
# 'images/interface/Inventory.png',
# 'images/interface/Icon_Bag.png',
# 'images/interface/give_item_bg.png',
# 'images/interface/Button_Yes.png',

# 'images/locations/imagebuttons/Kitchen/solar_oil.png',
# 'images/locations/imagebuttons/City_Home/Door.png',
# 'images/locations/imagebuttons/Milf_Room/phone_underpants_table.png',
# 'images/locations/imagebuttons/City_Shop/jay_bob.png',
# 'images/locations/imagebuttons/City_Shop/door.png',
# 'images/locations/buttons/Restroom_hover_1.png',
# 'images/locations/buttons/Hall_hover_0.png',
# 'images/locations/buttons/GG_Room_hover_1.png',
# 'images/locations/buttons/Corridor_hover_0.png',
# 'images/locations/buttons/Restroom_hover_0.png',
# 'images/locations/buttons/Hall_hover_1.png',
# 'images/locations/buttons/Milf_Room_hover_0.png',
# 'images/locations/buttons/kitchen_hover_0.png',
# 'images/locations/buttons/GG_Room_hover_0.png',
]

    call my_load_label from _call_my_load_label_5



    $ percent_load_now = '99%'

    $ images_load_now = [

# 'images/interface/phone_interface/Contacts_ava_noname.png',
# 'images/interface/phone_interface/SMS_ava_gg.png',
# 'images/interface/phone_interface/phone_main_bg.png',
# 'images/interface/phone_interface/phone_char.png',
# 'images/interface/phone_interface/Contacts_ava_igor.png',
# 'images/characters/Misha/emo/Smile.png',
# 'images/characters/Misha/emo/Embarrassment.png',
# 'images/characters/Misha/emo/Flower.png',
# 'images/characters/Misha/emo/Surprise.png',
# 'images/characters/Misha/emo/Normal.png',
# 'images/characters/Misha/emo/FlowerFight.png',
# 'images/characters/Misha/emo/Chagrin.png',
# 'images/characters/Bob/EMO/OMG.png',
# 'images/characters/Bob/EMO/Normal.png',
# 'images/characters/Bob/EMO/Mobile.png',


    ]



    call my_load_label from _call_my_load_label_7

    $ percent_load_now = '100%'

    $ images_load_now = [




# 'images/characters/GG/emo/Clock.png',
# 'images/characters/GG/emo/Dick_3.png',
# 'images/characters/GG/emo/Silence.png',
# 'images/characters/GG/emo/Please.png',
# 'images/characters/GG/emo/Nude_OMG.png',
# 'images/characters/GG/emo/Costume_Surprise.png',
# 'images/characters/GG/emo/WTF.png',

# 'images/characters/Milf/1POSES/n_body.png',
# 'images/characters/Officer/emo/Hm.png',
# 'images/characters/Officer/emo/Angry.png',
# 'images/characters/Officer/emo/Agr.png',
# 'images/characters/Officer/emo/Normal.png',
# 'images/characters/Officer/emo/Say.png',
# 'images/characters/Officer/emo/Pendant.png',

    ]



    show please_wait 100_per
    call my_load_label from _call_my_load_label_8




    hide please_wait
    hide screen please_wait_screen
    hide screen predict_load_screen
    hide screen please_wait_screen_tmp
    hide screen broken_save

    with Dissolve(.5)

    if mp.need_full_load:
        $ mp.need_full_load = None
        $ mp.save()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
