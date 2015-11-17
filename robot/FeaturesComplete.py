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



class Features:

    def __init__(self, name):
        self.name = name
    
    def runOnRobot(self, Nao, forward, backward, right, left):
        self.run(Nao.NaoIP, forward, backward, right, left)
        
              
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
    
class TakePicture(Features):
    
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
        
"Testing Features"
#k = Kick()
#nao = Nao("193.48.125.62",9559)
#k.runOnRobot(nao)
