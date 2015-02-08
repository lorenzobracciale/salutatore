import RPi.GPIO as GPIO
import time, os

class Head():
    """
    Control the head movements
    """
    current_position = None
    GPIO_ZERO = 22 #gpio pin for zero sensor 
    GPIO_STEP = 12 #gpio pin for step
    GPIO_DIR = 11 #gpio pin direction
    dc = 50.0 #duty cycle
    def init(self):
        ''' inizialize gpio and move the head to front '''
        GPIO.setup(GPIO_ZERO, GPIO.IN)
        GPIO.setup(GPIO_STEP, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(GPIO_DIR, GPIO.OUT, initial=GPIO.LOW)
        self.goto_zero()

    def cleanup(self):
        ''' cleanup GPIO on close '''
        GPIO.cleanup(GPIO_ZERO)
        GPIO.cleanup(GPIO_STEP)
        GPIO.cleanup(GPIO_DIR)
    def rotate(self, angle, speed, direction):
        ''' look at a specifi angle '''
        pass
    def raw_rotate(self, time, speed, direction):
        pass

    def goto_zero(self):
        freq = 20000.0 #hz
        p = GPIO.PWM(self.GPIO_STEP, freq)
        while GPIO.input(self.GPIO_ZERO):
            p.start(self.dc)
            time.sleep(0.01)
        p.stop()
        self.current_position = 0.0
