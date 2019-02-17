import re

fn='ex16_2.txt'
article_content=''
try:
    find_str=input('請輸入欲搜尋的字串：(n/N離開程式)')
    if find_str!='n' or find_str!='N':
        with open(fn) as file_Obj:
            article_content=file_Obj.read()
            txt=re.findall(find_str, article_content)
            print(txt)
except:
    print('異常發生!!')
finally:
    print('程式結束!!')