screen show_money:

  hbox xpos 10 ypos 180:

    spacing 10  

    text "[money]"  yalign 0.5 color "#00FF00" outlines [(3, "#000000", 0, 0)]

    add 'images/money.png'

default show_money_enable = 0

screen show_money_button:

  vbox xpos 10 ypos 10:

    textbutton "{i}Вернуться в комнату" action Jump('room') text_color "#00FF00" text_hover_color "#fff" text_size 42
    if show_money_enable == 0:
      textbutton "{i}Показать деньги" text_color "#00FF00" text_hover_color "#fff" text_size 42 action [
        SetVariable('show_money_enable', 1),
        Show('show_money')
      ]
    else:
      textbutton "{i}Скрыть деньги" text_color "#00FF00" text_hover_color "#fff" text_size 42 action [
        SetVariable('show_money_enable', 0),
        Hide('show_money')
      ]



screen test:

  modal True

  add 'images/btn-money.png' yalign 0.5 xalign 0.3