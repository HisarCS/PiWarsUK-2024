import pygame
import RPi.GPIO as GPIO
from time import sleep

from MotorController import MotorController

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

controller = MotorController()

try:
    while True:
        for event in pygame.event.get():
            if not (event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYHATMOTION):
                continue
            
            yRight = joystick.get_axis(3)
            yLeft = joystick.get_axis(1)
            button = joystick.get_button(3)
            button1 = joystick.get_button(1)
            
            motorSpeed = int(yRight * 100)
            directionSpeed = int(yLeft * 100)
            
            controller.ChangeDutyCycle(50)
            
            if motorSpeed > 25:
                controller.Forward()
                
            elif motorSpeed < -25:
                controller.Backward()
                
            elif directionSpeed > 25:
                controller.Left()
            
            elif directionSpeed < -25:
                controller.Right()
            
            else:
                controller.Stop()
                
            controller.ChangeDutyCycle(abs(motorSpeed))
            
            if directionSpeed > 10 or directionSpeed <-10:
                controller.ChangeDutyCycle(abs(directionSpeed))
                
        sleep(0.1)
        
except KeyboardInterrupt:
    pass

finally:
    controller.Cleanup()
    pygame.quit()