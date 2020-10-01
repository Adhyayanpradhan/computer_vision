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
import weather
import detection
import livedronevideo
import googlemaps
import json
import pprint
#import xlsxwriter
import time

def database():
    pass
def forecast():
    #webbrowser.open('https://www.accuweather.com/')
    # importing libraries 
	import pandas as pd 
	import numpy as np 
	import sklearn as sk 
	from sklearn.linear_model import LinearRegression 
	import matplotlib.pyplot as plt 

	# read the cleaned data 
	data = pd.read_csv("austin_final.csv") 

	# the features or the 'x' values of the data 
	# these columns are used to train the model 
	# the last column, i.e, precipitation column 
	# will serve as the label 
	X = data.drop(['PrecipitationSumInches'], axis = 1) 

	# the output or the label. 
	Y = data['PrecipitationSumInches'] 
	# reshaping it into a 2-D vector 
	Y = Y.values.reshape(-1, 1) 

	# consider a random day in the dataset 
	# we shall plot a graph and observe this 
	# day 
	day_index = 798
	days = [i for i in range(Y.size)] 

	# initialize a linear regression classifier 
	clf = LinearRegression() 
	# train the classifier with our 
	# input data. 
	clf.fit(X, Y) 

	# give a sample input to test our model 
	# this is a 2-D vector that contains values 
	# for each column in the dataset. 
	inp = np.array([[74], [60], [45], [67], [49], [43], [33], [45], 
					[57], [29.68], [10], [7], [2], [0], [20], [4], [31]]) 
	inp = inp.reshape(1, -1) 

	# print the output. 
	print('The precipitation in inches for the input is:', clf.predict(inp))
	

	# plot a graph of the precipitation levels 
	# versus the total number of days. 
	# one day, which is in red, is 
	# tracked here. It has a precipitation 
	# of approx. 2 inches. 
	print("the precipitation trend graph: ") 
	plt.scatter(days, Y, color = 'b') 
	plt.scatter(days[day_index], Y[day_index], color ='r') 
	plt.title("Precipitation level") 
	plt.xlabel("Days") 
	plt.ylabel("Precipitation in inches") 


	plt.show()
	from tkinter import messagebox
	if clf.predict(inp) > 1.1:
		messagebox.showinfo("Warning", "Flood Alert")

def message():
    pass
def live():
    livedronevideo.video()
def detect():
    detection.people()
def satellite():
    webbrowser.open('D:/project/computervision/garbage detection/pyPushBullet-master/sih/Cyclone_Wildfire_Flood_Earthquake_Database/Cyclone_Wildfire_Flood_Earthquake_Database/Cyclone')
def pre():
    global screen2
    screen2=Toplevel(main)
    screen2.title("PRE DISASTER PORTAL")
    screen2.geometry("500x400")
    screen2.iconbitmap(r'sosgot_Eoy_icon.ico')
    Label(screen2,text="").pack()
    y=Label(screen2, text="Welcome to PRE DISASTER Portal",font=60)
    y.pack()
    Label(screen2,text="").pack()    
    Button(screen2,text="Weather Forcast",width=30,height=1,command=forecast,bg='black',fg='white',borderwidth=3).pack()
    Label(screen2,text="").pack()
    Label(screen2, text="Click below and ",font=20).pack()
    Label(screen2,text="info will be send to rescue teams and victims",font=20).pack()
    Label(screen2,text="").pack()
    Button(screen2,text="Send pre-disaster info",width=30,height=1,command=toll_free,bg='black',fg='white',borderwidth=3).pack()
    Label(screen2,text="").pack()
    Button(screen2,text="Disaster analysis using satellite images",width=30,height=1,command=satellite,bg='black',fg='white',borderwidth=3).pack()
    Label(screen2,text="").pack()
   # Button(screen2,text="CHAT WITH EXPERT",width=15,height=1,command=contact).pack()
