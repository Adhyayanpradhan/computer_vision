import cv2

img=cv2.imread('6.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray=cv2.medianBlur(gray,3)
cv2.imwrite('new6.jpg',gray)
