from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import json
import requests
from requests.auth import HTTPBasicAuth
from websocket import create_connection
import argparse
import sys
import os
#from pushbullet.pushbullet import PushBullet
from requests.exceptions import HTTPError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from googletrans import Translator
#defining all subroutines
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
import webbrowser
import pandas as pd

from openpyxl import load_workbook
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import plotly.express as px

def ploting_excel():
    rain=pd.read_csv('D:/project/computervision/garbage detection/pyPushBullet-master/agrifinalyear/d_rain.csv')
    #print(rain.head())
    #fig = plt.figure()
    """ax = fig.add_subplot(222)
                bx = fig.add_subplot(212)"""
    fig,ax=plt.subplots(2)
    ax[0].scatter(rain['ANNUAL'],rain['STATE_UT_NAME'])
    ax[1].scatter(rain['ANNUAL'],rain['DISTRICT'])

    ax[0].set_title('DROUGT ANALYSIS USING RAINFALL')
    #bx.set_title('Epic Info')

    ax[0].set_ylabel('STATE_UT_NAME')
    ax[1].set_ylabel('DISTRICT')

    #ax[0].set_xlabel('ANNUAL')
    ax[1].set_xlabel('ANNUAL')

    plt.show()
def ploting_excel_again():
    rain=pd.read_csv('D:/project/computervision/garbage detection/pyPushBullet-master/agrifinalyear/d_rain.csv')
    #print(rain.head())
    #ax = plt
    bx = plt
    
    #ax.scatter(rain['ANNUAL'],rain['STATE_UT_NAME'])
    bx.scatter(rain['ANNUAL'],rain['DISTRICT'])

    #ax.title('Epic Info')
    bx.title('Epic Info')

    #ax.ylabel('STATE_UT_NAME')
    bx.ylabel('DISTRICT')

    #ax.xlabel('ANNUAL')
    bx.xlabel('ANNUAL')

    plt.show()


def image():
    webbrowser.open('https://colab.research.google.com/drive/1UHLOjjsRWwB1Dhr9SltP9OSK8NABLNrN#scrollTo=GStNeHWPkTcN')

def flooding_plant():
    webbrowser.open('https://colab.research.google.com/drive/1rn_3hVQ8kWkFp-BEvxmlLzCWhp2yOMOp#scrollTo=GStNeHWPkTcN')

def togovtportal():
    webbrowser.open('https://plants.sc.egov.usda.gov/java/')
def detection():
    LABELS = open("coco.names").read().strip().split("\n")
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
        dtype="uint8")
    print("[INFO] loading YOLO from disk...")
    net = cv2.dnn.readNetFromDarknet("yolov3.cfg", "yolov3.weights")
    ln = net.getLayerNames()
    #print('ln',ln)
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    #print('ln ',ln)
    print("[INFO] starting video stream...")
    vs = FileVideoStream("cow.mp4").start()
    time.sleep(1.0)
    fps = FPS().start()
    writer = None
    (W, H) = (None, None)

    while True:
        # grab the frame from the thr
        # read the next frame from the file
        frame = vs.read()
        frame=imutils.resize(frame,width=412)
        # if the frame dimensions are empty, grab them
        if W is None or H is None:
            (H, W) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
            swapRB=True, crop=False)
        net.setInput(blob)
        start = time.time()
        layerOutputs = net.forward(ln)
        #print(layerOutputs)
        end = time.time()

        # initialize our lists of detected bounding boxes, confidences,
        # and class IDs, respectively
        boxes = []
        confidences = []
        classIDs = []

        # loop over each of the layer outputs
        for output in layerOutputs:
            # loop over each of the detections
            for detection in output:
                # extract the class ID and confidence (i.e., probability)
                # of the current object detection
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]
                if confidence > 0.5:
                    
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")
                    # use the center (x, y)-coordinates to derive the top
                    # and and left corner of the bounding box
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    # update our list of bounding box coordinates,
                    # confidences, and class IDs
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)
                    #print(classID)
                    
                    """elif classID==1 or classID==2 or classID==3 or classID==4 or classID==5 or classID==6 or classID==7 or classID==67:
                                                                                    print('go')"""
            # apply non-maxima suppression to suppress weak, overlapping
        # bounding boxes

        idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5,
            0.3)
        #print(idxs)
        # ensure at least one detection exists
        if len(idxs) > 0:
            # loop over the indexes we are keeping
            for i in idxs.flatten():
                #print(i)
                # extract the bounding box coordinates
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])

                # draw a bounding box rectangle and label on the frame
                color = [int(c) for c in COLORS[classIDs[i]]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                text = "{}: {:.4f}".format(LABELS[classIDs[i]],
                    confidences[i])
                cv2.putText(frame, text, (x, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            
            cv2.putText(frame, "Number of cows detected: " + str(len(idxs)), (0,frame.shape[0] -40), cv2.FONT_HERSHEY_TRIPLEX, 0.7,  (255,255,255), 1)
            #cv2.putText(frame, "Estimated Troops to be deployed: " + str(int(len(idxs)-(len(idxs)/2))+1), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.7,  (255,255,255), 1)
            
            count=len(idxs)
            # some information on processing single frame
            # check if the video writer is None
        if writer is None:
            # initialize our video writer
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            writer = cv2.VideoWriter('cow_output.mp4', fourcc, 5,
                (frame.shape[1], frame.shape[0]), True)
            
        # show the output frame
        writer.write(frame)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

        # update the FPS counter
        fps.update()
    fps.stop()
    #print('number of object detected:',count)
    # do a bit of cleanup
    writer.release()
    cv2.destroyAllWindows()
    vs.stop()
def video():
    print("[INFO] starting video stream...")
    vs = VideoStream(src=1).start()
    time.sleep(1.0)
    fps = FPS().start()
    writer = None
    (W, H) = (None, None)
    while True:
        # grab the frame from the thr
        # read the next frame from the file
        frame = vs.read()
        frame=imutils.resize(frame,width=912)
        # if the frame dimensions are empty, grab them
        if W is None or H is None:
            (H, W) = frame.shape[:2]
        if writer is None:
            # initialize our video writer
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            writer = cv2.VideoWriter('live_video.mp4', fourcc, 5,
                (frame.shape[1], frame.shape[0]), True)
            
        # show the output frame
        writer.write(frame)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        fps.update()
    fps.stop()
    # do a bit of cleanup
    writer.release()
    cv2.destroyAllWindows()
    vs.stop()
    
global main
main=Tk()
main.title("AgriVision")
main.geometry("500x500")
main.iconbitmap(r'plant_0VY_icon.ico')

#create a menubar
menubar=Menu(main)
main.config(menu=menubar)

#create the submenu
subMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label='Open',command=togovtportal)
subMenu.add_command(label='Exit',command=quit)

menubar.add_command(label='Exit',command=quit)
#adding a label
x=Label(main, text="KRISHI",font=100)
x.pack()
#adding a button
y=Label(main, text="Welcome to KRISHI LAB Basestation",font=60)
y.pack()
Button(main,text="Live Video from drone for pilot view",width=50,command=video).pack()
Label(main,text="").pack()
Button(main,text="Live processing of field",width=50,command=detection).pack()
Label(main,text="").pack()
Button(main,text="R&D on plant diseases",width=50,command=image).pack()
Label(main,text="").pack()
Button(main,text="Detecting flooding crop and healthy crop",width=50,command=flooding_plant).pack()
Label(main,text="").pack()
Button(main,text="Rainfall Pattern",width=50,command=ploting_excel).pack()
Label(main,text="").pack()


main.mainloop()

