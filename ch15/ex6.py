import traceback
# ch15_15.py
def passWord(pwd):
    """檢查密碼長度必須是5到8個字元"""
    with open(pwd) as file_Obj:
        data = file_Obj.read()
        wordList = data.split()  # 將文章轉成串列
    if len(wordList) < 50:                          # 密碼長度不足
        raise Exception('文章長度不足')
    if len(wordList) > 100:                          # 密碼長度太長
        raise Exception('文章長度太長')
    print('文章長度正確')

files=['data01.txt', 'data02.txt', 'data03.txt', 'data04.txt', 'data05.txt']
for fn in files:
    try:
        passWord(fn)
    except Exception as err:
        with open('errdata.txt', 'a') as errlog:
            errlog.write(traceback.format_exc())
        print('異常錯誤寫入完成')