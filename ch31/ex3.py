# ex3.py
import turtle, time
colorsList = ['green', 'yellow', 'red']
circlePos = [60, 160, 260]
sleepTime = [10, 3, 10]

t = turtle.Pen()
t.forward(110)
t.right(90)
t.forward(350)
t.right(90)
t.forward(110)
t.right(90)
t.forward(350)
t.speed(10)                             # 加速繪製圖形
t.ht()                                  # 隱藏海龜游標
for count in range(10):
    for i in range(0,3):
        t.penup()
        t.setpos(105, -circlePos[i%3])
        t.pendown()
        t.color('white', colorsList[i%3])   # 更改色彩
        t.begin_fill()                      # 開始填充
        t.circle(50)                        # 繪製左方圓
        t.end_fill()                        # 結束填充
        time.sleep(sleepTime[i%3])                       # 每隔3秒執行一次迴圈
        t.fillcolor('white')
        t.begin_fill()  # 開始填充
        t.circle(50)  # 繪製左方圓
        t.end_fill()  # 結束填充




