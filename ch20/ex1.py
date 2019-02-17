import openpyxl,csv

fn='report.xlsx'
outfn='ex20_1.csv'
listReport=[]
wb=openpyxl.load_workbook(fn, data_only=True)
ws=wb.active
csvFile=open(outfn,'w',newline='')
outWriter=csv.writer(csvFile)
for row in ws.rows:
    for cell in row:
        listReport.append(cell.value)
    outWriter.writerow(listReport)
    listReport.clear()

csvFile.close()