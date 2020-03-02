import cv2
import numpy as np

def trackbarval(x):
    print(x)


cv2.namedWindow("Tracking...")
track = np.zeros((256,256,3),np.uint8)

cv2.createTrackbar("LH","Tracking...",0,255,trackbarval)
cv2.createTrackbar("LS","Tracking...",0,255,trackbarval)
cv2.createTrackbar("LV","Tracking...",0,255,trackbarval)
cv2.createTrackbar("HH","Tracking...",255,255,trackbarval)
cv2.createTrackbar("HS","Tracking...",255,255,trackbarval)
cv2.createTrackbar("HV","Tracking...",255,255,trackbarval)

cv2.createTrackbar("B","Tracking...",0,255,trackbarval)
cv2.createTrackbar("G","Tracking...",0,255,trackbarval)
cv2.createTrackbar("R","Tracking...",0,255,trackbarval)

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame,(512,512))
    img = cv2.imread("samples/smarties.png")

    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("Tracking...",track)


    LH = cv2.getTrackbarPos("LH","Tracking...")
    LS = cv2.getTrackbarPos("LS","Tracking...")
    LV = cv2.getTrackbarPos("LV","Tracking...")
    HH = cv2.getTrackbarPos("HH","Tracking...")
    HS = cv2.getTrackbarPos("HS","Tracking...")
    HV = cv2.getTrackbarPos("HV","Tracking...")

    B = cv2.getTrackbarPos("B","Tracking...")
    G = cv2.getTrackbarPos("G","Tracking...")
    R = cv2.getTrackbarPos("R","Tracking...")

    lr = np.array([LH,LS,LV])
    hr = np.array([HH,HS,HV])
    track[:] = [B,G,R]

    mask_img = cv2.inRange(hsv_img,lr,hr)
    mask_frame = cv2.inRange(hsv_frame,lr,hr)
    mask_frame = cv2.resize(mask_frame,(512,512))

    res = cv2.bitwise_and(img,img,mask=mask_img)
    res_frame = cv2.bitwise_and(frame,frame,mask=mask_frame)


    # cv2.imshow("Image",img)
    # cv2.imshow("HSV_IMG",hsv_img)
    cv2.imshow("MASK_Image",mask_img)
    cv2.imshow("RES",res)
    cv2.imshow("Capture",frame)
    cv2.imshow("RES_Frame",res_frame)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()
