label biblio_22:
    # Description: Купить женские парики для Зудилы и Бубнилы.
    # Task: Активировать Зудилуи Бубнилу
    
    call show_bg_image_label
    show Jay Silence
    show Jay Silence:
        ypos 1085
        xalign .65
    show Bob Normal
    show Bob Normal:
        ypos 1085
        xalign .95
    show GG Normal
    show GG Normal at go_from_left(xxalign = .15)
    with my_dissolve
    
    "[gg]" "А вот и снова я. Заждались?"
    "Зудило" "Мы практически передумали. Ты вовремя."
    "[gg]" "Вот ваш реквизит. Одевайте и погнали."
    "Зудило" "Парики? Это и вся маскировка?"
    "[gg]" "Ага."
    "Зудило" "С тебя 50 баксов за услугу."
    "Бубнило" ".................."
    "Зудило" "Каждому."
    show GG Surprise with my_dissolve
    "[gg]" "Имейте совесть!"
    "Зудило" "Или так, или никак."
    show GG Chagrin with my_dissolve
    "[gg]" "Ладно, юный таланты."
    show GG Angry with my_dissolve
    "[gg]" "Но чтоб отыграли как следует! ПО СТАНИСЛОВСКОМУ!"
    "Бубнило" "................."
    "Зудило" "Говори прямо, чо делать надо? Какие психи? Кого отвлечь?"
    show GG Normal with my_dissolve
    "[gg]" "В библиотеке зверствуют какие-то сектанты."
    "[gg]" "Требует секс. И бесплатно. Поведутся только на женщин, готовых вступить с ними в половое сношение."
    "[gg]" "Трахаться с ними я не прошу."
    "Зудило" "Дебил, мы бы и не стали!"
    "[gg]" "Соблазните и уведите из библиотеки. Всё."
    "Зудило" "Плёвое дело, чувачело."
    "Бубнило" "................. .........."
    
    $ events.pop("biblio_22", 0)
    $ Event("biblio_23", location = "City_Library")
    
    jump main_interface_label
