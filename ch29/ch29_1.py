# ch29_1.py
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('F:\\Book\\電腦書\\Python入門\\範例檔案\\ch29\\data29_1.jpg'))
print(text)



