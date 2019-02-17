import pyautogui
#locateAllOnScreen()函数会寻找所有相似图片，返回一个生成器：
for i in pyautogui.locateAllOnScreen('Image 004.png'):
    print(i)
# list(pyautogui.locateAllOnScreen('pyautogui/123.png'))
#locateCenterOnScreen()函数会返回图片在屏幕上的中心XY轴坐标值：
# pyautogui.locateCenterOnScreen('pyautogui/123.png')