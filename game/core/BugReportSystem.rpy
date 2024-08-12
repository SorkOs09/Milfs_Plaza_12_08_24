image bg_frame = Frame("interface/bg_frame.png", Borders(50, 50, 50, 50))

image bg_frame_size_0 = Frame(Transform("interface/bg_frame.png", zoom = .5), Borders(26, 26, 26, 26))

image bg_frame_size_1 = Frame(Transform("interface/bg_frame.png", zoom = .25), Borders(13, 13, 13, 13))


image bg_frame_size_2 = Frame(Transform("interface/bg_frame.png", zoom = .15), Borders(9, 9, 9, 9))


image bg_red_frame = AlphaMask(Solid("#F00"), 'bg_frame')
init python:

    import socket
    bug_report_text = ""
    def change_bug_report_text(value=""):
        global bug_report_text
        bug_report_text = str(value)

    # _alphabet = {
    # 'а':'a',
    # 'б':'b',
    # 'в':'v',
    # 'г':'g',
    # 'д':'d',
    # 'е':'e',
    # 'ё':'e',
    # 'ж':'zh',
    # 'з':'z',
    # 'и':'i',
    # 'й':'yo',
    # 'к':'k',
    # 'л':'l',
    # 'м':'m',
    # 'н':'n',
    # 'о':'o',
    # 'п':'p',
    # 'р':'r',
    # 'с':'s',
    # 'т':'t',
    # 'у':'u',
    # 'ф':'f',
    # 'х':'x',
    # 'ц':'c',
    # 'ч':'ch',
    # 'ш':'sh',
    # 'щ':'sh',
    # 'ъ':'[',
    # 'ы':'i',
    # 'ь':']',
    # 'э':'a',
    # 'ю':'you',
    # 'я':'ya'
    # }
    _socket_now = None
    bug_report_sended = False
    bug_report_id     = None
    def send_bug_report_descript(_text, need_close = True, file_type = "___descript___"):
        global _alphabet, bug_report_sended
        try:
            #ip = "91.223.123.9"
            #ip = "127.0.0.1"
            
            ip   = "185.198.164.69"
            port = 9999
            
            if store.bug_report_id is None:
                store.bug_report_id = create_bug_report_id()

            # создаём сокет для подключения
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((ip,port))
            sock.settimeout(None)

            # запрашиваем имя файла и отправляем серверу
            # f_name = os.path.join(renpy.loadsave.location.locations[0].directory, file + ".save")

            # sock.send((bytes(f_name, encoding = 'UTF-8')))

            # открываем файл в режиме байтового чтения
            #f = open (f_name, "rb")
            #from io import StringIO

            # f = StringIO()
            # f.write(str(text))
            # print(f.getvalue())
            #print >>output, 'Second line.'

            # Retrieve file contents -- this will be
            # 'First line.\nSecond line.\n'
            #contents = output.getvalue()

            # Close object and discard memory buffer --
            # .getvalue() will now raise an exception.
            #output.close()
            # читаем строку

            #buf.encode('utf8')


            #sock.send(str(code).encode('utf-8'))



            
            sock.send(store.bug_report_id.encode('utf-8'))
            sock.send(file_type.encode('utf-8'))

            #sock.send(dvll.encode('utf-8'))
            if _text:

                _text = str(_text)
                
                # for i in _alphabet:
                #     if i in _text:
                #         _text = _text.replace(i, _alphabet[i])
                #     if i.upper() in _text:
                #         _text = _text.replace(i.upper(), _alphabet[i].upper())
                #sock.send("\n".encode('utf-8'))
                _text = str(_text)
                
                sock.send(_text.encode('utf-8'))
            # l = f.read(1024)

            # while (l):
            #     # отправляем строку на сервер
            #     sock.send(l)
            #     l = f.read(1024)

            # f.close()
            if need_close:
                sock.close()
            else:
                return sock

            bug_report_sended = True
        except:
            
            bug_report_sended = False
            store.bug_report_id     = None

    def send_bug_report_file(file):
        global bug_report_sended

        #try:
        # запрашиваем имя файла и отправляем серверу
        f_name = str(os.path.join(renpy.loadsave.location.locations[0].directory, file + renpy.savegame_suffix))

        
        sock = send_bug_report_descript(None, False, file_type = "___save___")
        

        # открываем файл в режиме байтового чтения
        f = open (f_name, "rb")

        # читаем строку
        l = f.read(1024)

        while (l):
            # отправляем строку на сервер
            sock.send(l)
            l = f.read(1024)

        f.close()
        sock.close()
        
        bug_report_sended = True
        #except:
        #    bug_report_sended = False
    
        store.bug_report_id   = None
    
    def create_bug_report_id():

        now  = datetime.datetime.now()
        
        return now.strftime("%d_%m_%Y_%H_%M") + "_"+ str(now.microsecond)


    test_ggg = None