def near():
    API_KEY = 'AIzaSyCcG16PjfaMY3O59NPzp0DkSDWH8J6juQA'

    # Define the Client
    gmaps = googlemaps.Client(key = API_KEY)

    # Do a simple nearby search where we specify the location
    # in lat/lon format, along with a radius measured in meters
    places_result  = gmaps.places_nearby(location='21.4971,83.9038', radius = 40000, open_now =False , type = 'hospital')

    time.sleep(3)

    place_result  = gmaps.places_nearby(page_token = places_result['next_page_token'])

    stored_results = []

    # loop through each of the places in the results, and get the place details.      
    for place in places_result['results']:

        # define the place id, needed to get place details. Formatted as a string.
        my_place_id = place['place_id']

        # define the fields you would liked return. Formatted as a list.
        my_fields = ['name','formatted_phone_number','website']

        # make a request for the details.
        places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)

        # print the results of the details, returned as a dictionary.
        pprint.pprint(places_details['result'])

        # store the results in a list object.
        stored_results.append(places_details['result'])
def during():
    global screen3
    screen3=Toplevel(main)
    screen3.title("DURING THE DISASTER PORTAL")
    screen3.geometry("500x400")
    screen3.iconbitmap(r'sosgot_Eoy_icon.ico')
    Label(screen3,text="").pack()
    y=Label(screen3, text="Welcome to DURING THE DISASTER Portal",font=60)
    y.pack()
    Label(screen3,text="").pack()    
    Button(screen3,text="Live Video From Drone",width=30,height=1,command=live,bg='black',fg='white',borderwidth=3).pack()
    Label(screen3,text="").pack()
    
    Label(screen3,text="").pack()
    Button(screen3,text="Locating people in a disaster",width=30,height=1,command=detect,bg='black',fg='white',borderwidth=3).pack()
    Label(screen3,text="").pack()
    Label(screen3,text="").pack()

    Button(screen3,text="Locating safe places in a disaster",width=30,height=1,command=near,bg='black',fg='white',borderwidth=3).pack()
    Label(screen3,text="").pack()
    Label(screen3,text="").pack()

    Button(screen3,text="Auto-retrieval of locations",width=30,height=1,command=detect,bg='black',fg='white',borderwidth=3).pack()
    Label(screen3,text="").pack()
def three():
    webbrowser.open("file:///D:/project/computervision/garbage%20detection/pyPushBullet-master/sih/earthquake.html")

def modelling():
    global screen5
    screen5=Toplevel(main)
    screen5.title("POST Disaster Portal")
    screen5.geometry("500x400")
    screen5.iconbitmap(r'sosgot_Eoy_icon.ico')
    Label(screen5,text="").pack()
    y=Label(screen5, text="Welcome to 3D modelling Portal",font=60)
    y.pack()
    Label(screen5,text="").pack()    
    Button(screen5,text="3D model of Earthqake",width=30,height=1,command=three,bg='black',fg='white',borderwidth=3).pack()
    Label(screen5,text="").pack()

def damage():
    webbrowser.open("https://colab.research.google.com/drive/1UHLOjjsRWwB1Dhr9SltP9OSK8NABLNrN#scrollTo=GStNeHWPkTcN")

"""def blockage():
    pass"""
"""def image_comparision():
    r = requests.post(
    "https://api.deepai.org/api/image-similarity",
    files={
        'image1': open('D:/project/computervision/garbage detection/pyPushBullet-master/sih/1.jpg', 'rb'),
        'image2': open('D:/project/computervision/garbage detection/pyPushBullet-master/sih/2.jpg', 'rb'),
    },
    headers={'api-key': '3aa162a2-f3e8-4863-8abd-69246e217a66'}
    )
    print(r.json())"""
def post():
    global screen4
    screen4=Toplevel(main)
    screen4.title("POST Disaster Portal")
    screen4.geometry("500x400")
    screen4.iconbitmap(r'sosgot_Eoy_icon.ico')
    Label(screen4,text="").pack()
    y=Label(screen4, text="Welcome to POST Disaster Portal",font=60)
    y.pack()
    Label(screen4,text="").pack()    
    Button(screen4,text="3D model of the area after disaster",width=30,height=1,command=modelling,bg='black',fg='white',borderwidth=3).pack()
    Label(screen4,text="").pack()
    
    Label(screen4,text="").pack()
    Button(screen4,text="Damage Estimation",width=30,height=1,command=damage,bg='black',fg='white',borderwidth=3).pack()
    Label(screen4,text="").pack()
    Label(screen4,text="").pack()
    """Button(screen4,text="Image Comparision",width=30,height=1,command=image_comparision,bg='black',fg='white',borderwidth=3).pack()
                Label(screen4,text="").pack()
                Label(screen4,text="").pack()"""

    """Button(screen4,text="Scaning the area to find road blockage",width=30,height=1,command=blockage,bg='black',fg='white',borderwidth=3).pack()
                Label(screen4,text="").pack()
                Label(screen4,text="").pack()"""



