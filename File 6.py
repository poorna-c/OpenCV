import cv2
import numpy as np
def trackbarfun(pos):
    print(pos)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow("TRACKBAR")
cv2.namedWindow("IMAGE")

cv2.createTrackbar("B","TRACKBAR",0,255,trackbarfun)
cv2.createTrackbar("G","TRACKBAR",0,255,trackbarfun)
cv2.createTrackbar("R","TRACKBAR",0,255,trackbarfun)
cv2.createTrackbar("CrG","IMAGE",0,1,trackbarfun)

while True:
    img2 = cv2.imread('samples/lena.jpg')
    cv2.imshow("TRACKBAR",img)
    B = cv2.getTrackbarPos("B","TRACKBAR")
    G = cv2.getTrackbarPos("G","TRACKBAR")
    R = cv2.getTrackbarPos("R","TRACKBAR")
    CrG = cv2.getTrackbarPos("CrG","IMAGE")

    img[:] = [B,G,R]

    if CrG == 0:
        pass
    else:
        img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    cv2.imshow("IMAGE",img2)

    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()