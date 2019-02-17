# ex3.py
from PIL import Image, ImageDraw
import os

fn='signature.jpg'
signPict = Image.open(fn)

for dirName, sub_dirNames, fileNames in os.walk(r'F:\Book\電腦書\Python入門\範例檔案\ch27\ex3'):
    for jpgFile in fileNames:
        tup = os.path.splitext(jpgFile)
        if tup[1] == '.jpg':
            tmpPict = Image.open(jpgFile)
            tmpPict.paste(signPict, (275, 300))
            tmpPict.save(jpgFile)