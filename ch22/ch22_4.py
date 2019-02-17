# ch22_4.py
from selenium import webdriver

driverPath = 'E:\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'http://aaa.24ht.com.tw'
browser.get(url)                # 網頁下載至瀏覽器


            

