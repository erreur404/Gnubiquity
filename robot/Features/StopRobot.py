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
