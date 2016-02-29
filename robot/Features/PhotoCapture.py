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

        resolution = 2 # 0=kQQVGA (160*120px)  1=kQVGA (320*240) 2=kVGA (640*480) 3=kVGA (1280*960)
        cameraID = 0 # 0= camera on the top 1 =  camera on the bottom
        
        try :
            pC = ALProxy("ALPhotoCapture", robotIP, 9559)
            tts = ALProxy("ALTextToSpeech", robotIP, 9559)
            vD = ALProxy("ALVideoDevice", robotIP, 9559)
            tts.setLanguage("French")
            
            
        except Exception, e:
            print "Error when creating ALPhotoCapture proxy:"
            print str(e)
            exit(1)

        try :
            #pC.setResolution(resolution)
            #pC.setPictureFormat("jpg")
            #pC.takePicture("/home/nao/recordings/cameras/", "image")

            """
            vD.subscribeCamera("Gnubiquity", 0, resolution,10,30)
            results = vD.getImageRemote("Gnubiquity")
            image = (str)(results[6])
    
            if (image==None):
                print("image data null")
            else:
                print("image prise")
            """
            
            #           tts.say("Photo", "French")

        except Exception, e:
            print "Could not take a Picture with ALPhotoCapture"
            print "Error was: ", e

        #f = open("image.bmp", "wb")
        #f.write(image)
        #f.close()

        vD.releaseImage("Gnubiquity")
        vD.unsubscribe("Gnubiquity")
        
