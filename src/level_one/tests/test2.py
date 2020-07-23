    #Backwheel Test Case
    import backwheels.py
    
    print("Backwheel Test Case\n")
    running = True
    back_wheel = Back()
    while(running):
        key = input()
        #motion control
        if(key == 'f'):
            back_wheel.forward()

        elif(key == 'b'):
            back_wheel.backward()
            
        #speed control
        elif(key == 'l'):
            back_wheel.slow()
            
        elif(key == 'm'):
            back_wheel.medium()
            
        elif(key == 'h'):
            back_wheel.fast()
        
        #stop and quit
        elif(key == 's'):
            back_wheel.stopCar()
        
        elif(key == 'q'):
            print("Quitting...")
            back_wheel.cleanup()
            print("DONE")
            
        else:
            print("character not recognized")
