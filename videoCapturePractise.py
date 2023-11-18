import cv2 as cv

#get file path
videoObject = cv.VideoCapture("videos/parkingVideo.mp4")

#to display we iterate through each frame and display
while True:
    ret, frame = videoObject.read()

    #to check whether the video was read
    if (ret == False):
        break
    else:
        cv.imshow("video-window",frame)

    if (cv.waitKey(7) & 0xFF == ord("q")):
        break

videoObject.release()
cv.destroyAllWindows()




