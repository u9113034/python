# ex1.py
file_Obj=open("F:\Book\電腦書\Python入門\範例檔案\ch4\ex1.txt", mode="w")
print(" 姓名    國文    英文    總分", file=file_Obj)
print("%3s  %4d    %4d    %4d" % ("洪冰儒", 98, 90, 188), file=file_Obj)
print("%3s  %4d    %4d    %4d" % ("洪雨星", 96, 95, 191), file=file_Obj)
print("%3s  %4d    %4d    %4d" % ("洪冰雨", 92, 88, 180), file=file_Obj)
print("%3s  %4d    %4d    %4d" % ("洪星宇", 93, 97, 190), file=file_Obj)
