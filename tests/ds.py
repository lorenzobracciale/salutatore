#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

chan_list = [11,12]                             # also works with tuples
dir_pin = 11
step_pin = 12
frequency = 1000.0 #hz
dc = 30.0 #duty cycle
GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.LOW)

try:
	p = GPIO.PWM(step_pin, frequency)
	for i in range(4):
		GPIO.output(dir_pin, GPIO.LOW)                # sets all to GPIO.LOW
		p.start(dc)
		time.sleep(0.3)
		p.stop()
		time.sleep(0.1)
		GPIO.output(dir_pin, GPIO.HIGH)                # sets all to GPIO.LOW
		p.start(dc)
		time.sleep(0.3)
		p.stop()
		time.sleep(0.1)
except KeyboardInterrupt:
	pass
p.stop()

GPIO.cleanup(chan_list)

