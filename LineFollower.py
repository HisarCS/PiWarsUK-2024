from time import sleep
import cv2
from MotorController import MotorController

cap = cv2.VideoCapture(0)
cap.set(3, 160)
cap.set(4, 120)
controller = MotorController()
controller.ChangeDutyCycle(50)


def main():
    while True:
        ret, frame = cap.read()
        lastTurn = ""

        lower = (0,0,0)
        upper = (20,20,20)
        mask = cv2.inRange(frame, lower, upper)
        contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0 :
            c = max(contours, key=cv2.contourArea)
            
            M = cv2.moments(c)
            if M["m00"] !=0 :
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                if cx >= 120 :
                    lastTurn = "right"
                    controller.Right()
                    
                if cx < 120 and cx > 40 :
                    controller.Forward()
                    
                if cx <=40 :
                    lastTurn = "left"
                    controller.Left()
                    
                cv2.circle(frame, (cx,cy), 5, (255,255,255), -1)
        else :
            if lastTurn == "left":
                controller.LeftInverse()
            if lastTurn == "right":
                controller.RightInverse()
            else:
                controller.Backward()
        cv2.drawContours(frame, c, -1, (0,255,0), 1)
        cv2.imwrite("stream.jpg", frame)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nexiting")
        cap.release()
        controller.Cleanup()
        cv2.destroyAllWindows()