'''
Behaviour module for distance triggered events
'''
import time

class ProximityBehaviour():
    def __init__(self, salvo):
        self.salvo = salvo
        self.idle = True
    def callback(self, distance):
        if distance < 100:
            self.idle = False
            self.salvo.speak.say("Mi stai troppo vicino, spostati!", True)
            self.salvo.head.raw_rotate(10, 44000, 'cw')

            



    
