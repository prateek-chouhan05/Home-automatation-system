# from _future_ import print_function
import paho.mqtt.publish as publish
import string
import random
import urllib.request
import json
from time import sleep
import os
#import homeautomations.settings as settings

string.alphanum = '1234567890avcdefghijklmnopqrstuvwxyzxABCDEFGHIJKLMNOPQRSTUVWXYZ'

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = "1183062"


# The write API key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
writeAPIKey = "4BL5LWW7788ZKUNY"
readAPIKey = 'QYTFZ9UB1E8PU4S6'


# The hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"

# You can use any username.
mqttUsername = "prateek9144"

# Your MQTT API key from Account > My Profile.
mqttAPIKey = "9H688S2LQAEE1DZN"

tTransport = "websockets"
tPort = 80

#field = ['0', '0']

def updateChannel(chNum):
    # Create the  string.
    topic = "channels/" + channelID + "/publish/" + writeAPIKey

    clientID = ''

    channelField = 'field'+str(chNum)
    #print(field[chNum-1])
    prevValue = readData(channelField)
    if(prevValue == '1'): #and field[chNum-1]=='0'):

        command = 'python2 {}on.py'.format(channelField)
        os.system(command)
        #field[chNum-1]=prevValue

    elif(prevValue == '0'): #and field[chNum-1]!='1'):

        command =  'python2 {}off.py'.format(channelField)
        os.system(command)
        #field[chNum-1]=prevValue

def readData(channelField):
    conn = urllib.request.urlopen(
        "http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" % (channelID, readAPIKey))
    response = conn.read()
    #print("http status code=%s" % (conn.getcode()))
    #print(response)
    data = json.loads(response.decode("utf-8"))
    print(channelField, data[channelField])
    conn.close()
    return data[channelField]


while(True):

    updateChannel(1)
    updateChannel(2)

