#(a) 1+3+5+...n
n=int(input('input an odd number:'))
sum=0
for i in range(1,n,2):
    sum+=i
print(sum)
#(b) 1+2-3+...-(n-1)+n
n=int(input('input an even number:'))
sum=1
for i in range(2,n+1):
    if (i%2)==0 :
        sum+=i
    else:
        sum-=i
print(sum)
#(c) 1/n+2/n+...+n/n
sum=0
for i in range(1,n+1):
    sum+=i
print(sum/n)