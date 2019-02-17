# ex2.py
file_Obj=open("F:\Book\電腦書\Python入門\範例檔案\ch4\ex2.txt",mode="w")
sp = " " * 40
print("%s   1231 Delta Rd" % sp, file=file_Obj)
print("%s   Oxford, Mississippi" % sp, file=file_Obj)
print("%s   USA\n\n\n" % sp, file=file_Obj)
print("Dear Ivan", file=file_Obj)
print("I am pleased to inform you that your application for fall 2020 has", file=file_Obj)
print("been favorably reviewed by the Electrical and Computer Engineering", file=file_Obj)
print("Office.\n\n", file=file_Obj)
print("Best Regards", file=file_Obj)
print("Peter Malong", file=file_Obj)
