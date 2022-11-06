import cv2 

def show_carousel(*args):

    for img in args:
        cv2.imshow('image window', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return