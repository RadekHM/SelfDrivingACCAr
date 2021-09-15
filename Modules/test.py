import time
from MotorModule import *    
from UltrasonicModule import *

ultrasonic=Ultrasonic()  
PWM=Motor()  
        
def test_Motor(): 
    try:
        PWM.setMotorModel(1,1,1,1) 
        print ("The car is moving forward")
        time.sleep(1)
        PWM.setMotorModel(-1,-1,-1,-1)  
        print ("The car is going backwards")
        time.sleep(1)
        PWM.setMotorModel(-0.5,-0.5,1,1)     
        print ("The car is turning left")
        time.sleep(1)
        PWM.setMotorModel(1,1,-0.5,-0.5) 
        print ("The car is turning right")  
        time.sleep(1)
        PWM.setMotorModel(0,0,0,0)              
        print ("\nEnd of program")
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")



              
def test_Ultrasonic():
    try:
        while True:
            data=ultrasonic.get_distance()  
            print ("Obstacle distance is "+str(data)+"CM")
            time.sleep(1)
    except KeyboardInterrupt:
        print ("\nEnd of program")


if __name__ == '__main__':

    print ('Program is starting ... ')
    import sys
    if len(sys.argv)<2:
        print ("Parameter error: Please assign the device")
        exit() 

    elif sys.argv[1] == 'Motor':
        test_Motor()
    elif sys.argv[1] == 'Ultrasonic':
        test_Ultrasonic()


        
        
        
        
