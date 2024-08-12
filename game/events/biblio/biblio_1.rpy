label biblio_1:
    # Description: Ознакомиться с “Кама-сутра».
    # Task: Активировать книгу в инвентаре
    
    call show_bg_image_label
    show GG Surprise
    show GG Surprise at go_from_left(xxalign = .15)
    with my_dissolve
    
    "[gg]" "Хм..."
    "[gg]" "Из книги выпала какая-то шпаргалка."
    "[gg]" "Это записка или просто закладка?"
    
    show screen give_item_screen(i_path+'items/ticket.png', _('Любовная записка'), _('Листочек с чьими-то записями.'))
    pause
    hide screen give_item_screen
    # Спрайт с записью
    # («Если я тебе понравилась, верни мне книгу в пятницу.»)
    show GG Think
    with my_dissolve
    
    "[gg]" "Понятия не имею, что за каракули здесь написаны."
    "[gg]" "Похоже на какой-тот шифр."
    "[gg]" "Спрошу и Игоря."

    $ add_to_inventory(name = 'Любовная записка')
    
    $ events.pop("biblio_1", 0)
    $ Event("biblio_2", location = "Igor", button_name=_("Узнать про записку"))
    
    jump main_interface_label
