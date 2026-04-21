init:
    $ left2 = Position(xalign=-0.2, yalign=1.0)
    $ right = Position(xalign=0.8, yalign=1.0)

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene mc_room

    "В одном далеком городе жил один парень"

    "Жил не тужил"

    show mc outside_normal at left2

    mc "Снова утро, нафиг надо"

    mc "Нужно идти завтракать"
    
    mc "Надеюсь, мама что-то приготовила"

    hide mc outside_normal with moveoutright

    scene kitchen with fade

    show mc outside_normal at left2 with moveinleft

    mc "Как вкусно пахнет"

    show mc outside_smile at left2

    mc "Мама приготовила БОРЩ!!!!"


    show dad home_normal at right with moveinright:
        xzoom -1

    dad "Доброе утро, сынок"

    show mc outside_normal at left2

    mc "Доброе утро, пап"


    return
