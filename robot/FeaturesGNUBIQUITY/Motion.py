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

class stopRobot(Features):
    'Common base class for stopRobot feature'
    'The goal of this feature is to set a posture for the robot'
    'The posture chosen is LyingBack'
    
    def __init__(self):
        self.name = "Stop"
       
    def run(self, robotIP):
        try:
            postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
        except Exception, e:
            print "Could not create proxy to ALRobotPosture"
            print "Error was: ", e
               
        postureProxy.goToPosture("LyingBack", 0.7)
        
class Walk(Features):
    'Common base class for Walk feature'  
    'The Robot whistles while walking and he avoids obstacles'
 
    def __init__(self):
        self.name = "Walk"
    
    def run(self, robotIP, forward, backward, right, left):
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
       
        
        if forward :
             navigationProxy.moveTo(1.0, 0.0, 0.0)
             motionProxy.waitUntilMoveIsFinished()
        elif backward :
             navigationProxy.moveTo(-1.0, 0.0, 0.0)
             motionProxy.waitUntilMoveIsFinished()
        elif right :
             navigationProxy.moveTo(0.0, 0.0, -1.0)
             motionProxy.waitUntilMoveIsFinished()
        elif left :
             navigationProxy.moveTo(0.0, 0.0, 1.0)
             motionProxy.waitUntilMoveIsFinished()
                
                
        
    
        'Small message of end'
        # tts.say("WAALK FINISHED") 
        print("Walk is over!")
        
        # Send NAO to Pose Init
      
               
class Move(Features):
    'Common base class for Move feature'  
    'The Robot moves in accordance by the parameters given'
    'the parameters are: x,y and theta'
    
    def __init__(self, x, y, theta):
        self.name = "Move"
        self.x = x
        self.y = y
        self.theta = theta  
    
    def run(self, robotIP):
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
        
        # Send NAO to Pose Init
        postureProxy.goToPosture("StandInit", 0.6)
    
        navigationProxy.setSecurityDistance(0.5)
        
        X = self.x
        Y = self.y
        Theta = self.theta

        navigationProxy.moveTo(X, Y, Theta)
