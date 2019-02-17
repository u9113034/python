# copy program

in_fn=input('請輸入來源檔名: ')
out_fn=input('請輸入目的檔名: ')

r_Obj = open(in_fn)
w_Obj = open(out_fn, 'w')
r_str = r_Obj.read()
w_Obj.write(r_str)
r_Obj.close()
w_Obj.close()