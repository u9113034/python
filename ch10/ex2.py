A_list=list(range(1,99,2))
B_list=[]
for num in range(100):
    for i in range(2,num):
        if num%i==0:
            break
        else:
            B_list.append(num)
            break
A=set(A_list)
B=set(B_list)
print('intersection=',A&B)
print('union=',A|B)
print('A-B=',A-B)
print('B-A=',B-A)
print('A-B對稱差集=',A.symmetric_difference(B))
print('B-A對稱差集=',B.symmetric_difference(A))