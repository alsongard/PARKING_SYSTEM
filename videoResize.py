import cv2 as cv
myVideo = cv.VideoCapture("videos/parkingVideo.mp4")
new_width = 800
new_height = 580

myVideo.set(cv.CAP_PROP_FRAME_WIDTH, new_width)
myVideo.set(cv.CAP_PROP_FRAME_HEIGHT, new_height)
while True:
    ret, frame = myVideo.read()
    if (ret == False):    
        break
    else:
        resizedVideo = cv.resize(frame, (new_width, new_height))
        cv.imshow("resizedVideo", resizedVideo)

    if (cv.waitKey(50) & 0xFF == ord("q")):
        break

myVideo.release()
cv.destroyAllWindows()
