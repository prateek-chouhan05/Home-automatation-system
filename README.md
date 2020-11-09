# Home Automation and Facial Recognition security with Raspberry Pi 

This project was designed as a part of the IoT Course. The backend has been designed in django, and currently a thingspeak channel is being used as the endpoint for communication between the raspi and the server
You could make your own REST server to reduce response times and push times. Also, we have used facial recognition for security. 

# Features!

  - Control devices from any location
  - Facial recognition without any external training time
  

### Tech
Home Automation uses the following:

* Django - as the backend for the services
* paho-mqtt - for communication with the thingspeak channel
* RPi.GPIO - for communicating with the GPIO Pins on the Raspi
* OpenCV2 - for facial recognition
* face_recognition - for facial encodings
* requests - to communicate with the rest server


### Installation for the server
Home Automation requires django 2.6 to run.

For linux users
```sh
$ git clone https://github.com/Prateek9144/Home-automatation-system.git
$ cd Home-automatation-system
$ sudo pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

For windows users with conda
```sh
$ git clone https://github.com/Prateek9144/Home-automatation-system.git
$ cd Home-automatation-system
$ conda create -n myenv python=3.8
$ conda activate myenv
$ pip install -r requirements.txt
```

To test the app

```sh
$ python manage.py makemigrations ranklist && python manage.py migrate
$ python manage.py runserver
```
Open a browser tab and write http://localhost:8000/ to see the website.

If you want to deploy the app, you can use the following tutorial to deploy it on an AWS EC2 machine using apache - [tutorial](https://medium.com/saarthi-ai/ec2apachedjango-838e3f6014ab) 

### Installation for raspi
Ensure you have python3 with pip 20.x setup on your pi. You might have to build python from source because 

```sh
$ git clone https://github.com/Prateek9144/Home-automatation-system.git
$ cd Home-automatation-system/raspberrypi_files
$ pip install -r requirements.txt
$ python3 get_status.py
```

### Updates to be done
1) Bump up django to 3.0
2) Make a REST Server to remove thingspeak requirement
3) Add facial recognition to raspberry pi instead of personal device


Contributors - [Tanmay Ambadkar](https://github.com/TanmayAmbadkar), [Prateek Chouhan](https://github.com/Prateek9144), [Pushkar Patel](https://github.com/thepushkarp)
