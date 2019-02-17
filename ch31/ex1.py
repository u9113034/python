import turtle
import numpy as np

def calc_angle(x_point_s,y_point_s,x_point_e,y_point_e):
    angle=0
    y_se= y_point_e-y_point_s
    x_se= x_point_e-x_point_s
    if x_se==0 and y_se>0:
        angle = 360
    if x_se==0 and y_se<0:
        angle = 180
    if y_se==0 and x_se>0:
        angle = 90
    if y_se==0 and x_se<0:
        angle = 270
    if x_se>0 and y_se>0:
       angle = np.arctan(y_se/x_se)*180/np.pi
    elif x_se<0 and y_se>0:
       angle = 360 + np.arctan(y_se/x_se)*180/np.pi
    elif x_se<0 and y_se<0:
       angle = 180 + np.arctan(y_se/x_se)*180/np.pi
    elif x_se>0 and y_se<0:
       angle = 180 + np.arctan(y_se/x_se)*180/np.pi
    t.penup()
    t.setpos(x_point_s,y_point_s)
    t.seth(angle)
    t.pendown()
    t.forward(np.sqrt(y_se**2+x_se**2))


t = turtle.Pen()
t.pencolor('blue')
calc_angle(0, 0, -200, -50)
t.screen.mainloop()