# ch27_12.py
from PIL import Image

pict = Image.open("rushmore.jpg")                     # 建立Pillow物件
pict.transpose(Image.FLIP_LEFT_RIGHT).save("out27_12_1.jpg")    # 左右
pict.transpose(Image.FLIP_TOP_BOTTOM).save("out27_12_2.jpg")    # 上下









