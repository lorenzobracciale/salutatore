'''
Behaviour module for distance triggered events
'''
import time

class ProximityBehaviour():
    def __init__(self, salvo):
        self.salvo = salvo
    def callback(self, data):
        if data['distance'] < 100 and not salvo.is_busy():
            salvo.busy(True)
            self.salvo.speak.say("Mi stai troppo vicino, spostati!", True)
            self.salvo.head.raw_rotate(10, 44000, 'cw')
            salvo.busy(False)


            



    
