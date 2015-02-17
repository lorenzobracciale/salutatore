'''
Behaviour module for distance triggered events
'''
import time, random

class CarnivalBehaviour():
    frasi_simpatiche = [
        "Ma tu, da che ti sei vestito? io da manichino a a a a aaaaa aaaa ",
        "Ma E il naso tuo o te stai a magnaa una frappa? looool      aa aa aa aa"
        "Ma c e un cesso oltre te in questo locale? ahahahah",
        "Un tizio entra in un caffe, splasc ahahahaha",
        "Tu mi fai girar, tu mi fai girar come fossi una bambola",
        "Ma sei proprio cosi o ti sei mascherato? ahahah"
    ]
    def __init__(self, salvo):
        self.salvo = salvo
        self.idle = True
    def callback(self, distance):
        if distance < 75 and self.idle:
            self.idle = False

            self.salvo.speak.say(self.frasi_simpatiche[random.randint(0, len(self.frasi_simpatiche) - 1)], True)
            #self.salvo.head.wake()
            self.salvo.head.raw_rotate(1, 44000, 'cw')
            self.salvo.head.raw_rotate(1, 44000, 'ccw')
            self.salvo.head.raw_rotate(5, 44000, 'cw')
            #self.salvo.head.goto_zero()
            #self.salvo.head.sleep()
            self.idle = True

            



    
