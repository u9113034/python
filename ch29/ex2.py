# ch29_3.py
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('F:\\Book\\電腦書\\Python入門\\範例檔案\\ch29\\Image 001.png'),
                                    lang='chi_tra')
print(text)
with open('F:\\Book\\電腦書\\Python入門\\範例檔案\\ch29\\Image 001.txt', 'w') as fn:
    fn.write(text)


