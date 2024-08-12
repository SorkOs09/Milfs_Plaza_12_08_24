init python:
    prologue_loc_names = {
    'Я'     : 'Me',

    'Джеймс'  : 'James',
    ' '     : ' ',
    }
    prologue_loc = {



"Ты снова на задание?" :"Are you going on a mission again?",

"Да. И на этот раз я не могу дать сроков.":"Yes and this time, I don't know when I'll be back.",

"Это что-то очень серьёзное?": "Is it something serious?",

"Это всегда очень серьёзно.": "It's always very serious.",

"Но ты же говорил, что выйдешь на пенсию пораньше." :"But you said you'd retire early.",

"Так и будет. Это последняя командировка. Я обещаю.":"I will. This is the last business trip. I promise.",

"Больше я вас не покину.":"This is the last time I'm leaving you.",

"[1]":"[1]",

"Про меня можешь не волноваться. Волнуйся за свою жену.":"You don't have to worry about me. Think about your wife.",

"Так ты присмотришь за Мариной?":"Will you look after Mary?",

"А у меня есть выбор?":"Do I have a choice?",

"Спасибо, брат. Я знал, что могу положиться на тебя.": "Thanks, brother. I knew I could rely on you.",

"[2]":"[2]",

"И да, не вздумай влезать в мутные истории. Иначе моему возвращению ты рад не будешь.": "One more thing, make sure you stay away from shady business. Otherwise, you won't be happy to see me back.",

"Эй, хочешь, чтобы я заботился о твоей жене, но при этом не доверяешь мне?":"Hey, you want me to look after your wife but at the same time, you don't trust me?",


"Просто не подведи меня, брат." : "Just don't let me down, brother.",


"Удачи…":"Good luck…",
"Брат…":"Brother…",
"[3]":"[3]",
"Тяжело не чувствовать себя куском говна,\nкогда твой старший брат крутой супер-агент на службе у правительства,\nа ты – обычный парень без каких-либо талантов.":"It's hard not to feel like a piece of shit when\nyour older brother is a badass super-agent in the service of the government\nand you're just a regular guy with no talent whatsoever.",

"Понимая, что у меня никогда в жизни не получиться\nвзобраться так же высоко, я решил рыть вниз.":"Realising that I would never be able to\nclimb as high as my brother did, I decided to dig down instead.",
"[4]": "[4]",
"Продажа наркотиков, шулерство, поиск должников и хорошие,\nкак мне казалось, знакомства из криминального мира.":"Selling drugs, cheating, looking for debtors, and making,\nas I thought at that time, good acquaintances from criminal world.",
"Я не был отпетым бандитом,\nкоторый грабил или обманывал работяг.":"I wasn't a hardcore thug\nwho robbed or tricked simple folk.",
"Как бы смешно это не звучало, но я старался придерживаться морального кодекса.":"As funny as it might sound, I tried to stick to a moral code.",
"Свои грязные деньги я зарабатывал на таком же дерьме, как и я сам." : "All the dirty money I earned I made on shitty people like myself.",
"И в какой-то момент, данный маршрут завёл меня в тупик…": "And at some point, this road took me to a dead end…",
"[5]":"[5]",

"Те деньги, что брат оставил мне на время своего отсутствия,\nя проиграл в спортивном тотализаторе спустя неделю." :"The money that my brother left me for the time he'd be away\nI lost in a sports betting game a week later.",

"И чтобы не вымаливать у Марины мелочь на карманные расходы,\nя решил быстро подзаработать." : "And since I didn't want to bother Mary and ask her for some pocket money,\nI decided make some money and fast.",

"[6]":"[6]",

"Мой хороший друг Игорь (сын русских эмигрантов),\nнашёл каких-то простаков для игры в покер. Лёгкие деньги." : "My good friend Igor (son of Russian immigrants),\nfound some simpletons to play poker with. Easy money.",

"Так называемые «простачки» оказались детьми местных чиновников,\nа чиновники, в свою очередь, были компаньонами бандита по кличке «Жлоб». Короче говоря, люди непростые." : '''The so-called "simpletons" turned out to be the children of local officials, and the officials, in turn,\nwere companions of a gangster nicknamed "The Goon". In short, they were complicated people.''',

"Друзья «Жлоба» играли на редкость плохо. Дилетанты.":'''The friends of "The Sting" played remarkably bad. Amateurs.''',

"[7]":"[7]",

"Мы легко заграбастали весь «банк», ловко перебрасывая друг другу козырей.\nВот только не учли, что наша игра записывается на камеру слежения.":"We easily won all the money, cleverly throwing trump cards to each other.\nWhat we didn't realise was that our game was being recorded on a security camera.",

"[8]":"[8]",

"Очень скоро нас вычислили и потребовали всё вернуть.\nЕстественно, с «моральной» компенсацией.": "Very soon they found us and demanded that we return all the money.\nNaturally, with «moral» compensation.",

"Затребованная сумма была слишком большой, а сроки – слишком короткие.\nНам ничего не оставалось, кроме как пойти на крайние меры." : "They demanded too much and basically didn't give us any time to find money.\nWe had no choice but to go to extreme measures.", 
"[9]":"[9]",
"Я и Игорь попытались стащить несколько дорогостоящих часов в ювелирном магазине,\nно тут же были пойманы полицейским патрулём…" : "Igor and I tried to steal some expensive watches from a jewellery shop,\nbut were immediately caught by a police patrol…",

"Чёрт!..": "Fuck!..",

"Теперь у меня не только проблемы с бандитами, но и с законом…":
"Now I'm not only in trouble with gangsters, but also with the law…",

"Брат, прости…": "Brother, forgive me…"



    }



