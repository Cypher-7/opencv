import cv2 as cv
img = cv.imread('wind.jpg')
cv.imshow('wind', img)
capture=cv.VideoCapture('tom.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('s'):
        break

capture.release()
cv.destroyAllWindows()
