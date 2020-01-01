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
import face_recognition
#for tracking 
import dlib
import webbrowser
def faceid():

    video_capture = cv2.VideoCapture(0)
    time.sleep(1.0)
    fps = FPS().start()
    writer = None
    my_image = face_recognition.load_image_file("adhyayan.jpg")
    my_image_encoding = face_recognition.face_encodings(my_image)[0]

    # Load a second sample picture and learn how to recognize it.
    biden_image = face_recognition.load_image_file("biden.jpg")
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [
    my_image_encoding,
    biden_face_encoding
    ]
    known_face_names = [
    "adhyayan",
    "Joe Biden"
    ]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
    # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    #if name

                face_names.append(name)
            #print(face_names)
        process_this_frame = not process_this_frame
        """if name='unknown':
                                    f_count = 0
                                    success = 1
                                  
                                    while success:
                                        cv2.imwrite("frame%d.jpg" % f_count, frame) 
                                  
                                        f_count += 1
                                        if f_count==2:
                                            break"""

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        if writer is None:
            # initialize our video writer
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            writer = cv2.VideoWriter('Faces_detected.mp4', fourcc, 5,
                (frame.shape[1], frame.shape[0]), True)

        writer.write(frame)
        # Display the resulting image
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
        fps.update()
    fps.stop()
    #print('number of object detected:',count)
    # do a bit of cleanup
    writer.release()
    cv2.destroyAllWindows()
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
    vs = VideoStream(src=0).start()
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
            
            cv2.putText(frame, "Number of objects detected: " + str(len(idxs)), (0,frame.shape[0] -40), cv2.FONT_HERSHEY_TRIPLEX, 0.7,  (255,255,255), 1)
            cv2.putText(frame, "Estimated Troops to be deployed: " + str(int(len(idxs)-(len(idxs)/2))+1), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.7,  (255,255,255), 1)
            
            count=len(idxs)
            # some information on processing single frame
            # check if the video writer is None
        if writer is None:
            # initialize our video writer
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            writer = cv2.VideoWriter('detected_object_output.mp4', fourcc, 5,
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
    vs = VideoStream(src=0).start()
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
 
def crime():

    os.chdir("/project/computervision/garbage detection/pyPushBullet-master/guns-object-detection/model-20191217T031955Z-001/model/models/research/object_detection") 
    os.system('cmd /k "activate tense"')
    #webbrowser.open('https://colab.research.google.com/drive/1UHLOjjsRWwB1Dhr9SltP9OSK8NABLNrN#scrollTo=-Yw_MrrErRZq')

global main
main=Tk()
main.title("Binary Eagle")
main.geometry("500x500")
main.iconbitmap(r'sosgot_Eoy_icon.ico')

#create a menubar
menubar=Menu(main)
main.config(menu=menubar)

#create the submenu
subMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label='Open')
subMenu.add_command(label='Exit',command=quit)

menubar.add_command(label='Exit',command=quit)
#adding a label
x=Label(main, text="Binary Eagle",font=100)
x.pack()
#adding a button
y=Label(main, text="Welcome to Binary Eagle Basestation",font=60)
y.pack()
Label(main,text="").pack()

Button(main,text="Live Video from drone for pilot view",width=50,command=video).pack()
Label(main,text="").pack()
Button(main,text="Live processing of the area",width=50,command=detection).pack()
Label(main,text="").pack()
Button(main,text="Recognize face from nearby cameras",width=50,command=faceid).pack()
Label(main,text="").pack()
Button(main,text="Weapon detection",width=50,command=crime).pack()


main.mainloop()

