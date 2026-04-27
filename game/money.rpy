screen show_money:

  hbox xpos 10 ypos 180:

    spacing 10  

    text "[money]"  yalign 0.5 color "#00FF00" outlines [(3, "#000000", 0, 0)]

    add 'images/money.png'

default show_money_enable = 0

transform btn_hover:
  on hover:
    linear 0.2 matrixcolor BrightnessMatrix(0.2)
  on idle:
    linear 0.2 matrixcolor BrightnessMatrix(0.0)

screen show_money_button:

  vbox xpos 10 ypos 10:

    textbutton "{i}Вернуться в комнату" action Jump('room') text_color "#00FF00" text_hover_color "#fff" text_size 42
    if show_money_enable == 0:
      imagebutton:
        idle 'images/btn-money.png'
        hover 'images/btn-money.png' at btn_hover
        #im.MatrixColor('images/btn-money.png', im.matrix.brightness(0.3))
        action [
          SetVariable('show_money_enable', 1),
          Show('show_money')
        ]
    else:
      imagebutton:
        idle 'images/btn-money.png'
        hover 'images/btn-money.png' at btn_hover
        #im.MatrixColor('images/btn-money.png', im.matrix.brightness(0.3))
        action [
          SetVariable('show_money_enable', 0),
          Hide('show_money')
        ]

screen test:

  modal True

  imagebutton xpos 490 ypos 450:
    idle 'images/btn-money.png'
    hover 'images/btn-money.png' at btn_hover
    action [
      Hide('test'),
      Jump('room')
    ]