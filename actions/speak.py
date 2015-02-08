"""
Speak module
"""
import os

class Speak():
    def say(self, text):
        ''' say a sentence '''
        os.system("espeak -v it ' " + text + " ' & ")
