import threading
import RPi.GPIO as GPIO
import time

class DistanceTrigger(threading.Thread):
    GPIO_TRIG = 24
    GPIO_ECHO = 23
    shutdown = False
    def __init__(self, callback):
        threading.Thread.__init__(self)
        self.callback = callback

    def init_sensor(self):
        GPIO.setup(self.GPIO_TRIG, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
        GPIO.output(self.GPIO_TRIG, False)
        time.sleep(2)

    def cleanup(self):
        GPIO.cleanup(self.GPIO_TRIG)
        GPIO.cleanup(self.GPIO_ECHO)

    def distance(self):
        GPIO.output(self.GPIO_TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIG, False)

        while GPIO.input(self.GPIO_ECHO) == 0:
            pulse_start = time.time()


        while GPIO.input(self.GPIO_ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        print "Distanza: ", distance, "cm"
        return distance

    def stop(self):
        self.shutdown = True
        print "Stopping distance polling thread"

    def run(self):
        print "Start distance polling thread"
        self.init_sensor()
        while not self.shutdown:
            self.callback(self.distance())
            time.sleep(2)



