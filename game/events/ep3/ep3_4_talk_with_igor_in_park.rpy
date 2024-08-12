label ep3_4_talk_with_igor_in_park:

    $ events.pop('ep3_4_talk_with_igor_in_park', 0)
    call show_bg_image_label from _call_show_bg_image_label_16
    call show_additional_images_label from _call_show_additional_images_label_13

    with Dissolve(.5)

    show GG Normal
    show GG Normal:
        xalign .32
        ypos 1085
        zoom 1.0-0.035
    show Igor Normal
    show Igor Normal:
        xalign .85
        ypos 1085
        zoom 1.0-0.035
    with Dissolve(.5)


    "[gg]" "Как успехи? "
    show Igor Angry
    "Игорь" "Слышь, ревизор, ещё один такой вопрос, и об этом тебя будет спрашивать врач-ортопед."
    show GG Smile
    "[gg]" "Ладно-ладно. Я с добрыми новостями."


    show Igor Normal
    "Игорь" "С этого и нужно было начинать. "
    show GG Normal
    "[gg]" "Только давай без нервов, выслушай, а потом уже рви волосы на голове. Окей?"
    show Igor Ok
    "Игорь" "Не тяни кота за яйца."
    show GG Normal
    "[gg]" "Короче! "
    show GG Surprise
    "[gg]" "На днях я обнаружил дома сейф! Понимаешь? Настоящий сейф!! Он оказался в комнате Марины, за одной из картин над кроватью. "

    show GG Normal
    "[gg]" "Марина сказала, что у неё имеются кое-какие сбережения. Не хочу вдаваться в контекст разговора, но поверь мне, там наверняка достаточно денег, чтобы мы расплатились с долгами."



    show GG Normal
    "[gg]" "Зная своего брата, он бы точно не оставил Марину в бедности. Можешь не сомневаться. "


    show GG Normal
    "[gg]" "Я понятия не имею, как его открыть и где взять пароль. Важно только одно – там деньги, которые спасут наши задницы."
    show GG Normal
    "[gg]" "Расплатимся со Жлобом, свобода! Понимаешь?"
    show GG Angry
    "[gg]" "А дальше мы приложим все усилия!.. Слышишь? Все усилия! Чтобы заработать всю сумму, которую мы одолжили у Марины. Нужно будет вернуть эти деньги. Всё до копейки."

    show GG Normal
    "[gg]" "Вот такой план."
    show GG Normal
    "[gg]" "Ну? Почему молчишь?"
    show Igor Troll
    "Игорь" "Ждал, пока ты заткнёшься. "
    show Igor Normal
    "Игорь" "Из всего услышанного меня волнует только одно. Что ты делал в спальне своей подруги?"

    show GG Embarrassment
    "[gg]" "Ч-что? Я?.."
    show GG Laughs
    "[gg]" "Помогал прибираться, ясное дело. Ты ж знаешь, как это бывает, когда живёшь с подругой? Бытовуха, рутина…"

    show Igor Troll
    "Игорь" "Бро, я знаю тебя всю жизнь. Ты палец об палец не ударишь для наведения порядка дома."
    show GG Angry
    "[gg]" "Что за дурацкие вопросы? Какая вообще разница? Если тебе не интересно, я ухожу. "
    show Igor Normal
    "Игорь" "Ладно, постой. "
    show GG Normal

    show Igor Normal
    "Игорь" "Давай думать, что следует предпринять. "
    show GG Normal
    "[gg]" "Вот и думай. Я нашёл сейф, а ты включай мозги."
    show Igor Normal
    "Игорь" "По твоему я кто? «Настоящий Маккой»? "
    show Igor Ok
    "Игорь" "Как выглядит твой сейф? "
    show GG Normal
    "[gg]" "Обычный кнопочный сейф."
    show Igor Ok
    "Игорь" "Что ж, это упрощает задачу."
    show GG Normal
    "[gg]" "…?"
    show Igor Normal
    "Игорь" "Предлагаю начать с простого и выяснить, какой у него пароль. Скорее всего там что-то элементарное"
    show Igor Normal
    "Игорь" "В крайнем случае твоего брата. Может, какой-то знаменательный день. "

    show Igor Normal
    "Игорь" "Есть такой день?"
    show GG Surprise
    "[gg]" "Не знаю."
    show GG Normal
    "[gg]" ".."
    show Igor Normal
    "Игорь" "Окей, не страшно. Пока попробуй ваши дни рождения. Кстати, когда родилась Марина? "

    show GG Surprise
    "[gg]" "Эм… Не помню…"
    show Igor Normal
    "Игорь" "Ты не помнишь, какого числа родилась твоя подруга?!"

    show GG Embarrassment
    "[gg]" "…."
    show Igor Angry
    "Игорь" "Придурок."
    show GG Embarrassment
    "[gg]" "Справедливо."
    show Igor Angry
    "Игорь" "Короче! Твоя задача, в кротчайшие сроки выяснить дату рождения Марины и попробовать вбить эти цифры в код сейфа."

    show GG Normal
    "[gg]" "Понял, сделаю! Уже бегу!"
    show Igor Ok
    "Игорь" "Ты свою-то дату рождения помнишь?"
    show GG Normal
    "[gg]" "Свою помню."
    show Igor Ok
    "Игорь" "Всё равно придурок."
    show GG Angry
    "[gg]" "Эй!.."
    show Igor Normal
    "Игорь" "Вали уже. "
    show GG Normal
    "[gg]" "Пошёл в задницу!"
    #$ block_change_milf_position = False
    $ descript = _('Если я спрошу о Дне Рождении Марину, она наверняка обидится. Не хочу её огорчать. Снова. Узнаю эту информацию у Кристи, она точно помнит.')

    $ Event('ep3_milf_11', 'Christie')

    $ location_now = 'City_Park'


    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
