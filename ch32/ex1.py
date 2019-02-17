# ex1.py
from tkinter import *
from random import *
import time

tk = Tk()
tk.title('Racing Game')
tk.wm_attributes('-topmost', 1)
canvas= Canvas(tk, width=500, height=250)
canvas.pack()
id1 = canvas.create_oval(10,50,60,100,fill='yellow') # 電腦
id2 = canvas.create_oval(10,150,60,200,fill='aqua')  # 我
doChi = input('1.Yello or 2.Aqua WIN? (請輸入1或2)')
for x in range(0, 100):
    if randint(1,100) > 60:
        canvas.move(id2, 5, 0)  # id2 x軸移動5像素, y軸移動0像素
    else:
        canvas.move(id1, 5, 0)  # id1 x軸移動5像素, y軸移動0像素    
    tk.update()                 # 強制tkinter重繪
    time.sleep(0.05)
id1Loc = canvas.coords(id1)
id2Loc = canvas.coords(id2)
if id1Loc[2] > id2Loc[2]:
    print('電腦贏了')
else:
    print('你贏了')
