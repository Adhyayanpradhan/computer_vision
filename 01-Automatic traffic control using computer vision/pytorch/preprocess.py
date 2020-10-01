from __future__ import division

import torch 
import torch.nn as nn
import torch.nn.functional as F 
from torch.autograd import Variable
import numpy as np
import cv2 
import matplotlib.pyplot as plt
from util import count_parameters as count
from util import convert2cpu as cpu
from PIL import Image, ImageDraw
from imutils import perspective
import imutils
from skimage.filters import threshold_local
from skimage import measure
from collections import namedtuple
from skimage import segmentation




def letterbox_image(img, inp_dim):
    '''resize image with unchanged aspect ratio using padding'''
    img_w, img_h = img.shape[1], img.shape[0]
    w, h = inp_dim
    new_w = int(img_w * min(w/img_w, h/img_h))
    new_h = int(img_h * min(w/img_w, h/img_h))
    resized_image = cv2.resize(img, (new_w,new_h), interpolation = cv2.INTER_CUBIC)
    
    canvas = np.full((inp_dim[1], inp_dim[0], 3), 128)

    canvas[(h-new_h)//2:(h-new_h)//2 + new_h,(w-new_w)//2:(w-new_w)//2 + new_w,  :] = resized_image
    
    return canvas


        
def prep_image(img, inp_dim):
    """
    Prepare image for inputting to the neural network. 
    
    Returns a Variable 
    """

    orig_im = cv2.imread(img)
    dim = orig_im.shape[1], orig_im.shape[0]
    img = (letterbox_image(orig_im, (inp_dim, inp_dim)))
    img_ = img[:,:,::-1].transpose((2,0,1)).copy()
    img_ = torch.from_numpy(img_).float().div(255.0).unsqueeze(0)
    return img_, orig_im, dim

def prep_image_pil(img, network_dim):
    orig_im = Image.open(img)
    img = orig_im.convert('RGB')
    dim = img.size
    img = img.resize(network_dim)
    img = torch.ByteTensor(torch.ByteStorage.from_buffer(img.tobytes()))
    img = img.view(*network_dim, 3).transpose(0,1).transpose(0,2).contiguous()
    img = img.view(1, 3,*network_dim)
    img = img.float().div(255.0)
    return (img, orig_im, dim)

def inp_to_image(inp):
    inp = inp.cpu().squeeze()
    inp = inp*255
    try:
        inp = inp.data.numpy()
    except RuntimeError:
        inp = inp.numpy()
    inp = inp.transpose(1,2,0)

    inp = inp[:,:,::-1]
    return inp


def find_char_candidates(output , classes , orig_ims):
    LicensePlate = namedtuple("LicensePlateRegion", ["success", "plate", "thresh", "candidates"])
    cnt = 0
    results = []
    for idm , img in enumerate(orig_ims):
        for obj in output:
            if int(obj[0]) == idm :
                cnt += 1
                point1 = np.array(obj[1:3])
                point3 = np.array(obj[3:5])
                point2 = (point3[0] , point1[1])
                point4 = (point1[0] , point3[1])
                lpRegion =np.array([point1 , point2 , point3 , point4]).reshape(4,2)

                plate = perspective.four_point_transform(img, lpRegion)
                V = cv2.split(cv2.cvtColor(plate, cv2.COLOR_BGR2HSV))[2]
                T = threshold_local(V, 29, offset=15, method="gaussian")
                thresh = (V > T).astype("uint8") * 255
                thresh = cv2.bitwise_not(thresh)

                # resize the license plate region to a canonical size
                plate = imutils.resize(plate, width=400)
                thresh = imutils.resize(thresh, width=400)
                # cv2.imshow("Thresh", thresh)
                labels = measure.label(thresh, neighbors=8, background=0)
                charCandidates = np.zeros(thresh.shape, dtype="uint8")
                for label in np.unique(labels):
                    # if this is the background label, ignore it
                    if label == 0:
                        continue

                    # otherwise, construct the label mask to display only connected components for the
                    # current label, then find contours in the label mask
                    labelMask = np.zeros(thresh.shape, dtype="uint8")
                    labelMask[labels == label] = 255
                    cnts = cv2.findContours(labelMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
                                # ensure at least one contour was found in the mask
                    if len(cnts) > 0:
                        # grab the largest contour which corresponds to the component in the mask, then
                        # grab the bounding box for the contour
                        c = max(cnts, key=cv2.contourArea)
                        (boxX, boxY, boxW, boxH) = cv2.boundingRect(c)

                        # compute the aspect ratio, solidity, and height ratio for the component
                        aspectRatio = boxW / float(boxH)
                        solidity = cv2.contourArea(c) / float(boxW * boxH)
                        heightRatio = boxH / float(plate.shape[0])

                        # determine if the aspect ratio, solidity, and height of the contour pass
                        # the rules tests
                        keepAspectRatio = aspectRatio < 1.0
                        keepSolidity = solidity > 0.15
                        keepHeight = heightRatio > 0.4 and heightRatio < 0.95

                        # check to see if the component passes all the tests
                        if keepAspectRatio and keepSolidity and keepHeight:
                            # compute the convex hull of the contour and draw it on the character
                            # candidates mask
                            hull = cv2.convexHull(c)
                            cv2.drawContours(charCandidates, [hull], -1, 255, -1)

                charCandidates = segmentation.clear_border(charCandidates)
                lp = LicensePlate(success=True, plate=plate, thresh=thresh,candidates=charCandidates)
                i = 0 
                lpBox = lpRegion

                lpBox = np.array(lpBox).reshape((-1,1,2)).astype(np.int32)

                

                col , row = thresh.shape

                result= cv2.bitwise_not(cv2.bitwise_and(thresh , thresh , mask = lp.candidates))

                results.append(result)

                # cv2.imshow("result"+str(cnt) , result)
                cv2.imwrite("write"+str(cnt)+".jpg" , result)

    return results









