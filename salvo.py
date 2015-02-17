from actions.speak import Speak
from actions.move import Head
from triggers.distance import DistanceTrigger 
from triggers.nfc import NfcTrigger 
import sys

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
    __is_busy = False

    def init(self):
        print "init init"
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.head.init()
        print "end init"

    def behave(self, bclass, event):
        ''' register a behaviour '''
        self.behaviour_instances.append(bclass(self))
        self.callbacks[event] = self.behaviour_instances[-1].callback


    def run(self):
        ''' launch threads for all the triggers: new twitter message, new distance etc
        '''
        print "Salvo is alive!"
        print "press q + ENTER to quit"
        if 'distance' in self.callbacks:
            distanceThread = DistanceTrigger(self.callbacks['distance'])
            self.threadList.append(distanceThread)
        if 'nfc' in self.callbacks:
            nfcThread = NfcTrigger(self.callbacks['nfc'])
            self.threadList.append(nfcThread)

        # launch threads
        for t in self.threadList:
            t.start()
        # no return from here
        c = sys.stdin.read(1)
        if c == 'q':
            print "you say quit, I quit"
            self.stop()


    def stop(self):
        print "Salvo is going to sleep..."
        self.head.cleanup()
        for t in self.threadList:
            if t.isAlive():
                t.stop()
                t.join()

    def is_busy(self):
        return self.__is_busy

    def busy(self, status):
        # todo put a mutex
        self.__is_busy = status


