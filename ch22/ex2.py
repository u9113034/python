# ex2.py
import requests, os
from selenium import webdriver

driverPath = 'E:\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'http://www.grandtech.info/'
browser.get(url)                # 網頁下載至瀏覽器

destDir = 'out22_2'                                # 設定未來儲存圖片的資料夾
if os.path.exists(destDir) == False:
    os.mkdir(destDir)                               # 建立資料夾供未來儲存圖片

imgTag = browser.find_elements_by_tag_name('img')                      # 搜尋所有圖片檔案
for i in range(len(imgTag)):
    #print("標籤名稱 = %s, 內容是 = %s " % (tag5[i].tag_name, tag5[i].get_attribute('src')))
    imgUrl = imgTag[i].get_attribute('src')
    picture = requests.get(imgUrl)  # 下載圖片
    picture.raise_for_status()  # 驗證圖片是否下載成功
    print("%s 圖片下載成功" %  imgTag[i].get_attribute('src'))
    # 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(imgUrl)), 'wb')
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()  # 關閉檔案
        

    




    
