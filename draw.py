import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
blank[100:200,200:400]=((0,0,255))
cv.imshow('green',blank)
cv.rectangle(blank,(520,520),(0,0),(0,255,0),thickness=3)
cv.imshow('rectangle',blank)
img = cv.imread('wind.jpg')
cv.imshow('wind', img)
cv.waitKey(0)