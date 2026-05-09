label room:

    scene mc_room

    show mc outside_normal at left with moveinleft

    #show screen show_money

    show screen show_money_button

    show screen info_show_popup
    
    menu:
    
        "Купить компьютер" if money >= 1000:

            mc "Наконец-то этот день настал!"

            mc "У меня хватает денег на то, чтобы купить компьютер"

            mc "Осталось только доехать до магазина, и..."

            hide mc outside_normal at left with moveoutright

            $ work_counter = 0

            "Поздравяю, вы успешно прошли игру"

            "Однако, впереди у вас еще много приключений"

            "Это только начало ;)"

            
        "Пойти на работу" if work_counter <= 1:

            hide mc outside_normal at left with moveoutright

            jump work

        "Пойти на кухню":

            hide mc outside_normal at left with moveoutright

            jump kitchen

        "Выйти на улицу":

            hide mc outside_normal at left with moveoutright

            jump street

        "Лечь спать":

            hide mc outside_normal at left with moveoutright

            $ work_counter = 0

            "На следующий день"

            "У главного героя [money] рублей"

            "Осталось накопить [1000-money] рублей"

            jump room


return