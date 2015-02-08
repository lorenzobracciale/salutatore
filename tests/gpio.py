#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

chan_list = [11,12]                             # also works with tuples
dir_pin = 11
step_pin = 12
frequency = 20000.0 #hz
dc = 50.0 #duty cycle
GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(dir_pin, GPIO.HIGH)                # sets all to GPIO.LOW
p = GPIO.PWM(step_pin, frequency)

try:
	p.start(dc)
	time.sleep(1)
except KeyboardInterrupt:
	pass
p.stop()

GPIO.cleanup(chan_list)

