# ch14_22.py

fn = 'ex3_1.txt'          # 設定欲開啟的檔案
out_fn = 'ex3_4.txt'
str_Obj = ''                # 先設為空字串
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    str_Obj = file_Obj.read()  # 一次讀取

with open(out_fn, 'w') as out_Obj:
    out_Obj.write(str_Obj.replace('高手','專家'))
