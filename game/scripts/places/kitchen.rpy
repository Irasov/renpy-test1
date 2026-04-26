label kitchen:

    scene kitchen

    show mc outside_normal at left with moveinleft
    
    
    menu:

        "Пойти на работу" if work_counter <= 1:

            hide mc outside_normal at left with moveoutright

            jump work

        "Пойти в комнату":

            hide mc outside_normal at left with moveoutright

            jump room

        "Выйти на улицу":

            hide mc outside_normal at left with moveoutright

            jump street


return