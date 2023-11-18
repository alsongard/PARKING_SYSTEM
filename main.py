import cv2 as cv
import pickle
import cvzone
import numpy as nm
import cv2 as cv
myVideo = cv.VideoCapture("videos/carPark.mp4")

with open("CarParkingPosition", "rb") as f:
    posList = pickle.load(f)

new_width = 640
new_height = 480

myVideo.set(cv.CAP_PROP_FRAME_WIDTH, new_width)
myVideo.set(cv.CAP_PROP_FRAME_HEIGHT, new_height)
while True:
        if (myVideo.get(cv.CAP_PROP_POS_FRAMES) == myVideo.get(cv.CAP_PROP_FRAME_COUNT)):
            myVideo.set(cv.CAP_PROP_POS_FRAMES, 0)
        ret, frame = myVideo.read()
        
        for pos in posList:
            cv.rectangle(frame, pos, (pos[0] + new_width, pos[1] + new_height), (200, 100, 0), 2)
        if (ret == False):    
            break
        else:
            resizedVideo = cv.resize(frame, (new_width, new_height))
            cv.imshow("resizedVideoLoop", resizedVideo)
        if (cv.waitKey(20) & 0xFF == ord("q")):
            break


myVideo.release()
cv.destroyAllWindows()
