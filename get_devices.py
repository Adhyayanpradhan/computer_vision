import requests
import json

def get_device_api():
    header = {'Authorization':'Bearer <pushbullet-access-token>'}
    dev = requests.get('https://api.pushbullet.com/v2/devices', headers=header)

    dev_json = dev.json()
    #dev_data = json.loads(dev_json)

    for i in range(len(dev_json['devices'])):
        if "manufacturer" in dev_json['devices'][i]:
            print("identity - %s, device name - %s,  model - %s" %(dev_json['devices'][i]['iden'],dev_json['devices'][i]["manufacturer"],dev_json['devices'][i]["model"]))
            return dev_json['devices'][i]['iden']
        else:
            print(dev_json['devices'][i]["iden"])

