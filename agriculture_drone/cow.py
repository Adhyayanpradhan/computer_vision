import json
import requests
from requests.auth import HTTPBasicAuth
from websocket import create_connection
import argparse
import sys
import os
#from pushbullet.pushbullet import PushBullet
from requests.exceptions import HTTPError
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

#class for api
HOST = "https://api.pushbullet.com/v2"


class PushBullet():
    def __init__(self, apiKey):
        self.apiKey = apiKey

    def _request(self, method, url, postdata=None, params=None, files=None):
        headers = {"Accept": "application/json",
                   "Content-Type": "application/json",
                   "User-Agent": "pyPushBullet"}

        if postdata:
            postdata = json.dumps(postdata)

        r = requests.request(method,
                             url,
                             data=postdata,
                             params=params,
                             headers=headers,
                             files=files,
                             auth=HTTPBasicAuth(self.apiKey, ""))

        r.raise_for_status()
        return r.json()

    def getDevices(self):
        """ Get devices
            https://docs.pushbullet.com/v2/devices

            Get a list of devices, and data about them.
        """

        return self._request("GET", HOST + "/devices")["devices"]

    def pushNote(self, recipient, title, body, recipient_type="device_iden"):

        data = {"type": "note",
                "title": title,
                "body": body}

        data[recipient_type] = recipient
        #data['title']="Threat Detected"

        return self._request("POST", HOST + "/pushes", data)

def detection(net,ln):
	vs = VideoStream(src=1).start()
	time.sleep(1.0)
	fps = FPS().start()
	writer = None
	(W, H) = (None, None)
	count=0
	p_count=0

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
	        
	        cv2.putText(frame, "Number of object detected: " + str(len(idxs)), (0,frame.shape[0] -40), cv2.FONT_HERSHEY_TRIPLEX, 0.7,  (255,255,255), 1)
	        #cv2.putText(frame, "Estimated Troops to be deployed: " + str(int(len(idxs)-(len(idxs)/2))+1), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.7,  (255,255,255), 1)
	        
	        count=len(idxs)
	        # some information on processing single frame
	        # check if the video writer is None
	    if writer is None:
	        # initialize our video writer
	        fourcc = cv2.VideoWriter_fourcc(*"XVID")
	        writer = cv2.VideoWriter('output.mp4', fourcc, 5,
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
	print('number of object detected:',count)
	# do a bit of cleanup
	writer.release()
	cv2.destroyAllWindows()
	vs.stop()
	return count

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
x=detection(net,ln)

def getDevices(args):
    p = PushBullet(args.api_key)
    devices = p.getDevices()
    if args.json:
        print(json.dumps(devices))
        return
    for device in devices:
        if "manufacturer" in device:
            print("%s %s %s" % (device["iden"],
                            device["manufacturer"],
                            device["model"]))
        else:
            print(device["iden"])

def pushNote(args):
    p = PushBullet(args.api_key)
    args.title='Object Detected'
    args.body='Number of objects detected:'+str(x)

    note = p.pushNote(args.device, args.title, " ".join(args.body))
    if args.json:
        print(json.dumps(note))
        return
    if args.device and args.device[0] == '#':
        print("Note broadcast to channel %s" % (args.device))
    elif not args.device:
        print("Note %s sent to all devices" % (note["iden"]))
    else:
        print("Note %s sent to %s" % (note["iden"], note["target_device_iden"]))



parser = argparse.ArgumentParser()
parser.add_argument("--json", default=False, action="store_const", const=True)
parser.add_argument("api_key")
subparser = parser.add_subparsers(dest="type")

getdevices = subparser.add_parser("getdevices", help="Get a list of devices")
getdevices.set_defaults(vars=getDevices)


note = subparser.add_parser("note", help="Send a note")
note.add_argument('device', type=str, help="Device ID")
#note.add_argument('title')
#note.add_argument('body', nargs=argparse.REMAINDER)
note.set_defaults(vars=pushNote)
args = parser.parse_args()
args.vars(args)
