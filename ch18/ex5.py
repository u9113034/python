# ch18_8.py
import PyPDF2, os, re

try:
    for dirName, sub_dirNames, fileNames in os.walk('F:\\Book\\電腦書\\Python入門\\範例檔案\\ch18'):
        for fn in fileNames:
            txt = re.search(r'\w*\.pdf', fn, re.IGNORECASE)
            if txt != None:
                pdfFn=txt.group()
                pdfObj = open(pdfFn,'rb')
                pdfRd = PyPDF2.PdfFileReader(pdfObj)
                pdfWr = PyPDF2.PdfFileWriter()               # 新的PDF物件
                for pageNum in range(pdfRd.numPages):
                    pdfWr.addPage(pdfRd.getPage(pageNum))   # 一次將一頁放入新的PDF物件
                pdfWr.encrypt('python')                     # 執行加密
                refn=re.search(r'\w+[^.]', pdfFn, re.IGNORECASE)
                encryptPdf=refn.group()
                encryptPdf = open(encryptPdf+'_encryt.pdf', 'wb')       # 開啟二進位檔案供寫入
                pdfWr.write(encryptPdf)                     # 執行寫入
                print(pdfFn+'寫入成功')
                encryptPdf.close()
except FileNotFoundError as e:
    print(e)
finally:
    print('程式結束!!')