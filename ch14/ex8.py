import shutil, send2trash

shutil.copytree('mytest','c:\\CKM')
send2trash.send2trash('c:\\CKM')