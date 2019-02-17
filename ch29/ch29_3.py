# ch29_3.py
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('F:\\Book\\電腦書\\Python入門\\範例檔案\\ch29\\data29_3.jpg'),
                                    lang='chi_tra')
print(text)
with open('F:\\Book\\電腦書\\Python入門\\範例檔案\\ch29\\out29_3.txt', 'w') as fn:
    fn.write(text)


