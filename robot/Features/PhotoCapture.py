# -*- coding: cp1252 -*-
import sys
import time
import random
import math
import motion
import almath as m # python's wrapping of almath
import almath
import argparse
import vision_definitions
import Image

from naoqi import ALProxy
from NaoApplication import *
from Features import *




class PhotoCapture(Features) :

    def __init__(self):
        self.name = "PhotoCapture"

    def run(self, robotIP, feature):

        # 0=kQQVGA (160*120px)  1=kQVGA (320*240) 2=kVGA (640*480) 3=kVGA (1280*960)
        # 0= camera on the top 1 =  camera on the bottom
        
        try :
            t0=time.time()
            vD = ALProxy("ALVideoDevice", robotIP, 9559)
            t1 = time.time()

            print "delay creation proxy", t1-t0
            
        except Exception, e:
            print "Error when creating ALPhotoCapture proxy:"
            print str(e)
            exit(1)

        try :
            resolution = vision_definitions.kVGA
            colorSpace = vision_definitions.kRGBColorSpace
            fps=30

            nameId = vD.subscribe("python_GVM", resolution , colorSpace, fps)
            print nameId
            t0= time.time()
            image = vD.getImageRemote(nameId)
            t1 = time.time()
            print "temps de getImageRemote", t1-t0
            vD.unsubscribe(nameId)

            t2 = time.time()
            
            imageWidth = image[0]
            imageHeight= image[1]
            array = image[6]
            t3 = time.time()
            print "delai de transmission de l'image", t4-t2
            feature["photo"] = image
            
            
            im = Image.fromstring("RGB", (imageWidth, imageHeight), array)
            t5 = time.time()
            print "temps de fromstring : ",t5-t4
            #im.save("camImage.png", "PNG")
            #im.show()
            t6 = time.time()
            print "temps total de prise d'une photo", t6-t0

        except Exception, e:
            print "Could not take a Picture with ALPhotoCapture"
            print "Error was: ", e

