# ex6.py
answer = 30                 # 正確數字
guess = 0                   # 設定所猜數字的初始值
count=0                     # 猜的次數
while guess != answer:
    guess = int(input("請猜1-100間的數字 = "))
    if guess > answer:
        print("請猜小一點")
        count+=1
    elif guess < answer:
        print("請猜大一點")
        count += 1
    else:
        print("恭喜答對了")
        count += 1
        print("總共猜了%d次" %count)
