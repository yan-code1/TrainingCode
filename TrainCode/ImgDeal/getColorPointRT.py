from time import sleep
import numpy as np
import cv2 as cv
def winLD(img,text):
    winW = 25
    winH = 160
    leftUp = (0, img.shape[0] - winW)
    rightDown = (winH, img.shape[0])
    cv.rectangle(img, leftUp, rightDown, (255, 255, 255), thickness=-1)
    # text = 'R:225 G:225 B:255'
    cv.putText(img, text, (0, img.shape[0] - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

def getClikePointColor(img,x,y):
    #真坑啊，数组的x,y和鼠标回调坐标是调过来的,而且imread读取的是BGR通道
    B,G,R = img[y,x]
    return B,G,R

def clickFunction (event,x,y,flags,param):
    #不带事件默认鼠标移动事件
    # if event == cv.EVENT_LBUTTONDOWN:
        print(x, y)
        img = param
        B,G,R = getClikePointColor(img,x,y)
        text = 'R:'+str(R)+' G:'+str(G)+' B:'+str(B)
        winLD(img,text)
        # cv.putText(img,text,(x+5,y-5),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255))
        cv.circle(img,(x,y),2,(0,255,255))
        cv.imshow('image', img)

def main():
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 600)
    cv.namedWindow('image')

    while True:
        _, img = cap.read()
        # img = cv.imread('temp.jpg')
        # cv.imshow('image',img)
        cv.setMouseCallback('image',clickFunction,img)

        if cv.waitKey(20) & 0xFF == 27:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()