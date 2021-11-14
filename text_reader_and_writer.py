import pyautogui
import time
import pytesseract
import cv2
import numpy as np
from PIL import ImageGrab, Image
from bs4 import BeautifulSoup as bs
import webbrowser
def text_reader_and_writer():
    pytesseract.pytesseract.tesseract_cmd = r'path'

    webbrowser.open_new_tab("https://humanbenchmark.com/tests/typing")
    time.sleep(5)
    
    if __name__ == "__main__":
        # part of the screen
        im=ImageGrab.grab(bbox=(335,580,1800,850)) # X1,Y1,X2,Y2
        #with open("the img.png","wb") as f:
            #f.write(im)
        im.save("the img.png")

    img = cv2.imread("the img.png")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    text = pytesseract.image_to_string(img)
    #cv2.imshow('result',img)
    #cv2.waitKey(0)
    text = text.replace("\n"," ")
    text = text.replace("|","I")
    text = text.split()

    textoneline = []
    for txt in text:
        textoneline.append(txt)

    def listToString(s): 
        
        # initialize an empty string
        str1 = " " 
        
        # return string  
        return (str1.join(s))


    print(textoneline)

    pyautogui.write(listToString(textoneline), interval=0.001)


text_reader_and_writer()
