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

    def run(self, robotIP, command):
        print("I am on the Mime class Run")

        if(command == null):
            print("An Error has occured, your command is null")
        elif(command=="RArmUp"):
            print("You're running the RArmUP command")
             # Init proxies.
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

            # Set NAO in Stiffness On
            StiffnessOn(motionProxy)

            # Send NAO to Pose Init
            postureProxy.goToPosture("StandInit", 0.5)

            effector   = "RArm"
            space      = motion.FRAME_ROBOT
            """
            axisMask   = almath.AXIS_MASK_VEL    # just control position
            isAbsolute = False

            # Since we are in relative, the current position is zero
            currentPos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            # Define the changes relative to the current position
            dx         =  0.03      # translation axis X (meters)
            dy         =  0.03      # translation axis Y (meters)
            dz         =  0.00      # translation axis Z (meters)
            dwx        =  0.00      # rotation axis X (radians)
            dwy        =  0.00      # rotation axis Y (radians)
            dwz        =  0.00      # rotation axis Z (radians)
            targetPos  = [dx, dy, dz, dwx, dwy, dwz]

            # Go to the target and back again
            path       = [targetPos, currentPos]
            times      = [2.0, 4.0] # seconds
"""
            isAbsolute = False

                        
            # Motion of Arms with block process
            axisMask   = almath.AXIS_MASK_VEL  # control just the position
            times      = [0.5, 1.0,2.5]  # seconds

            dy         = +0.06                 # translation axis Y (meters)
            # Motion of Right Arm during the first half of the Torso motion
            effector   = "RArm"
            path       = [
              [0.05, 00.0, 0.15, 0.0, 0.0, 0.0],  # point 1
              [0.10, 0.0, 0.28, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.40, 0.0, 0.0, 0.0]]  # point 2
            
            motionProxy.positionInterpolation(effector, space, path, axisMask, times, isAbsolute)
        else:
            print("an unexpected error has occured")
            
        
