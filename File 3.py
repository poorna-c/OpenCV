import cv2
import numpy as np

img = cv2.imread('samples/detect_blob.png')
points = []
drawing = False
def click_event(event, x, y, flags, prams):
    global drawing
    b = img[y, x, 0]
    g = img[y, x, 1]
    r = img[y, x, 2]
    if event == cv2.EVENT_LBUTTONDBLCLK:
        strXY = str(x)+", "+str(y)
        cv2.circle(img,(x,y),2,(255,255,255),-1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-2],points[-1],(0,0,255),2)
        cv2.imshow("Mouse Events",img)
        print(flags,prams)
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img,(x,y),5,(255,255,255),-1)
        cv2.imshow("Mouse Events",img)
    if event == cv2.EVENT_RBUTTONDOWN:
        newImg = np.zeros((512,512,3),np.uint8)
        newImg[:] = [b,g,r]
        cv2.imshow("Color Identified",newImg)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        strBGR = str(b)+", "+str(g)+", "+str(r)
        cv2.putText(img,strBGR,(x,y), cv2.FONT_HERSHEY_SIMPLEX,0.4 , (0,255,255),1)
        cv2.imshow("Mouse Events",img)
        print(flags,prams)




cv2.imshow("Mouse Events",img)
cv2.setMouseCallback("Mouse Events",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()