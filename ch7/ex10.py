n=int(input('請輸入n值='))
m=int(input('請輸入m值='))
sum=0
if m>n:
    for i in range(n,m+1):
        sum+=i
    print(sum)
else:
    print("請輸入m大於n的值")