#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ZERO = 22
chan_list = [11,12,22]                             # also works with tuples
dir_pin = 11
step_pin = 12
frequency = 2000.0 #hz
dc = 50.0 #duty cycle
GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(dir_pin, GPIO.HIGH)                # sets all to GPIO.LOW
p = GPIO.PWM(step_pin, frequency)
GPIO.setup(ZERO, GPIO.IN)

def torna_allo_zero():
	try:
		while GPIO.input(ZERO):
			p.start(dc)
			time.sleep(0.01)
	except KeyboardInterrupt:
		pass
	p.stop()
			torna_allo_zero()

GPIO.cleanup(chan_list)
