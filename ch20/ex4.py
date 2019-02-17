# ex4.py
import csv

fn = 'csvReport.csv'
outfn='ex20_4.csv'
name,revenue,location=[],[],[]
tmpStr=''

csvOFile= open(outfn,'w',newline='')
csvWriter=csv.writer(csvOFile)
csvWriter.writerow(['Name','Revenue','Location'])

with open(fn) as csvFile:                   # 開啟csv檔案
    csvDictReader = csv.DictReader(csvFile) # 讀檔案建立DictReader物件   
    for row in csvDictReader:
        if tmpStr != row['Name']:
            csvWriter.writerow([row['Name'],row['Revenue'],row['Location']])
        else:
            csvWriter.writerow(['',row['Revenue'],row['Location']])
        tmpStr=row['Name']