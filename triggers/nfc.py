import time
import subprocess
import threading

class NfcTrigger(threading.Thread):
    """
    Trigger an event when NFC card is near the heart
    """
    shutdown = False
    def __init__(self, callback):
        threading.Thread.__init__(self)
        self.callback = callback
    def stop(self):
        self.shutdown = True
        print "Stopping nfc polling thread"
    def run(self):
        print "Start nfc polling thread"
        while not self.shutdown:
            #https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi?view=all
            # http://nfcpy.readthedocs.org/en/latest/topics/get-started.html#read-write-tags
            #http://www.raspberrypi.org/forums/viewtopic.php?t=42948&p=344523
            output = subprocess.check_output("nfc-list", shell=True)
            uindex = output.find("UID")
            if uindex >= 0:
                uid = output[uindex:].split('\n')[0][14:-2].replace(" ", "") #goofy but it works!
                data = {'uid': uid}
                self.callback(data)
            time.sleep(2)


