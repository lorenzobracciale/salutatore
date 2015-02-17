#!/usr/bin/env python
import RPi.GPIO as GPIO
import time, os

GPIO.setmode(GPIO.BOARD)

chan_list = [11,12]                             # also works with tuples
dir_pin = 11
step_pin = 12
TRIG = 24
ECHO = 23
ZERO = 22
frequency = 20000.0 #hz
dc = 50.0 #duty cycle


GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)
time.sleep(2)

GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(dir_pin, GPIO.HIGH)                # sets all to GPIO.LOW

GPIO.setup(ZERO, GPIO.IN)

def torna_allo_zero():
	try:
		while GPIO.input(ZERO):
			p.start(dc)
			time.sleep(0.001)
	except KeyboardInterrupt:
		pass
	p.stop()
	print "zero"


def distance():
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO) == 0:
	    pulse_start = time.time()


	while GPIO.input(ECHO) == 1:
	    pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)

	print "Distanza: ", distance, "cm"
	return distance

def say(text):
    os.system("espeak -v it ' " + text + " ' & ")

p = GPIO.PWM(step_pin, frequency)



try:
	while True:
		if distance() < 100.0:
			say("Tu mi fai giraarr tu mi fai giraarr come fossi una bambooola")
			p.start(dc)
			time.sleep(6)
			torna_allo_zero()
			break
		time.sleep(0.5)
except KeyboardInterrupt:
	pass
p.stop()

GPIO.cleanup(chan_list)

