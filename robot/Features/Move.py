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
from Features import *
from InitRobot import *
        
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