style bug_report_input:
    color "#000"



screen bug_report_screen:
    zorder 2000
    image '#000a'
    default stage  = 0
    default save_to_send = None

    default code = None

    default send_timer = 0


    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    if stage == 0:
        imagebutton:
            idle  "#000a"
            hover "#000a"
            action Hide("bug_report_screen")
    elif stage == 1:
        imagebutton:
            idle  "#000a"
            hover "#000a"
            action SetScreenVariable("stage", 0)
    else:
        if send_timer < 6:
            imagebutton:
                idle  "#000a"
                hover "#000a"
                action NullAction()
        else:
            imagebutton:
                idle  "#000a"
                hover "#000a"
                action SetVariable('bug_report_text', ''), Hide("bug_report_screen")
 #   textbutton "?!!!" action SetVariable('test_ggg', renpy.get_screen("bug_report_screen"))

    viewport:
        xalign .5
        yalign .5
        xmaximum 1400
        ymaximum 950
        image AlphaMask(Solid("#82c6b5"), 'bg_frame')
        imagebutton:
            idle  '#0000'
            hover '#0000'
            action NullAction()
        if stage == 0:
            text __("Максимально подробно опишите свою проблему"): 
                font 'fonts/mini_game.ttf' outlines [(3, '#000c', 0, 0)] 
                xalign .5 
                ypos 10
            viewport:
                xmaximum 1000
                ymaximum 800
                image AlphaMask(Solid("#d0c9c6"), 'bg_frame')
                xalign .5 ypos 70
                viewport:
                    xalign .5 yalign .5
                    xmaximum 900
                    ymaximum 750
                    add Input(default = bug_report_text, 
                    allow = u' 1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"|/@#$%^&*:;][,.?!=-+()' + u"'",
                    changed = change_bug_report_text, style = "bug_report_input")
            

            imagebutton:
                
                idle Text(__('{i}Далее...{/i}'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])
                hover Text(__('{i}Далее...{/i}'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])

                yanchor .5
                xalign .96
                if renpy.android:
                    yalign .04
                else:
                    yalign .96
                at PulseButtonXzoom09
                action SetScreenVariable("stage", 1)

        elif stage == 1:

            fixed:



                order_reverse True


                text __("Выберите сейв-файл с багом"): 
                    font 'fonts/mini_game.ttf' outlines [(3, '#000c', 0, 0)] 
                    xalign .5 
                    ypos 50
                    size 50

                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"

                    xalign 0.5
                    yalign 0.5

                    spacing gui.slot_spacing

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):

                        $ slot = i + 1
                        # viewport:
                        #     xmaximum 400
                        #     ymaximum 230
                        #     image '#000a'
                        $ _file_time = FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot"))
                        button:
                            if _file_time != "empty slot":
                                action SetScreenVariable("save_to_send", str(persistent._file_page) + "-" + str(slot))
                            else:
                                action NullAction()

                            has vbox
                            if str(save_to_send) == str(persistent._file_page) + "-" + str(slot):
                                add Composite((config.thumbnail_width, config.thumbnail_height), 
                                    (0, 0), FileScreenshot(slot),
                                    (0, 0), Solid("#fffb"),
                                    
                                    )


                                xalign 0.5
                            else:

                                add FileScreenshot(slot) xalign 0.5

                            text _file_time:
                                style "slot_time_text"
                                color "#fff"
                                font 'fonts/mini_game.ttf' 
                                outlines [(3, '#000c', 0, 0)] 

                            text FileSaveName(slot):
                                style "slot_name_text"
                                color "#fff"
                                font 'fonts/mini_game.ttf' 
                                outlines [(3, '#000c', 0, 0)] 

                            

                hbox:
                    style_prefix "page"

                    xalign 0.5
                    yalign .95

                    spacing gui.page_spacing

                    textbutton _("<") text_color "#fff" text_font 'fonts/mini_game.ttf' text_outlines [(3, '#000c', 0, 0)]  action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") text_color "#fff" text_font 'fonts/mini_game.ttf' text_outlines [(3, '#000c', 0, 0)] action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") text_color "#fff" text_font 'fonts/mini_game.ttf' text_outlines [(3, '#000c', 0, 0)] action FilePage("quick")


                    for page in range(1, 10):
                        textbutton "[page]": 
                            text_idle_color     "#fff" 
                            text_hover_color    "#fffd"
                            text_selected_color "#fffa" 

                            text_font 'fonts/mini_game.ttf' 
                            text_outlines [(3, '#000c', 0, 0)] 
                            action FilePage(page)

                    textbutton _(">") text_color "#fff" text_font 'fonts/mini_game.ttf' text_outlines [(3, '#000c', 0, 0)]  action FilePageNext()

            if save_to_send:
                imagebutton:
                    
                    idle Text(__('{i}Далее...{/i}'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])
                    hover Text(__('{i}Далее...{/i}'), font = 'fonts/mini_game.ttf', outlines = [(3, '#000c', 0, 0)])

                    yanchor .5
                    xalign .96
                    if renpy.android:
                        yalign .04
                    else:
                        yalign .96
                    at PulseButtonXzoom09
                    action SetScreenVariable("stage", 2)


                
        else:
            #text str(bug_report_sended) xalign .5
            if send_timer < 6:
                #timer 3 action Function(send_bug_report_file, save_to_send, code)
                if send_timer == 1:
                    timer 1 action [
                    Function(send_bug_report_descript, bug_report_text),
                    SetScreenVariable("send_timer", send_timer+1), 
                    ]
                elif send_timer == 3:
                    timer 1 action [
                    Function(send_bug_report_file, save_to_send),
                    SetScreenVariable("send_timer", send_timer+1), 
                    ]
                else:
                    timer 1 repeat True action [
                    SetScreenVariable("send_timer", send_timer+1), 
                    ]

                hbox:
                    xalign .5 
                    yalign .5
                    text __("Отправка "): 
                        font 'fonts/mini_game.ttf' outlines [(3, '#000c', 0, 0)] 
                        size 50
                    for i in range(3):
                        text ".":
                            size 50 font 'fonts/mini_game.ttf' outlines [(3, '#000c', 0, 0)] 
                            at transform:
                                easein .5+i/10 alpha 1.0
                                easeout .5+i/10 alpha .0
                                repeat
            else:
                if bug_report_sended:
                 
                    text __("Успешно! Спасибо за репорт."): 
                        font 'fonts/mini_game.ttf' 
                        outlines [(3, '#000c', 0, 0)] 
                        size 50
                        xalign .5
                        yalign .5
                    
                else:
                    text __("Что-то пошло не так. Попробуйте повторить позднее."):
                        font 'fonts/mini_game.ttf' 
                        outlines [(3, '#000c', 0, 0)] 
                        size 50
                        xalign .5
                        yalign .5
                
                    
                