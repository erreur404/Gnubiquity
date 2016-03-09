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

        # 0=kQQVGA (160*120px)  1=kQVGA (320*240) 2=kVGA (640*480) 3=k4VGA (1280*960)
        # 0= camera on the top 1 =  camera on the bottom
        
        try :
            t0=time.time()
            vD = ALProxy("ALVideoDevice", robotIP, 9559)
            t1 = time.time()

##            print "delay creation proxy", t1-t0
            
        except Exception, e:
            print "Error when creating ALPhotoCapture proxy:"
            print str(e)
            exit(1)

        try :
            #print feature["photo"]
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
            t3 = time.time()
            print "delai de transmission de l'image", t3-t2

            
            
            #im = Image.frombytes("RGB", (imageWidth, imageHeight), array)
            feature["photo"] = image
            t5 = time.time()
            print "temps de creation de l'image RGB : ",t5-t3
            #im.save("camImage.png", "PNG")
            t4 = time.time()
            print "temps de sauvegarde de l'image", t4-t5
            #im.show()
            t6 = time.time()
            print "temps d'affichage de l'image", t6-t4
            print "temps total de prise et affichage d'une photo", t6-t0

        except Exception, e:
            print "Could not take a Picture with ALPhotoCapture"
            print "Error was: ", e

