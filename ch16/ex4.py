import re, os

pattern1=r'[A-Za-z0-9]+\.txt'    # 副檔為txt的所有檔案
pattern2=r'ch14_1\d.py'        # 列出ch14_10.py~ch14_19.py的十個檔案
path='F:\\Book\\電腦書\\Python入門\\範例檔案\\ch14'
for dirName, sub_dirNames, fileNames in os.walk(path):
    for fileName in fileNames:
        txt=re.search(pattern2, fileName, re.IGNORECASE)
        if txt != None:
            print(txt.group())