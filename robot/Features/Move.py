# -*- coding: utf-8 -*-from NaoApplication import *from Features import *from naoqi import ALProxyclass Move(Features):    def __init__(self, robotProxy):        self.name = "Move"        self.bot = robotProxy    def run(self, robotIP, feature):        # Instanciation proxy pour les mouvements des bras lors de la marche        motionProxy = self.bot.gMotionProxy                  # Instanciation proxy pour les deplacements         try:            navigationProxy = ALProxy("ALNavigation", robotIP, 9559)        except Exception, e:            print "Could not create proxy to ALRobotNavigation"            print "Error was: ", e                    # Instanciation proxy pour la posture initiale           postureProxy = self.bot.gPostureProxy        # Mise en position intiale de NAO        postureProxy.goToPosture("StandInit", 0.5)               # Activation mouvement automatique des bras lors de la marche        motionProxy.setMoveArmsEnabled(True, True)        # Activation des detections des obstacles        motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])               if feature["stop"]:            motionProxy.stopMove()                    elif feature["forward"][0]!=0.0 or feature["forward"][1]!=0.0 :               x     = feature["forward"][0]/100.0            #y     = feature["forward"][1]/100            print("demande de mouvements")            y=0            theta = 0.0            frequency = 1.0            print(x)            motionProxy.moveToward(x, y, theta, [["Frequency", frequency]])                  elif feature["rotation"] != 0 :             navigationProxy.moveTo(0.0, 0.0, feature["rotation"])             motionProxy.waitUntilMoveIsFinished()                             