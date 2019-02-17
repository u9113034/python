# ex1.py
import os, requests
from selenium import webdriver

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }

driverPath = 'E:\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'http://aaa.24ht.com.tw/'
browser.get(url)                # 網頁下載至瀏覽器

destDir = 'out22_1'                                # 設定未來儲存圖片的資料夾
if os.path.exists(destDir) == False:
    os.mkdir(destDir)                               # 建立資料夾供未來儲存圖片

tag5 = browser.find_elements_by_tag_name('img')         # 傳回<img>
for i in range(len(tag5)):
    #print("標籤名稱 = %s, 內容是 = %s " % (tag5[i].tag_name, tag5[i].get_attribute('src')))
    imgUrl = tag5[i].get_attribute('src')
    picture = requests.get(imgUrl,headers=headers)  # 下載圖片
    picture.raise_for_status()  # 驗證圖片是否下載成功
    print("%s 圖片下載成功" %  tag5[i].get_attribute('src'))
    # 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(imgUrl)), 'wb')
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()  # 關閉檔案
