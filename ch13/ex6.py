# ch13_17.py
import random                       # 導入模組random

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
while len(fruits):
    temp=random.choice(fruits)
    print(temp)
    fruits.remove(temp)



