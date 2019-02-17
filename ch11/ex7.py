# ch11_26.py
def fibonacci(n):
    # 計算費式數列
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


value = 3
print(value, " 的階乘結果是 = ", fibonacci(value))
value = 9
print(value, " 的階乘結果是 = ", fibonacci(value))
