# ch13_16.py
import random                       # 導入模組random

cash = 500
min, max = 1, 100                   # 隨機數最小與最大值設定
winPercent = int(input("請輸入莊家贏的比率(0-100)之間 :"))

while True:
    print("猜大小遊戲: L或l表示大,  S或s表示小, Q或q則程式結束")
    print(cash)
    customerNum = input("= ")       # 讀取玩家輸入
    if cash <= 0:    # 若壽碼低於0
        break                                       # 程式結束
    num = random.randint(min, max)  # 產生是否讓玩家答對的隨機數
    if num > winPercent:            # 隨機數在81-100間回應玩家猜對
        print("恭喜!答對了\n")
        cash += 100
    else:                           # 隨機數在1-80間回應玩家猜錯
        print("答錯了!請再試一次\n")
        cash -= 100




