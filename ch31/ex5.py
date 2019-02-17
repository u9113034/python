#ex5.py
import turtle
    
def drawSignal(x, y):
    if x > 0 and y > 0:
        t.fillcolor('yellow')
        t.penup()
        t.setpos(x, y - 50)  # 設定繪圓起點
        t.begin_fill()
        t.circle(50)
        t.end_fill()
    elif x > 0 and y < 0:
        t.fillcolor('red')
        t.penup()
        t.setpos(x, y - 50)  # 設定繪圓起點
        t.begin_fill()
        t.circle(50)
        t.end_fill()
    elif x < 0 and y > 0:
        t.fillcolor('blue')
        t.penup()
        t.setpos(x, y - 50)  # 設定繪圓起點
        t.begin_fill()
        t.circle(50)
        t.end_fill()
    else:
        t.fillcolor('green')
        t.penup()
        t.setpos(x, y - 50)  # 設定繪圓起點
        t.begin_fill()
        t.circle(50)
        t.end_fill()

t = turtle.Pen()
t.setpos(-400, 0)
t.forward(800)
t.home()
t.right(90)
t.setpos(0,400)
t.forward(800)
t.home()
t.screen.onclick(drawSignal)
t.screen.mainloop()



