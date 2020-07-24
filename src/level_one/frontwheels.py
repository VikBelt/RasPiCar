import RPi.GPIO as GPIO
import time

class Front:
    #constructor
    def __init__(self):
        self.center = 6
        self.left = 4
        self.right = 8
        self.turning = False  
        self.servoPIN = 13 #Hardware PWM
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servoPIN, GPIO.OUT)
        self.p = GPIO.PWM(self.servoPIN, 50) # GPIO 13 for PWM with 50Hz
        self.p.start(6) # Initialization
    
    #method to turn right
    def turnRight(self):
        self.turning = True
        self.p.ChangeDutyCycle(self.right)
        time.sleep(.50)
    
    #method to straighten
    def straighten(self):
        self.turning = True
        self.p.ChangeDutyCycle(self.center)
        time.sleep(.50)
    
    #method to turn left
    def turnLeft(self):
        self.turning = True
        self.p.ChangeDutyCycle(self.left)
        time.sleep(.50)
    
    #cleanup GPIO - set #13 LOW 
    def cleanup(self):
        self.turning = False
        self.p.stop()
