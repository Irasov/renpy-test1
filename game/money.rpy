transform top_bottom_30px:
  ypos 200

  linear 0.5 ypos 170

  pause 0.3

  linear 0.5 ypos 200

  repeat

transform left_right:

  xpos 1920

  linear 0.2 xpos 1920-150

  pause 1.6

  linear 0.2 xpos 1920

  linear 0.6 ypos 0

  repeat


transform alpha_anim:

  alpha 1.0

  linear 1.0 alpha 0.2

  linear 1.0 alpha 0.2

  repeat

transform shrink:

  zoom 0.5


screen show_money:

  hbox xpos 10 ypos 180:

    spacing 10  

    text "[money]"  yalign 0.5 color "#00FF00" outlines [(3, "#000000", 0, 0)]

    add 'images/money.png'
  
  add "images/money.png" xalign 0.5 ypos 200 yanchor 1.0 at top_bottom_30px

default show_money_enable = 0

screen info_show_popup:

  add 'images/popup1.png' xpos 1920 ypos 30 at left_right

  timer 2.0 action Hide('info_show_popup')

screen show_money_button:

  vbox xpos 10 ypos 10:

    textbutton "{i}Вернуться в комнату" action Jump('room') text_color "#00FF00" text_hover_color "#fff" text_size 42
    if show_money_enable == 0:
      textbutton "{i}Показать деньги" text_color "#00FF00" text_hover_color "#fff" text_size 42 action [
        SetVariable('show_money_enable', 1),
        Show('show_money')
      ] at alpha_anim
    else:
      textbutton "{i}Скрыть деньги" text_color "#00FF00" text_hover_color "#fff" text_size 42 action [
        SetVariable('show_money_enable', 0),
        Hide('show_money')
      ]



screen test:

  modal True

  add 'images/btn-money.png' yalign 0.5 xalign 0.3