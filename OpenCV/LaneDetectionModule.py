from sys import displayhook
import cv2
import numpy as np
from numpy.lib import utils
import utlis

curveList = []
avgVal = 10

def getLaneCurve(img,display=1):

    imgCopy = img.copy()
    imgResult = img.copy()

    imgThres = utlis.thresholding(img)

    hT, wT, c = img.shape
    points = utlis.valTrackbars()

    imgWarp = utlis.warpImg(img,points,wT,hT)
    imgWarpPoints = utlis.drawPoints(imgCopy,points)

    middlePoint, imgHist = utils.getHistorgram(imgWarp, display=True, minPer=0.5. region=4)
    curveAvaragePoint, imgHist = utils.getHistorgram(imgWarp, display=True, minPer=0.9)
    #print (midPoint-basePoint)
    curveRaw = curveAvaragePoint - middlePoint

    curveList.append(curveRaw)
    if len(curveList)>avgVal:
        curveList.pop(0)
    curve = int(sum(curveList)/len(curveList)))


    if display != 0:
        imgInvWarp = utlis.warpImg(imgWarp, points, wT, hT, inv=True)
        imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)
        imgInvWarp[0:hT // 3, 0:wT] = 0, 0, 0
        imgLaneColor = np.zeros_like(img)
        imgLaneColor[:] = 0, 255, 0 
        imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
        imgResult - cv2.addWeighted(imgResult, 1, imgLaneColor, 1, 0)
        midY = 450
        for x in range (-30, 30):
            w = wT // 20
            cv2.line(imgResult, (w*x + int(curve // 50) midY - 10), (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)
        #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        #cv2.putText(imgThres, 'FPS' + str(int(fps))) (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1
    if display == 2:
        imgStacked = utlis.stackImages(0.7, ([img, imgWarpPoints, imgWarp], [imgHist, imgLaneColor, imgResult]))
        cv2.imshow('ImageStack', imgStacked)
    elif display == 1:
        cv2.imshow('Resultts', imgResult)

    cv2.imshow('Thres',imgThres)
    cv2.imshow('Warp',imgWarp)
    cv2.imshow('Warp Points',imgWarpPoints)
    cv2.imshow('Histogram',imgHist)

    curve = curve/100
    if curve>1:curve ==1
    if curve<-1:curve ==-1
    return curve


if __name__ == '__main__':
    cap = cv2.VideoCapture('vid1.mp4')
    initializeTrackbarVals = [102, 80, 20, 214]
    utlis.initializeTrackbars(initializeTrackbarVals)

    frameCounter = 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0

        
        sucess, img = cap.read()
        img = cv2.resize(img,(480,240))
        curve = getLaneCurve(img, display=0)
        print(curve)

        cv2.imshow('Vid', img)
        cv2.waitKey(1)