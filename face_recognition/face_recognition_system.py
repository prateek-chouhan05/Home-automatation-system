import face_recognition
import cv2
import numpy as np
import os
import glob
import paho.mqtt.publish as publish
import string
import random
import urllib.request
import json
from time import sleep

# For thingspeak
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


def updateChannel(chNum, value):
    # Create the  string.
    topic = "channels/" + channelID + "/publish/" + writeAPIKey

    clientID = ''

    channelField = 'field' + str(chNum)

    value = value.lower()
    print(value)

    if ('tanmay' in value):
        newValue = 1
    elif ('prateek' in value):
        newValue = 2
    else:
        newValue = 3
    # Create a random clientID.
    for x in range(1, 16):
        clientID += random.choice(string.alphanum)

    # build the payload string.
    payload = channelField + "=" + str(newValue)

    print(payload)
    # attempt to publish this data to the topic.
    try:
        publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort, auth={
            'username': mqttUsername, 'password': mqttAPIKey})
    except:
        print("There was an error while publishing the data.")
        sleep(1)

# For face recognition
faces_encodings = []
faces_names = []
cur_direc = os.getcwd()
path = os.path.join(cur_direc, 'faces/')
list_of_files = [f for f in glob.glob(path+'*.jpeg')]
number_files = len(list_of_files)
names = list_of_files.copy()


def detect_face(video_capture):
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations( rgb_small_frame)
    face_encodings = face_recognition.face_encodings( rgb_small_frame, face_locations)
    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces (faces_encodings, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance( faces_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = faces_names[best_match_index]
        face_names.append(name)
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Input text label with a name below the face
        cv2.rectangle(frame, (left, bottom - 40), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        name = name[name.rfind('\\')+1:]
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    # Display the resulting image
    cv2.imshow('Video', frame)
    return face_names


def main():
    for i in range(number_files):
        globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
        globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
        faces_encodings.append(globals()['image_encoding_{}'.format(i)])
        # Create array of known names
        names[i] = names[i].replace(os.path.join(cur_direc, 'faces\\'), "").rstrip(".jpeg")
        faces_names.append(names[i])

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    video_capture = cv2.VideoCapture(0)
    while True:
        face_names = detect_face(video_capture)
        if len(face_names) != 0:
            print(face_names[0])
            updateChannel(5, face_names[0])
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()
