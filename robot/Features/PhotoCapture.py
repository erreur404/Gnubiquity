import sys
import time
import random
import math
import motion
import almath as m # python's wrapping of almath
import almath
import argparse

from naoqi import ALProxy
from NaoApplication import *
from Features import *



class PhotoCapture(Features) :

    def __init__(self):
        self.name = "PhotoCapture"

    def run(self, robotIP, feature):
        try :
            photoCaptureProxy = ALProxy("ALPhotoCapture", robotIP, 9559)

        except Exception, e:
            print "Error when creating ALPhotoCapture proxy:"
            print str(e)
            exit(1)

        try :
            

        photoCaptureProxy.setResolution(2)
        photoCaptureProxy.setPictureFormat("jpg")
        photoCaptureProxy.takePictures(3, "/home/nao/recordings/cameras/", "image")
