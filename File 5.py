import cv2
import numpy as np

mask = np.zeros([500,1000,3],np.uint8)

# mask[:,500:] = (mask[:,500:]+1)*255
# cv2.imshow('w',mask)
# cv2.imwrite('file.png',mask)

img = cv2.imread('file.png')
# mask[0:150,400:600] = (mask[:150,400:600]+1) * 255
cv2.rectangle(mask,(400,0),(600,150),(255,255,255),-1)
not_img = cv2.bitwise_not(mask)
or_img = cv2.bitwise_or(mask,img)
and_img = cv2.bitwise_and(img,mask)

cv2.imshow('Window1',img)
cv2.imshow('Window2',mask)
cv2.imshow("Not_Img",not_img)
cv2.imshow("Or_Img",or_img)
cv2.imshow("And_Img",and_img)
cv2.bitwise_or
cv2.waitKey(0)
cv2.destroyAllWindows()