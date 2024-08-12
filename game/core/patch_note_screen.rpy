
screen patch_note_screen:
    #add '#0009'
    #image 'MainMenu3.png'
    imagebutton:
        idle '#0000'
        hover '#0000'
        action Function(set_new_patch, config.version)
    
    # text 'Content patch ' + str(config.version) bold True size 65 color '#000' xalign .5 ypos 5 font 'fonts/ARMB.ttf'
    
    # text 'Content patch ' + str(config.version) bold True size 60 color '#FFF' xalign .5 ypos 5 font 'fonts/ARMB.ttf'
    
    viewport:
        xmaximum 580
        ymaximum 1020
        #yalign
        align (.5, .4)
        add '#0008'

    viewport:
        xmaximum 515
        ymaximum 920
        ypos 80
        xalign .5
        #scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True

        vbox ypos 700:

                # text '' size 20

                # text '' size 20


                # text '' size 20
                # text '' size 20

                # text '' size 20

                # text '' size 20

                # text '' size 20

            # viewport:
            #     xmaximum 740
            #     ymaximum 775
            #     image '#000a'
                #text '1.0a' color '#ffae00' size 27 


            if preferences.language not in ('rus', None):
                text '1.0.7b' color '#ffae00' size 27 
                text '' size 5
                text "Start point of new Mary event moved forward at plot line." color '#fff' size 27 
                text '' size 5
                text '' size 5
                
                text '1.0.7' color '#ffae00' size 27 
                text '' size 5

                text 'Added:  ' color '#fff' size 27 
                text '' size 5
                text '- Belated but beautiful' color '#fff' size 27 
                text 'scene with Mary.' color '#fff' size 27
                text '' size 5
                text "- 2 animations" color '#fff' size 27 
                text '' size 20

                text 'Fixes:  ' color '#fff' size 27 
                text '' size 5
                text '- Fixes a bug in the relationship system with Mary when relationship level could reset at random moment' color '#fff' size 24 
                text '' size 5
                text "- Fix for incorrect clothing sprites in some scenes" color '#fff' size 24 
                text '' size 5
                text "- Fixes a bug in the clothing store, when it could be locked, even though it was needed for a quest" color '#fff' size 24 
                text '' size 5
                text "- Fix for a bug in name bars system when the bars staying on the wrong character/showed the wrong name/not displayed at all in some scenes" color '#fff' size 24 
                text '' size 5
                text "- Bug fix for not being able to open the bathroom door when it's needed by quest, but we haven't break down door before" color '#fff' size 24 
                text '' size 5
                text "- Updated description of some quests to make it clearer" color '#fff' size 24 
                text '' size 5
                text "- Updated English translation of many scenes from the beginning of the game " color '#fff' size 24 
                text '' size 5
                text "- Fixes typos in the text" color '#fff' size 24 
                text '' size 5
                text "- Fixes of untranslated text" color '#fff' size 24 
                text ''
                text '1.0.5' color '#ffae00' size 27 
                text '' size 5
                text 'JINGLE BAM, DAMN IT!' color '#fff' size 27 
                
                text "New Year's update is ready!" color '#fff' size 27 
                text ''

                text 'We broke our ass, but still managed to release a new content patch for the New Year!' color '#fff' size 27 
                text 'Yes, not everything we planned was implemented, but 2 out of 3 events were completed!' color '#fff' size 27 
                
                text "Even if you're not planning on celebrating New Year's, rest assured that these couple of wonderful scenes will brighten up your weekend." color '#fff' size 27 
                
                text 'Have a good game! Thanks for support!' color '#fff' size 27 
                
                text 'See you in the new year!' color '#fff' size 27 
                
                text ''
                text 'Details:' color '#fff' size 27 bold True
                text '- Christy "3rd level in the bathroom"' color '#fff' size 27 
                text '- Susan - continuation of the quest "Observation"' color '#fff' size 27 
                text '... in January we will complement this update with a new scene with Mary!' color '#fff' size 27 
                text ''
                text 'ALL! :3' color '#fff' size 27 

                text ''
                text ''
                text ''
                text ''
                text ''
                text '1.0' color '#ffae00' size 27 
                text 'Existential hello!' color '#fff' size 27 xalign .5 font 'fonts/FUTURA-N.ttf' text_align .5
                text ''
                text 'A month ago, Patreon kicked us in the balls by banning our page and disabling all active subscribers, thereby depriving us of our main income, but this did not break us and did not prevent further development of the game.' color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text ''
                
                text "We have returned. We're back with a fresh update! The most anticipated and hottest of all previously released is 1.0." color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text "It is short, even tiny, but contains a lot of animated scenes that we carefully created despite the current situation." color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5 
                text ''
                
                text "The resolution of the plot for Christy and Susan has come to an end, although the story itself is still far from over. I have to add a beautiful cliffhanger that will put an end to episode 1 of our game." color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text '' size 30
                
                text 'Soon we will announce the release of games on Steam. In the meantime, have a nice time!' color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text '' 
                text 'Content:' color '#fff' size 27 bold True xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text '' size 20
                text "The end of Christy and Susan's story." color '#fff' size 27  xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text "5 gorgeous animations." color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text "New sprites, twists, crazy finale!" color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5

                text ''
                
                text "Thank you so much for your support and trust. Everyone who stayed with us even after Patreon closed - you are the best!" color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5

                text '' size 20
                text '' size 20
                text '' size 20
                text '0.9.5g' color '#ffae00' size 27 

                text 'Fixed bug report system. Now it works again!' color '#fff' size 27 
                
                text 'Fixed bugs with quests getting stuck randomly (like movie quests).' color '#fff' size 27 
                
                text 'Fixed typos in the text and some omissions in the translation.' color '#fff' size 27 
                
                text '' size 20
                text '' size 20
                text '' size 20
                text '0.9.5f' color '#ffae00' size 27 

                text 'Changed patreon link to subscribestar.' color '#fff' size 27 
                
                text '' size 20
                text '' size 20
                text '' size 20

                text '0.9.5b-e' color '#ffae00' size 27 

                text 'Fixes bugs what was found by subscribers at beta test.' color '#fff' size 27 
                
                text '' size 20
                text '' size 20
                text '' size 20
                text '0.9.5a'  color '#ffae00' size 27 

                text "While you're taking a breath after the hot scenes in 0.9, we " color '#fff' size 27 

                text "decided that now it's time for dessert and so we're releasing " color '#fff' size 27 

                text '0.9.5, the content of which is pure fanservice.  ' color '#fff' size 27 

                text '' size 20
                text "Actually both 0.9, 0.9.5 and 1.0 were planned to be released " color '#fff' size 27 

                text "as a single huge update, but you wouldn't forgive us another month of waiting. " color '#fff' size 27 

                text "Besides, you should get happiness in parts, in " color '#fff' size 27 

                text 'small portions. So there you go, sign here! ' color '#fff' size 27 

                text '' size 20
                
                text 'What to expect in the update:' color '#fff' size 35 

                
                text 'Recurring scenes: ' color '#fff' size 27 

                
                text '1) Deep night dive with Christy napping. ' color '#fff' size 27 

                
                text '2) Bathroom hygiene procedures. ' color '#fff' size 27 

                
                text '3) You scratch my back, I scratch yours. ' color '#fff' size 27 


                text '' size 20
                
                text 'Enjoy the game! ' color '#fff' size 32 
                text '' size 20
                text '' size 20
                text '' size 20
                text '0.9b'  color '#ffae00' size 27 
                text 'Fixes bugs what was found by subscribers at beta test:' color '#fff' size 27 
                text '' size 20
                text 'Fixed disappearance of sprites in some dialogs.     ' color '#fff' size 27 
                text '' size 20

                text 'Removed the sound of the door, which played almost at     ' color '#fff' size 27 
                text 'any change of location, and sometimes twice.     ' color '#fff' size 27 
                
                text '(It now plays if there was a     ' color '#fff' size 27 
                text 'door between locations).     ' color '#fff' size 27 
                text '' size 20

                text 'Updated some scenes in the gallery     ' color '#fff' size 27 
                text '(previously they could be broken or missing).     ' color '#fff' size 27 
                text '' size 20

                text 'Added ability to disable cloud     ' color '#fff' size 27 
                text 'animation on the map     ' color '#fff' size 27 
                text '(In case it slows down).     ' color '#fff' size 27 
                text '' size 20
                text '' size 20
                text '' size 20
                text '0.9a'  color '#ffae00' size 27 
                text "Continuation of Christy and Susan's storyline.     " color '#fff' size 27 
                text '' size 20

                text 'Get ready for new icons, sprites, events, and more.     ' color '#fff' size 27 
                text '' size 20

                text 'Two amazing love scenes for Christy.     ' color '#fff' size 27 
                text '' size 20
                
                text 'One intriguing scene for Susan.     ' color '#fff' size 27 
                text '' size 20
                

                
                text 'A mini-game.     ' color '#fff' size 27 
                text '' size 20
                text '' size 20
                text '' size 20

                text 'New Interface Design:' color '#fff' size 27 
                text '' size 20

                text 'A sleek dialogue panel.     ' color '#fff' size 27 
                text 'Comic strips for scenes.     ' color '#fff' size 27 
                text 'A report icon.     ' color '#fff' size 27 
                text 'A dynamic menu in the bottom left corner.     ' color '#fff' size 27 
                text 'The city comes to life with moving clouds.     ' color '#fff' size 27 
                text '' size 20
                text '' size 20
                text '' size 20

                text 'New Costumes (ONLY for MECENATES):' color '#fff' size 27 
                text '' size 20
                text "(Costumes are entirely {i}unique{/i}, and the character's pose and location will change based on the chosen clothing and the time of day.)" color '#fff' size 27 
                text '' size 10
                
                text 'Gantz Costume.     ' color '#fff' size 40 
                text 'Cow costume.     ' color '#fff' size 40 
                text '' size 20
                text '' size 20
                text '' size 20


                text 'An Abundance of Animations and Effects:' color '#fff' size 27 
                text '' size 20
                text 'More sprites and events in one scene' color '#fff' size 27 
                text 'Programmed animation for eyeliner (our programmer went all out!)' color '#fff' size 27 
                text 'Two-dimensional animation during love scenes.' color '#fff' size 27 
                text ''
                text ''
                text ''


                text '0.8.9d2'  color '#ffae00' size 27 
                text 'Added a system for sending bug reports.' color '#fff' size 27 
                text ''

                text '0.8.9d'  color '#ffae00' size 27 
                text ''

                text 'The duration of the mini games with arrows has been increased. They are much easier now!' color '#fff' size 27 
                text ''

                text "Completely fixed the behavior of Susan's house. Now it's not giving scripting errors at all." color '#fff' size 27 
                text ''

                text 'Fixed additional quest "Movie" for Mary - now it is activated correctly.' color '#fff' size 27 
                text ''

                text 'Fixed the scene "Massage" - now it opens gradually,' color '#fff' size 27 
                text 'as you go through the story (previously it was opened at once completely)' color '#fff' size 27 
                text ''
                text 'Fix for Live2d at some platforms.' color '#fff' size 27 
                text ''
                text 'Added ability to return to the old gallery after full' color '#fff' size 27 
                text 'unlock via cheat menu (only for version 0.8.9d and higher. If you unlocked' color '#fff' size 27 
                text "the gallery before - alas, you can't go back)" color '#fff' size 27 
                text ''

                text 'Added the setting to change the scale of the interface. ' color '#fff' size 27 
                text '{color=#F00}WARNING!{/color} The game works 100%% correctly only at standard scale - 1.0.' color '#fff' size 27 
                text 'In case you have problems with a different scale - return the standard one,' color '#fff' size 27 
                text 'play the problematic place, then you can return to different one again.' color '#fff' size 27 
                text 'Also, game looks good only with 1.0 scale.' color '#fff' size 27 
                text ''
                text 'Fixed some spelling and translation omission in English text.' color '#fff' size 27 
                text ''
                text ''



                text 'Main fixes for critical bugs:' color '#fff' size 27 
                text ''


                text 'Fixed some quests looping, they now end correctly' color '#fff' size 27 
                text ''


                text 'Fixed eternal ability to give some quest items (gas canister) to Mary - now you can give them only once.' color '#fff' size 27 
                text ''


                text 'Fixed quest with buying Harley Quinn costume - now it is always available in the store' color '#fff' size 27 

                text 'when the quest is activated (Please check both stores!)' color '#fff' size 27 

                text ''
                text '0.8.9c'  color '#ffae00' size 27 
                text ''
                text 'Fix for Susan quests, when game crushed in some cases' color '#fff' size 27  
                text 'If you going to quest at afternoon.'  color '#fff' size 27 
                text ''
                text 'For escape some sadness bugs starts of Christie root little bit moved' color '#fff' size 27  
                text '(really little bit, 15 minutes of real gameplay)'  color '#fff' size 27 
                text ''

                text '0.8.9b'  color '#ffae00' size 27 
                text ''
                text 'A few more fixes for bugs that found attentive players.' color '#fff' size 27 
                text 'The main fix is the correct ending of the final event with Christy.' color '#fff' size 27 
                text 'Previously it did not end and going to the kitchen it could be played endlessly.' color '#fff' size 27 
                text 'Now everything works correctly (from old safes too!)' color '#fff' size 27 
                
                text ''
                text 'We have also slightly corrected grammar and punctuation in both languages of the game.' color '#fff' size 27 

                text 'We sincerely thank all players who help us with detailed bug reports and saves in buggy areas.' color '#fff' size 27 
                text "Even if it's just fixing a typo in the text - it's also a help for us." color '#fff' size 27 

                text 'You help us to make the game better.' color '#fff' size 27 

                text ''

                text '0.8.9a' color '#ffae00' size 27 
                text ''
                text "This update focuses on advancing Christie's storyline" color '#fff' size 27  
                text "That's been stale for a long time by introducing new spicy situations, exploring familiar characters in new ways, and showcasing beautifully animated love scenes." color '#fff' size 27  
                text 'And as an added bonus, a touch of tears :)' color '#fff' size 27  
                text 'Yes, you heard it right, tears. Remember, guys, girls come and go.' color '#fff' size 27  
                text 'Even wives leave. But a true friend stays with you forever.' color '#fff' size 27 

                text ''
                text 'So, what can you expect to see in the update:' color '#fff' size 27 

                text 'Introducing a new character, Helene (she replaces the old clothes saleswoman)' color '#fff' size 27 

                text "Development of Christie's plot." color '#fff' size 27 

                text 'Two love scenes.' color '#fff' size 27 

                text "Numerous animations that enhance the game's liveliness and interactivity." color '#fff' size 27 
                text ''
                
                text '0.8.7d' color '#ffae00' size 27 
                text ''
                text 'Fixes: ' color '#fff' size 27 
                text '    Hotfix for some bugs what we found at public release. ' color '#fff' size 27 
                text ''
                text '    The main fix is the quest where you need to spy at the Сat at evening.' color '#fff' size 27 
                text ''
                text '    Now it works fine (from old safe-files too!)' color '#fff' size 27 
                text ''
                
                text '0.8.7c' color '#ffae00' size 27 
                text ''
                text 'Fixes: ' color '#fff' size 27 
                text '    Fixed for android version.' color '#fff' size 27 
                text ''
                               
                text '0.8.7b ' color '#ffae00' size 27 
                text ''
                text 'Fixes: ' color '#fff' size 27 
                text '    Fixed bug with panties in the second episode, when the game did not allow to steal them and the passage got stuck. Now you can steal the panties in peace! ' color '#fff' size 27 
                text ''
                text '    Found the problematic places with the work of the cache in the engine RenPy and fixed. The game now runs much faster and more stable! ' color '#fff' size 27 
                text ''
                text 'Android: ' color '#fff' size 27 
                text '    The android version is now slightly more compressed than the pc version, making the game more stable, and taking into account the size of the phone screen, the difference is not visible. ' color '#fff' size 27 
                text ''
                text '    Scenes that what was crashed in the gallery now work without any problems.' color '#fff' size 27 
                text ''
                text ''
                text '0.8.7a  ' color '#ffae00' size 27 
                text ''
                
                text 'Fixes:  ' color '#fff' size 27 
                text '    Bugs with SMS that overlapped each other.  ' color '#fff' size 27 
                text ''
                text '    Removed binding of Mary to location and time from some quests.  ' color '#fff' size 27 
                text ''
                text '    Restricted access to high-level events, which were previously available from the start.  ' color '#fff' size 27 
                text ''
                text '    The system of active items on locations has been redesigned. For example, a missing refrigerator or a flower in the hallway.  ' color '#fff' size 27 
                text ''
                text '    The name system has been reworked so that they disappear nicely along with the characters.  ' color '#fff' size 27 
                text ''
                text '    Some deadly bugs in quests, like the $150 handover stage to a MILF.  ' color '#fff' size 27 
                text ''
                text '    Removed Russian text in the English version.  ' color '#fff' size 27 
                text ''
                text '    Made a more dense blur on the pictures in the scene gallery, so as not to spoil the plot.  ' color '#fff' size 27 
                text ''
                text '    Fixed a bug that dramatically increased the number of found "bags" to 100 in the inventory.  ' color '#fff' size 27 
                text ''
                text '    A bug where you can get a critical error if you close the computer menu before watching porn.  ' color '#fff' size 27 
                text ''
                text '    In the quest where you need to watch porn, we made a note text - "NIGHT"!  ' color '#fff' size 27 
                text ''
                text '    Something on trifles.  ' color '#fff' size 27 

                text 'Added:  ' color '#fff' size 27 
                text '    Icon for the file being launched.  ' color '#fff' size 27 
                text '    Emotions in some scenes for Christy and the Officer.  ' color '#fff' size 27 
                text '    SMS selection system.  ' color '#fff' size 27 
                text ''
                text ''
                
                text '0.8.65' color '#ffae00' size 27 
                text ''
                
                text 'Fixes:' color '#fff' size 27 
                text ''
                text 'In a situation where two or more events must start'  color '#fff' size 27 
                text 'You will given the choice of which event to start first.' color '#fff' size 27 
                text 'The next event can only be activated the next day.' color '#fff' size 27 
                text 'I hope this saves us from deadly bugs!' color '#fff' size 27 
                text '    Bug with SMS that overlapped with each other.' color '#fff' size 27 
                text '    Bug with items that replaced each other.' color '#fff' size 27 
                text "    Cat's Night Quest Bug - Bitch, now you're not going anywhere!" color '#fff' size 27 
                text '    Bug with the closing of the store that threw out into the street.' color '#fff' size 27 
                text '    Bug with the number of packets what you get in the park.' color '#fff' size 27 
                text '    Bug with pants that are there, but are not.' color '#fff' size 27 
                text "    Bug with Mary's ass abuzz (you could look endlessly under the dress in the kitchen, getting a reputation every time)." color '#fff' size 27 
                text '    Crash in the Christy root.' color '#fff' size 27 
                #text 'Баг со взломом двери в спальне Марины, который не позволял взламывать замок после 5 “эпизода”.
                text '    The translation has been corrected in some places.' color '#fff' size 27 
                text ''
                text 'Android:' color '#fff' size 27 
                text '    Invisible animations are now visible. Enjoy!' color '#fff' size 27 
                text ''
                text ''
                text ''
                text ''
                text ''
                
            else:
                text '1.0.7b' color '#ffae00' size 27 
                text '' size 5
                text "Точка активации нового ивента с Мариной передвинута дальше по сюжету." color '#fff' size 27 
                text '' size 5
                text '' size 5
                text '1.0.7b' color '#ffae00' size 27 
                text '' size 5

                text 'Добавлено:  ' color '#fff' size 27 
                text '' size 5
                text '- Запоздалая, но красивая' color '#fff' size 27 
                text 'сцена с Мариной.' color '#fff' size 27
                text '' size 5
                text "- 2 анимации" color '#fff' size 27 
                text ''

                text 'Исправления:  ' color '#fff' size 27 
                text '' size 5
                text '- Исправление ошибки в системе отношений с Мариной, когда уровень отношения мог сброситься сам по себе' color '#fff' size 22 
                text '' size 5
                text "- Исправление неправильных спрайтов одежды в некоторых сценах" color '#fff' size 22 
                text '' size 5
                text "- Исправление ошибки в магазине одежды, когда он мог заблокироваться, хотя нужен по квесту" color '#fff' size 22 
                text '' size 5
                text "- Исправление ошибки в плашках имен, когда плашки стояли не на том персонаже/показывали неправильное имя/не отображались совсем в некоторых сценах" color '#fff' size 22 
                text '' size 5
                text "- Исправление ошибки с невозможностью открыть дверь ванной когда это нужно по сюжету если мы не взломали её до этого" color '#fff' size 22 
                text '' size 5
                text "- Обновленно описание некоторых квестов чтобы было понятнее что нужно делать" color '#fff' size 22 
                text '' size 5
                text "- Обновлен перевод на английский многих сцен из начала игры" color '#fff' size 22 
                text '' size 5
                text "- Исправления опечаток в тексте" color '#fff' size 22 
                text '' size 5
                text "- Исправление не переведенных мест" color '#fff' size 22 
                

                text '1.0.5' color '#ffae00' size 27 
                text '' size 5
                text 'ДЖИНГЛ БЭМС, ЁПТА!' color '#fff' size 27 
                
                text "Предновогоднее обновление готово!" color '#fff' size 27 
                text ''

                text 'Мы порвали себе жопу, но таки успели выпустить новый контент-патч к Новому Году!' color '#fff' size 27 
                text 'Да, не всё, что мы планировали, смогли реализовать, однако 2 из 3 ивентов сделали!' color '#fff' size 27 
                
                text "Даже если вы и не планируете отмечать Новый Год, уверен, эти пару чудесных сцен скрасят ваши выходные. " color '#fff' size 27 
                
                text 'Приятной игры! Спасибо за поддержку!' color '#fff' size 27 
                
                text 'Увидимся в новом году!' color '#fff' size 27 
                
                text ''
                text 'Подробности:' color '#fff' size 27 bold True
                text '- Кристи "3й уровень в ванной"' color '#fff' size 27 
                text '- Сьюзен - продолжение квеста "Наблюдение"' color '#fff' size 27 
                text '... в Январе мы дополним это обновление новой сценой с Мариной!' color '#fff' size 27 
                text ''
                text 'ВСЁ! :3' color '#fff' size 27 




                text ''
                text ''
                text ''
                text ''
                text ''
                #Changed patreon link to subscribestar, because patreon page was banned
                text 'Экзистенциальный привет!' color '#fff' size 27 xalign .5 font 'fonts/FUTURA-N.ttf' text_align .5
                text ''
                text 'Месяц назад Патреон влупил нам по яйцам, забанив нашу страницу и отключив всех активных подписчиков, тем самым лишив нас основного дохода, но это не сломило нас, и не помешало дальнейшей разработке игры.' color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text ''
                
                text 'Мы вернулись. Вернулись со свежем обновлением! Самым ожидаемым и самым жарким из всех ранее выпущенных - 1.0.' color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text 'Оно короткое, даже крошечное, но содержится массу анимированных сцен, которые мы старательно создавали вопреки сложившейся ситуации.' color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5 
                text 'Развязку сюжета за Кристи и Сьюзен подошла к концу, хотя сама история еще далеко от завершения. Мне предстоит добавить красивый клифхендер, который поставит жирную точку в 1 эпизоде нашей игры.' color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text ''
                text 'Вскоре мы анонсируем выходит игры в Стим. Ну а пока, приятного время провождения!' color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text '' 
                text 'Содержание:' color '#fff' size 27 bold True xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text '' size 20
                text 'Окончание истории Кристи и Сьюзен.' color '#fff' size 27  xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text '5 шикарных анимаций.' color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5
                text 'Новые спрайты, твисты, угарный финал!' color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5

                text ''
                
                text 'Огромное спасибо за поддержку и доверие. Все, кто с нами остался даже после закрытия Патреона - вы лучшие!' color '#fff' size 27 xalign .5  font 'fonts/FUTURA-N.ttf' text_align .5

                text '' size 20
                text '' size 20
                text '' size 20
                #Changed patreon link to subscribestar, because patreon page was banned
                text '0.9.5g' color '#ffae00' size 27 

                text 'Исправленна система баг репортов. Теперь она снова работает!' color '#fff' size 27 
                
                text 'Исправленны баги с рандомным застреванием квестов (вроде квестов на просмотр кино).' color '#fff' size 27 
                
                text 'Исправленны опечатки текста и некоторые пропуски в переводе.' color '#fff' size 27 
                
                text '' size 20
                text '' size 20
                text '' size 20
                text '0.9.5f' color '#ffae00' size 27 

                text 'Ссылка на patreon заменена ссылкой на subscribestar.' color '#fff' size 27 
                
                text '' size 20
                text '' size 20
                text '' size 20

                text '0.9.5b-e' color '#ffae00' size 27 

                text 'Исправление багов найденных в ходе бета-теста подписчиками.' color '#fff' size 27 
                
                text '' size 20
                text '' size 20
                text '' size 20
                text '0.9.5a'  color '#ffae00' size 27 

                text 'Пока вы переводите дух после горячих сцен в 0.9, мы решили, ' color '#fff' size 27 

                text 'что сейчас самое время для десерта и выпускаем' color '#fff' size 27 

                text '0.9.5, всецело состоящий из фан-сервиса. ' color '#fff' size 27 

                text '' size 20
                text 'На самом деле и 0.9, и 0.9. 5 и 1.0 планировалось выпустить ' color '#fff' size 27 

                text 'единым обновлением, но ещё один месяц ожидания вы нам не ' color '#fff' size 27 

                text 'простили бы. К тому же, счастье надо получать по частям, ' color '#fff' size 27 

                text 'малыми порциями. Так что вот, держите, распишитесь! ' color '#fff' size 27 

                text '' size 20
                
                text 'Содержание:' color '#fff' size 35 

                
                text 'Повторяющиеся сцены: ' color '#fff' size 27 

                
                text '1) Глубокое ночное погружение с дремлющей Кристи. ' color '#fff' size 27 

                
                text '2) Гигиенисеские процедуры в ваной. ' color '#fff' size 27 

                
                text '3) Ты мне - я тебе. ' color '#fff' size 27 


                text '' size 20
                
                text 'Приятной игры!  ' color '#fff' size 32 
                text '' size 20
                text '' size 20
                text '' size 20
                text '0.9b'  color '#ffae00' size 27 
                text 'Исправление багов найденных в ходе бета-теста подписчиками:' color '#fff' size 27 
                text '' size 20
                text 'Исправленно исчезновение спрайтов в некоторых диалогах.     ' color '#fff' size 27 
                text '' size 20

                text 'Убран звук двери который воспроизводился практически при     ' color '#fff' size 27 
                text 'любой смене локации, причем иногда по два раза.     ' color '#fff' size 27 
                
                text '(Теперь он воспроизводится если     ' color '#fff' size 27 
                text 'между локациями была дверь).     ' color '#fff' size 27 
                text '' size 20

                text 'Обновленны некоторые сцены в галерее     ' color '#fff' size 27 
                text '(раньше они могли быть сломаны или отсутсвовали).     ' color '#fff' size 27 
                text '' size 20

                text 'Добавленна возможность отключать     ' color '#fff' size 27 
                text 'анимацию облаков на карте     ' color '#fff' size 27 
                text '(На случай если она тормозит).     ' color '#fff' size 27 
                text '' size 20
                text '' size 20
                text '' size 20
                text '0.9a'  color '#ffae00' size 27 
                text 'Продолжение сюжета Кристи и Сьюзен.     ' color '#fff' size 27 
                text '' size 20

                text 'Новые иконки, спрайты, события и так далее.     ' color '#fff' size 27 
                text '' size 20

                text 'Две изумительные любовные сцены для Кристи.     ' color '#fff' size 27 
                text '' size 20
                
                text 'Одна интригующая сцена  для Сьюзен.     ' color '#fff' size 27 
                text '' size 20
                

                
                text 'Мини-игра.     ' color '#fff' size 27 
                text '' size 20
                text '' size 20
                text '' size 20

                text 'Новое оформление интерфейса:' color '#fff' size 27 
                text '' size 20

                text 'Панель диалогов.     ' color '#fff' size 27 
                text 'Комикс-баблы для сцен.     ' color '#fff' size 27 
                text 'Значок репорта.     ' color '#fff' size 27 
                text 'Динамическое меню (в левом нижнем углу).     ' color '#fff' size 27 
                text 'Оживший город благодаря движущимся облакам.     ' color '#fff' size 27 
                text '' size 20
                text '' size 20
                text '' size 20

                text 'Новые костюмы ТОЛЬКО для МЕЦЕНАТОВ:' color '#fff' size 27 
                text '' size 20
                text '(Костюмы абсолютно {i}уникальные{/i}, и в зависимости от выбранной одежды, персонаж будет иметь разную позу и местоположение в зависимости времени суток)' color '#fff' size 27 
                text '' size 10
                
                text 'Костюм Gantz.     ' color '#fff' size 40 
                text 'Костюм Коровки.     ' color '#fff' size 40 
                text '' size 20
                text '' size 20
                text '' size 20


                text 'Обилие анимации и эффектов:' color '#fff' size 27 
                text '' size 20
                text 'Больше спрайтов и событий в одной сцене' color '#fff' size 27 
                text 'Программная анимация для подводки (Программист оторвался по полной!)' color '#fff' size 27 
                text 'Двухмерная анимация во время любовных эпизодов' color '#fff' size 27 
                text ''
                text ''
                text ''


                text '0.8.9d2'  color '#ffae00' size 27 
                
                text 'Добавлена система для отправки баг репортов' color '#fff' size 27 
                text ''

                text '0.8.9d'  color '#ffae00' size 27 
                text ''

                text 'Увеличена длительность мини игры со стрелками. Теперь они гораздо проще!' color '#fff' size 27 
                text ''

                text 'Полностью исправлено поведение дома Сьюзан. Теперь он не вызывает скриптовых ошибок.' color '#fff' size 27 
                text ''

                text 'Исправлен доп квест "фильм" у Марины - теперь он активируется правильно.' color '#fff' size 27 
                text ''

                text 'Исправлена сцена "Массаж" - теперь она открывается постепенно,' color '#fff' size 27 
                text 'по ходу прохождения сюжета (раньше она открывалась сразу полностью)' color '#fff' size 27 
                text ''
                text ''
                text 'Исправления Live2d модуля для некоторых платформ.' color '#fff' size 27 
                text ''
                text 'Добавлена возможность вернуться к старой галерее после полной разблокировки' color '#fff' size 27 
                text 'через чит меню (только для версии 0.8.9d и выше. Если вы разблокировали' color '#fff' size 27 
                text 'галерею до этого - увы, вернуться не получится)' color '#fff' size 27 
                text ''

                text 'Добавлена возможность менять масштаб интерфейса.' color '#fff' size 27 
                text '{color=#F00}ВНИМАНИЕ!{/color} Игра работает 100%% правильно только при стандартном масштабе 1.0.' color '#fff' size 27 
                text 'В случае если вы имеете проблемы с другим масштабом - верните стандартный, ' color '#fff' size 27 
                text 'пройдите проблемное место, затем можете снова поставить желаемый.' color '#fff' size 27 
                text 'Также, игра выглядит нормально только при масштабе 1.0' color '#fff' size 27 
                text ''
                text 'Исправлена некоторая орфография и пропуск перевода в английском тексте.' color '#fff' size 27 
                text ''
                text ''



                text 'Основные исправления критических багов:' color '#fff' size 27 
                text ''


                text 'Исправлена зацикленность некоторых квестов, теперь они заканчиваются правильно' color '#fff' size 27 
                text ''


                text 'Исправлена вечная возможность передавать некоторые квестовые предметы (газовый балончик) Марине - теперь их можно передать один раз' color '#fff' size 27 
                text ''


                text 'Исправлен квест с покупкой костюма Харли Квин - теперь он всегда доступен в магазине, ' color '#fff' size 27 

                text 'когда квест активирован (Пожалуйста, проверьте оба магазина!)' color '#fff' size 27 
                text ''


                # text ''
                text '0.8.9c'  color '#ffae00' size 27 
                text ''
                text 'Исправление для квеста Сьюзан, когда игра падала в некоторых случаях' color '#fff' size 27 
                text 'Если вы шли на квест днем.' color '#fff' size 27 
                text ''
                text 'Начало рута Кристи было сдвинуто чтобы избежать некоторые баги' color '#fff' size 27  
                text '(Сдвинуто совсем немного, буквально на 15 минут игры)'  color '#fff' size 27 
                text ''

                text '0.8.9b'  color '#ffae00' size 27 
                text ''
                text 'Еще несколько фиксов для багов что обнаружили внимательные игроки.' color '#fff' size 27 
                text 'Основное исправление - правильное завершение финального ивента с Кристи.' color '#fff' size 27 
                text 'Раньше он не заканчивался и заходя на кухню его можно было проигрывать бесконечно.' color '#fff' size 27 
                text 'Теперь все работает правильно (в том числе со старых сейвов!)' color '#fff' size 27 
                
                text ''
                text 'Также немного поправили грамматику и пунктуацию в обоих языках игры.' color '#fff' size 27 

                text 'Мы искренне благодарим всех игроков кто помогает нам подробными баг-репортами и сохранениями в местах ошибок.' color '#fff' size 27 
                text 'Даже если это просто исправление опечатки в тексте - это тоже помощь для нас.' color '#fff' size 27 

                text 'Вы помогаете делать нам игру лучше.' color '#fff' size 27 

                text ''
                text '0.8.9a'  color '#ffae00' size 27 
                text ''
                text 'Это сюжетнее обновление, сдвигающее с мёртвой точки рут Кристи.' color '#fff' size 27  
                text 'Мы вновь оказываемся в незаярудных ситуациях. Знакомимся со старыми персонажами по-новому.' color '#fff' size 27  
                text 'Лицезрим красивые, анимационные сцены любви. Ну и, как вишенка на торте - немного плачем :)' color '#fff' size 27  
                text 'Да-да, плачем. Запомните, чуваки, девки приходят и уходят.' color '#fff' size 27  
                text 'Даже жёны уходят. А друг останется навсегда.' color '#fff' size 27 

                text ''
                text 'Содержание:' color '#fff' size 27 

                text 'Новый персонаж Маша (вместо старой продавщицы одежды)' color '#fff' size 27 

                text 'Сюжетное развитие Кристи.' color '#fff' size 27 

                text 'Две любовные сцены.' color '#fff' size 27 

                text 'Много разнообразной анимации, которая делают игру ещё более живой и интерактивной.' color '#fff' size 27 
                text ''

                
                text '0.8.7d'  color '#ffae00' size 27 
                text ''
                text 'Исправления: ' color '#fff' size 27 
                text '    Хотфикс для списка багов которые мы обнаружили после релиза паблик версии. ' color '#fff' size 27 
                text ''
                text '    Основное исправление - квест где нужно следить за Кэт ночью.' color '#fff' size 27 
                text ''
                text '    Теперь он работает нормально (В том числе со старых сейвов!)' color '#fff' size 27 
                text ''
                
                text '0.8.7c'  color '#ffae00' size 27 
                text ''
                text 'Исправления: ' color '#fff' size 27 
                text '    Исправления для андроид версии.' color '#fff' size 27 
                text ''
                         
                text '0.8.7b  '  color '#ffae00' size 27 
                text ''
                text 'Исправления:  ' color '#fff' size 27 
                text 'Исправлен баг с трусами во втором эпизоде, когда игра не давала их украсть и прохождение застревало. Теперь можно спокойно украсть трусы! ' color '#fff' size 27 
                text ''
                text 'Найдены проблемные места с рабоой кэша в движке RenPy и поправлены. Теперь игра работает намного быстрее и стабильнее! ' color '#fff' size 27 
                text ''
                text 'Андроид:  ' color '#fff' size 27 
                text '    Рерусры андроид версии теперь сжаты чуть сильнее чем на пк, благодаря чему игра работает стабильнее, а с учетом размеров экрана телефона разница не видна. ' color '#fff' size 27 
                text ''
                text '    Сцены, которые крашились в галерее теперь работают без проблем  ' color '#fff' size 27 
                text ''
                text ''
                
                text '0.8.7a  '  color '#ffae00' size 27 
                text ''
                text 'Исправления:  ' color '#fff' size 27 
                text 'Баги с СМС, что накладывались друг на друга.  ' color '#fff' size 27 
                text 'Убрали у некоторых квестов обязательную привязку Марины/Мэри к локации и времени.  ' color '#fff' size 27 
                text ''                
                text 'Ограничили доступ к высокоуровневым ивентам, который прежде были доступны со старту.  ' color '#fff' size 27 
                text ''
                text 'Переделана система активных предметов на локациях. Например, пропадающий холодильник или цветок в коридоре.  ' color '#fff' size 27 
                text ''
                text 'Переделана система имён, чтобы они красиво исчезали вместе с персонажами.  ' color '#fff' size 27 
                text ''
                text 'Некоторые смертельные баги по квестам, например этап с передачей 150 долларов милфе.  ' color '#fff' size 27 
                text ''
                text 'Убран русский текст в английской версии.  ' color '#fff' size 27 
                text ''
                text 'Сделан более плотный блюр на картинках в галереи сцен, чтобы не спойлерить сюжет.  ' color '#fff' size 27 
                text ''
                text 'Исправлен баг, который резко увеличивал число найденных "мешочков" до 100 в инвентаре.  ' color '#fff' size 27 
                text ''
                text 'Баг, при котором можно получить критическую ошибку, если закрыть меню компьютера перед просмотром порно.  ' color '#fff' size 27 
                text ''
                text 'В квесте, где нужно смотреть порно, мы сделали пометку text "НОЧЬЮ!"  ' color '#fff' size 27 
                text ''
                text 'Кое что по мелочи.  ' color '#fff' size 27 
                text ''
                text ''
                text 'Добавлено:  ' color '#fff' size 27 
                text 'Иконка для запускаемого файла.  ' color '#fff' size 27 
                text 'Эмоции в некоторых сценах для Кристи и Офицера.  ' color '#fff' size 27 
                text 'Система выбора СМС.  ' color '#fff' size 27 
                text ''
                text ''
                text '0.8.65 '  color '#ffae00' size 27 
                text ''
                
                text 'Исправления:  ' color '#fff' size 27 
                text ''
                text 'В ситуации, когда должны сработать два и более событий, '  color '#fff' size 27 
                text 'Игроку предоставляется выбор какое событие  ' color '#fff' size 27 
                text 'Проиграть первым. Следующее событие можно активировать  ' color '#fff' size 27 
                text 'только на следующий день.  ' color '#fff' size 27 
                text 'Надеюсь, это спасёт нас от смертельных багов!  ' color '#fff' size 27 
                text ''
                
                text ''
                text '    Баг с предметами, что замещали друг друга.  ' color '#fff' size 27 
                text ''
                text '    Баг с ночным квестом Кэт - сука, теперь ты никуда не денешься!  ' color '#fff' size 27 
                text ''
                text '    Баг с закрытием магазина, что выкидывал на улицу.  ' color '#fff' size 27 
                text ''
                text '    Баг с количеством получаемых закладок в парке.  ' color '#fff' size 27 
                text ''
                text '    Баг со штанами, которые есть, но которых нет.  ' color '#fff' size 27 
                text ''
                text '    Баг с абузом жопы Марины (можно было бесконечно смотреть под платье на кухне, получая репутацию).  ' color '#fff' size 27 
                text ''
                text '    Баг с вылетом ошибки в руте Кристи.  ' color '#fff' size 27 
                #text 'Баг со взломом двери в спальне Марины, который не позволял взламывать замок после 5 “эпизода”.
                text ''
                text '    Кое-где поправлен перевод.  ' color '#fff' size 27 
                text ''
                text ''
                text 'Андроид:  ' color '#fff' size 27 
                text '    Невидимые анимации теперь видимые. Приятного просмотра!  ' color '#fff' size 27 
                text ''
                text ''
                text ''
                text ''
                text ''