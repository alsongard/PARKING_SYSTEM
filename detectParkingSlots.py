import cv2 as cv
import pickle

width, height = 46, 92

try:
    with open("CarParkingPosition", "rb") as f:
        posList = pickle.load(f)
except FileNotFoundError:
    posList = []

myImage = cv.imread("photos/oCarSlot.jpg")

def resize(frame, scale=0.50):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def mouseClick(events, x, y, flags, parameter):
    if events == cv.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open("CarParkingPosition", 'wb') as f:
        pickle.dump(posList, f)

cv.namedWindow("detectedParking")
cv.setMouseCallback("detectedParking", mouseClick)

while True:
    resizedImage = resize(myImage)
    for pos in posList:
        cv.rectangle(resizedImage, pos, (pos[0] + width, pos[1] + height), (200, 100, 0), 2)

    cv.imshow("detectedParking", resizedImage)
    
    if (cv.waitKey(3) & 0xFF == ord("q")):
        break


cv.destroyAllWindows()

