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
import cv2
import numpy as np
import os

def fillBlack(img):
     # pixel = np.zeros(3)
     pixel = 0
     for i in range(img.shape[0]):
          for j in range(img.shape[1]):
               if img[i][j] != 0:
                    pixel = img[i][j]

          img[][]
for path in open("1.txt"):
     path = path.replace('\n', '')  # 去除换行符号
     print(path)
     img = cv2.imread(path, 1)

     import  time
     s = time.time()
     width, height = img.shape[:2][::-1]
     img_resize = cv2.resize(img, (int(width * 1.0), int(height * 1.0)), interpolation = cv2.INTER_CUBIC)
     img_gray = cv2.cvtColor(img_resize, cv2.COLOR_RGB2GRAY)
     img_temp = img.flatten()
     # img_gray = img_gray[img_gray.shape[0]-10:img_gray.shape[0],img_gray.shape[1]-10:img_gray.shape[1]]
     imageVar = cv2.Laplacian(img_gray, cv2.CV_64F).var()  # 图像模糊度
     # print('>>>', path)
     # cv2.imshow(img_gray)
     print(">>>", int(imageVar),time.time() - s)
