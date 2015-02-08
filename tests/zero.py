#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

ZERO = 22


GPIO.setup(ZERO, GPIO.IN)

try:
	while True:
		status = GPIO.input(ZERO)
		if status:
			print "Aperto"
		else:
			print "Occluso"
		time.sleep(0.1)
except KeyboardInterrupt:
	pass



GPIO.cleanup()
