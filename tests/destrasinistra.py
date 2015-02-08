#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

chan_list = [11,12]                             # also works with tuples
dir_pin = 11
step_pin = 12
frequency = 1000.0 #hz
dc = 30.0 #duty cycle
dc2 = 50.0
GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.LOW)

try:
	p = GPIO.PWM(step_pin, frequency)
	for i in range(4):
		GPIO.output(dir_pin, GPIO.LOW)                # sets all to GPIO.LOW
		p.start(dc)
		time.sleep(0.1)
		p.stop()
		GPIO.output(dir_pin, GPIO.HIGH)                # sets all to GPIO.LOW
		p.start(dc)
		time.sleep(1)
		p.stop()
		GPIO.output(dir_pin, GPIO.LOW)                # sets all to GPIO.LOW
		p.start(dc)
		time.sleep(0.01)
		p.stop()
		GPIO.output(dir_pin, GPIO.HIGH)                # sets all to GPIO.LOW
		p.start(dc)
		time.sleep(1)
		p.stop()
except KeyboardInterrupt:
	pass
p.stop()

GPIO.cleanup(chan_list)

