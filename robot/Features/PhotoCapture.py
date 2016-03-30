# -*- coding: cp1252 -*-
# Feature : prise de photo
import sys
import time
import random
import math
import motion
import almath as m 
import almath
import argparse
import vision_definitions
from PIL import Image
from naoqi import ALProxy
from NaoApplication import *
from Features import *


class PhotoCapture(Features) :

    def __init__(self):
        self.name = "PhotoCapture"

    def run(self, robotIP, feature):

        # Creation proxy pour prendre des photos
        try :
            t0=time.time()
            vD = ALProxy("ALVideoDevice", robotIP, 9559)
            t1 = time.time()
            
        except Exception, e:
            print "Error when creating ALPhotoCapture proxy:"
            print str(e)
            exit(1)

        # Changement de resolu des photos 
        try :
            if(feature["photo"]==0):
                resolution = vision_definitions.kQQQVGA
            elif(feature["photo"]==1):
                resolution = vision_definitions.kQQVGA
            elif(feature["photo"]==2):
                resolution = vision_definitions.kQVGA
            elif(feature["photo"]==3):
                resolution = vision_definitions.kVGA
            elif(feature["photo"]==4):
                resolution = vision_definitions.k4VGA
                
            colorSpace = vision_definitions.kRGBColorSpace
            fps=30

            nameId = vD.subscribe("python_GVM", resolution , colorSpace, fps)
            print "photo"
            
            image = vD.getImageRemote(nameId)
            
            vD.unsubscribe(nameId)
            imageWidth = image[0]
            imageHeight= image[1]
            array = image[6]
            
            feature["photo"] = image
           

        except Exception, e:
            print "Could not take a Picture with ALPhotoCapture"
            print "Error was: ", e

