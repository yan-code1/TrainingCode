import numpy as np
import cv2

drawing = False
mode = True
ix,iy = -1,-1

def draw_circle(event,x,y,flags,param):
    img = param
    global drawing,mode,ix,iy
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event==cv2.EVENT_MOUSEMOVE :
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),2)
            else:
                cv2.circle(img,(x,y),50,(0,255,0),3)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
def main():
    img = np.zeros((512,512,3), np.uint8)
    cv2.namedWindow('opencv')
    cv2.setMouseCallback('opencv',draw_circle,img)
    while(1):
        cv2.imshow('opencv',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1) &0xFF == ord('m'):
            mode = not mode
    # cv2.imwrite('/home/wl/1.jpg',img)
    cv2.destroyAllWindows()
if __name__ =='__main__':
    main()