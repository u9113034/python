# ex5.py
hours=input("請輸入打工時數: ")
hours=int(hours)
if hours < 120 :
    paycheck=hours*150*0.8
elif hours==120 :
    paycheck=hours*150
elif hours > 120 and hours <= 150 :
    paycheck=hours*150*1.2
else :
    paycheck=hours*150*1.5
print("薪資為: ", int(paycheck))