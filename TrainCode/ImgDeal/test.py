import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import random
#桌面鼠标位置监听测试
# import os,time
# import pyautogui as pag
# try:
#     while True:
#             print("Press Ctrl-C to end")
#             x,y = pag.position() #返回鼠标的坐标
#             posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
#             print (posStr)#打印坐标
#             time.sleep(0.2)
#             os.system('cls')#清楚屏幕
# except  KeyboardInterrupt:
#     print ('end....')

#位置测试
# img = cv.imread('temp.jpg')
# print(img.shape[0])
# print(img.shape[1])
# winW = 25
# winH = 160
# leftUp = (0,img.shape[0]-winW)
# rightDown = (winH,img.shape[0])
# cv.rectangle(img,leftUp,rightDown,(255,255,255),thickness=-1)
# text = 'R:225 G:225 B:255'
# cv.putText(img,text,(0,img.shape[0]-5),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255))
# cv.imshow('image',img)
# cv.waitKey(0)

