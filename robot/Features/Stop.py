# -*- coding: utf-8 -*-from NaoApplication import *from naoqi import ALProxyclass Stop(Features):    def __init__(self):        self.name = "Stop"    def run(self, robotIP, feature):               # Instanciation proxy pour la posture initiale         try:            postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)        except Exception, e:            print "Could not create proxy to ALRobotPosture"            print "Error was: ", e                   # Instanciation proxy pour les mouvements des bras lors de la marche        try:            motionProxy = ALProxy("ALMotion", robotIP, 9559)        except Exception, e:            print "Could not create proxy to ALMotion"            print "Error was: ", e                   # Arret des mouvements et mise en position initiale                  motionProxy.stopMove()        postureProxy.goToPosture("StandInit", 0.5)        