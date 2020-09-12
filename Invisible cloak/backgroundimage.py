import cv2
#webcam
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret,image = cap.read()
    if ret:
        cv2.imshow("My window",image)
    key = cv2.waitKey(5)
    if(key == ord("q")):
        #storing it as image.jpg
        cv2.imwrite("image.jpg",image)
        break
cap.release()
cv2.destroyAllWindows()


