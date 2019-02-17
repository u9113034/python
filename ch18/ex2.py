import PyPDF2

pdfObj=open('ex2.pdf','rb')
pdfRd=PyPDF2.PdfFileReader(pdfObj)

pdfSecret=open('secret.pdf', 'rb')
pdfRdSecret=PyPDF2.PdfFileReader(pdfSecret)
secretPage=pdfRdSecret.getPage(0)

pdfWr=PyPDF2.PdfFileWriter()

for numPage in range(pdfRd.numPages):
    ssePage=pdfRd.getPage(numPage)
    ssePage.mergePage(secretPage)
    pdfWr.addPage(ssePage)

mergePdf=open('ex2_1.pdf', 'wb')
pdfWr.write(mergePdf)
mergePdf.close()
