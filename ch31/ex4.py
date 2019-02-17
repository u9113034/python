# ch31_10.py
import turtle

t = turtle.Pen()
step = 5                # 每次增加距離
radius = 100
for r in range(50):
    t.circle(radius)         # 繪製圓
    radius-=1
    t.penup()           # 將筆提起
    t.forward(step)     # 移動海龜位置起繪點
    t.pendown()         # 將筆放下準備繪製

t.screen.mainloop()
