# News_highlighter
This is a POC Project on Newspaper Highlighter using Python - Pillow, Tesseract, OpenCv & NumPy. The idea behind this to search a given key word through newspaper pages (images) and create a custom easy to read newspaper with only highlights (The lines with that key word) and important human faces.

#####################################################
To install and use Pytesseract on Windows:

1.Simply run pip install pytesseract.

2.You will also need to install Pillow with pip install Pillow to use Pytesseract.

3.Import it in your Python document like so from PIL import Image.

4.You will need to add the following line in your code in order to be able to call pytesseract on your machine: pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

5.Here I've found a detailed walkthrough of how to install Tesseract OCR for Windows (https://codetoprosper.com/tesseract-ocr-for-windows/) if you would like further guidance.
