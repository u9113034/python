# ex5.py
from PIL import Image, ImageDraw, ImageFont

newImage = Image.new('RGBA', (1000, 700), 'Yellow')  # 建立600*1000黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'National Yunlin University of Science and Technology'        # 設定欲列印英文字串
#drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小
# 使用古老英文字型, 字型大小是36
fontInfo1 = ImageFont.truetype('C:\Windows\Fonts\calibri.ttf', 36)
fontInfo2 = ImageFont.truetype('C:\Windows\Fonts\cambria.ttc', 36)
fontInfo3 = ImageFont.truetype('C:\Windows\Fonts\ITCBLKAD.TTF', 36)
fontInfo4 = ImageFont.truetype('C:\Windows\Fonts\BELL.TTF', 36)
fontInfo5 = ImageFont.truetype('C:\Windows\Fonts\AGENCYR.TTF', 36)
drawObj.text((50,50), strText, fill='Blue', font=fontInfo1)
drawObj.text((50,100), strText, fill='Blue', font=fontInfo2)
drawObj.text((50,150), strText, fill='Blue', font=fontInfo3)
drawObj.text((50,200), strText, fill='Blue', font=fontInfo4)
drawObj.text((50,250), strText, fill='Blue', font=fontInfo5)
# 處理中文字體
strCtext = '國立雲林科技大學'                           # 設定欲列印中文字串
fontInfo1 = ImageFont.truetype('C:\Windows\Fonts\kaiu.ttf', 48)
fontInfo2 = ImageFont.truetype('C:\Windows\Fonts\msmincho.ttc', 48)
fontInfo3 = ImageFont.truetype('C:\Windows\Fonts\msjh.ttf', 48)
fontInfo4 = ImageFont.truetype('C:\Windows\Fonts\simsun.ttc', 48)
fontInfo5 = ImageFont.truetype('C:\Windows\Fonts\simkai.ttf', 48)
drawObj.text((50,300), strCtext, fill='Blue', font=fontInfo1)
drawObj.text((50,350), strCtext, fill='Blue', font=fontInfo2)
drawObj.text((50,400), strCtext, fill='Blue', font=fontInfo3)
drawObj.text((50,450), strCtext, fill='Blue', font=fontInfo4)
drawObj.text((50,500), strCtext, fill='Blue', font=fontInfo5)
newImage.save("ex5.png")








