# 天穹的自動按鍵腳本 跑活動用
import pyautogui, time

def giveEnergy(xyTuple):
    pyautogui.click(pyautogui.center(xyTuple))  # hai
    time.sleep(0.5)
    xyTuple = pyautogui.locateOnScreen('Image 003.png')  # potion
    pyautogui.click(pyautogui.center(xyTuple))  # 找到位置並按下滑鼠
    time.sleep(0.5)
    xyTuple = pyautogui.locateOnScreen('Image 004.png')  # hai
    pyautogui.click(pyautogui.center(xyTuple))  # 找到位置並按下滑鼠
    time.sleep(1)
    xyTuple = pyautogui.locateOnScreen('Image 005.png')  # hai
    pyautogui.click(pyautogui.center(xyTuple))  # 找到位置並按下滑鼠
    time.sleep(0.5)
    pyautogui.moveTo(1529, 504)
    pyautogui.click()

count=25
while count != 0:
    xyTuple=()
    time.sleep(3)
    while True:
        pyautogui.moveTo(1451, 580)
        pyautogui.click()
        time.sleep(1)
        xyTuple = pyautogui.locateOnScreen('Image 002.png')  # 沒能量了
        if xyTuple is not None:
            giveEnergy(xyTuple)
            break
        else:
            break

    time.sleep(0.5)
    xyTuple = pyautogui.locateOnScreen('step1.png')  # 選擇第30關
    if xyTuple is not None:
        pyautogui.click(pyautogui.center(xyTuple))     #找到位置並按下滑鼠
    time.sleep(0.5)
    xyTuple=pyautogui.locateOnScreen('step2.png')  #選擇朋友
    pyautogui.click(pyautogui.center(xyTuple))     #找到位置並按下滑鼠
    time.sleep(0.5)
    xyTuple=pyautogui.locateOnScreen('step3.png')  #QUEST出發
    pyautogui.click(pyautogui.center(xyTuple))     #找到位置並按下滑鼠

    while True:
         time.sleep(3)
         xyTuple=pyautogui.locateOnScreen('step5.png')  #AUTO
         if xyTuple is not None:
             pyautogui.click(pyautogui.center(xyTuple))     #找到位置並按下滑鼠
             break

    time.sleep(0.5)
    xyTuple=pyautogui.locateOnScreen('step4.png')  #LB
    pyautogui.click(pyautogui.center(xyTuple))     #找到位置並按下滑鼠

    while True:
        time.sleep(5)
        xyTuple=pyautogui.locateOnScreen('step6.png')  #離開戰鬥
        if xyTuple is not None:
            pyautogui.click(pyautogui.center(xyTuple))     #找到位置並按下滑鼠
            break
    while True:
        time.sleep(3)
        xyTuple=pyautogui.locateOnScreen('step7.png')  #RESULT
        if xyTuple is not None:
            pyautogui.click(pyautogui.center(xyTuple))     #找到位置並按下滑鼠
        xyTuple = pyautogui.locateOnScreen('step1.png')  # 選擇第30關
        if xyTuple is not None:
            break

    time.sleep(0.5)
    # xyTuple=pyautogui.locateOnScreen('step8.png')  #確定
    # pyautogui.click(pyautogui.center(xyTuple))     #找到位置並按下滑鼠
    count-=1