# ex1.py
import json

fn = 'populations.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)                     # 讀json檔案
jsonfn = 'ex24_1.json'
fnObj = open(jsonfn, 'w')

for getData in getDatas:
    if getData['Year'] == '2000':                   # 篩選2000年的數據
        #countryName = getData['Country Name']       # 國家名稱
        json.dump(getData['Country Name'], fnObj)
        #countryCode = getData['Country Code']       # 國家代碼
        json.dump(getData['Country Code'], fnObj)
        #population = int(float(getData['Numbers'])) # 人口數據
        json.dump(int(float(getData['Numbers'])), fnObj)
        fnObj.write('\n')
        # print('國家代碼 =', countryCode,
        #       '國家名稱 =', countryName,
        #       '人口數 =', population)





        

