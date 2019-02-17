# ch29_4.py
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('F:\\Book\\電腦書\\Python入門\\範例檔案\\ch29\\data29_4.jpg'),
                                               lang='chi_sim')
print(text)
with open('F:\\Book\\電腦書\\Python入門\\範例檔案\\ch29\\out29_4.txt', 'w', encoding='utf-8') as fn:
    fn.write(text)


