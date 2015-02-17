import RPi.GPIO as GPIO
import time, os

class Head():
    """
    Control the head movements
    """
    position = None
    GPIO_ZERO = 22 #gpio pin for zero sensor 
    GPIO_STEP = 12 #gpio pin for step
    GPIO_DIR = 11 #gpio pin direction
    GPIO_SLEEP = 10 #gpio pin motor driver sleep. LOW sleep, HIGH wake
    dc = 50.0 #duty cycle
    degree_per_pulse = 1.6
    def init(self):
        ''' inizialize gpio and move the head to front '''
        GPIO.setup(self.GPIO_ZERO, GPIO.IN)
        GPIO.setup(self.GPIO_STEP, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.GPIO_DIR, GPIO.OUT, initial=GPIO.LOW) #ccw
        GPIO.setup(self.GPIO_SLEEP, GPIO.OUT, initial=GPIO.HIGH)
        print "head init, now go to zero..."
        #self.goto_zero()

    def cleanup(self):
        ''' cleanup GPIO on close '''
        GPIO.cleanup(self.GPIO_ZERO)
        GPIO.cleanup(self.GPIO_STEP)
        GPIO.cleanup(self.GPIO_DIR)

    def wake(self):
        GPIO.output(self.GPIO_SLEEP, GPIO.HIGH)
        time.sleep(1)

    def sleep(self):
        GPIO.output(self.GPIO_SLEEP, GPIO.LOW)

    def rotate(self, angle, speed, direction):
        ''' look at a specifi angle '''
        pass

    def raw_rotate(self, duration, speed, direction):
        #self.wake()
        if direction == 'cw':
            GPIO.output(self.GPIO_DIR, GPIO.HIGH)
        elif direction == 'ccw':
            GPIO.output(self.GPIO_DIR, GPIO.LOW)
        else:
            print "Direction not valid. Either choose cw or ccw"
            return
        p = GPIO.PWM(self.GPIO_STEP, speed)
        p.start(self.dc)
        time.sleep(duration)
        p.stop()
        #self.position +=  duration * speed * self.degree_per_pulse % 360
        #self.sleep()
        

    def goto_zero(self):
        #self.wake()
        freq = 20000.0 #hz
        p = GPIO.PWM(self.GPIO_STEP, freq)
        
        while GPIO.input(self.GPIO_ZERO):
            print "a"
            p.start(self.dc)
            time.sleep(0.001)
        p.stop()
        self.position = 0.0
        #self.sleep()
