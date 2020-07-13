# At this point I am testing the wheels (programming them)
# by using the GPIO Pins - as seen in frontwheels.py

import frontwheels.py

front = Front()
running = True
while(running):
    key = input("Enter Direction: ")
    #turn key
    if key == 'r':
        front.turnRight()
        
    elif key == 'l':
        front.turnLeft()
        
    elif key == 's':
        front.straighten()
        
    elif key == 'q':
        print("Quitting...")
        front.cleanup()
        running = False
        print("Cleanup Done")
    else:
        print("Enter a Valid Key")
