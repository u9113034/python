# ch22_11.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driverPath = 'E:\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'http://www.grandtech.info'
browser.get(url)                    # 網頁下載至瀏覽器

time.sleep(3)
browser.refresh()                   # 更新網頁
time.sleep(3)
browser.quit()                      # 關閉網頁








