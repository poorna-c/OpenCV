# OpenCV


cv2.imread()
cv2.imshow()
cv2.waitKey()
cv2.destroyAllWindows()
cv2.destroyAllWindow('Window_Name')
VideoCapture()
VideoCapture().isOpened()
VideoCapture().read()
VideoCapture().get(PROPERTY_NAME)
VideoCapture().release()

cv2.VideoWriter_fourcc('*XVID')
cv2.VideoWriter('out.avi',fourcc,frames/sec,(wid,hei))

cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.line(),arrowedLine(),rectangle(),circle(),putText(img,'text',(x,y),font,font_scale,(r,g,b),thickness,line_type)






1. Reading and Writing Images
	cv2.imread()
	cv2.imwrite()
2. Reading through WebCam
	cv2.VideoCapture()
	cv2.VideoWriter()
