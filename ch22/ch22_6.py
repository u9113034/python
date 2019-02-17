# ch22_6.py
from selenium import webdriver

driverPath = 'E:\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'http://aaa.24ht.com.tw'
browser.get(url)                # 網頁下載至瀏覽器

try:
    tag = browser.find_element_by_id('main')
    print(tag.tag_name)
except:
    print("沒有找到相符的元素")


            

