from time import time
import NaoApplication as NaoApplication
from threading import Thread
from PIL import Image
import os

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
                    "sound":False,
                    "photo":True,
                    "text":"",
                    "head":{"yaw":0, "pitch":0}
            }
        self.threadc = Control(self.controls)
        # Lancement du thread
        self.threadc.start()
        self.imgBuffer = open("placeholder.jpg", 'rb').read()
        #self.frames = [open('_robotDebug/'+str(f) + '.jpg', 'rb').read() for f in range(1,29)]

    def get_frame(self):
        #time.sleep(0.5)
        
        if (type(self.controls["photo"]) != type(True) and
            type(self.controls["photo"]) != type(1)):

            photo = self.controls["photo"]
            imageWidth = photo[0]
            imageHeight = photo[1]
            array = photo[6]
            image = Image.frombytes("RGB", (imageWidth, imageHeight), array)
            image.save("camImage.png", "PNG")
            
            #print(EXTENSION)
            f = open('camImage.png', 'rb')
            self.imgBuffer = f.read()
            f.close()
            self.controls["photo"] = True
        return self.imgBuffer

    def get_audio(self):
        open("_robotDebugSound/part1.wav", 'rb').read()

    def setPositionIdle(self):
        self.controls["stand"] = True
        print("je suis pret a bouger !")

    def setPositionRest(self):
        self.controls["sit"] = True
        print("je vais me reposer :)")

    def setPositionCue(self):
        self.controls["arm"] = True
        print("j attire l attention")

    def motion (self, joysticks):
        self.controls["forward"]=[joysticks['lefty'], joysticks['leftx']]      
        if joysticks['rightx'] > 20:
            self.controls["rotation"] = 1
        elif joysticks['rightx'] < -20:
            self.controls["rotation"] = -1
        else:
            self.controls["rotation"] = 0
        if (joysticks['lefty'] == 0 and
            joysticks['leftx'] == 0 and
            joysticks['rightx'] == 0):
            self.moving = True
        if (joysticks['lefty'] == 0 and
            joysticks['leftx'] == 0 and
            joysticks['rightx'] == 0 and
            self.moving):
            print("stop debbug")
            self.moving = False
            self.controls["stop"] = True
            
    def cameraMotion (self, orientation) :
        print("je veux bouger la tete")
        self.controls["head"]["yaw"]=orientation['yaw']
        self.controls["head"]["pitch"]=orientation['pitch']
        
    def playSound(self, sound):
        self.controls["sound"] = sound
        return

    def sayText(self, text):
        self.controls["text"] = text

    def __del__(self):
        pass
        #self.threadc.join()
