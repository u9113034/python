# ch20_11.py
import csv

dictList = [{'Name':'Hung', 'Age':'35', 'City':'Taipei','Phone':'\'0999123456'},       # 定義串列,元素是字典
            {'Name':'James', 'Age':'40', 'City':'Chicago','Phone':'\'0910987654'},
            {'Name': 'Marx', 'Age': '42', 'City': 'Tainan', 'Phone': '\'0910987654'},
            {'Name': 'Eryn', 'Age': '31', 'City': 'Kaochiung', 'Phone': '\'0910987654'},
            {'Name': 'Taco', 'Age': '41', 'City': 'Shinchu', 'Phone': '\'0910987654'},
            {'Name': 'Bruce', 'Age': '30', 'City': 'Japan', 'Phone': '\'0910987654'},
            {'Name': 'Katie', 'Age': '30', 'City': 'Oosaka', 'Phone': '\'0910987654'},
            {'Name': 'Kent', 'Age': '32', 'City': 'Okinawa', 'Phone': '\'0910987654'},
            {'Name': 'Tom', 'Age': '15', 'City': 'Tailand', 'Phone': '\'0910987654'},
            {'Name': 'Kevin', 'Age': '14', 'City': 'vietnam', 'Phone': '\'0910987654'}]
          
fn = 'ex20_5.csv'
with open(fn, 'w', newline = '') as csvFile:                    # 開啟csv檔案
    fields = ['Name', 'Age', 'City', 'Phone']
    dictWriter = csv.DictWriter(csvFile, fieldnames=fields)     # 建立Writer物件

    dictWriter.writeheader()                                    # 寫入標題
    for row in dictList:                                        # 寫入內容
        dictWriter.writerow(row)




