# ch14_42.py
import zipfile

listZipInfo = zipfile.ZipFile('out41.zip', 'r')
fn_list=[]
size_list=[]
#print(listZipInfo.namelist())       # 以列表列出所有壓縮檔案
#print("\n")
for info in listZipInfo.infolist():
    fn_list.append(info.filename)
    size_list.append(info.file_size)
    #print(info.filename, info.file_size, info.compress_size, info.date_time)

max=max(size_list)
min=min(size_list)
max_index=size_list.index(max)
min_index=size_list.index(min)
print("最大檔案名稱 %s, 大小為 %d" % (fn_list[max_index] , size_list[max_index]))
print("最小檔案名稱 %s, 大小為 %d" % (fn_list[min_index] , size_list[min_index]))