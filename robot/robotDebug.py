from time import time


class Robot(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
        self.frames = [open('_robotDebug/'+str(f) + '.jpg', 'rb').read() for f in range(1,10)]

    def get_frame(self):
        #time.sleep(0.5)
        return self.frames[int(time()) % len(self.frames)]

    def setPositionIdle(self):
        print("je suis pret a bouger !")

    def setPositionRest(self):
        print("je vais me reposer :)")

    def setPositionCue(self):
        print("j attire l attention")

    def moveForward(self, speed):
        print("j'avance a "+str(speed)+" de ma vitesse !")

    def turn(self, speed):
        print("je tourne a "+str(speed)+" de ma vitesse !")
