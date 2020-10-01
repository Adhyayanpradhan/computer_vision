import cv2
import numpy as np
#argparse module helps to write user-friendly command line interfaces
import argparse
#first for the reference image

img=cv2.imread('7.jpg',0)#1-image acquition for reference image
#img1=cv2.imread('new_a2.jpg',0)#1-image acquition for new image

    #grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#2rgb to gray conv.
    #grey1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)#2rgb to gray conv.

    #Why gamma correction is done?
    #Gamma correction function is a function that maps luminance levels
    #to compensate the non-linear luminance effect of display
    #devices (or sync it to human perceptive bias on brightness).
gamma=1.5
    #build a look up table mapping the pixel values[0,255]to their adjusted gamma values
    #lookup table-it is an array that replaces runtime computation with a simpler
    #array indexing operations.Used because it is significant and faster then undergoing
    #expensive operations
invgamma=1.0/gamma
table = np.array([((i / 255.0) ** invgamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
a=cv2.LUT(img,table)#cv2.LUT function take the input image and the table
    #  and find the correct mappings for each pixel value

#b=cv2.LUT(img1, table)#gamma coreection for new image

    # to filter the noise from the image first we have to gaussian blur it
img_gaussian = cv2.GaussianBlur(a, (3, 3), 0)
    #gaussianblur for new image
#img_gaussian1 = cv2.GaussianBlur(b, (3, 3), 0)

    #edge detection is done using prewitt edge detection
    # array is created for the convolution for x direction and y direction
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

    # 2D convolution takes place using cv2.filter2D
    # cv2.filter2D(src,ddepth=-1/cv_16U/cv_32F..,,kernel)
prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
prewitty = cv2.filter2D(img_gaussian, -1, kernely)
prewitt = prewittx + prewitty

    #for 2nd image
#prewittnewx = cv2.filter2D(img_gaussian1, -1, kernelx)
#prewittnewy = cv2.filter2D(img_gaussian1, -1, kernelx)
#prewittnew=prewittnewx+prewittnewy
#cv2.imshow('reference',img)
#cv2.imshow('gamma_reference',a)
#cv2.imshow('edge detection',prewitt)
#cv2.imwrite('edgedaynew1.jpg',prewitt)
#cv2.imshow('newimage',img1)
#cv2.imshow('gamma_new',b)
#cv2.imshow('edge_new',prewittnew)
cv2.imwrite('new7i.jpg',img_gaussian)

x=cv2.waitKey(0)
if x=='b':
    cv2.destroyAllWindows()

