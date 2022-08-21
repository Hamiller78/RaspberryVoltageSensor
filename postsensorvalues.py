import os
import requests
import time
import Adafruit_ADS1x15

def getSensorObj():
    adc = Adafruit_ADS1x15.ADS1115()
    GAIN = 1
    values = [0]*4
    for i in range(4):
        values[i] = adc.read_adc(i, gain=GAIN)
    valueObj = { 'values': values }
    return valueObj

def postData(dataObj):
    url = os.environ.get('SENSOR_URL')
    status = requests.post(url, json = dataObj)
    
sensorObj = getSensorObj()
postData(sensorObj)
