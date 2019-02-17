# ch31_17.py
import turtle, time

# t = turtle.Pen()
# t.color('blue')
# print(t.screen.getshapes())             # 列印海龜游標字串
#
# for cursor in t.screen.getshapes():
#     t.shape(cursor)                     # 更改海龜游標
#     t.stamp()                           # 海龜游標蓋章
#     t.forward(30)

t=turtle.Turtle()
screen=t.getscreen()
screen.register_shape("giphy.gif")
t.penup()
t.shape("giphy.gif")
t.pencolor('black')
t.forward(100)
t.right(90)
time.sleep(2)
t.forward(40)
t.right(90)
time.sleep(2)
t.forward(40)
t.right(90)
time.sleep(2)
t.forward(40)
t.right(90)
time.sleep(3)