# ch18_4.py
import PyPDF2

pdfObj = open('ex10_9.pdf','rb')
pdfRd = PyPDF2.PdfFileReader(pdfObj)
codeNotFound = True                                             # 尚未找到密碼為True
for i1 in range(1, 27):                                         # 第一位數
    if codeNotFound:            # 檢查是否找到沒有找到才會往下執行
        for i2 in range(1, 27):                                 # 第二位數
            if codeNotFound:    # 檢查是否找到沒有找到才會往下執行
                for i3 in range(1, 27):  # 第三位數
                    if codeNotFound:  # 檢查是否找到沒有找到才會往下執行
                        for i4 in range(1, 27):  # 第四位數
                            if codeNotFound:  # 檢查是否找到沒有找到才會往下執行
                                for i5 in range(1, 27):                         # 第五位數
                                    code = chr(i1+96) + chr(i2+96) + chr(i3+96) + chr(i4+96) + chr(i5+96) # 組成密碼
                                    if pdfRd.decrypt(code):  # 檢查密碼是否正確
                                        print('Bingo!', code)
                                        pageObj = pdfRd.getPage(0)  # 密碼正確則讀取第0頁
                                        txt = pageObj.extractText()
                                        print(txt)
                                        codeNotFound = False                    # 註明已經比對成功
                                        break
                                    else:
                                        print(code, end=' ')                    # 列印無效碼












