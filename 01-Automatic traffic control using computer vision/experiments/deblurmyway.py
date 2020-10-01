import cv2
import numpy as np
img=cv2.imread('new7weeee4.jpg',0)
cv2.imshow('image1',img)
kernel=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
img=cv2.filter2D(img,-1,kernel)
cv2.imshow('imshow2',img)
img_as_array=np.asarray(img)
#print(img_as_array)

h=len(img_as_array)#height of the image
w=len(img_as_array[0])#width of the image
#print(img_as_array[0])
#print(height,width)

for i in range(h):
    for j in range(w):
        if img_as_array[i][j]<110:
            img_as_array[i][j]=0
        elif img_as_array[i][j]>=110:
            img_as_array[i][j]=255
#print(img_as_array)
cv2.imshow('image',img_as_array)
cv2.imwrite('newimproved7weeee4.jpg',img_as_array)
cv2.waitKey(0)
cv2.destroyAllWindows()
