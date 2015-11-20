import sys
import time
import random
import math
import motion
import almath as m # python's wrapping of almath
import almath
import argparse
import Image

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
from Robot import *
from NaoApplication import *

class TakePicture(Features): #We should work on this class to create another one with the video
    
    def __init__(self):
        self.name = "TakePicture"
    
    def run(self, robotIP):
        try:
            camProxy = ALProxy("ALVideoDevice", robotIP, 9559)
        except Exception, e:
            print "Could not create proxy to ALVideoDevice"
            print "Error was: ", e
            
        resolution = 2  #VGA
        colorSpace = 11 #RGB
        
        videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)
        
        t0 = time.time()
            
        # Get a camera image.
        # image[6] contains the image data passed as an array of ASCII chars.
        naoImage = camProxy.getImageRemote(videoClient)
        
        t1 = time.time()
        
        # Time the image transfer.
        print "acquisition delay ", t1 - t0
        
        camProxy.unsubscribe(videoClient)
        
        
        # Now we work with the image returned and save it as a PNG  using ImageDraw package.
        
        # Get the image size and pixel array.
        imageWidth = naoImage[0]
        imageHeight = naoImage[1]
        array = naoImage[6]
        
        # Create a PIL Image from our pixel array.
        im = Image.fromstring("RGB", (imageWidth, imageHeight), array)
        
        # Save the image.
        im.save("camImage.png", "PNG")
        
        im.show()
