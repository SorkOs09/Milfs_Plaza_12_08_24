label ep1_2_morning:


    call show_bg_image_label from _call_show_bg_image_label_3

    with Dissolve(.5)

    play sound 'audio/sms.ogg'
    $ renpy.pause(.5, hard = True)
    $ descript = _('Я должен проверить СМС от друга.')
    '[gg]' "Я должен проверить СМС от друга."


    $ sms_now = SmsBlock('Игорь', 'igor', "4", Jump('ep1_2_morning_2'))
    $ sms_now.add_sms(_('TT: Чувак, ну как ты там? Обошлось?'))
    $ sms_now.add_sms(_('GG:  Дали пару недель общественных работ. '))
    $ sms_now.add_sms(_('TT: Хреново.'))
    $ sms_now.add_sms(_('TT: А я тебе говорил, надо было через переулок гнать!\n\n'))
    $ sms_now.add_sms(_('GG: Уже не важно. Лучше скажи, тебе удалось что-нибудь стащить?\n\n '))
    $ sms_now.add_sms(_('TT: Не, извини…'))
    $ sms_now.add_sms(_('GG: Отлично. Долг общий, а выкручиваться одному мне?\n\n'))
    $ sms_now.add_sms(_('TT: Могу вместо тебя дворы мести.'))
    $ sms_now.add_sms(_('GG: Согласен. '))
    $ sms_now.add_sms(_('TT: А что по деньгам? Придумал, где достать?'))
    $ sms_now.add_sms(_('GG: Придержи коней! Ничего ещё не думал. Давай, до связи.\n\n'))
    $ sms_now.add_sms(_('TT: ББ'))


    $ phone_warning = True

    $ events.pop('ep1_2_morning', 0)

    jump main_interface_label


label ep1_2_morning_2:

    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()

    call show_bg_image_label from _call_show_bg_image_label_4
    show GG Think
    show GG Think:
        ypos 1085
        zoom 1.0-0.035
        xalign .5

    with Dissolve(.5)



    $ block_exit_home  = True


    '[gg]' "{i}Я влип. И очень серьёзно.{/i}"




    '[gg]' "{i}Если в ближайшее время я не смогу вернуть крупную сумму денег местному бандиту, то рискую остаться не только без штанов, но и чего похуже.{/i}"

    '[gg]' "{i}Конечно, я разделю эту участь со своим лучшим другом, но мне от этого не легче.{/i}"

    '[gg]' "{i}Нам уже сделали одно предупреждение, и мне не охота услышать второе.{/i}"

    '[gg]' "{i} Я не хочу, чтобы Марина знала о моих проблемах. {/i}"

    '[gg]' "{i} Лучшее, что я могу сейчас сделать, это просто наладить с ней отношения. {/i}"

    $ descript = _('''Лучшее, что я могу сделать сейчас, это просто наладить с ней отношения.''')

    $ Event('ep1_3_mother', 'Milf')

    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
