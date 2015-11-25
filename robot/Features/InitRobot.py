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
from Features import *
from NaoApplication import *

class initRobot(Features):
    'Common base class for initRobot feature'
    'The goal of this feature is to set a posture for the robot'
    'The posture chosen is Stand'
    
    def __init__(self):
        self.name = "Init"
       
    def run(self, robotIP):
        try:
            postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
        except Exception, e:
            print "Could not create proxy to ALRobotPosture"
            print "Error was: ", e
               
        postureProxy.goToPosture("Stand", 0.8)
