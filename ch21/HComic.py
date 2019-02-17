# 抓取紳士漫畫網的漫畫 https://www.wnacg.org/
import requests, bs4, re

url = 'https://www.wnacg.org/albums-index-page-1-sname-%E3%82%AA%E3%82%AF%E3%83%A2%E3%83%88.html'
html = requests.get(url)
#print('網頁下載中...')
html.raise_for_status()
#print('網頁下載完成')

objSoup = bs4.BeautifulSoup(html.text, 'lxml')
dataTag = objSoup.select('.pic_box')    # 取得漫畫列表URL

lstURL = []
for i in range(len(dataTag)):
    lstURL.append(dataTag[i].find_all('a'))

pattern = r'/photos-index-aid-\d{5}.html'
pp = []
for url in lstURL:
    pp += re.findall(pattern, str(url))     # 找到URL列表

downUrl = []
for j in range(len(pp)):
    downUrl.append('https://www.wnacg.org' + str(pp[j]).replace('photos', 'download'))    # 將photos取代成download

fileUrl = []
for file in downUrl:
    url = str(file)
    html = requests.get(url)
    html.raise_for_status()
    objSoup = bs4.BeautifulSoup(html.text, 'html.parser')
    tag = objSoup.find('p','download_filename')
    print(tag.string)
    print(objSoup.find_all('a')[1].get('href'))