# ch29_2.py
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('F:\\Book\\電腦書\\Python入門\\範例檔案\\ch29\\data29_2.jpg'))
print(text)
with open('F:\\Book\\電腦書\\Python入門\\範例檔案\\ch29\\out29_2.txt', 'w') as fn:
    fn.write(text)


