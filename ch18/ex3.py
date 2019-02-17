# ch18_2.py
import PyPDF2

word_list=[]
tem=''
fn = 'travel.pdf'                       # 設定欲讀取的PDF檔案
pdfObj = open(fn,'rb')                  # 以二進位方式開啟
pdfRd = PyPDF2.PdfFileReader(pdfObj)    # 讀取PDF檔案
pdfWr = PyPDF2.PdfFileWriter()

for pageNum in range(pdfRd.numPages):
    pageObj = pdfRd.getPage(pageNum)              # 將第1頁內容讀入pageObj
    txt = pageObj.extractText()             # 擷取頁面內容
    for t in txt:
        if t != '\n':
            tem = tem + t
        else:
            word_list.append(tem)
            tem=''

    for word in word_list:
        if word == 'Traffic':
            pdfWr.addPage(pdfRd.getPage(pageNum))
            break

pdfOutFile=open('ex3_1.pdf', 'wb')
pdfWr.write(pdfOutFile)
pdfOutFile.close()