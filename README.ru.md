# Stext

Задача этой программы заключается в распознавании текста с экрана или изображения.

Читать на других языках: [En](https://github.com/Mark-TinZ/Stext/blob/main/README.md), [Ru](https://github.com/Mark-TinZ/Stext/blob/main/README.ru.md);

**Stext** — программа, которая должна распознавать текст с экрана или изображения на экране. Для реализации проекта я использую 
[Tesseract OCR](https://github.com/tesseract-ocr/tesseract), который будет распознавать текст с изображения. 
Приложение будет кроссплатформенным для Windows и Linux.

## О зависимостях

### Версия Python
Python 3.10 и выше

### Библиотеки
 - **PyQt5** - отображения интерфейса.
 - **pytesseract** - распознавание текста по изображению.
 - **opencv-python** - работа с изображениями.

### Установка

#### Linux - Ununtu
##### Установка библиотек
```
pip3 install PyQt5
```
```
pip3 install pytesseract
```
```
pip3 install opencv-python
```
##### Установка необходимых программ
```
sudo apt update
```
```
sudo apt install tesseract-ocr
```
#### Windows
##### Установка библиотек
```
pip install PyQt5
```
```
pip install pytesseract
```
```
pip install opencv-python
```
##### Установка необходимых программ
[Download Tesseract OCR](https://tesseract-ocr.github.io/tessdoc/Downloads.html)
### Tesseract OCR
Необходимые языки вы можете скачать сами, я буду использованием английского.
Подробно как скачать языки для Tesseract на [странице](https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc#languages-and-scripts).
