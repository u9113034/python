# ex1.py
import pyautogui
import time

print('按Ctrl-C 可以中斷本程式')
try:
    screenImage = pyautogui.screenshot()
    while True:
        xloc, yloc = pyautogui.position()       # 獲得滑鼠游標位置
        xylocStr = "x= " + str(xloc).rjust(4) + " y= " + str(yloc).rjust(4)
        xylocPixel = screenImage.getpixel((xloc, yloc))
        print(' '*50, end='\r', flush=True)
        print(xylocStr+' '+str(xylocPixel), end='\r', flush=True)   # 設定同一行最左邊輸出
        # print(xylocStr + ' ' + str(xylocPixel), end='')
        # print('\b'*len(xylocStr + ' ' + str(xylocPixel)), end='', flush=True)  # 設定同一行最左邊輸出
        time.sleep(0.5)
except KeyboardInterrupt:
    print('\nBye')


