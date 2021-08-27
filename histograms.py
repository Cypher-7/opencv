import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img= cv.imread('bost.jpg')
cv.imshow('bost',img)
blank = np.zeros(img.shape[:2],dtype='uint8')
#gray=cv.cvtColor(img,cv.COLOR_BGR2RGB)
#cv.imshow('gray',gray)
circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('mask',circle)
mask = cv.bitwise_and(img,img,mask=circle)
cv.imshow('mask',mask)
#grayscale histogram
#gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])
#plt.figure()
#plt.title('grayscale histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show()
#color histogram
plt.figure()
plt.title('color histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()    

cv.waitKey(0)