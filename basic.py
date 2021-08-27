import cv2 as cv
img = cv.imread('595712.jpg')
cv.imshow('imge',img)

#converting to gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
# blur an image
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blr',blur)

# edge cascade
canny=cv.Canny(img,125,175)
cv.imshow('cnny',canny)

#diolating the image
dilated =cv.dilate(canny,(9,9),iterations=5)
cv.imshow('dilated',dilated)

#eroding
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('eroded',eroded)

#resize
resized =cv.resize(img,(500,500))
cv.imshow('resiz',resized)

#croping
croped=img[50:100,200:400]
cv.imshow('crop',croped)
cv.waitKey(0)