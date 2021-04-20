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

#目标检测 人
# import cv2
# def is_inside(o, i):
#     ox, oy, ow, oh = o
#     ix, iy, iw, ih = i
#     # 如果符合条件，返回True，否则返回False
#     return ox > ix and oy > iy and ox + ow < ix + iw and oy + oh < iy + ih
#
# # 根据坐标画出人物所在的位置
# def draw_person(img, person):
#   x, y, w, h = person
#   cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
#
# # 定义HOG特征+SVM分类器
# img = cv2.imread("temp.jpg")
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# found, w = hog.detectMultiScale(img, winStride=(8, 8), scale=1.05)
#
# # 判断坐标位置是否有重叠
# found_filtered = []
# for ri, r in enumerate(found):
#     for qi, q in enumerate(found):
#         a = is_inside(r, q)
#         if ri != qi and a:
#             break
#     else:
#         found_filtered.append(r)
# # 勾画筛选后的坐标位置
# for person in found_filtered:
#     draw_person(img, person)
# # 显示图像
# cv2.imshow("people detection", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#
# import cv2
# import dlib
#
# tracker = dlib.correlation_tracker()  # 导入correlation_tracker()类
# cap = cv2.VideoCapture(0)  # opencv打开摄像头，参数为设备索引号，笔记本电脑，0表示使用其内置摄像头
#
# selection = None  # 实时跟踪鼠标的跟踪区域
# track_window = None  # 要检测的物体所在区域
# drag_start = None  # 标记，是否开始拖动鼠标
#
#
# # 鼠标点击事件回调函数
# def onmouse(event, x, y, flags, param):
#     global selection, track_window, drag_start  # 定义全局变量
#     if event == cv2.EVENT_LBUTTONDOWN:  # 鼠标左键按下
#         drag_start = (x, y)  # 鼠标起始位置
#         track_window = None
#     if drag_start:  # 是否开始拖动鼠标，记录鼠标位置
#         xmin = min(x, drag_start[0])
#         ymin = min(y, drag_start[1])
#         xmax = max(x, drag_start[0])
#         ymax = max(y, drag_start[1])
#         selection = (xmin, ymin, xmax, ymax)
#     if event == cv2.EVENT_LBUTTONUP:  # 鼠标左键松开
#         drag_start = None
#         track_window = selection
#         selection = None
#
#
# def main():
#     # 创建图像与窗口，并将窗口与回调函数绑定
#     cv2.namedWindow('image', 1)
#     cv2.setMouseCallback('image', onmouse)
#
#     k = 0
#     while (1):
#         ret, frame = cap.read()  # 从摄像头读入1帧，ret表明成功与否
#         if not ret:
#             print("Game over!")
#             break
#         print("Processing Frame {}".format(k))
#         img_raw = frame  # 初始帧
#         image = img_raw.copy()  # 不改变初始帧，拷贝新的帧
#
#         # 初始化第一帧
#         if k == 0:
#             # 用鼠标拖拽一个框来指定区域
#             while True:
#                 img_first = image.copy()  # 不改变原来的帧，拷贝一个新的
#                 if track_window:  # 跟踪目标的窗口画出后，实时标出跟踪目标
#                     cv2.rectangle(img_first, (track_window[0], track_window[1]), (track_window[2], track_window[3]),
#                                   (0, 0, 255), 1)
#                 elif selection:  # 跟踪目标的窗口随鼠标拖动实时显示
#                     cv2.rectangle(img_first, (selection[0], selection[1]), (selection[2], selection[3]), (0, 0, 255), 1)
#                 cv2.imshow('image', img_first)
#                 if cv2.waitKey(5) == 27:  # 等待时间为5ms,用户按下按下ESC(ASCII码为27)，退出循环
#                     break
#             tracker.start_track(image,
#                                 dlib.rectangle(track_window[0], track_window[1], track_window[2], track_window[3]))
#         else:
#             # 不是第一帧了
#             tracker.update(image)  # 更新，实时跟踪
#             # time.sleep(3)
#
#         box_predict = tracker.get_position()  # 得到目标的位置
#         cv2.rectangle(image, (int(box_predict.left()), int(box_predict.top())),
#                       (int(box_predict.right()), int(box_predict.bottom())), (0, 255, 255), 1)
#         cv2.imshow('image', image)
#
#         c = cv2.waitKey(5)
#         if c == 27: break  # 如果按下ESC，则退出
#         k += 1
#     cv2.destroyAllWindows()
#
#
# if __name__ == '__main__':
#     main()
import  cv2
import dlib
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-p','--prototxt',default='./object_detection/MobileNetSSD_deploy.prototxt.txt')
ap.add_argument('-m','--caffemodel',default='./object_detection/MobileNetSSD_deploy.caffemodel')
args = vars(ap.parse_args())
cap = cv2.VideoCapture(0)
net = cv2.dnn.readNetFromCaffe(args['prototxt'], args['caffemodel'])
while True:
    ret,frame = cap.read()
    blob = cv2.dnn.blobFromImage(cv2.resize(frame,(300,300)),0.000017,(300,300),127.5)
    # blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
    #                              0.007843, (300, 300), 127.5)
    net.setInput(blob)
    result = net.forward()
    print(result)
    if cv2.waitKey(5) == 27 & 0xff:
        break
    cv2.destroyAllWindows()
