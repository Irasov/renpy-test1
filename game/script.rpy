init:

    $ left2 = Position(xalign=0.1, yalign=1.0)

    $ right2 = Position(xalign=0.6, yalign=1.0)



default name = "Вася"
default age = 20
default adult = False

default work_counter = 0

default money = 0




label start:

    scene mc_room

    show mc outside_normal at left

    "Данная игра распространяется только для 18+ игроков"

    menu:

        "Вам есть 18 лет?"

        "Да":

            $ adult = True

        "Почти":

            pass

        "Нет, но да":

            pass

    
    if adult == True:

        "Отлично. Тогда запускаю игру"

    else:

        "Я вынужден закрыть игру, так как вам нет 18 лет."

        $renpy.quit()

    "В одном далеком городе, жил обычный парень"

    "Жил он как и все остальные парни его возраста"

    show mc outside_normal at left

    mc "Привет, меня зовут [name]"

    mc "Мне [age] лет"

    mc "Шутка, хехе"

    menu:
        
        mc "На самом деле меня зовут..."

        "Петя":

            $ name = "Петя"

        "Игорь":

            $ name = "Игорь"

        "Павел":

            $ name = "Павел"

    mc "На самом деле меня зовут [name]"

    mc "..."

    mc "Как же я ненавижу начало дня"
    
    mc "Нужно идти завтракать"
    
    mc "Надеюсь, {u}мама{/u} что-то приготовила"

    play sound "steps.mp3"

    hide mc outside_normal with moveoutright


    scene kitchen with fade
    

    show mc outside_normal at left with moveinleft

    mc "Как вкусно пахнет"

    show mc outside_smile at left

    mc "Мама приготовила БОРЩ!!!!"


    show dad home_normal at right with moveinright:
        xzoom -1

    dad "Доброе утро, сынок"

    show mc outside_normal at left

    mc "Доброе утро, пап"

    dad "Как твои дела? Какие планы на сегодня?"

    mc "Нужно ехать в университет"

    dad "У тебя сегодня занятия?"

    mc "Да. Сегодня ведь среда"

    dad "Ну да, точно..."

    menu:

        dad "Во сколько вернешься?"

        "В 8":

            mc "Я буду дома в 8"

            dad "Отлично"

        "Не знаю":

            mc "Не знаю"

            mc "До 11 вернусь"

            dad "Ты уж постарайся"

    dad "Мама хотела сделать семейный ужин"

    mc "Тогда я вернусь пораньше"

    dad "Мама рассказывала, что ты устроился на работу"

    mc "На подработку скорее"

    mc "Хочу накопить себе на компьютер"

    dad "О, это здорово"

    dad "Ладно, ты завтракай, а я пойду..."

    hide dad home_normal at right with moveoutright

    "Вам нужно помочь главному герою купить компьютер"

    "Для этого заработайте 1000 рублей"

    "Когда у вас будет нужна сумма, опция покупки появится ниже"

    menu:
        
        mc "Так, чем заняться?"

        "Пойти на работу" if work_counter <= 1:

            hide mc outside_normal at left with moveoutright

            jump work

        "Пойти в комнату":

            hide mc outside_normal at left with moveoutright

            jump room

        "Выйти на улицу":

            hide mc outside_normal at left with moveoutright

            jump street



    "Конец игры"

    # This ends the game.

return














