# ch18_10.py

secretcode = '899998'                                      # 設定密碼
codeNotFound = True                                     # 尚未找到密碼為True
for i1 in range(0, 10):                                 # 第一位數
    if codeNotFound:            # 檢查是否找到沒有找到才會往下執行
        for i2 in range(0, 10):                         # 第二位數
            if codeNotFound:    # 檢查是否找到沒有找到才會往下執行
                for i3 in range(0, 10):                 # 第三位數
                    if codeNotFound:  # 檢查是否找到沒有找到才會往下執行
                        for i4 in range(0, 10):         # 第四位數
                            if codeNotFound:  # 檢查是否找到沒有找到才會往下執行
                                for i5 in range(0, 10):  # 第五位數
                                    if codeNotFound:  # 檢查是否找到沒有找到才會往下執行
                                        for i6 in range(0, 10):  # 第六位數
                                            if codeNotFound:  # 檢查是否找到沒有找到才會往下執行
                                                for i7 in range(0, 10):  # 第七位數
                                                    if codeNotFound:  # 檢查是否找到沒有找到才會往下執行
                                                        for i8 in range(0, 10):  # 第八位數
                                                            code = str(i1) + str(i2) + str(i3) + str(i4) + str(i5) + str(i6) + str(i7) + str(i8)  # 組成密碼
                                                            if code == secretcode:              # 比對密碼
                                                                print('Bingo!', code)
                                                                codeNotFound = False            # 註明已經比對成功
                                                                break
                                                            else:
                                                                print(code)                     # 列印無效碼