def updates():
    pass
def phone():
    with open("phonelog.txt",'rt') as myfile:
        for myline in myfile:
            k=myline
            break
    #m=coordinate()
    return k

#making a gui
def coordinate():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(executable_path = 'D:/project/computervision/garbage detection/pyPushBullet-master/chromedriver_win32/chromedriver.exe', chrome_options=options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()
    #k=phone()
    return (latitude,longitude)
def toll_free():
    z=phone()
    l=coordinate()
    return z,l
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

Button(main,text="Database",width=30,command=database,borderwidth=6,bg='black',fg='white').pack()
Label(main,text="").pack()
Label(main,text="").pack()
Button(main,text="Pre Disaster",width=20,command=pre,borderwidth=3,bg='#000fff000',fg='black').pack()
Label(main,text="").pack()
"""Button(main,text="Recognize face from nearby cameras",width=50,command=faceid).pack()
Label(main,text="").pack()
Button(main,text="Weapon detection",width=50,command=crime).pack()"""
Button(main,text="During Disaster",width=20,command=during,borderwidth=3,bg='red',fg='black').pack()
Label(main,text="").pack()
Button(main,text="Post Disaster",width=20,command=post,borderwidth=3,bg='black',fg='white').pack()
Label(main,text="").pack()
Label(main,text="").pack()
Button(main,text="Live updates",width=30,command=updates,borderwidth=6,bg='black',fg='white').pack()
Label(main,text="").pack()

main.mainloop()

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
        """ Push a note
            https://docs.pushbullet.com/v2/pushes

            Arguments:
            recipient -- a recipient
            title -- a title for the note
            body -- the body of the note
            recipient_type -- a type of recipient (device, email, channel or client)
        """

        data = {"type": "note",
                "title": title,
                "body": body
                }

        data[recipient_type] = recipient
        #data['title']="Threat Detected"

        return self._request("POST", HOST + "/pushes", data)
    def pushNotephone(self, recipient, title, body, recipient_type="device_iden"):
        """ Push a note
            https://docs.pushbullet.com/v2/pushes

            Arguments:
            recipient -- a recipient
            title -- a title for the note
            body -- the body of the note
            recipient_type -- a type of recipient (device, email, channel or client)
        """

        data = {"type": "number",
                "title": title,
                "body": body
                }

        data[recipient_type] = recipient
        #data['title']="Threat Detected"

        return self._request("POST", HOST + "/pushes", data)

m,n=toll_free()
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
    args.title='phone number and coordinate of the user'
    args.body='phone Number:'+str(m) + 'at GPS Coordinates:'+str(n)+'Cyclone is comming. Go to the safe place'

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

def pushNotephone(args):
    p = PushBullet(args.api_key)
    args.title='phone number and coordinate of the user'
    args.body='phone Number:'+str(o) + 'needs help immediately. Open face recognition of nearby camera.'

    number = p.pushNote(args.device, args.title, " ".join(args.body))
    if args.json:
        print(json.dumps(number))
        return
    if args.device and args.device[0] == '#':
        print("Note broadcast to channel %s" % (args.device))
    elif not args.device:
        print("Note %s sent to all devices" % (number["iden"]))
    else:
        print("Note %s sent to %s" % (number["iden"], number["target_device_iden"]))

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

number = subparser.add_parser("number", help="Send a note")
number.add_argument('device', type=str, help="Device ID")
#note.add_argument('title')
#note.add_argument('body', nargs=argparse.REMAINDER)
number.set_defaults(vars=pushNotephone)
args = parser.parse_args()
args.vars(args)
