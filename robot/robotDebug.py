from time import time
import NaoApplication
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
                    "forward":False,
                    "backward":False,
                    "right":False,
                    "left":False,
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

    def moveForward(self, speed):
        if (speed > 0):
            self.controls["forward"] = True
            self.controls["backward"] = False
        elif (speed < 0):
            self.controls["backward"] = True
            self.controls["forward"] = False
        else:
            self.controls["forward"] = False
            self.controls["backward"] = False
        print("j'avance a "+str(speed)+" de ma vitesse !")

    def turn(self, speed):
        if (speed > 0):
            self.controls["right"] = True
            self.controls["left"] = False
        elif (speed < 0):
            self.controls["left"] = True
            self.controls["right"] = False
        else:
            self.controls["right"] = False
            self.controls["left"] = False
        print("je tourne a "+str(speed)+" de ma vitesse !")

    def playSound(sound):
        return

    def __del__(self):
        thread_1.join()
