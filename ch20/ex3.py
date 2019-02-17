# ex3.py
import csv

fn = 'csvReport.csv'
outfn='ex20_3.csv'
bestSalesman, worstSalesman='',''
man,revenue=[],[]

csvOFile = open(outfn,'w',newline='')
csvWriter=csv.writer(csvOFile)
csvWriter.writerow(['Year','Best','Worst'])

with open(fn) as csvFile:                   # 開啟csv檔案
    csvDictReader = csv.DictReader(csvFile) # 讀檔案建立DictReader物件   
    for row in csvDictReader:
        if row['Year']=='2015':
            man.append(row['Name'])
            revenue.append(int(row['Revenue']))

csvWriter.writerow(['2015',man[revenue.index(max(revenue))],man[revenue.index(min(revenue))]])

with open(fn) as csvFile:                   # 開啟csv檔案
    csvDictReader = csv.DictReader(csvFile) # 讀檔案建立DictReader物件
    for row in csvDictReader:
        if row['Year']=='2016':
            man.append(row['Name'])
            revenue.append(int(row['Revenue']))

csvWriter.writerow(['2016',man[revenue.index(max(revenue))],man[revenue.index(min(revenue))]])

csvOFile.close()
