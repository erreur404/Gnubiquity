from time import time
#import NaoApplication as NaoApplication
import NaoApplicationEmulation as NaoApplication
from threading import Thread

class Control(Thread):

    """Thread charge simplement d'afficher une lettre dans la console."""

    def __init__(self, command):
        Thread.__init__(self)
        self.command = command

    def run(self):
        """Code a executer pendant l'execution du thread."""
        NaoApplication.main(self.command)



class Robot(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
        self.moving = True
        # Creation du thread
        self.controls = {
                    "forward":[0, 0],
                    "rotation":0,
                    "stop":False,
                    "arm":False,
                    "sit":False,
                    "stand":False,
                    "head":{"roll":0, "pitch":0}
            }
        self.threadc = Control(self.controls)
        # Lancement du thread
        self.threadc.start()
        self.frames = [open('_robotDebug/'+str(f) + '.jpg', 'rb').read() for f in range(1,29)]

    def get_frame(self):
        #time.sleep(0.5)
        return self.frames[int(time()) % len(self.frames)]

    def setPositionIdle(self):
        self.controls["stand"] = True
        print("je suis pret a bouger !")

    def setPositionRest(self):
        self.controls["sit"] = True
        print("je vais me reposer :)")

    def setPositionCue(self):
        self.controls["arm"] = True
        print("j attire l attention")

    def moveForward(self, joystick):
        self.controls["forward"]=[joystick[1], joystick[0]]

    def turn(self, joystick):
        if joystick[0] > 20:
            self.controls["rotation"] = 1
        elif joystick[0] < 20:
            self.controls["rotation"] = -1
        else:
            self.controls["rotation"] = 0

    def playSound(sound):
        return

    def __del__(self):
        pass
        #self.threadc.join()
