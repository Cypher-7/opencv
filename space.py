import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread('884138.jpg')
def rescaleFrame(frame, scale=0.50):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
rescaled_image=rescaleFrame(img)  
cv.imshow('image', rescaled_image)
#plt.imshow(rescaled_image)
#plt.show()
#BGR to GRAY
gray=cv.cvtColor(rescaled_image,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#BGR to HSV
hsv=cv.cvtColor(rescaled_image,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)
#BGR to LAB
lab=cv.cvtColor(rescaled_image,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)
#BGR to RGB
rgb=cv.cvtColor(rescaled_image,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)
#HSV to BGR
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr',hsv_bgr)
cv.waitKey(0)
