'''
Behaviour module for recognizing an NFC card
'''
import time
import urllib2
import json

class LongTimeBehaviour():
    def __init__(self, salvo):
        self.salvo = salvo
        self.url = 'http://soci.fusolab.net/salutatore/%s/'
    def callback(self, data):
        if not self.salvo.is_busy():
            self.salvo.busy(True)
            try:
                response = urllib2.urlopen(self.url % data['uid'], timeout = 4)
                data = json.load(response) 
                print "presi dati di", data
                if data['personal']:
                    self.salvo.speak.say(data['personal'])
                else:
                    name = data['name'] if data['name'] else 'Signor nessuno'
                    if data['last_time']:
                        self.salvo.speak.say("Ciao %s, sono %d secondi che non ci vediamo, mi sei mancato tanto" % (name, data['last_time']))
                    else:
                        self.salvo.speak.say("Ciao %s benvenuto al fusolab. Oggi ci siamo conosciuti, me lo ricordero' per sempre" % (name))
            except:
                pass 
            self.salvo.busy(False)
    
