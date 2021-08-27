import cv2 as cv
img = cv.imread('wind.jpg')
cv.imshow('wind', img)
def rescaleFrame(frame, scale=0.50):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
rescaled_image=rescaleFrame(img)    
cv.imshow('image', rescaled_image)
# only work for live videos
def chaneRes(width,heigth):
    capture.set(3,width)
    capture.set(4,heigth)

capture=cv.VideoCapture('tom.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=0.75)
    cv.imshow('Video',frame)
    cv.imshow('video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('s'):
        break

capture.release()
cv.destroyAllWindows()