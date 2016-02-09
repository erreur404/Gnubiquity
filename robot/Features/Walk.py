import sys
import time
import random
import math
import motion
import almath as m # python's wrapping of almath
import almath
import argparse

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
from Robot import *
from NaoApplication import *
from Features import *
from InitRobot import *

class Walk(Features):
    'Common base class for Walk feature'  
    'The Robot whistles while walking and he avoids obstacles'
 
    def __init__(self):
        self.name = "Walk"
    
    def run(self, robotIP, command):
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
        tts.setLanguage("English")
        
        #####################
        ## Enable arms control by Walk algorithm
        #####################
        motionProxy.setWalkArmsEnabled(True, True)
        #~ motionProxy.setWalkArmsEnabled(False, False)
    
        #####################
        ## FOOT CONTACT PROTECTION
        #####################
        motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
        
        start = time.time()
       
        
        if (command =="fwd") :
             navigationProxy.moveTo(0.5, 0.0, 0.0)
             motionProxy.waitUntilMoveIsFinished()
        elif (command =="bwd"):
             navigationProxy.moveTo(-0.5, 0.0, 0.0)
             motionProxy.waitUntilMoveIsFinished()
        elif (command =="rgt") :
             navigationProxy.moveTo(0.0, 0.0, -1.0)
             motionProxy.waitUntilMoveIsFinished()
        elif (command =="lft") :
             navigationProxy.moveTo(0.0, 0.0, 1.0)
             motionProxy.waitUntilMoveIsFinished()
                
          #postureProxy.goToPosture("StandInit", 0.5)       
        
    
        'Small message of end'
        # tts.say("WAALK FINISHED") 
        print("Walk is over!")
        
        # Send NAO to Pose Init
