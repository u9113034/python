# ch28_19.py
import pyautogui

screenImage = pyautogui.screenshot()
x, y = 30, 30
print(screenImage.getpixel((x,y)))


