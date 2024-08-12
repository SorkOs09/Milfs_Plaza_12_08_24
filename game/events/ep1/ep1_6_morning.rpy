label ep1_6_morning:
    $ events.pop('ep1_6_morning', 0)

    stop music fadeout 1.5
    play music 'audio/n_girl.mp3' fadein 1.5
    scene expression 'images/cg/ep1/night_collector/Night_collector_1.png'
    show GG Invis
    show GG Invis:
        xalign .75
    with vpunch
    '[gg]' " Какого хера?!"
    'Ночная гостья' "Заткнись, иначе глотку перережу. "
    scene expression 'images/cg/ep1/night_collector/Night_collector_2.png'
    show GG Invis
    show GG Invis:
        xalign .75
    with vpunch
    '[gg]' " …."
    'Ночная гостья' "Так-то лучше, придурок."
    '[gg]' " Я не приду…"
    scene expression 'images/cg/ep1/night_collector/Night_collector_3.png'
    show GG Invis
    show GG Invis:
        xalign .75
    with vpunch
    'Ночная гостья' "Я не шучу!"
    '[gg]' " …"
    'Ночная гостья' "Чёрт, как же хочется тебя пырнуть. Без лишнего базара."
    '[gg]' " …"
    scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
    show GG Invis
    show GG Invis:
        xalign .75
    with Dissolve(.5)
    'Ночная гостья' "Ах да, на чём это я остановилась. .."
    'Ночная гостья' "Ну так вот, придурок. Ты задолжал нашему общему корешу"
    'Ночная гостья' "И он, чисто по-братски, попросил напомнить тебе, что деньги ему так и не дошли."
    '[gg]' " …"
    'Ночная гостья' "Да-да, теперь ты можешь открыть пасть для своих жалких оправданий."
    scene expression 'images/cg/ep1/night_collector/Night_collector_5.png'
    show GG Invis
    show GG Invis:
        xalign .75
    with Dissolve(.5)
    '[gg]' " Я отдам, клянусь. Но сумма слишком большая и я не могу это сделать прямо сейчас."
    '[gg]' " У меня намечается очень хорошая сделка, и уже на днях… ну, хотя бы через неделю, я лично приду к нашему «корешу» и верну ему всё до копеечки. "
    'Ночная гостья' "Примерно это я и ожидала услышать. "
    '[gg]' " Значит, вы дадите мне отсрочку? Ведь какой вам толк с мёртвого должника, верно?"
    scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
    show GG Invis
    show GG Invis:
        xalign .75
    with Dissolve(.5)
    'Ночная гостья' "Ха! Ты не такой уж и тупой, как выглядишь на самом деле, но выглядишь, как и прежде, полным придурком."
    'Ночная гостья' "Долг ты отдашь, хочешь ты того или нет. А пока что, я ставлю тебя на счётчик."
    '[gg]' " Счётчик?! Но мы так не договаривались!"

    'Ночная гостья' "Меня это не волнует. Я не собираюсь навещать тебя бесплатно. С тебя 20 баксов или всё, что у тебя есть."



    menu:
        "Вот, возьми (отдать {i}{b}20{/b}{/i} баксов)." if money >= 20:
            $ money -= 20
            $ show_text_animation('-20 money')
            scene expression 'images/cg/ep1/night_collector/Night_collector_8.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Люблю, когда всё по-моему. "
            '[gg]' " Надеюсь, ты удовлетворена и мы больше не увидимся."
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with vpunch
            'Ночная гостья' "Ещё чего. Я буду навещать тебя каждую неделю, пока ты, наконец, не выплатишь долг. "
            '[gg]' " …"
            scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Оривидэрчи, придурок. "
        "!Вот, возьми (отдать {i}{b}20{/b}{/i} баксов)." if money <  20:
            $ pass
        "Это всё, что я могу дать (отдать {i}{b}[money]{/b}{/i} баксов)." if money > 0 and money < 20:
            $ show_text_animation('-' + str(money) + ' money')
            
            $ add_ach('ACH_13')
            $ money = 0
            scene expression 'images/cg/ep1/night_collector/Night_collector_8.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Не густо, конечно, но это лучше, чем совсем ничего. "
            '[gg]' " Надеюсь, ты удовлетворена и мы больше не увидимся."
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with vpunch
            'Ночная гостья' "Ещё чего. Я буду навещать тебя каждую неделю, пока ты, наконец, не выплатишь долг. "
            '[gg]' " …"
            scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Оривидэрчи, придурок. "
        "Извини, но у меня вообще ничего нет…" if True:
            scene expression 'images/cg/ep1/night_collector/Night_collector_3.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Мать твою, ты что, хочешь, чтобы я выпотрошила тебя? "
            '[gg]' " Клянусь собственными яйцами, у меня нет ни копейки."
            'Ночная гостья' "Хочется в это верить, иначе в следующий раз, ты обязательно останешься без них."
            '[gg]' " В следующий раз?!"
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "А ты что думал? Я буду навещать тебя каждую неделю, пока ты, наконец, не выплатишь долг. "
            '[gg]' " …"
            scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Оривидэрчи, придурок. "
        "Я дам тебе вдвое больше, если ты покажешь мне сиськи (отдать {i}{b}40{/b}{/i} баксов)." if money >= 40:
            $ money -= 40
            scene expression 'images/cg/ep1/night_collector/Night_collector_3.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with vpunch
            'Ночная гостья' "Ублюдок хренов, да у тебя не иначе девять жизней!! "
            '[gg]' "Эй-эй, спокойней! Ты же сама сказала, что прибыла сюда не за тем, чтобы убить меня. Вот я и подумал, что…"
            'Ночная гостья' "Подумал, что я вот так просто покажу свои сиськи?!"
            scene expression 'images/cg/ep1/night_collector/Night_collector_9.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            '[gg]' " Не бесплатно, замечу. "
            'Ночная гостья' "Ты просто бесишь, козлина! "
            scene expression 'images/cg/ep1/night_collector/Night_collector_10.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Что мне мешает забрать эти 40 долларов и навешать тебе люлей?"
            '[gg]' " Наверное, то, что ты понятия не имеешь, где я храню свои деньги, и если вздумаешь меня калечить, на шум явится моя подруга."
            '[gg]' "Но Тебе не нужны свидетели, а мне – проблемы."
            '[gg]' "К тому же, если ты убьёшь меня, я не смогу отдать долг… и тогда долг, скорее-всего, придётся отдавать тебе."
            scene expression 'images/cg/ep1/night_collector/Night_collector_4.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Чёртов сукин сын… Мне следовало бы порешить тебя и будь таков."
            '[gg]' " Но…?"
            'Ночная гостья' "…."
            scene expression 'images/cg/ep1/night_collector/Night_collector_11.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Тебе всё равно никто не поверит"
            'Ночная гостья' "40 баксов это 40 баксов, чувак. Гони их сюда."
            '[gg]' " Сперва зрелище."
            'Ночная гостья' "Окей… Придурок."
            scene expression 'images/cg/ep1/night_collector/Night_collector_12.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Смотри и запоминай. Ты видишь их в первый и последний раз в жизни."
            '[gg]' "Чёрт, а ты горячая. "
            'Ночная гостья' "…"
            '[gg]' "А можно потрогать?"
            'Ночная гостья' "Нет."
            '[gg]' "И за большую сумму?"
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            'Ночная гостья' "Всё, заткнись. Представление окончено. Давай бабки."
            scene expression 'images/cg/ep1/night_collector/Night_collector_8.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            $ show_text_animation('-40 money')
            '[gg]' " Вот."
            'Ночная гостья' "Оривидэрчи, придурок. Увидимся на следующей неделе. "
            scene expression 'images/cg/ep1/night_collector/Night_collector_6.png'
            show GG Invis
            show GG Invis:
                xalign .75
            with Dissolve(.5)
            '[gg]' "Чего?!"
            'Ночная гостья' "А ты что думал? Я буду навещать тебя каждую неделю, пока ты, наконец, не выплатишь долг. "
            '[gg]' " …"
        "!Я дам тебе вдвое больше, если ты покажешь мне сиськи (отдать {i}{b}40{/b}{/i} баксов)." if money <  40:
            $ pass


    $ Event('night_girl', 'GG_Room', day_start = time.day_now + 7, time = ['morning'])



    scene black with Dissolve(.5)
    '[gg]' "Я срочно должен рассказать Игорю о ночном посетителе."

    if love_milf >= 1:

        $ descript = _('Я срочно должен рассказать Игорю о ночном посетителе.')

        $ sms_now = SmsBlock('Игорь', 'igor', "1", Jump('ep1_7_phone'))

        $ sms_now.add_sms(_('GG: Чувак, ты не поверишь, что со мной случилось этой ночью.\n\n'))
        $ sms_now.add_sms(_('TT: Попробуй удивить.'))
        $ sms_now.add_sms(_('GG: Какая-то деваха залезла ко мне в комнату и угрожала ножом, чтобы я поскорее отдал наш долг.\n\n\n'))
        $ sms_now.add_sms(_('TT: Деваха?! Вчера, когда я впрягался вместо тебя в парке, ко мне подошёл один из бугаёв Жлоба \nи тоже, знаешь ли, угрожал.\n\n'))
        $ sms_now.add_sms(_('GG: Чувак… Надеюсь, всё обошлось?'))
        $ sms_now.add_sms(_('TT: Не считая пару сломанных рёбер и угроз с требованием отдать кучу денег в кратчайшие сроки, всё ОХУЕНО обошлось.\n\n\n'))
        $ sms_now.add_sms(_('GG: Слушай, я пока не знаю, где мы можем достать столько денег, кроме как грабежом.\n\n'))
        $ sms_now.add_sms(_('TT: Скорее всего нас просто посадят. А потом, по просьбе Жлоба, \nпревратят в двух пидарастических сучек.\n\n'))
        $ sms_now.add_sms(_('GG: И что ты предлагаешь?!'))
        $ sms_now.add_sms(_('TT: Я ничего не предлагаю, чувак. Я в отчаянии. '))
        $ sms_now.add_sms(_('GG: Ладно, спишемся позже.'))
        $ sms_now.add_sms(_('TT: ББ'))
        
    elif True:

        $ descript = _('Требование: Привязанность Марины (1)')

        $ milf_love_quests = 1


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
