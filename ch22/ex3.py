# ex3.py
import requests, os
from selenium import webdriver

driverPath = 'E:\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'http://www.taiwanlottery.com.tw'
browser.get(url)                # 網頁下載至瀏覽器

dataTag=browser.find_elements_by_class_name('contents_box02')
for i in range(0,3,2):                       # 列出含contents_box02的串列
    balls=dataTag[i].text
    print(balls)