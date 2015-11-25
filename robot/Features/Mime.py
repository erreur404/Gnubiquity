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

class Mime(Features):
    
    '''
    def __init__(self, LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll):
      self.name = "Mime"
        self.LShoulderPitch = LShoulderPitch
        self.LShoulderRoll = LShoulderRoll
        self.LElbowYaw = LElbowYaw
        self.LElbowRoll = LElbowRoll
        self.RShoulderPitch = RShoulderPitch
        self.RShoulderRoll = RShoulderRoll
        self.RElbowYaw = RElbowYaw
        self.RElbowRoll = RElbowRoll
    '''
    
    def __init__(self, LShoulderPitch, LShoulderRoll):
        self.name = "Mime"
        self.LShoulderPitch = LShoulderPitch
        self.LShoulderRoll = LShoulderRoll
        
    def run(self, robotIP):
        # Init proxies
        try:
            motionProxy = ALProxy("ALMotion", robotIP, 9559)
        except Exception, e:
            print "Could not create proxy to ALMotion"
            print "Error was: ", e
            sys.exit(1)
        try:
            postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
        except Exception, e:
            print "Could not create proxy to ALRobotPosture"
            print "Error was: ", e
    
        # Send NAO to Pose Init
        postureProxy.goToPosture("StandInit", 1.0)
        
        #Test example with two joints
        #names = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll"]
        #angleLists = [self.LShoulderPitch, self.LShoulderRoll, self.LElbowYaw, self.LElbowRoll, self.RShoulderPitch, self.RShoulderRoll, self.RElbowYaw, self.RElbowRoll]
        
        names = ["LShoulderPitch", "LShoulderRoll"]
        angleLists = [self.LShoulderPitch, self.LShoulderRoll]
        fractionMaxSpeed = 0.3
        
        motionProxy.setAngles(names, angleLists, fractionMaxSpeed)
        
        time.sleep(5.0)
