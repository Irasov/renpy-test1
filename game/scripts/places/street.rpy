label street:

    scene wife_home_outside_day

    show mc outside_normal at left with moveinleft
    
    
    menu:

        "Пойти на работу" if work_counter <= 1:

            hide mc outside_normal at left with moveoutright

            jump work

        "Пойти домой":

            hide mc outside_normal at left with moveoutright

            jump room


return