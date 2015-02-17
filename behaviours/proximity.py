'''
Behaviour module for distance triggered events
'''
import time

class ProximityBehaviour():
    def __init__(self, salvo):
        self.salvo = salvo
    def callback(self, data):
        if data['distance'] < 100 and not self.salvo.is_busy():
            self.salvo.busy(True)
            self.salvo.speak.say("Mi stai troppo vicino, spostati!", True)
            self.salvo.head.wake()
            self.salvo.head.raw_rotate(10, 44000, 'cw')
            self.salvo.head.goto_zero()
            self.salvo.head.sleep()
            self.salvo.busy(False)


            



    
