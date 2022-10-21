# Stext

The task of this program is to recognize text from the screen or image!

Read this in other languages: [En](https://github.com/Mark-TinZ/Stext/blob/main/README.md), [Ru](https://github.com/Mark-TinZ/Stext/blob/main/README.ru.md);

**Stext** — a program that should recognize text from the screen or images on the screen. To implement the project, I use [Tesseract OCR](https://github.com/tesseract-ocr/tesseract), which will recognize text from an image. 
The application will be cross-platform for Windows and Linux.



## About the program

### Version Python
Python 3.10 and higher

### TODO
 - Creating custom functions for correct table recognition

### Libraries
 - **PyQt5** - interface displays.
 - **pytesseract** - text recognition from an image.
 - **opencv-python** - working with images.

### Installation

#### Linux - Ubuntu 
##### Installing Libraries
```
pip3 install PyQt5
```
```
pip3 install pytesseract
```
```
pip3 install opencv-python
```
##### Installing the necessary programs
```
sudo apt update
```
```
sudo apt install tesseract-ocr
```
#### Windows
##### Installing Libraries
```
pip install PyQt5
```
```
pip install pytesseract
```
```
pip install opencv-python
```
##### Installing the necessary programs
[Download Tesseract OCR](https://tesseract-ocr.github.io/tessdoc/Downloads.html)
### Tesseract OCR
You can download the necessary languages yourself, I will use English.
Learn more about how to download languages for Tesseract on the [page](https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc#languages-and-scripts).
