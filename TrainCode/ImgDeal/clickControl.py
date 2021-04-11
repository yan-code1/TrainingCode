import numpy as np
import cv2 as cv

def getClikePointColor(img,x,y):
    #真坑啊，数组的x,y和鼠标回调坐标是调过来的
    B,G,R = img[y,x]
    return B,G,R

def clickFunction (event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, y)
        img = param
        B,G,R = getClikePointColor(img,x,y)
        text = 'R:'+str(R)+' G:'+str(G)+' B:'+str(B)
        cv.putText(img,text,(x+5,y-5),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255))
        cv.circle(img,(x,y),1,(255,0,0))

def main():
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 600)
    _, img = cap.read()
    # img = cv.imread('temp.jpg')
    img_temp = img.copy()
    cv.namedWindow('image')
    cv.setMouseCallback('image',clickFunction,img)
    while True:
        cv.imshow('image',img)
        if cv.waitKey(20) & 0xFF == 27:
            break
        #清屏
        if cv.waitKey(20) & 0xFF == ord('c'):
            img = img_temp.copy()
            cv.setMouseCallback('image', clickFunction, img)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()