import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')
while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        #convert rgb to hsv
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #bgr value for blue
        blue = np.uint8([[[255,0,0]]])
        #hsv value for blue
        hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
        lr = np.array([110,50,50])
        ur = np.array([130,255,255])
        #highlight only blue colour
        mask = cv2.inRange(hsv,lr,ur)
        # all thing that is red
        part1 =cv2.bitwise_and(back, back , mask=mask)
        
        mask = cv2.bitwise_not(mask)
        
        part2 = cv2.bitwise_and(frame,frame,mask= mask )
        cv2.imshow("part2",part1+part2)

    key = cv2.waitKey(5)
    if(key == ord("q")):

        break
cap.release()
cv2.destroyAllWindows()
