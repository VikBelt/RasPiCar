from backwheels import Back
from frontwheels import Front

class Car:
    #constructor
    def __init__(self):
        self.frontWheels = Front()
        self.backWheels = Back()
    
    #car direction
    def drive(self):
        self.backWheels.forward()
        
    def reverse(self):
        self.backWheels.backward()
    
    def right(self):
        self.frontWheels.turnRight()
        
    def straight(self):
        self.frontWheels.straighten()
        
    def left(self):
        self.frontWheels.turnLeft()
        
    #car speed
    def slow(self):
        self.backWheels.slow()
        
    def normal(self):
        self.backWheels.medium()
        
    def fast(self):
        self.backWheels.fast()
    
    def end(self):
        self.frontWheels.cleanup()
        self.backWheels.cleanup()
