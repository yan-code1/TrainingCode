import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
def getMask(img):
    lower = np.array([110,50,25])
    upper = np.array([130,255,255])
    return cv.inRange(img,lower,upper)
while True:
    _,frame = cap.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    mask = getMask(hsv)
    res = cv.bitwise_and(frame,frame,mask = mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    if cv.waitKey(25) &0xff == 27:
        break
cv.destroyAllWindows()