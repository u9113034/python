# ch7_36.py
buyers = [['James', 1030],              # 建立買家購買紀錄
           ['Curry', 893],
           ['Durant', 2050],
           ['Jordan', 990],
           ['David', 2110],
           ['Marx', 95050],
          ['Eryn', 5500],
          ['Tommy', 85100],
          ['Kent', 4157],
          ['Katie', 10000],
          ['Joan', 6000],
          ['Iori', 47781],
          ['Bruce', 4796],
          ['Grace', 15000],
          ['Sammy', 7808]]
goldbuyers = []                         # Gold買家串列
vipbuyers =[]                           # VIP買家串列
infinitebuyers=[]                       # Infinite買家串列
while buyers:                           # 執行買家分類迴圈分類完成迴圈才會結束
    index_buyer = buyers.pop()
    if index_buyer[1] >= 10000:          # 用1000圓執行買家分類條件
        infinitebuyers.append(index_buyer)
    elif index_buyer[1] >= 1000:
        vipbuyers.append(index_buyer)  # 加入VIP買家串列
    else:
        goldbuyers.append(index_buyer)  # 加入Gold買家串列
print("Infinite買家資料", infinitebuyers)
print("VIP 買家資料", vipbuyers)
print("Gold買家資料", goldbuyers)


