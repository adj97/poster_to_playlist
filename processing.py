import cv2
import numpy as np

def gray_scale(img):
    # Convert to gry-scale
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def black_on_white(img):
    background = cv2.medianBlur(img, 51)
    return 255 - cv2.absdiff(background, img)

def blur_divide(img):
    blured1 = cv2.medianBlur(img,3)
    blured2 = cv2.medianBlur(img,51)
    divided = np.ma.divide(blured1, blured2).data
    normed = np.uint8(255*divided/divided.max())
    th, threshed = cv2.threshold(normed, 100, 255, cv2.THRESH_OTSU)

    return np.vstack((img, blured1, blured2, normed, threshed)) 