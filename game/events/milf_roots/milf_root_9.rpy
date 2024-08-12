label milf_root_9_0:
    $ new_events = True
    $ milf_root_9_text  = _("Всё слишком хорошо оборачивается для меня, чтобы жить припеваючи. Стоит быть на чеку. Мне кажется в течении 2-3 дней может произойти что-то, что вновь напомнит о прежних временах.")


    $ Event('milf_root_9', 'Corridor', day_start = time.day_now+2)
    return

label milf_root_9:
    if getattr(store, 'block_exit_home', False) or getattr(store, 'block_time_forward', False):
        $ Event('milf_root_9', 'Corridor', day_start = time.day_now+2)
        jump main_interface_label
    $ events.pop('milf_root_9', 0)







    call show_bg_image_label from _call_show_bg_image_label_158
    play sound 'audio/zvonok.mp3'
    $ renpy.pause(1, hard = True)
    show GG Think
    if getattr(store, 'old_location', None) in ['Hall', "Restroom"]:

        show GG Think at go_from_right(xxalign = .15)
    elif True:
        show GG Think at go_from_left
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "[gg]" "Кто бы это мог быть в такое время? Я никого не жду. "

    play sound 'audio/zvonok.mp3'
    show GG:
        xalign .15
    with my_dissolve
    "[gg]" "Продолжают звонить…"
   #show GG Think
    "[gg]" "У меня почему-то плохое предчувствие. "
   # show GG Think
    "[gg]" "Ну а раз так, то и открывать смысла нет. Я у себя дома, я никого не жду и принимать кого-либо в гостях не обязан."




    show Milf Normal
    show Milf Normal at go_from_right

    "Марина" "[gg], милый, почему ты стоишь у двери и не открываешь? Не слышишь, что ли, звонят!"
    show GG Normal
    show Milf Surprise:
        xalign .85
    with my_dissolve
    "[gg]" "Слышу, просто не хочу. "
    show Milf Angry
    "Марина" "Что за чушь? Очень грубо с твоей стороны заставлять человек ждать у двери. "
    show GG Passion
    "[gg]" "А если бы нас не было дома?"
    show Milf Normal
    "Марина" "Но мы дома, и ни от кого не скрываемся. Открой дверь, пожалуйста."
    show GG Smile
    "[gg]" "Ладно…"

    play sound 'audio/zvonok.mp3'

    $ renpy.pause(1, hard = True)

    show Officer Hm
    show Officer Hm:
        alpha 0 xalign .5
        easein_cubic .5 xalign .55 alpha 1.0






    show GG Angry
    with my_dissolve
    "Офицер" "Добрый вечер, сударыня. Добрый вечер, [gg]."

    show Officer:
        alpha 1.0
        easein_cubic .5 xalign .9
        xzoom -1
    show Milf:
        easein_cubic .5 xalign .3
        xzoom -1
    show GG Angry:
        easein_cubic .5 xalign .03


    "[gg]" "{i}Он был бы добрым, если бы ты, мудак, не припёрься сюда.{/i}"


    show Milf Normal:
        xalign .3 xzoom -1

    "Марина" "Здравствуйте, офицер."
    show Officer:
        alpha 1.0
        xalign .9
        xzoom -1
    show GG:
        xalign .03
    show Milf Normal:
        xzoom 1
    with my_dissolve
    "Марина" "[gg], поздоровайся с гостем. "
    show GG Normal
    "[gg]" "Я поздоровался."
    show Milf Normal
    "Марина" "Я почему-то не слышала."
    show GG Skepticism
    "[gg]" "Я просто кивнул. "
    show Officer Normal
    "Офицер" "Не волнуйтесь, это не столь важно"
    show Officer Say
    show Milf:
        xzoom -1
    with my_dissolve
    "Офицер" "Могу ли я побыть наедине с вашим подопечным, нам следует кое-что обсудить."
    show Milf Normal
    "Марина" "Конечно. Проходите в зал, а я пока сделаю чай. "
    show Officer Normal
    "Офицер" "Извините, но я бы хотел, чтобы нас никто не отвлекал. "
    show Officer Normal
    "Офицер" "Дайте мне минутку и я уйду."
    show Milf Surprise
    "Марина" "Что-то серьёзное?"
    show Officer Skepticism
    show Milf Sad
    with my_dissolve
    "Офицер" "Всё хорошо, я просто уточню пару деталей, которые касаются только меня и этого молодого человека."
    show GG Normal:
        easein_cubic .5 xalign .3
    show Milf:
        easein_cubic .5 xalign .03
    "[gg]" "Ладно, пойдём. "


    show Milf:
        xzoom 1
        easein_cubic 2.5 xalign -1.5

    $ renpy.pause(.3, hard = True)

    show GG WTF:
        easein_cubic 2 xalign 1.5
    show Officer:
        xzoom 1
        easein_cubic 2 xalign 1.5
    show black
    show black:
        alpha 0.0
        easein_cubic 1 alpha 1.0
    $ renpy.pause(1.2, hard = True)

    $ location_now = 'Hall'

    call show_bg_image_label from _call_show_bg_image_label_159
    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    show GG WTF

    show GG WTF at go_from_left


    show Officer Normal
    show Officer Normal at go_from_left(xxalign = .9)

    $ renpy.pause(1, hard = True)






    show Officer Normal:
        xzoom -1 xalign .9
    show GG WTF:
        xalign .15
    with my_dissolve
    "[gg]" "Слушаю вас."
    "Офицер" "Я только что от судьи и у тебя большие неприятности, парень."
    show Officer Hm
    "Офицер" "Тот жирдяй, который взял нас в заложники, хотел и тебя убить, много что рассказал на допросе, включая дела, в которых ты замешан. "
    show GG Angry
    "[gg]" "Херня!"
    show GG Angry
    "[gg]" "Я никогда не работал со Жлобом. Да и не стал бы. Он мокрушник. "
    show GG Angry
    "[gg]" "Чтобы он там не говорил, это враньё. У него нет доказательств. "
    show Officer Normal
    "Офицер" "Может да, может не, я со свечкой не стоял, [gg]."
    show Officer Normal
    "Офицер" "Так или иначе, он решил утянуть тебя с собой. "
    show Officer Normal
    "Офицер" "Ему грозит пожизненное, и терять нечего. "
    show Officer Normal
    "Офицер" "Например, есть неопровержимые доказательства того, что ты продавал наркотики."
    show GG Chagrin
    "[gg]" "Ну… Может, когда-то что-то такое и было. "
    show GG Chagrin
    "[gg]" "Если я в чём-то виноват, то готов понести наказание. "
    show GG Angry
    "[gg]" "Но Жлоб явно оклеветал меня, и подписываться под чужие дела я не намерен. "
    show Officer Smile
    "Офицер" "Всё это ты будешь рассказывать на суде, перед присяжными и под прикрытием хорошего адвоката, если, конечно, такой у тебя предвидится. "
    show Officer Smile
    "Офицер" "У следователя на руках полно доказательств твоей причастности, а уж настоящие они или нет, выясним по ходу дела."
    show GG Skepticism
    "[gg]" "Ну и зачем же вы пришли? Уведомить? Вручить мне повестку? "
    show Officer Normal
    "Офицер" "Я пришёл помочь, [gg]. "
    show Officer Normal
    "Офицер" "Твоя жизнь только начинается и ты, как мне кажется, давно извлёк правильные выводы из всех своих уроков. "
    show Officer Normal
    "Офицер" "Верно я говорю?"
    show GG Normal
    "[gg]" "Допустим."
    show Officer Smile
    "Офицер" "Я могу замолвить за тебя словечко… "
    show GG Skepticism
    "[gg]" "Да ну?"
    show Officer Hm
    "Офицер" "Могу настоять на том, чтобы следователь более тщательно перепроверил улики, убедившись, что ты никак не причастен к грязным делишкам Жлоба."
    show Officer Normal
    "Офицер" "Это избавит тебя от опасности заключения под стражу, от лишнего стресса и, конечно же, огромных трат на адвоката. "
    show GG Normal
    "[gg]" "Ну и что вы хотите взамен? "
    show Officer Skepticism
    "Офицер" "Едва ли ты можешь предложить материальную выгоды, да и не нужны мне твои деньги, парень."
    show Officer Skepticism
    show expression 'cg/ep45/shower_3/shadow.png':
        alpha .0
        easein_cubic 1 alpha .4
    "Офицер" "Речь идёт о куда более ценном..."
    show expression 'cg/ep45/shower_3/shadow.png':
        easein_cubic 1 alpha .6
    "Офицер" "...товаре"
    show Officer Smile
    show expression 'cg/ep45/shower_3/shadow.png':
        easein_cubic 1 alpha .85
    "Офицер" "Деньги – всего лишь средство. Главное то, что за них можно купить, но куда ценнее то, что за деньги не купишь..."
    show GG Think
    "[gg]" "И что же это? "
    hide expression 'cg/ep45/shower_3/shadow.png'
    with my_dissolve

    show Officer Laughs
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/district-four-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Офицер" "Марина."
    show GG Surprise
    with my_vpunch
    "[gg]" "Марина?! Ты хочешь мою подругу?!!"
    show GG Angry
    show Officer Angry
    with my_dissolve
    "[gg]" "Да она ни за что в жизни не будет с таким как ты!"
    show Officer Say
    "Офицер" "Позволь мне самому уладить этот вопрос, [gg]."
    show Officer Smile
    "Офицер" "От тебя лишь требуется самая малость – не мешать. "
    show GG Angry
    "[gg]" "Да пошёл ты!"
    show Officer Normal
    "Офицер" "Ну вот, опять старая песня."
    show Officer Normal
    "Офицер" "Я уже пытался быть джентльменом, но ты счёл это слабостью."
    show Officer Normal
    "Офицер" "Ты воспользовался моей добротой и кинул меня. Подарил медальон от своего имени – подло, [gg], очень подло."
    show Officer Normal
    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/hidden-agenda-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Офицер" "Но мстить я не стал, как ты помнишь."
    show Officer Smile
    "Офицер" "Ты расправился со Жлобом, тем самым спас и себя, и своих близких, и… меня, хе-хе."
    show GG Skepticism
    "[gg]" "Какое великодушие. С моей стороны, разумеется."
    show Officer Normal
    "Офицер" "Ну да. Ну да..."
    show Officer Normal
    "Офицер" "Вот только мой интерес к Марине не угас."
    show GG Angry
    "[gg]" "Не смей приближаться к Марине, подонок!"
    show Officer Hm
    "Офицер" "Больно было смотреть, как она бросилась к тебе в объятия… А ведь рядом был муж, хе-хе."
    show GG Angry
    with my_vpunch
    "[gg]" "Вали нахер из моего дома!!"
    show Officer Angry
    "Офицер" "А то что? "
    show Officer Angry
    "Офицер" "Нападёшь на полицейского при исполнении? "
    show Officer Laughs
    "Офицер" "Или побежишь плакаться Марине? Ха-ха-ха."
    show GG Angry:
        easein_cubic .5 xalign .5
    "[gg]" "Я сказал – пошёл вон!"
    show Officer Smile:
        easein_cubic 2.5 xalign .1
    show GG:
        1.75
        xzoom -1
    "Офицер" "Я вернусь. И очень скоро. "
    show GG:
        xzoom -1
    show Officer Normal:
        easein_cubic 4 xalign -1.5
    "Офицер" "Не провожай. "


    show GG:
        xzoom -1
        easein_cubic 3 xalign -1.5
    $ renpy.pause(1, hard = True)

    scene black with Dissolve(.5)



    $ location_now = 'Corridor'

    call show_bg_image_label from _call_show_bg_image_label_160
    with Dissolve(.5)

    $ renpy.pause(.5, hard = True)
    show GG Angry

    show GG Angry at go_from_right(xxalign = .99, xxzoom = -1)

    show Officer Normal
    show Officer Normal at go_from_right(xxalign = .7, xxzoom = -1)

    $ renpy.pause(1.3, hard = True)







    show Milf Normal
    show Milf Normal at go_from_left(xxzoom = -1)

    "Марина" "Вы уже уходите, офицер? "
    show Officer:
        xalign .7
        xzoom -1
    show Milf:
        xalign .15
        xzoom -1
    show GG:
        xalign .99
        xzoom -1
    with my_dissolve
    "Офицер" "О да. Разрешите откланяться. "
    show Milf Normal
    "Марина" "До сви…"
    show Officer Chagrin
    with my_vpunch
    "Офицер" "Ах да! Чуть не забыл."
    show Officer Say
    "Офицер" "У меня для вас кое-какое извещение."
    show Officer:
        xzoom 1
    "Точнее, нисколько для вас, сколько для этого паренька."
    show Officer Normal:
        xzoom -1
    "Офицер" "Мне почему-то сдаётся, вы должны быть в курсе. "
    show Milf Surprise
    "Марина" "Что это?"
    show Officer Normal
    "Офицер" "Вызов на предварительную беседу со следователем. "
    show Milf Surprise
    "Марина" "Но… почему?"
    show Officer Normal:
        xzoom 1
    "Офицер" "Думаю, [gg] вам всё расскажет."
    show Officer Normal:
        xzoom -1
    "Офицер" "А вот теперь я пошёл. Позвольте."
    show GG Angry
    "[gg]" "…"
    show Milf Normal
    "Марина" "Идите-идите…"

    show Officer:
        alpha 1.0
        easein_cubic 1 alpha .0 xalign .5

    show GG Angry:
        easein_cubic .7 xalign .8

    $ renpy.pause(1, hard = True)


    $ renpy.music.stop(fadeout=.5)
    $ renpy.music.play('audio/smooth-lovin-by-kevin-macleod-from-filmmusic-io.mp3', fadein = 1.5)
    "Марина" "[gg], как это понимать?"
    hide Officer
    show GG Chagrin:
        xalign .8
    with my_dissolve
    "[gg]" "Эхо прошлого."
    show Milf Sad
    "Марина" "Я серьёзно! Насколько опасными могут быть последствия похода к следователю? В чём тебя обвиняют… снова?"
    show GG Angry
    "[gg]" "Клянусь, это всё мерзавец-коп!"
    show GG Angry
    "[gg]" "Он запал на тебя. Ещё давно."
    show GG Chagrin
    "[gg]" "И не отстанет от нас, пока не получит желаемого. "
    show Milf Embarrassment
    "Марина" "Хочешь сказать, мы снова в опасности?"
    show GG Chagrin
    "[gg]" "К сожалению…"
    show Milf Normal
    "Марина" "Я ведь прямо могу ему заявить, чтобы он прекратил свои ухаживания!"
    show GG Laughs
    "[gg]" "Я думаю он прекрасно понимает, что ты питаешь к нему чувств. "
    show Milf Normal
    "Марина" "Ну и что же он собирается делать? Силой меня взять?!"
    show GG Angry
    "[gg]" "От него всё можно ожидать. Он представитель закона, за ним власть."
    show GG Please
    "[gg]" "Ему поверят больше, чем нам."
    show GG Please
    "[gg]" "Сейчас он пытается шантажировать меня, надеется «убрать меня с дороги», дабы я позволил ему встречаться с тобой. "
    show Milf Embarrassment
    "Марина" "А ты?"
    show GG Normal
    "[gg]" "Послал его нахер."
    show Milf Surprise
    "Марина" "Слишком беспечно."
    show Milf Sad
    "Марина" "А если следователь его сообщник, а? Что если они организуют всё так, что тебя посадят? Что тогда, [gg]?!"
    show Milf Chagrin
    "Марина" "Я очень волнуюсь за тебя, милый…"
    show GG Passion
    "[gg]" "Ничего со мной не будет, Марина."
    show GG Smile
    "[gg]" "Правда на моей стороне. "
    show GG Normal
    "[gg]" "Хотя и неправда тоже…"
    show GG Normal
    "[gg]" "Я выкручусь, как выкручивался всегда."
    show GG Normal
    "[gg]" "Сейчас нужно просто обезопасить себя. "
    show GG Normal
    "[gg]" "Я куплю тебе перцовый баллончик."
    show Milf Normal
    "Марина" "…."
    show Milf Normal

    "Марина" "Ну, если ты считаешь нужным."
    show GG Normal

    "[gg]" "Считаю."
    show Milf Normal
    "Марина" "…."




    $ perec_at_web_shop = 10
    if not hasattr(store, 'add_items_for_storein_shop_fixed'):
        $ add_items_for_storein_shop_fixed = []
    $ add_items_for_storein_shop_fixed.append(perec_at_web_shop)

    $ Event('milf_root_10', location = 'City_Shop', need_items = [10,])
    $ new_events = True

    $ milf_root_9_text = _("Купить перцовый баллончик для Марины.")
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
