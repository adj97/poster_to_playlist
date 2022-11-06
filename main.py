import cv2
import numpy as np
from pytesseract import image_to_string
from sys import argv
from processing import black_on_white, blur_divide, gray_scale

from utils import show_carousel

def main():
    print("1. Load image")
    filepath = argv[1]
    img = cv2.imread(filepath)

    print("2. Peprocess the image")
    img = gray_scale(img)
    img = black_on_white(img)
    img = blur_divide(img)

    show_carousel(img)

    print("2. Extract names")
    text = image_to_string(img)
    print(text)

    # print("3. Create playlist")
    # print("4. Add artist to playlist")

if __name__ == "__main__":
    exit(main())