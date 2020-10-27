# from _future_ import print_function
import paho.mqtt.publish as publish
import psutil
import string
import random
import urllib.request
import json
import numpy as np
from time import sleep

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


def updateChannel(chNum):
    # Create the  string.
    topic = "channels/" + channelID + "/publish/" + writeAPIKey

    clientID = ''

    channelField = 'field'+str(chNum)

    prevValue = readData(channelField)
    print(prevValue)
    if(prevValue == '1'):
        newValue = 0
    else:
        newValue = 1
    # Create a random clientID.
    for x in range(1, 16):
        clientID += random.choice(string.alphanum)

    # build the payload string.
    payload = channelField+"=" + str(newValue)

    print(payload)
    # attempt to publish this data to the topic.
    try:
        publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort, auth={
            'username': mqttUsername, 'password': mqttAPIKey})

    except:
        print("There was an error while publishing the data.")
        sleep(1)


def readData(channelField):
    conn = urllib.request.urlopen(
        "http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" % (channelID, readAPIKey))
    response = conn.read()
    print("http status code=%s" % (conn.getcode()))
    data = json.loads(response)
    # print(data)
    conn.close()
    return data[channelField]
