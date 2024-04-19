import cv2
import cv2.cv2
import numpy as np
import RPi.GPIO as GPIO
from MotorController import MotorController

cap = cv2.VideoCapture(0)
cap.set(3, 160)
cap.set(4, 120)
controller = MotorController()
controller.ChangeDutyCycle(10)

while True:
    ret, frame = cap.read()
    
    blur = cv2.GaussianBlur(frame,(9,9),0)
    img_split, _, _ = cv2.split(blur)
    thresh = cv2.adaptiveThreshold(blur, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4)
	
    contours, hierarchy = cv2.findContours(thresh, 1, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0 :
        c = max(contours, key=cv2.contourArea)
        
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            print("CX : "+str(cx)+"  CY : "+str(cy))
            if cx >= 120 :
                controller.Right()
                ...
            if cx < 120 and cx > 40 :
                controller.Forward()
                ...
            if cx <=40 :
                controller.Left()
                ...
            cv2.circle(frame, (cx,cy), 5, (255,255,255), -1)
    else :
        controller.Stop()
        ...
    cv2.drawContours(frame, c, -1, (0,255,0), 1)
    cv2.imwrite("stream.jpg", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        controller.Cleanup()
        break
cap.release()
cv2.destroyAllWindows()

