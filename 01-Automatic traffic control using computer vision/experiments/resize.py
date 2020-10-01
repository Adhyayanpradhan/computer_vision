import cv2

img = cv2.imread('a2.jpg', 0)
#print(img.shape)
resize_img = cv2.resize(img  , (985 , 268))
cv2.imshow('img' , resize_img)
a=cv2.imwrite('new_a2.jpg',resize_img)
x = cv2.waitKey(0)
if x == 27:
    cv2.destroyWindow('img')
