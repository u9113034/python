import re,docx

fn='ex17_2.docx'
txt=[]
count=0
try:
    wdoc=docx.Document(fn)
    find_str = input('請輸入欲搜尋的字串:')
    for paragraph in wdoc.paragraphs:
        txt.append(re.findall(find_str, paragraph.text))
        count+=len(txt)

    print('%s 總共出現 %d 次' % (find_str, count))
except Exception as e:
    print(e)
finally:
    print('程式結束!!')