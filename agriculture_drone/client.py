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
from googletrans import Translator
#defining all subroutines
def browse():
    global filenames
    filename=filedialog.askopenfilename()
def hindi():
    text="hello send me the pictures"
    translator=Translator()
    translations=translator.translate(text,dest='hi')
    print(translations.text)
def contact():
    tkinter.messagebox.showinfo("Expert",'9861101500')
def demo():

    global screen2
    screen2=Toplevel(main)
    screen2.title("KRISHI FOR YOU")
    screen2.geometry("400x350")
    Label(screen2,text="").pack()
    
    Button(screen2,text="PLANT DISEASE",width=15,height=1,command=browse).pack()
    Label(screen2,text="").pack()
    
    Button(screen2,text="CHAT WITH EXPERT",width=15,height=1,command=contact).pack()

def register_user():
    phone_info=phone.get()
    password_info=password.get()

    file=open("phonelog"+".txt","w")
    file.write(phone_info+"\n")
    file.write(password_info)
    file.close()

    phone_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1,text="Registration Sucess",fg="green",font=("calibri",11)).pack()
def register():
    global screen1
    screen1=Toplevel(main)
    screen1.title("Register")
    screen1.geometry("300x250")

    global phone
    global password
    global password_entry
    global phone_entry

    phone=StringVar()
    password=StringVar()

    Label(screen1,text="Please enter details below").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Phone Number * ").pack()
    phone_entry=Entry(screen1,textvariable=phone)
    phone_entry.pack()
    Label(screen1,text="Password * ").pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Register",width=10,height=1,command=register_user).pack()
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
main.title("KRISHI")
main.geometry("500x500")
main.iconbitmap(r'plant_0VY_icon.ico')

#create a menubar
menubar=Menu(main)
main.config(menu=menubar)

#create the submenu
subMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label='Open')
subMenu.add_command(label='Exit',command=quit)

subMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label='Contact Us',command=contact)

#subMenu=Menu(menubar,tearoff=0)
menubar.add_command(label='Register',command=register)

menubar.add_command(label='Exit',command=quit)
#adding a label
x=Label(main, text="KRISHI",font=100)
x.pack()
#adding a button
y=Label(main, text="Choose to continue",font=60)
y.pack()
Button(main,text="Enter the portal",width=30,command=demo).pack()
Label(main,text="").pack()

#Button(main,text="हिन्दी में",width=30,command=hindi).pack()
#Button(main,text="ଓଡ଼ିଆ ରେ",width=30,command=odia).pack()

Button(main,text="Drone Help From Krishi Lab",width=30,command=toll_free).pack()
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
                "body": body}

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
    args.body='phone Number:'+str(m) + 'Coordinates:'+str(n)

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
