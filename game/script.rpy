init:
    $ left2 = Position(xalign=-0.2, yalign=1.0)
    $ right = Position(xalign=0.8, yalign=1.0)

default name = "Вася"
default age = 20
default adult = False

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene mc_room

    play music "main_music.mp3" loop

    menu: 
        "Вам есть 18?"
        "да":
            $ adult = True
        "нет":
            pass
    if adult:
        "Отлично, играем!"
    else:
        "Извнин, но не сегодня!"
        $renpy.quit()

    "В одном далеком городе жил один парень"

    "Жил не тужил"

    show mc outside_normal at left2

    mc "Меня зовут [name]"

    mc "Мне [age] лет"

    mc "Шутка, хаха"

    menu: 
        mc "На самомом деле меня зовут..."

        "Петя":
            $ name = "Петя"

        "Вася":
            $ name = "Вася"

        "Димас":
            $ name = "Димас"

    mc "Мое настоящее имя [name]"

    mc "Снова утро, нафиг надо"

    mc "Нужно идти завтракать"
    
    mc "Надеюсь, мама что-то приготовила"

    play sound "steps.mp3"

    hide mc outside_normal with moveoutright

    scene kitchen with fade

    show mc outside_normal at left2 with moveinleft

    mc "Как вкусно пахнет"

    show mc outside_smile at left2

    mc "Мама приготовила БОРЩ!!!!"


    show dad home_normal at right with moveinright:
        xzoom -1

    dad "Доброе утро, {font=gui/fonts/Kurale.ttf}сынок{/font}"

    show mc outside_normal at left2

    mc "Доброе утро, пап"

    dad "Как твои дела? Какие планы на сегодня?"

    mc "Нужно ехать в университет"

    dad "У тебя сегодня занятия?"

    mc "Да. Сегодня ведь среда"

    dad "Ну да, точно..."

    menu:

        dad "Во сколько вернешься?"

        "В 8":

            call dial_1

        "Не знаю":

            call dial_2

    dad "Мама хотела сделать семейный ужин"   

    mc "Тогда я вернусь пораньше"




    return
