# ex4.py
cost=input("消費金額: ")
age = input("請輸入年齡: ")
cost=int(cost)
age = int(age)
ticket = 100
if age != 50 :
    if cost >= 100000:
        cost *= 0.9
        print("結價金額是: %d" % cost)
    elif (age >= 80000):
        cost *= 0.95
        print("結價金額是: %d" % cost)
    else:
        cost *= 0.98
        print("結價金額是: %d" % cost)
else :
    cost *= 0.95
    print("結價金額是: %d" % cost)