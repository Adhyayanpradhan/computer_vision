from imutils.video import VideoStream
from imutils.video import FPS
import numpy.core.multiarray
import numpy as np
import argparse
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import imutils
import time
import cv2
from imutils.video import FileVideoStream
import numpy as np
#import googlemaps

def video_plate():

    cap = cv2.VideoCapture('test3.mp4')
    while(cap.isOpened()):

        ret, frame = cap.read() 
        #cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
        #cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

        if ret:
            cv2.imshow("Image", frame)
        else:
           #print('no video')
           cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
           

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
cv2.destroyAllWindows()
if __name__=='__video_plate__':
    video_plate()