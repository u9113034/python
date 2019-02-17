# ch33_7.py
from tkinter import *
import pygame

def playmusic():                                        # 處理按撥放紐
    selection = var.get()                               # 獲得音樂選項
    if selection == '1':
        pygame.mixer.music.load('01. 奏 (かなで).mp3')         # 撥放選項1音樂
        pygame.mixer.music.play(-1)                     # 循環撥放
    if selection == '2':
        pygame.mixer.music.load('02. はなごのみ.mp3')      # 撥放選項2音樂
        pygame.mixer.music.play(-1)                     # 循環撥放
    if selection == '3':
        pygame.mixer.music.load('03. 中恵光城-さよならのコトバ.mp3')         # 撥放選項3音樂
        pygame.mixer.music.play(-1)                     # 循環撥放
    if selection == '4':
        pygame.mixer.music.load('04. 君がそばにいるように.mp3')         # 撥放選項3音樂
        pygame.mixer.music.play(-1)                     # 循環撥放
    if selection == '5':
        pygame.mixer.music.load('05. それは小さな光のような.mp3')         # 撥放選項3音樂
        pygame.mixer.music.play(-1)                     # 循環撥放
def stopmusic():                                        # 處理按結束紐
    pygame.mixer.music.stop()                           # 停止撥放此首mp3
def volumeup():
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.2)
def volumedown():
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.2)
def startmusic():
    pygame.mixer.music.unpause()
def pausemusic():
    pygame.mixer.music.pause()
    
# 建立mp3音樂選項鈕內容的串列
musics = [('01. 奏 (かなで).mp3', 1),                          # 音樂選單串列
          ('02. はなごのみ.mp3', 2),
          ('03. 中恵光城-さよならのコトバ.mp3', 3),
          ('04. 君がそばにいるように.mp3', 4),
          ('05. それは小さな光のような.mp3', 5)]

pygame.mixer.init()                                     # 最初化mixer

tk = Tk()
tk.geometry('550x250')                                  # 開啟視窗
tk.title('Mp3 Player')                                  # 建立視窗標題
mp3Label = Label(tk, text='\n我的Mp3 撥放程式')         # 視窗內標題
mp3Label.pack()
# 建立選項紐Radio button
var = StringVar()                                       # 設定以字串表示選單編號
var.set('1')                                            # 預設音樂是1
for music, num in musics:                               # 建立系列選項紐
    radioB = Radiobutton(tk, text=music, variable=var, value=num)
    radioB.pack()
# 建立按鈕Button
button1 = Button(tk, text='撥放', width=10, command=playmusic)    # 撥放mp3音樂
button1.place(x=150,y=170,anchor='nw')
button2 = Button(tk, text='暫停', width=10, command=pausemusic)
button2.place(x=250,y=170,anchor='nw')
button3 = Button(tk, text='恢復', width=10, command=startmusic)
button3.place(x=350,y=170,anchor='nw')
button4 = Button(tk, text='放大聲', width=10, command=volumeup)
button4.place(x=150,y=210,anchor='nw')
button5 = Button(tk, text='放小聲', width=10, command=volumedown)
button5.place(x=250,y=210,anchor='nw')
button6 = Button(tk, text='停止', width=10, command=stopmusic)    # 停止撥放mp3音樂
button6.place(x=350,y=210,anchor='nw')
mainloop()


