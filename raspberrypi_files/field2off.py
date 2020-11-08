import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)

GPIO.output(15, GPIO.HIGH)
