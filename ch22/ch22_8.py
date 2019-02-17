# ch22_8.py
from selenium import webdriver
import time

driverPath = 'E:\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'http://www.grandtech.info'
browser.get(url)                # 網頁下載至瀏覽器

eleLink = browser.find_element_by_link_text('Apple 專區')
print(type(eleLink))            # 列印eleLink資料類別
time.sleep(5)                   # 暫停5秒
eleLink.click()                 # 執行超連結至書級的證照類別







