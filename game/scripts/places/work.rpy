label work:

    scene work_pizza

    #show screen test

    #hide window

    #$renpy.pause()

    show screen show_money

    show rick work_normal at right:
        xzoom -1

    show mc outside_normal at left with moveinleft

    rick "А вот и ты"

    rick "Ну что, готов поработать?"

    mc "Да, вроде как..."

    rick "Тогда приступаем"

    jump work2

return



label work2:

    menu:

        "Работать в пол силы (+100 рублей)":

            hide rick work_normal at right with moveoutright

            hide mc outside_normal at left with moveoutright

            "Какое-то время спустя..."

            show rick work_normal at right with moveinleft:
                xzoom -1

            show mc outside_normal at left with moveinleft

            $ renpy.notify("+100 рублей")

            mc "Я немного устал..."

            rick "Неплохо поработали. Но можно лучше"

            $ money += 100

        "Работать на полную (+200 рублей)":

            hide rick work_normal at right with moveoutright

            hide mc outside_normal at left with moveoutright

            "Какое-то время спустя..."

            show rick work_normal at right with moveinleft:
                xzoom -1

            show mc outside_normal at left with moveinleft

            $ renpy.notify("+200 рублей")

            mc "Я вырубаюсь от усталости"

            rick "Хорошо поработали. Нужно продолжать в том же темпе"

            $ money += 200






    if work_counter <= 1:

        $ work_counter += 1

        rick "Готов еще поработать?"

        rick "Время у нас еще есть"

        jump work2


    else:

        rick "На сегодня работа закончена"

        rick "Приходи завтра"

        jump street


return