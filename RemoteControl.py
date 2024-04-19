import sys
import pygame
import RPi.GPIO as GPIO
from time import sleep

from MotorController import MotorController

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
pwm = 50
controller = MotorController()

try:
    while True:
        for event in pygame.event.get():
            if not (event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYHATMOTION or event.type == pygame.JOYBUTTONDOWN):
                continue
            
            yRight = joystick.get_axis(3)
            yLeft = joystick.get_axis(1)
            
            Trigger_L = joystick.get_button(5)
            Trigger_R = joystick.get_button(4)
            motorSpeed = int(yRight * 100)
            directionSpeed = int(yLeft * 100)
            
            controller.ChangeDutyCycle(pwm)
            
            if directionSpeed > 25:
                controller.Backward()
                
            elif directionSpeed < -25:
                controller.Forward()
                
            elif motorSpeed > 25:
                controller.Right()
            
            elif motorSpeed < -25:
                controller.Left()
            
            else:
                controller.Stop()
            
            
            if Trigger_L == 1 and pwm <= 90:
                pwm += 10
                controller.ChangeDutyCycle(pwm)
                print(pwm)
                sleep(0.5)
                
            elif Trigger_R == 1 and pwm >= 10:
                pwm -= 10
                controller.ChangeDutyCycle(pwm)
                print(pwm)
                sleep(0.5)
        
        sleep(0.1)
except KeyboardInterrupt:
    controller.Cleanup()
    pygame.quit()
    
finally:
    controller.Cleanup()
    pygame.quit()