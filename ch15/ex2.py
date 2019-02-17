# ch15_6.py

fn = 'ch15_6.txt'               # 設定欲開啟的檔案
try:
    in_str = input('請輸入字串=')
    #with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
     #   data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print("找不到 %s 檔案" % fn)
else:
    wordList = in_str.split()     # 將文章轉成串列
    print(fn, " 文章的字數是 ", len(wordList))    # 列印文章字數





