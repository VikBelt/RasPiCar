import RPi.GPIO as GPIO          
from time import sleep

class Back:
    def __init__(self):
        #declare GPIO Pins Used
        self.in1 = 23
        self.in2 = 24
        self.enA = 25
        self.enB = 17
        self.in3 = 27
        self.in4 = 22
        self.temp1=1
        #GPIO setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.in3,GPIO.OUT)
        GPIO.setup(self.in4,GPIO.OUT)
        GPIO.setup(self.enA,GPIO.OUT)
        GPIO.setup(self.enB,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)
        self.p=GPIO.PWM(self.enA,1000)
        self.q=GPIO.PWM(self.enB,1000)
        self.p.start(25)
        self.q.start(25)
    
    #stop function
    def stopCar(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)
    
    #Direction Changes
    #Move Forward
    def backward(self):
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)
        self.temp1=1
    
    #Move Backwards
    def forward(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)
        self.temp1=0
    
    #Speed Modulation
    #slow speed
    def slow(self):
        self.p.ChangeDutyCycle(25)
        self.q.ChangeDutyCycle(25)

    #medium speed
    def medium(self):
        self.p.ChangeDutyCycle(50)
        self.q.ChangeDutyCycle(50)
  
    #fast speed
    def fast(self):
        self.p.ChangeDutyCycle(75)
        self.q.ChangeDutyCycle(75)
    
    #quit and cleanup
    def cleanup(self):
        #stop car
        self.stopCar()
        self.p.stop()
        self.q.stop()
        GPIO.cleanup()
