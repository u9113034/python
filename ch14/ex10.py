# ch14_41.py
import zipfile
import glob, os

zf = zipfile.ZipFile('CKM.ZIP', mode='w')  # 只儲存不壓縮
# zf = zipfile.ZipFile(sFilePath + '.ZIP', mode = 'w', compression = zipfile.ZIP_DEFLATED)#預設的壓縮模式
# print sFilePath
for root, folders, files in os.walk("mytest"):
    for sfile in files:
        aFile = os.path.join(root, sfile)
        # print aFile
        zf.write(aFile)
zf.close()




