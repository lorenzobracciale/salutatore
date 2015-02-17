import time

class NfcTrigger(threading.Thread):
    """
    Trigger an event when 
    """
    def __init__(self.callback)
        threading.Thread.__init__(self)
        self.callback = callback
    def stop(self):
        self.shutdown = True
        print "Stopping nfc polling thread"
    def run(self):
        print "Start nfc polling thread"
        while not self.shutdown:
            pass
            #https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi?view=all
            # http://nfcpy.readthedocs.org/en/latest/topics/get-started.html#read-write-tags
            #http://www.raspberrypi.org/forums/viewtopic.php?t=42948&p=344523
            data = {}
            self.callback(data)
            time.sleep(2)


