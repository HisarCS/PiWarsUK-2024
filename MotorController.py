import time
import RPi.GPIO as GPIO
import configuration
class MotorController():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
        #Right Motor Setup
        GPIO.setup(configuration.R_EN1, GPIO.OUT)
        GPIO.setup(configuration.R_EN2, GPIO.OUT)
        GPIO.setup(configuration.R_IN1, GPIO.OUT)
        GPIO.setup(configuration.R_IN2, GPIO.OUT)
        GPIO.setup(configuration.R_IN3, GPIO.OUT)
        GPIO.setup(configuration.R_IN4, GPIO.OUT)
        
        self.R_EN1_PWM = GPIO.PWM(configuration.R_EN1, 100)
        self.R_EN2_PWM = GPIO.PWM(configuration.R_EN2, 100)
        self.R_EN1_PWM.start(0)
        self.R_EN2_PWM.start(0)
        
        GPIO.output(configuration.R_IN1, GPIO.LOW)
        GPIO.output(configuration.R_IN2, GPIO.LOW)
        GPIO.output(configuration.R_IN3, GPIO.LOW)
        GPIO.output(configuration.R_IN4, GPIO.LOW)
        
        
        #Left Motor Setup
        GPIO.setup(configuration.L_EN1, GPIO.OUT)
        GPIO.setup(configuration.L_EN2, GPIO.OUT)
        GPIO.setup(configuration.L_IN1, GPIO.OUT)
        GPIO.setup(configuration.L_IN2, GPIO.OUT)
        GPIO.setup(configuration.L_IN3, GPIO.OUT)
        GPIO.setup(configuration.L_IN4, GPIO.OUT)
        
        self.L_EN1_PWM = GPIO.PWM(configuration.L_EN1, 100)
        self.L_EN2_PWM = GPIO.PWM(configuration.L_EN2, 100)
        self.L_EN1_PWM.start(0)
        self.L_EN2_PWM.start(0)
        
        GPIO.output(configuration.L_IN1, GPIO.LOW)
        GPIO.output(configuration.L_IN2, GPIO.LOW)
        GPIO.output(configuration.L_IN3, GPIO.LOW)
        GPIO.output(configuration.L_IN4, GPIO.LOW)
    
    def ChangeDutyCycle(self, dutyCycle):
        # Right
        self.R_EN1_PWM.ChangeDutyCycle(dutyCycle)
        self.R_EN2_PWM.ChangeDutyCycle(dutyCycle)
        
        # Left
        self.L_EN1_PWM.ChangeDutyCycle(dutyCycle)
        self.L_EN2_PWM.ChangeDutyCycle(dutyCycle)

    def __L_Forward__(self):
        GPIO.output(configuration.L_IN1, GPIO.HIGH)
        GPIO.output(configuration.L_IN2, GPIO.LOW)
        GPIO.output(configuration.L_IN3, GPIO.HIGH)
        GPIO.output(configuration.L_IN4, GPIO.LOW)
        
    def __R_Forward__(self):
        GPIO.output(configuration.R_IN1, GPIO.HIGH)
        GPIO.output(configuration.R_IN2, GPIO.LOW)
        GPIO.output(configuration.R_IN3, GPIO.HIGH)
        GPIO.output(configuration.R_IN4, GPIO.LOW)
        
        
    def __L_Backward__(self):
        GPIO.output(configuration.L_IN1, GPIO.LOW)
        GPIO.output(configuration.L_IN2, GPIO.HIGH)
        GPIO.output(configuration.L_IN3, GPIO.LOW)
        GPIO.output(configuration.L_IN4, GPIO.HIGH)
        

    def __R_Backward__(self):
        GPIO.output(configuration.R_IN1, GPIO.LOW)
        GPIO.output(configuration.R_IN2, GPIO.HIGH)
        GPIO.output(configuration.R_IN3, GPIO.LOW)
        GPIO.output(configuration.R_IN4, GPIO.HIGH)
        
    def __L_Stop__(self):
        GPIO.output(configuration.L_IN1, GPIO.LOW)
        GPIO.output(configuration.L_IN2, GPIO.LOW)
        GPIO.output(configuration.L_IN3, GPIO.LOW)
        GPIO.output(configuration.L_IN4, GPIO.LOW)
        
    def __R_Stop__(self):
        GPIO.output(configuration.R_IN1, GPIO.LOW)
        GPIO.output(configuration.R_IN2, GPIO.LOW)
        GPIO.output(configuration.R_IN3, GPIO.LOW)
        GPIO.output(configuration.R_IN4, GPIO.LOW)
        
    def Forward(self):
        self.__L_Forward__()
        self.__R_Forward__()
    
    def Backward(self):
        self.__L_Backward__()
        self.__R_Backward__()
        
    def Right(self):
        self.__L_Forward__()
        self.__R_Backward__()
    
    def Left(self):
        self.__L_Backward__()
        self.__R_Forward__()
        
    def Stop(self):
        self.__L_Stop__()
        self.__R_Stop__()
        
    def Cleanup(self):
        GPIO.cleanup()
        
def test():
    contoller = MotorController()
    contoller.ChangeDutyCycle(100)
    contoller.Forward()
    time.sleep(3)
    contoller.Stop()
test()