screen prologue_screen(n_image, n_text, who='Я'):
    add n_image
    if preferences.language not in (None, 'eng', 'rus'):
        default prologue_loc_ntt = getattr(store, 'prologue_loc_'+preferences.language, prologue_loc)
    default m_size = 20
    viewport:
        xmaximum 1500
        ymaximum 300
        add '#0000'
        if preferences.language not in (None, 'eng', 'rus'):
            if who:
                text prologue_loc_names[who] + ': ' +  prologue_loc_ntt[n_text] xalign .5 size m_size bold True italic i_slash
            else:
                if '\n' in n_text:
                    $ texts =  prologue_loc_ntt[n_text].split('\n')
                    vbox xalign .5:
                        for i in texts:
                            text i xalign .5 size m_size bold True italic i_slash

                else:
                    text prologue_loc_ntt[n_text] xalign .5 size m_size bold True italic i_slash



        elif mp.language == 'ENG':
            if who:
                text prologue_loc_names[who] + ': ' +  prologue_loc[n_text] xalign .5 size m_size bold True italic i_slash
            else:
                if '\n' in n_text:
                    $ texts =  prologue_loc[n_text].split('\n')
                    vbox xalign .5:
                        for i in texts:
                            text i xalign .5 size m_size bold True italic i_slash

                else:
                    text prologue_loc[n_text] xalign .5 size m_size bold True italic i_slash



        else:
            if who:
                text who + ': ' + n_text xalign .5 size m_size bold True italic i_slash
            else:
                if '\n' in n_text:
                    $ texts = n_text.split('\n')
                    vbox xalign .5:
                        for i in texts:
                            text i xalign .5 size m_size bold True italic i_slash

                else:
                    text n_text xalign .5 size m_size bold True italic i_slash

        xalign .5 yalign .96

label prologue:
    $ i_slash = False

    play music 'audio/prologue.mp3' fadein 1.5
    show screen prologue_screen("cg/prologue/1.png", "Ты снова на задание?",) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/1.png", "Да. И на этот раз я не могу дать сроков.", 'Джеймс') with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/2.png", "Это что-то очень серьёзное?",) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/2.png", "Это всегда очень серьёзно.", 'Джеймс') with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/2.png", "Но ты же говорил, что выйдешь на пенсию пораньше.") with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/3.png", "Так и будет. Это последняя командировка. Я обещаю.", 'Джеймс') with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/3.png", "Больше я вас не покину.", 'Джеймс') with Dissolve(.25)

    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/2.png", "Про меня можешь не волноваться. Волнуйся за свою жену.") with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/2.png", "Так ты присмотришь за Мариной?", 'Джеймс') with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/2.png", "А у меня есть выбор?") with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/3.png", "Спасибо, брат. Я знал, что могу положиться на тебя.", 'Джеймс') with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/3.png", "И да, не вздумай влезать в мутные истории. Иначе моему возвращению ты рад не будешь.", 'Джеймс') with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/3.png", "Эй, хочешь, чтобы я заботился о твоей жене, но при этом не доверяешь мне?",) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/4.png", "Просто не подведи меня, брат.", 'Джеймс') with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Удачи…",) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Брат…", ) with Dissolve(.25)
    $ renpy.pause(9999999999)


    show screen prologue_screen("cg/prologue/5.png", "Тяжело не чувствовать себя куском говна,\nкогда твой старший брат крутой супер-агент на службе у правительства,\nа ты – обычный парень без каких-либо талантов.", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Понимая, что у меня никогда в жизни не получиться\nвзобраться так же высоко, я решил рыть вниз.", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Продажа наркотиков, шулерство, поиск должников и хорошие,\nкак мне казалось, знакомства из криминального мира.", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Я не был отпетым бандитом,\nкоторый грабил или обманывал работяг.", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Как бы смешно это не звучало, но я старался придерживаться морального кодекса.", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Свои грязные деньги я зарабатывал на таком же дерьме, как и я сам.", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "И в какой-то момент, данный маршрут завёл меня в тупик…", False) with Dissolve(.25)

    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Те деньги, что брат оставил мне на время своего отсутствия,\nя проиграл в спортивном тотализаторе спустя неделю.", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "И чтобы не вымаливать у Марины мелочь на карманные расходы,\nя решил быстро подзаработать.", False) with Dissolve(.25)

    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Мой хороший друг Игорь (сын русских эмигрантов),\nнашёл каких-то простаков для игры в покер. Лёгкие деньги.", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Так называемые «простачки» оказались детьми местных чиновников,\nа чиновники, в свою очередь, были компаньонами бандита по кличке «Жлоб». Короче говоря, люди непростые.", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Друзья «Жлоба» играли на редкость плохо. Дилетанты.", False) with Dissolve(.25)

    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Мы легко заграбастали весь «банк», ловко перебрасывая друг другу козырей.\nВот только не учли, что наша игра записывается на камеру слежения.", False) with Dissolve(.25)

    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Очень скоро нас вычислили и потребовали всё вернуть.\nЕстественно, с «моральной» компенсацией.", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Затребованная сумма была слишком большой, а сроки – слишком короткие.\nНам ничего не оставалось, кроме как пойти на крайние меры.", False) with Dissolve(.25)

    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Я и Игорь попытались стащить несколько дорогостоящих часов в ювелирном магазине,\nно тут же были пойманы полицейским патрулём…", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Чёрт!..", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Теперь у меня не только проблемы с бандитами, но и с законом…", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    show screen prologue_screen("cg/prologue/5.png", "Брат, прости…", False) with Dissolve(.25)
    $ renpy.pause(9999999999)
    hide screen prologue_screen with Dissolve(.25)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
