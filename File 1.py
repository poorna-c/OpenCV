import cv2
import datetime

img = cv2.imread('samples/lena.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Window1',img)
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('out.avi',fourcc,10,(int(cap.get(3)),int(cap.get(4))))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    dt = datetime.datetime.now()
    cv2.putText(frame,dt.strftime('%d %B,%Y:%I:%M:%S %p'),(10,25),cv2.FONT_HERSHEY_DUPLEX,0.5,(0,255,255),1)
    cv2.imshow('Live Feed',frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    writer.write(frame)
    cv2.imshow('Grayscale',gray)
    if cv2.waitKey(1) & 0xFF in [27,ord('q')]:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()