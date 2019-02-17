# ex2.py
print("判斷輸入字元類別")
ch = input("請輸入字元: ")
asc=ord(ch)
if ord(ch) >= ord("A") and ord(ch) <= ord("Z"):
    print("轉成小寫字元",chr(asc+32))
elif ord(ch) >= ord("a") and ord(ch) <= ord("z"):
    print("轉成大寫字元",chr(asc-32))
elif ord(ch) >= ord("0") and ord(ch) <= ord("9"):
    print("這是數字",chr(asc))
else:
    print("這是特殊字元")
    
