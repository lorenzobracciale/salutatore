"""
Speak module
"""
import os

class Speak():
    amplitude = 200 #volume

    def say(self, text, sync=False):
        ''' say a sentence '''
        # patch for espeak bug
        # http://www.raspberrypi.org/forums/viewtopic.php?f=38&t=98201
        text = 'hh ' + text

        if sync:
            # blocking call, wait for finish
            os.system("espeak -v it -a %d '%s' 2>/dev/null" % (self.amplitude, text) )
        else:
            # put it in background
            os.system("espeak -v it ' " + text + " ' 2>/dev/null & ")
