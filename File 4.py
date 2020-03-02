import cv2
import numpy as np

img1 = cv2.imread('samples/lena.jpg')
img2 = cv2.imread('samples/stuff.jpg')

cv2.imshow("Lena",img1)
cv2.imshow("stuff",img2)
b,g,r = cv2.split(img1)
cv2.imshow("Lena_b",b)
cv2.imshow("Lena_g",g)
cv2.imshow("Lena_r",r)
merged_lena = cv2.merge((b,g,r))
cv2.imshow("Merged_Lena",merged_lena)

img1_300 = cv2.resize(img1,(300,300))
img2_300 = cv2.resize(img2,(300,300))

added_imgs = cv2.add(img1_300,img2_300)
cv2.imshow("Added Images",added_imgs)
addW_imgs = cv2.addWeighted(img1_300,0.8,img2_300,0.2,0)
cv2.imshow("Add_Weighted",addW_imgs)




cv2.waitKey(0)
cv2.destroyAllWindows()