# ch13_14.py
import random           # 導入模組random

n = 1000
num_gap=[0,0,0,0,0,0,0,0,0,0]
for i in range(n):
    num=random.randint(1,100)
    if num >= 0 and num <= 10:
        num_gap[0] += 1
    elif num >= 11 and num <= 20:
        num_gap[1] += 1
    elif num >= 21 and num <= 30:
        num_gap[2] += 1
    elif num >= 31 and num <= 40:
        num_gap[3] += 1
    elif num >= 41 and num <= 50:
        num_gap[4] += 1
    elif num >= 51 and num <= 60:
        num_gap[5] += 1
    elif num >= 61 and num <= 70:
        num_gap[6] += 1
    elif num >= 71 and num <= 80:
        num_gap[7] += 1
    elif num >= 81 and num <= 90:
        num_gap[8] += 1
    else:
        num_gap[9] += 1

print(num_gap)