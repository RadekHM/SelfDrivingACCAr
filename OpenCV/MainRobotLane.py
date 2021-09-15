from MotorModule import Motor
from LaneDetectionModule import getLaneCurve
import WebcamModule
import cv2

motor = Motor(2,3,4,17,22,27)



def main():

    img = WebCamModule.getImg()
    curveVal= getLaneCurve(img,1)

    sen = 1.3
    maxVal = 0.3
    if curveVal>maxVal:curveVal=maxVal
    if curveVal<-maxVal:curveVal=-maxVal

    if curveVal>0:
        sen=1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0

    motor.move(0.20, -curveVal*sen,0.05)
    cv2.waitKey(1)

if __name__=='__main__':
    while True:
        main()