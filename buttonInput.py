import Adafruit_BBIO.GPIO as GPIO
import time 

#Plug the button output into this pin
GPIO.setup("P8_12", GPIO.IN)

init_time = 0 #seconds

curr_time = init_time

while True:
	#Read from pin connected to button output
	new_button_state = GPIO.input("P8_12")

	if new_button_state == 1:
		#Reset Timer
		curr_time = 0
		print ("Reset!")
	if new_button_state == 0:
		#Do nothing
		curr_time +=1
	print(curr_time)
	
	#Introduce a delay 
	time.sleep(0.1)
