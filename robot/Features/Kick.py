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

class Kick(Features):
     
    def __init__(self):
        self.name = "Kick"
    
    def computePath(self, proxy, effector, frame):
        dx      = 0.05                 # translation axis X (meters)
        dz      = 0.05                 # translation axis Z (meters)
        dwy     = 5.0*almath.TO_RAD    # rotation axis Y (radian)
    
        useSensorValues = False
    
        path = []
        currentTf = []
        try:
            currentTf = proxy.getTransform(effector, frame, useSensorValues)
        except Exception, errorMsg:
            print str(errorMsg)
            print "This example is not allowed on this robot."
            exit()
    
        # 1
        targetTf  = almath.Transform(currentTf)
        targetTf *= almath.Transform(-dx, 0.0, dz)
        targetTf *= almath.Transform().fromRotY(dwy)
        path.append(list(targetTf.toVector()))
    
        # 2
        targetTf  = almath.Transform(currentTf)
        targetTf *= almath.Transform(dx, 0.0, dz)
        path.append(list(targetTf.toVector()))
    
        # 3
        path.append(currentTf)
    
        return path
        
    def run(self, robotIP):
        ''' Example of a whole body kick
         Warning: Needs a PoseInit before executing
                 Whole body balancer must be inactivated at the end of the script
        '''
    
        motionProxy  = ALProxy("ALMotion", robotIP, 9559)
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    
        # Wake up robot
        motionProxy.wakeUp()
    
        # Send robot to Stand Init
        postureProxy.goToPosture("StandInit", 0.5)
    
        # Activate Whole Body Balancer
        isEnabled  = True
        motionProxy.wbEnable(isEnabled)
    
        # Legs are constrained fixed
        stateName  = "Fixed"
        supportLeg = "Legs"
        motionProxy.wbFootState(stateName, supportLeg)
    
        # Constraint Balance Motion
        isEnable   = True
        supportLeg = "Legs"
        motionProxy.wbEnableBalanceConstraint(isEnable, supportLeg)
    
        # Com go to LLeg
        supportLeg = "LLeg"
        duration   = 2.0
        motionProxy.wbGoToBalance(supportLeg, duration)
    
        # RLeg is free
        stateName  = "Free"
        supportLeg = "RLeg"
        motionProxy.wbFootState(stateName, supportLeg)
    
        # RLeg is optimized
        effector = "RLeg"
        axisMask = 63
        frame    = motion.FRAME_WORLD
    
        # Motion of the RLeg
        times   = [2.0, 2.7, 4.5]
    
        path = Kick.computePath(self, motionProxy, effector, frame)
    
        motionProxy.transformInterpolations(effector, frame, path, axisMask, times)
    
        # Example showing how to Enable Effector Control as an Optimization
        isActive     = False
        motionProxy.wbEnableEffectorOptimization(effector, isActive)
    
        # Com go to LLeg
        supportLeg = "RLeg"
        duration   = 2.0
        motionProxy.wbGoToBalance(supportLeg, duration)
    
        # RLeg is free
        stateName  = "Free"
        supportLeg = "LLeg"
        motionProxy.wbFootState(stateName, supportLeg)
    
        effector = "LLeg"
        path = Kick.computePath(self, motionProxy, effector, frame)
        motionProxy.transformInterpolations(effector, frame, path, axisMask, times)
    
        time.sleep(1.0)
    
        # Deactivate Head tracking
        isEnabled = False
        motionProxy.wbEnable(isEnabled)
    
        # send robot to Pose Init
        postureProxy.goToPosture("StandInit", 0.3)
    
        # Go to rest position
        motionProxy.rest()
