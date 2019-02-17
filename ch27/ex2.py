# ch27_18.py
from PIL import Image

pict = Image.open("Me.jpg")               # 建立Pillow物件
copyPict = pict.copy()                          # 複製
width, height = copyPict.size
resizePict = copyPict.resize((int(width/4),int(height/4)))
# cropPict = copyPict.crop((80, 30, 300, 200))    # 裁切區間
cropWidth, cropHeight = resizePict.size           # 獲得裁切區間的寬與高

width, height = 600, 340                        # 新影像寬與高
newImage = Image.new('RGB', (width, height), "Yellow")  # 建立新影像
for x in range(20, width-20, cropWidth):         # 雙層迴圈合成
    for y in range(20, height-20, cropHeight):
        newImage.paste(resizePict, (x, y))        # 合成

newImage.save("ex2_1.jpg")                   # 儲存









