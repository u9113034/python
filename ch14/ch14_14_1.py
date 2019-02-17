# ch14_14_1.py
import os, re

fn='anim_list.txt'
anims=[]
if os.path.exists(fn):
    os.remove(fn)
for dirName, sub_dirNames, fileNames in os.walk('F:\\Anime'):
    #print("目前工作目錄名稱:   ", dirName)
    #print("目前子目錄名稱串列: ", sub_dirNames)
    with open(fn, 'a') as file_Obj:
        t=os.path.split(dirName)
        file_Obj.write('＝＝＝＝＝ '+t[len(t)-1]+' ＝＝＝＝＝\n')
        for mp4_file in fileNames:
            tup = os.path.splitext(mp4_file)
            if tup[1] == '.mp4':
                file_Obj.write(mp4_file)
                file_Obj.write('\n')
        file_Obj.write('\n\n')
    #print("目前檔案名稱串列:   ", fileNames, "\n")