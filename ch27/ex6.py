# ex6.py
import qrcode

codeText = 'https://www.yuntech.edu.tw/'
img = qrcode.make(codeText)                 # 建立QR code 物件
print("檔案格式", type(img))
img.save("ex6.jpg")


