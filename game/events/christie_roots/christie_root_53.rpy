label christie_root_53:
    #Отправить Игорю ролик, где Кристи показывает стриптиз.
    #"ext" "Активировать СМС Игоря."
    
    $ descript_Christie = _("Отправить Игорю ролик, где Кристи показывает стриптиз.")
    if getattr(store, 'block_igor_position', False):


        $ descript_Christie_block_igor = _("Чтобы начать это задание нужно найти куда пропал Игорь...")


        $ Event('christie_root_53', 'GG_Room',  time = ['morning'], day_start = time.day_now + 1,)
        
        jump main_interface_label
    $ events.pop('christie_root_53', 0)
    call show_bg_image_label from _call_show_bg_image_label_224
    with my_dissolve
    show GG Think
    show GG Think at go_from_left(xxalign = .5)
    "[gg]" "Прежде чем отправлять Игорю видео со стриптизом Кристи, мне стоит вырезать кульминацию."
    
    "[gg]" "Слишком уж наш перфоманс зашёл далеко…"
    
    "[gg]" "Так, вроде удалил."

    $ sms_now = SmsBlock('Игорь', 'igor', "25", Jump('christie_root_53_1'))

    $ sms_now.add_sms(_('GG: Бро, всё готово!\n*отправка файла*'))
    
    $ sms_now.add_sms(_("TT: Окей."))
    $ sms_now.add_sms(_("TT: Приходи завтра\nутром в Парк."))
    $ sms_now.add_sms(_("TT: Верну «твой» телефон\nи заодно поведаю,\nчто получилось накопать."))
    $ sms_now.add_sms(_("GG: А сейчас почему\nне можешь рассказать?"))
    $ sms_now.add_sms(_("TT: Сейчас я\nсобираюсь подрочить."))
    $ sms_now.add_sms(_("GG: Ыыыыыыыыыыыы."))
    $ sms_now.add_sms(_("TT: Всё, бб."))
    $ sms_now.add_sms(_("GG: бб"))
    
    $ descript_Christie = _("Отправить Игорю Видео с Кристи.")

    #"ext" "//Mobile_SMS"

    jump main_interface_label

label christie_root_53_1:
    $ Hide('phone_sms_screen')()
    $ Hide('phone_contacts_screen')()
    $ Hide('phone_interface')()

    
    
    $ descript_Christie = _("Поговорить с Игорем в парке завтра Утром, узнав у него, смог он взломать телефон Маши или нет.")
   # $ christie_root_53_igor_fix = True

    # $ igor_position = {
    #         'morning'   : ('City_Park',  'igor_park'),
    #         'afternoon' : ('City_Park',  'igor_park'),
    #         'evening'   : ('None',       'None'),
    #         'night'     : ('None',       'None'),
            
    #         }


    call christie_root_try_to_del_descript_christie_block_igor from _call_christie_root_try_to_del_descript_christie_block_igor_8
    
    $ Event('christie_root_54', 'Igor', day_start = time.day_now + 1)

    jump main_interface_label