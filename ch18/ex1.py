import PyPDF2

pdfObj=open('travel.pdf','rb')
pdfRd=PyPDF2.PdfFileReader(pdfObj)

pdfWr=PyPDF2.PdfFileWriter()
for numPage in range(pdfRd.numPages):
    pdfWr.addPage(pdfRd.getPage(numPage))

pdfOutFile=open('ex18_1.pdf', 'wb')
pdfWr.write(pdfOutFile)
pdfOutFile.close()