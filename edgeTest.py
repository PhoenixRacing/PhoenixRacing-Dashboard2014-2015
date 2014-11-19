import Adafruit_BBIO.GPIO as GPIO
import time
pin = "P8_12"
debounceTime = .1
GPIO.setup(pin,GPIO.IN)

GPIO.add_event_detect(pin,GPIO.RISING)
previousTime = 0
while True:
	if GPIO.event_detected(pin):

		currentTime = time.time()
		
		if currentTime - previousTime > debounceTime:
			print "EDGE"
			previousTime = time.time()
