# ex2.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(0, 10, 500)           # 建立含500個元素的陣列
ypt1 = np.sin(xpt)                      # y陣列的變化
ypt2 = np.cos(xpt)
plt.scatter(xpt, ypt1, c=ypt1, cmap='cool') # 色彩映射表COOL
plt.scatter(xpt, ypt2, c=ypt2, cmap='hot')  # 色彩映射表HOT
plt.show()




