# ex8.py
import numpy as np
import matplotlib.pyplot as plt
from random import randint

def dice_generator(times, sides):
    ''' 處理隨機數 '''
    for i in range(times):              
        ranNum = randint(1, sides) + randint(1, sides) + randint(1, sides)          # 產生3個1-6隨機數
        dice.append(ranNum)
def dice_count(sides):
    '''計算1-6個出現次數'''
    for i in range(3, 19):
        frequency = dice.count(i)               # 計算i出現在dice串列的次數
        frequencies.append(frequency)
          
times = 1000                                     # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
frequencies = []                                # 儲存每一面骰子出現次數串列
dice_generator(times, sides)                    # 產生擲骰子的串列
dice_count(sides)                               # 將骰子串列轉成次數串列                          
x = np.arange(16)                              # 長條圖x軸座標
print(frequencies)
width = 0.35                                    # 長條圖寬度
plt.bar(x, frequencies, width, color='g')       # 繪製長條圖
plt.ylabel('Frequency')
plt.title('Test 1000 times')
plt.xticks(x, ('3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'))
plt.yticks(np.arange(0, 200, 15))
plt.show()

