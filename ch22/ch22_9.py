# ch22_9.py
from selenium import webdriver
import time

driverPath = 'E:\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'http://www.grandtech.info'
browser.get(url)                    # 網頁下載至瀏覽器

txtBox = browser.find_element_by_id('key')
txtBox.send_keys('洪錦魁')          # 輸入表單資料
time.sleep(5)                       # 暫停5秒
txtBox.submit()                     # 送出表單









