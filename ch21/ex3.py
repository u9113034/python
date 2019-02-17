# ch21_6.py
import requests

url = 'https://www.yuntech.edu.tw'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
else:
    print("取得網頁內容失敗")
print(htmlfile.text)            # 列印網頁內容




