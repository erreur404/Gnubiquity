# -*- coding: cp1252 -*-
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

<<<<<<< HEAD
        # 0=kQQVGA (160*120px)  1=kQVGA (320*240) 2=kVGA (640*480) 3=k4VGA (1280*960)
        # 0= camera on the top 1 =  camera on the bottom
=======
        resolution = 2 # 0=kQQVGA (160*120px)  1=kQVGA (320*240) 2=kVGA (640*480) 3=kVGA (1280*960)
        cameraID = 0 # 0= camera on the top 1 =  camera on the bottom
>>>>>>> da4c21945f4f3bf1f2030aad45bde29c37987706
        
        try :
            pC = ALProxy("ALPhotoCapture", robotIP, 9559)
            tts = ALProxy("ALTextToSpeech", robotIP, 9559)
            vD = ALProxy("ALVideoDevice", robotIP, 9559)
<<<<<<< HEAD
            t1 = time.time()

##            print "delay creation proxy", t1-t0
=======
            tts.setLanguage("French")
            
>>>>>>> da4c21945f4f3bf1f2030aad45bde29c37987706
            
        except Exception, e:
            print "Error when creating ALPhotoCapture proxy:"
            print str(e)
            exit(1)

        try :
<<<<<<< HEAD
            #print feature["photo"]
            resolution = vision_definitions.kQVGA
            colorSpace = vision_definitions.kRGBColorSpace
            fps=30

            nameId = vD.subscribe("python_GVM", resolution , colorSpace, fps)
            print nameId
            t0= time.time()
            image = vD.getImageRemote(nameId)
            t1 = time.time()
            
            print "temps de getImageRemote", t1-t0
            vD.unsubscribe(nameId)
            imageWidth = image[0]
            imageHeight= image[1]
            array = image[6]
            
            t2 = time.time()
            feature["photo"] = image
            t3 = time.time()
            print "delai de transmission de l'image", t3-t2

            
            
            im = Image.fromstring("RGB", (imageWidth, imageHeight), array)
            feature["photo"] = im
            t5 = time.time()
            print "temps de création de l'image RGB : ",t5-t3
            im.save("camImage.png", "PNG")
            t4 = time.time()
            print "temps de sauvegarde de l'image", t4-t5
            im.show()
            t6 = time.time()
            print "temps d'affichage de l'image", t6-t4
            print "temps total de prise et affichage d'une photo", t6-t0

        except Exception, e:
            print "Could not take a Picture with ALPhotoCapture"
            print "Error was: ", e

