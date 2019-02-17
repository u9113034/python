# ch30_6.py
import datetime

xtime = datetime.datetime(2020, 1, 1, 0, 0, 0)
deltaTime = datetime.timedelta(days=100)
# timeNow = datetime.datetime.now()
# print("現在時間是 : ", timeNow)
# print("100天後是  : ", timeNow + deltaTime)
ytime = xtime - deltaTime
print("100天前是  : ", ytime.strftime('%m'),'月',ytime.strftime('%d'),'號')

