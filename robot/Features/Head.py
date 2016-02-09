# -*- coding: utf-8 -*-
import sys
import time
import random
import math
import motion
import almath as m # python's wrapping of almath
import almath
import argparse
import time
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
from NaoApplication import *
from Features import *


class Head(Features):
    def __init__(self):
        self.name = "Head"
          
    def run(self, robotIP, feature):       
        try:
            motionProxy = ALProxy("ALMotion", robotIP, 9559)
        except Exception, e:
            print "Could not create proxy to ALMotion"
            print "Error was: ", e   
        try:
            postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
        except Exception, e:
            print "Could not create proxy to ALRobotPosture"
            print "Error was: ", e
        try:
            navigationProxy = ALProxy("ALNavigation", robotIP, 9559)
        except Exception, e:
            print "Could not create proxy to ALRobotNavigation"
            print "Error was: ", e
        try:
            memoryProxy = ALProxy("ALMemory", robotIP, 9559)
        except Exception, e:
            print "Could not create proxy to ALMemory"
            print "Error was: ", e
        try:
            tts = ALProxy("ALTextToSpeech", robotIP, 9559)
        except Exception, e:
            print "Could not create proxy to ALTextToSpeech"
            print "Error was: ", e    
        # Send NAO to Pose Init
        postureProxy.goToPosture("StandInit", 0.5)
        # setting the language for Nao
        tts.setLanguage("French")        
        start = time.time()
        







        if feature["head"] :
            try:
                proxy = ALProxy("ALMotion", robotIP, 9559)
            except Exception, e:
                print "Could not create proxy to ALMotion"
                print "Error was: ", e

           
            
            degreHori = (feature["head"][0])/90.0 
            degreVerti =(feature["head"][1])/45.0
           
            #  motionProxy.setAngles("HeadYaw", random.uniform(-1.0, 1.0), 0.6)
            #  motionProxy.setAngles("HeadPitch", random.uniform(-0.5, 0.5), 0.6)
            #
            proxy.setStiffnesses("Head", 1.0)
            names = "HeadYaw"
            angles = degreHori
            print angles,"\a"
            times = 1.5
            isAbsolute = True
            proxy.post.angleInterpolation(names, angles, times, isAbsolute)

           
            names = "HeadPitch"
            angles = degreVerti
            
            print angles,"\a"
            times = 1.5
            isAbsolute = True
            proxy.post.angleInterpolation(names, angles, times, isAbsolute)
            
##       
##
##            # Active Head tracking
##            effectorName = "Head"
##            isEnabled    = True
##            motionProxy.wbEnableEffectorControl(effectorName, isEnabled)
##
##            # Example showing how to set orientation target for Head tracking
##            # The 3 coordinates are absolute head orientation in NAO_SPACE
##            # Rotation in RAD in x, y and z axis
##
##            # X Axis Head Orientation feasible movement = [-20.0, +20.0] degree
##            # Y Axis Head Orientation feasible movement = [-75.0, +70.0] degree
##            # Z Axis Head Orientation feasible movement = [-30.0, +30.0] degree
##
##            targetCoordinateList = [
##            [+20.0,  00.0,  00.0], # target 0
##            [-20.0,  00.0,  00.0], # target 1
##            [ 00.0, +70.0,  00.0], # target 2
##            [ 00.0, +70.0, +30.0], # target 3
##            [ 00.0, +70.0, -30.0], # target 4
##            [ 00.0, -75.0,  00.0], # target 5
##            [ 00.0, -75.0, +30.0], # target 6
##            [ 00.0, -75.0, -30.0], # target 7
##            [ 00.0,  00.0,  00.0], # target 8
##            ]
##
##            # wbSetEffectorControl is a non blocking function
##            # time.sleep allow head go to his target
##            # The recommended minimum period between two successives set commands is
##            # 0.2 s.
##            for targetCoordinate in targetCoordinateList:
##                targetCoordinate = [target*math.pi/180.0 for target in targetCoordinate]
##                motionProxy.wbSetEffectorControl(effectorName, targetCoordinate)
##                time.sleep(3.0)
##
##            # Deactivate Head tracking
##            isEnabled = False
##            motionProxy.wbEnableEffectorControl(effectorName, isEnabled)
##
##            # Go to rest position
##            motionProxy.rest()

##if __name__ == "__main__":
##    parser = argparse.ArgumentParser()
##    parser.add_argument("--ip", type=str, default="127.0.0.1",
##                        help="Robot ip address")
##    parser.add_argument("--port", type=int, default=9559,
##                        help="Robot port number")
##
##    args = parser.parse_args()
##    main(args.ip, args.port)
##        print("Head is stand up")
##
##        



 




