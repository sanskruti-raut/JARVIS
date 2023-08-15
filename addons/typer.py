from PIL import ImageGrab
import pyautogui as py
import time
import pytesseract
import sys

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
orig_text = ""

def returnText(image):
    return pytesseract.image_to_string(image)


def grabImage(box):
    return ImageGrab.grab(box)


def changeFlg():
    global flg
    flg = 0


def fastType(box1):
    global orig_text
    img1 = grabImage(box1)
    new_text = returnText(img1).strip() + " "
    
    if new_text == orig_text:
        sys.exit()

    else:
        orig_text = new_text
        
    py.typewrite(new_text, interval = 0.01)

def main():
    box1 = (237, 266, 1058, 315)
    #box1 = (286, 442, 1202, 49)
    print("IMPLEMENTING FAST TYPER IN")
    
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)

    py.hotkey('ctrl', 'r')
    time.sleep(5)
    start = time.time()
    while time.time() < start + 60:
        fastType(box1)

def openSite():
    py.hotkey('win', 'r')
    time.sleep(1)
    py.typewrite("chrome", interval = 0.1)
    py.press('enter')
    time.sleep(2)
    py.typewrite("10fastfingers.com/typing-test/english", interval = 0.1)
    py.press('enter')
    main()
    
'''
def test():
    time.sleep(3)
    img = grabImage()
    if returnText(img) == '':
        print("YIP!")

    else:
        print(returnText(img))
    img.show()
'''
openSite()
#test()
