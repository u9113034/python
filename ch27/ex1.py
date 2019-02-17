# ex1.py
from PIL import Image, ImageDraw, ImageFont

fn = 'Me.jpg'
pict = Image.open(fn)
drawObj = ImageDraw.Draw(pict)
strText = '周侊懋'
fontInfo = ImageFont.truetype('C:\Windows\Fonts\kaiu.ttf', 36)
drawObj.text((30,30), strText, fill='Black', font=fontInfo)
width, height = pict.size
pict.resize((int(width*1.2), height)).save('ex1_a.jpg')
pict.resize((int(width*1.5), height)).save('ex1_b.jpg')
pict.resize((int(width*0.5), height)).save('ex1_c.jpg')
pict.resize((int(width*0.8), height)).save('ex1_d.jpg')
pict.resize((width, int(height*1.2))).save('ex1_e.jpg')
pict.resize((width, int(height*1.5))).save('ex1_f.jpg')
pict.resize((width, int(height*0.8))).save('ex1_g.jpg')
pict.resize((width, int(height*0.5))).save('ex1_h.jpg')
