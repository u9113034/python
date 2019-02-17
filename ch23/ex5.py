# ex5.py
import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8]                # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]           # data2線條
data3 = [1, 3, 6, 10, 15, 21, 28, 36]           # data3線條
data4 = [1, 7, 15, 26, 40, 57, 77, 100]         # data4線條

seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.subplot(2, 2, 1)
plt.plot(seq, data1, '-*')
plt.subplot(2, 2, 2)
plt.plot(seq, data2, '-o')
plt.subplot(2, 2, 3)
plt.plot(seq, data3, '-^')
plt.subplot(2, 2, 4)
plt.plot(seq, data4, '-+')
# plt.title("Test Chart", fontsize=24)
# plt.xlabel("x-Value", fontsize=14)
# plt.ylabel("y-Value", fontsize=14)
# plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()

