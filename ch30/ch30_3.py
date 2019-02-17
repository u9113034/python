# ch30_3.py
import datetime

timeStop = datetime.datetime(2018, 4, 29, 16, 4, 0)
while datetime.datetime.now() < timeStop:
    print("program is sleeping.", end="")
print("Wake up")






