# ch14_13.py
import os

totalsizes = 0
print("列出D:\\Python\\ch14工作目錄的所有檔案")
for file in os.listdir('F:\\Book\\電腦書\\Python入門\\範例檔案\\ch14'):
    print(file)
    totalsizes += os.path.getsize(os.path.join('F:\\Book\\電腦書\\Python入門\\範例檔案\\ch14', file))

print("全部檔案大小是 = ", totalsizes)

    





      




