import cv2 as cv
img = cv.imread('bost.jpg')
cv.imshow('image',img)
#averaging
average=cv.blur(img,(3,3))
cv.imshow('Average',average)
#gaussian blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('gaussian',gauss)
#median blur
median=cv.medianBlur(img,3)
cv.imshow('median',median)
#bilateral blur
bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('bilateral',bilateral)
cv.waitKey(0)