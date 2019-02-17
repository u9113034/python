# ex2.py
import csv

fn = 'csvReport.csv'
outfn='ex20_2.csv'
revenue2015, revenue2016=0, 0

with open(fn) as csvFile:                   # 開啟csv檔案
    csvDictReader = csv.DictReader(csvFile) # 讀檔案建立DictReader物件   
    for row in csvDictReader:
        if row['Year']=='2015':
            revenue2015+=int(row['Revenue'])
        elif row['Year']=='2016':
            revenue2016+=int(row['Revenue'])

with open(outfn,'w',newline='') as csvOFile:
    csvWriter=csv.writer(csvOFile)
    csvWriter.writerow(['Year','Total Revenue'])
    csvWriter.writerow(['2015',revenue2015])
    csvWriter.writerow(['2016',revenue2016])




