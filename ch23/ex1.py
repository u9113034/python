# ex1.py
import matplotlib.pyplot as plt

Benz = [3367, 4120, 5539, 6020, 6620]               # Benz線條
BMW = [4000, 3590, 4423, 4900, 4590]                # BMW線條
Lexus = [5200, 4930, 5350, 6200, 6930]              # Lexus線條

seq = [2018, 2019, 2020, 2021, 2022]                # 年度
plt.xticks(seq)                         # 設定x軸刻度
plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   
plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()


