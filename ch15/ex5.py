# ch15_11.py
def division(x, y):
    try:                        # try - except指令
        ans = int(x) / int(y)
    except ZeroDivisionError:   # 除數為0使用
        print("除數為0發生")
    except TypeError:           # 資料型別錯誤
        print("使用字元做除法運算異常")
    except ValueError:
        print("輸入錯誤字元")
    else:
        return ans

while True:
    a=input('input a number:')
    b=input('input b number:')
    if (a=='q' or a=='Q') or (b=='q' or b=='Q'):
        break
    print(division(a,b))





