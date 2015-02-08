from actions.speak import Speak
from actions.move import Head
from triggers.distance import DistanceTrigger 

import RPi.GPIO as GPIO


class Salvo():
    '''
    Salvo il salutatore
    '''

    head = Head()
    speak = Speak()
    callbacks = {}
    threadList = []
    behaviour_instances = []

    def init(self):
        GPIO.setmode(GPIO.BOARD)
        self.head.init()
    def behave(self, bclass, event):
        ''' register a behaviour '''
        self.behaviour_instances.append(bclass(self))
        self.callbacks[event] = self.behaviour_instances[-1].callback


    def run():
        ''' launch threads for all the triggers: new twitter message, new distance etc
        '''
        distanceThread = DistanceTrigger(callbacks['distance'])
        threadList.append(distanceThread)

        # launch threads
        for thread in threadList:
            t.run()
        # no return from here
        while True:
            time.sleep(10)

    def stop():
        self.head.cleanup()
        for thread in threadList:
            t.stop()
            t.join()






    
