import cv2
import numpy as np

img = np.zeros((500,500,3))
cv2.rectangle(img,(10,10),(100,100),(111,0,0),5)
cv2.arrowedLine(img,(300,300),(100,100),(0,255,111),3)
cv2.line(img,(100,300),(300,100),(255,0,222),4)
cv2.circle(img,(200,200),100,(0,0,255),10)
cv2.putText(img,"PoornaChand",(200,400),cv2.FONT_HERSHEY_SIMPLEX,1.25,(255,255,255),2)
cv2.imshow('Img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

