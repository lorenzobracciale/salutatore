#!/usr/bin/env python
"""
Salvo il Salutatore
Main main program
"""
from salvo import Salvo
from behaviours.proximity import ProximityBehaviour
from behaviours.carnival import CarnivalBehaviour




def main():
    salvo = Salvo()
    try:
        # init salvo
        salvo.init()
        # init behaviours
        salvo.behave(ProximityBehaviour, 'distance')
        salvo.behave(CarnivalBehaviour, 'distance')

        # start
        salvo.run()

    except KeyboardInterrupt:
        salvo.stop()




if __name__ == "__main__":
    main()
