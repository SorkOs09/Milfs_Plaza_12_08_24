screen christie_root_12_screen:
    imagebutton:
        idle 'cg/christie_root/misha_store/water_polka.png'
        hover im.MatrixColor('cg/christie_root/misha_store/water_polka.png', im.matrix.brightness(.3))
        focus_mask True
        at ButtonEffect01
        action Return()

image christie_root_12_bg = Composite((1920, 1080),
(1202, 0),  Crop((0,0,514,1080), "cg/christie_root/misha_store/misha_store_atlas.png"))

image christie_root_12 1 = "cg/christie_root/misha_store/Misha_Water_1.png"

image christie_root_12 2 = "cg/christie_root/misha_store/Misha_Water_2.png"

image christie_root_12 3 = "cg/christie_root/misha_store/Misha_Water_3.png"

image christie_root_12 4 = "cg/christie_root/misha_store/Misha_Water_4.png"

label christie_root_12:




    scene expression 'locations/bg/StoreIn/afternoon_without_girl.png'
    show christie_root_11_JayBob_Store_original
    with Dissolve(.5)
    $ renpy.pause(1, hard = True)
    call screen christie_root_12_screen






    scene expression 'cg/christie_root/afternoon_without_girl_blur.png'
    show christie_root_11_JayBob_Store_blur

    show christie_root_12 1
    with my_dissolve

    "[gg]" "Вроде дышит."
    "[gg]" "Попробую полить её немного. "

    show christie_root_12 2
    with my_dissolve

    $ renpy.music.stop(fadeout=1.5)
    $ renpy.music.play('audio/past-sadness-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)

    "[gg]" "Вода холодная, должна реагировать."

    show christie_root_12 3
    with my_dissolve


    "[gg]" "Действительно реагирует…"
    "[gg]" "И у меня, в общем, тоже заметная реакция теперь."
    "[gg]" "Какие у неё большие, красивые груди."
    "[gg]" "Её возбуждённые соски магнитят мою разгорячившуюся ладонь. "

    show christie_root_12 4
    with vpunch


    "[gg]" "Ой…"

    scene black with Dissolve(.5)

    $ renpy.pause(.75, hard = True)

    scene expression 'locations/bg/StoreIn/afternoon_without_girl.png'
    with Dissolve(.5)

    show Misha Water_Chagrin
    show Misha Water_Chagrin:
        xalign .85
        ypos 1085


    show GG Costume_Surprise:
        xzoom 1
        xalign .2


    with my_dissolve


    $ renpy.music.stop(fadeout=.5)

    $ renpy.music.play('audio/deadly-roulette-by-kevin-macleod-from-filmmusic-io.mp3', fadein = .5)

    "[gg]" "Извини, я всего лишь пытался привести тебя в порядок. "

    "Мишванда" "Это всё из-за твоих духов. "
    show Misha Water_Normal
    "Мишванда" "Теперь, пожалуйста, я попрошу тебя покинь магазин, пока у меня не возникло желание выяснить, что именно ты здесь делаешь, и зачем поливаешь мои сиськи водой."
    show GG Costume_Surprise
    "[gg]" "Намёк понял, не дурак, дурак бы не понял."
    $ store.name_boxes_displ.force_update = True
    show GG Costume_Please:
        xzoom -1
        ease .9 xalign -0.5
    show Misha:
        xzoom -1
        ease .9 xalign 1.4

    $ renpy.pause(1.3, hard = True)

    scene black with Dissolve(.5)




    $ time.time_now = "evening"

    $ location_now  = "City_Home"




    $ add_to_gallery('20_3')

    $ store.name_boxes_displ.force_update = False


    $ descript_Christie= _("Встретиться с Зудилой и Бубнилой, чтобы взять у них кофе «Релакс».")



    $ Event('christie_root_13', 'JayBob', priority = -1)

    if not from_gallery_check():
        #if preferences.language in ('eng', None, 'rus'): 
        call misha_root_0 from _call_misha_root_0




    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
